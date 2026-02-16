## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1924.11.0.0.0
-  __TEXT.__text: 0x194d5c
-  __TEXT.__auth_stubs: 0x14c0
-  __TEXT.__objc_methlist: 0x1161c
-  __TEXT.__cstring: 0x1586b
+1933.8.0.0.0
+  __TEXT.__text: 0x19e87c
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_methlist: 0x1162c
+  __TEXT.__cstring: 0x15af0
   __TEXT.__const: 0x5b8
-  __TEXT.__oslogstring: 0x18a5b
-  __TEXT.__gcc_except_tab: 0x7fd4
+  __TEXT.__oslogstring: 0x18a8c
+  __TEXT.__gcc_except_tab: 0x7968
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x53b0
+  __TEXT.__unwind_info: 0x5670
   __TEXT.__objc_classname: 0x2c27
-  __TEXT.__objc_methname: 0x25ac7
-  __TEXT.__objc_methtype: 0x61e3
+  __TEXT.__objc_methname: 0x25af1
+  __TEXT.__objc_methtype: 0x61e6
   __TEXT.__objc_stubs: 0x17080
   __DATA_CONST.__got: 0x1198
   __DATA_CONST.__const: 0x3c08

   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ff0
+  __DATA_CONST.__objc_selrefs: 0x7ff8
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x6e8
-  __AUTH_CONST.__auth_got: 0xa70
-  __AUTH_CONST.__const: 0x1ac0
+  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH_CONST.__const: 0x1ae0
   __AUTH_CONST.__cfstring: 0x12cc0
   __AUTH_CONST.__objc_const: 0x22d70
   __AUTH_CONST.__objc_intobj: 0x2298

   __AUTH.__objc_data: 0x4ab0
   __DATA.__objc_ivar: 0x1774
   __DATA.__data: 0x19d8
-  __DATA.__bss: 0xbf0
+  __DATA.__bss: 0xc00
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x2ee0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 80AE5792-E99B-3953-9C24-64E43B86DAD7
-  Functions: 8624
-  Symbols:   27428
-  CStrings:  14191
+  UUID: 7DA44A30-0FF1-3CE4-9269-2B74CE089E4E
+  Functions: 8802
+  Symbols:   28147
+  CStrings:  14194
 
Symbols:
+ +[_CDLogging contactCatalogChannel]
+ +[_CDLogging contactCatalogChannel].cold.1
+ -[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:]
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.518
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.569
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.577
+ ___123-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:]_block_invoke
+ ___123-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:]_block_invoke_2
+ ___123-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:]_block_invoke_3
+ ___123-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:]_block_invoke_4
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.978
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.978.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.983
+ ___35+[_CDLogging contactCatalogChannel]_block_invoke
+ ___35+[_CDLogging contactCatalogChannel]_block_invoke.cold.1
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.644
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.648
+ ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.706
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1044
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1044.cold.1
+ ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.652
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.1
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.2
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.3
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.4
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.5
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.808
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.811
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.1
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.2
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.3
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.4
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.5
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.6
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.590
+ ___65-[_CDComplications admissionCheckOnComplication:forRemote:error:]_block_invoke.20
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.664
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.664.cold.1
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.713
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.724
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.526
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.526.cold.1
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.792
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.794
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.795
+ ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.789
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.783
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.786
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.788
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.654
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.654.cold.1
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.605
+ ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.628
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.668
+ ___block_descriptor_73_e8_32s40s48s56s64r_e38_"_CDContactRecord"16?0"_CDContact"8ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80r88r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8r88l8s64l8s72l8
+ ___block_literal_global.1015
+ ___block_literal_global.130
+ ___block_literal_global.524
+ ___block_literal_global.542
+ ___block_literal_global.555
+ ___block_literal_global.57
+ ___block_literal_global.575
+ ___block_literal_global.576
+ ___block_literal_global.590
+ ___block_literal_global.61
+ ___block_literal_global.611
+ ___block_literal_global.625
+ ___block_literal_global.635
+ ___block_literal_global.641
+ ___block_literal_global.647
+ ___block_literal_global.651
+ ___block_literal_global.654
+ ___block_literal_global.671
+ ___block_literal_global.674
+ ___block_literal_global.691
+ ___block_literal_global.693
+ ___block_literal_global.694
+ ___block_literal_global.695
+ ___block_literal_global.699
+ ___block_literal_global.705
+ ___block_literal_global.724
+ ___block_literal_global.754
+ ___block_literal_global.766
+ ___block_literal_global.797
+ ___block_literal_global.846
+ ___block_literal_global.878
+ ___block_literal_global.955
+ ___block_literal_global.959
+ ___block_literal_global.962
+ _contactCatalogChannel.contactCatalogChannel
+ _contactCatalogChannel.onceToken
+ _objc_msgSend$createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:
- -[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]
- ___103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke
- ___103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke_2
- ___103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke_3
- ___103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke_4
- ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.509
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.560
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.568
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.969
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.969.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.974
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.635
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.639
- ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.697
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1035
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1035.cold.1
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.643
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.1
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.2
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.3
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.4
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.758.cold.5
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.799
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.802
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.1
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.2
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.3
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.4
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.5
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.733.cold.6
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.581
- ___65-[_CDComplications admissionCheckOnComplication:forRemote:error:]_block_invoke.17
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.655
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.655.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.704
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.715
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517.cold.1
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.783
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.785
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.786
- ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.780
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.774
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.777
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.779
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.645
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.645.cold.1
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.596
- ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.619
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.659
- ___block_descriptor_72_e8_32s40s48s56s64r_e38_"_CDContactRecord"16?0"_CDContact"8ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80r88r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8r88l8s64l8s72l8
- ___block_literal_global.1006
- ___block_literal_global.126
- ___block_literal_global.515
- ___block_literal_global.533
- ___block_literal_global.546
- ___block_literal_global.557
- ___block_literal_global.563
- ___block_literal_global.567
- ___block_literal_global.602
- ___block_literal_global.616
- ___block_literal_global.626
- ___block_literal_global.632
- ___block_literal_global.638
- ___block_literal_global.642
- ___block_literal_global.645
- ___block_literal_global.662
- ___block_literal_global.665
- ___block_literal_global.672
- ___block_literal_global.677
- ___block_literal_global.682
- ___block_literal_global.684
- ___block_literal_global.685
- ___block_literal_global.696
- ___block_literal_global.715
- ___block_literal_global.745
- ___block_literal_global.757
- ___block_literal_global.779
- ___block_literal_global.837
- ___block_literal_global.869
- ___block_literal_global.946
- ___block_literal_global.950
- ___block_literal_global.953
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:552"
+ "@68@0:8@16@24@32@40@48B56^@60"
+ "Couldn't create os_log_t contactCatalogChannel"
+ "batchFetchExistingKeywordRecords finished executeFetchRequest, fetchLimit %lu object(s), elapsed %f(sec), returned %lu object(s), Predicate: %{sensitive}@"
+ "contactCatalog"
+ "contactCatalogChannel"
+ "createInteractionRecord:context:keywordCache:attachmentCache:contactCache:recordAlreadyExists:error:"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:552"
- "@64@0:8@16@24@32@40@48^@56"
- "batchFetchExistingKeywordRecords finished executeFetchRequest, fetchLimit %lu object(s), elapsed %f(sec), returned %lu object(s), Predicate: %{private}@"
- "createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:"

```
