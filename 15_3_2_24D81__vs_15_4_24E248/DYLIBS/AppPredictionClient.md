## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/Versions/A/AppPredictionClient`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x18e594
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_methlist: 0x15ea0
+588.11.0.0.0
+  __TEXT.__text: 0x1901cc
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x17334
   __TEXT.__const: 0x6f0
-  __TEXT.__cstring: 0x19dec
-  __TEXT.__oslogstring: 0x15923
-  __TEXT.__gcc_except_tab: 0x20ac
+  __TEXT.__cstring: 0x19fe8
+  __TEXT.__oslogstring: 0x15bcb
+  __TEXT.__gcc_except_tab: 0x20a0
   __TEXT.__dlopen_cstrs: 0x26f
   __TEXT.__ustring: 0x18a
-  __TEXT.__unwind_info: 0x5f68
+  __TEXT.__unwind_info: 0x5fd0
   __TEXT.__objc_classname: 0x3754
-  __TEXT.__objc_methname: 0x30765
-  __TEXT.__objc_methtype: 0x63a5
-  __TEXT.__objc_stubs: 0x1a940
+  __TEXT.__objc_methname: 0x30920
+  __TEXT.__objc_methtype: 0x63a8
+  __TEXT.__objc_stubs: 0x1aa60
   __DATA_CONST.__got: 0x1600
-  __DATA_CONST.__const: 0x2ec8
+  __DATA_CONST.__const: 0x2ee8
   __DATA_CONST.__objc_classlist: 0xd20
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9270
+  __DATA_CONST.__objc_selrefs: 0x9418
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0xb68
   __DATA_CONST.__objc_arraydata: 0xac8
-  __AUTH_CONST.__auth_got: 0x670
-  __AUTH_CONST.__const: 0x5c10
-  __AUTH_CONST.__cfstring: 0x13e20
-  __AUTH_CONST.__objc_const: 0x44278
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0x5c50
+  __AUTH_CONST.__cfstring: 0x13e80
+  __AUTH_CONST.__objc_const: 0x41e98
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0x660
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x8340
-  __DATA.__objc_ivar: 0x1adc
+  __DATA.__objc_ivar: 0x1ae4
   __DATA.__data: 0x1b08
-  __DATA.__bss: 0x550
+  __DATA.__bss: 0x560
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 76AA2570-C7C7-3979-AA1F-811B25D9EE62
-  Functions: 9951
-  Symbols:   22665
-  CStrings:  14962
+  UUID: DE65925B-1E2B-3D15-8244-ED469AA7C935
+  Functions: 10090
+  Symbols:   22897
+  CStrings:  14996
 
