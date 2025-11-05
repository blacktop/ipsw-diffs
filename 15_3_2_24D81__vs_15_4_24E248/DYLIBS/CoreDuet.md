## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x1a384c
-  __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0xfec8
-  __TEXT.__cstring: 0x14ee5
+1892.20.1.0.0
+  __TEXT.__text: 0x1a2c98
+  __TEXT.__auth_stubs: 0x12c0
+  __TEXT.__objc_methlist: 0x11414
+  __TEXT.__cstring: 0x150e3
   __TEXT.__const: 0x5a0
-  __TEXT.__oslogstring: 0x1746d
-  __TEXT.__gcc_except_tab: 0x7748
+  __TEXT.__oslogstring: 0x178e0
+  __TEXT.__gcc_except_tab: 0x7890
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x52c0
-  __TEXT.__objc_classname: 0x2b35
-  __TEXT.__objc_methname: 0x252c6
-  __TEXT.__objc_methtype: 0x608c
-  __TEXT.__objc_stubs: 0x16360
+  __TEXT.__unwind_info: 0x5300
+  __TEXT.__objc_classname: 0x2b1a
+  __TEXT.__objc_methname: 0x257b4
+  __TEXT.__objc_methtype: 0x60c8
+  __TEXT.__objc_stubs: 0x164e0
   __DATA_CONST.__got: 0x10e8
-  __DATA_CONST.__const: 0xdf0
-  __DATA_CONST.__objc_classlist: 0xbf0
+  __DATA_CONST.__const: 0xe98
+  __DATA_CONST.__objc_classlist: 0xbe8
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7bc0
+  __DATA_CONST.__objc_selrefs: 0x7e08
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x658
-  __DATA_CONST.__objc_arraydata: 0x648
-  __AUTH_CONST.__auth_got: 0x960
-  __AUTH_CONST.__const: 0x4b30
-  __AUTH_CONST.__cfstring: 0x12f20
-  __AUTH_CONST.__objc_const: 0x245f0
-  __AUTH_CONST.__objc_intobj: 0x2118
+  __DATA_CONST.__objc_arraydata: 0x698
+  __AUTH_CONST.__auth_got: 0x970
+  __AUTH_CONST.__const: 0x4d70
+  __AUTH_CONST.__cfstring: 0x12da0
+  __AUTH_CONST.__objc_const: 0x220b0
+  __AUTH_CONST.__objc_intobj: 0x2160
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__objc_arrayobj: 0x588
+  __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x5000
-  __DATA.__objc_ivar: 0x16ac
+  __DATA.__objc_ivar: 0x16bc
   __DATA.__data: 0x19e8
-  __DATA.__bss: 0xd80
-  __DATA.__common: 0x31
-  __DATA_DIRTY.__objc_data: 0x2760
+  __DATA.__bss: 0xd90
+  __DATA.__common: 0x38
+  __DATA_DIRTY.__objc_data: 0x2710
   __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuetDaemonProtocol.framework/Versions/A/CoreDuetDaemonProtocol
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D97E56AE-BF4B-3DBF-9323-F0B1FE96D23E
-  Functions: 8287
-  Symbols:   17999
-  CStrings:  13952
+  UUID: 4EEF7EE6-2524-3AD6-87BD-7E6CE0891A1B
+  Functions: 8551
+  Symbols:   18256
+  CStrings:  13996
 
