## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1919.0.0.0.0
-  __TEXT.__text: 0x19c01c
-  __TEXT.__auth_stubs: 0x14e0
-  __TEXT.__objc_methlist: 0x11a4c
-  __TEXT.__cstring: 0x161a9
+1922.0.2.0.0
+  __TEXT.__text: 0x194040
+  __TEXT.__auth_stubs: 0x14c0
+  __TEXT.__objc_methlist: 0x11604
+  __TEXT.__cstring: 0x157c9
   __TEXT.__const: 0x5a8
-  __TEXT.__oslogstring: 0x188fa
-  __TEXT.__gcc_except_tab: 0x7fdc
+  __TEXT.__oslogstring: 0x186b2
+  __TEXT.__gcc_except_tab: 0x7f70
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x54d8
-  __TEXT.__objc_classname: 0x2c66
-  __TEXT.__objc_methname: 0x2691b
-  __TEXT.__objc_methtype: 0x61e7
-  __TEXT.__objc_stubs: 0x176c0
-  __DATA_CONST.__got: 0x11a0
-  __DATA_CONST.__const: 0x3dc8
-  __DATA_CONST.__objc_classlist: 0xc38
+  __TEXT.__unwind_info: 0x5398
+  __TEXT.__objc_classname: 0x2c27
+  __TEXT.__objc_methname: 0x259a7
+  __TEXT.__objc_methtype: 0x617e
+  __TEXT.__objc_stubs: 0x17020
+  __DATA_CONST.__got: 0x1190
+  __DATA_CONST.__const: 0x3c08
+  __DATA_CONST.__objc_classlist: 0xc28
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8260
+  __DATA_CONST.__objc_selrefs: 0x7fc8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x6a8
-  __DATA_CONST.__objc_arraydata: 0x7e8
-  __AUTH_CONST.__auth_got: 0xa80
-  __AUTH_CONST.__const: 0x1f20
-  __AUTH_CONST.__cfstring: 0x13480
-  __AUTH_CONST.__objc_const: 0x23368
-  __AUTH_CONST.__objc_intobj: 0x2400
+  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_arraydata: 0x6e8
+  __AUTH_CONST.__auth_got: 0xa70
+  __AUTH_CONST.__const: 0x1ac0
+  __AUTH_CONST.__cfstring: 0x12be0
+  __AUTH_CONST.__objc_const: 0x22d68
+  __AUTH_CONST.__objc_intobj: 0x2298
   __AUTH_CONST.__objc_doubleobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x6d8
+  __AUTH_CONST.__objc_arrayobj: 0x618
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x4ba0
-  __DATA.__objc_ivar: 0x17e8
-  __DATA.__data: 0x19e0
-  __DATA.__bss: 0xc10
+  __AUTH.__objc_data: 0x4b00
+  __DATA.__objc_ivar: 0x1774
+  __DATA.__data: 0x19d8
+  __DATA.__bss: 0xbf0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x2e90
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 51087382-48C0-3DB4-A8F0-031DBDA2D1AA
-  Functions: 8807
-  Symbols:   27951
-  CStrings:  14448
+  UUID: 2D794A6C-3C6F-3E02-AA78-2812EAB57AAE
+  Functions: 8619
+  Symbols:   27411
+  CStrings:  14159
 
