## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/Versions/A/AppPredictionInternal`

```diff

-584.9.0.0.0
-  __TEXT.__text: 0x481e28
-  __TEXT.__auth_stubs: 0x2c80
-  __TEXT.__objc_methlist: 0x357c4
-  __TEXT.__const: 0x2792
-  __TEXT.__cstring: 0x56eb2
-  __TEXT.__oslogstring: 0x378e6
-  __TEXT.__gcc_except_tab: 0xee08
+588.11.0.0.0
+  __TEXT.__text: 0x472e70
+  __TEXT.__auth_stubs: 0x2c10
+  __TEXT.__objc_methlist: 0x3793c
+  __TEXT.__const: 0x27c2
+  __TEXT.__cstring: 0x56e92
+  __TEXT.__oslogstring: 0x37896
+  __TEXT.__gcc_except_tab: 0xec8c
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__ustring: 0x90
-  __TEXT.__swift5_typeref: 0xce4
-  __TEXT.__constg_swiftt: 0x14f4
-  __TEXT.__swift5_reflstr: 0x67b
-  __TEXT.__swift5_fieldmd: 0x97c
+  __TEXT.__swift5_typeref: 0xd1c
+  __TEXT.__constg_swiftt: 0x14fc
+  __TEXT.__swift5_reflstr: 0x69b
+  __TEXT.__swift5_fieldmd: 0x988
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0x118
   __TEXT.__swift5_assocty: 0x1c8
   __TEXT.__swift5_capture: 0x3f8
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift_as_entry: 0xc0
+  __TEXT.__swift_as_ret: 0xac
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xd470
-  __TEXT.__eh_frame: 0x19dc
-  __TEXT.__objc_classname: 0x8a09
-  __TEXT.__objc_methname: 0xaa7bf
-  __TEXT.__objc_methtype: 0x19169
-  __TEXT.__objc_stubs: 0x4a960
-  __DATA_CONST.__got: 0x33a0
-  __DATA_CONST.__const: 0x4248
-  __DATA_CONST.__objc_classlist: 0x1ea8
+  __TEXT.__unwind_info: 0xd708
+  __TEXT.__eh_frame: 0x1a74
+  __TEXT.__objc_classname: 0x89d2
+  __TEXT.__objc_methname: 0xaa5df
+  __TEXT.__objc_methtype: 0x1912a
+  __TEXT.__objc_stubs: 0x4a900
+  __DATA_CONST.__got: 0x3390
+  __DATA_CONST.__const: 0x4258
+  __DATA_CONST.__objc_classlist: 0x1e98
   __DATA_CONST.__objc_catlist: 0x120
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1af98
+  __DATA_CONST.__objc_selrefs: 0x1b200
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x14b8
-  __DATA_CONST.__objc_arraydata: 0x12f8
-  __AUTH_CONST.__auth_got: 0x1658
-  __AUTH_CONST.__const: 0xf498
-  __AUTH_CONST.__cfstring: 0x39540
-  __AUTH_CONST.__objc_const: 0x83d28
-  __AUTH_CONST.__objc_intobj: 0x33f0
-  __AUTH_CONST.__objc_arrayobj: 0x1050
+  __DATA_CONST.__objc_superrefs: 0x14b0
+  __DATA_CONST.__objc_arraydata: 0x1360
+  __AUTH_CONST.__auth_got: 0x1620
+  __AUTH_CONST.__const: 0xf4b0
+  __AUTH_CONST.__cfstring: 0x395c0
+  __AUTH_CONST.__objc_const: 0x7ffc0
+  __AUTH_CONST.__objc_intobj: 0x33c0
+  __AUTH_CONST.__objc_arrayobj: 0x1068
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x13618
+  __AUTH.__objc_data: 0x13560
   __AUTH.__data: 0x1dd8
   __DATA.__objc_ivar: 0x49b0
-  __DATA.__data: 0x3d40
-  __DATA.__bss: 0x24a8
-  __DATA.__common: 0xb8
+  __DATA.__data: 0x3cf0
+  __DATA.__bss: 0x2478
+  __DATA.__common: 0xa8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: CF738264-FA32-3E7B-896D-5BB3140060D9
-  Functions: 23998
-  Symbols:   50992
-  CStrings:  41602
+  UUID: 9EAEAD3B-CB96-363B-A328-9928A4B319B4
+  Functions: 24291
+  Symbols:   51365
+  CStrings:  41583
 
Symbols:
+ +[ATXAWDUtils awdScoreWithScore:type:].cold.3
+ +[ATXActionFeedback sharedInstance].cold.1
+ +[ATXActionFeedbackWeights sharedInstance].cold.1
+ +[ATXActionLOIBoost sharedInstance].cold.1
+ +[ATXActionNotificationServer sharedInstance].cold.1
+ +[ATXActionPredictionBlacklist sharedInstanceWithAppPredictionBlacklist].cold.1
+ +[ATXActionPredictionBlacklist sharedInstanceWithoutAppPredictionBlacklist].cold.1
+ +[ATXActionPredictionServer sharedInstance].cold.1
+ +[ATXActivitySuggestionsFeedbackProcessor queue].cold.1
+ +[ATXAmbientLightMonitor sharedInstance].cold.1
+ +[ATXAnchorModelHyperParameters sharedInstance].cold.1
+ +[ATXAnchorModelInferenceEngine sharedInstance].cold.1
+ +[ATXAppDirectoryOrderingProvider sharedInstance].cold.1
+ +[ATXAppDirectoryServer sharedInstance].cold.1
+ +[ATXAppFeaturizer _predictNextAppLaunchEmbedding:into:launchSequence:].cold.1
+ +[ATXAppLaunchLogger sharedInstance].cold.1
+ +[ATXAppPredictionBlacklist sharedInstance].cold.1
+ +[ATXBBNotificationManager sharedInstance].cold.1
+ +[ATXCandidateRelevanceModelGlobals sharedInstance].cold.1
+ +[ATXCandidateRelevanceModelServerCoordinator sharedInstance].cold.1
+ +[ATXClientModelSuggestionReceiver sharedInstance].cold.1
+ +[ATXComplicationSuggestionParameters sharedInstance].cold.1
+ +[ATXContextHeuristicsServer sharedInstance].cold.1
+ +[ATXDailyRoutinesTriggerManager sharedInstance].cold.1
+ +[ATXDefaultWidgetSuggesterServer sharedInstance].cold.1
+ +[ATXDeviceStateMonitor airplaneMode].cold.1
+ +[ATXDeviceStateMonitor setAirplaneMode:].cold.1
+ +[ATXDeviceStateMonitor setSSID:].cold.1
+ +[ATXDigitalHealthBlacklist sharedInstance].cold.1
+ +[ATXDistributedNotificationHandler sharedInstance].cold.1
+ +[ATXFaceSuggestionServer sharedInstance].cold.1
+ +[ATXFakeCoreAnalyticsLogger sharedInstance].cold.1
+ +[ATXFallbackActionsFeedback sharedInstance].cold.1
+ +[ATXGamePlayKitRandomSource sharedRandom].cold.1
+ +[ATXGlobalAppScorePredictor sharedInstance].cold.1
+ +[ATXHeroAndClipConstants sharedInstance].cold.1
+ +[ATXHomeScreenLogSystemChangeDictionary systemChangeDictionaryAccumulatorKeys].cold.1
+ +[ATXHomeScreenLogSystemEventDictionaries systemLevelDictionaryAccumulatorKeys].cold.1
+ +[ATXHomeScreenLogSystemEventDictionaries systemLevelDictionaryAccumulatorSplitByLocationKeys].cold.1
+ +[ATXHomeScreenLogUploaderUtilities abGroup].cold.1
+ +[ATXHomeScreenLogWidgetAddSheetDictionaries rankKeysSplitBySize].cold.1
+ +[ATXHomeScreenLogWidgetEventDictionaries widgetEventDictionaryAccumulatorSplitByLocationKeys].cold.1
+ +[ATXHomeScreenLogWidgetRotationDictionaries widgetRotationDictionaryAccumulatorKeys].cold.1
+ +[ATXInfoSuggestionServer sharedInstance].cold.1
+ +[ATXLocationManager(Singleton) sharedInstance].cold.1
+ +[ATXLockScreenNotificationRankerServer sharedInstance].cold.1
+ +[ATXMLActionProducer consumerSubTypesToUpdate].cold.1
+ +[ATXMagicalMomentsAppPredictor sharedInstance].cold.2
+ +[ATXMagicalMomentsContexts eventIdentifierPredicateForValue:].cold.1
+ +[ATXMagicalMomentsContexts loiPredicateForUUIDString:].cold.1
+ +[ATXMagicalMomentsPredictionTableEntry compoundPredicateFromPredicateArray:].cold.1
+ +[ATXModeAnchorModelSuggestionClient sharedInstance].cold.1
+ +[ATXModeAutomationSuggestionTester sharedInstance].cold.1
+ +[ATXModeEntityScorerServer sharedInstance].cold.1
+ +[ATXModeMetadataConstants sharedInstance].cold.1
+ +[ATXNotificationCategorizationServer sharedInstance].cold.1
+ +[ATXNotificationDigestRankerServer sharedInstance].cold.1
+ +[ATXNotificationDigestRankingConstants sharedInstance].cold.1
+ +[ATXNotificationsDedupeTracker sharedInstance].cold.1
+ +[ATXNotificationsLoggingServer sharedInstance].cold.1
+ +[ATXPOICategoryVisitDuetDataProvider sharedInstance].cold.1
+ +[ATXPosterConfigurationCache sharedInstance].cold.1
+ +[ATXPosterDescriptorCache sharedInstance].cold.1
+ +[ATXPredictionJSONScoreLogger sharedInstance].cold.1
+ +[ATXPrivacyReset sharedInstance].cold.1
+ +[ATXRSWidgetSuggestionProducer replacementContainerBundleIdForDonationBundleId:].cold.1
+ +[ATXScoreInterpreterCache sharedInstance].cold.1
+ +[ATXScoreInterpreterFromAssetBuilder interpreterFromAssetFilename:].cold.1
+ +[ATXScoreInterpreterFromAssetBuilder interpreterFromAssetFilename:].cold.2
+ +[ATXServer consumerSubTypesToUpdate].cold.1
+ +[ATXServer sharedInstance].cold.1
+ +[ATXSettingsActionsServer sharedInstance].cold.1
+ +[ATXSleepSuggestionServer sharedInstance].cold.1
+ +[ATXSlotResolution isNotLaunchedWithinShortTimeSpan:].cold.1
+ +[ATXSmartActivationEarlyExitDetectionLogger sharedInstance].cold.1
+ +[ATXStackStateTracker sharedInstance].cold.1
+ +[ATXSuggestionModeFilter sharedInstance].cold.1
+ +[ATXUpdatePredictionsManager sharedInstance].cold.1
+ +[ATXUsageInsightsServer sharedInstance].cold.1
+ +[ATXWidgetSuggestionAbuseGuard sharedInstance].cold.1
+ +[ATXWifiStateMonitor sharedInstance].cold.1
+ +[_ATXActionUtils getActionTypesFromActionKeys:].cold.1
+ +[_ATXActionUtils getBundleIdsFromActionKeys:].cold.1
+ +[_ATXActionUtils limitParameterCombinations:limit:].cold.1
+ +[_ATXAggregateLogger sharedInstance].cold.1
+ +[_ATXAggregateLogger stringForPredictedItemOutcome:].cold.1
+ +[_ATXAggregateLogger stringForPredictionOutcome:].cold.1
+ +[_ATXAppIconState sharedInstance].cold.1
+ +[_ATXAppInfoManager sharedInstance].cold.1
+ +[_ATXAppLaunchCategoricalHistogram stringForPruningMethod:].cold.2
+ +[_ATXAppLaunchSequenceManager sharedInstance].cold.1
+ +[_ATXBundleIdSet sharedInstance].cold.1
+ +[_ATXDataStore sharedInstance].cold.1
+ +[_ATXDataStoreMigrations migrations].cold.1
+ +[_ATXDuetHelper sharedInstance].cold.1
+ +[_ATXFeedback sharedInstance].cold.1
+ +[_ATXFeedbackConstants actionDecayHalfLifeSeconds].cold.1
+ +[_ATXFeedbackConstants alphaForBundleId:].cold.1
+ +[_ATXFeedbackConstants baseAlpha].cold.1
+ +[_ATXFeedbackConstants baseBeta].cold.1
+ +[_ATXFeedbackConstants betaForBundleId:].cold.1
+ +[_ATXFeedbackConstants decayHalfLifeSeconds].cold.1
+ +[_ATXFeedbackConstants multiplierForAppAlphasAndBetas].cold.1
+ +[_ATXGlobals sharedInstance].cold.1
+ +[_ATXInspectionServer sharedInstance].cold.1
+ +[_ATXScoreTypes mappingForDayOfWeekDistributionSignals:forScoreInputCategory:].cold.1
+ +[_ATXScoreTypes mappingForTimeOfDayDistributionSignals:forScoreInputCategory:].cold.1
+ +[_ATXScoreTypes mappingForTimeOfDayDistributionSignals:forScoreInputCategory:].cold.2
+ +[_ATXScoreTypes mappingForTopRankedCoarseGeoHashSignals:forScoreInputCategory:].cold.1
+ +[_ATXScoreTypes mappingForTopRankedCoarseGeoHashSignals:forScoreInputCategory:].cold.2
+ +[_ATXScoreTypes mappingForTopRankedSpecificGeoHashSignals:forScoreInputCategory:].cold.1
+ +[_ATXScoreTypes mappingForTopRankedSpecificGeoHashSignals:forScoreInputCategory:].cold.2
+ +[_ATXScoreTypes mappingForTopRankedZoom7GeoHashSignals:].cold.1
+ +[_ATXScoreTypes scoreInputForString:].cold.1
+ -[ATXActionFeedback applyFinalFeedbackForActionResponse:engagementType:context:].cold.5
+ -[ATXActionFeedback applyFinalFeedbackForActionResponse:engagementType:context:].cold.6
+ -[ATXActionFeedback logHeuristicFeedbackToSuggestionsForAction:withActionType:].cold.2
+ -[ATXActionFeedbackWeights confirmWeightForFeedbackStage:consumerSubType:].cold.1
+ -[ATXActionFeedbackWeights confirmWeightForFeedbackStage:consumerSubType:].cold.2
+ -[ATXActionFeedbackWeights rejectWeightForFeedbackStage:consumerSubType:].cold.1
+ -[ATXActionFeedbackWeights rejectWeightForFeedbackStage:consumerSubType:].cold.2
+ -[ATXActionTimeEstimateAWDTracker _writeTimestamp:].cold.1
+ -[ATXAnchorModelOfflineDataHarvester initWithSamplingGroup:userId:].cold.1
+ -[ATXApp2VecMapping getVectorForBundleId:into:].cold.3
+ -[ATXApp2VecMapping initWithPath:].cold.5
+ -[ATXAppIntentDuetEvent initWithDKEvent:].cold.5
+ -[ATXAppLaunchDuetEvent initWithDKEvent:].cold.6
+ -[ATXAppLaunchEventProvider biomePublisherWithBookmark:].cold.1
+ -[ATXAudioDuetEvent initWithDKEvent:].cold.6
+ -[ATXBluetoothDuetEvent initWithDKEvent:].cold.5
+ -[ATXCandidateRelevanceModelTrainer generateAndSaveDatasetWithFilename:].cold.1
+ -[ATXCarPlayDuetEvent initWithDKEvent:].cold.2
+ -[ATXChargerPluggedInDuetEvent initWithDKEvent:].cold.3
+ -[ATXClientModelSuggestionReceiver blendingLayerUpdatedUICache:consumerSubType:].cold.1
+ -[ATXClientModelSuggestionReceiver blendingLayerUpdatedUICache:consumerSubType:].cold.2
+ -[ATXClientModelSuggestionReceiver blendingLayerUpdatedUICache:consumerSubType:].cold.3
+ -[ATXCorrelatedEventsDateBuffer endDateWithBufferForEvent:].cold.1
+ -[ATXCorrelatedEventsDateBuffer startDateWithBufferForEvent:].cold.1
+ -[ATXDegenerateStackAnalyzer isSmartStackPossiblyDegenerate:onPage:usingTimelineEntriesSinceDate:].cold.1
+ -[ATXDuetEvent initWithDKEvent:].cold.1
+ -[ATXEvent initWithEvent:startDate:endDate:].cold.1
+ -[ATXEvent initWithEvent:startDate:endDate:].cold.2
+ -[ATXEvent initWithEvent:startDate:endDate:].cold.3
+ -[ATXHistogramTable initWithDict:usedIds:datastore:blobType:].cold.2
+ -[ATXLocationVisitDuetEvent initWithLocationOfInterestIdentifier:startDate:endDate:].cold.1
+ -[ATXMediaApplications appSupportsMedia:].cold.1
+ -[ATXMicrolocationVisitDuetEvent initWithDKEvent:].cold.4
+ -[ATXMinimalSlotResolutionParameters initWithParameterHash:slotHash:uuid:paramCount:].cold.1
+ -[ATXModeFaceSuggestionGenerator _facesForModeType:modeUUID:allDescriptors:].cold.1
+ -[ATXMotionStateDuetEvent initWithDKEvent:].cold.2
+ -[ATXNotificationAndSuggestionDatabase updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:]
+ -[ATXNotificationAndSuggestionDatastore _appLaunchPublisher]
+ -[ATXNotificationAndSuggestionDatastore updateNotificationsWithNextAppLaunchTimestamp:bundleId:startTimestamp:]
+ -[ATXNotificationTelemetryQueryResult nextAppLaunchTimestamp]
+ -[ATXNotificationTelemetryQueryResult setNextAppLaunchTimestamp:]
+ -[ATXNowPlayingDuetEvent initWithDKEvent:].cold.6
+ -[ATXProactiveSuggestionPartialIntentHandlingPublisher _timestampFromEvent:].cold.2
+ -[ATXRootOfAppDataWithHashes serialize].cold.1
+ -[ATXScoreDict initWithDefaultValueForScoreTypeKeys].cold.1
+ -[ATXScreenLockStateDuetEvent initWithDKEvent:].cold.2
+ -[ATXServer sendFeedbackForConsumerType:consumerSubType:atxResponse:engagementType:engagedBundleId:bundleIdsShown:explicitlyRejectedBundleIds:reply:].cold.1
+ -[ATXSlotResolutionParametersStatistics _confirmRatio].cold.1
+ -[ATXSlotResolutionParametersStatistics _confirmRatio].cold.2
+ -[ATXSlotResolutionStatistics initWithActionKey:].cold.1
+ -[ATXSuggestedPagesContactsWidgetDataSource _createMediumContactsWidgetForPeople:entities:].cold.2
+ -[ATXSuggestedPagesContactsWidgetDataSource _createMediumContactsWidgetForPeople:entities:].cold.3
+ -[ATXSuggestedPagesContactsWidgetDataSource _createSmallContactsWidgetForPeople:].cold.2
+ -[ATXSuggestedPagesGenerator _suggestAppsFromPool:forPage:type:numberOfAppsNecessary:].cold.1
+ -[ATXSuggestedPagesGenerator _suggestShortcutsFromPool:forPage:type:numberOfShortcutsNecessary:].cold.1
+ -[ATXSuggestedPagesStackLayoutFourSmallOnTop layOutStacks:numberOfColumns:forPageType:].cold.1
+ -[ATXSuggestedPagesStackLayoutSmallSpiral layOutStacks:numberOfColumns:forPageType:].cold.1
+ -[ATXSuggestedPagesStackLayoutTwoLarge layOutStacks:numberOfColumns:forPageType:].cold.1
+ -[ATXSuggestedPagesStackLayoutTwoMedium layOutStacks:numberOfColumns:forPageType:].cold.1
+ -[ATXSuggestedPagesStackLayoutTwoSmallOnTop layOutStacks:numberOfColumns:forPageType:].cold.1
+ -[ATXSuggestionDeduplicator executableClassStringsToUnarchiveDuringComparison].cold.1
+ -[ATXTimelineRelevanceAdoption persistQuotasWithActivity:].cold.2
+ -[_ATXAppDailyDose _writeHistoricalDoseWithCompletion:].cold.1
+ -[_ATXAppDailyDose addLaunchForBundleId:date:completion:].cold.1
+ -[_ATXAppDailyDose addLaunchForBundleId:date:completion:].cold.2
+ -[_ATXAppDailyDose initWithDuetHelper:].cold.1
+ -[_ATXAppDailyDose initWithDuetHelper:].cold.2
+ -[_ATXAppDailyDose initWithDuetHelper:timeZone:today:alpha:historicalDosePath:completion:].cold.1
+ -[_ATXAppDailyDose stopAppUsageAtDate:].cold.1
+ -[_ATXAppHistoricalAverageDose skipTo:].cold.1
+ -[_ATXAppInfo initWithBundleId:isExtension:isEnterpriseApp:installDate:lastLaunch:lastSpotlightLaunch:averageSecondsBetweenLaunches:medianSecondsBetweenLaunches:genreId:subGenreIds:app2VecCluster:].cold.1
+ -[_ATXAppInfoManager initWithDataStore:].cold.2
+ -[_ATXAppLaunchCategoricalHistogram _reduceCategoryCountTo:].cold.2
+ -[_ATXAppLaunchCategoricalHistogram _tryGetCategoryIdforCategory:createIfMissing:categoryIdOut:].cold.1
+ -[_ATXAppLaunchCategoricalHistogram _tryGetEventIdforBundleId:createIfMissing:eventIdOut:].cold.1
+ -[_ATXAppLaunchCategoricalHistogram bundleIDCountForCategory:]
+ -[_ATXAppLaunchCategoricalHistogram bundleIDCountForCategory:].cold.1
+ -[_ATXAppLaunchCategoricalHistogram purgeUnusedCategories]
+ -[_ATXAppLaunchCategoricalHistogram purgeUnusedCategories].cold.1
+ -[_ATXAppLaunchSequenceManager initWithDataStore:].cold.2
+ -[_ATXAppLaunchSequenceManager launchSequenceForAppAction:].cold.1
+ -[_ATXAppLaunchSequenceManager launchSequenceForBundle:].cold.1
+ -[_ATXCategoricalHistogram initWithCoder:].cold.1
+ -[_ATXDataStore appIntentDuetEventsForActionsBetweenStartDate:endDate:].cold.1
+ -[_ATXDataStore appIntentDuetEventsForActionsBetweenStartDate:endDate:].cold.2
+ -[_ATXDataStore enumerateActionOfType:bundleId:block:].cold.1
+ -[_ATXDataStore enumerateActionOfType:bundleId:block:].cold.2
+ -[_ATXDataStore enumerateActionOfType:bundleId:block:].cold.3
+ -[_ATXDataStore enumerateActionsInUUIDSet:block:].cold.1
+ -[_ATXDataStore enumerateActionsInUUIDSet:block:].cold.2
+ -[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:].cold.1
+ -[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:].cold.2
+ -[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:].cold.3
+ -[_ATXDataStore enumerateSlotUuidsOfType:bundleId:block:].cold.1
+ -[_ATXDataStore enumerateSlotUuidsOfType:bundleId:block:].cold.2
+ -[_ATXDataStore enumerateSlotUuidsOfType:bundleId:block:].cold.3
+ -[_ATXDataStore initWithPath:andDuetHelper:].cold.3
+ -[_ATXDataStore migrationPre44WriteActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:].cold.2
+ -[_ATXDataStore migrationPre44WriteActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:].cold.3
+ -[_ATXDataStore migrationPre44WriteActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:].cold.4
+ -[_ATXDataStore migrationPre44WriteActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:].cold.5
+ -[_ATXDataStore migrationPre44WriteActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:].cold.6
+ -[_ATXDataStore migrationPre44WriteActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:].cold.7
+ -[_ATXDataStore minimalActionParametersforActionsBetweenStartDate:endDate:limit:].cold.1
+ -[_ATXDataStore minimalActionParametersforActionsBetweenStartDate:endDate:limit:].cold.2
+ -[_ATXDataStore numActionKeyOccurrencesBetweenStartDate:endDate:].cold.1
+ -[_ATXDataStore numActionKeyOccurrencesBetweenStartDate:endDate:].cold.2
+ -[_ATXDataStore numActionKeyOccurrencesForActionKey:startDate:endDate:].cold.1
+ -[_ATXDataStore numActionKeyOccurrencesForActionKey:startDate:endDate:].cold.2
+ -[_ATXDataStore numActionKeyOccurrencesForActionKey:startDate:endDate:].cold.3
+ -[_ATXDataStore numActionParameterHashOccurrencesForActionKey:parameterHash:startDate:endDate:].cold.1
+ -[_ATXDataStore numActionParameterHashOccurrencesForActionKey:parameterHash:startDate:endDate:].cold.2
+ -[_ATXDataStore numActionParameterHashOccurrencesForActionKey:parameterHash:startDate:endDate:].cold.3
+ -[_ATXDataStore numBundleIdOccurrencesForBundleId:startDate:endDate:].cold.1
+ -[_ATXDataStore numBundleIdOccurrencesForBundleId:startDate:endDate:].cold.2
+ -[_ATXDataStore numBundleIdOccurrencesForBundleId:startDate:endDate:].cold.3
+ -[_ATXDataStore regenerateSlotSetKeyForBundleId:].cold.1
+ -[_ATXDataStore removeActionDataForActionUUID:].cold.1
+ -[_ATXDataStore removeActionDataForActionUUIDs:].cold.1
+ -[_ATXDataStore removeActionDataForBundleId:].cold.1
+ -[_ATXDataStore updateOrInsertGenreId:subGenreIds:forBundleId:].cold.1
+ -[_ATXDataStore updateOrInsertInstallTimestamp:genreId:subGenreIds:app2VecCluster:forBundleId:isExtension:isEnterpriseApp:].cold.1
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.2
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.3
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.4
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.5
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.6
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.7
+ -[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:].cold.8
+ -[_ATXDataStore writeAppActionLaunches:followingAppAction:].cold.1
+ -[_ATXDataStore writeAppActionLaunches:followingAppAction:].cold.2
+ -[_ATXDataStore writeAppActionLaunches:followingAppAction:].cold.3
+ -[_ATXDataStore writeLaunches:followingBundle:].cold.1
+ -[_ATXDataStore writeLaunches:followingBundle:].cold.2
+ -[_ATXDataStore writeLaunches:followingBundle:].cold.3
+ -[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:].cold.1
+ -[_ATXDeprecatedScoreInterpreter _evalVariable:withCtx:].cold.3
+ -[_ATXDuetHelper _enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:batchSize:ascending:block:].cold.1
+ -[_ATXDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:batchSize:ascending:block:].cold.1
+ -[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:].cold.1
+ -[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:].cold.2
+ -[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:].cold.1
+ -[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:].cold.2
+ -[_ATXDuetHelper registerDeletionHandler:queue:].cold.1
+ -[_ATXDuetHelper registerDeletionHandler:queue:].cold.2
+ -[_ATXGlobals blacklistedAppActionsHelper:].cold.1
+ -[_ATXInternalNotification initWithNotificationName:].cold.1
+ -[_ATXNeuralNetwork _predict:freeInputsAfterUse:].cold.1
+ -[_ATXNeuralNetwork initWithData:].cold.1
+ -[_ATXNeuralNetworkBuilder addHiddenLayer:weights:bias:activation:skip:].cold.1
+ -[_ATXNeuralNetworkBuilder addHiddenLayer:weights:bias:activation:skip:].cold.2
+ -[_ATXNeuralNetworkBuilder addOutputLayer:weights:bias:activation:softmax:].cold.1
+ -[_ATXNeuralNetworkBuilder addOutputLayer:weights:bias:activation:softmax:].cold.2
+ -[_ATXNeuralNetworkBuilder serialize].cold.1
+ -[_ATXNeuralNetworkBuilder serialize].cold.2
+ -[_ATXRecentInstallCache initTrackingAppsMoreRecentThan:installMonitor:uninstallMonitor:].cold.1
+ -[_ATXRecentInstallCache initTrackingAppsMoreRecentThan:installMonitor:uninstallMonitor:].cold.2
+ -[_ATXRecentInstallCache initTrackingAppsMoreRecentThan:installMonitor:uninstallMonitor:].cold.3
+ -[_ATXScoreInterpreter _compileToBytecode:].cold.1
+ -[_ATXScoreInterpreter _compileToBytecode:].cold.2
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.13
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.14
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.15
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.16
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.17
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.18
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.19
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.20
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.21
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.22
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.23
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.24
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.25
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.26
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.27
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.28
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.29
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.30
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.31
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.32
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.33
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.34
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.35
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.36
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.37
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.38
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.39
+ -[_ATXScoreInterpreter _runOperator:arity:context:].cold.40
+ ATXUpdatePredictions.cold.2
+ GCC_except_table107
+ GCC_except_table111
+ GCC_except_table119
+ GCC_except_table127
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table142
+ GCC_except_table147
+ GCC_except_table163
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table72
+ GCC_except_table85
+ GCC_except_table90
+ GCC_except_table97
+ OBJC_IVAR_$_ATXNotificationAndSuggestionDatastore._appLaunchPublisher
+ OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._nextAppLaunchTimestamp
+ _ATXCopySqliteDatabaseClassC.cold.3
+ _ATXCopySqliteDatabaseClassC.cold.4
+ _ATXInitializeInOwnerProcess.cold.1
+ _DNDModeSemanticTypeFromSuggestedFaceType
+ _OBJC_$_PROP_LIST_ATXProactiveSuggestionClientModelEvaluatorPublishers.185
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _PROTOCOLS__TtC21AppPredictionInternal31ContextualEngineSuggestionStore.5
+ _ZL27__atx_xpc_private_queue_getv.cold.1
+ _ZL7entropyRKN9proactive3pas15SynchronizedPtrIN12_GLOBAL__N_113HDGuardedDataENS0_6detail14RecursiveMutexEEEtt.cold.1
+ _ZL7entropyRKN9proactive3pas15SynchronizedPtrIN12_GLOBAL__N_113HDGuardedDataENS0_6detail14RecursiveMutexEEEtt.cold.2
+ __101-[ATXHomeScreenWidgetDiscoverabilityLogHarvester _logRankBasedMetricsWithOnboardingStacks:algorithm:]_block_invoke.180
+ __102-[ATXAppSessionInterruptionsProvider cacheRecommendedAndCandidateAppsInDenyListForAllModesIfNecessary]_block_invoke.38
+ __102-[ATXDigestOnboardingAppSelectionMetricsLogger logDigestOnboardingAppSelectionMetricsWithXPCActivity:]_block_invoke.26
+ __103-[ATXAppSessionInterruptionsProvider cacheRecommendedAndCandidateAppsInAllowListForAllModesIfNecessary]_block_invoke.34
+ __103-[ATXAppSessionInterruptionsProvider cacheRecommendedAndCandidateAppsInAllowListForAllModesIfNecessary]_block_invoke.36
+ __103-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:completion:]_block_invoke.298
+ __103-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:completion:]_block_invoke.301
+ __105-[ATXAnchorModelDataStoreWrapper uniqueCandidateIdsThatOccurredAfterAnchor:candidateType:minOccurrences:]_block_invoke.407
+ __105-[ATXAnchorModelDataStoreWrapper uniqueCandidateIdsThatOccurredAfterAnchor:candidateType:minOccurrences:]_block_invoke_2.408
+ __105-[ATXAnchorModelDataStoreWrapper uniqueCandidateIdsThatOccurredAfterAnchor:candidateType:minOccurrences:]_block_invoke_2.408.cold.1
+ __105-[ATXNotificationAndSuggestionDatabase updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:]_block_invoke.148
+ __105-[ATXNotificationAndSuggestionDatabase updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:]_block_invoke.148.cold.1
+ __107-[ATXAppGroupedNotificationDigestRanker getRankedAppsFromAppGroupedNotificationStacks:maxAppMarqueeGroups:]_block_invoke.132
+ __110-[ATXAnchorModelDataStoreWrapper assignMetricsForTrainingResult:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.156
+ __110-[ATXAnchorModelDataStoreWrapper assignMetricsForTrainingResult:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.156.cold.1
+ __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke.175
+ __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.177
+ __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.177.cold.1
+ __110-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromFileData:digestTimeString:outError:]_block_invoke.56
+ __110-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromFileData:digestTimeString:outError:]_block_invoke.58
+ __110-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromFileData:digestTimeString:outError:]_block_invoke.58.cold.1
+ __111-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromFileData:modeString:outError:]_block_invoke.66
+ __111-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromFileData:modeString:outError:]_block_invoke.67
+ __111-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromFileData:modeString:outError:]_block_invoke.67.cold.1
+ __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.457
+ __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.457.cold.1
+ __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.105
+ __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.105.cold.1
+ __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.50
+ __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.50.cold.1
+ __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke.260
+ __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.272
+ __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.272.cold.1
+ __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.133
+ __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.133.cold.1
+ __114-[ATXAnchorModelDataStoreWrapper insertAnchorSuggestionOutcome:date:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.149
+ __114-[ATXAnchorModelDataStoreWrapper insertAnchorSuggestionOutcome:date:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.149.cold.1
+ __114-[ATXCandidateRelevanceModelDataStore writeVerificationStatusForModelUUID:clientModelName:expectedNumberOfModels:]_block_invoke.384
+ __114-[ATXHomeScreenLayoutSelector2 _assignExistingSuggestedSGWidgetsOnPages:withSuggestions:suggestionToRankingIndex:]_block_invoke.52
+ __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.199
+ __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.199.cold.1
+ __115+[ATXCandidateRelevanceModelDatasetGeneratorConfigMinimalAction candidatePublisherFromStartTime:endTime:datastore:]_block_invoke.107
+ __115+[ATXCandidateRelevanceModelDatasetGeneratorConfigMinimalAction candidatePublisherFromStartTime:endTime:datastore:]_block_invoke.107.cold.1
+ __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.196
+ __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.196.cold.1
+ __116-[ATXWidgetPredictionTrainer trainWidgetPredictionModelWithMLArrayBatchProvider:modelURL:andSaveToURL:withActivity:]_block_invoke.29
+ __116-[ATXWidgetPredictionTrainer trainWidgetPredictionModelWithMLArrayBatchProvider:modelURL:andSaveToURL:withActivity:]_block_invoke.29.cold.1
+ __116-[ATXWidgetPredictionTrainer trainWidgetPredictionModelWithMLArrayBatchProvider:modelURL:andSaveToURL:withActivity:]_block_invoke.29.cold.2
+ __118-[ATXInformationEngine initWithFilter:featurizer:ranker:infoStore:confidenceMapper:abuseControlConfig:featureWeights:]_block_invoke.39
+ __119-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:clientModelName:completion:]_block_invoke.308
+ __119-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:clientModelName:completion:]_block_invoke_2.309
+ __121-[ATXCandidateRelevanceModelDatasetGenerator initWithConfig:inferredModeStream:computedModeStream:pointOfInterestStream:]_block_invoke.137
+ __121-[ATXPredictionContextBuilder(CandidateContext) predictionContextForCurrentContextAndCandidatePublisher:contextOverride:]_block_invoke.11
+ __122-[ATXProactiveSuggestionShadowLogger enumerateShadowLoggingResultsWithBlock:clientModelCacheUpdatedBlock:completionBlock:]_block_invoke.27
+ __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.30
+ __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.30.cold.1
+ __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.30.cold.2
+ __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.38
+ __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.45
+ __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.45.cold.1
+ __123-[_ATXDataStore updateOrInsertInstallTimestamp:genreId:subGenreIds:app2VecCluster:forBundleId:isExtension:isEnterpriseApp:]_block_invoke.1171
+ __123-[_ATXDataStore updateOrInsertInstallTimestamp:genreId:subGenreIds:app2VecCluster:forBundleId:isExtension:isEnterpriseApp:]_block_invoke.1171.cold.1
+ __124-[ATXStableContactRepresentationDatabase insertCnContactIdToStableContactIdentifierWithCnContactId:stableContactIdentifier:]_block_invoke.11
+ __124-[ATXStableContactRepresentationDatabase insertCnContactIdToStableContactIdentifierWithCnContactId:stableContactIdentifier:]_block_invoke.11.cold.1
+ __125-[ATXNotificationTelemetryLogger userNotificationWithUUID:withTimeStamp:urgency:fromNotificationStreamWithStartTime:endTime:]_block_invoke.40
+ __130-[ATXNPlusOneStudyUploader _processClientModelUpdateStreamFromStartTime:shortcutSuggestionHandler:infoSuggestionHandler:activity:]_block_invoke.234
+ __130-[ATXNPlusOneStudyUploader _processClientModelUpdateStreamFromStartTime:shortcutSuggestionHandler:infoSuggestionHandler:activity:]_block_invoke.234.cold.1
+ __131-[_ATXAppLaunchCategoricalHistogram initWithHistogram:categoryToCategoryId:maxCategoryId:maxCategoryCount:lastDates:pruningMethod:]_block_invoke.62
+ __131-[_ATXAppLaunchCategoricalHistogram initWithHistogram:categoryToCategoryId:maxCategoryId:maxCategoryCount:lastDates:pruningMethod:]_block_invoke.62.cold.1
+ __135-[ATXPredictionDataHistograms initWithAppInfoManager:bundleIdTable:launchSequenceManager:histogramManager:dataStore:persistHistograms:]_block_invoke.31
+ __136+[ATXAppPredictorFeedback constructFeatureDictionaryWithFeedbackItems:engagedItem:shownItemIndexes:consumerType:histogramBundleIdTable:]_block_invoke.66
+ __140-[ATXAnchorModelEventHarvester fetchAppLaunchEventsAfterAnchorOccurrenceDate:limit:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.25
+ __140-[ATXAnchorModelEventHarvester fetchAppLaunchEventsAfterAnchorOccurrenceDate:limit:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.25.cold.1
+ __140-[ATXAnchorModelEventHarvester fetchAppLaunchEventsAfterAnchorOccurrenceDate:limit:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.28
+ __143-[ATXAnchorModelEventHarvester fetchEventsAfterAnchorOccurenceDate:withBiomePublisher:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.17
+ __143-[ATXAnchorModelEventHarvester fetchEventsAfterAnchorOccurenceDate:withBiomePublisher:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.17.cold.1
+ __143-[ATXAnchorModelEventHarvester fetchEventsAfterAnchorOccurenceDate:withBiomePublisher:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.20
+ __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.74
+ __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.74.cold.1
+ __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.76
+ __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.76.cold.1
+ __145-[ATXInformationEngine _pushPredictionsToBlendingLayerIfDifferentFromTheLastCacheUpdate:forClientModel:withClientModelVersion:cachedSuggestions:]_block_invoke.61
+ __146-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromSource:digestTimeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.61
+ __146-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromSource:digestTimeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.61.cold.1
+ __147-[ATXHomeScreenWidgetDiscoverabilityLogHarvester _generateWidgetDiscoverabilityMetricsWithHomeScreenItemProducer:descriptors:appMetrics:algorithm:]_block_invoke.160
+ __147-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromSource:modeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.68
+ __147-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromSource:modeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.68.cold.1
+ __149-[_ATXAppLaunchMonitor handleAppOrClipLaunchNotificationForBundleId:poweringAppClipBundleId:urlHash:isClip:appLaunchReason:appClipLaunchReason:date:]_block_invoke.136
+ __173-[ATXTimelineRelevanceMetricHarvester _addRotationHistoryForWidgetBundleId:appBundleId:widgetKind:widgetSize:withPBTimelineRelevanceContainer:anonymizeTimestampsRelativeTo:]_block_invoke.143
+ __173-[ATXTimelineRelevanceMetricHarvester _addRotationHistoryForWidgetBundleId:appBundleId:widgetKind:widgetSize:withPBTimelineRelevanceContainer:anonymizeTimestampsRelativeTo:]_block_invoke.143.cold.1
+ __173-[ATXTimelineRelevanceMetricHarvester _addRotationHistoryForWidgetBundleId:appBundleId:widgetKind:widgetSize:withPBTimelineRelevanceContainer:anonymizeTimestampsRelativeTo:]_block_invoke.145
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.101
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.106
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.114
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.116
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.125
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.125.cold.1
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.132
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.88
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.96
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.102
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.107
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.115
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.117
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.133
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.89
+ __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.97
+ __188+[ATXActionPredictions _predictionsForConsumerSubType:thirdStageScoreLogger:multiStageScoreLogger:context:actionPredictionCandidates:remainingPredictionItems:predictionsPerAppActionLimit:]_block_invoke.69
+ __188+[ATXActionPredictions _predictionsForConsumerSubType:thirdStageScoreLogger:multiStageScoreLogger:context:actionPredictionCandidates:remainingPredictionItems:predictionsPerAppActionLimit:]_block_invoke.69.cold.1
+ __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke.558
+ __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke.563
+ __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_2.559
+ __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_2.567
+ __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_3.560
+ __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_3.560.cold.1
+ __200-[_ATXAppPredictor predictWithLimit:consumerSubType:intent:candidateBundleIdentifiers:candidateActiontypes:scoreLogger:predictionItemsToKeep:predictedItemsOutParameter:context:datastore:featureCache:]_block_invoke.159
+ __209-[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]_block_invoke.47
+ __209-[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]_block_invoke.51
+ __212-[ATXRSWidgetSuggestionProducer initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.41
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.47
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.47.cold.1
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.48
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.48.cold.1
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.61
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.64
+ __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.64.cold.1
+ __27-[_ATXAppIconState _reload]_block_invoke.66
+ __28-[_ATXDataStore loadAppInfo]_block_invoke.322
+ __29-[_ATXAppLaunchMonitor start]_block_invoke.78
+ __29-[_ATXAppLaunchMonitor start]_block_invoke.82
+ __30-[ATXLockscreenBlacklist init]_block_invoke.30
+ __30-[ATXLockscreenBlacklist init]_block_invoke.32
+ __30-[_ATXFeedback doDecayAtTime:]_block_invoke.72
+ __31-[ATXFaceSuggestionServer init]_block_invoke.30
+ __31-[ATXFaceSuggestionServer init]_block_invoke.44
+ __33-[ATXAppModeModel scoredEntities]_block_invoke.27
+ __34-[ATXAppLaunchMicroLocation train]_block_invoke.65
+ __34-[ATXAppLaunchMicroLocation train]_block_invoke.65.cold.1
+ __34-[ATXAppLaunchMicroLocation train]_block_invoke.74
+ __34-[ATXHistogramData countWhereA:b:]_block_invoke.26
+ __34-[_ATXDataStore loadAppActionInfo]_block_invoke.329
+ __37-[ATXContactModeModel scoredEntities]_block_invoke.30
+ __38-[_ATXInspectionServer getActionLogs:]_block_invoke.201
+ __41-[ATXAppModeDenyListModel scoredEntities]_block_invoke.27
+ __41-[ATXClientModelSuggestionReceiver start]_block_invoke.40
+ __41-[ATXClientModelSuggestionReceiver start]_block_invoke.40.cold.1
+ __41-[ATXDuetKnowledgeStoreManager runBlock:]_block_invoke.7
+ __41-[_ATXAppLaunchLocation loadModelAtPath:]_block_invoke.101
+ __41-[_ATXAppLaunchLocation loadModelAtPath:]_block_invoke.89
+ __43+[ATXActionPredictionsProcessor userAlarms]_block_invoke.49
+ __43+[ATXActionPredictionsProcessor userAlarms]_block_invoke.49.cold.1
+ __43-[ATXModeAnchorModelSuggestionClient _init]_block_invoke.12
+ __43-[ATXNotificationCategorizationServer init]_block_invoke.42
+ __43-[ATXNotificationCategorizationServer init]_block_invoke_2.47
+ __43-[_ATXDataStore _appInfoForBundleIdNoSync:]_block_invoke.246
+ __43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke.789
+ __43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.791
+ __43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.791.cold.1
+ __43-[_ATXInspectionServer histogramsInMemory:]_block_invoke.236
+ __44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.100
+ __44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.100.cold.1
+ __44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.103
+ __44-[ATXModeConfigurationLogger retrieveEvents]_block_invoke.70
+ __44-[ATXStackStateTracker persistInternalState]_block_invoke.205
+ __44-[_ATXAppLaunchMonitor registerForAppChange]_block_invoke.101
+ __44-[_ATXAppLaunchMonitor registerForAppChange]_block_invoke.108
+ __44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.765
+ __44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.765.cold.1
+ __45-[ATXContactModeDenyListModel scoredEntities]_block_invoke.30
+ __45-[ATXFaceSuggestionRecentlyViewedSignal init]_block_invoke.20
+ __45-[ATXHistogramBundleIdTable permutationFrom:]_block_invoke.144
+ __45-[ATXHistogramBundleIdTable permutationFrom:]_block_invoke.144.cold.1
+ __45-[_ATXDataStore loadLaunchesFollowingBundle:]_block_invoke.366
+ __46-[ATXAppIntentMonitor _listenToActivityStream]_block_invoke.91
+ __46-[ATXAppPredictionBlacklist _listenForUpdates]_block_invoke.41
+ __46-[ATXPosterDescriptorCache updateDescriptors:]_block_invoke.33
+ __47-[ATXModeScoringSessionRange attachAppLaunches]_block_invoke.15
+ __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.410
+ __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.410.cold.1
+ __47-[_ATXDataStore _markBundleId:asEnterpriseApp:]_block_invoke.1182
+ __47-[_ATXDataStore writeBlob:type:expirationDate:]_block_invoke.509
+ __47-[_ATXDataStore(WebClip) writeWebClip:appClip:]_block_invoke.30
+ __47-[_ATXDataStore(WebClip) writeWebClip:appClip:]_block_invoke.30.cold.1
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.104.cold.2
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.111.cold.3
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.111.cold.4
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.111.cold.5
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.124.cold.1
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.138.cold.1
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.77.cold.3
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.77.cold.4
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.77.cold.5
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.90.cold.2
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.90.cold.3
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.97.cold.2
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.cold.2
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.cold.3
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke.cold.4
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.128.cold.3
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.128.cold.4
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.128.cold.5
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.142.cold.1
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.142.cold.2
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.142.cold.3
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.159.cold.1
+ __47-[_ATXDeprecatedScoreInterpreter _compileRoot:]_block_invoke_2.159.cold.2
+ __48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.111
+ __48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.111.cold.1
+ __48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.118
+ __48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.82
+ __48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.82.cold.1
+ __48-[_ATXDataStore loadAppActionLaunchesFollowing:]_block_invoke.379
+ __48-[_ATXInspectionServer createAppPredictionLogs:]_block_invoke.136
+ __48-[_ATXInspectionServer createAppPredictionLogs:]_block_invoke.138
+ __49-[ATXModeAnchorModelSuggestionClient _pingServer]_block_invoke.18
+ __49-[ATXModeSetupExperienceMetricsLogger logMetrics]_block_invoke.17
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.70
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.72
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.73
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.74
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.77
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.82
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.84
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.86
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.78
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.78.cold.1
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.78.cold.2
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.83
+ __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.90
+ __49-[ATXSuggestionModeFilter registerForModeChanges]_block_invoke.37
+ __49-[ATXSuggestionModeFilter registerForModeChanges]_block_invoke.37.cold.1
+ __49-[_ATXDataStore regenerateSlotSetKeyForBundleId:]_block_invoke.700
+ __49-[_ATXInspectionServer histogramsInMemoryBySize:]_block_invoke.240
+ __49-[_ATXInspectionServer histogramsInMemoryBySize:]_block_invoke.243
+ __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.44
+ __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.44.cold.1
+ __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.49
+ __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.52
+ __50-[_ATXAppLaunchMonitor registerForBacklightChange]_block_invoke.125
+ __50-[_ATXAppLaunchMonitor registerForBacklightChange]_block_invoke.132
+ __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.694
+ __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.696
+ __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.695
+ __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.697
+ __51-[_ATXDataStore pruneMessageRecipientsAddedBefore:]_block_invoke.194
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.710
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.711
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.715
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.726
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.727
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_2.719
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_2.731
+ __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_3.735
+ __52-[ATXAbstractVersionedDatabase currentSchemaVersion]_block_invoke.38
+ __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.18
+ __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.20
+ __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.20.cold.1
+ __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.23
+ __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.23.cold.1
+ __52-[_ATXDataStore actionExistsForBundleId:actionType:]_block_invoke.417
+ __52-[_ATXDataStore actionExistsForBundleId:actionType:]_block_invoke_2.418
+ __53-[ATXAppIntentMonitor handleIntentOrActivityDeletion]_block_invoke.165
+ __53-[ATXAppIntentMonitor handleIntentOrActivityDeletion]_block_invoke.167
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.350
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.350.cold.1
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.351
+ __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.351.cold.1
+ __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.125
+ __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.125.cold.1
+ __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.126
+ __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.126.cold.1
+ __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.24
+ __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.26
+ __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.26.cold.1
+ __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.27
+ __53-[_ATXDataStore(WebClip) webClipsForAppClipBundleId:]_block_invoke.21
+ __53-[_ATXDataStore(WebClip) webClipsForAppClipBundleId:]_block_invoke.23
+ __53-[_ATXDataStore(WebClip) webClipsForAppClipBundleId:]_block_invoke.23.cold.1
+ __54-[_ATXAppLaunchLocation _trainModelWithLOI:startDate:]_block_invoke.70
+ __54-[_ATXAppLaunchLocation _trainModelWithLOI:startDate:]_block_invoke.70.cold.1
+ __54-[_ATXAppLaunchLocation _trainModelWithLOI:startDate:]_block_invoke.80
+ __54-[_ATXDataStore enumerateActionOfType:bundleId:block:]_block_invoke.588
+ __54-[_ATXDataStore enumerateActionOfType:bundleId:block:]_block_invoke_2.589
+ __55-[ATXAnchorModelInferenceEngine exitCallbackForAnchor:]_block_invoke.62
+ __55-[ATXAppLaunchProvider cacheAppLaunchStreamIfNecessary]_block_invoke.15
+ __55-[ATXModeTimelineManager _modeTimelineDataFrom:toDate:]_block_invoke.34
+ __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.49
+ __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.49.cold.1
+ __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.54
+ __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.57
+ __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.57.cold.1
+ __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.61
+ __55-[ATXUserEducationSuggestionFocusModeSetupTrigger init]_block_invoke.23
+ __55-[_ATXDataStore addAppLaunchForAppLaunchSequence:date:]_block_invoke.487
+ __56+[ATXAppDirectoryOrderingProvider _reorderedRecentApps:]_block_invoke.169
+ __56-[ATXCorrelatedEventsManager insertEvents:forEventType:]_block_invoke.25
+ __56-[ATXCorrelatedEventsManager insertEvents:forEventType:]_block_invoke.26
+ __56-[ATXHeroDataServer listener:shouldAcceptNewConnection:]_block_invoke.49
+ __56-[ATXModeConfigurationLogger logMetricForConfiguration:]_block_invoke.57
+ __56-[ATXModeConfigurationLogger logMetricForConfiguration:]_block_invoke.61
+ __56-[ATXModeConfigurationLogger logMetricForConfiguration:]_block_invoke.62
+ __56-[_ATXDataStore _enumerateAppInfoBundlesExecutingBlock:]_block_invoke.395
+ __56-[_ATXDataStore _enumerateAppInfoBundlesExecutingBlock:]_block_invoke.395.cold.1
+ __57-[ATXActionNotificationServer deliveredNotificationCount]_block_invoke.190
+ __58+[ATXIdleTimeBeginAnchor weightedAverageOfHoursFromDates:]_block_invoke.32
+ __58-[ATXFaceGalleryLayoutGenerator rankedFeaturedDescriptors]_block_invoke.62
+ __58-[ATXHeroPoiManager poiCategoryEventsWithStreamPublisher:]_block_invoke.29
+ __58-[ATXMinimalAction actionFromDatastoreLookupForDatastore:]_block_invoke.20
+ __58-[ATXMinimalAction actionFromDatastoreLookupForDatastore:]_block_invoke.23
+ __58-[ATXMinimalAction actionFromDatastoreLookupForDatastore:]_block_invoke.23.cold.1
+ __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.37
+ __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.44
+ __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.44.cold.1
+ __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.47
+ __58-[ATXWidgetModeModel scoredEntitiesWithScoredAppEntities:]_block_invoke.27
+ __59-[ATXAnchorModelDataStoreWrapper trainingResultsForAnchor:]_block_invoke.198
+ __59-[ATXAnchorModelDataStoreWrapper trainingResultsForAnchor:]_block_invoke.198.cold.1
+ __59-[ATXAnchorModelInferenceEngine entranceCallbackForAnchor:]_block_invoke.60
+ __59-[ATXChinSuggestionThrottlingManager _acceptPendingRequest]_block_invoke.76
+ __59-[_ATXInspectionServer listener:shouldAcceptNewConnection:]_block_invoke.25
+ __59-[_ATXInspectionServer listener:shouldAcceptNewConnection:]_block_invoke.25.cold.1
+ __60-[ATXAppDirectoryServer listener:shouldAcceptNewConnection:]_block_invoke.26
+ __60-[ATXAppDirectoryServer listener:shouldAcceptNewConnection:]_block_invoke.26.cold.1
+ __60-[ATXProactiveSuggestionShadowLogger shadowLoggingPublisher]_block_invoke.34
+ __61-[ATXUsageInsightsServer listener:shouldAcceptNewConnection:]_block_invoke.23
+ __61-[ATXUsageInsightsServer listener:shouldAcceptNewConnection:]_block_invoke.23.cold.1
+ __62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke.158
+ __62-[ATXFaceSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.55
+ __62-[ATXFaceSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.55.cold.1
+ __62-[ATXInfoSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.39
+ __62-[ATXUpdatePredictionsManager processLockscreenFeedbackNoSync]_block_invoke.49
+ __62-[_ATXAppInstallMonitor noSyncUpdateWithWaitTime:andBackdate:]_block_invoke.47
+ __62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke.934
+ __62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.937
+ __62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.937.cold.1
+ __63-[ATXSettingsActionsServer listener:shouldAcceptNewConnection:]_block_invoke.19
+ __63-[ATXSettingsActionsServer listener:shouldAcceptNewConnection:]_block_invoke.19.cold.1
+ __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.61
+ __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.61.cold.1
+ __63-[ATXUserEducationSuggestionExploreFacesServer scheduleNextTry]_block_invoke.29
+ __64-[ATXActionPredictionServer listener:shouldAcceptNewConnection:]_block_invoke.37
+ __64-[ATXActionPredictionServer listener:shouldAcceptNewConnection:]_block_invoke.37.cold.1
+ __64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.83
+ __64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.83.cold.1
+ __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.246
+ __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.246.cold.1
+ __64-[ATXNotificationAndSuggestionDatabase getBookmarkDataFromName:]_block_invoke.87
+ __64-[ATXNotificationAndSuggestionDatabase getBookmarkDataFromName:]_block_invoke.89
+ __64-[ATXNotificationAndSuggestionDatabase getBookmarkDataFromName:]_block_invoke.89.cold.1
+ __64-[ATXNotificationAndSuggestionDatabase setBookmarkData:forName:]_block_invoke.99
+ __64-[ATXNotificationAndSuggestionDatabase setBookmarkData:forName:]_block_invoke.99.cold.1
+ __64-[ATXStackStateTracker updateStackRotationEventsByQueryingBiome]_block_invoke.182
+ __64-[ATXStackStateTracker updateStackRotationEventsByQueryingBiome]_block_invoke.182.cold.1
+ __64-[ATXStackStateTracker updateStackRotationEventsByQueryingBiome]_block_invoke.186
+ __64-[_ATXDataStore _deserializeActionLogRowWithStmt:invokingBlock:]_block_invoke.576
+ __65-[ATXBlendingBiomeStreamLogger logBlendingMetricsFromBiomeStream]_block_invoke.31
+ __65-[ATXDigestFeedbackProcessingPipeline logMetricsWithXPCActivity:]_block_invoke.22
+ __65-[ATXInferredModesAccumulator usageInsightsInferredATXModeEvents]_block_invoke.12
+ __65-[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:]_block_invoke.759
+ __66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.154
+ __66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.154.cold.1
+ __66-[ATXAppLaunchMicroLocation tryLoadCorrelationMatricesImmediately]_block_invoke.80
+ __66-[ATXStableContactRepresentationDatabase stableContactIdentifier:]_block_invoke.15
+ __66-[ATXStableContactRepresentationDatabase stableContactIdentifier:]_block_invoke.18
+ __66-[ATXStableContactRepresentationDatabase stableContactIdentifier:]_block_invoke.18.cold.1
+ __66-[ATXUserEducationSuggestionExploreFacesServer backlightEventSink]_block_invoke.51
+ __66-[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:]_block_invoke.29
+ __66-[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:]_block_invoke.32
+ __66-[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:]_block_invoke.32.cold.1
+ __67-[ATXDeviceUsageModeLoggingPipeline logDeviceUsageWithXPCActivity:]_block_invoke.36
+ __67-[ATXDeviceUsageModeLoggingPipeline logDeviceUsageWithXPCActivity:]_block_invoke.36.cold.1
+ __67-[ATXDeviceUsageModeLoggingPipeline logDeviceUsageWithXPCActivity:]_block_invoke.36.cold.2
+ __67-[ATXPredictionJSONScoreLogger flushWithCompletion:filenameSuffix:]_block_invoke.69
+ __67-[ATXSuggestedPagesHomeScreenModificationsMetricsLogger logMetrics]_block_invoke.23
+ __67-[ATXSuggestedPagesHomeScreenModificationsMetricsLogger logMetrics]_block_invoke.23.cold.1
+ __67-[ATXSuggestedPagesHomeScreenModificationsMetricsLogger logMetrics]_block_invoke.27
+ __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.35
+ __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.35.cold.1
+ __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.37
+ __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.37.cold.1
+ __68-[ATXNPlusOneStudyUploader _preparedEvents_numAppLaunches:activity:]_block_invoke.225
+ __68-[ATXNPlusOneStudyUploader _preparedEvents_numAppLaunches:activity:]_block_invoke.225.cold.1
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.137
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.141
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.141.cold.1
+ __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_2.138
+ __69-[ATXAnchorModelDataStoreWrapper deleteSamplesForBundleIdsNotInList:]_block_invoke.327
+ __69-[ATXAnchorModelDataStoreWrapper deleteSamplesForBundleIdsNotInList:]_block_invoke.328
+ __69-[ATXAnchorModelDataStoreWrapper deleteSamplesForBundleIdsNotInList:]_block_invoke.328.cold.1
+ __69-[ATXCandidateRelevanceModelDataStore candidateIdForCandidate:error:]_block_invoke.289
+ __69-[ATXCandidateRelevanceModelDataStore candidateIdForCandidate:error:]_block_invoke_2.290
+ __69-[ATXMindlessCyclingUsageAccumulator accumulateMindlessCyclingEvents]_block_invoke.14
+ __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.213
+ __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.213.cold.1
+ __69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke.1041
+ __69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.1048
+ __69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.1048.cold.1
+ __69-[_ATXFeedback putFeedbackScoresForApps:intoScores:confirms:rejects:]_block_invoke.85
+ __70+[ATXScoreInterpreterFromAssetBuilder scoreInterpretersForAllSubTypes]_block_invoke.37
+ __70+[ATXScoreInterpreterFromAssetBuilder scoreInterpretersForAllSubTypes]_block_invoke.42
+ __70+[_ATXAppLaunchMonitor _harvestAppPredictionDataForBundleId:response:]_block_invoke.144
+ __70-[ATXAnchorModelDataStoreWrapper populateCachedCountsForCandidateIds:]_block_invoke.367
+ __70-[ATXAnchorModelDataStoreWrapper populateCachedCountsForCandidateIds:]_block_invoke_2.370
+ __70-[ATXDefaultWidgetSuggesterServer listener:shouldAcceptNewConnection:]_block_invoke.22
+ __70-[ATXDefaultWidgetSuggesterServer listener:shouldAcceptNewConnection:]_block_invoke.22.cold.1
+ __70-[ATXNPlusOneStudyUploader _preparedEvents_suggestionCounts:activity:]_block_invoke.232
+ __70-[ATXNPlusOneStudyUploader _preparedEvents_suggestionCounts:activity:]_block_invoke.232.cold.1
+ __70-[_ATXAppInfoManager computeAverageAndMedianSecondsBetweenAppLaunches]_block_invoke.52
+ __71+[ATXActionPredictions filterHighQualityActionResults:consumerSubType:]_block_invoke.87
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.277.cold.1
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.283
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.290
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.292.cold.1
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.298
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.305
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.308.cold.1
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.314
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.284
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.284.cold.1
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.291
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.299
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.299.cold.1
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.307
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.315
+ __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.315.cold.1
+ __71-[ATXNotificationDeliverySuggestionManager activeSuggestionsWithReply:]_block_invoke.39
+ __71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.70
+ __71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.70.cold.1
+ __71-[ATXSettingsActionsServer recentActionsWithRequest:completionHandler:]_block_invoke.36
+ __71-[_ATXDataStore numActionKeyOccurrencesForActionKey:startDate:endDate:]_block_invoke.636
+ __72+[ATXCandidateRelevanceModelOfflineDataHarvester modelMetricsForConfig:]_block_invoke.26
+ __72+[ATXCandidateRelevanceModelOfflineDataHarvester modelMetricsForConfig:]_block_invoke.26.cold.1
+ __72-[ATXActionNotificationServer proactiveSuggestionsCurrentlyOnLockscreen]_block_invoke.193
+ __72-[ATXAnchorModelDataStoreWrapper uniqueAnchorEventIdentifiersForAnchor:]_block_invoke.344
+ __72-[ATXAnchorModelDataStoreWrapper uniqueAnchorEventIdentifiersForAnchor:]_block_invoke.344.cold.1
+ __72-[ATXAppSessionModeLoggingPipeline logAppSessionMetricsWithXPCActivity:]_block_invoke.30
+ __72-[ATXAppSessionModeLoggingPipeline logAppSessionMetricsWithXPCActivity:]_block_invoke.30.cold.1
+ __72-[ATXAppSessionModeLoggingPipeline logAppSessionMetricsWithXPCActivity:]_block_invoke.30.cold.2
+ __72-[ATXCandidateRelevanceModelTrainer generateAndSaveDatasetWithFilename:]_block_invoke.25
+ __72-[ATXCandidateRelevanceModelTrainer generateAndSaveDatasetWithFilename:]_block_invoke.48
+ __72-[ATXInformationEngine getSuggestionsForInfoSourceIdentifier:withReply:]_block_invoke.86
+ __72-[ATXModeEntitySuggestions suggestedBundleIDsForDenyListWithCompletion:]_block_invoke.24
+ __72-[ATXNotificationDigestRankerServer listener:shouldAcceptNewConnection:]_block_invoke.84
+ __72-[ATXNotificationDigestRankerServer listener:shouldAcceptNewConnection:]_block_invoke.84.cold.1
+ __72-[_ATXAppLaunchHistogram initWithHistogram:bucketCount:filter:timeBase:]_block_invoke.37
+ __72-[_ATXAppLaunchHistogram initWithHistogram:bucketCount:filter:timeBase:]_block_invoke.37.cold.1
+ __72-[_ATXAppLaunchHistogram initWithHistogram:bucketCount:filter:timeBase:]_block_invoke.37.cold.2
+ __72-[_ATXDataStore(IntentCache) writeSupportsBackgroundExecution:cacheKey:]_block_invoke.45
+ __72-[_ATXDataStore(IntentCache) writeSupportsBackgroundExecution:cacheKey:]_block_invoke.45.cold.1
+ __73+[ATXDeviceBacklightHelper getScreenOnIntervalsBetweenStartDate:endDate:]_block_invoke.11
+ __73-[ATXAnchorModelDataStoreWrapper dateAnchorModelWasLastTrainedForAnchor:]_block_invoke.205
+ __73-[ATXAnchorModelDataStoreWrapper dateAnchorModelWasLastTrainedForAnchor:]_block_invoke.205.cold.1
+ __73-[ATXCandidateRelevanceModelServer sortedProactiveSuggestionsForContext:]_block_invoke.29
+ __73-[ATXCandidateRelevanceModelServer sortedProactiveSuggestionsForContext:]_block_invoke.29.cold.1
+ __73-[ATXCandidateRelevanceModelServer sortedProactiveSuggestionsForContext:]_block_invoke.34
+ __73-[ATXHomeScreenFocusSuggestionLogger logHomeScreenFocusSuggestionMetrics]_block_invoke.22
+ __73-[ATXHomeScreenFocusSuggestionLogger logHomeScreenFocusSuggestionMetrics]_block_invoke.26
+ __73-[ATXModeEntitySuggestions suggestedBundleIDsForAllowListWithCompletion:]_block_invoke.18
+ __73-[ATXModeEntitySuggestions suggestedBundleIDsForAllowListWithCompletion:]_block_invoke.21
+ __73-[ATXModeFaceComplicationHeuristicDataSource _hasSignificantStocksEvents]_block_invoke.127
+ __73-[ATXNotificationDeliverySuggestionManager digestHasBeenShownEnoughTimes]_block_invoke.35
+ __73-[ATXNotificationsEventProvider cacheGlobalNotificationStreamIfNecessary]_block_invoke.17
+ __73-[_ATXHomeScreenStackState widgetForSuggestion:considerSuggestedWidgets:]_block_invoke.20
+ __73-[_PASSqliteDatabase(ATXExtras) atx_countRowsOfTable:returnValueOnError:]_block_invoke.8
+ __74-[ATXActivitySuggestionsFeedbackProcessor processFeedbackWithXPCActivity:]_block_invoke.23
+ __74-[ATXActivitySuggestionsFeedbackProcessor processFeedbackWithXPCActivity:]_block_invoke.23.cold.1
+ __74-[ATXCandidateRelevanceModelDatasetGenerator receiveDataPoint:completion:]_block_invoke.143
+ __74-[ATXModeEntityCorrelator featuresForEntitiesFromCompleteCorrelatorState:]_block_invoke.26
+ __74-[ATXNotificationCategorizationServer listener:shouldAcceptNewConnection:]_block_invoke.68
+ __74-[ATXNotificationCategorizationServer listener:shouldAcceptNewConnection:]_block_invoke.68.cold.1
+ __75+[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]_block_invoke.139
+ __75-[ATXAnchorModelDataStoreWrapper numModeOccurrencesInAllContextsForModeId:]_block_invoke.381
+ __75-[ATXBiomePrivacyPruner pruneWithStreamIdentifier:activity:config:endTime:]_block_invoke.90
+ __75-[ATXContinuousUsageAccumulator successfullyAccumulatedContinuousUseEvents]_block_invoke.15
+ __75-[ATXNPlusOneStudyUploader _preparedEvents_appScreenTimeCategory:activity:]_block_invoke.216
+ __75-[ATXNPlusOneStudyUploader _preparedEvents_appScreenTimeCategory:activity:]_block_invoke.216.cold.1
+ __75-[ATXNotificationResolutionAccumulator historicalResolutionForNotification]_block_invoke.67
+ __75-[ATXNotificationResolutionAccumulator historicalResolutionForNotification]_block_invoke.67.cold.1
+ __75-[ATXNotificationResolutionAccumulator historicalResolutionForNotification]_block_invoke.70
+ __75-[ATXUserNotificationDigest(EngagementTracking) computeNumDigestExpansions]_block_invoke.32
+ __75-[ATXUserNotificationDigest(EngagementTracking) computeNumDigestExpansions]_block_invoke.36
+ __76-[ATXLockScreenNotificationRankerServer listener:shouldAcceptNewConnection:]_block_invoke.20
+ __76-[ATXLockScreenNotificationRankerServer listener:shouldAcceptNewConnection:]_block_invoke.20.cold.1
+ __76-[ATXMLActionProducer _getActionsFromCacheForConsumerSubType:cacheFileData:]_block_invoke.30
+ __77+[ATXCandidateRelevanceModelOfflineDataHarvester candidateMetricsFromConfig:]_block_invoke.18
+ __77+[ATXCandidateRelevanceModelOfflineDataHarvester candidateMetricsFromConfig:]_block_invoke.18.cold.1
+ __77+[ATXCandidateRelevanceModelOfflineDataHarvester candidateMetricsFromConfig:]_block_invoke.20
+ __77-[ATXDailyNotificationsAccumulator successfullyAccumulatedNotificationEvents]_block_invoke.14
+ __77-[ATXModeInferredDurationAndCountProvider cacheInferredModeStreamIfNecessary]_block_invoke.13
+ __77-[ATXNotificationResolutionAccumulator computeTimeToLaunchAppForNotification]_block_invoke.50
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.1
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.2
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.3
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.4
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.5
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.6
+ __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.44.cold.7
+ __78-[ATXDigestOnboardingMetricsLogger logDigestOnboardingMetricsWithXPCActivity:]_block_invoke.26
+ __78-[ATXFaceSuggestionServer reloadLockScreenSuggestionsWithActivity:completion:]_block_invoke.78
+ __78-[ATXFaceSuggestionServer reloadLockScreenSuggestionsWithActivity:completion:]_block_invoke.78.cold.1
+ __78-[ATXFaceSuggestionServer reloadLockScreenSuggestionsWithActivity:completion:]_block_invoke.78.cold.2
+ __78-[ATXInformationEngine _updatePredictionRefreshDateIfNecessaryForSuggestions:]_block_invoke.78
+ __78-[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:]_block_invoke.106
+ __78-[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:]_block_invoke.110
+ __78-[ATXRecentAndSuggestedAppsLayoutSelector _accumulateRecentAppLaunchBundleIds]_block_invoke.33
+ __78-[ATXRecentAndSuggestedAppsLayoutSelector _accumulateRecentAppLaunchBundleIds]_block_invoke.37
+ __78-[_ATXDataStore(IntentCache) validParameterCombinationsWithSchemaForCacheKey:]_block_invoke.29
+ __78-[_ATXDataStore(IntentCache) validParameterCombinationsWithSchemaForCacheKey:]_block_invoke.31
+ __78-[_ATXDataStore(IntentCache) validParameterCombinationsWithSchemaForCacheKey:]_block_invoke.31.cold.1
+ __79-[ATXCandidateRelevanceModelDatasetGenerator receiveDatasetSession:completion:]_block_invoke.146
+ __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.347
+ __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.347.cold.1
+ __79-[ATXRSWidgetSuggestionProducer _candidatesFromRelevantShortcutsFromStartDate:]_block_invoke.62
+ __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.22
+ __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.30
+ __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.30.cold.1
+ __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.32
+ __80+[ATXFaceSuggestionAssetParameters posterDescriptorFromKey:withDescriptorCache:]_block_invoke.214
+ __80-[ATXAnchorModelDataStoreWrapper insertAnchorOccurrence:anchor:featureMetadata:]_block_invoke.270
+ __80-[ATXAnchorModelDataStoreWrapper insertAnchorOccurrence:anchor:featureMetadata:]_block_invoke.270.cold.1
+ __80-[ATXBlendingLayerSessionLogger clientModelCacheUpdatesFromBlendingCacheUpdate:]_block_invoke.53
+ __80-[ATXComplicationSuggestionGenerator _recentsComplications_unusedComplications:]_block_invoke.27
+ __80-[ATXDynamicBreakthroughFeaturesCorrelator currentLocationSemanticForGivenDate:]_block_invoke.22
+ __80-[ATXFaceSuggestionServer synchronousDateOfLastGalleryAppearanceWithCompletion:]_block_invoke.99
+ __80-[ATXModeFaceComplicationHeuristicDataSource _hasSignificantHomeAccessoryEvents]_block_invoke.123
+ __80-[ATXModeTransitionMetricsLogUploader uploadLogsToCoreAnalyticsWithXPCActivity:]_block_invoke.27
+ __80-[ATXSuggestedPagesStackHeuristicsDataSource _hasSignificantHomeAccessoryEvents]_block_invoke.159
+ __81-[ATXAnchorModelEventFeaturizer numEventsForEventIds:dateBuckets:biomePublisher:]_block_invoke.44
+ __81-[ATXAppInterruptionsEventProvider successfullyCalculatedAppSessionInterruptions]_block_invoke.22
+ __81-[ATXAppInterruptionsEventProvider successfullyCalculatedAppSessionInterruptions]_block_invoke.24
+ __81-[ATXHomeScreenWidgetFeedbackProcessor updateHistogramsForRecentHomeScreenEvents]_block_invoke.27
+ __81-[ATXHomeScreenWidgetFeedbackProcessor updateHistogramsForRecentHomeScreenEvents]_block_invoke.27.cold.1
+ __81-[ATXNotificationSmartPauseManager currentSuggestionsGivenCandiateNotifications:]_block_invoke.31
+ __81-[ATXNotificationSmartPauseManager currentSuggestionsGivenCandiateNotifications:]_block_invoke.33
+ __81-[ATXSmartActivationEarlyExitDetectionLogger _registerForModeChangeNotifications]_block_invoke.19
+ __81-[_ATXDataStore(IntentCache) writeValidParameterCombinationsWithSchema:cacheKey:]_block_invoke.23
+ __81-[_ATXDataStore(IntentCache) writeValidParameterCombinationsWithSchema:cacheKey:]_block_invoke.23.cold.1
+ __82-[ATXAnchorModelDataStoreWrapper minSlotResolutionParametersFromALogId:paramHash:]_block_invoke.429
+ __82-[ATXAnchorModelDataStoreWrapper minSlotResolutionParametersFromALogId:paramHash:]_block_invoke.429.cold.1
+ __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.114
+ __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.114.cold.1
+ __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.137
+ __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.137.cold.1
+ __82-[ATXInformationEngine clearSuggestionsForInfoSourceIdentifier:completionHandler:]_block_invoke.87
+ __82-[ATXIntentMetadataCacheInvalidationMonitor _listenForAppRegistrationAndUninstall]_block_invoke.17
+ __82-[ATXNotificationCategorizationServer rankUserNotificationWithRequest:completion:]_block_invoke.89
+ __82-[ATXNotificationCategorizationServer rankUserNotificationWithRequest:completion:]_block_invoke.89.cold.1
+ __82-[ATXNotificationResolutionAccumulator cacheAppLaunchDataFromStartTime:toEndTime:]_block_invoke.55
+ __82-[ATXNotificationResolutionAccumulator cacheAppLaunchDataFromStartTime:toEndTime:]_block_invoke.58
+ __82-[ATXSuggestedPagesAppAggregator _sortedApps:sortedFirstPageApps:appLaunchCounts:]_block_invoke.45
+ __82-[ATXUserEducationSuggestionFocusModeSetupTrigger modeHasPassedPastInferenceTest:]_block_invoke.26
+ __83-[ATXBiomeProactiveSuggestionUIFeedbackResultStreamWriter writeForConsumerSubType:]_block_invoke.37
+ __83-[ATXCandidateRelevanceModelDataStore trainingResultsForClientModelName:modelUUID:]_block_invoke.340
+ __84-[ATXAnchorModelEventFeaturizer historyForAppLaunchDuetEvents:anchorOccurrenceDate:]_block_invoke.34
+ __84-[ATXInformationEngine insertSuggestions:forInfoSourceIdentifier:completionHandler:]_block_invoke.74
+ __84-[ATXMissedNotificationRankingFeedbackProcessingPipeline logMetricsWithXPCActivity:]_block_invoke.21
+ __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.337
+ __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.337.cold.1
+ __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.158
+ __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.158.cold.1
+ __84-[ATXProactiveSuggestionClientModelEvaluator uiPublisherWithDeduplicatedEngagements]_block_invoke.193
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.205
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.210
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.220
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.230
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_2.209
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_2.211
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_2.224
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_3.219
+ __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_3.226
+ __85-[ATXActionTimeEstimateAWDTracker getTimeEstimatesFor:forAppLaunches:withActionType:]_block_invoke.52
+ __85-[ATXAppNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.22
+ __85-[ATXAppNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.24
+ __85-[ATXCandidateRelevanceModelDataStore deleteTrainedModelsWithTrainDateOlderThanDate:]_block_invoke.376
+ __85-[ATXCandidateRelevanceModelDataStore deleteTrainedModelsWithTrainDateOlderThanDate:]_block_invoke_2.377
+ __85-[ATXCandidateRelevanceModelDataStore deleteTrainedModelsWithTrainDateOlderThanDate:]_block_invoke_3.381
+ __85-[ATXInformationEngine resetSuggestionsTo:forInfoSourceIdentifier:completionHandler:]_block_invoke.85
+ __86-[ATXInterruptingNotificationsAccumulator successfullyAccumulatedInterruptingSessions]_block_invoke.16
+ __86-[ATXInterruptingNotificationsAccumulator successfullyAccumulatedInterruptingSessions]_block_invoke.18
+ __86-[ATXNotificationModeModel scoredEntitiesWithScoredAppEntities:scoredContactEntities:]_block_invoke.22
+ __88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.240
+ __88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.240.cold.1
+ __88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.241
+ __88-[ATXInformationFilter recordDismissOfSuggestion:isDismissalLongTerm:completionHandler:]_block_invoke.41
+ __88-[ATXModeSetupPredictionMetricsLogger fetchAllRelevantModeSemanticTypesInLastSevenDays:]_block_invoke.56
+ __88-[ATXModeSetupPredictionMetricsLogger globalAppSessionInterruptionsCalculatorSinceDate:]_block_invoke.23
+ __88-[ATXModeSetupPredictionMetricsLogger globalAppSessionInterruptionsCalculatorSinceDate:]_block_invoke.25
+ __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke.297
+ __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.298
+ __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.298.cold.1
+ __88-[ATXProactiveSuggestionPartialIntentHandlingPublisher partialIntentUIFeedbackPublisher]_block_invoke.22
+ __89-[ATXActionCacheReader enumerateActionsAndPredictionItemsForConsumerSubtype:limit:block:]_block_invoke.29
+ __89-[ATXAnchorModelDataStoreWrapper timestampOfMostRecentRecordedAnchorOccurrenceForAnchor:]_block_invoke.38
+ __89-[ATXAnchorModelDataStoreWrapper timestampOfMostRecentRecordedAnchorOccurrenceForAnchor:]_block_invoke.41
+ __89-[ATXAnchorModelDataStoreWrapper timestampOfMostRecentRecordedAnchorOccurrenceForAnchor:]_block_invoke.41.cold.1
+ __89-[ATXBlendingBiomeStreamLogger logLayoutSelectedMetricWithBlendingModelCacheUpdateEvent:]_block_invoke.67
+ __89-[ATXContactNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.20
+ __89-[ATXContactNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.22
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.386
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.395
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.402
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.396
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.396.cold.1
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.404
+ __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.404.cold.1
+ __89-[_ATXRecentInstallCache initTrackingAppsMoreRecentThan:installMonitor:uninstallMonitor:]_block_invoke.33
+ __90-[ATXModeConfigurationUIFlowMetricLogger logModeConfigurationUIFlowMetricWithXPCActivity:]_block_invoke.28
+ __91-[ATXCandidateRelevanceModelDataStore featurizationManagerIdForFeaturizationManager:error:]_block_invoke.230
+ __91-[ATXCandidateRelevanceModelDataStore featurizationManagerIdForFeaturizationManager:error:]_block_invoke_2.231
+ __91-[ATXModeFaceComplicationsAggregator provideComplicationsForSuggestedFaceType:environment:]_block_invoke.28
+ __91-[ATXModeFaceComplicationsAggregator provideComplicationsForSuggestedFaceType:environment:]_block_invoke.28.cold.1
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.363
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.369
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.371
+ __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.371.cold.1
+ __91-[ATXUnifiedComputedAndInferredModeStream computeUnifiedModeEventsFromStartTime:toEndTime:]_block_invoke.40
+ __91-[ATXUnifiedComputedAndInferredModeStream computeUnifiedModeEventsFromStartTime:toEndTime:]_block_invoke.44
+ __92-[ATXSpotlightLayoutSelector _validAutoShortcutContextualActionsForBundleId:limit:provider:]_block_invoke.245
+ __92-[ATXSuggestionPreprocessor suggestionsByPreprocessingRankedSuggestions:forConsumerSubType:]_block_invoke.52
+ __92-[ATXSuggestionPreprocessor suggestionsByPreprocessingRankedSuggestions:forConsumerSubType:]_block_invoke.59
+ __92-[ATXSuggestionPreprocessor suggestionsByPreprocessingRankedSuggestions:forConsumerSubType:]_block_invoke.59.cold.1
+ __93-[ATXAppSessionInterruptionsProvider cacheGlobalAppSessionInterruptionsCalculatorIfNecessary]_block_invoke.20
+ __93-[ATXAppSessionInterruptionsProvider cacheGlobalAppSessionInterruptionsCalculatorIfNecessary]_block_invoke.22
+ __93-[ATXCandidateRelevanceModelDatasetGenerator receiveCandidateDataPoint:completion:candidate:]_block_invoke.151
+ __93-[ATXModeFaceComplicationAppDataSource provideComplicationsForSuggestedFaceType:environment:]_block_invoke.23
+ __93-[ATXPredictionContextBuilder updateContextStreamAndReturnPredictionContextForCurrentContext]_block_invoke.84
+ __93-[ATXProactiveSuggestionShadowLogger enumerateShadowLoggingResultsWithBlock:completionBlock:]_block_invoke.20
+ __95+[ATXCandidateRelevanceModelDatasetGeneratorConfigApp candidatePublisherWithStartTime:endTime:]_block_invoke.68
+ __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.63
+ __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.66
+ __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.70
+ __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.75
+ __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.78
+ __95-[_ATXDataStore numActionParameterHashOccurrencesForActionKey:parameterHash:startDate:endDate:]_block_invoke.645
+ __96+[ATXAppPredictorFeedback checkFeedbackContainsUninstalledApps:consumerSubType:aggregateLogger:]_block_invoke.24
+ __96-[ATXModeFaceComplicationWidgetDataSource provideComplicationsForSuggestedFaceType:environment:]_block_invoke.23
+ __96-[ATXModeSetupPredictionMetricsLogger getRecommendedAndCandidateAppsInDenyListForSemanticTypes:]_block_invoke.45
+ __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.451
+ __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.451.cold.1
+ __96-[ATXNotificationManagementInspector fetchNotificationsFromBiomeFromStartDate:endDate:outError:]_block_invoke.92
+ __97-[ATXModeSetupPredictionMetricsLogger getRecommendedAndCandidateAppsInAllowListForSemanticTypes:]_block_invoke.39
+ __97-[ATXModeSetupPredictionMetricsLogger getRecommendedAndCandidateAppsInAllowListForSemanticTypes:]_block_invoke.43
+ __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke.278
+ __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.279
+ __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.279.cold.1
+ __97-[_ATXFeedback feedbackLaunchedWithConsumerType:forBundleId:rejected:explicitlyRejected:context:]_block_invoke.76
+ __98-[ATXDigestOnboardingSuggestionMetricsLogger logDigestOnboardingSuggestionMetricsWithXPCActivity:]_block_invoke.26
+ __98-[ATXLinkActionPreprocessor updatedLinkActionSuggestion:actionContainer:basedOnReversedPublisher:]_block_invoke.16
+ __99-[ATXNotificationAndSuggestionDatabase prepAndRunQuery:batchSize:XPCActivity:onPrep:onRow:onError:]_block_invoke.377
+ __Block_byref_object_copy_.149
+ __Block_byref_object_dispose_.150
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPK17ATXPredictionItemS6_PS4_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS5_EENS1_INS_4pairIU8__strongKS4_S8_EEEEEEEEPSF_EclB8ne190102Ev
+ __ZNKSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne190102Ev
+ __ZNKSt3__16vectorIDv8_fN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIDv8_iN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEENSA_ISF_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_out_of_rangeB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_out_of_rangeB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HDGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HTGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringPK17ATXPredictionItemEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP9ATXActioniEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEERNSA_ISF_EEE5clearB8ne190102Ev
+ __ZNSt3__114__split_bufferINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEERNS_9allocatorIS8_EEE5clearB8ne190102Ev
+ __ZNSt3__115allocate_sharedB8ne190102I27ATXGamePlayKitCDecisionNodeNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8ne190102I27ATXGamePlayKitCDecisionTreeNS_9allocatorIS1_EEJELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__116__insertion_sortB8ne190102INS_17_ClassicAlgPolicyERZ119-[_ATXAppPredictor _getPredictionForItems:clipBundleIdsToRank:consumerSubType:intent:scoreLogger:context:featureCache:]E3$_0NS_11__wrap_iterIP17ATXPredictionItemEEEEvT1_S8_T0_
+ __ZNSt3__116__rotate_forwardB8ne190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIP17ATXPredictionItemEEEET0_S6_S6_S6_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI17ATXPredictionItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS5_EENS1_INS_4pairIU8__strongKS4_S8_EEEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSJ_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__120__shared_ptr_emplaceI27ATXGamePlayKitCDecisionTreeNS_9allocatorIS1_EEEC2B8ne190102IJES3_Li0EEES3_DpOT_
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__120get_temporary_bufferB8ne190102I17ATXPredictionItemEENS_4pairIPT_lEEl
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString17ATXPredictionItemEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS6_EENS2_INS_4pairIU8__strongKS5_S9_EEEEEEEEPSG_EEED2B8ne190102Ev
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS5_EENS1_INS_4pairIU8__strongKS4_S8_EEEEEEEESF_EEvRT_PT0_SK_SK_
+ __ZNSt3__13mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS3_EENS_9allocatorINS_4pairIU8__strongKS2_S6_EEEEE6insertB8ne190102INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIS3_S6_EEPNS_11__tree_nodeISJ_PvEElEEEEEEvT_SQ_
+ __ZNSt3__13mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS3_EENS_9allocatorINS_4pairIU8__strongKS2_S6_EEEEEC2B8ne190102ERKSE_
+ __ZNSt3__14pairIRU8__strongP11objc_objectRU8__strongP14NSMutableArrayEaSB8ne190102IU8__strongKS2_S7_Li0EEERS9_RKNS0_IT_T0_EE
+ __ZNSt3__14pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEaSB8ne190102EOS7_
+ __ZNSt3__16__treeINS_12__value_typeIU8__strongP11objc_objectU8__strongP14NSMutableArrayEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE18_DetachedTreeCacheD2B8ne190102Ev
+ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE9push_backB8ne190102ERKS1_
+ __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEEC2B8ne190102Em
+ __ZNSt3__16vectorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEENSA_ISF_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102Em
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne190102IRNS_11__wrap_iterIP17ATXPredictionItemEES7_EEvOT_OT0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne190102IRNS_11__wrap_iterIP17ATXPredictionItemEES8_EEvOT_OT0_
+ __ZNSt3__19__shuffleB8ne190102INS_17_ClassicAlgPolicyENS_11__wrap_iterIP17ATXPredictionItemEES5_NS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEEET0_S8_T1_OT2_
+ __ZNSt3__19allocatorI27ATXGamePlayKitCDecisionTreeE7destroyB8ne190102EPS1_
+ __ZNSt3__19allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEE7destroyB8ne190102EPS8_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___105-[ATXNotificationAndSuggestionDatabase updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:]_block_invoke
+ ___105-[ATXNotificationAndSuggestionDatabase updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:]_block_invoke_2
+ ___ATXInitializeInOwnerProcess_block_invoke.384
+ ___ATXInitializeInOwnerProcess_block_invoke.394
+ ___ATXInitializeInOwnerProcess_block_invoke.419
+ ___ATXInitializeInOwnerProcess_block_invoke.429
+ ___ATXInitializeInOwnerProcess_block_invoke_2.389
+ ___ATXInitializeInOwnerProcess_block_invoke_2.401
+ ___ATXInitializeInOwnerProcess_block_invoke_2.401.cold.1
+ ___ATXInitializeInOwnerProcess_block_invoke_2.425
+ ___ATXInitializeInOwnerProcess_block_invoke_2.425.cold.1
+ _____atxlog_handle_carPlay_widgets_block_invoke
+ ___atxlog_handle_carPlay_widgets
+ ___block_descriptor_72_e8_32s40s48s56s64r_e22_v16?0"BMStoreEvent"8l
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_project_boxed_opaque_existential_0
+ __atxRegisterCTSJobHandler_block_invoke.cold.1
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
+ __block_literal_global.1007
+ __block_literal_global.1024
+ __block_literal_global.1043
+ __block_literal_global.1053
+ __block_literal_global.106
+ __block_literal_global.1061
+ __block_literal_global.108
+ __block_literal_global.109
+ __block_literal_global.1176
+ __block_literal_global.1184
+ __block_literal_global.121
+ __block_literal_global.124
+ __block_literal_global.126
+ __block_literal_global.127
+ __block_literal_global.131
+ __block_literal_global.135
+ __block_literal_global.138
+ __block_literal_global.139
+ __block_literal_global.156
+ __block_literal_global.158
+ __block_literal_global.165
+ __block_literal_global.166
+ __block_literal_global.167
+ __block_literal_global.169
+ __block_literal_global.176
+ __block_literal_global.177
+ __block_literal_global.180
+ __block_literal_global.184
+ __block_literal_global.189
+ __block_literal_global.192
+ __block_literal_global.195
+ __block_literal_global.196
+ __block_literal_global.200
+ __block_literal_global.203
+ __block_literal_global.205
+ __block_literal_global.216
+ __block_literal_global.218
+ __block_literal_global.220
+ __block_literal_global.229
+ __block_literal_global.231
+ __block_literal_global.235
+ __block_literal_global.237
+ __block_literal_global.246
+ __block_literal_global.249
+ __block_literal_global.254
+ __block_literal_global.256
+ __block_literal_global.278
+ __block_literal_global.279
+ __block_literal_global.284
+ __block_literal_global.286
+ __block_literal_global.294
+ __block_literal_global.299
+ __block_literal_global.310
+ __block_literal_global.323
+ __block_literal_global.330
+ __block_literal_global.343
+ __block_literal_global.345
+ __block_literal_global.347
+ __block_literal_global.349
+ __block_literal_global.362
+ __block_literal_global.369
+ __block_literal_global.373
+ __block_literal_global.384
+ __block_literal_global.392
+ __block_literal_global.394
+ __block_literal_global.396
+ __block_literal_global.398
+ __block_literal_global.403
+ __block_literal_global.405
+ __block_literal_global.406
+ __block_literal_global.412
+ __block_literal_global.427
+ __block_literal_global.431
+ __block_literal_global.441
+ __block_literal_global.444
+ __block_literal_global.446
+ __block_literal_global.453
+ __block_literal_global.458
+ __block_literal_global.461
+ __block_literal_global.465
+ __block_literal_global.468
+ __block_literal_global.473
+ __block_literal_global.477
+ __block_literal_global.481
+ __block_literal_global.485
+ __block_literal_global.488
+ __block_literal_global.504
+ __block_literal_global.509
+ __block_literal_global.513
+ __block_literal_global.514
+ __block_literal_global.524
+ __block_literal_global.526
+ __block_literal_global.529
+ __block_literal_global.537
+ __block_literal_global.546
+ __block_literal_global.554
+ __block_literal_global.557
+ __block_literal_global.561
+ __block_literal_global.562
+ __block_literal_global.572
+ __block_literal_global.575
+ __block_literal_global.591
+ __block_literal_global.594
+ __block_literal_global.604
+ __block_literal_global.607
+ __block_literal_global.61
+ __block_literal_global.621
+ __block_literal_global.624
+ __block_literal_global.628
+ __block_literal_global.635
+ __block_literal_global.638
+ __block_literal_global.64
+ __block_literal_global.687
+ __block_literal_global.69
+ __block_literal_global.699
+ __block_literal_global.767
+ __block_literal_global.772
+ __block_literal_global.777
+ __block_literal_global.798
+ __block_literal_global.81
+ __block_literal_global.836
+ __block_literal_global.876
+ __block_literal_global.881
+ __block_literal_global.90
+ __block_literal_global.913
+ __block_literal_global.915
+ __block_literal_global.923
+ __block_literal_global.936
+ __block_literal_global.939
+ __block_literal_global.970
+ __registerForDailyRoutinesCTSJob_block_invoke.456
+ __registerForEverydayShortcutsTriggersCTSJobs_block_invoke.451
+ __registerForNotificationAndSuggestionDatastorePruning_block_invoke.610
+ _kATXAddNextAppLaunchTimestampToNotifications
+ _kATXNotificationAndSuggestionAppLaunchTimestampDefaultsKey
+ _kATXUpdateNotificationAppLaunchTimestampQuery
+ _objc_msgSend$_appLaunchPublisher
+ _objc_msgSend$bundleIDCountForCategory:
+ _objc_msgSend$countWhereA:b:
+ _objc_msgSend$nextAppLaunchTimestamp
+ _objc_msgSend$purgeUnusedCategories
+ _objc_msgSend$setNextAppLaunchTimestamp:
+ _objc_msgSend$updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:
+ _objc_msgSend$updateNotificationsWithNextAppLaunchTimestamp:bundleId:startTimestamp:
+ _symbolic SccySay______pG______pG So30WLKSportsFavoriteRepresentableP s5ErrorP
+ _symbolic SccySb______pG s5ErrorP
+ _symbolic Sccyyt______pG s5ErrorP
+ block_copy_helper.25
+ block_copy_helper.32
+ block_copy_helper.36
+ block_descriptor.27
+ block_descriptor.38
+ block_destroy_helper.26
+ block_destroy_helper.33
+ block_destroy_helper.37
+ getTrialAssets.cold.1
+ keyTrackerForRotationSessionStackEngagementStatus:._pasExprOnceResult.179
+ keyTrackerForRotationSessionStackEngagementStatus:._pasExprOnceResult.180
+ keyTrackerForStackEngagementStatus:._pasExprOnceResult.126
+ keyTrackerForStackEngagementStatus:._pasExprOnceResult.127
+ keyTrackerForStackEngagementStatus:._pasExprOnceResult.128
+ keyTrackerForStackEngagementStatus:._pasExprOnceResult.129
+ keyTrackerForStackEngagementStatus:._pasExprOnceResult.130
+ keyTrackerForStackEngagementStatus:._pasExprOnceResult.131
+ purgeUnusedCategories.totalSavings
+ replacementContainerBundleIdForDonationBundleId:._pasOnceToken33
- +[ATXBlendedLocalAndGlobalScores blendedGlobalAndLocalScoresForGlobalScores:LOITypeLaunches:lastAppLaunches:timeOfDayLaunches:dayOfWeekLaunches:forApps:]
- +[ATXDirichletDistribution getGammaDistributionShapeParameterForComputingGlobalAppScoresWithAlpha:andNormalizationConstant:]
- +[ATXDirichletDistribution sharedInstance]
- +[ATXGlobalAppScoresUtil loadCoreMLModelWithName:]
- +[ATXGlobalAppScoresUtil loadCoreMLModelWithName:].cold.1
- +[ATXGlobalAppScoresUtil loadCoreMLModelWithName:].cold.2
- -[ATXDirichletDistribution getBlendedLocalAndGlobalScoresWithLocalCounts:andGlobalScores:withSamplingEnabled:]
- -[ATXDirichletDistribution init]
- -[ATXDirichletDistribution sampleProbabilitiesFromDirichletWithNormalizedParameters:andNormalizationConstant:]
- -[ATXGlobalAppScorePredictor globalPopularitiesAtTimeOfDay:atDayOfWeek:atLocation:withLastAppLaunched:]
- -[ATXGlobalAppScorePredictor globalPopularitiesAtTimeOfDay:atDayOfWeek:atLocation:withLastAppLaunched:].cold.1
- -[ATXGlobalAppScorePredictor globalPopularitiesAtTimeOfDay:atDayOfWeek:atLocation:withLastAppLaunched:].cold.2
- -[ATXGlobalAppScorePredictor globalPopularitiesForBundleIds:atTimeOfDayIndex:atDayOfWeekIndex:atLocationIndex:withLastAppLaunched:]
- -[ATXGlobalAppScorePredictor globalPopularityForBundleIds:atDate:atLocation:withLastAppLaunched:]
- -[ATXGlobalAppScorePredictor globalPopularityForBundleIdsGivenTimeDayLocationAndLastApp:context:]
- -[ATXGlobalAppScorePredictor globalPopularityPredictor]
- -[_ATXScoreInterpreter _evalVariable:withCtx:].cold.1
- GCC_except_table109
- GCC_except_table113
- GCC_except_table120
- GCC_except_table128
- GCC_except_table144
- GCC_except_table167
- GCC_except_table171
- GCC_except_table193
- GCC_except_table198
- GCC_except_table75
- GCC_except_table86
- GCC_except_table89
- OBJC_IVAR_$_ATXDirichletDistribution.kBlendedScoreNormalizationConstant
- OBJC_IVAR_$_ATXDirichletDistribution.kGlobalScoreMultiplier
- _ATXSampleFromGammaDistribution
- _OBJC_$_PROP_LIST_ATXProactiveSuggestionClientModelEvaluatorPublishers.179
- _OBJC_CLASS_$_ATXBlendedLocalAndGlobalScores
- _OBJC_CLASS_$_ATXDirichletDistribution
- _OBJC_METACLASS_$_ATXBlendedLocalAndGlobalScores
- _OBJC_METACLASS_$_ATXDirichletDistribution
- _PROTOCOLS__TtC21AppPredictionInternal31ContextualEngineSuggestionStore.4
- __101-[ATXHomeScreenWidgetDiscoverabilityLogHarvester _logRankBasedMetricsWithOnboardingStacks:algorithm:]_block_invoke.174
- __102-[ATXAppSessionInterruptionsProvider cacheRecommendedAndCandidateAppsInDenyListForAllModesIfNecessary]_block_invoke.32
- __102-[ATXDigestOnboardingAppSelectionMetricsLogger logDigestOnboardingAppSelectionMetricsWithXPCActivity:]_block_invoke.20
- __103-[ATXAppSessionInterruptionsProvider cacheRecommendedAndCandidateAppsInAllowListForAllModesIfNecessary]_block_invoke.28
- __103-[ATXAppSessionInterruptionsProvider cacheRecommendedAndCandidateAppsInAllowListForAllModesIfNecessary]_block_invoke.30
- __103-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:completion:]_block_invoke.292
- __103-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:completion:]_block_invoke.295
- __105-[ATXAnchorModelDataStoreWrapper uniqueCandidateIdsThatOccurredAfterAnchor:candidateType:minOccurrences:]_block_invoke.401
- __105-[ATXAnchorModelDataStoreWrapper uniqueCandidateIdsThatOccurredAfterAnchor:candidateType:minOccurrences:]_block_invoke_2.402
- __105-[ATXAnchorModelDataStoreWrapper uniqueCandidateIdsThatOccurredAfterAnchor:candidateType:minOccurrences:]_block_invoke_2.402.cold.1
- __107-[ATXAppGroupedNotificationDigestRanker getRankedAppsFromAppGroupedNotificationStacks:maxAppMarqueeGroups:]_block_invoke.126
- __110-[ATXAnchorModelDataStoreWrapper assignMetricsForTrainingResult:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.150
- __110-[ATXAnchorModelDataStoreWrapper assignMetricsForTrainingResult:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.150.cold.1
- __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke.157
- __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.159
- __110-[ATXNotificationAndSuggestionDatabase hasSuggestionBeenShownForEntityId:suggestionType:scope:sinceTimestamp:]_block_invoke_2.159.cold.1
- __110-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromFileData:digestTimeString:outError:]_block_invoke.50
- __110-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromFileData:digestTimeString:outError:]_block_invoke.52
- __110-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromFileData:digestTimeString:outError:]_block_invoke.52.cold.1
- __111-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromFileData:modeString:outError:]_block_invoke.60
- __111-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromFileData:modeString:outError:]_block_invoke.61
- __111-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromFileData:modeString:outError:]_block_invoke.61.cold.1
- __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.439
- __112-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationWithBundleId:notificationId:recordTimestamp:]_block_invoke.439.cold.1
- __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.44
- __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.44.cold.1
- __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.99
- __113-[ATXAnchorModelDataStoreWrapper updateOrInsertCandidateEventToDatabaseWithCandidateFeatures:anchor:anchorEvent:]_block_invoke.99.cold.1
- __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke.242
- __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.254
- __113-[ATXNotificationAndSuggestionDatabase getSmartPauseFeaturesForBundleIds:sinceTimestamp:positiveEngagementEnums:]_block_invoke_2.254.cold.1
- __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.124
- __113-[ATXNotificationAndSuggestionDatabase insertNotificationFromEvent:deliveryMethod:modeIdentifier:deliveryReason:]_block_invoke.124.cold.1
- __114-[ATXAnchorModelDataStoreWrapper insertAnchorSuggestionOutcome:date:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.143
- __114-[ATXAnchorModelDataStoreWrapper insertAnchorSuggestionOutcome:date:anchorType:anchorEventIdentifier:candidateId:]_block_invoke.143.cold.1
- __114-[ATXCandidateRelevanceModelDataStore writeVerificationStatusForModelUUID:clientModelName:expectedNumberOfModels:]_block_invoke.378
- __114-[ATXHomeScreenLayoutSelector2 _assignExistingSuggestedSGWidgetsOnPages:withSuggestions:suggestionToRankingIndex:]_block_invoke.46
- __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.181
- __114-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentAndMessageNotificationsSinceTimestamp:]_block_invoke.181.cold.1
- __115+[ATXCandidateRelevanceModelDatasetGeneratorConfigMinimalAction candidatePublisherFromStartTime:endTime:datastore:]_block_invoke.101.cold.1
- __115+[ATXCandidateRelevanceModelDatasetGeneratorConfigMinimalAction candidatePublisherFromStartTime:endTime:datastore:]_block_invoke.95
- __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.178
- __116-[ATXNotificationAndSuggestionDatabase engagementStatusOfActiveAndProminentNotificationsWithUrgency:sinceTimestamp:]_block_invoke.178.cold.1
- __116-[ATXWidgetPredictionTrainer trainWidgetPredictionModelWithMLArrayBatchProvider:modelURL:andSaveToURL:withActivity:]_block_invoke.23
- __116-[ATXWidgetPredictionTrainer trainWidgetPredictionModelWithMLArrayBatchProvider:modelURL:andSaveToURL:withActivity:]_block_invoke.23.cold.1
- __116-[ATXWidgetPredictionTrainer trainWidgetPredictionModelWithMLArrayBatchProvider:modelURL:andSaveToURL:withActivity:]_block_invoke.23.cold.2
- __118-[ATXInformationEngine initWithFilter:featurizer:ranker:infoStore:confidenceMapper:abuseControlConfig:featureWeights:]_block_invoke.33
- __119-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:clientModelName:completion:]_block_invoke.302
- __119-[ATXCandidateRelevanceModelDataStore receiveMostRecentVerifiedTrainedModelTrainingResults:clientModelName:completion:]_block_invoke_2.303
- __121-[ATXCandidateRelevanceModelDatasetGenerator initWithConfig:inferredModeStream:computedModeStream:pointOfInterestStream:]_block_invoke.131
- __121-[ATXPredictionContextBuilder(CandidateContext) predictionContextForCurrentContextAndCandidatePublisher:contextOverride:]_block_invoke.5
- __122-[ATXProactiveSuggestionShadowLogger enumerateShadowLoggingResultsWithBlock:clientModelCacheUpdatedBlock:completionBlock:]_block_invoke.21
- __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.24
- __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.24.cold.1
- __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.24.cold.2
- __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.32
- __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.39
- __123-[ATXHomeScreenLogUploader uploadHomeScreenSummaryLogsToCoreAnalyticsWithActivity:customStartDate:dryRunCompletionHandler:]_block_invoke.39.cold.1
- __123-[_ATXDataStore updateOrInsertInstallTimestamp:genreId:subGenreIds:app2VecCluster:forBundleId:isExtension:isEnterpriseApp:]_block_invoke.1165
- __123-[_ATXDataStore updateOrInsertInstallTimestamp:genreId:subGenreIds:app2VecCluster:forBundleId:isExtension:isEnterpriseApp:]_block_invoke.1165.cold.1
- __124-[ATXStableContactRepresentationDatabase insertCnContactIdToStableContactIdentifierWithCnContactId:stableContactIdentifier:]_block_invoke.5
- __124-[ATXStableContactRepresentationDatabase insertCnContactIdToStableContactIdentifierWithCnContactId:stableContactIdentifier:]_block_invoke.5.cold.1
- __125-[ATXNotificationTelemetryLogger userNotificationWithUUID:withTimeStamp:urgency:fromNotificationStreamWithStartTime:endTime:]_block_invoke.34
- __130-[ATXNPlusOneStudyUploader _processClientModelUpdateStreamFromStartTime:shortcutSuggestionHandler:infoSuggestionHandler:activity:]_block_invoke.228
- __130-[ATXNPlusOneStudyUploader _processClientModelUpdateStreamFromStartTime:shortcutSuggestionHandler:infoSuggestionHandler:activity:]_block_invoke.228.cold.1
- __131-[_ATXAppLaunchCategoricalHistogram initWithHistogram:categoryToCategoryId:maxCategoryId:maxCategoryCount:lastDates:pruningMethod:]_block_invoke.56
- __135-[ATXPredictionDataHistograms initWithAppInfoManager:bundleIdTable:launchSequenceManager:histogramManager:dataStore:persistHistograms:]_block_invoke.25
- __136+[ATXAppPredictorFeedback constructFeatureDictionaryWithFeedbackItems:engagedItem:shownItemIndexes:consumerType:histogramBundleIdTable:]_block_invoke.60
- __140-[ATXAnchorModelEventHarvester fetchAppLaunchEventsAfterAnchorOccurrenceDate:limit:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.19
- __140-[ATXAnchorModelEventHarvester fetchAppLaunchEventsAfterAnchorOccurrenceDate:limit:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.19.cold.1
- __140-[ATXAnchorModelEventHarvester fetchAppLaunchEventsAfterAnchorOccurrenceDate:limit:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.22
- __143-[ATXAnchorModelEventHarvester fetchEventsAfterAnchorOccurenceDate:withBiomePublisher:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.11
- __143-[ATXAnchorModelEventHarvester fetchEventsAfterAnchorOccurenceDate:withBiomePublisher:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.11.cold.1
- __143-[ATXAnchorModelEventHarvester fetchEventsAfterAnchorOccurenceDate:withBiomePublisher:maxSecondsBeforeAnchor:maxSecondsAfterAnchor:isIncluded:]_block_invoke.14
- __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.68
- __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.68.cold.1
- __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.70
- __144-[_ATXClientModelShadowMetricsDataSourceBase replayHistoryWithShadowEventPublisher:startDate:endDate:shadowEventHandler:predictionCacheHandler:]_block_invoke.70.cold.1
- __145-[ATXInformationEngine _pushPredictionsToBlendingLayerIfDifferentFromTheLastCacheUpdate:forClientModel:withClientModelVersion:cachedSuggestions:]_block_invoke.55
- __146-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromSource:digestTimeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.55
- __146-[ATXNotificationManagementInspector fetchSerializedNotificationDigestFromSource:digestTimeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.55.cold.1
- __147-[ATXHomeScreenWidgetDiscoverabilityLogHarvester _generateWidgetDiscoverabilityMetricsWithHomeScreenItemProducer:descriptors:appMetrics:algorithm:]_block_invoke.154
- __147-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromSource:modeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.62
- __147-[ATXNotificationManagementInspector fetchSerializedMissedNotificationRankingFromSource:modeString:startDate:endDate:shouldInferMessages:outError:]_block_invoke.62.cold.1
- __149-[_ATXAppLaunchMonitor handleAppOrClipLaunchNotificationForBundleId:poweringAppClipBundleId:urlHash:isClip:appLaunchReason:appClipLaunchReason:date:]_block_invoke.130
- __173-[ATXTimelineRelevanceMetricHarvester _addRotationHistoryForWidgetBundleId:appBundleId:widgetKind:widgetSize:withPBTimelineRelevanceContainer:anonymizeTimestampsRelativeTo:]_block_invoke.137
- __173-[ATXTimelineRelevanceMetricHarvester _addRotationHistoryForWidgetBundleId:appBundleId:widgetKind:widgetSize:withPBTimelineRelevanceContainer:anonymizeTimestampsRelativeTo:]_block_invoke.137.cold.1
- __173-[ATXTimelineRelevanceMetricHarvester _addRotationHistoryForWidgetBundleId:appBundleId:widgetKind:widgetSize:withPBTimelineRelevanceContainer:anonymizeTimestampsRelativeTo:]_block_invoke.139
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.100
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.108
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.110
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.119
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.119.cold.1
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.126
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.82
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.90
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke.95
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.101
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.109
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.111
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.127
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.83
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.91
- __175-[ATXAppDirectoryOrderingProvider initWithAppInfoManager:cache:blacklist:recentsCache:hiddenAppsCache:appClipDataProvider:appIconState:appClipChangeListener:histogramManager:]_block_invoke_2.96
- __188+[ATXActionPredictions _predictionsForConsumerSubType:thirdStageScoreLogger:multiStageScoreLogger:context:actionPredictionCandidates:remainingPredictionItems:predictionsPerAppActionLimit:]_block_invoke.63
- __188+[ATXActionPredictions _predictionsForConsumerSubType:thirdStageScoreLogger:multiStageScoreLogger:context:actionPredictionCandidates:remainingPredictionItems:predictionsPerAppActionLimit:]_block_invoke.63.cold.1
- __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke.552
- __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke.557
- __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_2.553
- __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_2.561
- __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_3.554
- __191-[_ATXDataStore writeActionType:bundleId:date:action:slotSets:timeZone:prevLocationUUID:locationUUID:weight:actionUUID:motionType:appSessionStartDate:appSessionEndDate:geohash:coarseGeohash:]_block_invoke_3.554.cold.1
- __200-[_ATXAppPredictor predictWithLimit:consumerSubType:intent:candidateBundleIdentifiers:candidateActiontypes:scoreLogger:predictionItemsToKeep:predictedItemsOutParameter:context:datastore:featureCache:]_block_invoke.153
- __209-[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]_block_invoke.41
- __209-[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]_block_invoke.45
- __212-[ATXRSWidgetSuggestionProducer initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.35
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.41
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.41.cold.1
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.42
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.42.cold.1
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.55
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.58
- __215+[ATXActionPredictions _actionPredictionCandidatesForCandidateBundleIdentifiers:candidateActiontypes:firstStageScoreLogger:secondStageScoreLogger:multiStageScoreLogger:context:featureCache:remainingPredictionItems:]_block_invoke.58.cold.1
- __27-[_ATXAppIconState _reload]_block_invoke.60
- __28-[_ATXDataStore loadAppInfo]_block_invoke.316
- __29-[_ATXAppLaunchMonitor start]_block_invoke.72
- __29-[_ATXAppLaunchMonitor start]_block_invoke.76
- __30-[ATXLockscreenBlacklist init]_block_invoke.24
- __30-[ATXLockscreenBlacklist init]_block_invoke.26
- __30-[_ATXFeedback doDecayAtTime:]_block_invoke.66
- __31-[ATXFaceSuggestionServer init]_block_invoke.24
- __31-[ATXFaceSuggestionServer init]_block_invoke.38
- __33-[ATXAppModeModel scoredEntities]_block_invoke.21
- __34-[ATXAppLaunchMicroLocation train]_block_invoke.59
- __34-[ATXAppLaunchMicroLocation train]_block_invoke.68
- __34-[ATXHistogramData countWhereA:b:]_block_invoke.20
- __34-[_ATXDataStore loadAppActionInfo]_block_invoke.323
- __37-[ATXContactModeModel scoredEntities]_block_invoke.24
- __38-[_ATXInspectionServer getActionLogs:]_block_invoke.195
- __41-[ATXAppModeDenyListModel scoredEntities]_block_invoke.21
- __41-[ATXClientModelSuggestionReceiver start]_block_invoke.34
- __41-[ATXClientModelSuggestionReceiver start]_block_invoke.34.cold.1
- __41-[ATXDuetKnowledgeStoreManager runBlock:]_block_invoke.3
- __41-[_ATXAppLaunchLocation loadModelAtPath:]_block_invoke.83
- __41-[_ATXAppLaunchLocation loadModelAtPath:]_block_invoke.95
- __43+[ATXActionPredictionsProcessor userAlarms]_block_invoke.43
- __43+[ATXActionPredictionsProcessor userAlarms]_block_invoke.43.cold.1
- __43-[ATXModeAnchorModelSuggestionClient _init]_block_invoke.6
- __43-[ATXNotificationCategorizationServer init]_block_invoke.36
- __43-[ATXNotificationCategorizationServer init]_block_invoke_2.41
- __43-[_ATXDataStore _appInfoForBundleIdNoSync:]_block_invoke.240
- __43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke.783
- __43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.785
- __43-[_ATXDataStore _removeActionsWithoutTitle]_block_invoke_2.785.cold.1
- __43-[_ATXInspectionServer histogramsInMemory:]_block_invoke.230
- __44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.94
- __44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.94.cold.1
- __44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.97
- __44-[ATXModeConfigurationLogger retrieveEvents]_block_invoke.64
- __44-[ATXStackStateTracker persistInternalState]_block_invoke.199
- __44-[_ATXAppLaunchMonitor registerForAppChange]_block_invoke.102
- __44-[_ATXAppLaunchMonitor registerForAppChange]_block_invoke.89
- __44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.759
- __44-[_ATXDataStore removeAllSlotsFromActionLog]_block_invoke.759.cold.1
- __45-[ATXContactModeDenyListModel scoredEntities]_block_invoke.24
- __45-[ATXFaceSuggestionRecentlyViewedSignal init]_block_invoke.14
- __45-[ATXHistogramBundleIdTable permutationFrom:]_block_invoke.138
- __45-[ATXHistogramBundleIdTable permutationFrom:]_block_invoke.138.cold.1
- __45-[_ATXDataStore loadLaunchesFollowingBundle:]_block_invoke.360
- __46-[ATXAppIntentMonitor _listenToActivityStream]_block_invoke.85
- __46-[ATXAppPredictionBlacklist _listenForUpdates]_block_invoke.35
- __46-[ATXPosterDescriptorCache updateDescriptors:]_block_invoke.27
- __47-[ATXModeScoringSessionRange attachAppLaunches]_block_invoke.9
- __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.393
- __47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.393.cold.1
- __47-[_ATXDataStore _markBundleId:asEnterpriseApp:]_block_invoke.1176
- __47-[_ATXDataStore writeBlob:type:expirationDate:]_block_invoke.503
- __47-[_ATXDataStore(WebClip) writeWebClip:appClip:]_block_invoke.24
- __47-[_ATXDataStore(WebClip) writeWebClip:appClip:]_block_invoke.24.cold.1
- __48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.105
- __48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.105.cold.1
- __48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.112
- __48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.76
- __48-[ATXServer listener:shouldAcceptNewConnection:]_block_invoke.76.cold.1
- __48-[_ATXDataStore loadAppActionLaunchesFollowing:]_block_invoke.373
- __48-[_ATXInspectionServer createAppPredictionLogs:]_block_invoke.130
- __48-[_ATXInspectionServer createAppPredictionLogs:]_block_invoke.132
- __49-[ATXModeAnchorModelSuggestionClient _pingServer]_block_invoke.12
- __49-[ATXModeSetupExperienceMetricsLogger logMetrics]_block_invoke.11
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.61
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.64
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.66
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.68
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.71
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.76
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.78
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke.80
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.72
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.72.cold.1
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.72.cold.2
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.77
- __49-[ATXModeSetupPredictionMetricsLogger logMetrics]_block_invoke_2.84
- __49-[ATXSuggestionModeFilter registerForModeChanges]_block_invoke.31
- __49-[ATXSuggestionModeFilter registerForModeChanges]_block_invoke.31.cold.1
- __49-[_ATXDataStore regenerateSlotSetKeyForBundleId:]_block_invoke.694
- __49-[_ATXInspectionServer histogramsInMemoryBySize:]_block_invoke.234
- __49-[_ATXInspectionServer histogramsInMemoryBySize:]_block_invoke.237
- __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.38
- __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.38.cold.1
- __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.43
- __50-[_ATXAppIconState initWithHomeScreenConfigCache:]_block_invoke.46
- __50-[_ATXAppLaunchMonitor registerForBacklightChange]_block_invoke.119
- __50-[_ATXAppLaunchMonitor registerForBacklightChange]_block_invoke.126
- __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.688
- __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke.690
- __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.689
- __50-[_ATXDataStore _regenerateSlotSetKeyForBundleId:]_block_invoke_2.691
- __51-[_ATXDataStore pruneMessageRecipientsAddedBefore:]_block_invoke.188
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.704
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.705
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.709
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.720
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke.721
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_2.713
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_2.725
- __51-[_ATXDataStore trimActionHistoryWithAppWhitelist:]_block_invoke_3.729
- __52-[ATXAbstractVersionedDatabase currentSchemaVersion]_block_invoke.32
- __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.12
- __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.14
- __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.14.cold.1
- __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.17
- __52-[ATXUserEducationSuggestionModeChangeNotifier init]_block_invoke.17.cold.1
- __52-[_ATXDataStore actionExistsForBundleId:actionType:]_block_invoke.411
- __52-[_ATXDataStore actionExistsForBundleId:actionType:]_block_invoke_2.412
- __53-[ATXAppIntentMonitor handleIntentOrActivityDeletion]_block_invoke.159
- __53-[ATXAppIntentMonitor handleIntentOrActivityDeletion]_block_invoke.161
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.333
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.333.cold.1
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.334
- __53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.334.cold.1
- __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.116
- __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.116.cold.1
- __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.117
- __53-[ATXSpotlightLayoutSelector _indexSpotlightActions:]_block_invoke.117.cold.1
- __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.18
- __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.20
- __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.20.cold.1
- __53-[ATXUnifiedActivityBiomeStream efficientCurrentMode]_block_invoke.21
- __53-[_ATXDataStore(WebClip) webClipsForAppClipBundleId:]_block_invoke.15
- __53-[_ATXDataStore(WebClip) webClipsForAppClipBundleId:]_block_invoke.17
- __53-[_ATXDataStore(WebClip) webClipsForAppClipBundleId:]_block_invoke.17.cold.1
- __54-[_ATXAppLaunchLocation _trainModelWithLOI:startDate:]_block_invoke.64
- __54-[_ATXAppLaunchLocation _trainModelWithLOI:startDate:]_block_invoke.74
- __54-[_ATXDataStore enumerateActionOfType:bundleId:block:]_block_invoke.582
- __54-[_ATXDataStore enumerateActionOfType:bundleId:block:]_block_invoke_2.583
- __55-[ATXAnchorModelInferenceEngine exitCallbackForAnchor:]_block_invoke.56
- __55-[ATXAppLaunchProvider cacheAppLaunchStreamIfNecessary]_block_invoke.9
- __55-[ATXModeTimelineManager _modeTimelineDataFrom:toDate:]_block_invoke.28
- __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.38
- __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.38.cold.1
- __55-[ATXNotificationAndSuggestionDatastore updateDatabase]_block_invoke.43
- __55-[ATXUserEducationSuggestionFocusModeSetupTrigger init]_block_invoke.17
- __55-[_ATXDataStore addAppLaunchForAppLaunchSequence:date:]_block_invoke.481
- __56+[ATXAppDirectoryOrderingProvider _reorderedRecentApps:]_block_invoke.163
- __56-[ATXCorrelatedEventsManager insertEvents:forEventType:]_block_invoke.21
- __56-[ATXCorrelatedEventsManager insertEvents:forEventType:]_block_invoke.22
- __56-[ATXHeroDataServer listener:shouldAcceptNewConnection:]_block_invoke.43
- __56-[ATXModeConfigurationLogger logMetricForConfiguration:]_block_invoke.51
- __56-[ATXModeConfigurationLogger logMetricForConfiguration:]_block_invoke.55
- __56-[ATXModeConfigurationLogger logMetricForConfiguration:]_block_invoke.56
- __56-[_ATXDataStore _enumerateAppInfoBundlesExecutingBlock:]_block_invoke.389
- __56-[_ATXDataStore _enumerateAppInfoBundlesExecutingBlock:]_block_invoke.389.cold.1
- __57-[ATXActionNotificationServer deliveredNotificationCount]_block_invoke.181
- __58+[ATXIdleTimeBeginAnchor weightedAverageOfHoursFromDates:]_block_invoke.26
- __58-[ATXFaceGalleryLayoutGenerator rankedFeaturedDescriptors]_block_invoke.56
- __58-[ATXHeroPoiManager poiCategoryEventsWithStreamPublisher:]_block_invoke.23
- __58-[ATXMinimalAction actionFromDatastoreLookupForDatastore:]_block_invoke.14
- __58-[ATXMinimalAction actionFromDatastoreLookupForDatastore:]_block_invoke.17
- __58-[ATXMinimalAction actionFromDatastoreLookupForDatastore:]_block_invoke.17.cold.1
- __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.31
- __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.38
- __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.38.cold.1
- __58-[ATXRSRelevanceMonitor _queue_startMonitoringModeChanges]_block_invoke.41
- __58-[ATXWidgetModeModel scoredEntitiesWithScoredAppEntities:]_block_invoke.21
- __59-[ATXAnchorModelDataStoreWrapper trainingResultsForAnchor:]_block_invoke.192
- __59-[ATXAnchorModelDataStoreWrapper trainingResultsForAnchor:]_block_invoke.192.cold.1
- __59-[ATXAnchorModelInferenceEngine entranceCallbackForAnchor:]_block_invoke.54
- __59-[ATXChinSuggestionThrottlingManager _acceptPendingRequest]_block_invoke.70
- __59-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke.cold.1
- __59-[_ATXInspectionServer listener:shouldAcceptNewConnection:]_block_invoke.19
- __59-[_ATXInspectionServer listener:shouldAcceptNewConnection:]_block_invoke.19.cold.1
- __60-[ATXAppDirectoryServer listener:shouldAcceptNewConnection:]_block_invoke.20
- __60-[ATXAppDirectoryServer listener:shouldAcceptNewConnection:]_block_invoke.20.cold.1
- __60-[ATXProactiveSuggestionShadowLogger shadowLoggingPublisher]_block_invoke.28
- __61-[ATXUsageInsightsServer listener:shouldAcceptNewConnection:]_block_invoke.17
- __61-[ATXUsageInsightsServer listener:shouldAcceptNewConnection:]_block_invoke.17.cold.1
- __62-[ATXFaceSuggestionAssetParameters dayZeroFeaturedDescriptors]_block_invoke.109
- __62-[ATXFaceSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.49
- __62-[ATXFaceSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.49.cold.1
- __62-[ATXInfoSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.33
- __62-[ATXUpdatePredictionsManager processLockscreenFeedbackNoSync]_block_invoke.43
- __62-[_ATXAppInstallMonitor noSyncUpdateWithWaitTime:andBackdate:]_block_invoke.41
- __62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke.928
- __62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.931
- __62-[_ATXDataStore migration_DeprecateIntentForAllAppsHistograms]_block_invoke_2.931.cold.1
- __63-[ATXSettingsActionsServer listener:shouldAcceptNewConnection:]_block_invoke.13
- __63-[ATXSettingsActionsServer listener:shouldAcceptNewConnection:]_block_invoke.13.cold.1
- __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.55
- __63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.55.cold.1
- __63-[ATXUserEducationSuggestionExploreFacesServer scheduleNextTry]_block_invoke.23
- __64-[ATXActionPredictionServer listener:shouldAcceptNewConnection:]_block_invoke.31
- __64-[ATXActionPredictionServer listener:shouldAcceptNewConnection:]_block_invoke.31.cold.1
- __64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.77
- __64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.77.cold.1
- __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.228
- __64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.228.cold.1
- __64-[ATXNotificationAndSuggestionDatabase getBookmarkDataFromName:]_block_invoke.78
- __64-[ATXNotificationAndSuggestionDatabase getBookmarkDataFromName:]_block_invoke.80
- __64-[ATXNotificationAndSuggestionDatabase getBookmarkDataFromName:]_block_invoke.80.cold.1
- __64-[ATXNotificationAndSuggestionDatabase setBookmarkData:forName:]_block_invoke.90
- __64-[ATXNotificationAndSuggestionDatabase setBookmarkData:forName:]_block_invoke.90.cold.1
- __64-[ATXStackStateTracker updateStackRotationEventsByQueryingBiome]_block_invoke.176
- __64-[ATXStackStateTracker updateStackRotationEventsByQueryingBiome]_block_invoke.176.cold.1
- __64-[ATXStackStateTracker updateStackRotationEventsByQueryingBiome]_block_invoke.180
- __64-[_ATXDataStore _deserializeActionLogRowWithStmt:invokingBlock:]_block_invoke.570
- __65-[ATXBlendingBiomeStreamLogger logBlendingMetricsFromBiomeStream]_block_invoke.25
- __65-[ATXDigestFeedbackProcessingPipeline logMetricsWithXPCActivity:]_block_invoke.16
- __65-[ATXInferredModesAccumulator usageInsightsInferredATXModeEvents]_block_invoke.6
- __65-[_ATXDataStore enumerateFeedbackForActionOfType:bundleId:block:]_block_invoke.753
- __66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.148
- __66+[ATXComplicationSuggestionHeuristics _countedHomeAccessoryEvents]_block_invoke.148.cold.1
- __66-[ATXAppLaunchMicroLocation tryLoadCorrelationMatricesImmediately]_block_invoke.74
- __66-[ATXStableContactRepresentationDatabase stableContactIdentifier:]_block_invoke.12
- __66-[ATXStableContactRepresentationDatabase stableContactIdentifier:]_block_invoke.12.cold.1
- __66-[ATXStableContactRepresentationDatabase stableContactIdentifier:]_block_invoke.9
- __66-[ATXUserEducationSuggestionExploreFacesServer backlightEventSink]_block_invoke.45
- __66-[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:]_block_invoke.23
- __66-[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:]_block_invoke.26
- __66-[_ATXDataStore(ActionTypes) enumerateActionTypesOlderThan:block:]_block_invoke.26.cold.1
- __67-[ATXDeviceUsageModeLoggingPipeline logDeviceUsageWithXPCActivity:]_block_invoke.30
- __67-[ATXDeviceUsageModeLoggingPipeline logDeviceUsageWithXPCActivity:]_block_invoke.30.cold.1
- __67-[ATXDeviceUsageModeLoggingPipeline logDeviceUsageWithXPCActivity:]_block_invoke.30.cold.2
- __67-[ATXPredictionJSONScoreLogger flushWithCompletion:filenameSuffix:]_block_invoke.63
- __67-[ATXSuggestedPagesHomeScreenModificationsMetricsLogger logMetrics]_block_invoke.17
- __67-[ATXSuggestedPagesHomeScreenModificationsMetricsLogger logMetrics]_block_invoke.17.cold.1
- __67-[ATXSuggestedPagesHomeScreenModificationsMetricsLogger logMetrics]_block_invoke.21
- __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.29
- __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.29.cold.1
- __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.31
- __67-[ATXUserEducationSuggestionExploreFacesServer tryToSendSuggestion]_block_invoke.31.cold.1
- __68-[ATXNPlusOneStudyUploader _preparedEvents_numAppLaunches:activity:]_block_invoke.219
- __68-[ATXNPlusOneStudyUploader _preparedEvents_numAppLaunches:activity:]_block_invoke.219.cold.1
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.128
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.132
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.132.cold.1
- __68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_2.129
- __69-[ATXAnchorModelDataStoreWrapper deleteSamplesForBundleIdsNotInList:]_block_invoke.321
- __69-[ATXAnchorModelDataStoreWrapper deleteSamplesForBundleIdsNotInList:]_block_invoke.322
- __69-[ATXAnchorModelDataStoreWrapper deleteSamplesForBundleIdsNotInList:]_block_invoke.322.cold.1
- __69-[ATXCandidateRelevanceModelDataStore candidateIdForCandidate:error:]_block_invoke.283
- __69-[ATXCandidateRelevanceModelDataStore candidateIdForCandidate:error:]_block_invoke_2.284
- __69-[ATXMindlessCyclingUsageAccumulator accumulateMindlessCyclingEvents]_block_invoke.8
- __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.195
- __69-[ATXNotificationAndSuggestionDatabase mostRecentActiveNotifications]_block_invoke.195.cold.1
- __69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke.1035
- __69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.1042
- __69-[_ATXDataStore migration_forceUpdateNewCrystalSystemAppsInstallDate]_block_invoke_2.1042.cold.1
- __69-[_ATXFeedback putFeedbackScoresForApps:intoScores:confirms:rejects:]_block_invoke.79
- __70+[ATXScoreInterpreterFromAssetBuilder scoreInterpretersForAllSubTypes]_block_invoke.31
- __70+[ATXScoreInterpreterFromAssetBuilder scoreInterpretersForAllSubTypes]_block_invoke.36
- __70+[_ATXAppLaunchMonitor _harvestAppPredictionDataForBundleId:response:]_block_invoke.138
- __70-[ATXAnchorModelDataStoreWrapper populateCachedCountsForCandidateIds:]_block_invoke.361
- __70-[ATXAnchorModelDataStoreWrapper populateCachedCountsForCandidateIds:]_block_invoke_2.364
- __70-[ATXDefaultWidgetSuggesterServer listener:shouldAcceptNewConnection:]_block_invoke.16
- __70-[ATXDefaultWidgetSuggesterServer listener:shouldAcceptNewConnection:]_block_invoke.16.cold.1
- __70-[ATXNPlusOneStudyUploader _preparedEvents_suggestionCounts:activity:]_block_invoke.226
- __70-[ATXNPlusOneStudyUploader _preparedEvents_suggestionCounts:activity:]_block_invoke.226.cold.1
- __70-[_ATXAppInfoManager computeAverageAndMedianSecondsBetweenAppLaunches]_block_invoke.46
- __71+[ATXActionPredictions filterHighQualityActionResults:consumerSubType:]_block_invoke.81
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.271
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.271.cold.1
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.284
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.286
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.286.cold.1
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.299
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.302
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke.302.cold.1
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.278
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.278.cold.1
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.285
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.293
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.293.cold.1
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.301
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.309
- __71-[ATXAnchorModelDataStoreWrapper deleteSamplesThatAreMoreThan28DaysOld]_block_invoke_2.309.cold.1
- __71-[ATXNotificationDeliverySuggestionManager activeSuggestionsWithReply:]_block_invoke.33
- __71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.64
- __71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.64.cold.1
- __71-[ATXSettingsActionsServer recentActionsWithRequest:completionHandler:]_block_invoke.30
- __71-[_ATXDataStore numActionKeyOccurrencesForActionKey:startDate:endDate:]_block_invoke.630
- __72+[ATXCandidateRelevanceModelOfflineDataHarvester modelMetricsForConfig:]_block_invoke.20
- __72+[ATXCandidateRelevanceModelOfflineDataHarvester modelMetricsForConfig:]_block_invoke.20.cold.1
- __72-[ATXActionNotificationServer proactiveSuggestionsCurrentlyOnLockscreen]_block_invoke.184
- __72-[ATXAnchorModelDataStoreWrapper uniqueAnchorEventIdentifiersForAnchor:]_block_invoke.338
- __72-[ATXAnchorModelDataStoreWrapper uniqueAnchorEventIdentifiersForAnchor:]_block_invoke.338.cold.1
- __72-[ATXAppSessionModeLoggingPipeline logAppSessionMetricsWithXPCActivity:]_block_invoke.24
- __72-[ATXAppSessionModeLoggingPipeline logAppSessionMetricsWithXPCActivity:]_block_invoke.24.cold.1
- __72-[ATXAppSessionModeLoggingPipeline logAppSessionMetricsWithXPCActivity:]_block_invoke.24.cold.2
- __72-[ATXCandidateRelevanceModelTrainer generateAndSaveDatasetWithFilename:]_block_invoke.19
- __72-[ATXCandidateRelevanceModelTrainer generateAndSaveDatasetWithFilename:]_block_invoke.42
- __72-[ATXInformationEngine getSuggestionsForInfoSourceIdentifier:withReply:]_block_invoke.80
- __72-[ATXModeEntitySuggestions suggestedBundleIDsForDenyListWithCompletion:]_block_invoke.18
- __72-[ATXNotificationDigestRankerServer listener:shouldAcceptNewConnection:]_block_invoke.78
- __72-[ATXNotificationDigestRankerServer listener:shouldAcceptNewConnection:]_block_invoke.78.cold.1
- __72-[_ATXAppLaunchHistogram initWithHistogram:bucketCount:filter:timeBase:]_block_invoke.31
- __72-[_ATXDataStore(IntentCache) writeSupportsBackgroundExecution:cacheKey:]_block_invoke.39
- __72-[_ATXDataStore(IntentCache) writeSupportsBackgroundExecution:cacheKey:]_block_invoke.39.cold.1
- __73+[ATXDeviceBacklightHelper getScreenOnIntervalsBetweenStartDate:endDate:]_block_invoke.5
- __73-[ATXAnchorModelDataStoreWrapper dateAnchorModelWasLastTrainedForAnchor:]_block_invoke.199
- __73-[ATXAnchorModelDataStoreWrapper dateAnchorModelWasLastTrainedForAnchor:]_block_invoke.199.cold.1
- __73-[ATXCandidateRelevanceModelServer sortedProactiveSuggestionsForContext:]_block_invoke.23
- __73-[ATXCandidateRelevanceModelServer sortedProactiveSuggestionsForContext:]_block_invoke.23.cold.1
- __73-[ATXCandidateRelevanceModelServer sortedProactiveSuggestionsForContext:]_block_invoke.28
- __73-[ATXHomeScreenFocusSuggestionLogger logHomeScreenFocusSuggestionMetrics]_block_invoke.10
- __73-[ATXHomeScreenFocusSuggestionLogger logHomeScreenFocusSuggestionMetrics]_block_invoke.20
- __73-[ATXModeEntitySuggestions suggestedBundleIDsForAllowListWithCompletion:]_block_invoke.12
- __73-[ATXModeEntitySuggestions suggestedBundleIDsForAllowListWithCompletion:]_block_invoke.15
- __73-[ATXModeFaceComplicationHeuristicDataSource _hasSignificantStocksEvents]_block_invoke.121
- __73-[ATXNotificationDeliverySuggestionManager digestHasBeenShownEnoughTimes]_block_invoke.29
- __73-[ATXNotificationsEventProvider cacheGlobalNotificationStreamIfNecessary]_block_invoke.11
- __73-[_ATXHomeScreenStackState widgetForSuggestion:considerSuggestedWidgets:]_block_invoke.14
- __73-[_PASSqliteDatabase(ATXExtras) atx_countRowsOfTable:returnValueOnError:]_block_invoke.2
- __74-[ATXActivitySuggestionsFeedbackProcessor processFeedbackWithXPCActivity:]_block_invoke.17
- __74-[ATXActivitySuggestionsFeedbackProcessor processFeedbackWithXPCActivity:]_block_invoke.17.cold.1
- __74-[ATXCandidateRelevanceModelDatasetGenerator receiveDataPoint:completion:]_block_invoke.137
- __74-[ATXModeEntityCorrelator featuresForEntitiesFromCompleteCorrelatorState:]_block_invoke.20
- __74-[ATXNotificationCategorizationServer listener:shouldAcceptNewConnection:]_block_invoke.62
- __74-[ATXNotificationCategorizationServer listener:shouldAcceptNewConnection:]_block_invoke.62.cold.1
- __75+[ATXComplicationSuggestionHeuristics _numBluetoothConnectionsOverLastWeek]_block_invoke.133
- __75-[ATXAnchorModelDataStoreWrapper numModeOccurrencesInAllContextsForModeId:]_block_invoke.375
- __75-[ATXBiomePrivacyPruner pruneWithStreamIdentifier:activity:config:endTime:]_block_invoke.84
- __75-[ATXContinuousUsageAccumulator successfullyAccumulatedContinuousUseEvents]_block_invoke.9
- __75-[ATXNPlusOneStudyUploader _preparedEvents_appScreenTimeCategory:activity:]_block_invoke.210
- __75-[ATXNPlusOneStudyUploader _preparedEvents_appScreenTimeCategory:activity:]_block_invoke.210.cold.1
- __75-[ATXNotificationResolutionAccumulator historicalResolutionForNotification]_block_invoke.61
- __75-[ATXNotificationResolutionAccumulator historicalResolutionForNotification]_block_invoke.61.cold.1
- __75-[ATXNotificationResolutionAccumulator historicalResolutionForNotification]_block_invoke.64
- __75-[ATXUserNotificationDigest(EngagementTracking) computeNumDigestExpansions]_block_invoke.26
- __75-[ATXUserNotificationDigest(EngagementTracking) computeNumDigestExpansions]_block_invoke.30
- __76-[ATXLockScreenNotificationRankerServer listener:shouldAcceptNewConnection:]_block_invoke.14
- __76-[ATXLockScreenNotificationRankerServer listener:shouldAcceptNewConnection:]_block_invoke.14.cold.1
- __76-[ATXMLActionProducer _getActionsFromCacheForConsumerSubType:cacheFileData:]_block_invoke.24
- __77+[ATXCandidateRelevanceModelOfflineDataHarvester candidateMetricsFromConfig:]_block_invoke.12
- __77+[ATXCandidateRelevanceModelOfflineDataHarvester candidateMetricsFromConfig:]_block_invoke.12.cold.1
- __77+[ATXCandidateRelevanceModelOfflineDataHarvester candidateMetricsFromConfig:]_block_invoke.14
- __77-[ATXDailyNotificationsAccumulator successfullyAccumulatedNotificationEvents]_block_invoke.8
- __77-[ATXModeInferredDurationAndCountProvider cacheInferredModeStreamIfNecessary]_block_invoke.7
- __77-[ATXNotificationResolutionAccumulator computeTimeToLaunchAppForNotification]_block_invoke.44
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.1
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.2
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.3
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.4
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.5
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.6
- __78-[ATXContextHeuristicsMetricCollector lifetimeEngagementMetricsWithPublisher:]_block_invoke.38.cold.7
- __78-[ATXDigestOnboardingMetricsLogger logDigestOnboardingMetricsWithXPCActivity:]_block_invoke.20
- __78-[ATXFaceSuggestionServer reloadLockScreenSuggestionsWithActivity:completion:]_block_invoke.72
- __78-[ATXFaceSuggestionServer reloadLockScreenSuggestionsWithActivity:completion:]_block_invoke.72.cold.1
- __78-[ATXFaceSuggestionServer reloadLockScreenSuggestionsWithActivity:completion:]_block_invoke.72.cold.2
- __78-[ATXInformationEngine _updatePredictionRefreshDateIfNecessaryForSuggestions:]_block_invoke.72
- __78-[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:]_block_invoke.100
- __78-[ATXModeFaceSuggestionGenerator _posterCandidatesForModeType:allDescriptors:]_block_invoke.98
- __78-[ATXRecentAndSuggestedAppsLayoutSelector _accumulateRecentAppLaunchBundleIds]_block_invoke.27
- __78-[ATXRecentAndSuggestedAppsLayoutSelector _accumulateRecentAppLaunchBundleIds]_block_invoke.31
- __78-[_ATXDataStore(IntentCache) validParameterCombinationsWithSchemaForCacheKey:]_block_invoke.23
- __78-[_ATXDataStore(IntentCache) validParameterCombinationsWithSchemaForCacheKey:]_block_invoke.25
- __78-[_ATXDataStore(IntentCache) validParameterCombinationsWithSchemaForCacheKey:]_block_invoke.25.cold.1
- __79-[ATXCandidateRelevanceModelDatasetGenerator receiveDatasetSession:completion:]_block_invoke.140
- __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.330
- __79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.330.cold.1
- __79-[ATXRSWidgetSuggestionProducer _candidatesFromRelevantShortcutsFromStartDate:]_block_invoke.56
- __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.16
- __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.20
- __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.24
- __79-[ATXTripDuetDataProvider groupTripsFromPublisher:startTimestamp:endTimestamp:]_block_invoke.24.cold.1
- __80+[ATXFaceSuggestionAssetParameters posterDescriptorFromKey:withDescriptorCache:]_block_invoke.165
- __80-[ATXAnchorModelDataStoreWrapper insertAnchorOccurrence:anchor:featureMetadata:]_block_invoke.264
- __80-[ATXAnchorModelDataStoreWrapper insertAnchorOccurrence:anchor:featureMetadata:]_block_invoke.264.cold.1
- __80-[ATXBlendingLayerSessionLogger clientModelCacheUpdatesFromBlendingCacheUpdate:]_block_invoke.47
- __80-[ATXComplicationSuggestionGenerator _recentsComplications_unusedComplications:]_block_invoke.21
- __80-[ATXDynamicBreakthroughFeaturesCorrelator currentLocationSemanticForGivenDate:]_block_invoke.16
- __80-[ATXFaceSuggestionServer synchronousDateOfLastGalleryAppearanceWithCompletion:]_block_invoke.93
- __80-[ATXModeFaceComplicationHeuristicDataSource _hasSignificantHomeAccessoryEvents]_block_invoke.117
- __80-[ATXModeTransitionMetricsLogUploader uploadLogsToCoreAnalyticsWithXPCActivity:]_block_invoke.21
- __80-[ATXSuggestedPagesStackHeuristicsDataSource _hasSignificantHomeAccessoryEvents]_block_invoke.153
- __81-[ATXAnchorModelEventFeaturizer numEventsForEventIds:dateBuckets:biomePublisher:]_block_invoke.38
- __81-[ATXAppInterruptionsEventProvider successfullyCalculatedAppSessionInterruptions]_block_invoke.16
- __81-[ATXAppInterruptionsEventProvider successfullyCalculatedAppSessionInterruptions]_block_invoke.18
- __81-[ATXHomeScreenWidgetFeedbackProcessor updateHistogramsForRecentHomeScreenEvents]_block_invoke.21
- __81-[ATXHomeScreenWidgetFeedbackProcessor updateHistogramsForRecentHomeScreenEvents]_block_invoke.21.cold.1
- __81-[ATXNotificationSmartPauseManager currentSuggestionsGivenCandiateNotifications:]_block_invoke.25
- __81-[ATXNotificationSmartPauseManager currentSuggestionsGivenCandiateNotifications:]_block_invoke.27
- __81-[ATXSmartActivationEarlyExitDetectionLogger _registerForModeChangeNotifications]_block_invoke.13
- __81-[_ATXDataStore(IntentCache) writeValidParameterCombinationsWithSchema:cacheKey:]_block_invoke.17
- __81-[_ATXDataStore(IntentCache) writeValidParameterCombinationsWithSchema:cacheKey:]_block_invoke.17.cold.1
- __82-[ATXAnchorModelDataStoreWrapper minSlotResolutionParametersFromALogId:paramHash:]_block_invoke.423
- __82-[ATXAnchorModelDataStoreWrapper minSlotResolutionParametersFromALogId:paramHash:]_block_invoke.423.cold.1
- __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.108
- __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.108.cold.1
- __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.131
- __82-[ATXAnchorModelDataStoreWrapper updateOrInsertAnchorModelTrainingResults:anchor:]_block_invoke.131.cold.1
- __82-[ATXInformationEngine clearSuggestionsForInfoSourceIdentifier:completionHandler:]_block_invoke.81
- __82-[ATXIntentMetadataCacheInvalidationMonitor _listenForAppRegistrationAndUninstall]_block_invoke.11
- __82-[ATXNotificationCategorizationServer rankUserNotificationWithRequest:completion:]_block_invoke.83
- __82-[ATXNotificationCategorizationServer rankUserNotificationWithRequest:completion:]_block_invoke.83.cold.1
- __82-[ATXNotificationResolutionAccumulator cacheAppLaunchDataFromStartTime:toEndTime:]_block_invoke.49
- __82-[ATXNotificationResolutionAccumulator cacheAppLaunchDataFromStartTime:toEndTime:]_block_invoke.52
- __82-[ATXSuggestedPagesAppAggregator _sortedApps:sortedFirstPageApps:appLaunchCounts:]_block_invoke.39
- __82-[ATXUserEducationSuggestionFocusModeSetupTrigger modeHasPassedPastInferenceTest:]_block_invoke.20
- __83-[ATXBiomeProactiveSuggestionUIFeedbackResultStreamWriter writeForConsumerSubType:]_block_invoke.31
- __83-[ATXCandidateRelevanceModelDataStore trainingResultsForClientModelName:modelUUID:]_block_invoke.334
- __84-[ATXAnchorModelEventFeaturizer historyForAppLaunchDuetEvents:anchorOccurrenceDate:]_block_invoke.28
- __84-[ATXInformationEngine insertSuggestions:forInfoSourceIdentifier:completionHandler:]_block_invoke.68
- __84-[ATXMissedNotificationRankingFeedbackProcessingPipeline logMetricsWithXPCActivity:]_block_invoke.15
- __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.320
- __84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.320.cold.1
- __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.140
- __84-[ATXNotificationAndSuggestionDatabase updateNotificationUIForNotifications:nextUI:]_block_invoke.140.cold.1
- __84-[ATXProactiveSuggestionClientModelEvaluator uiPublisherWithDeduplicatedEngagements]_block_invoke.187
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.199
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.204
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.214
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke.224
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_2.203
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_2.205
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_2.218
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_3.213
- __84-[_ATXDataStore enumerateStateForApps:withGlobalBlock:thenWithPerAppBlock:readOnly:]_block_invoke_3.220
- __85-[ATXActionTimeEstimateAWDTracker getTimeEstimatesFor:forAppLaunches:withActionType:]_block_invoke.46
- __85-[ATXAppNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.16
- __85-[ATXAppNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.18
- __85-[ATXCandidateRelevanceModelDataStore deleteTrainedModelsWithTrainDateOlderThanDate:]_block_invoke.370
- __85-[ATXCandidateRelevanceModelDataStore deleteTrainedModelsWithTrainDateOlderThanDate:]_block_invoke_2.371
- __85-[ATXCandidateRelevanceModelDataStore deleteTrainedModelsWithTrainDateOlderThanDate:]_block_invoke_3.375
- __85-[ATXInformationEngine resetSuggestionsTo:forInfoSourceIdentifier:completionHandler:]_block_invoke.79
- __86-[ATXInterruptingNotificationsAccumulator successfullyAccumulatedInterruptingSessions]_block_invoke.10
- __86-[ATXInterruptingNotificationsAccumulator successfullyAccumulatedInterruptingSessions]_block_invoke.12
- __86-[ATXNotificationModeModel scoredEntitiesWithScoredAppEntities:scoredContactEntities:]_block_invoke.16
- __88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.234
- __88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.234.cold.1
- __88-[ATXAppDirectoryOrderingProvider _updateScreenTimeMappingsForAppBundleIds:withRetries:]_block_invoke.235
- __88-[ATXInformationFilter recordDismissOfSuggestion:isDismissalLongTerm:completionHandler:]_block_invoke.35
- __88-[ATXModeSetupPredictionMetricsLogger fetchAllRelevantModeSemanticTypesInLastSevenDays:]_block_invoke.50
- __88-[ATXModeSetupPredictionMetricsLogger globalAppSessionInterruptionsCalculatorSinceDate:]_block_invoke.17
- __88-[ATXModeSetupPredictionMetricsLogger globalAppSessionInterruptionsCalculatorSinceDate:]_block_invoke.19
- __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke.280
- __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.281
- __88-[ATXNotificationAndSuggestionDatabase _countNotificationsPerAppWithFilters:stmtBinder:]_block_invoke_2.281.cold.1
- __88-[ATXProactiveSuggestionPartialIntentHandlingPublisher partialIntentUIFeedbackPublisher]_block_invoke.16
- __89-[ATXActionCacheReader enumerateActionsAndPredictionItemsForConsumerSubtype:limit:block:]_block_invoke.23
- __89-[ATXAnchorModelDataStoreWrapper timestampOfMostRecentRecordedAnchorOccurrenceForAnchor:]_block_invoke.32
- __89-[ATXAnchorModelDataStoreWrapper timestampOfMostRecentRecordedAnchorOccurrenceForAnchor:]_block_invoke.35
- __89-[ATXAnchorModelDataStoreWrapper timestampOfMostRecentRecordedAnchorOccurrenceForAnchor:]_block_invoke.35.cold.1
- __89-[ATXBlendingBiomeStreamLogger logLayoutSelectedMetricWithBlendingModelCacheUpdateEvent:]_block_invoke.61
- __89-[ATXContactNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.14
- __89-[ATXContactNotificationEngagementEventProvider successfullyCalculatedNotificationEvents]_block_invoke.16
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.369
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.378
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.385
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.379
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.379.cold.1
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.387
- __89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.387.cold.1
- __89-[_ATXRecentInstallCache initTrackingAppsMoreRecentThan:installMonitor:uninstallMonitor:]_block_invoke.27
- __90-[ATXModeConfigurationUIFlowMetricLogger logModeConfigurationUIFlowMetricWithXPCActivity:]_block_invoke.22
- __91-[ATXCandidateRelevanceModelDataStore featurizationManagerIdForFeaturizationManager:error:]_block_invoke.224
- __91-[ATXCandidateRelevanceModelDataStore featurizationManagerIdForFeaturizationManager:error:]_block_invoke_2.225
- __91-[ATXModeFaceComplicationsAggregator provideComplicationsForSuggestedFaceType:environment:]_block_invoke.22
- __91-[ATXModeFaceComplicationsAggregator provideComplicationsForSuggestedFaceType:environment:]_block_invoke.22.cold.1
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.346
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.352
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.354
- __91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.354.cold.1
- __91-[ATXUnifiedComputedAndInferredModeStream computeUnifiedModeEventsFromStartTime:toEndTime:]_block_invoke.34
- __91-[ATXUnifiedComputedAndInferredModeStream computeUnifiedModeEventsFromStartTime:toEndTime:]_block_invoke.38
- __92-[ATXSpotlightLayoutSelector _validAutoShortcutContextualActionsForBundleId:limit:provider:]_block_invoke.236
- __92-[ATXSuggestionPreprocessor suggestionsByPreprocessingRankedSuggestions:forConsumerSubType:]_block_invoke.46
- __92-[ATXSuggestionPreprocessor suggestionsByPreprocessingRankedSuggestions:forConsumerSubType:]_block_invoke.53
- __92-[ATXSuggestionPreprocessor suggestionsByPreprocessingRankedSuggestions:forConsumerSubType:]_block_invoke.53.cold.1
- __93-[ATXAppSessionInterruptionsProvider cacheGlobalAppSessionInterruptionsCalculatorIfNecessary]_block_invoke.14
- __93-[ATXAppSessionInterruptionsProvider cacheGlobalAppSessionInterruptionsCalculatorIfNecessary]_block_invoke.16
- __93-[ATXCandidateRelevanceModelDatasetGenerator receiveCandidateDataPoint:completion:candidate:]_block_invoke.145
- __93-[ATXModeFaceComplicationAppDataSource provideComplicationsForSuggestedFaceType:environment:]_block_invoke.17
- __93-[ATXPredictionContextBuilder updateContextStreamAndReturnPredictionContextForCurrentContext]_block_invoke.78
- __93-[ATXProactiveSuggestionShadowLogger enumerateShadowLoggingResultsWithBlock:completionBlock:]_block_invoke.14
- __95+[ATXCandidateRelevanceModelDatasetGeneratorConfigApp candidatePublisherWithStartTime:endTime:]_block_invoke.62
- __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.57
- __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.60
- __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.64
- __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.69
- __95-[ATXCandidateRelevanceModelTrainer trainWithXPCActivity:disregardDatasetMetadataRequirements:]_block_invoke.72
- __95-[_ATXDataStore numActionParameterHashOccurrencesForActionKey:parameterHash:startDate:endDate:]_block_invoke.639
- __96+[ATXAppPredictorFeedback checkFeedbackContainsUninstalledApps:consumerSubType:aggregateLogger:]_block_invoke.18
- __96-[ATXModeFaceComplicationWidgetDataSource provideComplicationsForSuggestedFaceType:environment:]_block_invoke.17
- __96-[ATXModeSetupPredictionMetricsLogger getRecommendedAndCandidateAppsInDenyListForSemanticTypes:]_block_invoke.39
- __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.433
- __96-[ATXNotificationAndSuggestionDatabase telemetryDataForNotificationsFromTimestamp:endTimestamp:]_block_invoke.433.cold.1
- __96-[ATXNotificationManagementInspector fetchNotificationsFromBiomeFromStartDate:endDate:outError:]_block_invoke.86
- __97-[ATXModeSetupPredictionMetricsLogger getRecommendedAndCandidateAppsInAllowListForSemanticTypes:]_block_invoke.33
- __97-[ATXModeSetupPredictionMetricsLogger getRecommendedAndCandidateAppsInAllowListForSemanticTypes:]_block_invoke.37
- __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke.261
- __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.262
- __97-[ATXNotificationAndSuggestionDatabase allNotificationsBetweenStartTimestamp:endTimestamp:limit:]_block_invoke_2.262.cold.1
- __97-[_ATXFeedback feedbackLaunchedWithConsumerType:forBundleId:rejected:explicitlyRejected:context:]_block_invoke.70
- __98-[ATXDigestOnboardingSuggestionMetricsLogger logDigestOnboardingSuggestionMetricsWithXPCActivity:]_block_invoke.20
- __98-[ATXLinkActionPreprocessor updatedLinkActionSuggestion:actionContainer:basedOnReversedPublisher:]_block_invoke.10
- __99-[ATXNotificationAndSuggestionDatabase prepAndRunQuery:batchSize:XPCActivity:onPrep:onRow:onError:]_block_invoke.360
- __Block_byref_object_copy_.143
- __Block_byref_object_dispose_.144
- __OBJC_$_CLASS_METHODS_ATXBlendedLocalAndGlobalScores
- __OBJC_$_CLASS_METHODS_ATXDirichletDistribution
- __OBJC_$_INSTANCE_METHODS_ATXDirichletDistribution
- __OBJC_$_INSTANCE_VARIABLES_ATXDirichletDistribution
- __OBJC_CLASS_RO_$_ATXBlendedLocalAndGlobalScores
- __OBJC_CLASS_RO_$_ATXDirichletDistribution
- __OBJC_METACLASS_RO_$_ATXBlendedLocalAndGlobalScores
- __OBJC_METACLASS_RO_$_ATXDirichletDistribution
- __ZGVZ30ATXSampleFromGammaDistributionE3rng
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPK17ATXPredictionItemS6_PS4_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS5_EENS1_INS_4pairIU8__strongKS4_S8_EEEEEEEENS_16reverse_iteratorIPSF_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEEENS_16reverse_iteratorIPS9_EEEclB8ne180100Ev
- __ZNKSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE20__throw_out_of_rangeB8ne180100Ev
- __ZNKSt3__16vectorIDv8_fN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIDv8_iN12_GLOBAL__N_120SimdAlignedAllocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEENSA_ISF_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_out_of_rangeB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_out_of_rangeB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HDGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne180100EPS8_
- __ZNSt3__110unique_ptrIN9proactive3pas18SynchronizedObjectIN12_GLOBAL__N_113HTGuardedDataENS2_6detail14RecursiveMutexEEENS_14default_deleteIS8_EEE5resetB8ne180100EPS8_
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEERNSA_ISF_EEE5clearB8ne180100Ev
- __ZNSt3__114__split_bufferINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEERNS_9allocatorIS8_EEE5clearB8ne180100Ev
- __ZNSt3__115allocate_sharedB8ne180100I27ATXGamePlayKitCDecisionNodeNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8ne180100I27ATXGamePlayKitCDecisionTreeNS_9allocatorIS1_EEJEvEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__116__insertion_sortB8ne180100INS_17_ClassicAlgPolicyERZ119-[_ATXAppPredictor _getPredictionForItems:clipBundleIdsToRank:consumerSubType:intent:scoreLogger:context:featureCache:]E3$_0NS_11__wrap_iterIP17ATXPredictionItemEEEEvT1_S8_T0_
- __ZNSt3__116__rotate_forwardB8ne180100INS_17_ClassicAlgPolicyENS_11__wrap_iterIP17ATXPredictionItemEEEET0_S6_S6_S6_
- __ZNSt3__118gamma_distributionIdEclINS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEEEdRT_RKNS1_10param_typeE
- __ZNSt3__118generate_canonicalB8ne180100IdLm53ENS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEEET_RT1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI17ATXPredictionItemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS5_EENS1_INS_4pairIU8__strongKS4_S8_EEEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSJ_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__120__shared_ptr_emplaceI27ATXGamePlayKitCDecisionTreeNS_9allocatorIS1_EEEC2B8ne180100IJES3_Li0EEES3_DpOT_
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__120get_temporary_bufferB8ne180100I17ATXPredictionItemEENS_4pairIPT_lEEl
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEP17ATXPredictionItemS8_NS_11__wrap_iterIS8_EELi0EEENS_4pairIT0_T2_EESC_T1_SD_
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPNS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessISA_EENS_9allocatorINS_4pairIU8__strongKS9_SD_EEEEEESM_SM_Li0EEENSH_IT0_T2_EESN_T1_SO_
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEPNS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEESF_SF_Li0EEENS7_IT0_T2_EESG_T1_SH_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString17ATXPredictionItemEEPvEEEEEclB8ne180100EPSA_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringPK17ATXPredictionItemEEPvEEEEEclB8ne180100EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP9ATXActioniEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS6_EENS2_INS_4pairIU8__strongKS5_S9_EEEEEEEENS_16reverse_iteratorIPSG_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEEENS_16reverse_iteratorIPSA_EEEEED2B8ne180100Ev
- __ZNSt3__13mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS3_EENS_9allocatorINS_4pairIU8__strongKS2_S6_EEEEE6insertB8ne180100INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIS3_S6_EEPNS_11__tree_nodeISJ_PvEElEEEEEEvT_SQ_
- __ZNSt3__13mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS3_EENS_9allocatorINS_4pairIU8__strongKS2_S6_EEEEEC2B8ne180100ERKSE_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS5_EENS1_INS_4pairIU8__strongKS4_S8_EEEEEEEENS_16reverse_iteratorIPSF_EESJ_SJ_EET2_RT_T0_T1_SK_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEEENS_16reverse_iteratorIPS9_EESD_SD_EET2_RT_T0_T1_SE_
- __ZNSt3__14pairIRU8__strongP11objc_objectRU8__strongP14NSMutableArrayEaSB8ne180100IU8__strongKS2_S7_LPv0EEERS9_RKNS0_IT_T0_EE
- __ZNSt3__14pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEaSB8ne180100EOS7_
- __ZNSt3__16__treeINS_12__value_typeIU8__strongP11objc_objectU8__strongP14NSMutableArrayEENS_19__map_value_compareIS4_S8_NS_4lessIS4_EELb1EEENS_9allocatorIS8_EEE18_DetachedTreeCacheD2B8ne180100Ev
- __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI17ATXPredictionItemNS_9allocatorIS1_EEEC2Em
- __ZNSt3__16vectorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEENSA_ISF_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_3mapIU8__strongP11objc_objectU8__strongP14NSMutableArrayNS_4lessIS4_EENS_9allocatorINS_4pairIU8__strongKS3_S7_EEEEEENSA_ISF_EEE26__swap_out_circular_bufferERNS_14__split_bufferISF_RSG_EE
- __ZNSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS8_RSA_EE
- __ZNSt3__16vectorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEENS_9allocatorIS8_EEE9push_backB8ne180100EOS8_
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2Em
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne180100IRNS_11__wrap_iterIP17ATXPredictionItemEES7_EEvOT_OT0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8ne180100IRNS_11__wrap_iterIP17ATXPredictionItemEES8_EEvOT_OT0_
- __ZNSt3__19__shuffleB8ne180100INS_17_ClassicAlgPolicyENS_11__wrap_iterIP17ATXPredictionItemEES5_NS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEEET0_S8_T1_OT2_
- __ZNSt3__19allocatorI27ATXGamePlayKitCDecisionTreeE7destroyB8ne180100EPS1_
- __ZNSt3__19allocatorINS_4pairIU8__strongP11objc_objectNS_10shared_ptrI27ATXGamePlayKitCDecisionNodeEEEEE7destroyB8ne180100EPS8_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZZ30ATXSampleFromGammaDistributionE3rng
- __ZZ30ATXSampleFromGammaDistributionE4lock
- ___103-[ATXGlobalAppScorePredictor globalPopularitiesAtTimeOfDay:atDayOfWeek:atLocation:withLastAppLaunched:]_block_invoke
- ___110-[ATXDirichletDistribution getBlendedLocalAndGlobalScoresWithLocalCounts:andGlobalScores:withSamplingEnabled:]_block_invoke
- ___110-[ATXDirichletDistribution sampleProbabilitiesFromDirichletWithNormalizedParameters:andNormalizationConstant:]_block_invoke
- ___42+[ATXDirichletDistribution sharedInstance]_block_invoke
- ___59-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke
- ___ATXInitializeInOwnerProcess_block_invoke.378
- ___ATXInitializeInOwnerProcess_block_invoke.388
- ___ATXInitializeInOwnerProcess_block_invoke.413
- ___ATXInitializeInOwnerProcess_block_invoke.423
- ___ATXInitializeInOwnerProcess_block_invoke_2.383
- ___ATXInitializeInOwnerProcess_block_invoke_2.395
- ___ATXInitializeInOwnerProcess_block_invoke_2.395.cold.1
- ___ATXInitializeInOwnerProcess_block_invoke_2.419
- ___ATXInitializeInOwnerProcess_block_invoke_2.419.cold.1
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSNumber"16^B24l
- ___block_descriptor_48_e8_32s_e35_v32?0"NSString"8"NSNumber"16^B24l
- ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSNumber"16^B24l
- ___cxa_guard_acquire
- ___cxa_guard_release
- __block_literal_global.1001
- __block_literal_global.1018
- __block_literal_global.1037
- __block_literal_global.1047
- __block_literal_global.1055
- __block_literal_global.11
- __block_literal_global.115
- __block_literal_global.1170
- __block_literal_global.1178
- __block_literal_global.118
- __block_literal_global.120
- __block_literal_global.123
- __block_literal_global.132
- __block_literal_global.137
- __block_literal_global.142
- __block_literal_global.145
- __block_literal_global.146
- __block_literal_global.147
- __block_literal_global.150
- __block_literal_global.16
- __block_literal_global.168
- __block_literal_global.170
- __block_literal_global.171
- __block_literal_global.178
- __block_literal_global.183
- __block_literal_global.186
- __block_literal_global.193
- __block_literal_global.194
- __block_literal_global.202
- __block_literal_global.207
- __block_literal_global.210
- __block_literal_global.211
- __block_literal_global.212
- __block_literal_global.217
- __block_literal_global.219
- __block_literal_global.225
- __block_literal_global.234
- __block_literal_global.239
- __block_literal_global.243
- __block_literal_global.250
- __block_literal_global.266
- __block_literal_global.267
- __block_literal_global.273
- __block_literal_global.280
- __block_literal_global.288
- __block_literal_global.293
- __block_literal_global.295
- __block_literal_global.304
- __block_literal_global.311
- __block_literal_global.324
- __block_literal_global.326
- __block_literal_global.332
- __block_literal_global.337
- __block_literal_global.339
- __block_literal_global.341
- __block_literal_global.356
- __block_literal_global.363
- __block_literal_global.371
- __block_literal_global.374
- __block_literal_global.378
- __block_literal_global.380
- __block_literal_global.381
- __block_literal_global.385
- __block_literal_global.388
- __block_literal_global.390
- __block_literal_global.395
- __block_literal_global.399
- __block_literal_global.415
- __block_literal_global.425
- __block_literal_global.429
- __block_literal_global.432
- __block_literal_global.440
- __block_literal_global.443
- __block_literal_global.447
- __block_literal_global.452
- __block_literal_global.459
- __block_literal_global.462
- __block_literal_global.467
- __block_literal_global.471
- __block_literal_global.475
- __block_literal_global.479
- __block_literal_global.482
- __block_literal_global.486
- __block_literal_global.503
- __block_literal_global.507
- __block_literal_global.508
- __block_literal_global.518
- __block_literal_global.520
- __block_literal_global.523
- __block_literal_global.528
- __block_literal_global.531
- __block_literal_global.545
- __block_literal_global.548
- __block_literal_global.555
- __block_literal_global.556
- __block_literal_global.560
- __block_literal_global.563
- __block_literal_global.573
- __block_literal_global.588
- __block_literal_global.592
- __block_literal_global.595
- __block_literal_global.6
- __block_literal_global.606
- __block_literal_global.609
- __block_literal_global.622
- __block_literal_global.626
- __block_literal_global.629
- __block_literal_global.67
- __block_literal_global.681
- __block_literal_global.693
- __block_literal_global.70
- __block_literal_global.75
- __block_literal_global.761
- __block_literal_global.766
- __block_literal_global.771
- __block_literal_global.792
- __block_literal_global.8
- __block_literal_global.830
- __block_literal_global.87
- __block_literal_global.870
- __block_literal_global.875
- __block_literal_global.9
- __block_literal_global.907
- __block_literal_global.909
- __block_literal_global.917
- __block_literal_global.924
- __block_literal_global.933
- __block_literal_global.96
- __block_literal_global.964
- __registerForDailyRoutinesCTSJob_block_invoke.450
- __registerForEverydayShortcutsTriggersCTSJobs_block_invoke.445
- __registerForNotificationAndSuggestionDatastorePruning_block_invoke.604
- __swift_FORCE_LOAD_$_swiftFileProvider
- __swift_FORCE_LOAD_$_swiftFileProvider_$_AppPredictionInternal
- _fmodf
- _kDayOfWeek
- _kDayOfWeek_sampled
- _kLOIType
- _kLOIType_sampled
- _kLastApp
- _kLastApp_sampled
- _kTimeOfDay
- _kTimeOfDay_sampled
- _objc_msgSend$appPredictionBlendedScoreNormalizationConstant
- _objc_msgSend$appPredictionGlobalScoreMultiplierPerApp
- _objc_msgSend$blendedGlobalAndLocalScoresForGlobalScores:LOITypeLaunches:lastAppLaunches:timeOfDayLaunches:dayOfWeekLaunches:forApps:
- _objc_msgSend$getBlendedLocalAndGlobalScoresWithLocalCounts:andGlobalScores:withSamplingEnabled:
- _objc_msgSend$getGammaDistributionShapeParameterForComputingGlobalAppScoresWithAlpha:andNormalizationConstant:
- _objc_msgSend$globalPopularitiesAtTimeOfDay:atDayOfWeek:atLocation:withLastAppLaunched:
- _objc_msgSend$globalPopularitiesForBundleIds:atTimeOfDayIndex:atDayOfWeekIndex:atLocationIndex:withLastAppLaunched:
- _objc_msgSend$globalPopularityForBundleIds:atDate:atLocation:withLastAppLaunched:
- _objc_msgSend$globalPopularityForBundleIdsGivenTimeDayLocationAndLastApp:context:
- _objc_msgSend$globalPopularityPredictor
- _objc_msgSend$sampleProbabilitiesFromDirichletWithNormalizedParameters:andNormalizationConstant:
- block_descriptor.25
- block_descriptor.32
- keyTrackerForRotationSessionStackEngagementStatus:._pasExprOnceResult.173
- keyTrackerForRotationSessionStackEngagementStatus:._pasExprOnceResult.174
- keyTrackerForStackEngagementStatus:._pasExprOnceResult.119
- keyTrackerForStackEngagementStatus:._pasExprOnceResult.120
- keyTrackerForStackEngagementStatus:._pasExprOnceResult.121
- keyTrackerForStackEngagementStatus:._pasExprOnceResult.122
- keyTrackerForStackEngagementStatus:._pasExprOnceResult.123
- keyTrackerForStackEngagementStatus:._pasExprOnceResult.124
- replacementContainerBundleIdForDonationBundleId:._pasOnceToken35
CStrings:
+ ":nextAppLaunchTimestamp"
+ "ALTER TABLE notifications ADD COLUMN nextAppLaunchTimestamp REAL"
+ "ATXNotificationAndSuggestionDatastoreAppLaunchTimestamp"
+ "Category %@ isn't touched in more than %d days, current potential savings: %lu, total savings in this run: %lu"
+ "Category %@ was last touched: %d days ago"
+ "Error updating notification with app launch timestamp: %@"
+ "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :receivedMode, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isDeliveredInPrioritySection, :isSummarized, :isPartOfStack, :isStackSummary, 0, :numberOfNotificationsInStack, :notificationPriorityStatus, :notificationSummaryStatus, :isPriorityNotificationEnabled, :isNotificationSummaryEnabled, NULL)"
+ "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
+ "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled,     nextAppLaunchTimestamp FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
+ "SLS: ATXSpotlightLayoutSelector suggestion =[%lu] contextCode found: %ld for reasons %llu"
+ "SLS: Checking suggestion '%lu' for media intent. Intent of class%@"
+ "SLS: _collectionsWithSuggestions removing dupe `%lu` from contextCode %ld"
+ "SLS: _collectionsWithSuggestions suggestionDict[%@] = [%lu]"
+ "SLS: context=[%{sensitive}@] criteria[%{sensitive}@]"
+ "Slot Resolution Score Logging - Stage One Succeeded"
+ "T@\"NSDate\",&,N,V_nextAppLaunchTimestamp"
+ "UPDATE notifications SET nextAppLaunchTimestamp = :nextAppLaunchTimestamp WHERE bundleId = :bundleId AND receiveTimestamp > :startTimestamp AND receiveTimestamp < :nextAppLaunchTimestamp"
+ "[%@] Could not fetch app launch stream with error: %@"
+ "[Index] CSSearchableItem from suggestion %lu --> %@"
+ "[Index] No search item from suggestion %lu"
+ "_nextAppLaunchTimestamp"
+ "bundleIDCountForCategory:"
+ "carPlay"
+ "com.apple.EmojiPoster.EmojiPosterExtension:nature"
+ "com.apple.GradientPoster.GradientPosterExtension:plum.preset3"
+ "com.apple.MercuryPoster:fluidity"
+ "com.apple.NanoUniverse.AegirProxyApp.AegirPoster:Earth"
+ "com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster:black"
+ "com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster:blue"
+ "com.apple.WatchFacesWallpaperSupport.ExtragalacticPoster:unity"
+ "com.apple.WatchFacesWallpaperSupport.RhizomePoster:variant-1"
+ "com.apple.WatchFacesWallpaperSupport.RhizomePoster:variant-4"
+ "com.apple.WatchFacesWallpaperSupport.RhizomePoster:variant-5"
+ "com.apple.WatchFacesWallpaperSupport.Unity2025Poster"
+ "com.apple.WatchFacesWallpaperSupport.Unity2025Poster:unity/com.apple.PridePoster.PridePosterExtension:main"
+ "com.apple.duetexpertd.histogramSaver"
+ "com.apple.weather.poster:weather-poster-gallery"
+ "failed to get suggestions executable info from %@"
+ "nextAppLaunchTimestamp"
+ "purgeUnusedCategories"
+ "setNextAppLaunchTimestamp:"
+ "timeToNextAppLaunch"
+ "unity"
+ "updateNotificationWithAppLaunchTimestamp:bundleId:startTimestamp:"
+ "updateNotificationsWithNextAppLaunchTimestamp:bundleId:startTimestamp:"
- "-[ATXFaceSuggestionAssetParameters unitySectionDescriptors]_block_invoke"
- "@36@0:8i16i20i24@28"
- "@44@0:8@16i24i28i32@36"
- "@48@0:8@16@24q32@40"
- "ATXBlendedLocalAndGlobalScores"
- "ATXDirichletDistribution"
- "ATXGammaDistribution.mm"
- "ATXGlobalAppScorePredictor.m"
- "ATXGlobalAppSignals"
- "ATXGlobalAppSignalsUtil: Error initializing %@ model: %@"
- "ATXGlobalAppSignalsUtil: Missing model name"
- "ATXGlobalSignals - Error during inference on the CoreMLModel: %@"
- "ATXGlobalSignals - Error initializing MLDictionaryFeatureProvider for inference on the CoreMLModel: %@"
- "ATXGlobalSignals: BundleId index %d exceeded the output layer size %lu"
- "ATXRSWidgetSuggestionProducer: no context derived from relevant intent: %@"
- "ATXRSWidgetSuggestionProducer: no relevantContext on CHSWidgetRelevance. Skipping."
- "Can't construct Array with count < 0"
- "DayOfWeek_sampled"
- "Division by zero"
- "Division results in an overflow"
- "INSERT OR IGNORE INTO notifications VALUES (:uuid, :receiveTimestamp, :deliveryMethod, :urgency, :bundleId, :threadId, :contactId, :isGroupMessage, :isMessage, :latestOutcome, :latestOutcomeTimestamp, :isProminent, :isActive, 0, :rawIdentifier, :receivedMode, NULL, NULL, :deliveryReason, :recordTimestamp, :notificationID, :notificationBodyLength, :notificationTitleLength, :notificationSubtitleLength, :summaryLength, :isDeliveredInPrioritySection, :isSummarized, :isPartOfStack, :isStackSummary, 0, :numberOfNotificationsInStack, :notificationPriorityStatus, :notificationSummaryStatus, :isPriorityNotificationEnabled, :isNotificationSummaryEnabled)"
- "Insufficient space allocated to copy string contents"
- "LOIType_sampled"
- "LastApp"
- "LastApp_sampled"
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled FROM notifications WHERE     bundleId = :bundleId AND     notificationId = :notificationId AND     recordTimestamp = :recordTimestamp ORDER BY recordTimestamp DESC LIMIT 1 "
- "SELECT     uuid,     receiveTimestamp,     deliveryMethod,     urgency,     bundleId,     isMessage,     latestOutcome,     latestOutcomeTimestamp,     numExpansions,     receivedMode,     firstUI,     mostRecentUI,     deliveryReason,     notificationBodyLength,     notificationTitleLength,     notificationSubtitleLength,     summaryLength,     isDeliveredInPrioritySection,     isSummarized,     isPartOfStack,     isStackSummary,     numberOfNotificationsInStack,     notificationPriorityStatus,     notificationSummaryStatus,     isPriorityNotificationEnabled,     isNotificationSummaryEnabled FROM notifications WHERE     receiveTimestamp > :startTimestamp AND     receiveTimestamp < :endTimestamp "
- "SLS: ATXSpotlightLayoutSelector suggestion =[%@] contextCode found: %ld for reasons %llu"
- "SLS: Checking suggestion '%@' for media intent. Intent of class%@"
- "SLS: _collectionsWithSuggestions removing dupe `%@` from contextCode %ld"
- "SLS: _collectionsWithSuggestions suggestionDict[%@] =[%@]"
- "SLS: context=[%@] criteria[%@]"
- "Slot  Resolution Score Logging - Stage One Succeeded"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "TimeOfDay"
- "TimeOfDay_sampled"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnitySectionDescriptors"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "[Index] CSSearchableItem from suggestion %@ --> %@"
- "[Index] No search item from suggestion %@"
- "blendedGlobalAndLocalScoresForGlobalScores:LOITypeLaunches:lastAppLaunches:timeOfDayLaunches:dayOfWeekLaunches:forApps:"
- "double ATXSampleFromGammaDistribution(double, double)"
- "getBlendedLocalAndGlobalScoresWithLocalCounts:andGlobalScores:withSamplingEnabled:"
- "getGammaDistributionShapeParameterForComputingGlobalAppScoresWithAlpha:andNormalizationConstant:"
- "globalPopularitiesAtTimeOfDay:atDayOfWeek:atLocation:withLastAppLaunched:"
- "globalPopularitiesForBundleIds:atTimeOfDayIndex:atDayOfWeekIndex:atLocationIndex:withLastAppLaunched:"
- "globalPopularityForBundleIds:atDate:atLocation:withLastAppLaunched:"
- "globalPopularityForBundleIdsGivenTimeDayLocationAndLastApp:context:"
- "globalPopularityPredictor"
- "invalid Collection: less than 'count' elements in collection"
- "kBlendedScoreNormalizationConstant"
- "kGlobalScoreMultiplier"
- "output"
- "sampleProbabilitiesFromDirichletWithNormalizedParameters:andNormalizationConstant:"
- "scale > 0"
- "shape > 0"

```
