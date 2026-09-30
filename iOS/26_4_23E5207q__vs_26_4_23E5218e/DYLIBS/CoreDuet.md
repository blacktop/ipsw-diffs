## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1933.8.0.0.0
-  __TEXT.__text: 0x19e87c
+1933.10.0.0.0
+  __TEXT.__text: 0x19edc8
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0x1162c
-  __TEXT.__cstring: 0x15af0
+  __TEXT.__objc_methlist: 0x1166c
+  __TEXT.__cstring: 0x15b34
   __TEXT.__const: 0x5b8
   __TEXT.__oslogstring: 0x18a8c
   __TEXT.__gcc_except_tab: 0x7968
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x5670
+  __TEXT.__unwind_info: 0x5680
   __TEXT.__objc_classname: 0x2c27
-  __TEXT.__objc_methname: 0x25af1
-  __TEXT.__objc_methtype: 0x61e6
-  __TEXT.__objc_stubs: 0x17080
+  __TEXT.__objc_methname: 0x25c2d
+  __TEXT.__objc_methtype: 0x620a
+  __TEXT.__objc_stubs: 0x17120
   __DATA_CONST.__got: 0x1198
-  __DATA_CONST.__const: 0x3c08
+  __DATA_CONST.__const: 0x3c30
   __DATA_CONST.__objc_classlist: 0xc28
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ff8
+  __DATA_CONST.__objc_selrefs: 0x8020
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x6e8
   __AUTH_CONST.__auth_got: 0xa40
   __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0x12cc0
-  __AUTH_CONST.__objc_const: 0x22d70
+  __AUTH_CONST.__cfstring: 0x12d40
+  __AUTH_CONST.__objc_const: 0x22df0
   __AUTH_CONST.__objc_intobj: 0x2298
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x4ab0
-  __DATA.__objc_ivar: 0x1774
+  __DATA.__objc_ivar: 0x177c
   __DATA.__data: 0x19d8
   __DATA.__bss: 0xc00
   __DATA.__common: 0x38

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7DA44A30-0FF1-3CE4-9269-2B74CE089E4E
-  Functions: 8802
-  Symbols:   28147
-  CStrings:  14194
+  UUID: 3BECE57A-152D-3A52-BC43-8FD18A9A94E7
+  Functions: 8808
+  Symbols:   28167
+  CStrings:  14213
 
