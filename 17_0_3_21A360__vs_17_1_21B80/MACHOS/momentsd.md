## momentsd

> `/usr/libexec/momentsd`

```diff

-117.0.13.0.0
-  __TEXT.__text: 0x188874
-  __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_stubs: 0x15000
-  __TEXT.__objc_methlist: 0xb08c
-  __TEXT.__objc_classname: 0x1540
-  __TEXT.__objc_methname: 0x20df7
-  __TEXT.__objc_methtype: 0x2584
-  __TEXT.__cstring: 0x1c244
-  __TEXT.__oslogstring: 0x19e14
+125.0.13.0.0
+  __TEXT.__text: 0x18ee10
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0x15d00
+  __TEXT.__objc_methlist: 0xb51c
+  __TEXT.__objc_classname: 0x156b
+  __TEXT.__objc_methname: 0x221f9
+  __TEXT.__objc_methtype: 0x2653
+  __TEXT.__cstring: 0x1bf64
+  __TEXT.__oslogstring: 0x1c06c
   __TEXT.__const: 0x842
-  __TEXT.__gcc_except_tab: 0x49d4
-  __TEXT.__ustring: 0xa
+  __TEXT.__gcc_except_tab: 0x4b54
+  __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0xa9
   __TEXT.__constg_swiftt: 0x118
   __TEXT.__swift5_typeref: 0x10d

   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_reflstr: 0x30
-  __TEXT.__unwind_info: 0x361c
+  __TEXT.__unwind_info: 0x37c0
   __TEXT.__eh_frame: 0x270
-  __DATA_CONST.__auth_got: 0x8a0
+  __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x2c0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x6cb8
-  __DATA_CONST.__cfstring: 0x1b9e0
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__const: 0x7218
+  __DATA_CONST.__cfstring: 0x1bc60
+  __DATA_CONST.__objc_classlist: 0x5b0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x2940
-  __DATA_CONST.__objc_floatobj: 0x180
-  __DATA_CONST.__objc_arraydata: 0xb98
-  __DATA_CONST.__objc_arrayobj: 0x420
+  __DATA_CONST.__objc_intobj: 0x2988
+  __DATA_CONST.__objc_floatobj: 0x1c0
+  __DATA_CONST.__objc_arraydata: 0xb70
+  __DATA_CONST.__objc_arrayobj: 0x438
   __DATA_CONST.__objc_doubleobj: 0x2e0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA.__objc_const: 0x14bb8
-  __DATA.__objc_selrefs: 0x6288
+  __DATA.__objc_const: 0x15100
+  __DATA.__objc_selrefs: 0x65a8
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x970
-  __DATA.__objc_superrefs: 0x4a0
-  __DATA.__objc_ivar: 0xeac
-  __DATA.__objc_data: 0x39c0
-  __DATA.__data: 0x1168
+  __DATA.__objc_classrefs: 0x9b0
+  __DATA.__objc_superrefs: 0x4b0
+  __DATA.__objc_ivar: 0xf00
+  __DATA.__objc_data: 0x3a60
+  __DATA.__data: 0x1198
   __DATA.__bss: 0x150
-  __DATA.__common: 0xa0
+  __DATA.__common: 0xa8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/Frameworks/WeatherKit.framework/WeatherKit
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams

   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3EA98BC3-BBAB-39B0-AD1B-B6E1956329A8
-  Functions: 5736
-  Symbols:   40976
-  CStrings:  14539
+  UUID: 7CC195FB-A5CA-3CEE-B089-6C663C7BA6CB
+  Functions: 5935
+  Symbols:   42296
+  CStrings:  14850
 
Symbols:
+ +[MOContextAnnotationUtilities addPhotoResourcesWithDateArray:universe:handler:]
+ +[MOContextAnnotationUtilities addPhotoResourcesWithDateArray:universe:handler:].cold.1
+ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:]
+ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:].cold.1
+ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:].cold.2
+ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:].cold.3
+ +[MOEventBundleMetaDataUtility setMetaDataForTime:metaData:]
+ +[MOMediaPlayMetrics bucketedKeys]
+ +[MOMediaPlayMetrics event]
+ +[MOMediaPlayMetrics supportedMetricKeys]
+ +[MOMediaPlaySession describeCategory:]
+ +[MOMediaPlaySession isFirstPartyApp:]
+ +[MOOnboardingAndSettingsPersistence _fetchSignificantLocationEnablementStatus]
+ +[MOSummarizationUtilities combineMediaResources:]
+ +[MOSummarizationUtilities combinePhotoResources:]
+ +[MOSummarizationUtilities combinePhotoResources:].cold.1
+ +[MOSummarizationUtilities createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:]
+ +[MOSummarizationUtilities createDominantBundleFromBundles:withParameters:timeZoneManager:]
+ +[MOSummarizationUtilities createMegaBundleFromBundles:parameters:timeZoneManager:]
+ +[MOSummarizationUtilities createOutingMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:]
+ +[MOSummarizationUtilities getPlacesFromBundles:forSummaryBundle:]
+ +[MOSummarizationUtilities getResourcesForOutingSummaryBundleWithWorkoutResources:photoResources:mediaResources:shouldUpLevelPhoto:]
+ +[MOSummarizationUtilities getResourcesForWeeklyWorkoutSummaryBundleWithWorkoutResources:photoResources:mediaResources:]
+ +[MOSummarizationUtilities getResourcesFromBundles:forSummaryBundle:]
+ +[MOSummarizationUtilities hasWorkoutRoute:]
+ +[MOSummarizationUtilities isBundle:insideTheSameDayAsOtherBundle:]
+ +[MOSummarizationUtilities isBundleWithAssets:]
+ +[MOSummarizationUtilities mergeOutingBundlesWithInDayWithGrouppedBundles:remainingSingletonBundles:parameters:isCoarseGranularity:timeZoneManager:]
+ +[MOSummarizationUtilities sortedBundleByPhotoAssetsCount:]
+ +[MOSummarizationUtilities sortedWorkoutBundleByDuration:]
+ +[MOSummarizationUtilities updateRankMetaDataFrom:forSummaryBundle:].cold.1
+ +[MOTime buildSimpleTimeTagIntervalsWithLeewayForDate:]
+ +[MOTime dateReferenceTagFromStartDate:endDate:nowDate:timeZone:]
+ +[MOTime dateReferenceTagFromStartDate:endDate:timeZone:]
+ +[MOTime dayOfWeekFromStartDate:endDate:timeZoneManager:]
+ +[MOTime dayOfWeekFromStartDate:endDate:timeZoneManager:].cold.1
+ +[MOTime dayOfWeekFromStartDate:endDate:timeZoneManager:].cold.2
+ +[MOTime dayOfWeekFromStartDate:endDate:timeZoneManager:].cold.3
+ +[MOTime localTimeOfDate:timeZone:]
+ +[MOTime timeForDate:]
+ +[MOTime timeForDate:timeZoneManager:]
+ +[MOTime timeFromStartDate:endDate:timeZoneManager:]
+ +[MOTime timeFromStartDate:endDate:timeZoneManager:].cold.1
+ +[MOVisitAnnotationManager scoreVisitBundleAssets:]
+ -[MOAggregationManager eventBundleRanking]
+ -[MOAggregationManager filterEventBundlesEligibleForSummarization:]
+ -[MOAggregationManager setEventBundleRanking:]
+ -[MOAnnotationManager timeZoneManager]
+ -[MOContactAggregationManager .cxx_destruct]
+ -[MOContactAggregationManager configurationManager]
+ -[MOContactAggregationManager initWithUniverse:]
+ -[MOContactAggregationManager setConfigurationManager:]
+ -[MOConversationAnnotationManager configurationManager]
+ -[MODefaultsManager initWithSuiteName:]
+ -[MODiagnosticReporter reportIncident:subtype:context:].cold.4
+ -[MODominantBundleCreationManager .cxx_destruct]
+ -[MODominantBundleCreationManager fUniverse]
+ -[MODominantBundleCreationManager initWithUniverse:]
+ -[MOEngagementHistoryManager didEngagementEventPosted:withBundles:timestamp:withContext:withTrialExperimentIDs:].cold.3
+ -[MOEvent setTimeZone:]
+ -[MOEvent timeZone]
+ -[MOEventBundle intersectedActivityOrVisitForObject:other:]
+ -[MOEventBundle intersectedSubBundleIDForObject:other:]
+ -[MOEventBundle isEqualBasicPropertiesForObject:other:]
+ -[MOEventBundle localEndDate]
+ -[MOEventBundle localStartDate]
+ -[MOEventBundleFetchOptions initWithAllowedCategories:dateInterval:ascending:limit:includeDeletedBundles:skipRanking:interfaceType:]
+ -[MOEventBundleFetchOptions initWithDateInterval:ascending:limit:includeDeletedBundles:skipRanking:interfaceType:]
+ -[MOEventBundleFetchOptions interfaceType]
+ -[MOEventBundleManager eventBundleRanking]
+ -[MOEventBundleManager setEventBundleRanking:]
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.1
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.2
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.3
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.4
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.5
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.6
+ -[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:].cold.1
+ -[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:].cold.2
+ -[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:].cold.3
+ -[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:].cold.4
+ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:].cold.2
+ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:].cold.3
+ -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:]
+ -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:].cold.1
+ -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:].cold.2
+ -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:].cold.3
+ -[MOEventBundleRanking safeSavePropertyToDictionary:withKey:andValue:]
+ -[MOEventBundleRanking safeSavePropertyToDictionary:withKey:andValue:].cold.1
+ -[MOEventBundleRankingInput placeNames]
+ -[MOEventBundleRankingInput setPlaceNames:]
+ -[MOEventBundleRankingInput setWorkoutTypes:]
+ -[MOEventBundleRankingInput workoutTypes]
+ -[MOEventBundleStore _submitRankingParamsAnalytics:withSubmissionDate:].cold.1
+ -[MOEventBundleStore _submitRankingParamsAnalytics:withSubmissionDate:].cold.2
+ -[MOEventBundleStore purgeDeletedEventBundlesWithCompletionHandler:]
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.1
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.10
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.11
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.12
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.13
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.14
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.2
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.3
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.4
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.5
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.6
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.7
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.8
+ -[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:].cold.9
+ -[MOEventMedia mediaFirstPartyTimePlayedRatio]
+ -[MOEventMedia setMediaFirstPartyTimePlayedRatio:]
+ -[MOEventRefreshScheduler notificationsManager]
+ -[MOEventRefreshScheduler setNotificationsManager:]
+ -[MOMediaPlayAnnotationManager _createBundlesFromEvents:]
+ -[MOMediaPlayMetrics firstPartyAppRatio]
+ -[MOMediaPlayMetrics firstPartyAppTime]
+ -[MOMediaPlayMetrics initWithFirstPartyAppRatio:firstPartyAppTime:musciAppTime:]
+ -[MOMediaPlayMetrics initWithLoggingEnabled:]
+ -[MOMediaPlayMetrics musicAppTime]
+ -[MOMediaPlayMetrics setFirstPartyAppRatio:]
+ -[MOMediaPlayMetrics setFirstPartyAppTime:]
+ -[MOMediaPlayMetrics setMusicAppTime:]
+ -[MOMediaPlayMetrics setValues]
+ -[MOMediaPlayMetrics submitMetricsWithError:]
+ -[MOMotionManager _rehydrateMotionActivity:forLocationSetting:handler:]
+ -[MOMotionManager _updateDeviceLocationsForMotionEvents:forLocationSetting:handler:]
+ -[MONotificationScheduleItem initScheduleWithHour:minute:weekdays:]
+ -[MONotificationsManager _getArrayScheduledDateComponents]
+ -[MONotificationsManager _getArrayScheduledDateComponents].cold.1
+ -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]
+ -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:].cold.1
+ -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:].cold.2
+ -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:].cold.3
+ -[MONotificationsManager _getNextNotificationDateComponentsWithOptions:afterDate:numWeeks:setComponents:]
+ -[MONotificationsManager _getNextScheduledCalendarNotificationTrigger]
+ -[MONotificationsManager _getSortedArrayScheduledDatesWithOptions:afterDate:numWeeks:setComponents:]
+ -[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]
+ -[MONotificationsManager _serviceSuggestionsNotificationsTestForBundle:usingTrigger:useAppSchedule:completionHandler:]
+ -[MONotificationsManager _sheetIsVisible]
+ -[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]
+ -[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]
+ -[MONotificationsManager setupPeriodicTimeToWriteMomentsNotificationsWithSchedule:options:handler:].cold.1
+ -[MONowPlayingMediaManager _fetchAppCateogryByBundleIds:]
+ -[MONowPlayingMediaManager _fetchAppCateogryByBundleIds:].cold.1
+ -[MONowPlayingMediaManager _filterMediaSessionsBasedOnFirstPartyApps:]
+ -[MONowPlayingMediaManager _filterMediaSessionsBasedOnMusicApps:]
+ -[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:startDate:handler:]
+ -[MONowPlayingMediaManager bundleIdCategoryMappings]
+ -[MONowPlayingMediaManager mediaBundleDeniedIdSet]
+ -[MONowPlayingMediaManager thirdPartyMediaBundleIdSet]
+ -[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]
+ -[MOOnboardingAndSettingsPersistence setOnboardingFlowCompletionStatus:].cold.2
+ -[MOPhotoManager _getPhotosByAssetProperties:UserLocations:MaxDistance:]
+ -[MOPromptMetrics getAndSetAgeGender].cold.1
+ -[MOPromptMetrics getAndSetAgeGender].cold.2
+ -[MORoutineServiceManager _setRehydratedGeoMapItemProperties:visit:].cold.1
+ -[MORoutineServiceManager fetchHomeLOI].cold.2
+ -[MOSharedWithYouManager fetchSharedContentBetweenStartDate:EndDate:CompletionHandler:].cold.1
+ -[MOSignificantContactManager _eligibleInteraction:]
+ -[MOSignificantContactManager _eligibleInteraction:].cold.1
+ -[MOSummarizationManager _dedupAssetForMediaBundle:nonPlayedMediaBudnles:isRecommendTab:]
+ -[MOSummarizationManager _removeDuplicateFromResource:nonMediaKeySet:mediaOnRepeatDict:eventBundleDayKey:keyName:]
+ -[MOSummarizationManager _sortResourcesByPriorityScore:]
+ -[MOSummarizationManager eventBundleRanking]
+ -[MOSummarizationManager removeDuplicateAssetsFromMediaBundle:]
+ -[MOSummarizationManager setEventBundleRanking:]
+ -[MOSummarizationParameters coarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold]
+ -[MOSummarizationParameters coarseGranularity_outingBundlesExclusionGoodnessScoreThreshold]
+ -[MOSummarizationParameters fineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold]
+ -[MOSummarizationParameters fineGranularity_outingBundlesExclusionGoodnessScoreThreshold]
+ -[MOSummarizationParameters mediaBundleFirstPartyPlayTimePercentageThreshold]
+ -[MOSummarizationParameters setCoarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold:]
+ -[MOSummarizationParameters setCoarseGranularity_outingBundlesExclusionGoodnessScoreThreshold:]
+ -[MOSummarizationParameters setFineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold:]
+ -[MOSummarizationParameters setFineGranularity_outingBundlesExclusionGoodnessScoreThreshold:]
+ -[MOSummarizationParameters setMediaBundleFirstPartyPlayTimePercentageThreshold:]
+ -[MOSummarizationParameters setWeeklyActivitySummary_suppressionGoodnessScoreThreshold:]
+ -[MOSummarizationParameters weeklyActivitySummary_suppressionGoodnessScoreThreshold]
+ -[MOTime date]
+ -[MOTime localTime]
+ -[MOTime timeZoneObject]
+ -[MOTimeContextAggregationManager _maximumGoodnessScoreDeltaFromBundle:toCluster:]
+ -[MOTimeZoneManager .cxx_destruct]
+ -[MOTimeZoneManager condensedRecordsFromRecords:]
+ -[MOTimeZoneManager condensedRecords]
+ -[MOTimeZoneManager description]
+ -[MOTimeZoneManager keywordForDate:]
+ -[MOTimeZoneManager processTimeZoneEvents:]
+ -[MOTimeZoneManager processTimeZoneEvents:].cold.1
+ -[MOTimeZoneManager processTimeZoneEvents:].cold.2
+ -[MOTimeZoneManager setCondensedRecords:]
+ -[MOTimeZoneManager setTimeZoneRecords:]
+ -[MOTimeZoneManager timeZoneAtDate:]
+ -[MOTimeZoneManager timeZoneRecords]
+ -[MOTrendsAnalyzer(Metrics) setCommonFields:].cold.1
+ -[MOTrendsAnalyzer(Metrics) setCommonFields:].cold.2
+ -[MOTripAnnotationManager _assignPriorityScoreForPlace:placeInfoArray:]
+ -[MOTripAnnotationManager _filterPlaceUsingPredicates:]
+ -[MOTripAnnotationManager _filterPlaceUsingPredicates:].cold.1
+ -[MOTripAnnotationManager _updateMOPlacePriorityScore:priorityScore:handler:]
+ -[MOTripAnnotationManager _updateMetaDataForRanking:forEvents:places:]
+ -[MOTripAnnotationManager _updateMetaDataForRanking:forEvents:places:].cold.1
+ -[MOTripAnnotationManager dominantPlaceNamesFromEvents:]
+ -[MOTripAnnotationManager dominantPlaceNamesFromEvents:countryMode:]
+ -[MOTripAnnotationManager hometownReferenceLocations].cold.1
+ -[MOTripAnnotationManager minimumDwellTime]
+ -[MOTripAnnotationManager resourcesFromEvents:handler:]
+ -[MOTripAnnotationManager setMinimumDwellTime:]
+ -[MOTripParameters maximumFamiliarityIndex]
+ -[MOTripParameters setMaximumFamiliarityIndex:]
+ -[MOWatchDog _pet].cold.1
+ -[MOWorkoutAnnotationManager removeDuplicateWorkouts:]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MOMediaPlayMetrics.o
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MOTimeZoneManager.o
+ GCC_except_table106
+ GCC_except_table117
+ GCC_except_table140
+ GCC_except_table148
+ GCC_except_table27
+ GCC_except_table33
+ GCC_except_table46
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table72
+ GCC_except_table79
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table90
+ GCC_except_table94
+ MOMediaPlayMetrics.m
+ MOTimeZoneManager.m
+ OBJC_IVAR_$_MOAggregationManager._eventBundleRanking
+ OBJC_IVAR_$_MOAnnotationManager._timeZoneManager
+ OBJC_IVAR_$_MOContactAggregationManager._configurationManager
+ OBJC_IVAR_$_MOConversationAnnotationManager._configurationManager
+ OBJC_IVAR_$_MODiagnosticReporter._isOnboardedOnJournalStudy
+ OBJC_IVAR_$_MODominantBundleCreationManager._fUniverse
+ OBJC_IVAR_$_MOEvent._timeZone
+ OBJC_IVAR_$_MOEventBundleFetchOptions._interfaceType
+ OBJC_IVAR_$_MOEventBundleManager._eventBundleRanking
+ OBJC_IVAR_$_MOEventBundleRankingInput._placeNames
+ OBJC_IVAR_$_MOEventBundleRankingInput._workoutTypes
+ OBJC_IVAR_$_MOEventMedia._mediaFirstPartyTimePlayedRatio
+ OBJC_IVAR_$_MOEventRefreshScheduler._notificationsManager
+ OBJC_IVAR_$_MOMediaPlayMetrics._firstPartyAppRatio
+ OBJC_IVAR_$_MOMediaPlayMetrics._firstPartyAppTime
+ OBJC_IVAR_$_MOMediaPlayMetrics._musicAppTime
+ OBJC_IVAR_$_MONowPlayingMediaManager._bundleIdCategoryMappings
+ OBJC_IVAR_$_MONowPlayingMediaManager._mediaBundleDeniedIdSet
+ OBJC_IVAR_$_MONowPlayingMediaManager._thirdPartyMediaBundleIdSet
+ OBJC_IVAR_$_MOOnboardingAndSettingsPersistence._settingsChangeCount
+ OBJC_IVAR_$_MOOnboardingAndSettingsPersistence._settingsChangeTransaction
+ OBJC_IVAR_$_MOOnboardingAndSettingsPersistence._settingsChangeTransactionHoldCount
+ OBJC_IVAR_$_MOSignificantContactManager._callLikeMechanismsSet
+ OBJC_IVAR_$_MOSignificantContactManager._tollFreeNumberPrefixes
+ OBJC_IVAR_$_MOSummarizationManager._eventBundleRanking
+ OBJC_IVAR_$_MOSummarizationParameters._coarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold
+ OBJC_IVAR_$_MOSummarizationParameters._coarseGranularity_outingBundlesExclusionGoodnessScoreThreshold
+ OBJC_IVAR_$_MOSummarizationParameters._fineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold
+ OBJC_IVAR_$_MOSummarizationParameters._fineGranularity_outingBundlesExclusionGoodnessScoreThreshold
+ OBJC_IVAR_$_MOSummarizationParameters._mediaBundleFirstPartyPlayTimePercentageThreshold
+ OBJC_IVAR_$_MOSummarizationParameters._weeklyActivitySummary_suppressionGoodnessScoreThreshold
+ OBJC_IVAR_$_MOTimeZoneManager._condensedRecords
+ OBJC_IVAR_$_MOTimeZoneManager._timeZoneRecords
+ OBJC_IVAR_$_MOTripAnnotationManager._minimumDwellTime
+ OBJC_IVAR_$_MOTripParameters._maximumFamiliarityIndex
+ _MOAnalyticsEventMediaPlayMetrics
+ _MOEventBundleTypeConversationTrend
+ _MOEventBundleTypeWorkoutTrend
+ _MOLogFacilitySettingsChange
+ _MOMediaPlayMetaDataKeyPlayerFirstPartyRatio
+ _MOMediaPlayMetaDataKeyPlayerStartDate
+ _MOPhotoResourceLocalTime
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSMediaTask
+ _OBJC_CLASS_$_MOMediaPlayMetrics
+ _OBJC_CLASS_$_MOTimeZoneManager
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSProcessPredicate
+ _OBJC_METACLASS_$_MOMediaPlayMetrics
+ _OBJC_METACLASS_$_MOTimeZoneManager
+ __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.460
+ __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.cold.1
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.408
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.408.cold.1
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.410
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.186
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.186.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.192
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.192.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.198
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.198.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.204
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.204.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.210
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.210.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.216
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.216.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.216.cold.2
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.220
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.225
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.230.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.236
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.236.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.241
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.241.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.241.cold.2
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.cold.1
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.187
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.193
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.199
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.205
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.211
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.226
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.237
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.188
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.194
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.200
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.206
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.212
+ __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.238
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.379
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.379.cold.1
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.383
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1054
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1056
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1056.cold.1
+ __118-[MONotificationsManager _serviceSuggestionsNotificationsTestForBundle:usingTrigger:useAppSchedule:completionHandler:]_block_invoke.cold.1
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.358
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.356
+ __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.357
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.340
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.346
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.342
+ __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.344
+ __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.514
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.371
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.369
+ __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.370
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.364
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.362
+ __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.363
+ __23-[MODaemonUniverse run]_block_invoke.108
+ __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1606
+ __38-[MOEventManager storeEvents:handler:]_block_invoke.274
+ __44-[MODaemonClient _localDataDumpWithHandler:]_block_invoke.372
+ __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.445
+ __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.446
+ __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.281
+ __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.314
+ __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.413
+ __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.414
+ __50-[MODaemonClient getMomentsNotificationsSchedule:]_block_invoke.216
+ __50-[MOUserData _fetchUserDataWithCompletionHandler:]_block_invoke.cold.5
+ __50-[MOUserData _fetchUserDataWithCompletionHandler:]_block_invoke.cold.6
+ __53-[MOManageServer listener:shouldAcceptNewConnection:]_block_invoke.165
+ __53-[MOTripAnnotationManager hometownReferenceLocations]_block_invoke.157
+ __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.133
+ __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.134
+ __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.135
+ __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.137
+ __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke_2.136
+ __55-[MOEventRefreshScheduler registerLightRefreshActivity]_block_invoke.164
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.483
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.321
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.325
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.329
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.339
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.349
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.353
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.357
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.361
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.365
+ __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.369
+ __57-[MOEventRefreshScheduler registerDefaultRefreshActivity]_block_invoke.102
+ __57-[MOEventRefreshScheduler registerDefaultRefreshActivity]_block_invoke.112
+ __57-[MONowPlayingMediaManager _fetchAppCateogryByBundleIds:]_block_invoke.cold.1
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.296
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.298
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.298.cold.1
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.621
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.621.cold.1
+ __59-[MOEventManager fetchEventsWithOptions:CompletionHandler:]_block_invoke.281
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.285
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.286
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.287
+ __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.289
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.469
+ __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.469.cold.1
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.421
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.425
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.429
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.433
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.437
+ __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.441
+ __61-[MOEventManager cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.373
+ __61-[MOEventManager collectEventsWithRefreshVariant:andHandler:]_block_invoke.144
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.851
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.386
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.386.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.390
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.397
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.397.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.404
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.404.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.408
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.408.cold.1
+ __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.409
+ __62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke.158
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.cold.5
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.cold.6
+ __64-[MORoutineServiceManager _removeVisitsDeletedAtSource:handler:]_block_invoke.154
+ __64-[MORoutineServiceManager _removeVisitsDeletedAtSource:handler:]_block_invoke.154.cold.1
+ __64-[MORoutineServiceManager _removeVisitsDeletedAtSource:handler:]_block_invoke.154.cold.2
+ __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.230
+ __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.235
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.248
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.249
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.250
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.254
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.255
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.259
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.263
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.264
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.265
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.266
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.267
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.268
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.269
+ __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.270
+ __65-[MOMediaPlayAnnotationManager _sortEventGroupsBasedOnRepetions:]_block_invoke.108
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.286
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.286.cold.1
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.290
+ __66-[MOEventRefreshScheduler _dataDumpWithRefreshVariant:completion:]_block_invoke.223
+ __67-[MOAggregationManager filterEventBundlesEligibleForSummarization:]_block_invoke.77
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.356
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.379
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.386
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.175
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.179
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.180
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.184
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.185
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.189
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.190
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.194
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.195
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.199
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.199.cold.1
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.200
+ __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.204
+ __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.182
+ __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.190
+ __68-[MOEventBundleStore purgeDeletedEventBundlesWithCompletionHandler:]_block_invoke.cold.1
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.448
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.453
+ __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.257
+ __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.280
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.316
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.317
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.321
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.328
+ __71-[MOEventBundleManager clearEventBundlesWithRefreshVariant:andHandler:]_block_invoke.658
+ __71-[MOEventBundleManager clearEventBundlesWithRefreshVariant:andHandler:]_block_invoke.658.cold.1
+ __71-[MOEventBundleManager fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.609
+ __71-[MOEventBundleManager fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.609.cold.1
+ __71-[MOEventBundleManager fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.610
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.598
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.598.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.599
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.599.cold.1
+ __71-[MOMotionManager _rehydrateMotionActivity:forLocationSetting:handler:]_block_invoke.138
+ __71-[MOMotionManager _rehydrateMotionActivity:forLocationSetting:handler:]_block_invoke.139
+ __71-[MOMotionManager _rehydrateMotionActivity:forLocationSetting:handler:]_block_invoke.140
+ __71-[MOMotionManager _rehydrateMotionActivity:forLocationSetting:handler:]_block_invoke.cold.1
+ __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke.157
+ __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke_2.158
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.617
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.617.cold.1
+ __72-[MOMotionManager _fetchMotionActivityBetweenStartDate:EndDate:handler:]_block_invoke.112
+ __73-[MOEventBundleManager cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.639
+ __73-[MOEventBundleManager cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.639.cold.1
+ __73-[MOEventBundleManager cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.640
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.650
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.650.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.651
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.251
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.251.cold.1
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.169
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.171
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.172
+ __74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke.172.cold.1
+ __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.120
+ __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.120.cold.1
+ __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.120.cold.2
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.302
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.302.cold.1
+ __76-[MORoutineServiceManager _createEventsFromVisits:familiarityIndex:handler:]_block_invoke.193
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.376
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.377
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.383
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.380
+ __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.380.cold.1
+ __77-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:startDate:handler:]_block_invoke_3.cold.1
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.144
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.146
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.146.cold.1
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.146.cold.2
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.147
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.148
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.151
+ __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.151.cold.1
+ __79-[MOConversationAnnotationManager _buildMappingFromBaseEvents:toPatternEvents:]_block_invoke.228
+ __80-[MOPhotosAtHomeManager _performAnnotationWithEvents:withPatternEvents:handler:]_block_invoke.136
+ __81-[MOHostingAtHomeManager _performAnnotationWithEvents:withPatternEvents:handler:]_block_invoke.135
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.250
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.250.cold.1
+ __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.296
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.476
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.481
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.486
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.491
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.496
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.501
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.506
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.511
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.516
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.521
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.526
+ __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.527
+ __82-[MOEventRefreshScheduler _purgeEventsAndBundlesWithRefreshVariant:andCompletion:]_block_invoke.209
+ __83-[MOContactAggregationManager aggregateBundles:withParameters:granularity:handler:]_block_invoke.68
+ __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke.381
+ __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke.383
+ __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke_2.382
+ __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke_2.384
+ __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.682
+ __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.687
+ __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.689
+ __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.699
+ __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.704
+ __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.704.cold.1
+ __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.420
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.304
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.305
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.312
+ __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.295
+ __84-[MOMotionManager _updateDeviceLocationsForMotionEvents:forLocationSetting:handler:]_block_invoke.141
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.348
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.350
+ __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.351
+ __85-[MOTimeAtHomeAnomalyManager _performAnnotationWithEvents:withPatternEvents:handler:]_block_invoke.135
+ __87-[MOTimeContextAggregationManager aggregateBundles:withParameters:granularity:handler:]_block_invoke.323
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.cold.1
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.240
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.241
+ __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.156
+ __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.156.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.326
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.327
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.331
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.332
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.336
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.336.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.337
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.341
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.341.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.341.cold.2
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.342
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.346
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.347
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.351.cold.1
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.352
+ __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.357
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.433
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.433.cold.1
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.cold.1
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.cold.2
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.cold.3
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.189
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.190
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.190.cold.1
+ __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.192
+ __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.127
+ __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.130
+ __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.138
+ __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.135
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1042
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.398
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.411
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.419
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.423
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.427
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.431
+ __OBJC_$_CLASS_METHODS_MOMediaPlayMetrics
+ __OBJC_$_CLASS_METHODS_MOOnboardingAndSettingsPersistence
+ __OBJC_$_CLASS_METHODS_MOVisitAnnotationManager
+ __OBJC_$_INSTANCE_METHODS_MOMediaPlayMetrics
+ __OBJC_$_INSTANCE_METHODS_MOTimeZoneManager
+ __OBJC_$_INSTANCE_VARIABLES_MOContactAggregationManager
+ __OBJC_$_INSTANCE_VARIABLES_MODominantBundleCreationManager
+ __OBJC_$_INSTANCE_VARIABLES_MOMediaPlayMetrics
+ __OBJC_$_INSTANCE_VARIABLES_MOTimeZoneManager
+ __OBJC_$_PROP_LIST_MOContactAggregationManager
+ __OBJC_$_PROP_LIST_MODominantBundleCreationManager
+ __OBJC_$_PROP_LIST_MOMediaPlayMetrics
+ __OBJC_$_PROP_LIST_MOTimeZoneManager
+ __OBJC_CLASS_PROTOCOLS_$_MOMediaPlayMetrics
+ __OBJC_CLASS_RO_$_MOMediaPlayMetrics
+ __OBJC_CLASS_RO_$_MOTimeZoneManager
+ __OBJC_METACLASS_RO_$_MOMediaPlayMetrics
+ __OBJC_METACLASS_RO_$_MOTimeZoneManager
+ ___101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke
+ ___112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke
+ ___115+[MOSummarizationUtilities createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:]_block_invoke
+ ___118-[MONotificationsManager _serviceSuggestionsNotificationsTestForBundle:usingTrigger:useAppSchedule:completionHandler:]_block_invoke
+ ___55-[MOTripAnnotationManager _filterPlaceUsingPredicates:]_block_invoke
+ ___56-[MOSummarizationManager _sortResourcesByPriorityScore:]_block_invoke
+ ___57-[MONowPlayingMediaManager _fetchAppCateogryByBundleIds:]_block_invoke
+ ___58+[MOSummarizationUtilities sortedWorkoutBundleByDuration:]_block_invoke
+ ___59+[MOSummarizationUtilities sortedBundleByPhotoAssetsCount:]_block_invoke
+ ___60-[MOTripAnnotationManager annotateBaseEvents:contextEvents:]_block_invoke_2
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke
+ ___63-[MOSummarizationManager removeDuplicateAssetsFromMediaBundle:]_block_invoke
+ ___63-[MOSummarizationManager removeDuplicateAssetsFromMediaBundle:]_block_invoke_2
+ ___66+[MOSummarizationUtilities getPlacesFromBundles:forSummaryBundle:]_block_invoke
+ ___67-[MOAggregationManager filterEventBundlesEligibleForSummarization:]_block_invoke
+ ___68-[MOEventBundleStore purgeDeletedEventBundlesWithCompletionHandler:]_block_invoke
+ ___69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke
+ ___69-[MONotificationsManager serviceSuggestionsNotificationsWithHandler:]_block_invoke_2
+ ___71-[MOMotionManager _rehydrateMotionActivity:forLocationSetting:handler:]_block_invoke
+ ___72-[MODaemonClient setupMomentsNotificationsWithSchedule:options:handler:]_block_invoke
+ ___72-[MODaemonClient setupMomentsNotificationsWithSchedule:options:handler:]_block_invoke_2
+ ___74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke
+ ___74-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterSettingChange]_block_invoke_2
+ ___77-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:startDate:handler:]_block_invoke
+ ___77-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:startDate:handler:]_block_invoke_2
+ ___77-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:startDate:handler:]_block_invoke_3
+ ___79+[MOOnboardingAndSettingsPersistence _fetchSignificantLocationEnablementStatus]_block_invoke
+ ___80+[MOContextAnnotationUtilities addPhotoResourcesWithDateArray:universe:handler:]_block_invoke
+ ___84-[MOMotionManager _updateDeviceLocationsForMotionEvents:forLocationSetting:handler:]_block_invoke
+ ___88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke
+ ___89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke
+ ___99-[MONotificationsManager setupPeriodicTimeToWriteMomentsNotificationsWithSchedule:options:handler:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72bs80r88r_e34_v24?0"NSError"8"NSDictionary"16lr80l8r88l8s72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72bs80r88r_e34_v24?0"NSError"8"NSDictionary"16lr80l8s32l8s40l8s48l8r88l8s56l8s72l8s64l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80bs88r96r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8r88l8r96l8s80l8s64l8s72l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88bs96r104r_e29_v24?0"NSArray"8"NSError"16lr96l8s88l8s32l8s40l8s48l8s56l8s64l8r104l8s72l8s80l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88bs96r104r_e29_v24?0"NSArray"8"NSError"16ls32l8r96l8s88l8s40l8s48l8s56l8s64l8r104l8s72l8s80l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96bs104r112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8r104l8s96l8s72l8r112l8s80l8s88l8
+ ___block_descriptor_32_e30_v32?0"MOEventBundle"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e54_v48?0"NSArray"8Q16"NSDate"24"NSDate"32"NSArray"40ls32l8
+ ___block_descriptor_40_e8_32r_e24_v32?0"MOPlace"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32r_e25_v32?0"MOAction"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32r40r_e20_v24?0"NSArray"8Q16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e20_v24?0q8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e31_v32?0"_CDInteraction"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e41_v32?0"NSArray"8"NSArray"16"NSArray"24ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_60_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32r40r48r56r_e54_v48?0"NSArray"8Q16"NSDate"24"NSDate"32"NSArray"40lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_65_e8_32s40bs48r56r_e29_v24?0"NSArray"8"NSError"16ls40l8r48l8r56l8s32l8
+ ___block_descriptor_65_e8_32s40s48bs56r_e29_v24?0"NSArray"8"NSError"16ls48l8r56l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e32_v32?0"NSArray"8Q16"NSError"24lr40l8r48l8r56l8r64l8r72l8s32l8
+ ___block_descriptor_89_e8_32s40r48r56r64r72r80r_e36_v32?0"NSMutableDictionary"8Q16^B24lr40l8r48l8r56l8r64l8r72l8r80l8s32l8
+ ___block_descriptor_96_e8_32s40s48s56bs64r72r80r_e5_v8?0ls32l8r64l8s40l8r72l8r80l8s56l8s48l8
+ __block_literal_global.137
+ __block_literal_global.167
+ __block_literal_global.231
+ __block_literal_global.233
+ __block_literal_global.253
+ __block_literal_global.294
+ __block_literal_global.304
+ __block_literal_global.306
+ __block_literal_global.308
+ __block_literal_global.310
+ __block_literal_global.338
+ __block_literal_global.350
+ __block_literal_global.354
+ __block_literal_global.356
+ __block_literal_global.360
+ __block_literal_global.366
+ __block_literal_global.367
+ __block_literal_global.369
+ __block_literal_global.371
+ __block_literal_global.373
+ __block_literal_global.375
+ __block_literal_global.378
+ __block_literal_global.380
+ __block_literal_global.382
+ __block_literal_global.397
+ __block_literal_global.404
+ __block_literal_global.411
+ __block_literal_global.413
+ __block_literal_global.415
+ __block_literal_global.442
+ __block_literal_global.444
+ __block_literal_global.485
+ __block_literal_global.487
+ __block_literal_global.545
+ __block_literal_global.562
+ __block_literal_global.602
+ __block_literal_global.664
+ __block_literal_global.79
+ __block_literal_global.98
+ _emptyString
+ _emptyStringSet
+ _kEventDwellDuration
+ _kIsCoarseGranularitySummaryKey
+ _kIsPseudoDupKey
+ _kMODiagnosticReporterIsOnboardedOnJournalStudy
+ _kMOEventMediaFirstPartyTimePlayedRatio
+ _kMOLabelFormatterMetaKeywordDateReferenceRecency
+ _kMOLabelFormatterMetaKeywordDateReferenceTimeTag
+ _kMOLabelFormatterMetaKeywordDoubleDominantPlaces
+ _kMOLabelFormatterMetaKeywordVicinityPrefix
+ _kMOPlaceEndDate
+ _kMOPlacePOICategory
+ _kMOPlaceStartDate
+ _kMOPlaceUUID
+ _kMOTripAnnotationManagerMaximumFamiliarityIndexDefault
+ _kMOTripAnnotationManagerMaximumFamiliarityIndexDefaultKeyword
+ _kMOTripAnnotationManagerMaximumFamiliarityIndexInternationalTrip
+ _kMOTripAnnotationManagerMaximumFamiliarityIndexInternationalTripKeyword
+ _kMediaBundleIdDenyList
+ _kMinSensedBundleCountInRecommendedTab
+ _kNumMediaAssetsResourcesNormalizedKey
+ _kNumPhotoAssetsResourcesNormalizedKey
+ _kPhotoCurationScore
+ _kPlaceNamesSetKey
+ _kRichnessScoreScalingParameterKey
+ _kSummarizationThresholdForActivitySubTypeVariants
+ _kSummarizationThresholdForVisitSubTypeVariants
+ _kThirdPartyMediaBundleId
+ _kWorkoutTypesSetKey
+ _kisEligibleForSummarization
+ _objc_msgSend$_Moments_LocalizedStringForKey:withTable:
+ _objc_msgSend$_assignPriorityScoreForPlace:placeInfoArray:
+ _objc_msgSend$_calculateRankingScore:withMinRecommendedBundleCountRequirement:
+ _objc_msgSend$_createBundlesFromEvents:
+ _objc_msgSend$_dedupAssetForMediaBundle:nonPlayedMediaBudnles:isRecommendTab:
+ _objc_msgSend$_eligibleInteraction:
+ _objc_msgSend$_fetchAppCateogryByBundleIds:
+ _objc_msgSend$_fetchSignificantLocationEnablementStatus
+ _objc_msgSend$_filterMediaSessionsBasedOnFirstPartyApps:
+ _objc_msgSend$_filterMediaSessionsBasedOnMusicApps:
+ _objc_msgSend$_filterPlaceUsingPredicates:
+ _objc_msgSend$_getArrayScheduledDateComponents
+ _objc_msgSend$_getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:
+ _objc_msgSend$_getNextNotificationDateComponentsWithOptions:afterDate:numWeeks:setComponents:
+ _objc_msgSend$_getNextScheduledCalendarNotificationTrigger
+ _objc_msgSend$_getPhotosByAssetProperties:UserLocations:MaxDistance:
+ _objc_msgSend$_getSortedArrayScheduledDatesWithOptions:afterDate:numWeeks:setComponents:
+ _objc_msgSend$_maximumGoodnessScoreDeltaFromBundle:toCluster:
+ _objc_msgSend$_rehydrateMotionActivity:forLocationSetting:handler:
+ _objc_msgSend$_removeDuplicateFromResource:nonMediaKeySet:mediaOnRepeatDict:eventBundleDayKey:keyName:
+ _objc_msgSend$_saveMediaPlayGroupsByDayTitle:startDate:handler:
+ _objc_msgSend$_serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:
+ _objc_msgSend$_serviceSuggestionsNotificationsTestForBundle:usingTrigger:useAppSchedule:completionHandler:
+ _objc_msgSend$_sheetIsVisible
+ _objc_msgSend$_sortResourcesByPriorityScore:
+ _objc_msgSend$_updateDeviceLocationsForMotionEvents:forLocationSetting:handler:
+ _objc_msgSend$_updateMOPlacePriorityScore:priorityScore:handler:
+ _objc_msgSend$_updateMetaDataForRanking:forEvents:places:
+ _objc_msgSend$addFinishBlock:
+ _objc_msgSend$addPhotoResourcesWithDateArray:universe:handler:
+ _objc_msgSend$bagForProfile:profileVersion:
+ _objc_msgSend$bagSubProfile
+ _objc_msgSend$bagSubProfileVersion
+ _objc_msgSend$bmAbsoluteTime
+ _objc_msgSend$buildSimpleTimeTagIntervalsWithLeewayForDate:
+ _objc_msgSend$bundleIdCategoryMappings
+ _objc_msgSend$coarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold
+ _objc_msgSend$coarseGranularity_outingBundlesExclusionGoodnessScoreThreshold
+ _objc_msgSend$combineMediaResources:
+ _objc_msgSend$combinePhotoResources:
+ _objc_msgSend$componentsInTimeZone:fromDate:
+ _objc_msgSend$condensedRecords
+ _objc_msgSend$condensedRecordsFromRecords:
+ _objc_msgSend$createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:
+ _objc_msgSend$createDominantBundleFromBundles:withParameters:timeZoneManager:
+ _objc_msgSend$createMegaBundleFromBundles:parameters:timeZoneManager:
+ _objc_msgSend$createOutingMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:
+ _objc_msgSend$currentState
+ _objc_msgSend$dateFormatFromTemplate:options:locale:
+ _objc_msgSend$dateReferenceTagFromStartDate:endDate:nowDate:timeZone:
+ _objc_msgSend$dayOfWeekFromStartDate:endDate:timeZoneManager:
+ _objc_msgSend$dominantPlaceNamesFromEvents:
+ _objc_msgSend$dominantPlaceNamesFromEvents:countryMode:
+ _objc_msgSend$endowmentNamespaces
+ _objc_msgSend$eventBundleRanking
+ _objc_msgSend$fetchRoutineStateWithHandler:
+ _objc_msgSend$filterEventBundlesEligibleForSummarization:
+ _objc_msgSend$fineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold
+ _objc_msgSend$fineGranularity_outingBundlesExclusionGoodnessScoreThreshold
+ _objc_msgSend$firstPartyTimePlayedRatio
+ _objc_msgSend$generateBundleRanking:withMinRecommendedBundleCountRequirement:
+ _objc_msgSend$getMomentsNotificationsSchedule:
+ _objc_msgSend$getPlacesFromBundles:forSummaryBundle:
+ _objc_msgSend$getResourcesForOutingSummaryBundleWithWorkoutResources:photoResources:mediaResources:shouldUpLevelPhoto:
+ _objc_msgSend$getResourcesForWeeklyWorkoutSummaryBundleWithWorkoutResources:photoResources:mediaResources:
+ _objc_msgSend$getResourcesFromBundles:forSummaryBundle:
+ _objc_msgSend$handleForPredicate:error:
+ _objc_msgSend$hasWorkoutRoute:
+ _objc_msgSend$homeLOI
+ _objc_msgSend$initScheduleWithHour:minute:weekdays:
+ _objc_msgSend$initWithAllowedCategories:dateInterval:ascending:limit:includeDeletedBundles:skipRanking:interfaceType:
+ _objc_msgSend$initWithDateInterval:ascending:limit:includeDeletedBundles:skipRanking:interfaceType:
+ _objc_msgSend$initWithFirstPartyAppRatio:firstPartyAppTime:musciAppTime:
+ _objc_msgSend$initWithName:value:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithType:clientIdentifier:clientVersion:bag:
+ _objc_msgSend$initWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$intersectedActivityOrVisitForObject:other:
+ _objc_msgSend$intersectedSubBundleIDForObject:other:
+ _objc_msgSend$isBundle:insideTheSameDayAsOtherBundle:
+ _objc_msgSend$isBundleWithAssets:
+ _objc_msgSend$isEqualBasicPropertiesForObject:other:
+ _objc_msgSend$isEqualToTimeZone:
+ _objc_msgSend$keysSortedByValueUsingSelector:
+ _objc_msgSend$keywordForDate:
+ _objc_msgSend$localTime
+ _objc_msgSend$localTimeOfDate:timeZone:
+ _objc_msgSend$localizedString:withTable:
+ _objc_msgSend$maximumFamiliarityIndex
+ _objc_msgSend$mediaBundleFirstPartyPlayTimePercentageThreshold
+ _objc_msgSend$mediaEvent
+ _objc_msgSend$mediaFirstPartyTimePlayedRatio
+ _objc_msgSend$mergeOutingBundlesWithInDayWithGrouppedBundles:remainingSingletonBundles:parameters:isCoarseGranularity:timeZoneManager:
+ _objc_msgSend$nextDateAfterDate:matchingComponents:options:
+ _objc_msgSend$nextTriggerDate
+ _objc_msgSend$perform
+ _objc_msgSend$photoOverallAestheticScore
+ _objc_msgSend$placeNames
+ _objc_msgSend$postRefreshTriggerAfterSettingChange
+ _objc_msgSend$predicateMatchingBundleIdentifier:
+ _objc_msgSend$processTimeZoneEvents:
+ _objc_msgSend$purgeDeletedEventBundlesWithCompletionHandler:
+ _objc_msgSend$queryItems
+ _objc_msgSend$removeAllPendingNotificationRequests
+ _objc_msgSend$removeDuplicateAssetsFromMediaBundle:
+ _objc_msgSend$removeDuplicateWorkouts:
+ _objc_msgSend$resourcesFromEvents:handler:
+ _objc_msgSend$responseDataItems
+ _objc_msgSend$safeSavePropertyToDictionary:withKey:andValue:
+ _objc_msgSend$scoreVisitBundleAssets:
+ _objc_msgSend$secondsFromGMTForDate:
+ _objc_msgSend$serviceSuggestionsNotificationsWithHandler:
+ _objc_msgSend$setBundleIdentifiers:
+ _objc_msgSend$setCondensedRecords:
+ _objc_msgSend$setMaximumFamiliarityIndex:
+ _objc_msgSend$setMediaFirstPartyTimePlayedRatio:
+ _objc_msgSend$setNumMediaTypeResourcesNormalized:
+ _objc_msgSend$setNumPhotoAssetsResourcesNormalized:
+ _objc_msgSend$setPlaceNames:
+ _objc_msgSend$setQueryItems:
+ _objc_msgSend$setTimeZoneRecords:
+ _objc_msgSend$setWorkoutTypes:
+ _objc_msgSend$setupFallbackAppBrandedNotificationsWithDateComponents:handler:
+ _objc_msgSend$setupPeriodicTimeToWriteMomentsNotificationsWithSchedule:options:handler:
+ _objc_msgSend$significantContactEvent
+ _objc_msgSend$sortedBundleByPhotoAssetsCount:
+ _objc_msgSend$string
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$taskState
+ _objc_msgSend$timeForDate:timeZoneManager:
+ _objc_msgSend$timeFromStartDate:endDate:timeZoneManager:
+ _objc_msgSend$timeZoneAtDate:
+ _objc_msgSend$timeZoneManager
+ _objc_msgSend$timeZoneObject
+ _objc_msgSend$timeZoneRecords
+ _objc_msgSend$timeZoneWithName:
+ _objc_msgSend$timezone
+ _objc_msgSend$weeklyActivitySummary_suppressionGoodnessScoreThreshold
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$workoutTypes
+ _unnamed_array_storage.1015
+ _unnamed_array_storage.1025
+ _unnamed_array_storage.104
+ _unnamed_array_storage.140
+ _unnamed_array_storage.222
+ _unnamed_array_storage.272
+ _unnamed_array_storage.294
+ _unnamed_array_storage.768
+ _unnamed_array_storage.778
+ _unnamed_array_storage.793
+ _unnamed_array_storage.798
+ _unnamed_array_storage.807
+ _unnamed_array_storage.816
+ _unnamed_array_storage.823
+ _unnamed_array_storage.830
+ _unnamed_array_storage.839
+ _unnamed_array_storage.92
+ _unnamed_array_storage.98
- +[MOContextAnnotationUtilities addPhotoResources:universe:handler:].cold.1
- +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:].cold.1
- +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:].cold.2
- +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:].cold.3
- +[MOSummarizationUtilities createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:]
- +[MOSummarizationUtilities createDominantBundleFromBundles:withParameters:]
- +[MOSummarizationUtilities createMegaBundleFromBundles:parameters:]
- +[MOSummarizationUtilities createOutingMegaBundleFromBundles:withParameters:isCoarseGranularity:]
- +[MOSummarizationUtilities getPlacesFromBundles:]
- +[MOSummarizationUtilities getResourcesFromBundles:]
- +[MOSummarizationUtilities mergeOutingBundlesWithInDayWithGrouppedBundles:remainingSingletonBundles:parameters:isCoarseGranularity:]
- +[MOTime dateReferenceTagFromStartDate:endDate:nowDate:]
- +[MOTime dayOfWeekFromStartDate:endDate:]
- +[MOTime timeFromDate:]
- -[MODominantBundleCreationManager init]
- -[MOEventBundleManager notificationsManager]
- -[MOEventBundleRanking FIDownRankThreshold]
- -[MOEventBundleRanking _calculateRankingScore:]
- -[MOEventBundleRanking _calculateRankingScore:].cold.1
- -[MOEventBundleRanking _calculateRankingScore:].cold.2
- -[MOEventBundleRanking _calculateRankingScore:].cold.3
- -[MOEventBundleRanking _calculateRankingScore:].cold.4
- -[MOEventBundleRanking _fillQualityInfoForRanking:forBundle:].cold.5
- -[MOEventBundleRanking burstyInteractionCountThreshold]
- -[MOEventBundleRanking callDurationThreshold]
- -[MOEventBundleRanking distanceToHomeThreshold]
- -[MOEventBundleRanking generateBundleRanking:]
- -[MOEventBundleRanking generateBundleRanking:].cold.1
- -[MOEventBundleRanking generateBundleRanking:].cold.2
- -[MOEventBundleRanking generateBundleRanking:].cold.3
- -[MOEventBundleRanking maxPeopleCountFromSocialContext]
- -[MOEventBundleRanking mediaPlayTimeThreshold]
- -[MOEventBundleRanking setBurstyInteractionCountThreshold:]
- -[MOEventBundleRanking setCallDurationThreshold:]
- -[MOEventBundleRanking setDistanceToHomeThreshold:]
- -[MOEventBundleRanking setFIDownRankThreshold:]
- -[MOEventBundleRanking setMaxPeopleCountFromSocialContext:]
- -[MOEventBundleRanking setMediaPlayTimeThreshold:]
- -[MOEventBundleRanking setShareCountThreshold:]
- -[MOEventBundleRanking setTimeAtHomeDurationThreshold:]
- -[MOEventBundleRanking setWorkoutDurationThreshold:]
- -[MOEventBundleRanking shareCountThreshold]
- -[MOEventBundleRanking timeAtHomeDurationThreshold]
- -[MOEventBundleRanking workoutDurationThreshold]
- -[MOHostingAtHomeManager routineManager]
- -[MOHostingAtHomeManager setRoutineManager:]
- -[MOMotionManager _rehydrateMotionActivity:handler:]
- -[MOMotionManager _updateDeviceLocationsForMotionEvents:handler:]
- -[MONotificationsManager _clearDeprecatedNotifications]
- -[MONotificationsManager _clearDeprecatedNotifications].cold.1
- -[MONotificationsManager _getAppCalendarNotificationTrigger]
- -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesWithCompletionHandler:]
- -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesWithCompletionHandler:].cold.1
- -[MONotificationsManager _getNewTargetTimeToWriteEventBundlesWithCompletionHandler:].cold.2
- -[MONotificationsManager _getNextPossibleNotificationDateComponents]
- -[MONotificationsManager _getNextPossibleNotificationDateComponents].cold.1
- -[MONotificationsManager _getNextPossibleNotificationDateComponents].cold.2
- -[MONotificationsManager _getNextPossibleNotificationDateComponents].cold.3
- -[MONotificationsManager _postTimeToWriteAppNotificationUsingTrigger:withCompletionHandler:]
- -[MONotificationsManager _serviceSuggestionsNotificationsInternalForBundle:usingTrigger:useAppSchedule:completionHandler:]
- -[MONotificationsManager serviceSuggestionsNotifications]
- -[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:handler:]
- -[MONowPlayingMediaManager filterMediaSessionsBasedOnApps:]
- -[MONowPlayingMediaManager firstPartyPlayTimePercentageThreshold]
- -[MONowPlayingMediaManager setFirstPartyPlayTimePercentageThreshold:]
- -[MOPhotoManager _getFallbackPhotos:]
- -[MOPhotosAtHomeManager routineManager]
- -[MOPhotosAtHomeManager setRoutineManager:]
- -[MORoutineServiceManager setHomeLOI:]
- -[MOTimeAtHomeAnomalyManager routineManager]
- -[MOTimeAtHomeAnomalyManager setRoutineManager:]
- -[MOTripAnnotationManager _updateMetaDataForRanking:forEvents:]
- -[MOTripAnnotationManager dominantPlaceNameFromEvents:]
- -[MOTripAnnotationManager dominantPlaceNameFromEvents:].cold.1
- -[MOTripAnnotationManager dominantPlaceNameFromEvents:countryMode:]
- -[MOTripAnnotationManager dominantPlaceNameFromEvents:countryMode:].cold.1
- -[MOTripAnnotationManager resourcesFromEvents:]
- GCC_except_table112
- GCC_except_table128
- GCC_except_table135
- GCC_except_table143
- GCC_except_table21
- GCC_except_table36
- GCC_except_table57
- GCC_except_table67
- GCC_except_table76
- GCC_except_table81
- GCC_except_table87
- OBJC_IVAR_$_MOEventBundleManager._notificationsManager
- OBJC_IVAR_$_MOEventBundleRanking._FIDownRankThreshold
- OBJC_IVAR_$_MOEventBundleRanking._burstyInteractionCountThreshold
- OBJC_IVAR_$_MOEventBundleRanking._callDurationThreshold
- OBJC_IVAR_$_MOEventBundleRanking._distanceToHomeThreshold
- OBJC_IVAR_$_MOEventBundleRanking._maxPeopleCountFromSocialContext
- OBJC_IVAR_$_MOEventBundleRanking._mediaPlayTimeThreshold
- OBJC_IVAR_$_MOEventBundleRanking._shareCountThreshold
- OBJC_IVAR_$_MOEventBundleRanking._timeAtHomeDurationThreshold
- OBJC_IVAR_$_MOEventBundleRanking._workoutDurationThreshold
- OBJC_IVAR_$_MOHostingAtHomeManager._routineManager
- OBJC_IVAR_$_MONowPlayingMediaManager._firstPartyPlayTimePercentageThreshold
- OBJC_IVAR_$_MOPhotosAtHomeManager._routineManager
- OBJC_IVAR_$_MOTimeAtHomeAnomalyManager._routineManager
- _PLLogRegisteredEvent
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.395
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.395.cold.1
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.397
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.399
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke_2.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.248
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.257
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.266
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.273
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.274
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.281
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.289
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.298
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.301
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.302
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.302.cold.1
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke.302.cold.2
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.222
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.240
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.249
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.258
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.282
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.290
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_2.299
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.223
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.241
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.250
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.259
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.291
- __105-[MOEventManager _collectCompleteEventsBetweenStartDate:endDate:refreshVariant:withStoredEvents:handler:]_block_invoke_3.300
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1034
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1036
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1036.cold.1
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.352
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.353
- __119-[MOEngagementHistoryManager getEvergreenTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.354
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.337
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke.343
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_2.339
- __119-[MOEngagementHistoryManager getInterfaceTypeCountForSuggestionEngagmentEvent:from:to:onceForEachBundle:skipForEvents:]_block_invoke_3.341
- __122-[MONotificationsManager _serviceSuggestionsNotificationsInternalForBundle:usingTrigger:useAppSchedule:completionHandler:]_block_invoke.cold.1
- __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.cold.1
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.365
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.366
- __177-[MOEngagementHistoryManager getEvergreenTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.367
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke.358
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_2.359
- __177-[MOEngagementHistoryManager getInterfaceTypeCountForAppEntryEvent:withMinAddedCharacterCount:andMaxAddedCharacterCount:fromStartDate:toEndDate:onceForEachBundle:skipForEvents:]_block_invoke_3.360
- __18-[MOWatchDog _pet]_block_invoke.cold.1
- __23-[MODaemonUniverse run]_block_invoke.106
- __38-[MOEventManager storeEvents:handler:]_block_invoke.350
- __44-[MODaemonClient _localDataDumpWithHandler:]_block_invoke.391
- __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.623
- __44-[MOEventManager _purgePreOnboardingEvents:]_block_invoke.624
- __47-[MOEventBundleRanking _calculateRankingScore:]_block_invoke.cold.1
- __47-[MOEventManager _rehydrateEvents:withHandler:]_block_invoke.396
- __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.567
- __48-[MOEventManager _updateEventsDeletedAtSources:]_block_invoke.568
- __52-[MOMotionManager _rehydrateMotionActivity:handler:]_block_invoke.138
- __52-[MOMotionManager _rehydrateMotionActivity:handler:]_block_invoke.139
- __52-[MOMotionManager _rehydrateMotionActivity:handler:]_block_invoke.140
- __52-[MOMotionManager _rehydrateMotionActivity:handler:]_block_invoke.cold.1
- __53-[MOManageServer listener:shouldAcceptNewConnection:]_block_invoke.163
- __53-[MOTripAnnotationManager hometownReferenceLocations]_block_invoke.128
- __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.163
- __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.164
- __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.165
- __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke.167
- __55-[MOEventRefreshScheduler registerFirstRefreshActivity]_block_invoke_2.166
- __55-[MOEventRefreshScheduler registerLightRefreshActivity]_block_invoke.196
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.498
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.409
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.416
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.423
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.442
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.461
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.468
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.475
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.482
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.489
- __57-[MOEventManager _rehydrateEventsBySingleSource:handler:]_block_invoke.496
- __57-[MOEventRefreshScheduler registerDefaultRefreshActivity]_block_invoke.127
- __57-[MOEventRefreshScheduler registerDefaultRefreshActivity]_block_invoke.140
- __57-[MONotificationsManager serviceSuggestionsNotifications]_block_invoke_2.cold.1
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.170
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.172
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.172.cold.1
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.747
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.747.cold.1
- __59-[MOEventManager fetchEventsWithOptions:CompletionHandler:]_block_invoke.360
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.364
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.365
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.366
- __60-[MOEventManager _fetchEventsWithOptions:CompletionHandler:]_block_invoke.368
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.656
- __60-[MOEventManager runAnalyticsWithRefreshVariant:andHandler:]_block_invoke.656.cold.1
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.581
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.588
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.595
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.602
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.609
- __61-[MOEventManager _updateEventsDeletedAtSingleSource:handler:]_block_invoke.616
- __61-[MOEventManager cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.503
- __61-[MOEventManager collectEventsWithRefreshVariant:andHandler:]_block_invoke.178
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.525
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.525.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.532
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.542
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.542.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.552
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.552.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.559
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.559.cold.1
- __62-[MOEventManager _cleanUpEventsWithRefreshVariant:andHandler:]_block_invoke.560
- __64-[MORoutineServiceManager _removeVisitsDeletedAtSource:handler:]_block_invoke.187
- __64-[MORoutineServiceManager _removeVisitsDeletedAtSource:handler:]_block_invoke.187.cold.1
- __64-[MORoutineServiceManager _removeVisitsDeletedAtSource:handler:]_block_invoke.187.cold.2
- __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.252
- __65-[MODaemonClient _fetchEventsWithOptions:withContext:andHandler:]_block_invoke.260
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.312
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.313
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.314
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.321
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.322
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.329
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.336
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.337
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.338
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.339
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.340
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.341
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.342
- __65-[MOEventManager _collectEventsBetweenStartDate:EndDate:handler:]_block_invoke.343
- __65-[MOMediaPlayAnnotationManager _sortEventGroupsBasedOnRepetions:]_block_invoke.107
- __65-[MOMotionManager _updateDeviceLocationsForMotionEvents:handler:]_block_invoke.141
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.322
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.322.cold.1
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.329
- __66-[MOEventRefreshScheduler _dataDumpWithRefreshVariant:completion:]_block_invoke.251
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.404
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.430
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.443
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.207
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.211
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.212
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.216
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.217
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.221
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.222
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.226
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.226.cold.1
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.227
- __67-[MOEventRefreshScheduler refreshWithRefreshVariant:andCompletion:]_block_invoke.231
- __67-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:handler:]_block_invoke_3.cold.1
- __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.172
- __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.180
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.518
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.526
- __71-[MODaemonClient _fetchEventBundlesWithOptions:withContext:andHandler:]_block_invoke.282
- __71-[MODaemonClient _purgeEventsWithContext:andRefreshVariant:andHandler:]_block_invoke.305
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.363
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.364
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.368
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.375
- __71-[MOEventBundleManager clearEventBundlesWithRefreshVariant:andHandler:]_block_invoke.805
- __71-[MOEventBundleManager clearEventBundlesWithRefreshVariant:andHandler:]_block_invoke.805.cold.1
- __71-[MOEventBundleManager fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.729
- __71-[MOEventBundleManager fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.729.cold.1
- __71-[MOEventBundleManager fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.730
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.712
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.712.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.713
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.713.cold.1
- __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke.154
- __71-[MOOnboardingAndSettingsPersistence postRefreshTriggerAfterOnboarding]_block_invoke_2.155
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.740
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.740.cold.1
- __72-[MOMotionManager _fetchMotionActivityBetweenStartDate:EndDate:handler:]_block_invoke.111
- __73-[MOEventBundleManager cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.774
- __73-[MOEventBundleManager cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.774.cold.1
- __73-[MOEventBundleManager cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.775
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.791
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.791.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.792
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.202
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.202.cold.1
- __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.154
- __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.154.cold.1
- __74-[MORoutineServiceManager _fetchVisitsBetweenStartDate:CompletionHandler:]_block_invoke.154.cold.2
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.176
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.176.cold.1
- __76-[MORoutineServiceManager _createEventsFromVisits:familiarityIndex:handler:]_block_invoke.232
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.373
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.374
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke.380
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.377
- __77-[MOEngagementHistoryManager eventBundleStore:needsEngagementInfoForBundles:]_block_invoke_2.377.cold.1
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.177
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.179
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.179.cold.1
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.179.cold.2
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.180
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.181
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.184
- __78-[MORoutineServiceManager fetchAndSaveVisitsBetweenStartDate:EndDate:handler:]_block_invoke.184.cold.1
- __79-[MOConversationAnnotationManager _buildMappingFromBaseEvents:toPatternEvents:]_block_invoke.197
- __80-[MOPhotosAtHomeManager _performAnnotationWithEvents:withPatternEvents:handler:]_block_invoke.135
- __81-[MOHostingAtHomeManager _performAnnotationWithEvents:withPatternEvents:handler:]_block_invoke.134
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.201
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.201.cold.1
- __82-[MODaemonClient _analyzeTrendsInEvents:withContext:andRefreshVariant:andHandler:]_block_invoke.321
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.551
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.559
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.567
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.575
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.583
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.591
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.599
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.607
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.615
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.623
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.631
- __82-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:events:handler:]_block_invoke.632
- __82-[MOEventRefreshScheduler _purgeEventsAndBundlesWithRefreshVariant:andCompletion:]_block_invoke.236
- __83-[MOContactAggregationManager aggregateBundles:withParameters:granularity:handler:]_block_invoke.65
- __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke.402
- __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke.404
- __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke_2.403
- __83-[MODaemonClient _dataDumpAndUploadWithFeedback:refreshVariant:context:completion:]_block_invoke_2.405
- __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.841
- __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.855
- __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.857
- __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.870
- __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.878
- __83-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:andHandler:]_block_invoke.878.cold.1
- __84-[MODaemonClient didAppEntryUpdateUsingSuggestions:onEvent:duringInterval:withInfo:]_block_invoke.441
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.346
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.347
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.356
- __84-[MOEventManager _fetchEventsFromDBAndRehydrateEventsWithOptions:CompletionHandler:]_block_invoke.374
- __84-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesWithCompletionHandler:]_block_invoke.427
- __84-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesWithCompletionHandler:]_block_invoke.cold.1
- __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.89
- __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.91
- __85-[MOSummarizationManager _aggregateEventBundles:withAggregtaionDateInterval:handler:]_block_invoke.92
- __85-[MOTimeAtHomeAnomalyManager _performAnnotationWithEvents:withPatternEvents:handler:]_block_invoke.134
- __87-[MOTimeContextAggregationManager aggregateBundles:withParameters:granularity:handler:]_block_invoke.65
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.190
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.191
- __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.189
- __88-[MORoutineServiceManager _fetchFamiliarityIndexesLOIForDateInterval:CompletionHandler:]_block_invoke.189.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.350
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.355
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.355.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.360
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.360.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.360.cold.2
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.365
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.366
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.370
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.370.cold.1
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.371
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.375
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.376
- __89-[MODaemonClient _refreshEventsWithContext:andRefreshVariant:andSoftKindFlag:andHandler:]_block_invoke.380
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.228
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.229
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.229.cold.1
- __89-[MORoutineServiceManager _fetchVisitsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.231
- __92-[MONotificationsManager _postTimeToWriteAppNotificationUsingTrigger:withCompletionHandler:]_block_invoke.cold.1
- __92-[MONotificationsManager _postTimeToWriteAppNotificationUsingTrigger:withCompletionHandler:]_block_invoke.cold.2
- __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.114
- __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.117
- __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.125
- __93-[MONowPlayingMediaManager _fetchNowPlayingEventsBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.122
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1022
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.463
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.477
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.484
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.491
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.491.cold.1
- ___101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke_2
- ___122-[MONotificationsManager _serviceSuggestionsNotificationsInternalForBundle:usingTrigger:useAppSchedule:completionHandler:]_block_invoke
- ___18-[MOWatchDog _pet]_block_invoke
- ___21-[MOWatchDog dealloc]_block_invoke
- ___37-[MOPromptMetrics getAndSetAgeGender]_block_invoke_2
- ___45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke_2
- ___47-[MOEventBundleRanking _calculateRankingScore:]_block_invoke
- ___49+[MOSummarizationUtilities getPlacesFromBundles:]_block_invoke
- ___52-[MOMotionManager _rehydrateMotionActivity:handler:]_block_invoke
- ___57-[MONotificationsManager serviceSuggestionsNotifications]_block_invoke
- ___57-[MONotificationsManager serviceSuggestionsNotifications]_block_invoke_2
- ___62-[MOEventManager _collectEventsWithRefreshVariant:andHandler:]_block_invoke_3
- ___65-[MOMotionManager _updateDeviceLocationsForMotionEvents:handler:]_block_invoke
- ___67-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:handler:]_block_invoke
- ___67-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:handler:]_block_invoke_2
- ___67-[MONowPlayingMediaManager _saveMediaPlayGroupsByDayTitle:handler:]_block_invoke_3
- ___68+[MOContextAnnotationUtilities distanceFromHomeToLocation:universe:]_block_invoke
- ___70+[MOContextAnnotationUtilities distanceFromHomeToCLLocation:universe:]_block_invoke
- ___84-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesWithCompletionHandler:]_block_invoke
- ___88-[MOTimeContextAggregationManager _megaBundleFromActivityTimeContextBundles:parameters:]_block_invoke
- ___92-[MONotificationsManager _postTimeToWriteAppNotificationUsingTrigger:withCompletionHandler:]_block_invoke
- ___95-[MOTimeContextAggregationManager _megaBundlesFromOutingActivityTimeContextBundles:parameters:]_block_invoke
- ___99+[MOSummarizationUtilities createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56bs64r72r80r88r_e5_v8?0ls32l8r64l8s40l8r72l8r80l8r88l8s56l8s48l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88bs96r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8r96l8s88l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s80s88bs96r_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8s64l8r96l8s72l8s88l8s80l8
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96bs104r_e29_v24?0"NSArray"8"NSError"16ls32l8r104l8s96l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8r112l8s104l8s72l8s80l8s88l8s96l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104bs112r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r112l8s104l8s88l8s96l8
- ___block_descriptor_40_e8_32s_e31_v32?0"_CDInteraction"8Q16^B24ls32l8
- ___block_descriptor_49_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40bs48r56r_e29_v24?0"NSArray"8"NSError"16ls40l8r48l8r56l8s32l8
- ___block_descriptor_64_e8_32s40bs48r56r_e34_v24?0"NSError"8"NSDictionary"16ls32l8r48l8r56l8s40l8
- ___block_descriptor_72_e8_32s40bs48r56r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8r56l8s40l8
- ___block_descriptor_72_e8_32s40r48r56r64r_e32_v32?0"NSArray"8Q16"NSError"24lr40l8r48l8r56l8r64l8s32l8
- ___block_descriptor_72_e8_32s40r48r56r64r_e36_v32?0"NSMutableDictionary"8Q16^B24lr40l8r48l8r56l8r64l8s32l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- __block_literal_global.101
- __block_literal_global.104
- __block_literal_global.108
- __block_literal_global.112
- __block_literal_global.123
- __block_literal_global.165
- __block_literal_global.168
- __block_literal_global.178
- __block_literal_global.200
- __block_literal_global.202
- __block_literal_global.204
- __block_literal_global.303
- __block_literal_global.305
- __block_literal_global.307
- __block_literal_global.335
- __block_literal_global.347
- __block_literal_global.351
- __block_literal_global.357
- __block_literal_global.364
- __block_literal_global.370
- __block_literal_global.376
- __block_literal_global.425
- __block_literal_global.430
- __block_literal_global.432
- __block_literal_global.434
- __block_literal_global.436
- __block_literal_global.500
- __block_literal_global.502
- __block_literal_global.656
- __block_literal_global.673
- __block_literal_global.716
- __block_literal_global.814
- __block_literal_global.92
- __block_literal_global.95
- __block_literal_global.97
- _callLikeMechanisms
- _objc_msgSend$_calculateRankingScore:
- _objc_msgSend$_clearDeprecatedNotifications
- _objc_msgSend$_createBundlesFromGroupedEvents:
- _objc_msgSend$_getAppCalendarNotificationTrigger
- _objc_msgSend$_getFallbackPhotos:
- _objc_msgSend$_getNewTargetTimeToWriteEventBundlesWithCompletionHandler:
- _objc_msgSend$_getNextPossibleNotificationDateComponents
- _objc_msgSend$_groupBaseEvents:category:
- _objc_msgSend$_postTimeToWriteAppNotificationUsingTrigger:withCompletionHandler:
- _objc_msgSend$_rehydrateMotionActivity:handler:
- _objc_msgSend$_saveMediaPlayGroupsByDayTitle:handler:
- _objc_msgSend$_serviceSuggestionsNotificationsInternalForBundle:usingTrigger:useAppSchedule:completionHandler:
- _objc_msgSend$_suppressDuplicateMediaBundles:comparedWithActivitybundles:parameters:
- _objc_msgSend$_updateDeviceLocationsForMotionEvents:handler:
- _objc_msgSend$_updateMetaDataForRanking:forEvents:
- _objc_msgSend$createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:
- _objc_msgSend$createDominantBundleFromBundles:withParameters:
- _objc_msgSend$createMegaBundleFromBundles:parameters:
- _objc_msgSend$createOutingMegaBundleFromBundles:withParameters:isCoarseGranularity:
- _objc_msgSend$dateReferenceTagFromStartDate:endDate:nowDate:
- _objc_msgSend$dayOfWeekFromStartDate:endDate:
- _objc_msgSend$describeType
- _objc_msgSend$dominantPlaceNameFromEvents:
- _objc_msgSend$dominantPlaceNameFromEvents:countryMode:
- _objc_msgSend$filterMediaSessionsBasedOnApps:
- _objc_msgSend$generateBundleRanking:
- _objc_msgSend$getPlacesFromBundles:
- _objc_msgSend$getResourcesFromBundles:
- _objc_msgSend$initWithHour:minute:weekdays:
- _objc_msgSend$mergeOutingBundlesWithInDayWithGrouppedBundles:remainingSingletonBundles:parameters:isCoarseGranularity:
- _objc_msgSend$removePendingNotificationRequestsWithIdentifiers:
- _objc_msgSend$resourcesFromEvents:
- _objc_msgSend$serviceSuggestionsNotifications
- _objc_msgSend$timeFromDate:
- _objc_msgSend$timeFromStartDate:endDate:
- _objc_msgSend$timeOfDayPrefixFromBaseEvents:
- _unnamed_array_storage.1005
- _unnamed_array_storage.139
- _unnamed_array_storage.271
- _unnamed_array_storage.491
- _unnamed_array_storage.750
- _unnamed_array_storage.760
- _unnamed_array_storage.775
- _unnamed_array_storage.780
- _unnamed_array_storage.785
- _unnamed_array_storage.794
- _unnamed_array_storage.803
- _unnamed_array_storage.810
- _unnamed_array_storage.819
- _unnamed_array_storage.89
- _unnamed_array_storage.95
- _unnamed_array_storage.995
CStrings:
+ "\x01\x14"
+ "\v"
+ "\x17!\x1e"
+ "\x1b"
+ "\"%@\" %@ and %@. Take time to write today."
+ "%@ to %@"
+ "%@, TimeZone entry, keyword, %@, event.timeZone, %@ ADD"
+ "%@, TimeZoneManager.condensedRecords, %lu"
+ "%@, TimeZoneManager.timeZoneRecords, %lu"
+ "%@, bundle to delete, %@"
+ "%@, bundling startDate, %@, adjusted startDate, %@, endDate, %@"
+ "%@, bundling startDate, %@, adjusted startDate, %@, endDate, %@, refreshVariant, %@"
+ "%@, collect startDate, %@, adjusted startDate, %@, endDate, %@, refreshVariant, %@"
+ "%@, date %@, keyword, %@, timeZone, %@, source, interpolated"
+ "%@, date %@, keyword, %@, timeZone, %@, source, lookup"
+ "%@, date %@, keyword, %@, timeZone, %@, source, system"
+ "%@, existing event bundle idx, %lu, identifier, %@, startDate, %@, endDate, %@, bundling startDate candidate, %@, isCutExistingBundle, %@"
+ "%@, fetched photo memory bundle count, %lu, error, %@"
+ "%@, filter out ineligible interaction with phone number, %@"
+ "%@, poi, %@, timezone, %@"
+ "%@, purge deleted events, stay, %lu, deleted, %lu"
+ "%@, raw timeZone, date %@, keyword, %@, event.timeZone, %@"
+ "%@, request, %@, results count, %lu, error, %@, incorrect context in eventBundle, %@"
+ "%@, skip bundling due to no valid startDate!"
+ "%ld"
+ "%s, bundleHasFamilyOrFriendContact, %@, bundleHasCoworkerContact, %@"
+ "%s, media event inside daily media bundles filtered by first party play time ratio, ratio, %f, threshold, %f, media title, %@."
+ "%s, media event inside daily media bundles passed first party play time ratio, ratio, %f, threshold, %f, media title, %@."
+ "%s, media event inside mega bundle filtered by first party play time ratio, ratio, %f, threshold, %f, media title, %@."
+ "%s, media event inside mega bundle passed first party play time ratio, ratio, %f, threshold, %f, media title, %@."
+ "+1800"
+ "+1822"
+ "+1833"
+ "+1844"
+ "+1855"
+ "+1866"
+ "+1877"
+ "+1880"
+ "+1881"
+ "+1882"
+ "+1883"
+ "+1884"
+ "+1885"
+ "+1886"
+ "+1887"
+ "+1888"
+ "+1889"
+ "+1900"
+ "+1976"
+ "+[MOSummarizationUtilities updateRankMetaDataFrom:forSummaryBundle:]"
+ "-%@-%@"
+ "-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]"
+ "-[MONowPlayingMediaManager _fetchAppCateogryByBundleIds:]"
+ "-[MOTripAnnotationManager _filterPlaceUsingPredicates:]"
+ "-[MOTripAnnotationManager _updateMetaDataForRanking:forEvents:places:]"
+ "."
+ "/Library/Caches/com.apple.xbs/Sources/Moments/momentsd/PromptEngine/PromptSource/NowPlaying/MONowPlayingMediaManager.m"
+ "/System/Library/PrivateFrameworks/Moments.framework/LabelTemplates"
+ "1"
+ "800"
+ "822"
+ "833"
+ "844"
+ "855"
+ "866"
+ "877"
+ "880"
+ "881"
+ "882"
+ "883"
+ "884"
+ "885"
+ "886"
+ "887"
+ "888"
+ "889"
+ "900"
+ "976"
+ "<%@:%@>"
+ "<MOEvent eventIdentifier, %@, identifierFromProvider, %@, startDate, %@, endDate, %@, creationDate, %@, sourceCreationDate, %@, expirationDate, %@, timeZone, %@, provider, %@, category, %@, rehydrationFailCount, %lu, source app, %@, %@>"
+ "<MOEventBundle bundleIdentifier, %@, suggestionID, %@, startDate, %@, endDate, %@, creationDate, %@, localStartDate, %@, localEndDate, %@, source, %lu, interfaceType, %lu, photoSource, %lu, expirationDate, %@, filtered, %@, promptLanguage, %@, action, %@, concurrentMediaAction, %@, actions, %@, persons, %@, place, %@, time, %@, predominantWeather %@, aggregated and suppressed, %@, summarization granularity, %lu, places, %@, sub bundle IDs, %@, metaData.count, %lu,  events.count, %lu, labels, %@, prompts, %@, allResources, %@, meta, %lu, meta keywords, %@, metaDataForRank, %@, rankings, %@, suggestionEngagements, %@, suggestionEngagementViewCount, %lu, appEntryEngagementEvents %@,includedInSummaryBundleOnly, %@, bundleSubType, %lu, bundleSuperType, %lu>"
+ "<MOTime identifier, %@, timestamp, %f, timeString, %@, timeZone, %@, localTime, %@, timeTag, %lu, dateReferenceTag, %lu>"
+ "@\"MOTimeZoneManager\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"NSTimeZone\""
+ "@40@0:8d16d24d32"
+ "@48@0:8Q16@24q32@40"
+ "@52@0:8@16B24@28B36B40Q44"
+ "@60@0:8@16@24B32@36B44B48Q52"
+ "Accepted curated asset by properties, localIdentifier, %@, creationDate, %@, mediaType, %lu, mediaSubtypes, %lu, importProperties.importedBy, %lu"
+ "Adding asset, %@, location object is nil"
+ "Adding photo asset, %@, since distanceInMeters, %f is cleared"
+ "Aggregation for TimeContext: groupped bundle count: %lu, granularity: %lu"
+ "AllDayBeaconing"
+ "Already 2 notifications in the last week. Ineligible for new notification"
+ "App sourced notification posted for time to write, identifer: %@"
+ "Attempting to report MODiagnosticReporter incident but user is not onboarded in journal study. Skipping."
+ "BundleEventsDeepSummarizationPurgeEventBundles"
+ "Business"
+ "CA payload (%@) is nil. Skip submission"
+ "Catalogs"
+ "CoarseGranularityAggregation for TimeContext: bundle does not meet summarization criteria, bundle1: %@, bundle2: %@"
+ "CoarseGranularityAggregation for TimeContext: the last bundle in cluster start date, %@, end date, %@, bundle to be add to cluster: start date, %@, end date, %@"
+ "CoarseGranularityAggregation for TimeContext: two bundles should be merged for outing, bundle1: startDate:%@, endDate:%@, action:%@, place:%@, bundle 2: startDate:%@, endDate:%@, action:%@, place:%@"
+ "CoarseGranularityAggregation for TimeContext: two bundles should not merge since one of thme is covering more than one day, bundle1: start date, %@, end date, %@, bundle 2: start date, %@, end date, %@"
+ "CoarseGranularityAggregation for TimeContext:bundle goodness is too high to include into group."
+ "CoarseGranularityAggregation for TimeContext:bundle goodness score, %f"
+ "CoarseGranularityAggregation for TimeContext:bundle is for home or work so exclude from group."
+ "CoarseGranularityAggregation for contact: skip aggregation"
+ "CoarseGranularityAggregation: Filtered time context input eventBundles count, %lu"
+ "CoarseGranularityAggregation: distance between visits from two outing related bundles: %f (thres=%f)"
+ "CoarseGranularityAggregation: max goodness score deta between bundle and members in existing cluster: %f (thres=%f)"
+ "CoarseGranularityAggregation: time interval between visits from two outing related bundles: %f (thres=%f)"
+ "Current allowed sensed bundle count=%lu, total sensed bundle count in Recommended tab =%lu, minimum sensed bundle count threshold in Reocommended tab %lu"
+ "Current bundle subtype, %lu, acceptThreshold,%.3f, recommendThreshold, %.3f, recommendThresholdMultiplier, %.3f"
+ "Denied curated asset by properties, localIdentifier, %@, creationDate, %@, mediaType, %lu, mediaSubtypes, %lu, importProperties.importedBy, %lu"
+ "DiagnosticReporterIsOnboardedOnJournalStudy"
+ "DiagnosticReporterOverrideIsOnboardedOnJournalStudy"
+ "Education"
+ "EventBundleManagerBundleEventsDeepSummarizationPurgeEventBundles"
+ "Evergreen type is set to %@"
+ "Failure getting next notification service time"
+ "Fallback app repeating trigger scheduled, error: %@"
+ "Final assets for bundling count, %lu"
+ "Finance"
+ "FineGranularityAggregation for TimeContext: the last bundle in cluster start date, %@, end date, %@, bundle to be add to cluster: start date, %@, end date, %@"
+ "FineGranularityAggregation for TimeContext: two bundles should be merged for outing, bundle1: startDate:%@, endDate:%@, action:%@, place:%@, bundle 2: startDate:%@, endDate:%@, action:%@, place:%@"
+ "FineGranularityAggregation for TimeContext: two bundles should not merge since one of thme is covering more than one day, bundle1: start date, %@, end date, %@, bundle 2: start date, %@, end date, %@"
+ "FineGranularityAggregation for TimeContext:bundle goodness is too high to include into group."
+ "FineGranularityAggregation for TimeContext:bundle goodness score, %f"
+ "FineGranularityAggregation for TimeContext:bundle is for home or work so exclude from group."
+ "FineGranularityAggregation: Filtered time context input eventBundles count, %lu"
+ "FineGranularityAggregation: distance between visits from two outing related bundles: %f (thres=%f)"
+ "FineGranularityAggregation: max goodness score deta between bundle and members in existing cluster: %f (thres=%f)"
+ "FineGranularityAggregation: time interval between visits from two outing related bundles: %f (thres=%f)"
+ "Games"
+ "HealthAndFitness"
+ "Highlights from photos SPI after filtering by location and properties count, %lu"
+ "Highlights from photos SPI count, %lu"
+ "Ignoring PhotoKit asset, %@, location object is nil"
+ "Ignoring engagement for clientIdentifier: %@"
+ "Ineligible for unscheduled notification now"
+ "Input eventBundles count after filtered by isEligibleForSummarization: %lu."
+ "Input eventBundles count, %lu"
+ "Labeled all unrejected bundles to be shown on Recommended tab"
+ "Last notification was < holdoff period. Ineligible for new notification"
+ "Lifestyle"
+ "Localizable"
+ "Lookback window for notification start date, %@"
+ "Lookback window start date is after NOW, use default unscheduled lookback window instead, %@"
+ "MM/dd"
+ "MOMENTS_NOTIFICATION_TITLE"
+ "MOMediaPlayMetaDataKeyPlayerFirstPartyRatio"
+ "MOMediaPlayMetaDataKeyPlayerStartDate"
+ "MOMediaPlayMetrics"
+ "MOPhotoResourceLocalTime"
+ "MOSummarizationUtilities.m"
+ "MOTimeZoneManager"
+ "MOTripAnnotationManager.m"
+ "MediaPlayMetrics"
+ "Medical"
+ "Mind and Body Workout"
+ "MomentsUIService is foregrounded, notification will not be shown."
+ "NUM_MOMENTS_NOTIFICATION_FORMAT"
+ "Navigation"
+ "News"
+ "Newsstand"
+ "Next notification date: %@"
+ "No bundle available for the sheet"
+ "No bundles available for notification"
+ "No date components set for fallback notifications"
+ "Notification eligible bundle count: %lu"
+ "Notification scheduling complete, error: %@"
+ "Onboarding state unknown, skipping defaults write"
+ "Photo asset, %@, distanceInMeters, %f"
+ "Photo asset, %@, has already passed location check"
+ "Photo asset, %@, not added since distanceInMeters, %f is out of range"
+ "Photo asset, distanceInMeters is nil"
+ "PhotoAndVideo"
+ "Productivity"
+ "Q48@0:8@16@24@32@40"
+ "Recommendation threshold is set to rejection threshold, but still can't satisfy minimum suggestion count requirement (%lu). continue"
+ "Reference"
+ "Requesting settings change refresh"
+ "SETTINGS-CHANGE"
+ "Scheduled notification time out of week range."
+ "Scheduled notification time out of week range. dateInMinutes: %@"
+ "ScheduledRefreshNotificationService"
+ "Semaphore wait failed with context: %@"
+ "Sensed suggestion count in Recommended tab (%lu) is less than required (%lu). Setting lower recommended threshold %f "
+ "Settings change detected (first one), taking a transaction"
+ "Settings change detected (n=%i changes, n=%i transaction holds), scheduling refresh in %lf seconds"
+ "Settings change refresh completed, scheduling transaction release attempt in %lf seconds"
+ "Settings change refresh failed with error %@, scheduling transaction release attempt in %lf seconds"
+ "Settings change transaction release complete"
+ "Settings change transaction release deferred (n=%i transaction holds)"
+ "SettingsChange"
+ "Sheet is visible. Suppressing notification"
+ "SocialNetworking"
+ "Start to fetch category info with bundleIds, %@"
+ "Successfully fetched category name, %@, %@, %@"
+ "Summarization: Media bundle remove duplicate asset with key, %@, value, %@, title, %@"
+ "SummarizationUtilities: activity bundle goodness score, %f"
+ "SummarizationUtilities: bundle 1 with start date, %@, and bundle 2 with start date, %@,  are inside one day: %d"
+ "SummarizationUtilities: one of activity bundle goodness is too high. Stop creating weekly workout summary"
+ "SummarizationUtilities: places count: %lu, for bundle with start date, %@"
+ "Summarization_CoarseGranularityOutingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "Summarization_CoarseGranularityOutingBundlesExclusionGoodnessScoreThreshold"
+ "Summarization_FineGranularityOutingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "Summarization_FineGranularityOutingBundlesExclusionGoodnessScoreThreshold"
+ "Summarization_WeeklyActivitySummarySuppressionGoodnessScoreThreshold"
+ "Summary bundle distanceToHomeInMiles is NaN (in %s:%d)"
+ "Summary bundle distanceToHomeInMiles is negative (in %s:%d)"
+ "Summary bundle familiarity index is -1"
+ "System notification posted, error: %@"
+ "System notifications not authorized"
+ "T@\"MOEventBundleRanking\",&,N,V_eventBundleRanking"
+ "T@\"MOTimeZoneManager\",R,N,V_timeZoneManager"
+ "T@\"NSDictionary\",&,N,V_condensedRecords"
+ "T@\"NSDictionary\",&,N,V_timeZoneRecords"
+ "T@\"NSMutableDictionary\",R,N,V_bundleIdCategoryMappings"
+ "T@\"NSNumber\",&,N,V_mediaFirstPartyTimePlayedRatio"
+ "T@\"NSSet\",&,N,V_placeNames"
+ "T@\"NSSet\",&,N,V_workoutTypes"
+ "T@\"NSSet\",R,N,V_mediaBundleDeniedIdSet"
+ "T@\"NSSet\",R,N,V_thirdPartyMediaBundleIdSet"
+ "T@\"NSTimeZone\",&,N,V_timeZone"
+ "T@\"RTLocation\",R,N,V_homeLOI"
+ "TQ,R,N,V_interfaceType"
+ "Td,N,V_maximumFamiliarityIndex"
+ "Tf,N,V_coarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "Tf,N,V_coarseGranularity_outingBundlesExclusionGoodnessScoreThreshold"
+ "Tf,N,V_fineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "Tf,N,V_fineGranularity_outingBundlesExclusionGoodnessScoreThreshold"
+ "Tf,N,V_mediaBundleFirstPartyPlayTimePercentageThreshold"
+ "Tf,N,V_weeklyActivitySummary_suppressionGoodnessScoreThreshold"
+ "Ti,N,V_firstPartyAppRatio"
+ "Ti,N,V_firstPartyAppTime"
+ "Ti,N,V_musicAppTime"
+ "TimeContextAggregation (granularity=%lu): Input eventBundles count, %lu"
+ "TimeContextAggregation (granularity=%lu): Insufficient event bundles (<2). Skip summarization"
+ "TimeZone records:"
+ "Trip bundle distanceToHomeInMiles is NaN (in %s:%d)"
+ "Trip bundle distanceToHomeInMiles is negative (in %s:%d)"
+ "Trip bundle familiarity index is -1"
+ "Unique place set for visits:%@"
+ "Unique workout types set for activity:%@"
+ "UserNotificationOlderUnscheduledNotificationDate"
+ "UserNotificationRecentUnscheduledNotificationDate"
+ "UserNotificationScheduledGoodnessScoreThreshold"
+ "UserNotificationUnscheduledGoodnessScoreThreshold"
+ "Utilities"
+ "Visit bundle to %@ got suppressed from Recommended tab since it has the same place(s) with the other bundle with higher ranking score. Current uniquePlacesSet:%@"
+ "Workout bundle with %@ got suppressed from Recommended tab since it has the same workout type(s) with the other bundle with higher ranking score. Current uniqueworkouttypeset %@"
+ "Workout bundle with elapsed time %f got suppressed from Recommended tab since weekly workout summary is shown on Recommended tab"
+ "XPCRefreshNotificationService"
+ "You've scheduled time to write. Take a moment to reflect."
+ "_Moments_LocalizedStringForKey:withTable:"
+ "_assignPriorityScoreForPlace:MOPlace id is:%@, name is %@, priorityscore:%f, startdate:%@ enddate:%@"
+ "_assignPriorityScoreForPlace:placeInfoArray:"
+ "_bundleIdCategoryMappings"
+ "_calculateRankingScore:withMinRecommendedBundleCountRequirement:"
+ "_callLikeMechanismsSet"
+ "_coarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "_coarseGranularity_outingBundlesExclusionGoodnessScoreThreshold"
+ "_condensedRecords"
+ "_createBundlesFromEvents:"
+ "_dedupAssetForMediaBundle:nonPlayedMediaBudnles:isRecommendTab:"
+ "_eligibleInteraction:"
+ "_eventBundleRanking"
+ "_fetchAppCateogryByBundleIds:"
+ "_fetchSignificantLocationEnablementStatus"
+ "_filterMediaSessionsBasedOnFirstPartyApps:"
+ "_filterMediaSessionsBasedOnMusicApps:"
+ "_filterPlaceUsingPredicates:"
+ "_filterPlaceUsingPredicates: interestingPOIcategories is empty (in %s:%d)"
+ "_filterPlaceUsingPredicates:sorted array is %@ and start priority score is %lu"
+ "_fineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "_fineGranularity_outingBundlesExclusionGoodnessScoreThreshold"
+ "_firstPartyAppRatio"
+ "_firstPartyAppTime"
+ "_getArrayScheduledDateComponents"
+ "_getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:"
+ "_getNextNotificationDateComponentsWithOptions:afterDate:numWeeks:setComponents:"
+ "_getNextScheduledCalendarNotificationTrigger"
+ "_getPhotosByAssetProperties:UserLocations:MaxDistance:"
+ "_getSortedArrayScheduledDatesWithOptions:afterDate:numWeeks:setComponents:"
+ "_isOnboardedOnJournalStudy"
+ "_maximumFamiliarityIndex"
+ "_maximumGoodnessScoreDeltaFromBundle:toCluster:"
+ "_mediaBundleDeniedIdSet"
+ "_mediaBundleFirstPartyPlayTimePercentageThreshold"
+ "_mediaFirstPartyTimePlayedRatio"
+ "_musicAppTime"
+ "_placeNames"
+ "_rehydrateMotionActivity:forLocationSetting:handler:"
+ "_removeDuplicateFromResource:nonMediaKeySet:mediaOnRepeatDict:eventBundleDayKey:keyName:"
+ "_saveMediaPlayGroupsByDayTitle:startDate:handler:"
+ "_serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:"
+ "_serviceSuggestionsNotificationsTestForBundle:usingTrigger:useAppSchedule:completionHandler:"
+ "_settingsChangeCount"
+ "_settingsChangeTransaction"
+ "_settingsChangeTransactionHoldCount"
+ "_sheetIsVisible"
+ "_sortResourcesByPriorityScore:"
+ "_thirdPartyMediaBundleIdSet"
+ "_timeZoneManager"
+ "_timeZoneRecords"
+ "_tollFreeNumberPrefixes"
+ "_updateDeviceLocationsForMotionEvents:forLocationSetting:handler:"
+ "_updateMOPlacePriorityScore:priorityScore:handler:"
+ "_updateMetaDataForRanking:forEvents:places:"
+ "_weeklyActivitySummary_suppressionGoodnessScoreThreshold"
+ "_workoutTypes"
+ "addFinishBlock:"
+ "addPhotoResourcesWithDateArray:universe:handler:"
+ "attributes"
+ "auxiliary photo asset, %@, priority score, %f"
+ "bagForProfile:profileVersion:"
+ "bagSubProfile"
+ "bagSubProfileVersion"
+ "bmAbsoluteTime"
+ "build meta, time zone, %@, startDate, %@, localDate, %@"
+ "buildSimpleTimeTagIntervalsWithLeewayForDate:"
+ "bundleIdCategoryMappings"
+ "bundleSubType != %lu"
+ "coarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "coarseGranularity_outingBundlesExclusionGoodnessScoreThreshold"
+ "collec start or end date cannot be nil"
+ "com.apple.MomentsUIService"
+ "com.apple.frontboard.visibility"
+ "com.apple.momentsd.prompt-manager-fetch-test"
+ "com.apple.momentsd.settings-change"
+ "com.google.podcasts"
+ "com.webex.meeting"
+ "combineMediaResources:"
+ "combinePhotoResources:"
+ "componentsInTimeZone:fromDate:"
+ "condensedRecords"
+ "condensedRecordsFromRecords:"
+ "conversationTrend"
+ "createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:"
+ "createDominantBundleFromBundles:withParameters:timeZoneManager:"
+ "createMegaBundleFromBundles:parameters:timeZoneManager:"
+ "createOutingMegaBundleFromBundles:withParameters:isCoarseGranularity:timeZoneManager:"
+ "current placeNames:%@"
+ "current workoutTypes:%@"
+ "currentState"
+ "dateFormatFromTemplate:options:locale:"
+ "dateReferenceTagFromStartDate:endDate:nowDate:timeZone:"
+ "dateReferenceTagFromStartDate:endDate:timeZone:"
+ "date_referece_recency"
+ "date_referece_time_tag"
+ "dayOfWeekFromStartDate:endDate:timeZoneManager:"
+ "dominantPlaceNamesFromEvents:"
+ "dominantPlaceNamesFromEvents:countryMode:"
+ "double_dominant_places"
+ "endowmentNamespaces"
+ "eventBundleRanking"
+ "eventMediaFirstPartyTimePlayedRatio"
+ "extended event fetching start date from (%@) to (%@) with variant (%@)"
+ "f32@0:8@16@24"
+ "fail to fetch category info with error:%@"
+ "familyAndFriends"
+ "fetchCuratedPhotosFromHighlights, startDate, %@, endDate, %@"
+ "fetchPhotosBetweenStartDate, startDate, %@, endDate, %@, suggestionID, %@"
+ "fetchRoutineStateWithHandler:"
+ "fetched asset within timerange identifier, %@, creationDate, %@"
+ "fetching curated assets for highlight,%@, asset count is 0"
+ "fetching curated assets for highlight,%@, hit error, %@"
+ "fetching curated assets successful for highlight,%@,asset count,%lu"
+ "filterEventBundlesEligibleForSummarization:"
+ "filtered == YES"
+ "fineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold"
+ "fineGranularity_outingBundlesExclusionGoodnessScoreThreshold"
+ "firstPartyAppRatio"
+ "firstPartyAppTime"
+ "generateBundleRanking:withMinRecommendedBundleCountRequirement:"
+ "genreDisplayName"
+ "get notification schedule"
+ "getMomentsNotificationsSchedule"
+ "getPlacesFromBundles:forSummaryBundle:"
+ "getResourcesForOutingSummaryBundleWithWorkoutResources:photoResources:mediaResources:shouldUpLevelPhoto:"
+ "getResourcesForWeeklyWorkoutSummaryBundleWithWorkoutResources:photoResources:mediaResources:"
+ "getResourcesFromBundles:forSummaryBundle:"
+ "handleForPredicate:error:"
+ "hasWorkoutRoute:"
+ "initScheduleWithHour:minute:weekdays:"
+ "initWithAllowedCategories:dateInterval:ascending:limit:includeDeletedBundles:skipRanking:interfaceType:"
+ "initWithDateInterval:ascending:limit:includeDeletedBundles:skipRanking:interfaceType:"
+ "initWithFirstPartyAppRatio:firstPartyAppTime:musciAppTime:"
+ "initWithSuiteName:"
+ "initWithType:clientIdentifier:clientVersion:bag:"
+ "initWithURL:resolvingAgainstBaseURL:"
+ "intersectedActivityOrVisitForObject:other:"
+ "intersectedSubBundleIDForObject:other:"
+ "ios"
+ "isBundle:insideTheSameDayAsOtherBundle:"
+ "isBundleWithAssets:"
+ "isCoarseGranularitySummaryKey"
+ "isEligibleForSummarization"
+ "isEqualBasicPropertiesForObject:other:"
+ "isEqualToTimeZone:"
+ "isFirstPartyApp:"
+ "isPseudoDup"
+ "kEventDwellDuration"
+ "kMOContactAggregationManagerShouldAggregateBundlesForCoarseGranularity"
+ "kMOConversationAnnotationManagerMaximumInteractionInterval"
+ "kMOConversationAnnotationManagerMaximumOutgoingInteractionInterval"
+ "kMOConversationAnnotationManagerMinimumDurationDailyCall"
+ "kMOConversationAnnotationManagerMinimumDurationSingleCall"
+ "kMOConversationAnnotationManagerMinimumInteractionCount"
+ "kMOConversationAnnotationManagerMinimumOutgoingInteractionCount"
+ "kMOConversationAnnotationManagerMinimumPatternEventCount"
+ "kMOPlaceEndDate"
+ "kMOPlacePOICategory"
+ "kMOPlaceStartDate"
+ "kMOPlaceUUID"
+ "kMOTripAnnotationManagerMaximumFamiliarityIndexDefault"
+ "kMOTripAnnotationManagerMaximumFamiliarityIndexInternationalTrip"
+ "kPhotoCurationScore"
+ "kPhotoCurationScore != 0 AND (kEventDwellDuration < %f) AND NOT (kMOPlacePOICategory IN %@)"
+ "kPhotoCurationScore != 0 AND (kEventDwellDuration < %f) AND kMOPlacePOICategory IN %@"
+ "kPhotoCurationScore != 0 AND (kEventDwellDuration >= %f) AND NOT (kMOPlacePOICategory IN %@)"
+ "kPhotoCurationScore != 0 AND (kEventDwellDuration >= %f) AND kMOPlacePOICategory IN %@"
+ "kPhotoCurationScore == 0 AND (kEventDwellDuration < %f) AND NOT (kMOPlacePOICategory IN %@)"
+ "kPhotoCurationScore == 0 AND (kEventDwellDuration < %f) AND kMOPlacePOICategory IN %@"
+ "kPhotoCurationScore == 0 AND (kEventDwellDuration >= %f) AND NOT (kMOPlacePOICategory IN %@)"
+ "kPhotoCurationScore == 0 AND (kEventDwellDuration >= %f) AND kMOPlacePOICategory IN %@"
+ "key-value pair contains nil value (key=%@, value=%@). Skip dict update"
+ "keysSortedByValueUsingSelector:"
+ "keywordForDate:"
+ "localTime"
+ "localTime, object date, %@, object timezone, %@, system timezone, %@, timezone diff, %ld, adjusted date, %@"
+ "localTimeOfDate:timeZone:"
+ "localizedString:withTable:"
+ "maximumFamiliarityIndex"
+ "media asset from outing name, %@, priority score, %f"
+ "media asset from workout name, %@, priority score, %f"
+ "mediaBundleDeniedIdSet"
+ "mediaBundleFirstPartyPlayTimePercentageThreshold"
+ "mediaFirstPartyTimePlayedRatio"
+ "mergeOutingBundlesWithInDayWithGrouppedBundles:remainingSingletonBundles:parameters:isCoarseGranularity:timeZoneManager:"
+ "minSensedBundleCountInRecommendedTab"
+ "mind and body workout"
+ "musicAppTime"
+ "nextDateAfterDate:matchingComponents:options:"
+ "nextTriggerDate"
+ "no curated highlights fetched from photos"
+ "notification service complete, error: %@"
+ "numMediaAssetsResourcesNormalized"
+ "on %@"
+ "perform"
+ "placeNames"
+ "placeNamesSet"
+ "platformAttributes"
+ "postRefreshTriggerAfterSettingChange"
+ "predicateMatchingBundleIdentifier:"
+ "processTimeZoneEvents:"
+ "purgeDeletedEventBundlesWithCompletionHandler, startDate, %@, endDate, %@, results, %@, error, %@"
+ "purgeDeletedEventBundlesWithCompletionHandler:"
+ "queryItems"
+ "rankingDictionary.isEligibleForSummarization == %@"
+ "remaining photo asset, %@, priority score, %f"
+ "removeAllPendingNotificationRequests"
+ "removeDuplicateAssetsFromMediaBundle:"
+ "removeDuplicateWorkouts:"
+ "resourcesFromEvents:handler:"
+ "responseDataItems"
+ "richnessScoreScalingParameter"
+ "safeSavePropertyToDictionary:withKey:andValue:"
+ "scheduledDate, %@"
+ "scoreVisitBundleAssets:"
+ "secondary photo asset, %@, priority score, %f"
+ "secondsFromGMTForDate:"
+ "serviceSuggestionsNotificationsWithHandler:"
+ "setBundleIdentifiers:"
+ "setCoarseGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold:"
+ "setCoarseGranularity_outingBundlesExclusionGoodnessScoreThreshold:"
+ "setCondensedRecords:"
+ "setEventBundleRanking:"
+ "setFineGranularity_outingBundlesAggregationGoodnessScoreDeltaThreshold:"
+ "setFineGranularity_outingBundlesExclusionGoodnessScoreThreshold:"
+ "setFirstPartyAppRatio:"
+ "setFirstPartyAppTime:"
+ "setMaximumFamiliarityIndex:"
+ "setMediaBundleFirstPartyPlayTimePercentageThreshold:"
+ "setMediaFirstPartyTimePlayedRatio:"
+ "setMetaDataForTime:metaData:"
+ "setMusicAppTime:"
+ "setPlaceNames:"
+ "setQueryItems:"
+ "setTimeZoneRecords:"
+ "setWeeklyActivitySummary_suppressionGoodnessScoreThreshold:"
+ "setWorkoutTypes:"
+ "settingsChangePurge"
+ "setup notifications with schedule"
+ "setupFallbackAppBrandedNotificationsWithDateComponents:handler:"
+ "setupMomentsNotificationsWithSchedule"
+ "significant location disabled."
+ "sortedBundleByPhotoAssetsCount:"
+ "sortedWorkoutBundleByDuration:"
+ "startDate:%@, endDate:%@, action:%@, place:%@, rankingDict:%@"
+ "startDate:%@, endDate:%@, action:%@, placee:%@, rankingDict:%@"
+ "suggestionID:%@, subType:%lu, priorityScoreForResourceTypeDict:%@"
+ "summarizationThresholdForActivitySubTypeVariants"
+ "summarizationThresholdForVisitSubTypeVariants"
+ "systemTimeZone"
+ "taskState"
+ "thirdPartyMediaBundleIdSet"
+ "timeForDate:"
+ "timeForDate:timeZoneManager:"
+ "timeFromStartDate:endDate:timeZoneManager:"
+ "timeZone != nil"
+ "timeZone crossing, timeZone, %@, endTimeZone, %@"
+ "timeZone, date, %@, timeZone, %@, source, system"
+ "timeZone, date, %@, timeZone, %@, source, timeZoneManager, %@"
+ "timeZone, endDate, %@, timeZone, %@, source, system"
+ "timeZone, startDate, %@, timeZone, %@, source, system"
+ "timeZone, startDate, %@, timeZone, %@, source, timeZoneManager, %@"
+ "timeZoneAtDate:"
+ "timeZoneManager"
+ "timeZoneManager, %@, startDate, %@, endDate, %@, events, %lu"
+ "timeZoneObject"
+ "timeZoneRecords"
+ "timeZoneWithName:"
+ "timezone"
+ "trip manager (dominantPlaceNameFromEvents), place, %@, dwell, %f"
+ "trip manager (dominantPlaceNameFromEvents), the dominant name, %@, ratio, %f, the second name, %@, ratio, %f"
+ "trip manager (group is dropped), count, %lu, startDate, %@, endDate, %@, dwellTime, %f, familiarityIndex, %f"
+ "trip manager (new grouped travel), count, %lu, startDate, %@, endDate, %@, dwellTime, %f, familiarityIndex, %f"
+ "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8Q16"
+ "v28@0:8B16@?20"
+ "v48@?0@\"NSArray\"8Q16@\"NSDate\"24@\"NSDate\"32@\"NSArray\"40"
+ "vicinity_"
+ "weeklyActivitySummary_suppressionGoodnessScoreThreshold"
+ "whitespaceCharacterSet"
+ "workoutTrend"
+ "workoutTypes"
+ "workoutTypesSet"
+ "\xe2"
+ "\xf0\x922\x12"
- "\x14  "
- "\x16!\x1e"
- "\"%@\" %@ and %@ other moments. Take time to write today."
- "\"%@\" %@ and 1 other moment. Take time to write today."
- "+[MOContextAnnotationUtilities distanceFromHomeToCLLocation:universe:]"
- "+[MOContextAnnotationUtilities distanceFromHomeToLocation:universe:]"
- "-[MOEventBundleRanking _calculateRankingScore:]"
- "/AppleInternal/Library/PrivateFrameworks/Moments.framework/LabelTemplates"
- "/Library/Caches/com.apple.xbs/Sources/Moments/momentsd/PromptEngine/PromptProvider/MOContextAnnotationUtilities.m"
- "<MOEvent eventIdentifier, %@, identifierFromProvider, %@, startDate, %@, endDate, %@, creationDate, %@, sourceCreationDate, %@, expirationDate, %@, provider, %@, category, %@, rehydrationFailCount, %lu, source app, %@, %@>"
- "<MOEventBundle bundleIdentifier, %@, suggestionID, %@, startDate, %@, endDate, %@, creationDate, %@, source, %lu, interfaceType, %lu, photoSource, %lu, expirationDate, %@, filtered, %@, promptLanguage, %@, action, %@, concurrentMediaAction, %@, actions, %@, persons, %@, place, %@, time, %@, predominantWeather %@, aggregated and suppressed, %@, summarization granularity, %lu, places, %@, sub bundle IDs, %@, metaData.count, %lu,  events.count, %lu, labels, %@, prompts, %@, allResources, %@, meta, %lu, meta keywords, %@, metaDataForRank, %@, rankings, %@, suggestionEngagements, %@, suggestionEngagementViewCount, %lu, appEntryEngagementEvents %@,includedInSummaryBundleOnly, %@, bundleSubType, %lu, bundleSuperType, %lu>"
- "<MOTime identifier, %@, timestamp, %f, timeString, %@, timeZone, %@, timeTag, %lu, dateReferenceTag, %lu>"
- "App sourced notification posted for time to write"
- "CaptureCurrentDBFetchRanking"
- "Clearing old queued Moments notifications"
- "CoarseGranularity for TimeContext: two bundles should not merge since one of thme is covering more than one day, bundle1: start date, %@, end date, %@, bundle 2: start date, %@, end date, %@"
- "CoarseGranularityAggregation for TimeContext: two bundles should be merged for outing, bundle1: %@, bundle 2: %@"
- "CoarseGranularityAggregation: distance between visits from two outing related bundles: %f"
- "CoarseGranularityAggregation: time interval between visits from two outing related bundles: %f"
- "Current bundle subtype, %lu, acceptThreshold,%.3f, recommendThreshold, %.3f"
- "EventBundleManagerCaptureCurrentDBFetchRanking"
- "EventBundleManagerOverrideRefreshMinimumLookBackWindowHeavy"
- "EventManagerOverrideRefreshMinimumLookBackWindowHeavy"
- "Fallback highlights photos count,%lu"
- "FineGranularity for TimeContext: two bundles should not merge since one of thme is covering more than one day, bundle1: start date, %@, end date, %@, bundle 2: start date, %@, end date, %@"
- "FineGranularityAggregation for TimeContext: distance between visits from two outing related bundles: %f"
- "FineGranularityAggregation for TimeContext: groupped bundle count: %lu, granularity: %lu"
- "FineGranularityAggregation for TimeContext: time interval between visits from two outing related bundles: %f"
- "FineGranularityAggregation for TimeContext: two bundles should be merged for outing, bundle1: %@, bundle 2: %@"
- "HKWorkoutActivityTypeCycling"
- "HKWorkoutActivityTypeRunning"
- "HKWorkoutActivityTypeWalking"
- "Heavy"
- "Holdoff period not reached yet since last posted notification"
- "Ineligible for new notification"
- "Last notification was > holdoff period. Eligible for new notification"
- "Location filtered highlights photos count,%lu"
- "Mind and Body"
- "Missing user consent"
- "MomentsTask"
- "New Journaling Suggestion"
- "Not eligible for unscheduled notification, bundleCount: %lu"
- "Not implemented"
- "Photo asset,%@,adding photo as fallback - taken on front/back camera"
- "System notification posted with error: %@"
- "T@\"MONotificationsManager\",R,N,V_notificationsManager"
- "T@\"RTLocation\",&,N,V_homeLOI"
- "Take a moment to reflect and write in your journal."
- "Tf,N,V_FIDownRankThreshold"
- "Tf,N,V_callDurationThreshold"
- "Tf,N,V_distanceToHomeThreshold"
- "Tf,N,V_firstPartyPlayTimePercentageThreshold"
- "Tf,N,V_mediaPlayTimeThreshold"
- "Tf,N,V_shareCountThreshold"
- "Tf,N,V_timeAtHomeDurationThreshold"
- "Tf,N,V_workoutDurationThreshold"
- "Ti,N,V_burstyInteractionCountThreshold"
- "Ti,N,V_maxPeopleCountFromSocialContext"
- "Time to Write"
- "Total highlights asset count,%lu"
- "UserNotificationGoodnessScoreThreshold"
- "UserNotificationLastSentNotificationDate"
- "_FIDownRankThreshold"
- "_burstyInteractionCountThreshold"
- "_calculateRankingScore:"
- "_callDurationThreshold"
- "_clearDeprecatedNotifications"
- "_distanceToHomeThreshold"
- "_firstPartyPlayTimePercentageThreshold"
- "_getAppCalendarNotificationTrigger"
- "_getFallbackPhotos:"
- "_getNewTargetTimeToWriteEventBundlesWithCompletionHandler:"
- "_getNextPossibleNotificationDateComponents"
- "_maxPeopleCountFromSocialContext"
- "_mediaPlayTimeThreshold"
- "_postTimeToWriteAppNotificationUsingTrigger:withCompletionHandler:"
- "_rehydrateMotionActivity:handler:"
- "_saveMediaPlayGroupsByDayTitle:handler:"
- "_serviceSuggestionsNotificationsInternalForBundle:usingTrigger:useAppSchedule:completionHandler:"
- "_shareCountThreshold"
- "_timeAtHomeDurationThreshold"
- "_updateDeviceLocationsForMotionEvents:handler:"
- "_updateMetaDataForRanking:forEvents:"
- "_workoutDurationThreshold"
- "auxilliary"
- "begin"
- "createActivityMegaBundleFromBundles:withParameters:isCoarseGranularity:"
- "createDominantBundleFromBundles:withParameters:"
- "createMegaBundleFromBundles:parameters:"
- "createOutingMegaBundleFromBundles:withParameters:isCoarseGranularity:"
- "daily mediaPlaySession events filtered by first party play time ratio, first party count, %lu, all apps count, %lu, ratio, %f, threshold, %f, first party app time, %f, all apps time, %f."
- "daily mediaPlaySession events passed first party play time ratio, first party count, %lu, all apps count, %lu, ratio, %f, threshold, %f, first party app time, %f, all apps time, %f."
- "dateNowInMinutes: %@"
- "dateReferenceTagFromStartDate:endDate:nowDate:"
- "dayOfWeekFromStartDate:endDate:"
- "dominantPlaceNameFromEvents:"
- "dominantPlaceNameFromEvents:countryMode:"
- "end"
- "fetchCuratedPhotosFromHighlights,startDate,%@, endDate,%@"
- "fetchPhotosBetweenStartDate,startDate,%@,         endDate,%@,suggestionID,%@"
- "fetching curated assets successful,curatedAssets %@"
- "fetching curated assets, hit error, %@"
- "filterMediaSessionsBasedOnApps:"
- "firstPartyPlayTimePercentageThreshold"
- "found next scheduled time"
- "friend"
- "generateBundleRanking:"
- "getPlacesFromBundles:"
- "getResourcesFromBundles:"
- "mergeOutingBundlesWithInDayWithGrouppedBundles:remainingSingletonBundles:parameters:isCoarseGranularity:"
- "mind and body"
- "momentsUserNotification"
- "no curated photo inside the time range"
- "notifications not scheduled, reason: %@"
- "on %@/%@"
- "on (%@/%@ - %@/%@)"
- "removePendingNotificationRequestsWithIdentifiers:"
- "resourcesFromEvents:"
- "scheduledMinuteTime: %@"
- "serviceSuggestionsNotifications"
- "servicing user notifications"
- "setBurstyInteractionCountThreshold:"
- "setCallDurationThreshold:"
- "setDistanceToHomeThreshold:"
- "setFIDownRankThreshold:"
- "setFirstPartyPlayTimePercentageThreshold:"
- "setHomeLOI:"
- "setMaxPeopleCountFromSocialContext:"
- "setMediaPlayTimeThreshold:"
- "setShareCountThreshold:"
- "setTimeAtHomeDurationThreshold:"
- "setWorkoutDurationThreshold:"
- "task"
- "task-name"
- "timeFromDate:"
- "timetamp"
- "trip manager (dominantPlaceNameFromEvents), home country code is unknown"
- "trip manager (dominantPlaceNameFromEvents), the dominant name, %@, ratio, %f"
- "trip manager (new grouped travel), count, %lu, startDate, %@, endDate, %@, dwellTime, %f"
- "~"
- "\xb2"
- "\xf0\x922"

```