Symbols:
+ -[_CDInteractionRecord conversationId]
+ -[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]
+ GCC_except_table103
+ GCC_except_table106
+ __OBJC_$_INSTANCE_METHODS__CDInteractionRecord
+ ___100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.211
+ ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.506
+ ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke
+ ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke_2
+ ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke_3
+ ___110-[_CDInteractionStore iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:]_block_invoke_3.cold.1
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.557
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.565
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.966
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.966.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.971
+ ___31-[_CDInteractionCache _refetch]_block_invoke.92
+ ___31-[_CDInteractionCache _refetch]_block_invoke.92.cold.1
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.632
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.636
+ ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.694
+ ___41-[_CDInteractionStore metadataDictionary]_block_invoke.294
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1032
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1032.cold.1
+ ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.640
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.131
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.164
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.1
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.2
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.3
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.4
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.755.cold.5
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.796
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.799
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.1
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.2
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.3
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.4
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.5
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.730.cold.6
+ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.26
+ ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.29
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.578
+ ___66-[_CDSocialInteractionAdvisor tuneUsingSettings:heartBeatHandler:]_block_invoke.41
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.652
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.652.cold.1
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.701
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.712
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.514
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.514.cold.1
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.780
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.782
+ ___75-[_CDSocialInteractionAdvisor rankContacts:withSeedContacts:usingSettings:]_block_invoke.27
+ ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.777
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.771
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.776
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.642
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.642.cold.1
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.593
+ ___87-[_CDSocialInteractionAdvisor adviseInteractionsForDate:andSeedContacts:usingSettings:]_block_invoke.36
+ ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.616
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.656
+ ___block_descriptor_73_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1003
+ ___block_literal_global.195
+ ___block_literal_global.256
+ ___block_literal_global.297
+ ___block_literal_global.303
+ ___block_literal_global.512
+ ___block_literal_global.530
+ ___block_literal_global.543
+ ___block_literal_global.554
+ ___block_literal_global.560
+ ___block_literal_global.564
+ ___block_literal_global.569
+ ___block_literal_global.578
+ ___block_literal_global.599
+ ___block_literal_global.613
+ ___block_literal_global.623
+ ___block_literal_global.629
+ ___block_literal_global.635
+ ___block_literal_global.639
+ ___block_literal_global.659
+ ___block_literal_global.669
+ ___block_literal_global.674
+ ___block_literal_global.678
+ ___block_literal_global.679
+ ___block_literal_global.683
+ ___block_literal_global.687
+ ___block_literal_global.693
+ ___block_literal_global.712
+ ___block_literal_global.742
+ ___block_literal_global.754
+ ___block_literal_global.776
+ ___block_literal_global.785
+ ___block_literal_global.834
+ ___block_literal_global.866
+ ___block_literal_global.90
+ ___block_literal_global.943
+ ___block_literal_global.947
- +[_CDInteractionsStatisticsConfig computationBlockForStatName:]
- +[_CDInteractionsStatisticsConfig computationBlockForStatName:].cold.1
- +[_CDInteractionsStatisticsConfig isDateInWeekend:]
- +[_CDInteractionsStatisticsConfig isDateInWeekend:].cold.1
- -[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]
- -[_CDInteractionStore getInteractionsStatisticsForConfig:]
- -[_CDInteractionsStatistics .cxx_destruct]
- -[_CDInteractionsStatistics _addConversationId:]
- -[_CDInteractionsStatistics aggregateSum:resultFeatureName:]
- -[_CDInteractionsStatistics bundleIdForConversationId:]
- -[_CDInteractionsStatistics computeCandidateLevelSignals]
- -[_CDInteractionsStatistics computeFeatureForMethod:arguments:]
- -[_CDInteractionsStatistics computeFeatureForMethod:arguments:].cold.1
- -[_CDInteractionsStatistics computeFeatureForMethod:arguments:].cold.2
- -[_CDInteractionsStatistics computeFeaturesForRecipe:]
- -[_CDInteractionsStatistics computeNumberOfAppsSharedFromWithConversation]
- -[_CDInteractionsStatistics computeNumberOfEngagedSuggestionsToTargetApp]
- -[_CDInteractionsStatistics computeNumberOfFacesSharedWithConversation]
- -[_CDInteractionsStatistics computeNumberOfSharesToTargetApp]
- -[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]
- -[_CDInteractionsStatistics computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:]
- -[_CDInteractionsStatistics conversationIds]
- -[_CDInteractionsStatistics copyFeature:toFeatureName:]
- -[_CDInteractionsStatistics descriptionRedacted:]
- -[_CDInteractionsStatistics description]
- -[_CDInteractionsStatistics divide:withDivisor:resultFeatureName:]
- -[_CDInteractionsStatistics exponential:withMultiplier:resultFeatureName:]
- -[_CDInteractionsStatistics features]
- -[_CDInteractionsStatistics hasEverSharePlayed:]
- -[_CDInteractionsStatistics imputeFeature:withConstant:]
- -[_CDInteractionsStatistics includeFeature:from:]
- -[_CDInteractionsStatistics incrementValueForFeature:andConversationId:]
- -[_CDInteractionsStatistics initFeature:withValue:]
- -[_CDInteractionsStatistics initWithDefaultValues:]
- -[_CDInteractionsStatistics initWithProperties:features:defaultValues:]
- -[_CDInteractionsStatistics isUsingDefaultValue:forConversationId:]
- -[_CDInteractionsStatistics laplaceProbability:withAlpha:resultFeatureName:]
- -[_CDInteractionsStatistics log:withBase:resultFeatureName:]
- -[_CDInteractionsStatistics multiply:with:resultFeatureName:]
- -[_CDInteractionsStatistics multiply:withMultiplier:resultFeatureName:]
- -[_CDInteractionsStatistics nonNilFeaturesForConversationId:]
- -[_CDInteractionsStatistics power:withExponent:resultFeatureName:]
- -[_CDInteractionsStatistics privatizedConversationId:]
- -[_CDInteractionsStatistics properties]
- -[_CDInteractionsStatistics queryStats]
- -[_CDInteractionsStatistics reciprocal:withOffset:resultFeatureName:]
- -[_CDInteractionsStatistics recordSharePlayInformation:]
- -[_CDInteractionsStatistics redactedDescription]
- -[_CDInteractionsStatistics removeConversationIds:]
- -[_CDInteractionsStatistics removeFeature:andConversation:]
- -[_CDInteractionsStatistics renameFeature:withFeatureName:]
- -[_CDInteractionsStatistics saveAppSharedFrom:forConversationId:]
- -[_CDInteractionsStatistics savePersonId:forConversationId:forSyntheticInteraction:]
- -[_CDInteractionsStatistics savePersonsInPhoto:forConversationId:]
- -[_CDInteractionsStatistics setQueryStats:]
- -[_CDInteractionsStatistics setValue:forFeature:andConversationId:]
- -[_CDInteractionsStatistics setValue:forProperty:andConversationId:]
- -[_CDInteractionsStatistics sum:with:resultFeatureName:]
- -[_CDInteractionsStatistics sum:withAddend:resultFeatureName:]
- -[_CDInteractionsStatistics valueForFeature:forConversationId:]
- -[_CDInteractionsStatistics valueForProperty:forConversationId:]
- -[_CDInteractionsStatistics valueOrDefaultValueForFeature:forConversationId:]
- -[_CDInteractionsStatisticsConfig .cxx_destruct]
- -[_CDInteractionsStatisticsConfig _shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:]
- -[_CDInteractionsStatisticsConfig _shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:]
- -[_CDInteractionsStatisticsConfig anchorDate]
- -[_CDInteractionsStatisticsConfig appBundleIdForAppExtBundleId:]
- -[_CDInteractionsStatisticsConfig appToAppExtMapping]
- -[_CDInteractionsStatisticsConfig bundleId]
- -[_CDInteractionsStatisticsConfig communicationInteractionPredicate]
- -[_CDInteractionsStatisticsConfig computeAppsSharedFromForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeConversationBundleIdForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeConversationGroupNameForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeConversationINImageURLForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeHasEverSharePlayedWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsFromCurrentAppWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsOfDetectedPeopleWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsOfPhotoFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsOfTopDomainURLWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfIncomingInteractionsWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfOutgoingInteractionsWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfRecentOutgoingInteractionsWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfSharesFromCurrentAppWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfSharesOfDetectedPeopleWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfSharesOfTopDomainURLWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeNumberOfSharesWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computePastSharedPeopleInPhotoForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computePhotoFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeRecipientListConversationIdForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeScenesBasedFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeStatsForInteractionRecord:inInteractionsStatistics:chunkIndex:]
- -[_CDInteractionsStatisticsConfig computeStatsForInteractionRecord:inInteractionsStatistics:chunkIndex:].cold.1
- -[_CDInteractionsStatisticsConfig computeTimeSinceLastIncomingInteractionForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeTimeSinceLastOutgoingInteractionForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeTimeSinceLastPhotoShareWithConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeTimeSinceLastShareWithConversation:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig computeTimeSinceLastUIEngagementForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig configuredSceneCategoryTagNames]
- -[_CDInteractionsStatisticsConfig defaultValues]
- -[_CDInteractionsStatisticsConfig detectedSceneCategoryNamesFromSceneNetTags:]
- -[_CDInteractionsStatisticsConfig featureNamesToSortWith]
- -[_CDInteractionsStatisticsConfig fetchBatchSize]
- -[_CDInteractionsStatisticsConfig fetchLimit]
- -[_CDInteractionsStatisticsConfig getConversationIdForRecord:]
- -[_CDInteractionsStatisticsConfig initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:]
- -[_CDInteractionsStatisticsConfig initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:]
- -[_CDInteractionsStatisticsConfig isFallbackFetch]
- -[_CDInteractionsStatisticsConfig leftBoundDate]
- -[_CDInteractionsStatisticsConfig maxComputationTime]
- -[_CDInteractionsStatisticsConfig peopleInPhotoIdentifiers]
- -[_CDInteractionsStatisticsConfig rightBoundDate]
- -[_CDInteractionsStatisticsConfig sceneTagsInPhotoIdentifiers]
- -[_CDInteractionsStatisticsConfig setAppToAppExtMapping:]
- -[_CDInteractionsStatisticsConfig setBundleId:]
- -[_CDInteractionsStatisticsConfig setFeatureNamesToSortWith:]
- -[_CDInteractionsStatisticsConfig setFetchBatchSize:]
- -[_CDInteractionsStatisticsConfig setFetchLimit:]
- -[_CDInteractionsStatisticsConfig setIsFallbackFetch:]
- -[_CDInteractionsStatisticsConfig setPeopleInPhotoIdentifiers:]
- -[_CDInteractionsStatisticsConfig setSceneTagsInPhotoIdentifiers:]
- -[_CDInteractionsStatisticsConfig setStatsToCompute:]
- -[_CDInteractionsStatisticsConfig setTopDomainURL:]
- -[_CDInteractionsStatisticsConfig sharingInteractionPredicate]
- -[_CDInteractionsStatisticsConfig shouldContinue]
- -[_CDInteractionsStatisticsConfig shouldUseSuggestionEngaged]
- -[_CDInteractionsStatisticsConfig statsToCompute]
- -[_CDInteractionsStatisticsConfig topDomainURL]
- _OBJC_CLASS_$__CDInteractionsStatistics
- _OBJC_CLASS_$__CDInteractionsStatisticsConfig
- _OBJC_IVAR_$__CDInteractionsStatistics._appsSharedFromByConversationId
- _OBJC_IVAR_$__CDInteractionsStatistics._defaultValues
- _OBJC_IVAR_$__CDInteractionsStatistics._features
- _OBJC_IVAR_$__CDInteractionsStatistics._hasSharePlayedWith
- _OBJC_IVAR_$__CDInteractionsStatistics._personsCountsForRealInteractions
- _OBJC_IVAR_$__CDInteractionsStatistics._personsCountsForSyntheticInteractions
- _OBJC_IVAR_$__CDInteractionsStatistics._personsSharedInPastPhotos
- _OBJC_IVAR_$__CDInteractionsStatistics._properties
- _OBJC_IVAR_$__CDInteractionsStatistics._queryStats
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._anchorDate
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._anchorTimeStamp
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._appToAppExtMapping
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._bundleId
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._defaultValues
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._featureNamesToSortWith
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._fetchBatchSize
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._fetchLimit
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._isFallbackFetch
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._isWeekEndShare
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._leftBoundDate
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._maxComputationTime
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._peopleInPhotoIdentifiers
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._rightBoundDate
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._sceneTagsInPhotoIdentifiers
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._scenesBasedFeatures
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._scenesMinimumNumberOfTags
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._shouldUseSuggestionEngaged
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._statsToCompute
- _OBJC_IVAR_$__CDInteractionsStatisticsConfig._topDomainURL
- _OBJC_METACLASS_$__CDInteractionsStatistics
- _OBJC_METACLASS_$__CDInteractionsStatisticsConfig
- __OBJC_$_INSTANCE_METHODS__CDInteractionsStatistics
- __OBJC_$_INSTANCE_METHODS__CDInteractionsStatisticsConfig
- __OBJC_$_INSTANCE_VARIABLES__CDInteractionsStatistics
- __OBJC_$_INSTANCE_VARIABLES__CDInteractionsStatisticsConfig
- __OBJC_$_PROP_LIST__CDInteractionsStatistics
- __OBJC_$_PROP_LIST__CDInteractionsStatisticsConfig
- __OBJC_CLASS_RO_$__CDInteractionsStatistics
- __OBJC_CLASS_RO_$__CDInteractionsStatisticsConfig
- __OBJC_METACLASS_RO_$__CDInteractionsStatistics
- __OBJC_METACLASS_RO_$__CDInteractionsStatisticsConfig
- ___100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.379
- ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.509
- ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke
- ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_2
- ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_3
- ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_3.cold.1
- ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_3.cold.2
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.728
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.736
- ___116-[_CDInteractionsStatisticsConfig computePhotoFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
- ___122-[_CDInteractionsStatisticsConfig computeScenesBasedFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
- ___126-[_CDInteractionsStatisticsConfig computePastSharedPeopleInPhotoForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
- ___144-[_CDInteractionsStatisticsConfig computeNumberOfEngagedSuggestionsOfPhotoFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1137
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1137.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.1142
- ___31-[_CDInteractionCache _refetch]_block_invoke.260
- ___31-[_CDInteractionCache _refetch]_block_invoke.260.cold.1
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.635
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.639
- ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.697
- ___41-[_CDInteractionStore metadataDictionary]_block_invoke.481
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1203
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.1203.cold.1
- ___49-[_CDInteractionsStatistics descriptionRedacted:]_block_invoke
- ___49-[_CDInteractionsStatistics descriptionRedacted:]_block_invoke_2
- ___49-[_CDInteractionsStatistics descriptionRedacted:]_block_invoke_3
- ___51+[_CDInteractionsStatisticsConfig isDateInWeekend:]_block_invoke
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.643
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.299
- ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.332
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
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.461
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke_2
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke_2.465
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_10
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_11
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_12
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_13
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_14
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_15
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_16
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_17
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_18
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_19
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_2
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_20
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_21
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_22
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_23
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_24
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_25
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_26
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_27
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_28
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_29
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_3
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_4
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_5
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_6
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_7
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_8
- ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_9
- ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.194
- ___64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.197
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.749
- ___66-[_CDSocialInteractionAdvisor tuneUsingSettings:heartBeatHandler:]_block_invoke.209
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.823
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.823.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.704
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.715
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.517.cold.1
- ___73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke
- ___73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke.cold.1
- ___73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke_2
- ___73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke_3
- ___74-[_CDInteractionsStatistics computeNumberOfAppsSharedFromWithConversation]_block_invoke
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.785
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.786
- ___75-[_CDSocialInteractionAdvisor rankContacts:withSeedContacts:usingSettings:]_block_invoke.195
- ___78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.780
- ___78-[_CDInteractionsStatisticsConfig detectedSceneCategoryNamesFromSceneNetTags:]_block_invoke
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.777
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.779
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.813
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.813.cold.1
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.596
- ___87-[_CDSocialInteractionAdvisor adviseInteractionsForDate:andSeedContacts:usingSettings:]_block_invoke.204
- ___90-[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:]_block_invoke.787
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.827
- ___block_descriptor_32_e109_v40?0"_CDInteractionsStatisticsConfig"8"NSString"16"_CDInteractionRecord"24"_CDInteractionsStatistics"32l
- ___block_descriptor_32_e29_16?0"_CDAttachmentRecord"8l
- ___block_descriptor_32_e39_"NSString"16?0"_CDAttachmentRecord"8l
- ___block_descriptor_32_e40_"NSString"16?0"_CDInteractionRecord"8l
- ___block_descriptor_40_e8_32s_e31_v24?0"NSString"8"NSString"16ls32l8
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSMutableSet"16^B24ls32l8
- ___block_descriptor_48_e8_32s40s_e28_"NSNumber"16?0"NSString"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e37_v28?0"_CDInteractionRecord"8i16^B20ls32l8s40l8
- ___block_descriptor_49_e8_32s40s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1174
- ___block_literal_global.182
- ___block_literal_global.192
- ___block_literal_global.206
- ___block_literal_global.219
- ___block_literal_global.258
- ___block_literal_global.262
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.278
- ___block_literal_global.280
- ___block_literal_global.282
- ___block_literal_global.284
- ___block_literal_global.286
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.316
- ___block_literal_global.320
- ___block_literal_global.322
- ___block_literal_global.334
- ___block_literal_global.337
- ___block_literal_global.339
- ___block_literal_global.341
- ___block_literal_global.363
- ___block_literal_global.424
- ___block_literal_global.484
- ___block_literal_global.490
- ___block_literal_global.505
- ___block_literal_global.515
- ___block_literal_global.533
- ___block_literal_global.546
- ___block_literal_global.557
- ___block_literal_global.566
- ___block_literal_global.581
- ___block_literal_global.602
- ___block_literal_global.632
- ___block_literal_global.638
- ___block_literal_global.645
- ___block_literal_global.665
- ___block_literal_global.672
- ___block_literal_global.677
- ___block_literal_global.684
- ___block_literal_global.685
- ___block_literal_global.686
- ___block_literal_global.690
- ___block_literal_global.696
- ___block_literal_global.715
- ___block_literal_global.735
- ___block_literal_global.740
- ___block_literal_global.745
- ___block_literal_global.757
- ___block_literal_global.779
- ___block_literal_global.784
- ___block_literal_global.788
- ___block_literal_global.794
- ___block_literal_global.837
- ___block_literal_global.869
- ___block_literal_global.946
- ___block_literal_global.953
- _arc4random
- _computationBlockForStatName:._pasOnceToken19
- _computationBlockForStatName:.statNameToComputationBlock
- _isDateInWeekend:._pasExprOnceResult
- _isDateInWeekend:._pasOnceToken18
- _log
- _objc_msgSend$_addConversationId:
- _objc_msgSend$_iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:
- _objc_msgSend$_pas_mappedSetWithTransform:
- _objc_msgSend$_shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:
- _objc_msgSend$_shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:
- _objc_msgSend$aggregateSum:resultFeatureName:
- _objc_msgSend$autoupdatingCurrentCalendar
- _objc_msgSend$bundleIdForConversationId:
- _objc_msgSend$communicationInteractionPredicate
- _objc_msgSend$computeFeatureForMethod:arguments:
- _objc_msgSend$computeNumberOfAppsSharedFromWithConversation
- _objc_msgSend$computeNumberOfEngagedSuggestionsToTargetApp
- _objc_msgSend$computeNumberOfFacesSharedWithConversation
- _objc_msgSend$computeNumberOfSharesToTargetApp
- _objc_msgSend$computeStatsForInteractionRecord:inInteractionsStatistics:chunkIndex:
- _objc_msgSend$conversationIds
- _objc_msgSend$copyFeature:toFeatureName:
- _objc_msgSend$defaultValues
- _objc_msgSend$divide:withDivisor:resultFeatureName:
- _objc_msgSend$exponential:withMultiplier:resultFeatureName:
- _objc_msgSend$fetchBatchSize
- _objc_msgSend$generateConversationIdFromInteractionRecipientRecords:
- _objc_msgSend$hasEverSharePlayed:
- _objc_msgSend$imputeFeature:withConstant:
- _objc_msgSend$incrementValueForFeature:andConversationId:
- _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:
- _objc_msgSend$initWithDefaultValues:
- _objc_msgSend$initWithProperties:features:defaultValues:
- _objc_msgSend$initWithTimeIntervalSinceReferenceDate:
- _objc_msgSend$laplaceProbability:withAlpha:resultFeatureName:
- _objc_msgSend$log:withBase:resultFeatureName:
- _objc_msgSend$maxComputationTime
- _objc_msgSend$multiply:with:resultFeatureName:
- _objc_msgSend$multiply:withMultiplier:resultFeatureName:
- _objc_msgSend$power:withExponent:resultFeatureName:
- _objc_msgSend$privatizedConversationId:
- _objc_msgSend$reciprocal:withOffset:resultFeatureName:
- _objc_msgSend$recordSharePlayInformation:
- _objc_msgSend$removeFeature:andConversation:
- _objc_msgSend$renameFeature:withFeatureName:
- _objc_msgSend$saveAppSharedFrom:forConversationId:
- _objc_msgSend$savePersonId:forConversationId:forSyntheticInteraction:
- _objc_msgSend$savePersonsInPhoto:forConversationId:
- _objc_msgSend$setQueryStats:
- _objc_msgSend$setValue:forFeature:andConversationId:
- _objc_msgSend$setValue:forProperty:andConversationId:
- _objc_msgSend$sharingInteractionPredicate
- _objc_msgSend$shouldContinue
- _objc_msgSend$sum:with:resultFeatureName:
- _objc_msgSend$sum:withAddend:resultFeatureName:
- _objc_msgSend$valueForFeature:forConversationId:
- _objc_msgSend$valueForProperty:forConversationId:
- _objc_msgSend$valueOrDefaultValueForFeature:forConversationId:
- _stringifyRecipientList
- _stringifyRecipientList_block_invoke
CStrings:
+ "conversationId"
+ "iterInteractionRecordsWithPredicate"
+ "iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:"
+ "saveFeedbackInCoreDuetd:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:reply:"
+ "v52@0:8@16Q24B32@?36@?44"
+ "v60@0:8@\"NSString\"16@\"NSString\"24q32@\"NSString\"40B48@?<v@?B>52"
+ "v60@0:8@16@24q32@40B48@?52"
- "\t\t%@: %@\n"
- "\t\t%@: %@ \n"
- "\tnumberOfFeatures: %tu \n"
- "\tnumberOfProperties: %tu \n"
- "%du"
- "(startDate >= %@) && (startDate <= %@)"
- "@\"NSNumber\"16@?0@\"NSString\"8"
- "@\"NSString\"16@?0@\"_CDAttachmentRecord\"8"
- "@\"NSString\"16@?0@\"_CDInteractionRecord\"8"
- "@16@?0@\"_CDAttachmentRecord\"8"
- "@76@0:8@16@24@32Q40d48@56B64@68"
- "@92@0:8@16@24@32Q40d48@56B64@68@76@84"
- "@max.self"
- "ConversationBundleId"
- "ConversationGroupName"
- "ConversationINImageURL"
- "NOT (bundleId IN %@)"
- "RecipientListConversationId"
- "T@\"NSArray\",&,N,V_featureNamesToSortWith"
- "T@\"NSArray\",&,N,V_statsToCompute"
- "T@\"NSDate\",R,N,V_anchorDate"
- "T@\"NSDate\",R,N,V_leftBoundDate"
- "T@\"NSDate\",R,N,V_rightBoundDate"
- "T@\"NSDictionary\",&,N,V_appToAppExtMapping"
- "T@\"NSDictionary\",C,N,V_queryStats"
- "T@\"NSDictionary\",R,N,V_defaultValues"
- "T@\"NSSet\",&,N,V_peopleInPhotoIdentifiers"
- "T@\"NSSet\",&,N,V_sceneTagsInPhotoIdentifiers"
- "T@\"NSString\",&,N,V_topDomainURL"
- "TB,N,V_isFallbackFetch"
- "TB,R,N,V_shouldUseSuggestionEngaged"
- "TQ,N,V_fetchLimit"
- "Td,R,N,V_maxComputationTime"
- "Ti,N,V_fetchBatchSize"
- "TimeSinceLastUIEngagement"
- "_CDInteractionsStatistics"
- "_CDInteractionsStatistics(\n"
- "_CDInteractionsStatistics: insufficient arguments passed to computeFeatureForMethod"
- "_CDInteractionsStatistics: union of shared people sets had cardinality zero"
- "_CDInteractionsStatistics: unknown methodName passed to computeFeatureForMethod"
- "_CDInteractionsStatisticsConfig"
- "_CDInteractionsStatisticsConfig: record returned nil conversationId"
- "_CDInteractionsStatisticsConfig: skipping %@ –\u00a0computation block was nil"
- "_addConversationId:"
- "_anchorDate"
- "_anchorTimeStamp"
- "_appToAppExtMapping"
- "_appsSharedFromByConversationId"
- "_defaultValues"
- "_featureNamesToSortWith"
- "_features"
- "_fetchBatchSize"
- "_fetchLimit"
- "_hasSharePlayedWith"
- "_isFallbackFetch"
- "_isWeekEndShare"
- "_iterInteractionRecordsWithPredicate"
- "_iterInteractionRecordsWithPredicate: query exception: %@"
- "_iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:"
- "_leftBoundDate"
- "_maxComputationTime"
- "_pas_mappedSetWithTransform:"
- "_peopleInPhotoIdentifiers"
- "_personsCountsForRealInteractions"
- "_personsCountsForSyntheticInteractions"
- "_personsSharedInPastPhotos"
- "_queryStats"
- "_rightBoundDate"
- "_sceneTagsInPhotoIdentifiers"
- "_scenesBasedFeatures"
- "_scenesMinimumNumberOfTags"
- "_shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:"
- "_shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:"
- "_shouldUseSuggestionEngaged"
- "_statsToCompute"
- "_topDomainURL"
- "aggregateSum:"
- "aggregateSum:resultFeatureName:"
- "anchorDate"
- "appToAppExtMapping"
- "autoupdatingCurrentCalendar"
- "bundleIdForConversationId:"
- "com.apple."
- "com.apple.iCal"
- "com.apple.telephonyutilities.callservicesd"
- "communicationInteractionPredicate"
- "communicationInteractions.%@"
- "computeCandidateLevelSignals"
- "computeFeatureForMethod:arguments:"
- "computeFeaturesForRecipe:"
- "computeNumberOfAppsSharedFromWithConversation"
- "computeNumberOfEngagedSuggestionsToTargetApp"
- "computeNumberOfFacesSharedWithConversation"
- "computeNumberOfSharesToTargetApp"
- "computePASSFeatureWithPeopleDetectedInPhoto:"
- "computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:"
- "computeStatsForInteractionRecord:inInteractionsStatistics:chunkIndex:"
- "configuredSceneCategoryTagNames"
- "conversationId: %@ \n"
- "conversationIds"
- "copy:to:"
- "copyFeature:toFeatureName:"
- "defaultValues"
- "detectedSceneCategoryNamesFromSceneNetTags:"
- "divide:withDivisor:"
- "divide:withDivisor:resultFeatureName:"
- "exponential:withMultiplier:"
- "exponential:withMultiplier:resultFeatureName:"
- "featureNamesToSortWith"
- "features"
- "fetchBatchSize"
- "foundInInteractionStoreChunk"
- "getInteractionsStatisticsForConfig:"
- "getInteractionsStatisticsForConfig: processing communication interactions"
- "getInteractionsStatisticsForConfig: processing sharing interactions"
- "hasEverSharePlayed:"
- "hasEverSharePlayedWithConversation"
- "impute:withConstant:"
- "imputeFeature:withConstant:"
- "includeFeature:from:"
- "incrementValueForFeature:andConversationId:"
- "initFeature:withValue:"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:"
- "initWithDefaultValues:"
- "initWithProperties:features:defaultValues:"
- "initWithTimeIntervalSinceReferenceDate:"
- "isFallbackFetch"
- "isFirstPartyApp"
- "isUsingDefaultValue:forConversationId:"
- "laplaceProbability:withAlpha:"
- "laplaceProbability:withAlpha:resultFeatureName:"
- "leftBoundDate"
- "log:withBase:"
- "log:withBase:resultFeatureName:"
- "maxComputationTime"
- "multiply:with:"
- "multiply:with:resultFeatureName:"
- "multiply:withMultiplier:"
- "multiply:withMultiplier:resultFeatureName:"
- "nonNilFeaturesForConversationId:"
- "numberOfAppsSharedFromWithConversation"
- "numberOfDifferentFacesSharedWithConversation"
- "numberOfEngagedSuggestionsFromCurrentAppWithConversation"
- "numberOfEngagedSuggestionsOfDetectedPeopleWithConversation"
- "numberOfEngagedSuggestionsOfPeopleInPhotoWithConversation"
- "numberOfEngagedSuggestionsOfTopDomainURLWithConversation"
- "numberOfEngagedSuggestionsToTargetApp"
- "numberOfEngagedSuggestionsWithConversation"
- "numberOfIncomingInteractionsWithConversation"
- "numberOfInteractionsDuringTimePeriodWithConversation"
- "numberOfOutgoingInteractionsWithConversation"
- "numberOfRecentOutgoingInteractionsWithConversation"
- "numberOfSharesFromCurrentAppWithConversation"
- "numberOfSharesOfDetectedPeopleWithConversation"
- "numberOfSharesOfDetectedScenesWithConversation"
- "numberOfSharesOfPeopleInPhotoIoUWithConversation"
- "numberOfSharesOfPeopleInPhotoWithConversation"
- "numberOfSharesOfScenesInPhotoWithConversation"
- "numberOfSharesOfTopDomainURLWithConversation"
- "numberOfSharesWithConversation"
- "numberOfTotalSharesToTargetApp"
- "peopleInPhotoIdentifiers"
- "power:withExponent:"
- "power:withExponent:resultFeatureName:"
- "privatizedConversationId:"
- "privatizedConversationIdentifier"
- "queryStats"
- "reciprocal:withOffset:"
- "reciprocal:withOffset:resultFeatureName:"
- "recordSharePlayInformation:"
- "removeConversationIds:"
- "removeFeature:andConversation:"
- "rename:with:"
- "renameFeature:withFeatureName:"
- "rightBoundDate"
- "saveAppSharedFrom:forConversationId:"
- "saveFeedbackInCoreDuetd:forSessionId:feedbackActionType:isFallbackFetch:reply:"
- "savePersonId:forConversationId:forSyntheticInteraction:"
- "savePersonsInPhoto:forConversationId:"
- "sceneTagsInPhotoIdentifiers"
- "scenesBasedFeatures"
- "setAppToAppExtMapping:"
- "setFeatureNamesToSortWith:"
- "setIsFallbackFetch:"
- "setPeopleInPhotoIdentifiers:"
- "setQueryStats:"
- "setSceneTagsInPhotoIdentifiers:"
- "setStatsToCompute:"
- "setTopDomainURL:"
- "setValue:forFeature:andConversationId:"
- "setValue:forProperty:andConversationId:"
- "sharingInteractionPredicate"
- "sharingInteractions.%@"
- "shouldContinue"
- "shouldUseSuggestionEngaged"
- "statsToCompute"
- "sum:with:"
- "sum:with:resultFeatureName:"
- "sum:withAddend:"
- "sum:withAddend:resultFeatureName:"
- "timeSinceLastIncomingInteraction"
- "timeSinceLastOutgoingInteraction"
- "timeSinceLastPhoneCallWithConversation"
- "timeSinceLastPhotoShareWithConversation"
- "timeSinceLastShareWithConversation"
- "topDomainURL"
- "updatedInInteractionStoreChunk"
- "v28@?0@\"_CDInteractionRecord\"8i16^B20"
- "v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24"
- "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
- "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"
- "v32@?0@\"NSString\"8Q16^B24"
- "v36@0:8@16@24B32"
- "v36@0:8@16@24i32"
- "v40@0:8@16d24@32"
- "v40@?0@\"_CDInteractionsStatisticsConfig\"8@\"NSString\"16@\"_CDInteractionRecord\"24@\"_CDInteractionsStatistics\"32"
- "v52@0:8@\"NSString\"16@\"NSString\"24q32B40@?<v@?B>44"
- "v52@0:8@16@24q32B40@?44"
- "v56@0:8@16Q24Q32@?40@?48"
- "valueForFeature:forConversationId:"
- "valueForProperty:forConversationId:"
- "valueOrDefaultValueForFeature:forConversationId:"

```