Symbols:
+ +[ATXABHelper abGroupForConsumerSubType:].cold.1
+ +[ATXAction getDateFromUserActivityString:forActionKey:].cold.1
+ +[ATXAction getDateFromUserActivityString:forActionKey:].cold.2
+ +[ATXAction(Factory) atx_setAlarmActionWithTitle:subtitle:eventIdentifier:eventTitle:alarmDate:heuristicName:].cold.3
+ +[ATXAction(Factory) atx_updateAlarmActionWithTitle:subtitle:alarmID:alarmTitle:heuristicName:].cold.3
+ +[ATXActionSearchResult _recentDonationProactiveSuggestionFromScoredAction:withClientModelId:].cold.1
+ +[ATXActivitySuggestionClient sharedInstance].cold.1
+ +[ATXAppDirectoryClient sharedInstance].cold.1
+ +[ATXAppPredictorAssetMapping sharedInstanceWithMobileAssets].cold.1
+ +[ATXAssets2 onUpdateRestartThisProcess].cold.1
+ +[ATXAssetsAggregateLogger logKey:replaceScalarValueWith:].cold.1
+ +[ATXBatteryDrainBehavior sharedInstance].cold.1
+ +[ATXClientDuetHelper sharedInstance].cold.1
+ +[ATXDNDModeConfigurationClient sharedInstance].cold.1
+ +[ATXDefaultHomeScreenItemManager isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:]
+ +[ATXDefaultHomeScreenItemManager sharedInstance].cold.1
+ +[ATXDeviceClass isConstrainedForActions].cold.1
+ +[ATXDigestOnboardingSuggestionClient sharedInstance].cold.1
+ +[ATXEngagementRecordManager sharedInstance].cold.1
+ +[ATXFaceSuggestionClient sharedInstance].cold.1
+ +[ATXInformationStore sharedInstance].cold.1
+ +[ATXIntentGlobals sharedInstance].cold.1
+ +[ATXMetrics _sharedInstance].cold.1
+ +[ATXModeEntityTrialClientWrapper sharedInstance].cold.1
+ +[ATXModeGlobals sharedInstance].cold.1
+ +[ATXNotificationManagementMAConstants sharedInstance].cold.1
+ +[ATXRecentActionEngagementCache sharedInstance].cold.1
+ +[ATXRunningBoardAssertion performWorkWithFinishTaskAssertionName:block:].cold.3
+ +[ATXSportsClient sharedInstance].cold.1
+ +[ATXSpotlightClient _resultWithIntent:title:subtitle:bundleIdForDisplay:appIcon:].cold.1
+ +[ATXSpotlightZKWTrialClientWrapper sharedInstance].cold.1
+ +[ATXWatchFaceConfigurationCollector sharedInstance].cold.1
+ +[ATXWidgetDescriptorCache sharedInstance].cold.1
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.1
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.2
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.3
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.4
+ -[ATXAction initWithActivityProxy:activity:activityString:itemIdentifier:contentAttributeSet:intent:actionUUID:bundleId:type:heuristic:heuristicMetadata:criteria:isFutureMedia:routeInfo:title:subtitle:languageCode:cachedHash:].cold.5
+ -[ATXActionCacheClientReader _getLockScreenPredictionIndices:].cold.1
+ -[ATXAppPredictorAssetMapping getAssetFileAndSubscoreForConsumerSubType:].cold.3
+ -[ATXAppPredictorAssetMapping initWithUseMobileAssets:].cold.4
+ -[ATXAssetsABHelper initWithAssetContents:specifiedABGroup:indexForDevice:].cold.4
+ -[ATXClientDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:block:].cold.1
+ -[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:].cold.2
+ -[ATXClientDuetHelper _queryDuetStreamUnbatched:startDate:endDate:otherPredicates:limit:].cold.3
+ -[ATXContactModeEntity initWithDisplayName:rawIdentifier:cnContactId:stableContactIdentifier:].cold.1
+ -[ATXDefaultHomeScreenItemAppLaunchScorer _appLaunchScoreForContactsWidget].cold.1
+ -[ATXDefaultHomeScreenItemAppLaunchScorer _appLaunchScoreForSleepWidget].cold.2
+ -[ATXDefaultHomeScreenItemAppLaunchScorer _appLaunchScoreForSleepWidget].cold.3
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]
+ -[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache].cold.1
+ -[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlay]
+ -[ATXDefaultHomeScreenItemManager _readCarPlayUpdateFromFileWithCompletionHandler:]
+ -[ATXDefaultHomeScreenItemManager initWithHomeScreenPath:ambientPath:carPlayPath:]
+ -[ATXDefaultHomeScreenItemManager writeCarPlayUpdate:completionHandler:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer _carPlayOnboardingStacks]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:]
+ -[ATXDefaultHomeScreenItemOnboardingStacksProducer isCarPlay]
+ -[ATXDefaultHomeScreenItemProducer carPlayOnboardingStacks]
+ -[ATXDefaultHomeScreenItemUpdater _updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:]
+ -[ATXDefaultHomeScreenItemUpdater updateDefaultsDueToCarPlayConfigUpdate]
+ -[ATXFeedbackStateBuilder finish].cold.1
+ -[ATXFeedbackStateBuilder initWithABGroup:assetVersion:].cold.1
+ -[ATXFeedbackStateBuilder recordPrediction:actionHash:totalScore:scoreInputs:isMediumConfidenceForBlendingLayer:isHighConfidenceForBlendingLayer:].cold.2
+ -[ATXFeedbackStateBuilder recordPrediction:actionHash:totalScore:scoreInputs:isMediumConfidenceForBlendingLayer:isHighConfidenceForBlendingLayer:].cold.3
+ -[ATXFeedbackStateReader initWithData:predictedItemKeyClass:].cold.3
+ -[ATXIntentEvent initWithBundleId:intentType:dateInterval:].cold.1
+ -[ATXIntentEvent initWithBundleId:intentType:dateInterval:].cold.2
+ -[ATXLazyIntent initWithIntent:intentData:].cold.1
+ -[ATXNotificationGroupEvent initWithEventType:uuid:eventDate:].cold.1
+ -[ATXNotificationGroupEvent initWithEventType:uuid:eventDate:].cold.2
+ -[ATXNotificationSuggestionInteractionEvent initWithSuggestionType:eventType:suggestionUUID:eventDate:].cold.1
+ -[ATXNotificationSuggestionInteractionEvent initWithSuggestionType:eventType:suggestionUUID:eventDate:].cold.2
+ -[ATXNotificationSuggestionInteractionEvent initWithSuggestionType:eventType:suggestionUUID:eventDate:].cold.3
+ -[ATXNotificationSuggestionInteractionEvent initWithSuggestionType:eventType:suggestionUUID:eventDate:].cold.4
+ -[ATXPredictionSetBuilder finish].cold.1
+ -[ATXPredictionSetBuilder recordPrediction:score:].cold.1
+ -[ATXPredictionSetBuilder recordPrediction:score:].cold.2
+ -[ATXPredictionSetReader initWithData:predictedItemClass:].cold.3
+ -[ATXProactiveSuggestionClient remoteSyncBlendingLayerServer].cold.1
+ -[ATXScoredPrediction initWithPredictedItem:score:].cold.1
+ -[ATXSettingsAction initWithProactiveSuggestion:action:date:navigationLink:].cold.1
+ -[ATXTimeSection initWithRows:title:kind:representedTimeRangeStart:representedTimeRangeEnd:].cold.1
+ -[ATXTimeSectionRow initWithEvents:accessories:dateComponents:isCurrent:prominence:identifier:].cold.1
+ -[ATXTimeSectionRow initWithEvents:accessories:dateComponents:isCurrent:prominence:identifier:].cold.2
+ ATXPBExecutableReferenceCacheReadFrom.cold.1
+ ATXPBExecutableReferenceKeyReadFrom.cold.1
+ ATXPBFaceGalleryConfigurationReadFrom.cold.1
+ ATXPBFaceGalleryEventReadFrom.cold.1
+ ATXPBHomeScreenEventMetadataReadFrom.cold.1
+ ATXPBHomeScreenEventMetadataReadFrom.cold.2
+ ATXSlotSetsSerialize.cold.2
+ ATXSlotSetsSerialize.cold.3
+ ATXSlotSetsSerialize.cold.4
+ GCC_except_table374
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemManager._carPlayPath
+ OBJC_IVAR_$_ATXDefaultHomeScreenItemOnboardingStacksProducer._isCarPlay
+ _OBJC_$_PROP_LIST_ATXActivitySuggestion.68
+ _OBJC_$_PROP_LIST_ATXUserEducationSuggestion.64
+ __100-[ATXNotificationCategorizationClient collectDynamicBreakthroughFeaturesForNotification:completion:]_block_invoke.16
+ __102-[ATXHomeScreenSuggestionClient _updateLoggerStacksToStackSuggestionsFromHomeScreenCachedSuggestions:]_block_invoke.165
+ __104-[ATXDigestSetupFlowClient _helperAppsSortedByNotificationsReceivedInPreviousNumDays:completionHandler:]_block_invoke.7
+ __104-[ATXDigestSetupFlowClient _helperAppsSortedByNotificationsReceivedInPreviousNumDays:completionHandler:]_block_invoke.7.cold.1
+ __104-[ATXInformationStore upcomingDateThatTimelineScoreChangesToOrFromZeroForWidget:kind:familyMask:intent:]_block_invoke.644
+ __104-[ATXInformationStore upcomingDateThatTimelineScoreChangesToOrFromZeroForWidget:kind:familyMask:intent:]_block_invoke.648
+ __104-[ATXInformationStore upcomingDateThatTimelineScoreChangesToOrFromZeroForWidget:kind:familyMask:intent:]_block_invoke.648.cold.1
+ __105-[ATXInformationStore recentRelevantTimelineEntriesOrderedByDescendingScoreForWidget:kind:family:intent:]_block_invoke.654
+ __108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.44
+ __108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.54
+ __108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.57
+ __110-[ATXUserActivityStream _enumerateActivityIntentEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:]_block_invoke.13
+ __112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.37
+ __112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.38
+ __112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.38.cold.1
+ __113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.41
+ __113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.43
+ __113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.32
+ __113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.33
+ __113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.33.cold.1
+ __117-[ATXInformationStore fetchStackConfigStatisticsForWidgetBundleId:widgetKind:containerBundleIdentifier:widgetFamily:]_block_invoke.847
+ __117-[ATXInformationStore fetchStackConfigStatisticsForWidgetBundleId:widgetKind:containerBundleIdentifier:widgetFamily:]_block_invoke.847.cold.1
+ __117-[ATXInformationStore mostRecentRotationRecordForWidget:kind:intent:considerStalenessRotation:filterByClientModelId:]_block_invoke.507
+ __117-[ATXInformationStore mostRecentRotationRecordForWidget:kind:intent:considerStalenessRotation:filterByClientModelId:]_block_invoke.515
+ __117-[ATXInformationStore mostRecentRotationRecordForWidget:kind:intent:considerStalenessRotation:filterByClientModelId:]_block_invoke.515.cold.1
+ __124-[ATXModeEntityScorerClient assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:reply:]_block_invoke.105
+ __125-[ATXModeEntityScorerClient modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:reply:]_block_invoke.101
+ __141-[ATXActionPredictionClient getActionPredictionsForCandidateBundleIdentifiers:candidateActionTypes:consumerType:consumerSubType:limit:reply:]_block_invoke.34
+ __141-[ATXActionPredictionClient getActionPredictionsForCandidateBundleIdentifiers:candidateActionTypes:consumerType:consumerSubType:limit:reply:]_block_invoke.34.cold.1
+ __144-[ATXActionPredictionClient getActionPredictionsForContext:includeBundleIds:excludeBundleIds:includeActionTypes:excludeActionTypes:limit:reply:]_block_invoke.54
+ __144-[ATXActionPredictionClient getActionPredictionsForContext:includeBundleIds:excludeBundleIds:includeActionTypes:excludeActionTypes:limit:reply:]_block_invoke.54.cold.1
+ __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.21
+ __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.21.cold.1
+ __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.25
+ __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.25.cold.1
+ __161-[ATXHomeScreenSuggestionClient _replaceSuggestionWithId:fromSuggestionsArray:suggestionLayoutType:usedFallbackIndexSet:shouldSuggestionsBeDisjoint:guardedData:]_block_invoke.235
+ __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.94
+ __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.94.cold.1
+ __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.95
+ __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.95.cold.1
+ __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke_2.90
+ __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke_2.90.cold.1
+ __18-[ATXAction proto]_block_invoke.108
+ __202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.94
+ __23-[ATXSportsClient init]_block_invoke.20
+ __248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.104
+ __30-[ATXAppDirectoryClient _init]_block_invoke.17
+ __30-[ATXAppDirectoryClient _init]_block_invoke.17.cold.1
+ __30-[ATXUsageInsightsClient init]_block_invoke.8
+ __30-[ATXUsageInsightsClient init]_block_invoke.8.cold.1
+ __31-[ATXFaceSuggestionClient init]_block_invoke.29
+ __31-[ATXFaceSuggestionClient init]_block_invoke.29.cold.1
+ __31-[ATXSuggestedPagesClient init]_block_invoke.8
+ __32-[ATXSettingsActionsClient init]_block_invoke.11
+ __32-[ATXSettingsActionsClient init]_block_invoke.11.cold.1
+ __33-[ATXModeEntityScorerClient init]_block_invoke.63
+ __35-[ATXClient approvedSiriKitIntents]_block_invoke.21
+ __35-[ATXClient approvedSiriKitIntents]_block_invoke.21.cold.1
+ __35-[ATXSettingsAction navigationLink]_block_invoke.51
+ __38-[ATXClient shouldPredictAppBundleId:]_block_invoke.25
+ __38-[ATXClient shouldPredictAppBundleId:]_block_invoke.25.cold.1
+ __38-[ATXModeEntityScore encodeWithCoder:]_block_invoke.45
+ __38-[ATXModeEntityScore encodeWithCoder:]_block_invoke.45.cold.1
+ __38-[ATXModeEntityScore encodeWithCoder:]_block_invoke.45.cold.2
+ __38-[ATXModeEntityScorer scoreApps:mode:]_block_invoke.15
+ __38-[ATXModeEntityScorer scoreApps:mode:]_block_invoke.19
+ __38-[ATXModeEntityScorer scoreApps:mode:]_block_invoke.19.cold.1
+ __40+[ATXAssets2 onUpdateRestartThisProcess]_block_invoke.18
+ __40-[ATXCacheReader initWithCacheBasePath:]_block_invoke.25
+ __41-[ATXModeEntityScorer rankedAppsForMode:]_block_invoke.21
+ __41-[ATXModeEntityScorer rankedAppsForMode:]_block_invoke.22
+ __41-[ATXModeEntityScorer rankedAppsForMode:]_block_invoke.22.cold.1
+ __41-[ATXNotificationDigestRankerClient init]_block_invoke.76
+ __42+[ATXAppDisplayIdentifiers allIdentifiers]_block_invoke.21
+ __43-[ATXInformationStore pruneTimelineEntries]_block_invoke.691
+ __43-[ATXInformationStore pruneTimelineEntries]_block_invoke.691.cold.1
+ __43-[ATXNotificationCategorizationClient init]_block_invoke.8
+ __43-[ATXNotificationCategorizationClient init]_block_invoke.8.cold.1
+ __44-[ATXInformationStore readAllDismissRecords]_block_invoke.617
+ __44-[ATXInformationStore readAllDismissRecords]_block_invoke_2.619
+ __44-[ATXInformationStore readAllDismissRecords]_block_invoke_2.619.cold.1
+ __44-[ATXInformationStore readCachedSuggestions]_block_invoke.361
+ __44-[ATXInformationStore readCachedSuggestions]_block_invoke.361.cold.1
+ __44-[ATXInformationStore readCachedSuggestions]_block_invoke.365
+ __44-[ATXInformationStore readCachedSuggestions]_block_invoke.365.cold.1
+ __45-[ATXInformationStore readAllInfoSuggestions]_block_invoke.372
+ __45-[ATXInformationStore readAllInfoSuggestions]_block_invoke.372.cold.1
+ __45-[ATXLockScreenNotificationRankerClient init]_block_invoke.67
+ __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke.460
+ __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke.470
+ __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.464
+ __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.464.cold.1
+ __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.471
+ __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.471.cold.1
+ __47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.24
+ __47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.24.cold.1
+ __48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.82
+ __48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.82.cold.1
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke.820
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke.830
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_2.821
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_2.835
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_2.835.cold.1
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_3.826
+ __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_3.826.cold.1
+ __49+[ATXAppDirectoryClient _sortedDefaultCategories]_block_invoke.78
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.57
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.57.cold.1
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.57.cold.2
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.67
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.84
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85.cold.1
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85.cold.2
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85.cold.3
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85.cold.4
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85.cold.5
+ __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.85.cold.6
+ __49-[ATXActivitySuggestionClient _fetchAndCacheLOIs]_block_invoke.61
+ __49-[ATXActivitySuggestionClient _fetchAndCacheLOIs]_block_invoke.61.cold.1
+ __49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.54
+ __49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.54.cold.1
+ __50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.27
+ __50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.28
+ __50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.28.cold.1
+ __50-[ATXModeEntityScorerClient scoreApps:mode:reply:]_block_invoke.84
+ __51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.23
+ __51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.23.cold.1
+ __52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.55
+ __52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.55.cold.1
+ __53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.56
+ __53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.56.cold.1
+ __53-[ATXModeEntityScorerClient rankedAppsForMode:reply:]_block_invoke.85
+ __54-[ATXActivitySuggestionClient initWithRoutineManager:]_block_invoke.17
+ __54-[ATXModeEntityScorerClient scoreContacts:mode:reply:]_block_invoke.78
+ __55-[ATXInformationStore readCurrentlyRelevantSuggestions]_block_invoke.380
+ __55-[ATXInformationStore readCurrentlyRelevantSuggestions]_block_invoke.380.cold.1
+ __56-[ATXModeEntityScorerClient rankedWidgetsForMode:reply:]_block_invoke.86
+ __57-[ATXActivitySuggestionClient _setUpPublisherIfNecessary]_block_invoke.29
+ __57-[ATXActivitySuggestionClient _setUpPublisherIfNecessary]_block_invoke.29.cold.1
+ __57-[ATXActivitySuggestionClient _setUpPublisherIfNecessary]_block_invoke.29.cold.2
+ __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke.405
+ __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke_2.406
+ __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke_3.407
+ __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke_3.407.cold.1
+ __57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.29
+ __57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.29.cold.1
+ __57-[ATXModeEntityScorerClient rankedContactsForMode:reply:]_block_invoke.81
+ __58+[NSDate(TimeManipulationForTesting) test_setCurrentDate:]_block_invoke.cold.1
+ __59-[ATXIntentStream getIntentEventForSourceItemID:forSource:]_block_invoke.30
+ __59-[ATXModeEntityScorerClient scoreNotifications:mode:reply:]_block_invoke.87
+ __61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.30
+ __61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.30.cold.1
+ __61-[ATXModeEntityScorerClient scoreAppsForDenyList:mode:reply:]_block_invoke.94
+ __62-[ATXAppDirectoryClient categoriesWithShouldUseDefault:reply:]_block_invoke.24
+ __62-[ATXAppDirectoryClient categoriesWithShouldUseDefault:reply:]_block_invoke.24.cold.1
+ __62-[ATXAppDirectoryClient categoriesWithShouldUseDefault:reply:]_block_invoke.27
+ __62-[ATXModeEntityScorerClient rankedNotificationsForMode:reply:]_block_invoke.88
+ __64+[NSDate(TimeManipulationForTesting) test_endManipulationOfTime]_block_invoke.cold.1
+ __64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.57
+ __64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.57.cold.1
+ __64-[ATXModeEntityScorerClient rankedAppsForDenyListForMode:reply:]_block_invoke.95
+ __65-[ATXModeEntityScorerClient scoreContactsForDenyList:mode:reply:]_block_invoke.99
+ __65-[ATXUsageInsightsClient fetchAllPhubbingSessionsWithCompletion:]_block_invoke.18
+ __66+[NSDate(TimeManipulationForTesting) test_beginManipulationOfTime]_block_invoke.cold.1
+ __66-[ATXInformationStore latestInfoSuggestionRelevantNowForSourceId:]_block_invoke.389
+ __66-[ATXInformationStore latestInfoSuggestionRelevantNowForSourceId:]_block_invoke.389.cold.1
+ __66-[ATXInformationStore readAllInfoSuggestionsWithSourceIdentifier:]_block_invoke.384
+ __66-[ATXInformationStore readAllInfoSuggestionsWithSourceIdentifier:]_block_invoke.384.cold.1
+ __67-[ATXInformationStore widgetSuggestionRemovalRecordsForDiagnostics]_block_invoke.603
+ __68-[ATXHomeScreenPageAppRanker appsInAscendingOrderOfHistoricalUsage:]_block_invoke.15
+ __68-[ATXHomeScreenSuggestionClient listener:shouldAcceptNewConnection:]_block_invoke.183
+ __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke.669
+ __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke.678
+ __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke_2.680
+ __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke_2.680.cold.1
+ __69-[ATXModeEntityScorerClient rankedAppsForNotificationsForMode:reply:]_block_invoke.89
+ __70+[ATXHomeScreenStackSuggestion stackSuggestionsFromCachedSuggestions:]_block_invoke.28
+ __71-[ATXActionPredictionClient shouldDisplayDailyRoutineForContext:reply:]_block_invoke.51
+ __71-[ATXActionPredictionClient shouldDisplayDailyRoutineForContext:reply:]_block_invoke.51.cold.1
+ __71-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationWithCompletion:]_block_invoke.40
+ __71-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationWithCompletion:]_block_invoke.41
+ __71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.44
+ __71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.45
+ __71-[ATXWidgetDescriptorCache initWithProvider:cachePath:legacyCachePath:]_block_invoke.29
+ __72-[ATXUsageInsightsClient fetchAllContinuousUsageSessionsWithCompletion:]_block_invoke.20
+ __72-[ATXUsageInsightsClient fetchAllInterruptingAppSessionsWithCompletion:]_block_invoke.16
+ __72-[ATXUsageInsightsClient fetchAllMindlessCyclingSessionsWithCompletion:]_block_invoke.19
+ __73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.236
+ __73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.236.cold.1
+ __73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.236.cold.2
+ __73-[ATXDefaultHomeScreenItemManager _writeUpdate:atPath:completionHandler:]_block_invoke.25
+ __73-[ATXDefaultHomeScreenItemManager _writeUpdate:atPath:completionHandler:]_block_invoke.35
+ __73-[ATXDefaultHomeScreenItemManager _writeUpdate:atPath:completionHandler:]_block_invoke.40
+ __73-[ATXInterruptionManager recommendedAndCandidateDeniedAppsForMode:reply:]_block_invoke.48
+ __73-[ATXInterruptionManager recommendedAndCandidateDeniedAppsForMode:reply:]_block_invoke.48.cold.1
+ __73-[ATXModeEntityScorerClient rankedContactsForNotificationsForMode:reply:]_block_invoke.90
+ __74-[ATXClient shouldPredictBundleIdForShortcuts:action:forPrimaryShortcuts:]_block_invoke.31
+ __74-[ATXClient shouldPredictBundleIdForShortcuts:action:forPrimaryShortcuts:]_block_invoke.31.cold.1
+ __74-[ATXInformationStore firstEngagementOfWidget:kind:intent:sinceTimestamp:]_block_invoke.740
+ __76-[ATXEngagementRecordManager updateForClientModelCacheUpdate:clientModelId:]_block_invoke.22
+ __76-[ATXFaceSuggestionClient regenerateFaceGalleryConfigurationWithCompletion:]_block_invoke.34
+ __76-[ATXFaceSuggestionClient regenerateFaceGalleryConfigurationWithCompletion:]_block_invoke.36
+ __76-[ATXInformationStore recordWidgetReloadForSuggestion:date:readyForDisplay:]_block_invoke.868
+ __76-[ATXInformationStore recordWidgetReloadForSuggestion:date:readyForDisplay:]_block_invoke.868.cold.1
+ __76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke.100
+ __77+[NSDate(TimeManipulationForTesting) test_adjustCurrentDateWithTimeInterval:]_block_invoke.cold.1
+ __77-[ATXInformationStore atomicallyDeleteInfoSuggestions:insertInfoSuggestions:]_block_invoke.450
+ __77-[ATXInformationStore atomicallyDeleteInfoSuggestions:insertInfoSuggestions:]_block_invoke_2.451
+ __77-[ATXInformationStore atomicallyDeleteInfoSuggestions:insertInfoSuggestions:]_block_invoke_2.451.cold.1
+ __77-[ATXInformationStore deleteAllSuggestionsForSourceId:excludingSuggestionId:]_block_invoke.480
+ __77-[ATXInformationStore deleteAllSuggestionsForSourceId:excludingSuggestionId:]_block_invoke.480.cold.1
+ __80-[ATXDigestOnboardingSuggestionClient hasNotificationProblemForPreviousNumDays:]_block_invoke.44
+ __80-[ATXDigestOnboardingSuggestionClient hasNotificationProblemForPreviousNumDays:]_block_invoke_2.47
+ __80-[ATXInformationStore addAbuseControlOutcomeForSuggestion:forTimestamp:outcome:]_block_invoke.800
+ __80-[ATXInformationStore addAbuseControlOutcomeForSuggestion:forTimestamp:outcome:]_block_invoke.800.cold.1
+ __81+[ATXSpotlightClientResponse _limitingResults:scores:spotlightRecentIndex:limit:]_block_invoke.64
+ __81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke.17
+ __81-[ATXNotificationCategorizationClient fetchContextForMailWithRequest:completion:]_block_invoke.30
+ __82-[ATXNotificationCategorizationClient rankUserNotificationWithRequest:completion:]_block_invoke.22
+ __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.25
+ __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.25.cold.1
+ __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.27
+ __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.27.cold.1
+ __83-[ATXUserNotificationDigestNotificationGroup initWithNotifications:useDigestOrder:]_block_invoke.19
+ __84+[ATXAppDirectoryClient _sortedBundleIDsByCategoryWithHardcodedAppCategoryMappings:]_block_invoke.69
+ __84-[ATXNotificationCategorizationClient fetchContextForMessageWithRequest:completion:]_block_invoke.34
+ __84-[ATXSuggestedPagesClient suggestedPagesWithFilter:layoutOptions:completionHandler:]_block_invoke.13
+ __84-[ATXSuggestedPagesClient suggestedPagesWithFilter:layoutOptions:completionHandler:]_block_invoke.13.cold.1
+ __86-[ATXDigestOnboardingSuggestionClient observeValueForKeyPath:ofObject:change:context:]_block_invoke.59
+ __86-[ATXInformationStore recordUserRemovalOfSuggestedWidget:kind:intent:atDate:duration:]_block_invoke.564
+ __86-[ATXInformationStore recordUserRemovalOfSuggestedWidget:kind:intent:atDate:duration:]_block_invoke.564.cold.1
+ __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.29
+ __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.32
+ __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.34
+ __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.39
+ __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.43
+ __89-[ATXActionPredictionClient removeActionPredictionNotificationsMatchingSuggestion:reply:]_block_invoke.45
+ __89-[ATXActionPredictionClient removeActionPredictionNotificationsMatchingSuggestion:reply:]_block_invoke.45.cold.1
+ __89-[ATXInformationStore nextImportantDateAmongTimelineInducedProactiveStackRotationRecords]_block_invoke.528
+ __89-[ATXInformationStore nextImportantDateAmongTimelineInducedProactiveStackRotationRecords]_block_invoke.531
+ __89-[ATXInformationStore nextImportantDateAmongTimelineInducedProactiveStackRotationRecords]_block_invoke.531.cold.1
+ __89-[ATXNotificationCategorizationClient fetchContextForNotificationWithRequest:completion:]_block_invoke.26
+ __90-[ATXNotificationCategorizationClient collectCoreAnalyticsJsonForNotification:completion:]_block_invoke.18
+ __90-[ATXUserEducationSuggestionConnectorListenerDelegate listener:shouldAcceptNewConnection:]_block_invoke.24
+ __91+[ATXUpcomingMediaQuery getUpcomingMediaForBundle:isInternalApplication:completionHandler:]_block_invoke.21
+ __91+[ATXUpcomingMediaQuery getUpcomingMediaForBundle:isInternalApplication:completionHandler:]_block_invoke.21.cold.1
+ __91+[ATXUpcomingMediaQuery getUpcomingMediaForBundle:isInternalApplication:completionHandler:]_block_invoke.21.cold.2
+ __91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.53
+ __91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.57
+ __91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.57.cold.1
+ __91-[ATXDefaultHomeScreenItemUpdater _updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.cold.1
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.62.cold.1
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.63
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.63.cold.1
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.63.cold.2
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.63.cold.3
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.63.cold.4
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.64
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.68
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.69
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.73
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.74
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.77
+ __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.75
+ __94-[ATXNotificationDigestRankerClient appsSortedByNotificationsReceivedInPreviousNumDays:reply:]_block_invoke.95
+ __96-[ATXInformationStore mostRecentTimelineEntryWithScoreForWidget:kind:family:intentIndexingHash:]_block_invoke.632
+ __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.29
+ __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.29.cold.1
+ __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.29.cold.2
+ __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.29.cold.3
+ __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.29.cold.4
+ __98-[ATXHomeScreenSuggestionClient _replaceSuggestionWithId:shouldSuggestionsBeDisjoint:guardedData:]_block_invoke.232
+ ___108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke_2
+ ___73-[ATXDefaultHomeScreenItemUpdater updateDefaultsDueToCarPlayConfigUpdate]_block_invoke
+ ___83-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]_block_invoke
+ ___91-[ATXDefaultHomeScreenItemUpdater _updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke
+ _____atxlog_handle_carPlay_widgets_block_invoke
+ ___atxlog_handle_carPlay_widgets
+ __atxlog_handle_action_prediction.cold.1
+ __atxlog_handle_anchor.cold.1
+ __atxlog_handle_app_install.cold.1
+ __atxlog_handle_app_library.cold.1
+ __atxlog_handle_app_prediction.cold.1
+ __atxlog_handle_backup.cold.1
+ __atxlog_handle_blending.cold.1
+ __atxlog_handle_blending_ecosystem.cold.1
+ __atxlog_handle_blending_internal_cache.cold.1
+ __atxlog_handle_carPlay_widgets.cold.1
+ __atxlog_handle_carPlay_widgets.log
+ __atxlog_handle_carPlay_widgets.onceToken
+ __atxlog_handle_context_heuristic.cold.1
+ __atxlog_handle_context_user_education_suggestions.cold.1
+ __atxlog_handle_contextual_actions.cold.1
+ __atxlog_handle_contextual_engine.cold.1
+ __atxlog_handle_dailyroutines.cold.1
+ __atxlog_handle_default.cold.1
+ __atxlog_handle_deletions.cold.1
+ __atxlog_handle_feedback.cold.1
+ __atxlog_handle_gi.cold.1
+ __atxlog_handle_hero.cold.1
+ __atxlog_handle_heuristic.cold.1
+ __atxlog_handle_home_screen.cold.1
+ __atxlog_handle_intents_helper.cold.1
+ __atxlog_handle_lock_screen.cold.1
+ __atxlog_handle_metrics.cold.1
+ __atxlog_handle_modes.cold.1
+ __atxlog_handle_notification_categorization.cold.1
+ __atxlog_handle_notification_management.cold.1
+ __atxlog_handle_notifications.cold.1
+ __atxlog_handle_pmm.cold.1
+ __atxlog_handle_relevance_model.cold.1
+ __atxlog_handle_relevant_shortcut.cold.1
+ __atxlog_handle_settings_actions.cold.1
+ __atxlog_handle_sleep_schedule.cold.1
+ __atxlog_handle_time_intelligence.cold.1
+ __atxlog_handle_timeline.cold.1
+ __atxlog_handle_trial_assets.cold.1
+ __atxlog_handle_ui.cold.1
+ __atxlog_handle_usage_insights.cold.1
+ __atxlog_handle_watch.cold.1
+ __atxlog_handle_xpc.cold.1
+ __atxlog_handle_zkw_hide.cold.1
+ __block_literal_global.100
+ __block_literal_global.102
+ __block_literal_global.11
+ __block_literal_global.111
+ __block_literal_global.125
+ __block_literal_global.127
+ __block_literal_global.135
+ __block_literal_global.138
+ __block_literal_global.140
+ __block_literal_global.170
+ __block_literal_global.182
+ __block_literal_global.185
+ __block_literal_global.196
+ __block_literal_global.216
+ __block_literal_global.221
+ __block_literal_global.223
+ __block_literal_global.225
+ __block_literal_global.28
+ __block_literal_global.30
+ __block_literal_global.302
+ __block_literal_global.342
+ __block_literal_global.345
+ __block_literal_global.377
+ __block_literal_global.396
+ __block_literal_global.401
+ __block_literal_global.409
+ __block_literal_global.46
+ __block_literal_global.466
+ __block_literal_global.473
+ __block_literal_global.523
+ __block_literal_global.533
+ __block_literal_global.54
+ __block_literal_global.541
+ __block_literal_global.546
+ __block_literal_global.55
+ __block_literal_global.555
+ __block_literal_global.57
+ __block_literal_global.58
+ __block_literal_global.605
+ __block_literal_global.613
+ __block_literal_global.660
+ __block_literal_global.665
+ __block_literal_global.682
+ __block_literal_global.689
+ __block_literal_global.696
+ __block_literal_global.699
+ __block_literal_global.70
+ __block_literal_global.707
+ __block_literal_global.723
+ __block_literal_global.728
+ __block_literal_global.733
+ __block_literal_global.742
+ __block_literal_global.747
+ __block_literal_global.759
+ __block_literal_global.768
+ __block_literal_global.78
+ __block_literal_global.807
+ __block_literal_global.81
+ __block_literal_global.82
+ __block_literal_global.860
+ __block_literal_global.876
+ __block_literal_global.881
+ __block_literal_global.93
+ __block_literal_global.97
+ _kATXCarPlayConfigDidUpdateNotification
+ _objc_msgSend$_carPlayOnboardingStacks
+ _objc_msgSend$_generateSmartStackForCarPlayWithDescriptorCache
+ _objc_msgSend$_generateSmartStacksForCarPlay
+ _objc_msgSend$_readCarPlayUpdateFromFileWithCompletionHandler:
+ _objc_msgSend$_updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:
+ _objc_msgSend$carPlayOnboardingStacks
+ _objc_msgSend$initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:
+ _objc_msgSend$initWithHomeScreenPath:ambientPath:carPlayPath:
+ _objc_msgSend$isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:
+ _objc_msgSend$isCarPlay
+ _objc_msgSend$writeCarPlayUpdate:completionHandler:
+ dateManipulationQueue.cold.1
+ getAsset.cold.1
+ getTrialAssets.cold.1
- -[ATXDefaultHomeScreenItemManager initWithHomeScreenPath:ambientPath:]
- -[ATXDefaultHomeScreenItemOnboardingStacksProducer initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:]
- GCC_except_table373
- _OBJC_$_PROP_LIST_ATXActivitySuggestion.65
- _OBJC_$_PROP_LIST_ATXUserEducationSuggestion.58
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
- __100-[ATXNotificationCategorizationClient collectDynamicBreakthroughFeaturesForNotification:completion:]_block_invoke.10
- __102-[ATXHomeScreenSuggestionClient _updateLoggerStacksToStackSuggestionsFromHomeScreenCachedSuggestions:]_block_invoke.159
- __104-[ATXDigestSetupFlowClient _helperAppsSortedByNotificationsReceivedInPreviousNumDays:completionHandler:]_block_invoke.3
- __104-[ATXDigestSetupFlowClient _helperAppsSortedByNotificationsReceivedInPreviousNumDays:completionHandler:]_block_invoke.3.cold.1
- __104-[ATXInformationStore upcomingDateThatTimelineScoreChangesToOrFromZeroForWidget:kind:familyMask:intent:]_block_invoke.638
- __104-[ATXInformationStore upcomingDateThatTimelineScoreChangesToOrFromZeroForWidget:kind:familyMask:intent:]_block_invoke.642
- __104-[ATXInformationStore upcomingDateThatTimelineScoreChangesToOrFromZeroForWidget:kind:familyMask:intent:]_block_invoke.642.cold.1
- __105-[ATXInformationStore recentRelevantTimelineEntriesOrderedByDescendingScoreForWidget:kind:family:intent:]_block_invoke.648
- __108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.38
- __108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.45
- __108-[ATXDefaultHomeScreenItemManager fetchGalleryItemsForVariant:gridSize:supportedFamilies:completionHandler:]_block_invoke.48
- __110-[ATXUserActivityStream _enumerateActivityIntentEventsBetweenStartDate:endDate:bundleIdFilter:reversed:block:]_block_invoke.7
- __112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.31
- __112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.32
- __112-[ATXModeEntityScorer assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:]_block_invoke.32.cold.1
- __113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.35
- __113-[ATXAppDirectoryClient predictedAppsAndRecentAppsWithMaxNumberOfPredictedApps:shouldUseDefaultCategories:reply:]_block_invoke.37
- __113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.26
- __113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.27
- __113-[ATXModeEntityScorer modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:]_block_invoke.27.cold.1
- __117-[ATXInformationStore fetchStackConfigStatisticsForWidgetBundleId:widgetKind:containerBundleIdentifier:widgetFamily:]_block_invoke.841
- __117-[ATXInformationStore fetchStackConfigStatisticsForWidgetBundleId:widgetKind:containerBundleIdentifier:widgetFamily:]_block_invoke.841.cold.1
- __117-[ATXInformationStore mostRecentRotationRecordForWidget:kind:intent:considerStalenessRotation:filterByClientModelId:]_block_invoke.501
- __117-[ATXInformationStore mostRecentRotationRecordForWidget:kind:intent:considerStalenessRotation:filterByClientModelId:]_block_invoke.509
- __117-[ATXInformationStore mostRecentRotationRecordForWidget:kind:intent:considerStalenessRotation:filterByClientModelId:]_block_invoke.509.cold.1
- __124-[ATXModeEntityScorerClient assignModeEntityScores:entityTypeIdentifier:entityIdentifier:score:modeConfigurationType:reply:]_block_invoke.99
- __125-[ATXModeEntityScorerClient modeEntityScoresFromCacheForModeEntityTypeIdentifier:modeIdentifier:modeConfigurationType:reply:]_block_invoke.95
- __141-[ATXActionPredictionClient getActionPredictionsForCandidateBundleIdentifiers:candidateActionTypes:consumerType:consumerSubType:limit:reply:]_block_invoke.28
- __141-[ATXActionPredictionClient getActionPredictionsForCandidateBundleIdentifiers:candidateActionTypes:consumerType:consumerSubType:limit:reply:]_block_invoke.28.cold.1
- __144-[ATXActionPredictionClient getActionPredictionsForContext:includeBundleIds:excludeBundleIds:includeActionTypes:excludeActionTypes:limit:reply:]_block_invoke.48
- __144-[ATXActionPredictionClient getActionPredictionsForContext:includeBundleIds:excludeBundleIds:includeActionTypes:excludeActionTypes:limit:reply:]_block_invoke.48.cold.1
- __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.15
- __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.15.cold.1
- __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.19
- __157-[ATXIntentStream _enumerateIntentEventsBetweenStartDate:endDate:forSource:bundleIdFilter:allowMissingTitles:reversed:INIntentFilter:linkActionFilter:block:]_block_invoke.19.cold.1
- __161-[ATXHomeScreenSuggestionClient _replaceSuggestionWithId:fromSuggestionsArray:suggestionLayoutType:usedFallbackIndexSet:shouldSuggestionsBeDisjoint:guardedData:]_block_invoke.229
- __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.82
- __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.83
- __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.83.cold.1
- __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke.88.cold.1
- __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke_2.84
- __178-[ATXHomeScreenSuggestionClient initWithHomeScreenConfigCache:engagementRecordManager:widgetDwellTracker:widgetDismissManager:uiCacheManager:actionPredictionClient:store:logger:]_block_invoke_2.84.cold.1
- __18-[ATXAction proto]_block_invoke.102
- __202-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedAmbientOnboardingStacksForSize:stack1RequiredWidgetPersonalities:stack2RequiredWidgetPersonalities:rankedWidgets:usedWidgetPersonalities:]_block_invoke.88
- __23-[ATXSportsClient init]_block_invoke.14
- __248-[ATXDefaultHomeScreenItemOnboardingStacksProducer _personalizedOnboardingStackForSize:requiredWidgetPersonalities:conditionalWidgetPersonalities:fallbackWidgetPersonalities:rankedThirdPartyWidgets:usedWidgetPersonalities:shouldAdd3PWidgetToStack:]_block_invoke.98
- __30-[ATXAppDirectoryClient _init]_block_invoke.11
- __30-[ATXAppDirectoryClient _init]_block_invoke.11.cold.1
- __30-[ATXUsageInsightsClient init]_block_invoke.2
- __30-[ATXUsageInsightsClient init]_block_invoke.2.cold.1
- __31-[ATXFaceSuggestionClient init]_block_invoke.23
- __31-[ATXFaceSuggestionClient init]_block_invoke.23.cold.1
- __31-[ATXSuggestedPagesClient init]_block_invoke.2
- __32-[ATXSettingsActionsClient init]_block_invoke.5
- __32-[ATXSettingsActionsClient init]_block_invoke.5.cold.1
- __33-[ATXModeEntityScorerClient init]_block_invoke.57
- __35-[ATXClient approvedSiriKitIntents]_block_invoke.15
- __35-[ATXClient approvedSiriKitIntents]_block_invoke.15.cold.1
- __35-[ATXSettingsAction navigationLink]_block_invoke.45
- __38-[ATXClient shouldPredictAppBundleId:]_block_invoke.19
- __38-[ATXClient shouldPredictAppBundleId:]_block_invoke.19.cold.1
- __38-[ATXModeEntityScore encodeWithCoder:]_block_invoke.39
- __38-[ATXModeEntityScore encodeWithCoder:]_block_invoke.39.cold.1
- __38-[ATXModeEntityScore encodeWithCoder:]_block_invoke.39.cold.2
- __38-[ATXModeEntityScorer scoreApps:mode:]_block_invoke.13
- __38-[ATXModeEntityScorer scoreApps:mode:]_block_invoke.13.cold.1
- __38-[ATXModeEntityScorer scoreApps:mode:]_block_invoke.9
- __40+[ATXAssets2 onUpdateRestartThisProcess]_block_invoke.6
- __40-[ATXCacheReader initWithCacheBasePath:]_block_invoke.19
- __41-[ATXModeEntityScorer rankedAppsForMode:]_block_invoke.15
- __41-[ATXModeEntityScorer rankedAppsForMode:]_block_invoke.16
- __41-[ATXModeEntityScorer rankedAppsForMode:]_block_invoke.16.cold.1
- __41-[ATXNotificationDigestRankerClient init]_block_invoke.70
- __42+[ATXAppDisplayIdentifiers allIdentifiers]_block_invoke.15
- __43-[ATXInformationStore pruneTimelineEntries]_block_invoke.685
- __43-[ATXInformationStore pruneTimelineEntries]_block_invoke.685.cold.1
- __43-[ATXNotificationCategorizationClient init]_block_invoke.2
- __43-[ATXNotificationCategorizationClient init]_block_invoke.2.cold.1
- __44-[ATXInformationStore readAllDismissRecords]_block_invoke.611
- __44-[ATXInformationStore readAllDismissRecords]_block_invoke_2.613
- __44-[ATXInformationStore readAllDismissRecords]_block_invoke_2.613.cold.1
- __44-[ATXInformationStore readCachedSuggestions]_block_invoke.355
- __44-[ATXInformationStore readCachedSuggestions]_block_invoke.355.cold.1
- __44-[ATXInformationStore readCachedSuggestions]_block_invoke.359
- __44-[ATXInformationStore readCachedSuggestions]_block_invoke.359.cold.1
- __45-[ATXInformationStore readAllInfoSuggestions]_block_invoke.366
- __45-[ATXInformationStore readAllInfoSuggestions]_block_invoke.366.cold.1
- __45-[ATXLockScreenNotificationRankerClient init]_block_invoke.61
- __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke.454
- __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke.464
- __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.458
- __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.458.cold.1
- __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.465
- __47-[ATXInformationStore deleteExpiredSuggestions]_block_invoke_2.465.cold.1
- __47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.18
- __47-[ATXModeEntityScorer scoreNotifications:mode:]_block_invoke.18.cold.1
- __48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.76
- __48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.76.cold.1
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke.814
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke.824
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_2.815
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_2.829
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_2.829.cold.1
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_3.820
- __48-[ATXInformationStore addStackConfigStatistics:]_block_invoke_3.820.cold.1
- __49+[ATXAppDirectoryClient _sortedDefaultCategories]_block_invoke.72
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.48
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.48.cold.1
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.48.cold.2
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.58
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke.75
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76.cold.1
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76.cold.2
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76.cold.3
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76.cold.4
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76.cold.5
- __49-[ATXActionSearchResultExecution executeShortcut]_block_invoke_2.76.cold.6
- __49-[ATXActivitySuggestionClient _fetchAndCacheLOIs]_block_invoke.55
- __49-[ATXActivitySuggestionClient _fetchAndCacheLOIs]_block_invoke.55.cold.1
- __49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.48
- __49-[ATXModeEntityScorer scoreAppsForDenyList:mode:]_block_invoke.48.cold.1
- __50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.21
- __50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.22
- __50-[ATXModeEntityScorer rankedNotificationsForMode:]_block_invoke.22.cold.1
- __50-[ATXModeEntityScorerClient scoreApps:mode:reply:]_block_invoke.78
- __51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.17
- __51-[ATXModeEntityScorer scoreUserNotifications:mode:]_block_invoke.17.cold.1
- __52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.49
- __52-[ATXModeEntityScorer rankedAppsForDenyListForMode:]_block_invoke.49.cold.1
- __53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.50
- __53-[ATXModeEntityScorer scoreContactsForDenyList:mode:]_block_invoke.50.cold.1
- __53-[ATXModeEntityScorerClient rankedAppsForMode:reply:]_block_invoke.79
- __54-[ATXActivitySuggestionClient initWithRoutineManager:]_block_invoke.11
- __54-[ATXModeEntityScorerClient scoreContacts:mode:reply:]_block_invoke.72
- __55-[ATXInformationStore readCurrentlyRelevantSuggestions]_block_invoke.374
- __55-[ATXInformationStore readCurrentlyRelevantSuggestions]_block_invoke.374.cold.1
- __56-[ATXModeEntityScorerClient rankedWidgetsForMode:reply:]_block_invoke.80
- __57-[ATXActivitySuggestionClient _setUpPublisherIfNecessary]_block_invoke.23
- __57-[ATXActivitySuggestionClient _setUpPublisherIfNecessary]_block_invoke.23.cold.1
- __57-[ATXActivitySuggestionClient _setUpPublisherIfNecessary]_block_invoke.23.cold.2
- __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke.399
- __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke_2.400
- __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke_3.401
- __57-[ATXInformationStore earliestFutureSuggestionChangeDate]_block_invoke_3.401.cold.1
- __57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.23
- __57-[ATXModeEntityScorer rankedAppsForNotificationsForMode:]_block_invoke.23.cold.1
- __57-[ATXModeEntityScorerClient rankedContactsForMode:reply:]_block_invoke.75
- __59-[ATXIntentStream getIntentEventForSourceItemID:forSource:]_block_invoke.24
- __59-[ATXModeEntityScorerClient scoreNotifications:mode:reply:]_block_invoke.81
- __61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.24
- __61-[ATXModeEntityScorer rankedContactsForNotificationsForMode:]_block_invoke.24.cold.1
- __61-[ATXModeEntityScorerClient scoreAppsForDenyList:mode:reply:]_block_invoke.88
- __62-[ATXAppDirectoryClient categoriesWithShouldUseDefault:reply:]_block_invoke.18
- __62-[ATXAppDirectoryClient categoriesWithShouldUseDefault:reply:]_block_invoke.18.cold.1
- __62-[ATXAppDirectoryClient categoriesWithShouldUseDefault:reply:]_block_invoke.21
- __62-[ATXModeEntityScorerClient rankedNotificationsForMode:reply:]_block_invoke.82
- __64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.51
- __64-[ATXModeEntityScorer rankedContactsForDenyListForMode:options:]_block_invoke.51.cold.1
- __64-[ATXModeEntityScorerClient rankedAppsForDenyListForMode:reply:]_block_invoke.89
- __65-[ATXModeEntityScorerClient scoreContactsForDenyList:mode:reply:]_block_invoke.93
- __65-[ATXUsageInsightsClient fetchAllPhubbingSessionsWithCompletion:]_block_invoke.12
- __66-[ATXInformationStore latestInfoSuggestionRelevantNowForSourceId:]_block_invoke.383
- __66-[ATXInformationStore latestInfoSuggestionRelevantNowForSourceId:]_block_invoke.383.cold.1
- __66-[ATXInformationStore readAllInfoSuggestionsWithSourceIdentifier:]_block_invoke.378
- __66-[ATXInformationStore readAllInfoSuggestionsWithSourceIdentifier:]_block_invoke.378.cold.1
- __67-[ATXInformationStore widgetSuggestionRemovalRecordsForDiagnostics]_block_invoke.597
- __68-[ATXHomeScreenPageAppRanker appsInAscendingOrderOfHistoricalUsage:]_block_invoke.9
- __68-[ATXHomeScreenSuggestionClient listener:shouldAcceptNewConnection:]_block_invoke.177
- __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke.663
- __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke.672
- __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke_2.668
- __69-[ATXInformationStore _insertTimelineEntries:forWidget:storageLimit:]_block_invoke_2.668.cold.1
- __69-[ATXModeEntityScorerClient rankedAppsForNotificationsForMode:reply:]_block_invoke.83
- __70+[ATXHomeScreenStackSuggestion stackSuggestionsFromCachedSuggestions:]_block_invoke.22
- __71-[ATXActionPredictionClient shouldDisplayDailyRoutineForContext:reply:]_block_invoke.45
- __71-[ATXActionPredictionClient shouldDisplayDailyRoutineForContext:reply:]_block_invoke.45.cold.1
- __71-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationWithCompletion:]_block_invoke.34
- __71-[ATXFaceSuggestionClient fetchFaceGalleryConfigurationWithCompletion:]_block_invoke.35
- __71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.38
- __71-[ATXFaceSuggestionClient fetchFaceSuggestionsForFocusMode:completion:]_block_invoke.39
- __71-[ATXWidgetDescriptorCache initWithProvider:cachePath:legacyCachePath:]_block_invoke.23
- __72-[ATXUsageInsightsClient fetchAllContinuousUsageSessionsWithCompletion:]_block_invoke.14
- __72-[ATXUsageInsightsClient fetchAllInterruptingAppSessionsWithCompletion:]_block_invoke.10
- __72-[ATXUsageInsightsClient fetchAllMindlessCyclingSessionsWithCompletion:]_block_invoke.13
- __73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.227
- __73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.227.cold.1
- __73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.227.cold.2
- __73-[ATXDefaultHomeScreenItemManager _writeUpdate:atPath:completionHandler:]_block_invoke.19
- __73-[ATXDefaultHomeScreenItemManager _writeUpdate:atPath:completionHandler:]_block_invoke.23
- __73-[ATXDefaultHomeScreenItemManager _writeUpdate:atPath:completionHandler:]_block_invoke.34
- __73-[ATXInterruptionManager recommendedAndCandidateDeniedAppsForMode:reply:]_block_invoke.42
- __73-[ATXInterruptionManager recommendedAndCandidateDeniedAppsForMode:reply:]_block_invoke.42.cold.1
- __73-[ATXModeEntityScorerClient rankedContactsForNotificationsForMode:reply:]_block_invoke.84
- __74-[ATXClient shouldPredictBundleIdForShortcuts:action:forPrimaryShortcuts:]_block_invoke.25
- __74-[ATXClient shouldPredictBundleIdForShortcuts:action:forPrimaryShortcuts:]_block_invoke.25.cold.1
- __74-[ATXInformationStore firstEngagementOfWidget:kind:intent:sinceTimestamp:]_block_invoke.734
- __76-[ATXEngagementRecordManager updateForClientModelCacheUpdate:clientModelId:]_block_invoke.16
- __76-[ATXFaceSuggestionClient regenerateFaceGalleryConfigurationWithCompletion:]_block_invoke.28
- __76-[ATXFaceSuggestionClient regenerateFaceGalleryConfigurationWithCompletion:]_block_invoke.30
- __76-[ATXInformationStore recordWidgetReloadForSuggestion:date:readyForDisplay:]_block_invoke.862
- __76-[ATXInformationStore recordWidgetReloadForSuggestion:date:readyForDisplay:]_block_invoke.862.cold.1
- __76-[ATXModeEntityScorerClient rankedContactsForDenyListForMode:options:reply:]_block_invoke.94
- __77-[ATXInformationStore atomicallyDeleteInfoSuggestions:insertInfoSuggestions:]_block_invoke.444
- __77-[ATXInformationStore atomicallyDeleteInfoSuggestions:insertInfoSuggestions:]_block_invoke_2.445
- __77-[ATXInformationStore atomicallyDeleteInfoSuggestions:insertInfoSuggestions:]_block_invoke_2.445.cold.1
- __77-[ATXInformationStore deleteAllSuggestionsForSourceId:excludingSuggestionId:]_block_invoke.474
- __77-[ATXInformationStore deleteAllSuggestionsForSourceId:excludingSuggestionId:]_block_invoke.474.cold.1
- __80-[ATXDigestOnboardingSuggestionClient hasNotificationProblemForPreviousNumDays:]_block_invoke.38
- __80-[ATXDigestOnboardingSuggestionClient hasNotificationProblemForPreviousNumDays:]_block_invoke_2.41
- __80-[ATXInformationStore addAbuseControlOutcomeForSuggestion:forTimestamp:outcome:]_block_invoke.794
- __80-[ATXInformationStore addAbuseControlOutcomeForSuggestion:forTimestamp:outcome:]_block_invoke.794.cold.1
- __81+[ATXSpotlightClientResponse _limitingResults:scores:spotlightRecentIndex:limit:]_block_invoke.58
- __81-[ATXAppLaunches _rawLaunchCountAndDistinctDaysLaunchedOverLast28DaysWithFilter:]_block_invoke.11
- __81-[ATXNotificationCategorizationClient fetchContextForMailWithRequest:completion:]_block_invoke.24
- __82-[ATXNotificationCategorizationClient rankUserNotificationWithRequest:completion:]_block_invoke.16
- __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.19
- __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.19.cold.1
- __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.21
- __83-[ATXDefaultWidgetSuggesterClient defaultWidgetSuggestionOfType:completionHandler:]_block_invoke.21.cold.1
- __83-[ATXUserNotificationDigestNotificationGroup initWithNotifications:useDigestOrder:]_block_invoke.13
- __84+[ATXAppDirectoryClient _sortedBundleIDsByCategoryWithHardcodedAppCategoryMappings:]_block_invoke.63
- __84-[ATXNotificationCategorizationClient fetchContextForMessageWithRequest:completion:]_block_invoke.28
- __84-[ATXSuggestedPagesClient suggestedPagesWithFilter:layoutOptions:completionHandler:]_block_invoke.7
- __84-[ATXSuggestedPagesClient suggestedPagesWithFilter:layoutOptions:completionHandler:]_block_invoke.7.cold.1
- __86-[ATXDigestOnboardingSuggestionClient observeValueForKeyPath:ofObject:change:context:]_block_invoke.53
- __86-[ATXInformationStore recordUserRemovalOfSuggestedWidget:kind:intent:atDate:duration:]_block_invoke.558
- __86-[ATXInformationStore recordUserRemovalOfSuggestedWidget:kind:intent:atDate:duration:]_block_invoke.558.cold.1
- __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.23
- __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.26
- __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.28
- __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.33
- __88-[ATXHomeScreenPageIconRanker iconIndexesInAscendingOrderOfHistoricalUsageForPageIndex:]_block_invoke.37
- __89-[ATXActionPredictionClient removeActionPredictionNotificationsMatchingSuggestion:reply:]_block_invoke.39
- __89-[ATXActionPredictionClient removeActionPredictionNotificationsMatchingSuggestion:reply:]_block_invoke.39.cold.1
- __89-[ATXInformationStore nextImportantDateAmongTimelineInducedProactiveStackRotationRecords]_block_invoke.522
- __89-[ATXInformationStore nextImportantDateAmongTimelineInducedProactiveStackRotationRecords]_block_invoke.525
- __89-[ATXInformationStore nextImportantDateAmongTimelineInducedProactiveStackRotationRecords]_block_invoke.525.cold.1
- __89-[ATXNotificationCategorizationClient fetchContextForNotificationWithRequest:completion:]_block_invoke.20
- __90-[ATXNotificationCategorizationClient collectCoreAnalyticsJsonForNotification:completion:]_block_invoke.12
- __90-[ATXUserEducationSuggestionConnectorListenerDelegate listener:shouldAcceptNewConnection:]_block_invoke.20
- __91+[ATXUpcomingMediaQuery getUpcomingMediaForBundle:isInternalApplication:completionHandler:]_block_invoke.15
- __91+[ATXUpcomingMediaQuery getUpcomingMediaForBundle:isInternalApplication:completionHandler:]_block_invoke.15.cold.1
- __91+[ATXUpcomingMediaQuery getUpcomingMediaForBundle:isInternalApplication:completionHandler:]_block_invoke.15.cold.2
- __91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke.44
- __91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.48
- __91-[ATXDefaultHomeScreenItemUpdater _updateAmbientDefaultsOnQueueWithReason:appLaunchCounts:]_block_invoke_2.48.cold.1
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.56
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.56.cold.1
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.56.cold.2
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.56.cold.3
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.56.cold.4
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.57
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.61
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.66
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.67
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke.70
- __93-[ATXDefaultHomeScreenItemManager _fetchSmartStackOfVariant:localObserver:completionHandler:]_block_invoke_2.68
- __94-[ATXNotificationDigestRankerClient appsSortedByNotificationsReceivedInPreviousNumDays:reply:]_block_invoke.89
- __96-[ATXInformationStore mostRecentTimelineEntryWithScoreForWidget:kind:family:intentIndexingHash:]_block_invoke.626
- __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.23
- __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.23.cold.1
- __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.23.cold.2
- __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.23.cold.3
- __97-[ATXHomeScreenEventLogger initWithHomeScreenConfigCache:biomeUIStream:PETEventTracker:defaults:]_block_invoke.23.cold.4
- __98-[ATXHomeScreenSuggestionClient _replaceSuggestionWithId:shouldSuggestionsBeDisjoint:guardedData:]_block_invoke.226
- __block_literal_global.105
- __block_literal_global.12
- __block_literal_global.121
- __block_literal_global.126
- __block_literal_global.129
- __block_literal_global.134
- __block_literal_global.164
- __block_literal_global.176
- __block_literal_global.179
- __block_literal_global.190
- __block_literal_global.210
- __block_literal_global.215
- __block_literal_global.217
- __block_literal_global.219
- __block_literal_global.296
- __block_literal_global.336
- __block_literal_global.339
- __block_literal_global.34
- __block_literal_global.371
- __block_literal_global.390
- __block_literal_global.395
- __block_literal_global.403
- __block_literal_global.460
- __block_literal_global.467
- __block_literal_global.48
- __block_literal_global.517
- __block_literal_global.52
- __block_literal_global.527
- __block_literal_global.535
- __block_literal_global.540
- __block_literal_global.549
- __block_literal_global.599
- __block_literal_global.60
- __block_literal_global.607
- __block_literal_global.64
- __block_literal_global.654
- __block_literal_global.659
- __block_literal_global.67
- __block_literal_global.676
- __block_literal_global.683
- __block_literal_global.690
- __block_literal_global.693
- __block_literal_global.701
- __block_literal_global.717
- __block_literal_global.722
- __block_literal_global.727
- __block_literal_global.736
- __block_literal_global.741
- __block_literal_global.75
- __block_literal_global.753
- __block_literal_global.762
- __block_literal_global.801
- __block_literal_global.848
- __block_literal_global.87
- __block_literal_global.870
- __block_literal_global.875
- __block_literal_global.9
- __block_literal_global.90
- __block_literal_global.94
- _fmod
- _objc_msgSend$initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:
- _objc_msgSend$initWithHomeScreenPath:ambientPath:
CStrings:
+ "%s: New first time CarPlay connection. Returning default OnBoarding suggestions"
+ "%s: No OnBoarding suggestions available, returning nil"
+ "%s: generated CarPlay smart stacks were nil"
+ "%s: generated CarPlay smart stacks. Stack1: %tu widgets, stack2: %tu widgets"
+ "%s: generating onboarding stacks for CarPlay. dayZero:%d, numDescriptors:%lu, descriptorCacheSize:%lu"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStackForCarPlayWithDescriptorCache]"
+ "-[ATXDefaultHomeScreenItemManager _generateSmartStacksForCarPlay]"
+ "-[ATXDefaultHomeScreenItemProducer carPlayOnboardingStacks]"
+ "-[ATXDefaultHomeScreenItemUpdater _updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:]"
+ "@84@0:8@16@24@32Q40B48B52B56@60@68B76B80"
+ "ATXCarPlayDefaultWidgetStacks"
+ "ATXDefaultHomeScreenItemUpdater: %s error fetching CarPlay config: %@"
+ "ATXDefaultHomeScreenItemUpdater: Error writing CarPlay defaults to file: %@"
+ "ATXDefaultHomeScreenItemUpdater: Finished updating CarPlay default stack and widget suggestions"
+ "ATXDefaultHomeScreenItemUpdater: updating defaults due to CarPlay config update"
+ "CarPlay config update"
+ "TB,R,N,V_isCarPlay"
+ "_carPlayOnboardingStacks"
+ "_carPlayPath"
+ "_generateSmartStackForCarPlayWithDescriptorCache"
+ "_generateSmartStacksForCarPlay"
+ "_isCarPlay"
+ "_readCarPlayUpdateFromFileWithCompletionHandler:"
+ "_updateCarPlayDefaultsOnQueueWithReason:appLaunchCounts:"
+ "carPlay"
+ "carPlayOnboardingStacks"
+ "com.apple.duetexpertd.ATXDefaultHomeScreenItemUpdater.updateCarPlayDefaults"
+ "com.apple.proactive.CarPlay.WidgetConfigurationManager.cacheDidUpdate"
+ "initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:isCarPlay:"
+ "initWithHomeScreenPath:ambientPath:carPlayPath:"
+ "isCHSWidgetDescriptorAllowedForCarPlayOnboardingStacks:"
+ "isCarPlay"
+ "updateDefaultsDueToCarPlayConfigUpdate"
+ "writeCarPlayUpdate:completionHandler:"
- "@80@0:8@16@24@32Q40B48B52B56@60@68B76"
- "initWithCandidateWidgets:cachedWidgetPersonalityToAppScore:personalityToDescriptorDictionary:adblDrainClassification:isiPad:isDayZeroExperience:shouldIncludeContactsWidget:cachedHasiCloudFamily:appLaunchCounts:isAmbient:"
- "initWithHomeScreenPath:ambientPath:"

```