Symbols:
+ -[_CDAttachment contentKeywords]
+ -[_CDAttachment contentTitle]
+ -[_CDAttachment initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:contentTitle:contentKeywords:]
+ -[_CDAttachment setContentKeywords:]
+ -[_CDAttachment setContentTitle:]
+ -[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:]
+ GCC_except_table110
+ _OBJC_IVAR_$__CDAttachment._contentKeywords
+ _OBJC_IVAR_$__CDAttachment._contentTitle
+ ___100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.219
+ ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.557
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.608
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.616
+ ___132-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:]_block_invoke
+ ___132-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:]_block_invoke.287
+ ___132-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:]_block_invoke_2
+ ___132-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:]_block_invoke_3
+ ___132-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:]_block_invoke_3.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1017
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1017.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1022
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.683
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.687
+ ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.745
+ ___41-[_CDInteractionStore metadataDictionary]_block_invoke.303
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1083
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1083.cold.1
+ ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.691
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.139
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.172
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.806
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.806.cold.1
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.806.cold.2
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.806.cold.3
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.806.cold.4
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.806.cold.5
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.847
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.850
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781.cold.1
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781.cold.2
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781.cold.3
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781.cold.4
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781.cold.5
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.781.cold.6
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.629
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.703
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.703.cold.1
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.752
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.763
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.565
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.565.cold.1
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.831
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.833
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.834
+ ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.828
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.822
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.825
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.827
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.693
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.693.cold.1
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.644
+ ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.667
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.707
+ ___block_descriptor_40_e8_32bs_e5_C8?0ls32l8
+ ___block_literal_global.1001
+ ___block_literal_global.1054
+ ___block_literal_global.203
+ ___block_literal_global.264
+ ___block_literal_global.306
+ ___block_literal_global.312
+ ___block_literal_global.352
+ ___block_literal_global.563
+ ___block_literal_global.594
+ ___block_literal_global.605
+ ___block_literal_global.614
+ ___block_literal_global.615
+ ___block_literal_global.620
+ ___block_literal_global.629
+ ___block_literal_global.650
+ ___block_literal_global.664
+ ___block_literal_global.680
+ ___block_literal_global.710
+ ___block_literal_global.713
+ ___block_literal_global.720
+ ___block_literal_global.725
+ ___block_literal_global.729
+ ___block_literal_global.730
+ ___block_literal_global.732
+ ___block_literal_global.733
+ ___block_literal_global.734
+ ___block_literal_global.738
+ ___block_literal_global.744
+ ___block_literal_global.763
+ ___block_literal_global.793
+ ___block_literal_global.805
+ ___block_literal_global.827
+ ___block_literal_global.836
+ ___block_literal_global.885
+ ___block_literal_global.917
+ ___block_literal_global.994
+ ___block_literal_global.998
+ _objc_msgSend$contentKeywords
+ _objc_msgSend$contentTitle
+ _objc_msgSend$initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:contentTitle:contentKeywords:
+ _objc_msgSend$iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:
+ _objc_msgSend$setContentKeywords:
+ _objc_msgSend$setContentTitle:
- -[_CDAttachment initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:]
- GCC_except_table103
- ___100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.211
- ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.518
- ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke
- ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke_2
- ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke_3
- ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke_3.cold.1
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.569
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.577
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.978
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.978.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.983
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.644
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.648
- ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.706
- ___41-[_CDInteractionStore metadataDictionary]_block_invoke.294
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1044
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1044.cold.1
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.652
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.131
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.164
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.1
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.2
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.3
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.4
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.767.cold.5
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.808
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.811
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.1
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.2
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.3
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.4
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.5
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.742.cold.6
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.590
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.664
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.664.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.713
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.724
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.526
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.526.cold.1
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.792
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.794
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.795
- ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.789
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.783
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.786
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.788
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.654
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.654.cold.1
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.605
- ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.628
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.668
- ___block_literal_global.1015
- ___block_literal_global.195
- ___block_literal_global.256
- ___block_literal_global.297
- ___block_literal_global.303
- ___block_literal_global.343
- ___block_literal_global.524
- ___block_literal_global.542
- ___block_literal_global.555
- ___block_literal_global.566
- ___block_literal_global.572
- ___block_literal_global.575
- ___block_literal_global.576
- ___block_literal_global.590
- ___block_literal_global.625
- ___block_literal_global.635
- ___block_literal_global.641
- ___block_literal_global.647
- ___block_literal_global.651
- ___block_literal_global.654
- ___block_literal_global.671
- ___block_literal_global.681
- ___block_literal_global.691
- ___block_literal_global.694
- ___block_literal_global.695
- ___block_literal_global.699
- ___block_literal_global.705
- ___block_literal_global.724
- ___block_literal_global.754
- ___block_literal_global.766
- ___block_literal_global.788
- ___block_literal_global.797
- ___block_literal_global.846
- ___block_literal_global.878
- ___block_literal_global.955
- ___block_literal_global.959
- ___block_literal_global.962
- _objc_msgSend$initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:
CStrings:
+ "\f"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:552"
+ "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
+ "T@\"NSArray\",&,D,N"
+ "T@\"NSArray\",&,V_contentKeywords"
+ "T@\"NSString\",&,V_contentTitle"
+ "_contentKeywords"
+ "_contentTitle"
+ "contentKeywords"
+ "contentKeywords: %@ "
+ "contentTitle"
+ "contentTitle: %@ "
+ "initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:contentTitle:contentKeywords:"
+ "iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:"
+ "setContentKeywords:"
+ "setContentTitle:"
+ "v56@0:8@16Q24B32B36@?40@?48"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:552"
- "@96@0:8@16@24@32@40@48@56@64@72@80@88"
- "initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:"

```
