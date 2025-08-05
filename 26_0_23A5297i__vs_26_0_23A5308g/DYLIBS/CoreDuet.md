## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1922.0.2.0.0
+1924.0.0.0.0
   __TEXT.__text: 0x194040
   __TEXT.__auth_stubs: 0x14c0
   __TEXT.__objc_methlist: 0x11604

   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x4b00
+  __AUTH.__objc_data: 0x4ab0
   __DATA.__objc_ivar: 0x1774
   __DATA.__data: 0x19d8
   __DATA.__bss: 0xbf0
   __DATA.__common: 0x38
-  __DATA_DIRTY.__objc_data: 0x2e90
+  __DATA_DIRTY.__objc_data: 0x2ee0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x390
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D794A6C-3C6F-3E02-AA78-2812EAB57AAE
+  UUID: 2499E61B-445C-3F14-B976-76888BEAF40F
   Functions: 8619
   Symbols:   27411
   CStrings:  14159
Symbols:
+ ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.509
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.560
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.568
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.969
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.969.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.974
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.635
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.639
+ ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.697
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1035
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1035.cold.1
+ ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.643
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.1
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.2
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.3
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.4
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.5
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.799
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.802
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.1
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.2
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.3
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.4
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.5
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.6
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.581
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.655
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.655.cold.1
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.704
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.715
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517.cold.1
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.785
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.786
+ ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.780
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.777
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.779
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.645
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.645.cold.1
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.596
+ ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.619
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.659
+ ___block_literal_global.1006
+ ___block_literal_global.515
+ ___block_literal_global.533
+ ___block_literal_global.546
+ ___block_literal_global.557
+ ___block_literal_global.566
+ ___block_literal_global.567
+ ___block_literal_global.572
+ ___block_literal_global.581
+ ___block_literal_global.602
+ ___block_literal_global.616
+ ___block_literal_global.626
+ ___block_literal_global.632
+ ___block_literal_global.638
+ ___block_literal_global.645
+ ___block_literal_global.665
+ ___block_literal_global.672
+ ___block_literal_global.677
+ ___block_literal_global.684
+ ___block_literal_global.685
+ ___block_literal_global.686
+ ___block_literal_global.690
+ ___block_literal_global.696
+ ___block_literal_global.715
+ ___block_literal_global.745
+ ___block_literal_global.757
+ ___block_literal_global.779
+ ___block_literal_global.788
+ ___block_literal_global.837
+ ___block_literal_global.869
+ ___block_literal_global.946
+ ___block_literal_global.953
- ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.506
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.557
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.565
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.966
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.966.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.971
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.632
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.636
- ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.694
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1032
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1032.cold.1
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.640
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.1
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.2
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.3
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.4
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.5
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.796
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.799
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.1
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.2
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.3
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.4
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.5
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.6
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.578
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.652
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.652.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.701
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.712
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.514
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.514.cold.1
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.780
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.782
- ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.777
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.771
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.776
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.642
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.642.cold.1
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.593
- ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.616
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.656
- ___block_literal_global.1003
- ___block_literal_global.512
- ___block_literal_global.530
- ___block_literal_global.543
- ___block_literal_global.554
- ___block_literal_global.560
- ___block_literal_global.564
- ___block_literal_global.569
- ___block_literal_global.578
- ___block_literal_global.599
- ___block_literal_global.613
- ___block_literal_global.623
- ___block_literal_global.629
- ___block_literal_global.635
- ___block_literal_global.639
- ___block_literal_global.659
- ___block_literal_global.669
- ___block_literal_global.674
- ___block_literal_global.678
- ___block_literal_global.679
- ___block_literal_global.683
- ___block_literal_global.687
- ___block_literal_global.693
- ___block_literal_global.712
- ___block_literal_global.742
- ___block_literal_global.754
- ___block_literal_global.776
- ___block_literal_global.785
- ___block_literal_global.834
- ___block_literal_global.866
- ___block_literal_global.943
- ___block_literal_global.947

```