Symbols:
+ +[_CDAutoSuConfig config].cold.1
+ +[_CDDeviceInfo isRunningOnInternalBuild].cold.1
+ +[_CDEventStreams privacyPolicyForEventStreamName:].cold.1
+ +[_CDEventStreams rateLimiterForEventStreamName:].cold.1
+ +[_CDEventStreams sharedInstance].cold.1
+ +[_CDGenericInteractionRanker isDateInWeekend:].cold.1
+ +[_CDHomeManagerUtilities sharedInstance].cold.1
+ +[_CDInteraction _internPool].cold.1
+ +[_CDInteraction conversationIdPercentEscapes].cold.1
+ +[_CDInteraction generateConversationIdFromObjectsWithIdentifiers:].cold.1
+ +[_CDInteraction generateConversationIdFromObjectsWithIdentifiers:].cold.2
+ +[_CDInteraction generateConversationIdFromObjectsWithIdentifiers:].cold.3
+ +[_CDInteraction inverseConversationIdPercentEscapes].cold.1
+ +[_CDInteractionAdvisor sharedInteractionAdvisor].cold.1
+ +[_CDInteractionPolicies disallowedCSSIBundleIds]
+ +[_CDInteractionRecorder interactionRecorder].cold.1
+ +[_CDInteractionStoreNotifier sharedInstance].cold.1
+ +[_CDInteractionsStatisticsConfig computationBlockForStatName:].cold.1
+ +[_CDInteractionsStatisticsConfig isDateInWeekend:].cold.1
+ +[_CDLogging admissionCheckChannel].cold.1
+ +[_CDLogging autoSUChannel].cold.1
+ +[_CDLogging communicatorChannel].cold.1
+ +[_CDLogging contextChannel].cold.1
+ +[_CDLogging dataCollectionChannel].cold.1
+ +[_CDLogging instrumentationChannel].cold.1
+ +[_CDLogging interactionChannel].cold.1
+ +[_CDLogging interactionSignpost].cold.1
+ +[_CDLogging knowledgeChannel].cold.1
+ +[_CDLogging knowledgeSignpost].cold.1
+ +[_CDLogging mediaAnalysisChannel].cold.1
+ +[_CDLogging spotlightReceiverChannel].cold.1
+ +[_CDLogging syncChannel].cold.1
+ +[_CDMemoryUsageIntervalTracker sharedInstance].cold.1
+ +[_CDPerfMetricFamily perfMetricFamilyWithName:].cold.1
+ +[_CDPeriodicScheduler sharedInstance].cold.1
+ +[_CDPrivacyPolicy sharedPrivacyPolicy].cold.1
+ +[_CDRateLimiter sharedRateLimiter].cold.1
+ +[_CDReceiverNotifier sharedInstance].cold.1
+ +[_CDSharedMemoryKeyValueStore log].cold.1
+ +[_CDSizeMetricFamily sizeMetricFamilyWithName:].cold.1
+ +[_CDSpotlightContactResolver sharedInstance].cold.1
+ +[_CDSpotlightItemUtils mechanismUtiMap].cold.1
+ +[_CDSpotlightItemUtils policies].cold.1
+ +[_CDSpotlightItemUtils shouldFilterEmailAddress:].cold.1
+ +[_CDSpotlightItemUtils utiConformCache].cold.1
+ +[_CDSpotlightQuerier osxBundleIdForUTI:].cold.1
+ +[_CDSpotlightQuerier osxUTItoUniqueIdentifierKeyMap].cold.1
+ +[_CDStringTokenizer isEnglishStopWord:].cold.1
+ +[_CDUncachedSentinel sharedInstance].cold.1
+ +[_CDXPCCodecs _log].cold.1
+ +[_CDXPCCodecs eventTypeWithEvent:].cold.1
+ +[_CDXPCCodecs supportedClassesToUnarchive].cold.1
+ +[_DKBiomeStreamCache sharedCache].cold.1
+ +[_DKCategoryCache sharedCached].cold.1
+ +[_DKEvent(CSSearchableItem) allowedWebpageURLSchemes].cold.1
+ +[_DKEventQuery allDevices].cold.1
+ +[_DKEventQuery onlyLocalDevice].cold.1
+ +[_DKEventQuery onlyRemoteDevice].cold.1
+ +[_DKEventStatsCollection collectionWithName:].cold.1
+ +[_DKEventStatsUtilities safeStringWithString:].cold.1
+ +[_DKEventStreamCache sharedCached].cold.1
+ +[_DKKnowledgeStorageLogging sharedInstance].cold.1
+ +[_DKMetadataPersistenceLookupTable attributeToKey].cold.1
+ +[_DKMetadataPersistenceLookupTable keyToIndex].cold.1
+ +[_DKPerformSyncDownPeerAdditionsOperation _updateEventStatsWithIsNewestMissingWindow:].cold.1
+ +[_DKPerformSyncDownPeerAdditionsOperation _updateEventStatsWithPreviousSyncDate:transportType:].cold.1
+ +[_DKPerformSyncDownPeerAdditionsOperation _updateEventStatsWithSyncLatencyOfEvent:ingressDate:transportType:].cold.1
+ +[_DKPerformSyncDownPeerAdditionsOperation _updateEventStatsWithTotal:streamNameCounts:transportType:].cold.1
+ +[_DKPerformSyncDownPeerDeletionsOperation _updateEventStatsWithPreviousSyncDate:transportType:].cold.1
+ +[_DKPerformSyncDownPeerDeletionsOperation _updateEventStatsWithTotal:transportType:].cold.1
+ +[_DKPerformSyncDownPeerOperation _updateEventStatsWithTransportType:].cold.1
+ +[_DKPerformSyncUpHistoryAdditionsOperation _updateEventStatsWithPreviousSyncDate:transportType:].cold.1
+ +[_DKPerformSyncUpHistoryAdditionsOperation _updateEventStatsWithTotal:streamNameCounts:transportType:].cold.1
+ +[_DKPerformSyncUpHistoryDeletionsOperation _updateEventStatsWithPreviousSyncDate:transportType:].cold.1
+ +[_DKPerformSyncUpHistoryDeletionsOperation _updateEventStatsWithTotal:transportType:].cold.1
+ +[_DKPlatform deviceUUID].cold.1
+ +[_DKPredictor predictorLog].cold.1
+ +[_DKPrivacyPolicyEnforcer privacyPolicyEnforcer].cold.1
+ +[_DKRateLimitPolicyEnforcer rateLimitPolicyEnforcer].cold.1
+ +[_DKSync2Coordinator _updateEventStatsWithSyncElapsedTimeStartDate:endDate:].cold.1
+ +[_DKSync2Coordinator _updateEventStatsWithSyncType:].cold.1
+ +[_DKSync2Coordinator shouldDeferSyncOperationWithClass:syncType:transport:peer:policy:].cold.2
+ +[_DKSync2Policy policyCache].cold.1
+ +[_DKSync3Policy disabledPolicy].cold.1
+ +[_DKSync3Policy policyCache].cold.1
+ +[_DKSyncBlockCompositeOperation blockCompositeOperationWithBlock:].cold.1
+ +[_DKSyncCloudKitKnowledgeStorage sharedInstance].cold.1
+ +[_DKSyncContextObjectFactory objectFactoryForClass:context:].cold.1
+ +[_DKSyncDownCloudKitKnowledgeStorage sharedInstance].cold.1
+ +[_DKSyncLocalKnowledgeStorage _updateEventStatsWithFetchEventsTotal:streamNameCounts:].cold.1
+ +[_DKSyncLocalKnowledgeStorage _updateEventStatsWithFetchTombstonesTotal:streamNameCounts:].cold.1
+ +[_DKSyncPeerStatusTracker syncPeerTransportsStrings].cold.1
+ +[_DKSyncRapportCommonStorage sharedInstance].cold.1
+ +[_DKSyncRapportContextStorage sharedInstance].cold.1
+ +[_DKSyncRapportKnowledgeStorage sharedInstance].cold.1
+ +[_DKSyncSerializer sharedInstance].cold.1
+ +[_DKSyncUpCloudKitKnowledgeStorage sharedInstance].cold.1
+ +[_DKSyncUrgencyTracker sharedInstance].cold.1
+ +[_DKSyncWindow choppedWindowsFromSortedNormalizedWindows:betweenWindowMinimumDate:andWindowMaximumDate:].cold.1
+ +[_DKSyncWindow lastWindowMissingFromSortedNormalizedWindows:windowMinimumDate:windowMaximumDate:].cold.1
+ +[_DKSyncWindow lastWindowMissingFromSortedWindows:windowMinimumDate:windowMaximumDate:].cold.1
+ +[_DKSyncWindow redundantWindowsFromSortedWindows:olderThanDate:].cold.1
+ +[_DKSyncWindow unionOfSortedSyncWindows:].cold.1
+ +[_DKSyncedFeatures sharedInstance].cold.1
+ -[NSDate(_DKAdditions) timeSinceMidnight:].cold.1
+ -[NSDate(_DKDeduping) dk_dedup].cold.1
+ -[NSNumber(_DKDeduping) dk_dedup].cold.1
+ -[NSString(_DKDeduping) dk_dedup].cold.1
+ -[_CDEventHandlerForActivityLevel init].cold.1
+ -[_CDEventHandlerForAppInFocus init].cold.1
+ -[_CDEventHandlerForDefaultPairedNearby init].cold.1
+ -[_CDEventHandlerForWatchNearby init].cold.1
+ -[_CDEventIndexerBookmark description].cold.1
+ -[_CDEventIndexerBookmark encodeWithCoder:].cold.1
+ -[_CDEventIndexerBookmark encodeWithCoder:].cold.2
+ -[_CDEventIndexerBookmark isEqual:].cold.1
+ -[_CDInteraction setAccount:].cold.1
+ -[_CDInteraction setBundleId:].cold.1
+ -[_CDInteraction setContentURL:].cold.1
+ -[_CDInteraction setDerivedIntentIdentifier:].cold.1
+ -[_CDInteraction setDomainIdentifier:].cold.1
+ -[_CDInteraction setGroupName:].cold.1
+ -[_CDInteraction setNsUserName:].cold.1
+ -[_CDInteraction setSender:].cold.1
+ -[_CDInteraction setTargetBundleId:].cold.1
+ -[_CDInteractionCache _refetch].cold.1
+ -[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:].cold.2
+ -[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]
+ -[_CDInteractionStore lowPriorityWorkCanContinue]
+ -[_CDInteractionStore runHighPriorityDBBlock:]
+ -[_CDInteractionStore runLowPriorityDBPreemptableBlock:]
+ -[_CDInteractionsStatistics aggregateSum:resultFeatureName:]
+ -[_CDInteractionsStatistics computeCandidateLevelSignals]
+ -[_CDInteractionsStatistics computeNumberOfAppsSharedFromWithConversation]
+ -[_CDInteractionsStatistics computeNumberOfEngagedSuggestionsToTargetApp]
+ -[_CDInteractionsStatistics computeNumberOfFacesSharedWithConversation]
+ -[_CDInteractionsStatistics computeNumberOfSharesToTargetApp]
+ -[_CDInteractionsStatistics computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:]
+ -[_CDInteractionsStatistics saveAppSharedFrom:forConversationId:]
+ -[_CDInteractionsStatistics savePersonsInPhoto:forConversationId:]
+ -[_CDInteractionsStatistics sum:withAddend:resultFeatureName:]
+ -[_CDInteractionsStatisticsConfig _shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:]
+ -[_CDInteractionsStatisticsConfig _shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:]
+ -[_CDInteractionsStatisticsConfig anchorDate]
+ -[_CDInteractionsStatisticsConfig appBundleIdForAppExtBundleId:]
+ -[_CDInteractionsStatisticsConfig appToAppExtMapping]
+ -[_CDInteractionsStatisticsConfig communicationInteractionPredicate]
+ -[_CDInteractionsStatisticsConfig computeAppsSharedFromForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeNumberOfRecentOutgoingInteractionsWithConversationForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computePastSharedPeopleInPhotoForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeScenesBasedFeaturesForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeStatsForInteractionRecord:inInteractionsStatistics:chunkIndex:].cold.1
+ -[_CDInteractionsStatisticsConfig computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeTimeSinceLastPhotoShareWithConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeTimeSinceLastShareWithConversation:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig computeTimeSinceLastUIEngagementForConversationId:interactionRecord:inInteractionsStatistics:]
+ -[_CDInteractionsStatisticsConfig getConversationIdForRecord:]
+ -[_CDInteractionsStatisticsConfig initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:]
+ -[_CDInteractionsStatisticsConfig initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:]
+ -[_CDInteractionsStatisticsConfig leftBoundDate]
+ -[_CDInteractionsStatisticsConfig maxComputationTime]
+ -[_CDInteractionsStatisticsConfig peopleInPhotoIdentifiers]
+ -[_CDInteractionsStatisticsConfig scenesBasedFeaturesNames]
+ -[_CDInteractionsStatisticsConfig scenesInPhotoIdentifiers]
+ -[_CDInteractionsStatisticsConfig setAppToAppExtMapping:]
+ -[_CDInteractionsStatisticsConfig setScenesInPhotoIdentifiers:]
+ -[_CDInteractionsStatisticsConfig sharingInteractionPredicate]
+ -[_CDInteractionsStatisticsConfig shouldContinue]
+ -[_CDInteractionsStatisticsConfig statsToCompute]
+ -[_CDInteractionsStatisticsConfig topLevelScenesFromSceneNetTags:]
+ -[_CDMDSearchQueryDelegate searchQuery:didFailWithError:].cold.2
+ -[_CDMDSearchQueryDelegate searchQuery:didReturnItems:].cold.1
+ -[_CDMDSearchQueryDelegate searchQuery:statusChanged:].cold.1
+ -[_CDMemoryUsageInterval end].cold.1
+ -[_CDMemoryUsageIntervalTracker init].cold.1
+ -[_CDObservationCenter _removeObserver:name:observerObserver:].cold.1
+ -[_CDObservationCenter _removeObserver:observerObserver:].cold.1
+ -[_CDSerializableKeyedData isEqual:].cold.1
+ -[_CDSiriLearningSettings allLearningDisabledBundleIDs].cold.1
+ -[_CDSpotlightEventIndexer beginIndexingWithBatchSize:completion:].cold.1
+ -[_CDSpotlightEventIndexer finishIndexing].cold.1
+ -[_CDSpotlightItemRecorder _addOrUpdateCoreDuetInteractions:bundleID:].cold.1
+ -[_CDSpotlightItemRecorder deleteAllItemsWithBundleID:isCSSIDeletion:completion:]
+ -[_CDSpotlightItemRecorder deleteInteractionsWithIdentifiers:bundleID:protectionClass:withCompletion:].cold.1
+ -[_CDSpotlightItemRecorder deleteSearchableItemsWithIdentifiers:bundleID:withCompletion:].cold.3
+ -[_CDSpotlightItemRecorder deleteSearchableItemsWithIdentifiers:bundleID:withCompletion:].cold.4
+ -[_DKCategoryCache categoryWithInteger:type:].cold.1
+ -[_DKCoreDataStorage managedObjectModel].cold.2
+ -[_DKCoreDataStorage persistentStoreCoordinatorFor:].cold.15
+ -[_DKHistogramQuery executeUsingCoreDataStorage:error:].cold.3
+ -[_DKKnowledgeStorage _databaseChangedWithNotification:].cold.1
+ -[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:].cold.2
+ -[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:].cold.2
+ -[_DKKnowledgeStorage updateDataBeforeAutoMigrationFromVersion:inStoreAtURL:error:].cold.8
+ -[_DKKnowledgeStore deleteRemoteState:].cold.1
+ -[_DKKnowledgeStore executeQuery:responseQueue:].cold.2
+ -[_DKKnowledgeStore synchronizeWithError:].cold.1
+ -[_DKPredictionTimeline description].cold.1
+ -[_DKPredictionTimeline initWithCoder:].cold.1
+ -[_DKPredictionTimeline isEqual:].cold.1
+ -[_DKSync2Coordinator __performSyncWithCompletion:].cold.3
+ -[_DKSync2Coordinator __performSyncWithCompletion:].cold.4
+ -[_DKSyncCloudKitKnowledgeStorage hasAdditionsFlagForPeer:].cold.2
+ -[_DKSyncCloudKitKnowledgeStorage hasDeletionsFlagForPeer:].cold.2
+ -[_DKSyncCloudKitKnowledgeStorage setHasAdditionsFlag:forPeer:].cold.2
+ -[_DKSyncCloudKitKnowledgeStorage setHasDeletionsFlag:forPeer:].cold.2
+ -[_DKSyncCloudKitKnowledgeStorage syncDownAdditionsFromCloudWithZoneID:windows:streamNames:limit:fetchOrder:completion:].cold.2
+ -[_DKSyncSerializer addDependentOperation:].cold.1
+ -[_DKSyncType initWithCoder:].cold.1
+ -[_DKThrottledActivity activityThrottler].cold.1
+ GCC_except_table107
+ GCC_except_table116
+ GCC_except_table134
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table144
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table183
+ GCC_except_table191
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table205
+ GCC_except_table206
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table236
+ GCC_except_table247
+ GCC_except_table249
+ GCC_except_table279
+ GCC_except_table289
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table83
+ InteractionAnalysisPETInteractionEventsReadFrom.cold.1
+ OBJC_IVAR_$__CDInteractionStore._waitingForDB
+ OBJC_IVAR_$__CDInteractionsStatistics._appsSharedFromByConversationId
+ OBJC_IVAR_$__CDInteractionsStatistics._personsSharedInPastPhotos
+ OBJC_IVAR_$__CDInteractionsStatisticsConfig._appToAppExtMapping
+ OBJC_IVAR_$__CDInteractionsStatisticsConfig._defaultValues
+ OBJC_IVAR_$__CDInteractionsStatisticsConfig._scenesBasedFeatures
+ OBJC_IVAR_$__CDInteractionsStatisticsConfig._scenesInPhotoIdentifiers
+ OBJC_IVAR_$__CDInteractionsStatisticsConfig._scenesMinimumNumberOfTags
+ _CDFormattedDate.cold.1
+ _CDInteractionNSXPCInterface.cold.1
+ _DKDaemonInterface.cold.1
+ _DKPRChangeSetReadFrom.cold.1
+ _DKPREventReadFrom.cold.1
+ _DKPRMetadataReadFrom.cold.1
+ _DKQueryLoggingEnabled.cold.1
+ _DKStringContainsPrivacySensitiveMetadataKey.cold.1
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_78
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ __100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.376
+ __100-[_DKKnowledgeStorage(DataMigration) updateDataAfterAutoMigrationToVersion:inPersistentStore:error:]_block_invoke.cold.2
+ __100-[_DKKnowledgeStorage(DataMigration) updateDataAfterAutoMigrationToVersion:inPersistentStore:error:]_block_invoke.cold.3
+ __103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke.277
+ __103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke.279
+ __104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.506
+ __104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.510
+ __104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke_2.511
+ __107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_3.cold.1
+ __107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_3.cold.2
+ __113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.720
+ __113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.728
+ __31-[_CDInteractionCache _refetch]_block_invoke.254
+ __31-[_CDInteractionCache _refetch]_block_invoke.254.cold.1
+ __35-[_CDInteractionStoreNotifier init]_block_invoke.35
+ __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.630
+ __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.635
+ __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.662
+ __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.673
+ __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.666
+ __40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.712
+ __41-[_CDInteractionStore metadataDictionary]_block_invoke.487
+ __42-[_DKKnowledgeStorage _saveObjects:error:]_block_invoke.cold.2
+ __44-[_CDSpotlightItemRecorder submitOperation:]_block_invoke.753
+ __46-[_DKSyncedFeatures _fetchScreenTimeSyncState]_block_invoke.cold.2
+ __47-[_DKKnowledgeStorage migrationStreamsWithMOC:]_block_invoke.683
+ __49-[_CDInteractionsStatistics descriptionRedacted:]_block_invoke.190
+ __49-[_CDSpotlightEventIndexer indexAdditionsAsBatch]_block_invoke.cold.2
+ __49-[_CDSpotlightEventIndexer indexDeletionsAsBatch]_block_invoke.cold.2
+ __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.298
+ __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.331
+ __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke_2.cold.1
+ __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke_2.cold.2
+ __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.762
+ __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.762.cold.1
+ __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.762.cold.2
+ __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.762.cold.3
+ __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.762.cold.4
+ __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.762.cold.5
+ __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.808
+ __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.813
+ __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.811
+ __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.814
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737.cold.1
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737.cold.2
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737.cold.3
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737.cold.4
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737.cold.5
+ __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.737.cold.6
+ __58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.464
+ __58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.466
+ __58-[_DKHistogramQuery _fetchRemoteResultsWithStorage:error:]_block_invoke.cold.2
+ __60-[_CDSpotlightCoalescedDeletionManager setupCoalescingTimer]_block_invoke.17
+ __60-[_CDSpotlightCoalescedDeletionManager setupCoalescingTimer]_block_invoke.18
+ __63-[_DKKnowledgeStorage _sendEventsNotificationName:withObjects:]_block_invoke.573
+ __64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.188
+ __64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.190
+ __64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.194
+ __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.729
+ __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.737
+ __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.741
+ __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke_2.733
+ __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke_2.748
+ __66-[_CDSocialInteractionAdvisor tuneUsingSettings:heartBeatHandler:]_block_invoke.203
+ __66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.816
+ __66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.816.cold.1
+ __66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.708
+ __67-[_DKSyncCloudKitKnowledgeStorage _cloudSyncAvailabilityDidChange:]_block_invoke.cold.1
+ __67-[_DKSyncCloudKitKnowledgeStorage _cloudSyncAvailabilityDidChange:]_block_invoke.cold.2
+ __67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.189.cold.1
+ __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke.685
+ __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke.693
+ __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke.702
+ __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke_2.689
+ __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke_2.696
+ __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.511
+ __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.511.cold.1
+ __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.515
+ __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.515.cold.1
+ __70-[_CDSpotlightItemRecorder _addOrUpdateCoreDuetInteractions:bundleID:]_block_invoke.755
+ __73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke.205
+ __73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke.cold.1
+ __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.792
+ __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.794
+ __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.795
+ __74-[_DKSyncCloudKitKnowledgeStorage configurePeerWithSourceDeviceID:zoneID:]_block_invoke.cold.1
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.18
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.21
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.23
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.28
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.30
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.31
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.31.cold.1
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke_2.24
+ __75-[_CDSocialInteractionAdvisor rankContacts:withSeedContacts:usingSettings:]_block_invoke.189
+ __78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.777
+ __78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.778
+ __78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.787
+ __79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.802
+ __79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.802.cold.1
+ __84-[_CDSpotlightItemRecorder addInteractions:bundleID:protectionClass:withCompletion:]_block_invoke.cold.1
+ __86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.609.cold.3
+ __87-[_CDSocialInteractionAdvisor adviseInteractionsForDate:andSeedContacts:usingSettings:]_block_invoke.198
+ __93-[_CDSpotlightCoalescedDeletionOperation enumerateDeletionPredicatesAndCompletionsWithBlock:]_block_invoke.127
+ __95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.824
+ __95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.827
+ __CDProcessNameForXPCConnection
+ __MergedGlobals
+ __PASEvaluateLogFaultAndProbCrashCriteria
+ ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke
+ ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_2
+ ___107-[_CDInteractionStore _iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:]_block_invoke_3
+ ___126-[_CDInteractionsStatisticsConfig computePastSharedPeopleInPhotoForConversationId:interactionRecord:inInteractionsStatistics:]_block_invoke
+ ___53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke_2
+ ___59-[_CDInteractionsStatisticsConfig scenesBasedFeaturesNames]_block_invoke
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_21
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_22
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_23
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_24
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_25
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_26
+ ___63+[_CDInteractionsStatisticsConfig computationBlockForStatName:]_block_invoke_27
+ ___66-[_CDInteractionsStatisticsConfig topLevelScenesFromSceneNetTags:]_block_invoke
+ ___74-[_CDInteractionsStatistics computeNumberOfAppsSharedFromWithConversation]_block_invoke
+ ___81-[_CDSpotlightItemRecorder deleteAllItemsWithBundleID:isCSSIDeletion:completion:]_block_invoke
+ ____cdcontextstore_signpost_deprecated_api_block_invoke
+ ___block_descriptor_32_e18_16?0"NSString"8l
+ ___block_descriptor_32_e31_v24?0"NSString"8"NSString"16l
+ ___block_descriptor_32_e39_"NSString"16?0"_CDAttachmentRecord"8l
+ ___block_descriptor_40_e23_B24?0"_CDContact"8Q16l
+ ___block_descriptor_40_e8_32s_e27_B32?0"_CDContact"8Q16^B24l
+ ___block_descriptor_40_e8_32s_e31_v24?0"NSString"8"NSString"16l
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSMutableSet"16^B24l
+ ___block_descriptor_48_e8_32s40s_e37_v28?0"_CDInteractionRecord"8i16^B20l
+ ___block_descriptor_56_e8_32s40s48r_e22_B16?0"BMStoreEvent"8l
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_56_e8_32s40s48s_e32_v32?0"NSString"8"NSSet"16^B24l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_C8?0l
+ ___block_descriptor_88_e8_32s40s48s56bs64bs_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64r72r80r
+ ___destroy_helper_block_e8_32s40s48s56s64r72r80r
+ __block_literal_global.122
+ __block_literal_global.15
+ __block_literal_global.176
+ __block_literal_global.186
+ __block_literal_global.200
+ __block_literal_global.21
+ __block_literal_global.252
+ __block_literal_global.259
+ __block_literal_global.261
+ __block_literal_global.262
+ __block_literal_global.265
+ __block_literal_global.269
+ __block_literal_global.27
+ __block_literal_global.271
+ __block_literal_global.273
+ __block_literal_global.275
+ __block_literal_global.277
+ __block_literal_global.279
+ __block_literal_global.281
+ __block_literal_global.283
+ __block_literal_global.285
+ __block_literal_global.287
+ __block_literal_global.289
+ __block_literal_global.291
+ __block_literal_global.293
+ __block_literal_global.295
+ __block_literal_global.297
+ __block_literal_global.299
+ __block_literal_global.30
+ __block_literal_global.301
+ __block_literal_global.303
+ __block_literal_global.305
+ __block_literal_global.307
+ __block_literal_global.311
+ __block_literal_global.313
+ __block_literal_global.315
+ __block_literal_global.327
+ __block_literal_global.331
+ __block_literal_global.358
+ __block_literal_global.426
+ __block_literal_global.490
+ __block_literal_global.496
+ __block_literal_global.51
+ __block_literal_global.514
+ __block_literal_global.55
+ __block_literal_global.567
+ __block_literal_global.630
+ __block_literal_global.638
+ __block_literal_global.641
+ __block_literal_global.665
+ __block_literal_global.676
+ __block_literal_global.681
+ __block_literal_global.686
+ __block_literal_global.694
+ __block_literal_global.695
+ __block_literal_global.698
+ __block_literal_global.711
+ __block_literal_global.719
+ __block_literal_global.726
+ __block_literal_global.732
+ __block_literal_global.749
+ __block_literal_global.776
+ __block_literal_global.783
+ __block_literal_global.797
+ __block_literal_global.950
+ __cdcontextstore_signpost_deprecated_api
+ _abort
+ _cd_dispatch_async_xpc
+ _cdcontextstore_signpost_deprecated_api.client
+ _cdcontextstore_signpost_deprecated_api.cold.1
+ _cdcontextstore_signpost_deprecated_api.onceToken
+ _exp2
+ _extend_feature_name
+ _internPool._pasOnceToken20
+ _logChannel.cold.1
+ _objc_msgSend$_handoffCurrentReplyToQueue:block:
+ _objc_msgSend$_iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:
+ _objc_msgSend$_pas_filteredArrayWithIndexedTest:
+ _objc_msgSend$_pas_mappedSetWithTransform:
+ _objc_msgSend$_shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:
+ _objc_msgSend$_shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:
+ _objc_msgSend$aggregateSum:resultFeatureName:
+ _objc_msgSend$bundleIdForConversationId:
+ _objc_msgSend$communicationInteractionPredicate
+ _objc_msgSend$computeNumberOfAppsSharedFromWithConversation
+ _objc_msgSend$computeNumberOfEngagedSuggestionsToTargetApp
+ _objc_msgSend$computeNumberOfFacesSharedWithConversation
+ _objc_msgSend$computeNumberOfSharesToTargetApp
+ _objc_msgSend$disallowedCSSIBundleIds
+ _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$lowPriorityWorkCanContinue
+ _objc_msgSend$maxComputationTime
+ _objc_msgSend$publisherWithUseCase:options:
+ _objc_msgSend$runHighPriorityDBBlock:
+ _objc_msgSend$runLowPriorityDBPreemptableBlock:
+ _objc_msgSend$saveAppSharedFrom:forConversationId:
+ _objc_msgSend$savePersonsInPhoto:forConversationId:
+ _objc_msgSend$sharingInteractionPredicate
+ _objc_msgSend$shouldContinue
+ _objc_msgSend$sum:withAddend:resultFeatureName:
+ _xpc_transaction_exit_clean
+ active_memory_limit.cold.1
+ computationBlockForStatName:._pasOnceToken19
+ isDateInWeekend:._pasOnceToken18
+ mediaAnalysisChannel._pasOnceToken54
+ resolve.cold.2
+ sharedInstance._pasOnceToken20
+ sharedInstance._pasOnceToken21
- +[_CDDiagnosticDataReporter addValue:forScalarKey:]
- +[_CDDiagnosticDataReporter clearDistributionKey:]
- +[_CDDiagnosticDataReporter clearScalarKey:]
- +[_CDDiagnosticDataReporter pushValue:forDistributionKey:]
- +[_CDDiagnosticDataReporter setValue:forDistributionKey:]
- +[_CDDiagnosticDataReporter setValue:forScalarKey:]
- +[_CDDiagnosticDataReporter setValue:forScalarKey:limitingSigDigs:]
- +[_CDInteractionAdvisorUtils updateConsumerModelSettings:]
- +[_CDInteractionAdvisorUtils updateConsumerModelSettings:].cold.1
- +[_CDInteractionFeedbackLogger aggdKeyForAdviceSource:]
- +[_CDInteractionFeedbackLogger aggdKeyForPresentationStyle:]
- +[_CDSpotlightItemRecorder recordAggdReceiverAction:bundleID:count:]
- +[_DKSyncPolicy policy].cold.1
- +[_DKSyncPolicy policy].cold.2
- +[_DKSyncWindow completedWindowsFromWindows:firstEvent:lastEvent:fetchOrder:fillOrder:hitLimit:].cold.1
- +[_DKSyncWindow completedWindowsFromWindows:firstEvent:lastEvent:fetchOrder:fillOrder:hitLimit:].cold.2
- -[_CDDataCollection _execute].cold.1
- -[_CDDataCollection _execute].cold.10
- -[_CDDataCollection _execute].cold.2
- -[_CDDataCollection _execute].cold.3
- -[_CDDataCollection _execute].cold.4
- -[_CDDataCollection _execute].cold.5
- -[_CDDataCollection _execute].cold.6
- -[_CDDataCollection _execute].cold.7
- -[_CDDataCollection _execute].cold.8
- -[_CDDataCollection _execute].cold.9
- -[_CDDataCollection cleanup].cold.1
- -[_CDDataCollection submitDataForCollection].cold.1
- -[_CDDataCollection submitDataForCollection].cold.2
- -[_CDDataCollection submitDataForCollection].cold.3
- -[_CDDataCollection truncatedFileHandle].cold.1
- -[_CDEventStreamsRegister getEventHandlerDictForStreams].cold.1
- -[_CDFileUtility fileHandlerUtiity:withBundleId:withMetaData:].cold.1
- -[_CDFileUtility writeJSON:withFileHandle:].cold.1
- -[_CDInteractionsStatistics laplaceProbabilityCorrected:withAlpha:resultFeatureName:]
- -[_CDInteractionsStatisticsConfig computeTimeSinceOutgoingInteractionNumber10ForConversationId:interactionRecord:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig getConversationIdAndComputeStatForStatName:record:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig getConversationIdAndComputeStatForStatNames:record:inInteractionsStatistics:]
- -[_CDInteractionsStatisticsConfig initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldSortAscending:shouldUseSuggestionEngaged:statsDefaultValues:]
- -[_CDInteractionsStatisticsConfig init]
- -[_CDInteractionsStatisticsConfig interactionsSelectionPredicateBetweenStartDate:andEndDate:]
- -[_CDInteractionsStatisticsConfig predicate]
- -[_CDInteractionsStatisticsConfig setShouldSortAscending:]
- -[_CDInteractionsStatisticsConfig shouldStopRecordProcessing:]
- -[_CDServerRequest URLSession:didBecomeInvalidWithError:].cold.1
- -[_CDServerRequest URLSession:downloadTask:didFinishDownloadingToURL:].cold.1
- -[_CDServerRequest URLSession:downloadTask:didFinishDownloadingToURL:].cold.2
- -[_CDServerRequest URLSession:downloadTask:didFinishDownloadingToURL:].cold.3
- -[_CDServerRequest URLSession:task:didCompleteWithError:].cold.1
- -[_CDServerRequest URLSession:task:didCompleteWithError:].cold.2
- -[_CDServerRequest URLSession:task:didCompleteWithError:].cold.3
- -[_CDServerRequest URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:].cold.1
- -[_CDServerRequest URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:].cold.2
- -[_CDServerRequest startDataTaskWithURI:headers:timeoutInterval:responseHandler:].cold.1
- -[_CDSharedMemoryKeyValueStore initWithName:size:].cold.1
- -[_CDSharedMemoryKeyValueStore initWithName:size:].cold.2
- -[_CDSpotlightEventIndexer indexAdditionsAsBatch].cold.1
- -[_CDSpotlightEventIndexer indexAdditionsAsBatch].cold.2
- -[_CDSpotlightEventIndexer indexDeletionsAsBatch].cold.1
- -[_CDSpotlightEventIndexer indexDeletionsAsBatch].cold.2
- -[_CDSpotlightItemRecorder _deleteUserActivitiesWithPersistentIdentifiers:bundleID:].cold.1
- -[_CDSpotlightItemRecorder deleteAllItemsWithBundleID:completion:]
- -[_CDSpotlightItemRecorder deleteKnowledgeEventsMatchingPredicate:withCompletion:].cold.1
- -[_CDSpotlightItemRecorder getUidOfDonator].cold.1
- -[_CDSpotlightItemRecorder getUidOfDonator].cold.2
- -[_CDSpotlightItemRecorder getUidOfDonator].cold.3
- -[_CDSpotlightItemRecorder getUserNameOfDonator].cold.1
- -[_CDSpotlightItemRecorder getUserNameOfDonator].cold.2
- -[_CDSpotlightItemRecorder getUserNameOfDonator].cold.3
- -[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:].cold.1
- -[_CDSpotlightItemRecorder saveRateLimitedEvents:donatorUid:responseQueue:withCompletion:].cold.2
- -[_CDTemporalInteractionAdvisor dataQueue]
- -[_CDTemporalInteractionAdvisor dealloc]
- -[_CDTemporalInteractionAdvisor setDataQueue:]
- -[_CDTemporalInteractionAdvisor setSettingsNotifyToken:]
- -[_CDTemporalInteractionAdvisor settingsNotifyToken]
- -[_CDTemporalInteractionAdvisor updateConsumerModel]
- -[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:].cold.1
- -[_DKCloudUtilities _updateAccountInfo:error:].cold.1
- -[_DKCloudUtilities _updateAccountInfo:error:].cold.2
- -[_DKCloudUtilities _updateAccountInfo:error:].cold.3
- -[_DKCloudUtilities _updateAccountInfo:error:].cold.4
- -[_DKCloudUtilities isSingleDevice].cold.1
- -[_DKCloudUtilities isSingleDevice].cold.2
- -[_DKCoreDataStorage handleDataProtectionChangeFor:willBeAvailable:].cold.1
- -[_DKCoreDataStorage migratePersistentStoreAtURL:toManagedObjectModel:protectionClass:startVersion:endVersion:error:].cold.1
- -[_DKCoreDataStorage migratePersistentStoreAtURL:toManagedObjectModel:protectionClass:startVersion:endVersion:error:].cold.2
- -[_DKCoreDataStorage removePersistentStoresInCoordinator:].cold.1
- -[_DKDeviceActivityStandingQuery executeWithStorage:referenceDate:].cold.1
- -[_DKDeviceActivityStandingQuery executeWithStorage:referenceDate:].cold.2
- -[_DKDeviceActivityStandingQuery executeWithStorage:referenceDate:].cold.3
- -[_DKDeviceActivityStandingQuery executeWithStorage:referenceDate:].cold.4
- -[_DKDeviceActivityStandingQuery executeWithStorage:referenceDate:].cold.5
- -[_DKDeviceActivityStandingQuery executeWithStorage:referenceDate:].cold.6
- -[_DKEventCKConverter eventDataFromRecord:].cold.1
- -[_DKEventCKConverter eventDataFromRecord:].cold.2
- -[_DKEventCKConverter eventDataFromRecord:].cold.3
- -[_DKEventCKConverter recordFromEventData:event:].cold.1
- -[_DKEventCKConverter recordFromEventData:event:].cold.2
- -[_DKEventStatsCounterInternal indexOfTypeValue:success:].cold.1
- -[_DKEventStatsCounterInternal indexOfTypeValue:success:].cold.2
- -[_DKKnowledgeStorage _deleteObjects:error:].cold.1
- -[_DKKnowledgeStorage _deleteObjects:error:].cold.2
- -[_DKKnowledgeStorage _tombstoneObjects:error:].cold.1
- -[_DKKnowledgeStorage migrateStream:context:].cold.1
- -[_DKKnowledgeStorage setKeyValueObject:forKey:domain:].cold.1
- -[_DKKnowledgeStorage syncStorageIfAvailable].cold.1
- -[_DKKnowledgeStorage syncStorageIfAvailable].cold.2
- -[_DKKnowledgeStorage syncStorageIfAvailable].cold.3
- -[_DKObjectFromMOCache reportMetrics]
- -[_DKPerformSyncDownOperation performSyncDown2].cold.1
- -[_DKPerformSyncDownOperation performSyncDown2].cold.2
- -[_DKPerformSyncDownOperation performSyncDown2].cold.3
- -[_DKPerformSyncDownOperation performSyncDown2].cold.4
- -[_DKPerformSyncDownPeerAdditionsOperation coalesceRedundantOverlappingWindows].cold.1
- -[_DKPerformSyncDownPeerAdditionsOperation coalesceRedundantOverlappingWindows].cold.2
- -[_DKPerformSyncDownPeerAdditionsOperation handleFetchedEvents:completedWindows:missingWindows:].cold.1
- -[_DKPerformSyncDownPeerAdditionsOperation handleFetchedEvents:completedWindows:missingWindows:].cold.2
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithCompletedWindows:].cold.1
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithCompletedWindows:].cold.2
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithCompletedWindows:].cold.3
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithCompletedWindows:].cold.4
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithCompletedWindows:].cold.5
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithDidPrewarm:orError:].cold.1
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithDidPrewarm:orError:].cold.2
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditionsWithHighWaterMark:orError:].cold.1
- -[_DKPerformSyncDownPeerAdditionsOperation performSyncDownPeerAdditions].cold.1
- -[_DKPerformSyncDownPeerDeletionsOperation handleFetchedDeletedEventIDs:startDate:endDate:untilDate:].cold.1
- -[_DKPerformSyncDownPeerDeletionsOperation handleFetchedDeletedEventIDs:startDate:endDate:untilDate:].cold.2
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithDidPrewarm:orError:].cold.1
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithDidPrewarm:orError:].cold.2
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithHighWaterMark:orError:].cold.1
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithPreviousUntilDate:].cold.1
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithPreviousUntilDate:].cold.2
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithPreviousUntilDate:].cold.3
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithPreviousUntilDate:].cold.4
- -[_DKPerformSyncDownPeerDeletionsOperation performSyncDownPeerDeletionsWithPreviousUntilDate:].cold.5
- -[_DKPerformSyncDownPeerOperation performSyncDownPeer].cold.1
- -[_DKPerformSyncDownPeerOperation performSyncDownPeer].cold.2
- -[_DKPerformSyncDownPeerOperation performSyncDownPeer].cold.3
- -[_DKPerformSyncDownPeerOperation performSyncDownPeer].cold.4
- -[_DKPerformSyncUpChangeOperation performSyncUpChange].cold.1
- -[_DKPerformSyncUpChangeOperation performSyncUpChange].cold.2
- -[_DKPerformSyncUpHistoryAdditionsOperation handleUpdateStorageWithFetchedWindow:eventsCount:error:].cold.1
- -[_DKPerformSyncUpHistoryAdditionsOperation handleUpdateStorageWithFetchedWindow:eventsCount:error:].cold.2
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditionsWithAdditionsHighWaterMark:orError:].cold.1
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditionsWithAdditionsHighWaterMark:orError:].cold.2
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditionsWithPreviousHighWaterMark:].cold.1
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditionsWithPreviousHighWaterMark:].cold.2
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditionsWithPreviousHighWaterMark:].cold.3
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditionsWithPreviousHighWaterMark:].cold.4
- -[_DKPerformSyncUpHistoryAdditionsOperation performSyncUpHistoryAdditions].cold.1
- -[_DKPerformSyncUpHistoryDeletionsOperation handleUpdateStorageWithStartDate:endDate:deletedEventIDsCount:orError:].cold.1
- -[_DKPerformSyncUpHistoryDeletionsOperation handleUpdateStorageWithStartDate:endDate:deletedEventIDsCount:orError:].cold.2
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletionsWithDeletionsHighWaterMark:orError:].cold.1
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletionsWithDeletionsHighWaterMark:orError:].cold.2
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletionsWithPreviousHighWaterMark:].cold.1
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletionsWithPreviousHighWaterMark:].cold.2
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletionsWithPreviousHighWaterMark:].cold.3
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletions].cold.1
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletions].cold.2
- -[_DKPerformSyncUpHistoryDeletionsOperation performSyncUpHistoryDeletions].cold.3
- -[_DKPerformSyncUpHistoryOperation performSyncUpHistory].cold.1
- -[_DKPerformSyncUpHistoryOperation performSyncUpHistory].cold.2
- -[_DKPerformSyncUpHistoryOperation performSyncUpHistory].cold.3
- -[_DKPerformSyncUpHistoryOperation performSyncUpHistory].cold.4
- -[_DKPredictionQuery likelihoodForTopN:withMinLikelihood:withData:].cold.1
- -[_DKPredictionQuery likelihoodForTopN:withMinLikelihood:withData:].cold.2
- -[_DKPredictionQuery predictionOfType:withData:].cold.1
- -[_DKPredictionQuery predictionOfType:withData:].cold.2
- -[_DKPredictionQuery predictionOfType:withData:].cold.3
- -[_DKPredictionQuery predictionOfType:withData:].cold.4
- -[_DKPredictor predictionForStreamsWithNames:withPredicate:withPredictionType:withDataPartitionType:asOfDate:].cold.1
- -[_DKSync2Coordinator _checkInTriggeredSyncActivity:isStartup:].cold.1
- -[_DKSync2Coordinator _checkInTriggeredSyncActivity:isStartup:].cold.2
- -[_DKSync2Coordinator _createPushConnection].cold.1
- -[_DKSync2Coordinator _createPushConnection].cold.2
- -[_DKSync2Coordinator _createPushConnection].cold.3
- -[_DKSync2Coordinator _createPushConnection].cold.4
- -[_DKSync2Coordinator _deleteForeignSiriEvents].cold.1
- -[_DKSync2Coordinator _deleteNextBatchOfOurSiriEventsFromCloudWithStartDate:].cold.1
- -[_DKSync2Coordinator _deleteNextBatchOfOurSiriEventsFromCloudWithStartDate:].cold.2
- -[_DKSync2Coordinator _finishActivityWithError:].cold.1
- -[_DKSync2Coordinator _finishActivityWithError:].cold.2
- -[_DKSync2Coordinator _finishActivityWithError:].cold.3
- -[_DKSync2Coordinator _finishActivityWithError:].cold.4
- -[_DKSync2Coordinator _finishActivityWithError:].cold.5
- -[_DKSync2Coordinator _finishActivityWithError:].cold.6
- -[_DKSync2Coordinator _performInitialSync].cold.1
- -[_DKSync2Coordinator _performPeriodicJob].cold.1
- -[_DKSync2Coordinator _performSyncTogglesChangedActions].cold.1
- -[_DKSync2Coordinator _performSyncTogglesChangedActions].cold.2
- -[_DKSync2Coordinator _registerDatabaseObservers].cold.1
- -[_DKSync2Coordinator _registerPeriodicJob].cold.1
- -[_DKSync2Coordinator _registerPeriodicJob].cold.2
- -[_DKSync2Coordinator _registerRapportLaunchOnDemandHandler].cold.1
- -[_DKSync2Coordinator _reregisterPeriodicJob].cold.1
- -[_DKSync2Coordinator _reregisterPeriodicJob].cold.2
- -[_DKSync2Coordinator _reregisterPeriodicJob].cold.3
- -[_DKSync2Coordinator _reregisterPeriodicJob].cold.4
- -[_DKSync2Coordinator _synchronizeWithUrgency:client:completion:].cold.1
- -[_DKSync2Coordinator _unregisterDatabaseObservers].cold.1
- -[_DKSync2Coordinator _unregisterPeriodicJob].cold.1
- -[_DKSync2Coordinator _updateTriggeredSyncActivity].cold.1
- -[_DKSync2Coordinator _updateTriggeredSyncActivity].cold.2
- -[_DKSync2Coordinator _updateTriggeredSyncActivity].cold.3
- -[_DKSync2Coordinator handleFetchedSourceDeviceID:version:fromPeer:error:].cold.1
- -[_DKSync2Coordinator possiblyUpdateIsBusyProperty].cold.1
- -[_DKSync2Coordinator possiblyUpdateIsBusyProperty].cold.2
- -[_DKSync2Coordinator(APSConnectionDelegate) connection:didReceiveIncomingMessage:].cold.1
- -[_DKSync2Policy initWithDictionary:].cold.1
- -[_DKSync2Policy initWithDictionary:].cold.2
- -[_DKSync2Policy queryStartDateWithSyncType:lastSyncDate:lastDaySyncCount:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _createPushConnection].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _createPushConnection].cold.2
- -[_DKSyncCloudKitKnowledgeStorage _createPushConnection].cold.3
- -[_DKSyncCloudKitKnowledgeStorage _createPushConnection].cold.4
- -[_DKSyncCloudKitKnowledgeStorage _handleAnySpecialnessWithOperationError:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _previousServerChangeTokenForRecordZoneID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _queueOperationForPrivateCloudDatabase:dependent:policy:error:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _queueOperationForPrivateCloudDatabase:dependent:policy:error:].cold.2
- -[_DKSyncCloudKitKnowledgeStorage _queueOperationForPrivateCloudDatabase:dependent:policy:error:].cold.3
- -[_DKSyncCloudKitKnowledgeStorage _registerDatabaseChangesSubscription].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _resetPreviousServerChangeTokenForRecordZoneID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _setPreviousServerChangeToken:forRecordZoneID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _storeZoneIDFromRecords:orError:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage _storeZoneIDFromRecords:orError:].cold.2
- -[_DKSyncCloudKitKnowledgeStorage addSourceDeviceIdentifierWithRecordZoneID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage commitFetchDatabaseChangesServerChangeToken].cold.1
- -[_DKSyncCloudKitKnowledgeStorage commitFetchDatabaseChangesServerChangeToken].cold.2
- -[_DKSyncCloudKitKnowledgeStorage commitFetchDatabaseChangesServerChangeToken].cold.3
- -[_DKSyncCloudKitKnowledgeStorage configureCloudPseudoPeerWithMySyncZoneID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage fastForwardPastDeletionsInNewZone:sourceDeviceID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage fastForwardPastDeletionsInNewZone:sourceDeviceID:].cold.2
- -[_DKSyncCloudKitKnowledgeStorage finishStartOrError:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage removeSourceDeviceIdentifierWithRecordZoneID:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage runUpdateSourceDeviceIdentifiersPeriodicJobWithCompletion:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage setHasZoneAdditionChanges:forZone:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage setHasZoneDeletionChanges:forZone:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage setPrewarmedFlag].cold.1
- -[_DKSyncCloudKitKnowledgeStorage unregisterUpdateSourceDeviceIdentifiersPeriodicJob].cold.1
- -[_DKSyncCloudKitKnowledgeStorage updateSourceDeviceIdentifiersWithRecordZonesByZoneID:completion:].cold.1
- -[_DKSyncCloudKitKnowledgeStorage updateSourceDeviceIdentifiersWithRecordZonesByZoneID:completion:].cold.2
- -[_DKSyncPeerStatusTracker registerNewPeer:].cold.1
- -[_DKSyncRapportCommonStorage clientForPeer:].cold.1
- -[_DKSyncRapportCommonStorage handleAvailabilityFailureWithPeer:completion:].cold.1
- -[_DKSyncRapportCommonStorage handleAvailabilityFailureWithPeer:completion:].cold.2
- -[_DKSyncRapportCommonStorage handleAvailabilityFailureWithPeer:completion:].cold.3
- -[_DKSyncRapportCommonStorage handleAvailabilityFailureWithPeer:completion:].cold.4
- -[_DKSyncRapportCommonStorage removeClient:forPeer:retiring:].cold.1
- -[_DKSyncRapportCommonStorage removeClient:forPeer:retiring:].cold.2
- -[_DKSyncRapportCommonStorage sendRequestID:request:peer:highPriority:options:responseHandler:].cold.1
- -[_DKSyncRapportCommonStorage sendRequestID:request:peer:highPriority:options:responseHandler:].cold.2
- -[_DKSyncRapportCommonStorage sendRequestID:request:peer:highPriority:options:responseHandler:].cold.3
- -[_DKSyncRapportCommonStorage startRapport].cold.1
- -[_DKSyncRapportCommonStorage startRapport].cold.2
- -[_DKSyncRapportCommonStorage startRapport].cold.3
- -[_DKSyncRapportKnowledgeStorage changeSetFromCompressedData:deviceIdentifier:sequenceNumber:].cold.1
- -[_DKSyncedFeatures _fetchScreenTimeSyncState].cold.1
- GCC_except_table106
- GCC_except_table121
- GCC_except_table126
- GCC_except_table127
- GCC_except_table128
- GCC_except_table131
- GCC_except_table164
- GCC_except_table199
- GCC_except_table212
- GCC_except_table214
- GCC_except_table216
- GCC_except_table217
- GCC_except_table233
- GCC_except_table239
- GCC_except_table256
- GCC_except_table261
- GCC_except_table263
- GCC_except_table296
- GCC_except_table298
- GCC_except_table309
- GCC_except_table40
- GCC_except_table60
- GCC_except_table88
- GCC_except_table91
- GCC_except_table94
- OBJC_IVAR_$__CDInteractionsStatisticsConfig._shouldSortAscending
- OBJC_IVAR_$__CDInteractionsStatisticsConfig._statsDefaultValues
- OBJC_IVAR_$__CDTemporalInteractionAdvisor._dataQueue
- OBJC_IVAR_$__CDTemporalInteractionAdvisor._settingsNotifyToken
- _OBJC_CLASS_$__CDDiagnosticDataReporter
- _OBJC_METACLASS_$__CDDiagnosticDataReporter
- __100-[_CDInteractionStore queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:]_block_invoke.327
- __103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke.229
- __103-[_CDInteractionStore createInteractionRecord:context:keywordCache:attachmentCache:contactCache:error:]_block_invoke.231
- __104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.500
- __104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.504
- __104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke_2.505
- __113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.672
- __113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.680
- __31-[_CDInteractionCache _refetch]_block_invoke.206
- __31-[_CDInteractionCache _refetch]_block_invoke.206.cold.1
- __35-[_CDInteractionStoreNotifier init]_block_invoke.29
- __38-[_CDSpotlightEventIndexer resetIndex]_block_invoke.cold.1
- __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.624
- __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.629
- __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.656
- __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.667
- __38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.660
- __40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.706
- __41+[_CDSiriLearningSettings sharedInstance]_block_invoke.cold.1
- __41+[_CDSiriLearningSettings sharedInstance]_block_invoke.cold.2
- __41-[_CDInteractionStore metadataDictionary]_block_invoke.434
- __42-[_DKSync2Coordinator _performPeriodicJob]_block_invoke.cold.1
- __42-[_DKSync2Coordinator _performPeriodicJob]_block_invoke.cold.2
- __43-[_CDSharedMemoryKeyValueStore dataForKey:]_block_invoke.cold.1
- __44-[_CDSpotlightItemRecorder submitOperation:]_block_invoke.705
- __47-[_DKKnowledgeStorage migrationStreamsWithMOC:]_block_invoke.677
- __49-[_CDInteractionsStatistics descriptionRedacted:]_block_invoke.141
- __49-[_DKCoreDataStorage copyStorageFor:toDirectory:]_block_invoke.cold.1
- __49-[_DKSync2Coordinator _runTriggeredSyncActivity:]_block_invoke.cold.1
- __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.250
- __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.286
- __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.286.cold.1
- __53-[_CDInteractionStore recordInteractionsBatch:error:]_block_invoke.286.cold.2
- __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.756
- __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.756.cold.1
- __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.756.cold.2
- __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.756.cold.3
- __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.756.cold.4
- __55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.756.cold.5
- __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.802
- __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.807
- __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.805
- __56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.808
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731.cold.1
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731.cold.2
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731.cold.3
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731.cold.4
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731.cold.5
- __56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.731.cold.6
- __58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.378
- __58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.384
- __58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.cold.1
- __58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke.cold.2
- __60-[_CDSpotlightCoalescedDeletionManager setupCoalescingTimer]_block_invoke.11
- __60-[_CDSpotlightCoalescedDeletionManager setupCoalescingTimer]_block_invoke.12
- __63-[_DKKnowledgeStorage _sendEventsNotificationName:withObjects:]_block_invoke.567
- __64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.140
- __64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.142
- __64-[_CDSiriLearningSettings _startWithCallback:invokeCallbackNow:]_block_invoke.146
- __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.681
- __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.689
- __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.697
- __65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke_2.685
- __66-[_CDSocialInteractionAdvisor tuneUsingSettings:heartBeatHandler:]_block_invoke.161
- __66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.790
- __66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.790.cold.1
- __66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.702
- __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke.679
- __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke.687
- __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke.696
- __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke_2.683
- __68-[_DKBiomeQuery _publisherForQueryReturningIndividualResults:error:]_block_invoke_2.690
- __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.505
- __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.505.cold.1
- __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.509
- __68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.509.cold.1
- __70-[_CDSpotlightItemRecorder _addOrUpdateCoreDuetInteractions:bundleID:]_block_invoke.707
- __73-[_CDInteractionsStatistics computePASSFeatureWithPeopleDetectedInPhoto:]_block_invoke.155
- __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.786
- __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.788
- __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.789
- __74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.cold.1
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.12
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.15
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.17
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.22
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.24
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.25
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.25.cold.1
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke_2.18
- __75-[_CDSocialInteractionAdvisor rankContacts:withSeedContacts:usingSettings:]_block_invoke.147
- __78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.758
- __78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.772
- __78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.775
- __78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.cold.1
- __79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.776
- __87-[_CDSocialInteractionAdvisor adviseInteractionsForDate:andSeedContacts:usingSettings:]_block_invoke.156
- __93-[_CDSpotlightCoalescedDeletionOperation enumerateDeletionPredicatesAndCompletionsWithBlock:]_block_invoke.121
- __95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.798
- __95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.801
- __95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.801.cold.1
- __CDCollectDonationMetricsForEventsInDomain
- __OBJC_$_CLASS_METHODS__CDDiagnosticDataReporter
- __OBJC_CLASS_RO_$__CDDiagnosticDataReporter
- __OBJC_METACLASS_RO_$__CDDiagnosticDataReporter
- ___47-[_CDTemporalInteractionAdvisor initWithStore:]_block_invoke
- ___55-[_CDTemporalInteractionAdvisor setConsumerToModelMap:]_block_invoke
- ___58-[_CDInteractionStore getInteractionsStatisticsForConfig:]_block_invoke_3
- ___66-[_CDSpotlightItemRecorder deleteAllItemsWithBundleID:completion:]_block_invoke
- ___block_descriptor_40_e8_32s_e20_B16?0"_CDContact"8l
- ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_56_e8_32s40s48r_e22_v16?0"BMStoreEvent"8l
- ___block_descriptor_80_e8_32s40s48s56r64r_e21_v24?0"NSArray"8^B16l
- __block_literal_global.102
- __block_literal_global.11
- __block_literal_global.128
- __block_literal_global.138
- __block_literal_global.158
- __block_literal_global.165
- __block_literal_global.178
- __block_literal_global.181
- __block_literal_global.183
- __block_literal_global.185
- __block_literal_global.187
- __block_literal_global.189
- __block_literal_global.191
- __block_literal_global.193
- __block_literal_global.195
- __block_literal_global.197
- __block_literal_global.199
- __block_literal_global.201
- __block_literal_global.203
- __block_literal_global.204
- __block_literal_global.205
- __block_literal_global.207
- __block_literal_global.209
- __block_literal_global.211
- __block_literal_global.215
- __block_literal_global.217
- __block_literal_global.22
- __block_literal_global.234
- __block_literal_global.29
- __block_literal_global.31
- __block_literal_global.386
- __block_literal_global.437
- __block_literal_global.458
- __block_literal_global.508
- __block_literal_global.561
- __block_literal_global.624
- __block_literal_global.632
- __block_literal_global.635
- __block_literal_global.659
- __block_literal_global.675
- __block_literal_global.678
- __block_literal_global.680
- __block_literal_global.682
- __block_literal_global.683
- __block_literal_global.684
- __block_literal_global.692
- __block_literal_global.699
- __block_literal_global.713
- __block_literal_global.731
- __block_literal_global.736
- __block_literal_global.743
- __block_literal_global.757
- __block_literal_global.791
- __block_literal_global.9
- __block_literal_global.931
- _additionalFlagsForInternal.flag
- _additionalFlagsForInternal.onceToken
- _fmodf
- _handleAnySpecialnessWithOperationError:.unrecoverableDecryptionErrorCounter
- _handleAnySpecialnessWithOperationError:.unrecoverableDecryptionErrorCounterInitialized
- _handleAnySpecialnessWithOperationError:.unrecoverableDecryptionErrorRepeatCounter
- _internPool._pasOnceToken5
- _ldexp
- _objc_msgSend$addValue:forScalarKey:
- _objc_msgSend$aggdKeyForAdviceSource:
- _objc_msgSend$aggdKeyForPresentationStyle:
- _objc_msgSend$dataQueue
- _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldSortAscending:shouldUseSuggestionEngaged:statsDefaultValues:
- _objc_msgSend$interactionsSelectionPredicateBetweenStartDate:andEndDate:
- _objc_msgSend$laplaceProbabilityCorrected:withAlpha:resultFeatureName:
- _objc_msgSend$longValue
- _objc_msgSend$publisherWithUseCase:
- _objc_msgSend$pushValue:forDistributionKey:
- _objc_msgSend$setDataQueue:
- _objc_msgSend$shouldStopRecordProcessing:
- _objc_msgSend$updateConsumerModel
- _objc_msgSend$updateConsumerModelSettings:
- _syncCoordinatorDidCreateChangeSetOfType:.syncCounter
- _syncCoordinatorDidCreateChangeSetOfType:.syncCounterInitialized
- computationBlockForStatName:._pasOnceToken2
- dk_localtimeString.formatter
- dk_localtimeString.initialized
- isDateInWeekend:._pasOnceToken3
- isSiriPortraitDisabled.initialized
- isSiriPortraitDisabled.previousResult
- knowledgeStorage:didInsertEventsWithStreamNameCounts:.ingestCounter
- knowledgeStorage:didInsertEventsWithStreamNameCounts:.ingestCounterInitialized
- knowledgeStorage:didInsertLocalEventsWithStreamNameCounts:.ingestCounterInitialized
- knowledgeStorage:didInsertLocalEventsWithStreamNameCounts:.ingestLocalCounter
- mediaAnalysisChannel._pasOnceToken52
- notificationQueue.onceToken
- notificationQueue.queue
- portraitStreamNames.initialized
- portraitStreamNames.portraitStreamNames
- sharedInstance._pasOnceToken5
- sharedInstance._pasOnceToken6
- streamNamesNotificationWhitelist.initialized
- streamNamesNotificationWhitelist.streamNamesNotificationWhitelist
- syncCoordinator:didAddRemoteEventsWithStreamNameCounts:events:.additionSyncLatencyTimerCounter
- syncCoordinator:didAddRemoteEventsWithStreamNameCounts:events:.syncCounter
- syncCoordinator:didAddRemoteEventsWithStreamNameCounts:events:.syncCounterInitialized
- syncCoordinator:didDeleteRemoteEventsWithCount:.syncCounter
- syncCoordinator:didDeleteRemoteEventsWithCount:.syncCounterInitialized
- syncCoordinator:didInsertLocalAdditionEventsWithStreamNameCounts:.syncCounter
- syncCoordinator:didInsertLocalAdditionEventsWithStreamNameCounts:.syncCounterInitialized
- typeValueWithStreamName:.initialized
- typeValueWithStreamName:.typeValueByStreamName
- updateToFinalMetadata:.metadataRemoval
- updateToFinalMetadata:.metadataTranslation
- updateToFinalMetadata:.onceToken
CStrings:
+ "%.2f"
+ "%{public}s expected %{public}s, got %{public}@, ignoring assignment: %{sensitive}@"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:550"
+ "/System/AppleInternal/Library/Frameworks/AssistantServices.framework/AssistantServices"
+ "/System/AppleInternal/Library/Frameworks/BiomeStorage.framework/BiomeStorage"
+ "/System/AppleInternal/Library/Frameworks/BiomeStreams.framework/BiomeStreams"
+ "/System/AppleInternal/Library/Frameworks/Contacts.framework/Contacts"
+ "/System/AppleInternal/Library/Frameworks/CoreDuetContext.framework/CoreDuetContext"
+ "/System/AppleInternal/Library/Frameworks/CoreServices.framework/CoreServices"
+ "/System/AppleInternal/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight"
+ "/System/AppleInternal/Library/Frameworks/HomeKit.framework/HomeKit"
+ "/System/AppleInternal/Library/Frameworks/PeopleSuggester.framework/PeopleSuggester"
+ "/System/AppleInternal/Library/Frameworks/ProactiveEventTracker.framework/ProactiveEventTracker"
+ "/System/AppleInternal/Library/Frameworks/ScreenTimeCore.framework/ScreenTimeCore"
+ "/System/AppleInternal/Library/Frameworks/SpotlightReceiver.framework/SpotlightReceiver"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"NSString\"16@?0@\"_CDAttachmentRecord\"8"
+ "@16@?0@\"NSString\"8"
+ "@76@0:8@16@24@32Q40d48@56B64@68"
+ "@92@0:8@16@24@32Q40d48@56B64@68@76@84"
+ "B16@?0@\"BMStoreEvent\"8"
+ "B24@?0@\"_CDContact\"8Q16"
+ "B32@?0@\"_CDContact\"8Q16^B24"
+ "C8@?0"
+ "CoreDuet: CDInteractionCache refetch"
+ "CoreDuet: _CDSiriLearningSettings startSanitizingKnowledgeStore"
+ "CoreDuet: addInteractions:bundleID:protectionClass:"
+ "CoreDuet: addOrUpdateSearchableItems:bundleID:"
+ "CoreDuet: addUserAction:withItem:"
+ "CoreDuet: adviseInteractionsForDate"
+ "CoreDuet: adviseInteractionsForKeywordsInString"
+ "CoreDuet: adviseInteractionsUsingSettings"
+ "CoreDuet: adviseSocialInteractionsForDate"
+ "CoreDuet: clientNeedsHelpCallback"
+ "CoreDuet: confirmConnectionWithError"
+ "CoreDuet: countContactsUsingPredicate async"
+ "CoreDuet: countContactsUsingPredicate sync"
+ "CoreDuet: countInteractionsUsingPredicate async"
+ "CoreDuet: countInteractionsUsingPredicate sync"
+ "CoreDuet: deleteAllEventsInEventStream async"
+ "CoreDuet: deleteAllEventsInEventStream sync"
+ "CoreDuet: deleteAllEventsMatchingPredicate async"
+ "CoreDuet: deleteAllEventsMatchingPredicate sync"
+ "CoreDuet: deleteAllInteractionsWithBundleID:protectionClass:"
+ "CoreDuet: deleteAllSearchableItemsWithBundleID:"
+ "CoreDuet: deleteAllUserActivities:"
+ "CoreDuet: deleteInteractionsMatchingPredicate async"
+ "CoreDuet: deleteInteractionsMatchingPredicate sync"
+ "CoreDuet: deleteInteractionsWithBundleId account async"
+ "CoreDuet: deleteInteractionsWithBundleId async"
+ "CoreDuet: deleteInteractionsWithBundleId domainIdentifier async"
+ "CoreDuet: deleteInteractionsWithBundleId domainIdentifiers async"
+ "CoreDuet: deleteInteractionsWithBundleId domainIdentifiers dispatch"
+ "CoreDuet: deleteInteractionsWithBundleId sync"
+ "CoreDuet: deleteInteractionsWithGroupIdentifiers:bundleID:protectionClass:"
+ "CoreDuet: deleteInteractionsWithIdentifiers:bundleID:protectionClass:"
+ "CoreDuet: deleteObjects async"
+ "CoreDuet: deleteObjects sync"
+ "CoreDuet: deleteRemoteState"
+ "CoreDuet: deleteSearchableItemsSinceDate:bundleID:"
+ "CoreDuet: deleteSearchableItemsWithDomainIdentifiers:bundleID:"
+ "CoreDuet: deleteSearchableItemsWithIdentifiers:bundleID:"
+ "CoreDuet: deleteUserActivitiesWithPersistentIdentifiers:bundleID:"
+ "CoreDuet: deviceActivityLikelihood"
+ "CoreDuet: deviceActivityLikelihoodQueryPredicate"
+ "CoreDuet: deviceUUID"
+ "CoreDuet: disableSyncPolicy"
+ "CoreDuet: displayOnLikelihood"
+ "CoreDuet: donateRelevantShortcuts:bundleID:"
+ "CoreDuet: executeQuery async"
+ "CoreDuet: executeQuery async no completion"
+ "CoreDuet: executeQuery sync"
+ "CoreDuet: expectedInBedPeriod"
+ "CoreDuet: isSyncPolicyDisabled"
+ "CoreDuet: launchLikelihoodForTopNApplications"
+ "CoreDuet: launchLikelihoodPredictionForApp"
+ "CoreDuet: localInBedPeriod"
+ "CoreDuet: pluginLikelihood"
+ "CoreDuet: predictionForStreamsWithNames"
+ "CoreDuet: queryContactsUsingPredicate async"
+ "CoreDuet: queryContactsUsingPredicate sync"
+ "CoreDuet: queryInteractionsUsingPredicate async"
+ "CoreDuet: queryInteractionsUsingPredicate sync"
+ "CoreDuet: rankCandidateContacts"
+ "CoreDuet: recordInteractions async"
+ "CoreDuet: recordInteractions sync"
+ "CoreDuet: saveObjects async"
+ "CoreDuet: saveObjects sync"
+ "CoreDuet: sourceDeviceIdentityFromObject"
+ "CoreDuet: suggestPeople async"
+ "CoreDuet: suggestPeople sync"
+ "CoreDuet: synchronizeWithError"
+ "CoreDuet: synchronizeWithUrgency"
+ "CoreDuet: synchronizeWithUrgency async"
+ "CoreDuet: tuneSocialAdvisorUsingSettings"
+ "Deleting searchable items with bundleID: %{public}@"
+ "DeprecatedAPI"
+ "Ignoring call to delete all searchable items for %{public}@ (File provider bundle ID)"
+ "Ignoring call to delete all searchable items for %{public}@ (Messages bundle ID)"
+ "Interaction store ignoring call to delete all searchable items for %{public}@ (disallowed bundle ID)"
+ "Interaction store ignoring call to delete domain identifiers for %{public}@ (disallowed bundle ID)"
+ "Interaction store ignoring call to delete searchable items by ID for %{public}@ (disallowed bundle ID)"
+ "Recording interaction: %{sensitive}@"
+ "T@\"NSArray\",&,N,V_featureNamesToSortWith"
+ "T@\"NSArray\",&,N,V_statsToCompute"
+ "T@\"NSDate\",R,N,V_anchorDate"
+ "T@\"NSDate\",R,N,V_leftBoundDate"
+ "T@\"NSDate\",R,N,V_rightBoundDate"
+ "T@\"NSDictionary\",&,N,V_appToAppExtMapping"
+ "T@\"NSDictionary\",&,N,V_consumerToModelMap"
+ "T@\"NSDictionary\",R,N,V_defaultValues"
+ "T@\"NSSet\",&,N,V_peopleInPhotoIdentifiers"
+ "T@\"NSSet\",&,N,V_scenesInPhotoIdentifiers"
+ "TB,R,N,V_shouldUseSuggestionEngaged"
+ "TQ,N,V_fetchLimit"
+ "Td,R,N,V_maxComputationTime"
+ "TimeSinceLastUIEngagement"
+ "_CDInteractionsStatistics: union of shared people sets had cardinality zero"
+ "_CDInteractionsStatisticsConfig: record returned nil conversationId"
+ "_CDInteractionsStatisticsConfig: skipping %@ –\u00a0computation block was nil"
+ "_appToAppExtMapping"
+ "_appsSharedFromByConversationId"
+ "_handoffCurrentReplyToQueue:block:"
+ "_iterInteractionRecordsWithPredicate"
+ "_iterInteractionRecordsWithPredicate: finished processing interactions, fetchLimit %tu object(s), elapsed %f(sec), found %tu object(s), processed %tu object(s) (%tu were skipped due to timeout)"
+ "_iterInteractionRecordsWithPredicate: query error: %@"
+ "_iterInteractionRecordsWithPredicate: query exception: %@"
+ "_iterInteractionRecordsWithPredicate:fetchLimit:batchSize:updateTelemetry:withBlock:"
+ "_pas_filteredArrayWithIndexedTest:"
+ "_pas_mappedSetWithTransform:"
+ "_personsSharedInPastPhotos"
+ "_scenesBasedFeatures"
+ "_scenesInPhotoIdentifiers"
+ "_scenesMinimumNumberOfTags"
+ "_shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:"
+ "_shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:"
+ "_waitingForDB"
+ "admission"
+ "aggregateSum:"
+ "aggregateSum:resultFeatureName:"
+ "anchorDate"
+ "api=%{signpost.telemetry:string1,public}s client=%{signpost.telemetry:string2,public}s  enableTelemetry=YES "
+ "appToAppExtMapping"
+ "autosu"
+ "com.apple."
+ "com.apple.mobileslideshow"
+ "communicationInteractionPredicate"
+ "communicationInteractions.%@"
+ "computeCandidateLevelSignals"
+ "computeNumberOfAppsSharedFromWithConversation"
+ "computeNumberOfEngagedSuggestionsToTargetApp"
+ "computeNumberOfFacesSharedWithConversation"
+ "computeNumberOfSharesToTargetApp"
+ "computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:"
+ "conditioned_%@"
+ "dataCollection"
+ "disallowedCSSIBundleIds"
+ "dkpredictor"
+ "fetchTimeInMillis"
+ "getInteractionsStatisticsForConfig: processing communication interactions"
+ "getInteractionsStatisticsForConfig: processing sharing interactions"
+ "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:"
+ "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "instrumentation"
+ "isFirstPartyApp"
+ "leftBoundDate"
+ "lowPriorityWorkCanContinue"
+ "maxComputationTime"
+ "notifier"
+ "numberOfAppsSharedFromWithConversation"
+ "numberOfDifferentFacesSharedWithConversation"
+ "numberOfEngagedSuggestionsToTargetApp"
+ "numberOfRecentOutgoingInteractionsWithConversation"
+ "numberOfSharesOfDetectedScenesWithConversation"
+ "numberOfSharesOfPeopleInPhotoIoUWithConversation"
+ "numberOfSharesOfScenesInPhotoWithConversation"
+ "numberOfTotalSharesToTargetApp"
+ "peopleInPhotoIdentifiers"
+ "pid:%d"
+ "processingTimeInMillis"
+ "publisherWithUseCase:options:"
+ "recordCount"
+ "reportShareSheetTimeoutWithReply:"
+ "runHighPriorityDBBlock:"
+ "runLowPriorityDBPreemptableBlock:"
+ "saveAppSharedFrom:forConversationId:"
+ "savePersonsInPhoto:forConversationId:"
+ "scenesBasedFeatures"
+ "scenesBasedFeaturesNames"
+ "scenesInPhotoIdentifiers"
+ "setAppToAppExtMapping:"
+ "setScenesInPhotoIdentifiers:"
+ "sharingInteractionPredicate"
+ "sharingInteractions.%@"
+ "shouldContinue"
+ "spotlightReceiver"
+ "statsToCompute"
+ "sum:withAddend:"
+ "sum:withAddend:resultFeatureName:"
+ "timeSinceLastPhoneCallWithConversation"
+ "timeSinceLastPhotoShareWithConversation"
+ "timeSinceLastShareWithConversation"
+ "topLevelScenesFromSceneNetTags:"
+ "v24@?0@\"NSString\"8@\"NSString\"16"
+ "v28@?0@\"_CDInteractionRecord\"8i16^B20"
+ "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
+ "v56@0:8@16Q24Q32@?40@?48"
- "%@.averageImageBytes"
- "%@.deleting"
- "%@.deleting.%@"
- "%@.donationHasImage"
- "%@.donations"
- "%@.recording"
- "%@.recording.%@"
- "%@.source.%@.%@"
- "%@.userAction"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:579"
- "@80@0:8@16@24@32Q40d48@56B64B68@72"
- "B16@?0@\"_CDContact\"8"
- "Deleting searchable items with bundleID: %@"
- "Duet: CDInteractionCache refetch"
- "Duet: _CDSiriLearningSettings startSanitizingKnowledgeStore"
- "Duet: addInteractions:bundleID:protectionClass:"
- "Duet: addOrUpdateSearchableItems:bundleID:"
- "Duet: addUserAction:withItem:"
- "Duet: adviseInteractionsForDate"
- "Duet: adviseInteractionsForKeywordsInString"
- "Duet: adviseInteractionsUsingSettings"
- "Duet: adviseSocialInteractionsForDate"
- "Duet: clientNeedsHelpCallback"
- "Duet: confirmConnectionWithError"
- "Duet: countContactsUsingPredicate async"
- "Duet: countContactsUsingPredicate sync"
- "Duet: countInteractionsUsingPredicate async"
- "Duet: countInteractionsUsingPredicate sync"
- "Duet: deleteAllEventsInEventStream async"
- "Duet: deleteAllEventsInEventStream sync"
- "Duet: deleteAllEventsMatchingPredicate async"
- "Duet: deleteAllEventsMatchingPredicate sync"
- "Duet: deleteAllInteractionsWithBundleID:protectionClass:"
- "Duet: deleteAllSearchableItemsWithBundleID:"
- "Duet: deleteAllUserActivities:"
- "Duet: deleteInteractionsMatchingPredicate async"
- "Duet: deleteInteractionsMatchingPredicate sync"
- "Duet: deleteInteractionsWithBundleId account async"
- "Duet: deleteInteractionsWithBundleId async"
- "Duet: deleteInteractionsWithBundleId domainIdentifier async"
- "Duet: deleteInteractionsWithBundleId domainIdentifiers async"
- "Duet: deleteInteractionsWithBundleId domainIdentifiers dispatch"
- "Duet: deleteInteractionsWithBundleId sync"
- "Duet: deleteInteractionsWithGroupIdentifiers:bundleID:protectionClass:"
- "Duet: deleteInteractionsWithIdentifiers:bundleID:protectionClass:"
- "Duet: deleteObjects async"
- "Duet: deleteObjects sync"
- "Duet: deleteRemoteState"
- "Duet: deleteSearchableItemsSinceDate:bundleID:"
- "Duet: deleteSearchableItemsWithDomainIdentifiers:bundleID:"
- "Duet: deleteSearchableItemsWithIdentifiers:bundleID:"
- "Duet: deleteUserActivitiesWithPersistentIdentifiers:bundleID:"
- "Duet: deviceActivityLikelihood"
- "Duet: deviceActivityLikelihoodQueryPredicate"
- "Duet: deviceUUID"
- "Duet: disableSyncPolicy"
- "Duet: displayOnLikelihood"
- "Duet: donateRelevantShortcuts:bundleID:"
- "Duet: executeQuery async"
- "Duet: executeQuery async no completion"
- "Duet: executeQuery sync"
- "Duet: expectedInBedPeriod"
- "Duet: isSyncPolicyDisabled"
- "Duet: launchLikelihoodForTopNApplications"
- "Duet: launchLikelihoodPredictionForApp"
- "Duet: localInBedPeriod"
- "Duet: pluginLikelihood"
- "Duet: predictionForStreamsWithNames"
- "Duet: queryContactsUsingPredicate async"
- "Duet: queryContactsUsingPredicate sync"
- "Duet: queryInteractionsUsingPredicate async"
- "Duet: queryInteractionsUsingPredicate sync"
- "Duet: rankCandidateContacts"
- "Duet: recordInteractions async"
- "Duet: recordInteractions sync"
- "Duet: saveObjects async"
- "Duet: saveObjects sync"
- "Duet: sourceDeviceIdentityFromObject"
- "Duet: suggestPeople async"
- "Duet: suggestPeople sync"
- "Duet: synchronizeWithError"
- "Duet: synchronizeWithUrgency"
- "Duet: synchronizeWithUrgency async"
- "Duet: tuneSocialAdvisorUsingSettings"
- "Ignoring call to delete all searchable items for %@"
- "OriginShareBundleId"
- "Recording iteraction: %{sensitive}@"
- "T@\"NSMutableDictionary\",&,N,V_consumerToModelMap"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dataQueue"
- "Ti,V_settingsNotifyToken"
- "Updating model parameters: %@"
- "_CDDiagnosticDataReporter"
- "_dataQueue"
- "_shouldSortAscending"
- "_statsDefaultValues"
- "addValue:forScalarKey:"
- "aggdKeyForAdviceSource:"
- "aggdKeyForPresentationStyle:"
- "autoComplete"
- "clearDistributionKey:"
- "clearScalarKey:"
- "com.apple.coreduet.admissionCheck"
- "com.apple.coreduet.autosu"
- "com.apple.coreduet.cdtemporalAdvisor.serialqueue"
- "com.apple.coreduet.context"
- "com.apple.coreduet.coreData.failedToLoadMOM"
- "com.apple.coreduet.coreData.failedToMigrateDB"
- "com.apple.coreduet.dataCollection"
- "com.apple.coreduet.deletedDB.couldNotOpen"
- "com.apple.coreduet.dkpredictor"
- "com.apple.coreduet.inBedDetector"
- "com.apple.coreduet.instrumentation"
- "com.apple.coreduet.interactionAdvisor.feedback"
- "com.apple.coreduet.knowledge.sync"
- "com.apple.coreduet.knowledgeStore.privacyEventsDeleted"
- "com.apple.coreduet.peoplePrediction.quickAction.Messages"
- "com.apple.coreduet.peoplePrediction.quickAction.Phone"
- "com.apple.coreduet.peoplePrediction.shareSheet"
- "com.apple.coreduet.receiver.notifier"
- "com.apple.coreduet.sleepSPIforAutoSU.eventStreamStateFailure"
- "com.apple.coreduet.sleepSPIforAutoSU.insufficientInterval"
- "com.apple.coreduet.sleepSPIforAutoSU.planFailed"
- "com.apple.coreduet.sleepSPIforAutoSU.suEndTruncated"
- "com.apple.coreduet.sleepSPIforAutoSU.suStartTruncated"
- "com.apple.coreduet.sleepSPIforAutoSU.totalCount"
- "com.apple.coreduet.sleepSPIforAutoSU.totalDefaultTimes"
- "com.apple.coreduet.sleepSPIforAutoSU.totalNonDefaultTimes"
- "com.apple.coreduet.spotlightReceiver"
- "com.apple.coreduet.spotlightreceiver"
- "coreduet"
- "dataQueue"
- "favorites"
- "getConversationIdAndComputeStatForStatName:record:inInteractionsStatistics:"
- "getInteractionsStatisticsForConfig"
- "getInteractionsStatisticsForConfig processing"
- "getInteractionsStatisticsForConfig: finished executeFetchRequest, fetchLimit %tu object(s), elapsed %f(sec), found %tu object(s)"
- "getInteractionsStatisticsForConfig: finished processing, fetchLimit %tu object(s), elapsed %f(sec), found %tu object(s), processed %tu object(s) (%tu were skipped due to timeout)"
- "getInteractionsStatisticsForConfig: query error: %@"
- "getInteractionsStatisticsForConfig: query exception: %@"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldSortAscending:shouldUseSuggestionEngaged:statsDefaultValues:"
- "interactionStoreQueryTimeInMillis"
- "interactionsSelectionPredicateBetweenStartDate:andEndDate:"
- "laplaceProbabilityCorrected:withAlpha:"
- "laplaceProbabilityCorrected:withAlpha:resultFeatureName:"
- "longValue"
- "managedResult.count"
- "nextPerson"
- "other"
- "publisherWithUseCase:"
- "pushValue:forDistributionKey:"
- "quickAction"
- "relevantShortcuts"
- "request.fetchBatchSize"
- "request.fetchLimit"
- "request.predicate"
- "setDataQueue:"
- "setSettingsNotifyToken:"
- "setShouldSortAscending:"
- "setValue:forDistributionKey:"
- "setValue:forScalarKey:"
- "setValue:forScalarKey:limitingSigDigs:"
- "settingsNotifyToken"
- "shouldStopRecordProcessing:"
- "timeSinceOutgoingInteractionNumber10"
- "updateConsumerModel"
- "updateConsumerModelSettings:"
- "v32@0:8d16@24"
- "v40@0:8q16@24Q32"

```
