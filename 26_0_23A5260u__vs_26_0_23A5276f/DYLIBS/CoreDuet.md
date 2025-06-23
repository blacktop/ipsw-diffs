## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1917.0.1.0.0
-  __TEXT.__text: 0x19be50
+1919.0.0.0.0
+  __TEXT.__text: 0x19c01c
   __TEXT.__auth_stubs: 0x14e0
   __TEXT.__objc_methlist: 0x11a4c
   __TEXT.__cstring: 0x161a9
   __TEXT.__const: 0x5a8
-  __TEXT.__oslogstring: 0x18869
-  __TEXT.__gcc_except_tab: 0x8000
+  __TEXT.__oslogstring: 0x188fa
+  __TEXT.__gcc_except_tab: 0x7fdc
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x54e8
+  __TEXT.__unwind_info: 0x54d8
   __TEXT.__objc_classname: 0x2c66
-  __TEXT.__objc_methname: 0x268e8
+  __TEXT.__objc_methname: 0x2691b
   __TEXT.__objc_methtype: 0x61e7
-  __TEXT.__objc_stubs: 0x176a0
+  __TEXT.__objc_stubs: 0x176c0
   __DATA_CONST.__got: 0x11a0
-  __DATA_CONST.__const: 0x3da0
+  __DATA_CONST.__const: 0x3dc8
   __DATA_CONST.__objc_classlist: 0xc38
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8258
+  __DATA_CONST.__objc_selrefs: 0x8260
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x6a8
   __DATA_CONST.__objc_arraydata: 0x7e8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A116C5EF-3E4B-3603-AA66-89D3477DAA28
-  Functions: 8808
+  UUID: 76EF640B-BA43-3B30-AF38-912132363D61
+  Functions: 8807
   Symbols:   27951
-  CStrings:  14445
+  CStrings:  14448
 
Symbols:
+ -[_CDContactFavoritesUtilities accessEntriesForContact:withBlock:]
+ -[_CDContactFavoritesUtilities accessFavoriteContactEntriesWithBlock:]
+ ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.509
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.728
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.736
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1137
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1137.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1142
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.635
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.639
+ ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.697
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1203
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1203.cold.1
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
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.749
+ ___66-[_CDContactFavoritesUtilities accessEntriesForContact:withBlock:]_block_invoke
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.823
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.823.cold.1
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.704
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.715
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517.cold.1
+ ___70-[_CDContactFavoritesUtilities accessFavoriteContactEntriesWithBlock:]_block_invoke
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.785
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.786
+ ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.780
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.777
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.779
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.813
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.813.cold.1
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.596
+ ___87-[_CDCloudFamilyDataCollectionTask callFeaturesFromInteractions:avgCallLength:contact:]_block_invoke
+ ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.787
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.827
+ ___block_descriptor_40_e8_32bs_e21_v16?0"CNFavorites"8ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e21_v16?0"CNFavorites"8ls40l8s32l8
+ ___block_literal_global.1174
+ ___block_literal_global.515
+ ___block_literal_global.533
+ ___block_literal_global.546
+ ___block_literal_global.557
+ ___block_literal_global.566
+ ___block_literal_global.581
+ ___block_literal_global.602
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
+ ___block_literal_global.735
+ ___block_literal_global.740
+ ___block_literal_global.745
+ ___block_literal_global.757
+ ___block_literal_global.779
+ ___block_literal_global.784
+ ___block_literal_global.794
+ ___block_literal_global.837
+ ___block_literal_global.869
+ ___block_literal_global.946
+ ___block_literal_global.953
+ _objc_msgSend$accessEntriesForContact:withBlock:
- -[_CDContactFavoritesUtilities entriesForContact:]
- -[_CDContactFavoritesUtilities favoriteContactEntries]
- ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.506
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.725
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.733
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1134
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1134.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1139
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.632
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.636
- ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.694
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1200
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1200.cold.1
- ___50-[_CDContactFavoritesUtilities entriesForContact:]_block_invoke
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.640
- ___54-[_CDContactFavoritesUtilities favoriteContactEntries]_block_invoke
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
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.746
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.817
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.817.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.701
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.712
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.514
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.514.cold.1
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.780
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.782
- ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.777
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.771
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.776
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.807
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.807.cold.1
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.593
- ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.781
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.821
- ___block_descriptor_40_e8_32r_e21_v16?0"CNFavorites"8lr32l8
- ___block_descriptor_48_e8_32s40r_e21_v16?0"CNFavorites"8lr40l8s32l8
- ___block_literal_global.1171
- ___block_literal_global.512
- ___block_literal_global.530
- ___block_literal_global.543
- ___block_literal_global.554
- ___block_literal_global.560
- ___block_literal_global.578
- ___block_literal_global.599
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
- ___block_literal_global.732
- ___block_literal_global.737
- ___block_literal_global.742
- ___block_literal_global.754
- ___block_literal_global.776
- ___block_literal_global.781
- ___block_literal_global.785
- ___block_literal_global.834
- ___block_literal_global.866
- ___block_literal_global.943
- ___block_literal_global.947
CStrings:
+ "SpotlightRecorder INStartCallIntent received with no contacts"
+ "SpotlightRecorder unable to unarchive serialized interaction for INStartCallIntent"
+ "accessEntriesForContact:withBlock:"
+ "accessFavoriteContactEntriesWithBlock:"
- "favoriteContactEntries"

```
