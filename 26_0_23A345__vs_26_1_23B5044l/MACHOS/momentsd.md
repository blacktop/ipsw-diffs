## momentsd

> `/usr/libexec/momentsd`

```diff

-297.0.0.0.0
-  __TEXT.__text: 0x24ca00
-  __TEXT.__auth_stubs: 0x1ad0
-  __TEXT.__objc_stubs: 0x1d240
-  __TEXT.__objc_methlist: 0x111e0
-  __TEXT.__cstring: 0x267cf
-  __TEXT.__objc_classname: 0x1b58
-  __TEXT.__objc_methtype: 0x315e
-  __TEXT.__objc_methname: 0x36cf5
-  __TEXT.__oslogstring: 0x2f7fb
-  __TEXT.__const: 0x1231
-  __TEXT.__gcc_except_tab: 0x7f2c
+302.0.2.0.0
+  __TEXT.__text: 0x24e5b0
+  __TEXT.__auth_stubs: 0x1b10
+  __TEXT.__objc_stubs: 0x1d3c0
+  __TEXT.__objc_methlist: 0x112c0
+  __TEXT.__cstring: 0x261ef
+  __TEXT.__objc_classname: 0x1b66
+  __TEXT.__objc_methtype: 0x3182
+  __TEXT.__objc_methname: 0x36f0e
+  __TEXT.__oslogstring: 0x2f2db
+  __TEXT.__const: 0x1221
+  __TEXT.__gcc_except_tab: 0x7dac
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x5ec
   __TEXT.__swift5_typeref: 0x456
-  __TEXT.__swift5_reflstr: 0x149
   __TEXT.__swift5_fieldmd: 0x238
   __TEXT.__swift5_types: 0x3c
   __TEXT.__swift5_capture: 0x300
   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x4c
+  __TEXT.__swift5_reflstr: 0x149
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x4e58
+  __TEXT.__unwind_info: 0x4e90
   __TEXT.__eh_frame: 0xa68
-  __DATA_CONST.__auth_got: 0xd80
-  __DATA_CONST.__got: 0xba8
+  __DATA_CONST.__auth_got: 0xda0
+  __DATA_CONST.__got: 0xb88
   __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0xb4e0
-  __DATA_CONST.__cfstring: 0x258a0
+  __DATA_CONST.__const: 0xb6b0
+  __DATA_CONST.__cfstring: 0x24fc0
   __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_intobj: 0x3ea0
-  __DATA_CONST.__objc_arraydata: 0x16b0
-  __DATA_CONST.__objc_arrayobj: 0xac8
+  __DATA_CONST.__objc_intobj: 0x36c0
+  __DATA_CONST.__objc_arraydata: 0x14e0
+  __DATA_CONST.__objc_arrayobj: 0x9c0
+  __DATA_CONST.__objc_floatobj: 0x250
   __DATA_CONST.__objc_doubleobj: 0x4c0
   __DATA_CONST.__objc_dictobj: 0xf0
-  __DATA_CONST.__objc_floatobj: 0x250
-  __DATA.__objc_const: 0x1d2d0
-  __DATA.__objc_selrefs: 0x92c0
-  __DATA.__objc_ivar: 0x16cc
+  __DATA.__objc_const: 0x1d3c0
+  __DATA.__objc_selrefs: 0x9320
+  __DATA.__objc_ivar: 0x16e8
   __DATA.__objc_data: 0x55c0
   __DATA.__data: 0x18c8
   __DATA.__common: 0x2e4
-  __DATA.__bss: 0x3a0
+  __DATA.__bss: 0x3b0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4EFB8BD8-AFED-397E-B3FA-BBD2799B37BF
-  Functions: 8411
-  Symbols:   59668
-  CStrings:  20820
+  UUID: 5BAA4D25-CBB1-3E69-B593-D5105641AAD3
+  Functions: 8435
+  Symbols:   59852
+  CStrings:  20672
 
Symbols:
+ +[MOEngagementAndSuggestionAnalyticsParams analyticsSuggestionTypes]
+ +[MOEngagementAndSuggestionAnalyticsParams eventBundleVisibilityCategoryForUIForAnalyticsSuggestionUIVisibilityCategory:]
+ +[MOEngagementAndSuggestionAnalyticsParams isEventBundleSubType:mappedToAnalyticsSuggestionType:]
+ +[MOEngagementAndSuggestionAnalyticsParams sensedAnalyticsSuggestionTypes]
+ +[MOEngagementAndSuggestionAnalyticsParams suggestionUIVisibilityCategoriesExtended]
+ +[MOEngagementAndSuggestionAnalyticsParams suggestionUIVisibilityCategories]
+ +[MOPlatformInfo _createDefaultsManagerDaemon]
+ +[MOPlatformInfo _createDefaultsManagerDaemon].cold.1
+ +[MOPlatformInfo _getMainBundleIdentifier]
+ +[MOPlatformInfo _getMainBundleIdentifier].cold.1
+ -[MOCloudKitPushNotifications start]
+ -[MOCloudKitPushNotifications stop]
+ -[MOCloudKitPushNotifications subscribeWithSubscriptionID:completion:]
+ -[MOCloudKitPushNotifications unsubscribeWithSubscriptionID:completion:]
+ -[MOEngagementAndSuggestionAnalyticsManager _submitWeeklySuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]
+ -[MOEngagementAndSuggestionAnalyticsManager bundleHasPhotoOrMediaResources:]
+ -[MOEngagementAndSuggestionAnalyticsManager calculateAverageAgeInDaysForEventBundles:withSubmissionDate:]
+ -[MOEngagementAndSuggestionAnalyticsManager calculateMaxAgeInDaysForEventBundles:withSubmissionDate:]
+ -[MOEngagementAndSuggestionAnalyticsManager countActivityBundlesWithSameActionName:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithBirthdayLabel:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithHolidayLabel:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithPersons:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithResourceType:FromEventBudles:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithSamePersons:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithSamePlace:]
+ -[MOEngagementAndSuggestionAnalyticsManager countEventBundlesWithSamePlace:locationThreshold:]
+ -[MOEngagementAndSuggestionAnalyticsManager countRepetitiveOutingBundles:]
+ -[MOEngagementAndSuggestionAnalyticsManager countUniqueAnalyticsSuggestionTypesForEventBundles:]
+ -[MOEventBundleManager _expireOutdatedNotificationsWithHandler:]
+ -[MOEventBundleManager notificationCenter]
+ -[MOEventBundleManager setNotificationCenter:]
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ -[MOPlace(Comparison) _isString:equalToString:]
+ -[MOPlace(Comparison) isSimilarToPlace:]
+ -[MOPlace(Comparison) isSimilarToPlace:locationThreshold:]
+ -[MOPlace(Comparison) placeKey]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/momentsd.build/Objects-normal/arm64e/MOPlace+Comparison.o
+ GCC_except_table115
+ GCC_except_table137
+ GCC_except_table160
+ GCC_except_table174
+ GCC_except_table86
+ MOPlace+Comparison.m
+ OBJC_IVAR_$_MOCloudKitPushNotifications._actorQueue
+ OBJC_IVAR_$_MOCloudKitPushNotifications._apsTopics
+ OBJC_IVAR_$_MOCloudKitPushNotifications._isSubscribed
+ OBJC_IVAR_$_MOCloudKitPushNotifications._namedDelegatePort
+ OBJC_IVAR_$_MOCloudKitPushNotifications._notificationsResumed
+ OBJC_IVAR_$_MOCloudKitPushNotifications._started
+ OBJC_IVAR_$_MOCloudKitPushNotifications._subscriptionID
+ OBJC_IVAR_$_MOEventBundleManager._notificationCenter
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
+ _NSUserDefaultsDidChangeNotification
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.772
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774.cold.1
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.846
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.853
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.850
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.854
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.854.cold.1
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.311
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.313
+ __146-[MOEngagementAndSuggestionAnalyticsManager _submitWeeklySuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.262
+ __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.176
+ __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.191
+ __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.207
+ __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.211
+ __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.213
+ __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke_2.205
+ __185-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:andCompletionHandler:]_block_invoke.125
+ __189-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:submitDefaultMetrics:submitWeeklyRotationMetrics:WithOnboardingStatus:andCompletionResult:]_block_invoke.259
+ __189-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:submitDefaultMetrics:submitWeeklyRotationMetrics:WithOnboardingStatus:andCompletionResult:]_block_invoke.261
+ __35-[MOCloudKitPushNotifications stop]_block_invoke.18
+ __36-[MOCloudKitPushNotifications start]_block_invoke.16
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.424
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.424.cold.1
+ __48-[MODaemonUniverse(SetupServices) setupServices]_block_invoke.155
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.427
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.575
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.335
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337.cold.1
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.758
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.758.cold.1
+ __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.637
+ __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.639
+ __64-[MOEventBundleManager _expireOutdatedNotificationsWithHandler:]_block_invoke.952
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.672
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.680
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.683
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.340
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.352
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.357
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.361
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.362
+ __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.365
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.425
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.448
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.462
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.873
+ __70-[MOCloudKitPushNotifications subscribeWithSubscriptionID:completion:]_block_invoke.24
+ __70-[MOCloudKitPushNotifications subscribeWithSubscriptionID:completion:]_block_invoke.28
+ __70-[MOCloudKitPushNotifications subscribeWithSubscriptionID:completion:]_block_invoke.29
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.524
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.529
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.619
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.619.cold.1
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.620
+ __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.620.cold.1
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.389
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.390
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.394
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.398
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.738
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.738.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.739
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.739.cold.1
+ __72-[MOCloudKitPushNotifications unsubscribeWithSubscriptionID:completion:]_block_invoke.33
+ __72-[MOCloudKitPushNotifications unsubscribeWithSubscriptionID:completion:]_block_invoke.34
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.753
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.753.cold.1
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.907
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.908
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.914
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.926
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.928
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.933
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.937
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.941
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.942
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.927
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.929
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.929.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.785
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.785.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.789
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.789.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.796
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.796.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.800
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.800.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.801
+ __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.754
+ __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.754.cold.1
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.946
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.946.cold.1
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.946.cold.2
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.948
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.743
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.377
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.378
+ __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.385
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.711
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.715
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.719
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.729
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.730
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.758
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.477
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.478
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.485
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.487
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.495
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.499
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.503
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.507
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.874
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.874.cold.1
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.878
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.882
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.886
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.890
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.552
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.557
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.562
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.567
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.572
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.577
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.582
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.587
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.592
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.597
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.602
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.607
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.612
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.617
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.619
+ __OBJC_$_INSTANCE_METHODS_MOPlace(MOPlaceMO|Comparison)
+ ___146-[MOEngagementAndSuggestionAnalyticsManager _submitWeeklySuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke
+ ___146-[MOEngagementAndSuggestionAnalyticsManager _submitWeeklySuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke_2
+ ___35-[MOCloudKitPushNotifications stop]_block_invoke
+ ___35-[MOCloudKitPushNotifications stop]_block_invoke_2
+ ___35-[MOCloudKitPushNotifications stop]_block_invoke_3
+ ___36-[MOCloudKitPushNotifications start]_block_invoke
+ ___36-[MOCloudKitPushNotifications start]_block_invoke_2
+ ___42+[MOPlatformInfo _getMainBundleIdentifier]_block_invoke
+ ___46+[MOPlatformInfo _createDefaultsManagerDaemon]_block_invoke
+ ___64-[MOEventBundleManager _expireOutdatedNotificationsWithHandler:]_block_invoke
+ ___70-[MOCloudKitPushNotifications subscribeWithSubscriptionID:completion:]_block_invoke
+ ___72-[MOCloudKitPushNotifications unsubscribeWithSubscriptionID:completion:]_block_invoke
+ ___block_descriptor_32_e49_v32?0"NSString"8"CKSubscription"16"NSError"24l
+ ___block_descriptor_40_e40_B24?0"MOEventBundle"8"NSDictionary"16l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e24_v16?0"NSNotification"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e40_B24?0"MOEventBundle"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e29_v24?0"NSArray"8"NSError"16ls48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s64l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s56l8s72l8s64l8
+ __block_literal_global.180
+ __block_literal_global.27
+ __block_literal_global.284
+ __block_literal_global.32
+ __block_literal_global.333
+ __block_literal_global.41
+ __block_literal_global.580
+ __block_literal_global.585
+ __block_literal_global.678
+ __block_literal_global.685
+ __block_literal_global.702
+ __block_literal_global.742
+ __block_literal_global.76
+ __block_literal_global.806
+ __block_literal_global.811
+ __block_literal_global.813
+ __block_literal_global.920
+ _createDefaultsManagerDaemon.isMomentsDaemon
+ _createDefaultsManagerDaemon.onceToken
+ _dispatch_barrier_async
+ _dispatch_queue_create_with_target$V2
+ _dispatch_suspend
+ _getMainBundleIdentifier.bundleIdentifier
+ _getMainBundleIdentifier.onceToken
+ _kAnalyticsEventSuggestionPerformanceAggregatedMetrics
+ _kAnalyticsEventWeeklySuggestionPerformanceAggregatedMetrics
+ _kDefaultSameLocationThreshold
+ _kMOBundleActionMetadata
+ _kMOBundleDateReferenceTag
+ _kMOBundleTimeIdentifier
+ _kMOEngagementAndSuggestionAnalyticsParams_outingSuggestionWithSamePlaceCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_repetitiveActivitySuggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_repetitiveOutingSuggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_repetitiveTimeAtHomeSuggestionCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithBirthdayLabelCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithHolidayLabelCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithInviteCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithMediaCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithPersonsCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithPhotoCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_suggestionsWithStateOfMindLogCountKey
+ _kMOEngagementAndSuggestionAnalyticsParams_uniqueSensedSuggestionTypeCountKey
+ _kMONotifications_suggestionNotificationIdentifier
+ _kMOPhotoTraitAssociatedPersonLocalIdentifiers
+ _kMOPhotoTraitHolidayIdentifier
+ _kMOPhotoTraitLabelType
+ _kMOPhotoTraitMeaningIdentifier
+ _kMOThematicSummaryLabelWithMoreThanThreePersons
+ _objc_msgSend$_createDefaultsManagerDaemon
+ _objc_msgSend$_expireOutdatedNotificationsWithHandler:
+ _objc_msgSend$_getMainBundleIdentifier
+ _objc_msgSend$_isString:equalToString:
+ _objc_msgSend$_submitWeeklySuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$analyticsSuggestionTypes
+ _objc_msgSend$bundleHasPhotoOrMediaResources:
+ _objc_msgSend$calculateAverageAgeInDaysForEventBundles:withSubmissionDate:
+ _objc_msgSend$calculateMaxAgeInDaysForEventBundles:withSubmissionDate:
+ _objc_msgSend$content
+ _objc_msgSend$countActivityBundlesWithSameActionName:
+ _objc_msgSend$countEventBundlesWithBirthdayLabel:
+ _objc_msgSend$countEventBundlesWithHolidayLabel:
+ _objc_msgSend$countEventBundlesWithPersons:
+ _objc_msgSend$countEventBundlesWithResourceType:FromEventBudles:
+ _objc_msgSend$countEventBundlesWithSamePersons:
+ _objc_msgSend$countEventBundlesWithSamePlace:
+ _objc_msgSend$countEventBundlesWithSamePlace:locationThreshold:
+ _objc_msgSend$countRepetitiveOutingBundles:
+ _objc_msgSend$countUniqueAnalyticsSuggestionTypesForEventBundles:
+ _objc_msgSend$eventBundleVisibilityCategoryForUIForAnalyticsSuggestionUIVisibilityCategory:
+ _objc_msgSend$getDeliveredNotificationsWithCompletionHandler:
+ _objc_msgSend$isEventBundleSubType:mappedToAnalyticsSuggestionType:
+ _objc_msgSend$isSimilarToPlace:locationThreshold:
+ _objc_msgSend$notificationCenter
+ _objc_msgSend$pCountMaxNormalized
+ _objc_msgSend$pCountWeightedAverageNormalized
+ _objc_msgSend$pCountWeightedSumNormalized
+ _objc_msgSend$placeKey
+ _objc_msgSend$removeDeliveredNotificationsWithIdentifiers:
+ _objc_msgSend$request
+ _objc_msgSend$sensedAnalyticsSuggestionTypes
+ _objc_msgSend$setPCountMaxNormalized:
+ _objc_msgSend$setPCountWeightedAverageNormalized:
+ _objc_msgSend$setPCountWeightedSumNormalized:
+ _objc_msgSend$shutdown
+ _objc_msgSend$stop
+ _objc_msgSend$subscribeWithSubscriptionID:completion:
+ _objc_msgSend$suggestionUIVisibilityCategories
+ _objc_msgSend$suggestionUIVisibilityCategoriesExtended
+ _objc_msgSend$unsubscribeWithSubscriptionID:completion:
+ _objc_retain_x10
+ _onOnboardingStatusUpdate
- +[MOEngagementAndSuggestionAnalyticsParams bundleSubTypeToAnalyticsSuggestionTypeMap]
- +[MOEngagementAndSuggestionAnalyticsParams suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap]
- -[MOCloudKitPushNotifications subscribeWithSubscriptionID:]
- -[MOEventBundleRankingInput peopleCountMaxNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
- -[MONotificationsManager _clearAllNotifications]
- -[MONotificationsManager _clearAllNotifications].cold.1
- -[MONotificationsManager _getArrayScheduledDateComponents]
- -[MONotificationsManager _getArrayScheduledDateComponents].cold.1
- -[MONotificationsManager _getAuthorizationNotificationsError]
- -[MONotificationsManager _getCurrentApplicationIcon]
- -[MONotificationsManager _getGenericNotificationErrorWithReason:]
- -[MONotificationsManager _getMomentsFrameworkNotAvailableNotificationsError]
- -[MONotificationsManager _getNextNotificationDateComponentsWithOptions:afterDate:numWeeks:setComponents:]
- -[MONotificationsManager _getSortedArrayScheduledDatesWithOptions:afterDate:numWeeks:setComponents:]
- -[MONotificationsManager _userConsentCompleted]
- -[MONotificationsManager _usingAppSchedule]
- -[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]
- -[MOSignificantContactManager _conversationsFromInteractions:].cold.1
- -[MOSignificantContactManager _conversationsFromInteractions:].cold.2
- GCC_except_table156
- GCC_except_table84
- GCC_except_table99
- OBJC_IVAR_$_MOCloudKitPushNotifications._currentUser
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
- _$s8momentsd18MOAppCategoryUsageC13totalDurationSdvpACTK
- _$s8momentsd18MOAppCategoryUsageC13totalDurationSdvpACTk
- _$s8momentsd18MOAppCategoryUsageC8categorySSvpACTK
- _$s8momentsd18MOAppCategoryUsageC8categorySSvpACTk
- _OBJC_CLASS_$_UNCalendarNotificationTrigger
- _OBJC_CLASS_$_UNMutableNotificationContent
- _OBJC_CLASS_$_UNNotificationIcon
- _OBJC_CLASS_$_UNNotificationRequest
- _OBJC_CLASS_$_UNNotificationSound
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.775
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.777
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.777.cold.1
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.843
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.850
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.847
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.851
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.851.cold.1
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.316
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.317
- __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.200
- __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.215
- __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.231
- __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.235
- __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke.237
- __161-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:AndCompletionHandler:]_block_invoke_2.229
- __185-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:submitDefaultMetrics:submitWeeklyRotationMetrics:andCompletionHandler:]_block_invoke.129
- __189-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:submitDefaultMetrics:submitWeeklyRotationMetrics:WithOnboardingStatus:andCompletionResult:]_block_invoke.286
- __189-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:submitDefaultMetrics:submitWeeklyRotationMetrics:WithOnboardingStatus:andCompletionResult:]_block_invoke.288
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.427
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.427.cold.1
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.430
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.578
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.337
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.339
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.339.cold.1
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.15
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.20
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.25
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke.26
- __59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke_2.23
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.755
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.755.cold.1
- __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.683
- __61-[MONotificationsManager setUpNotificationTimerWithFireDate:]_block_invoke.685
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.669
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.677
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.680
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.339
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.351
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.355
- __66-[MOEventBundleManager bundleEventsWithRefreshVariant:andHandler:]_block_invoke.358
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.422
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.445
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.459
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.867
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.521
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.526
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.666
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.666.cold.1
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.667
- __70-[MONotificationsManager _generateAvailabilityPredictionsWithHandler:]_block_invoke.667.cold.1
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.383
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.384
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.391
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.395
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.735
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.735.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.736
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.736.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.750
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.750.cold.1
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.904
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.905
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.911
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.923
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.925
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.930
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.934
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.938
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.939
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.924
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.926
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.926.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.782
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.782.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.786
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.786.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.793
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.793.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.797
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.797.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.798
- __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.751
- __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.751.cold.1
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.943
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.943.cold.1
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.943.cold.2
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.945
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.740
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.371
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.372
- __84-[MOEventBundleManager _computeSensedBundleEngagementScoreParams:withRankingParams:]_block_invoke.379
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.706
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.706.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.710
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.710.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.717
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.718
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.722
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.732
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.733
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.605
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.605.cold.1
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.cold.1
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.cold.2
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.761
- __94-[MOThematicSummarizationManager generateThematicSummarizationBundles:withEmbeddings:handler:]_block_invoke.118
- __94-[MOThematicSummarizationManager generateThematicSummarizationBundles:withEmbeddings:handler:]_block_invoke.118.cold.1
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.474
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.475
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.482
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.484
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.492
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.496
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.500
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.504
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.871
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.871.cold.1
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.875
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.879
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.883
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.887
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.549
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.554
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.559
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.564
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.569
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.574
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.579
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.584
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.589
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.594
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.599
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.604
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.609
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.614
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.616
- __OBJC_$_INSTANCE_METHODS_MOPlace(MOPlaceMO)
- ___48-[MONotificationsManager _clearAllNotifications]_block_invoke
- ___59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke
- ___59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke_2
- ___59-[MOCloudKitPushNotifications subscribeWithSubscriptionID:]_block_invoke_3
- ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
- ___89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke
- ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
- ___block_descriptor_40_e8_32s_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e32_v24?0"CKRecordID"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e49_v32?0"NSString"8"CKSubscription"16"NSError"24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e11_v20?0B8q12ls48l8s32l8s40l8
- ___block_descriptor_60_e8_32bs40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8s64l8r72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s72l8s48l8s56l8s64l8
- __block_literal_global.204
- __block_literal_global.287
- __block_literal_global.335
- __block_literal_global.356
- __block_literal_global.583
- __block_literal_global.588
- __block_literal_global.672
- __block_literal_global.679
- __block_literal_global.699
- __block_literal_global.739
- __block_literal_global.803
- __block_literal_global.808
- __block_literal_global.810
- __block_literal_global.917
- _kMOBundleConcurrentMediaActionName
- _kMOThematicSummaryLabelWithMoreThanTwoContacts
- _objc_msgSend$_getArrayScheduledDateComponents
- _objc_msgSend$_getAuthorizationNotificationsError
- _objc_msgSend$_getCurrentAppDefaultActionURL
- _objc_msgSend$_getGenericNotificationErrorWithReason:
- _objc_msgSend$_getMomentsFrameworkNotAvailableNotificationsError
- _objc_msgSend$_getSortedArrayScheduledDatesWithOptions:afterDate:numWeeks:setComponents:
- _objc_msgSend$addNotificationRequest:withCompletionHandler:
- _objc_msgSend$bundleSubTypeToAnalyticsSuggestionTypeMap
- _objc_msgSend$defaultSound
- _objc_msgSend$fetchUserRecordIDWithCompletionHandler:
- _objc_msgSend$getPendingNotificationRequestsWithCompletionHandler:
- _objc_msgSend$iconForApplicationIdentifier:
- _objc_msgSend$localizedStringForKey:
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$recordName
- _objc_msgSend$removeAllPendingNotificationRequests
- _objc_msgSend$requestWithIdentifier:content:trigger:
- _objc_msgSend$setBody:
- _objc_msgSend$setDefaultActionURL:
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
- _objc_msgSend$setSound:
- _objc_msgSend$setTitle:
- _objc_msgSend$setWeekday:
- _objc_msgSend$subscribeWithSubscriptionID:
- _objc_msgSend$suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap
- _objc_msgSend$triggerWithDateMatchingComponents:repeats:
CStrings:
+ "%@|%@"
+ "B32@0:8@16d24"
+ "B32@0:8Q16Q24"
+ "Comparison"
+ "ERROR: Deleting iCloud Subscription: %@ %@"
+ "ERROR: Registering iCloud Notification: %@"
+ "EventBundleManagerExpireOldNotification"
+ "MOPushNotificationQueue_Notfication"
+ "Q32@0:8@16d24"
+ "Q32@0:8Q16@24"
+ "SignPostExpireOldNotification"
+ "Submitting weekly suggestion performance analytics to %@."
+ "Submitting weekly suggestion performance metric for %lu bundles."
+ "Submitting weekly suggestion performance metric for suggestionVisibilityCategory %@: bundleCount=%lu."
+ "Successfully deleted subscribed: %@"
+ "Successfully deregistered iCloud Notification"
+ "Suggestion perf analytics result was submitted: %{private}@"
+ "T@\"UNUserNotificationCenter\",&,N,V_notificationCenter"
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "User is not onboarded to JS, avoid timer setup."
+ "[MOCloudKitPushNotifications] Starting iCloud push notifications..."
+ "[MOCloudKitPushNotifications] Stopping iCloud push notifications..."
+ "[checkNotificationExpiration] Delivered notification count: %lu"
+ "[checkNotificationExpiration] No delivered suggestion notification"
+ "[checkNotificationExpiration] Notification is delivered for suggestionID: %@"
+ "[checkNotificationExpiration] Removing expired notification, suggestionID: %@"
+ "[checkNotificationExpiration] SuggestionID found: %@, uiVisibility: %@"
+ "[unsubscribeWithSubscriptionID] Not subscribed for: %@"
+ "_actorQueue"
+ "_apsTopics"
+ "_createDefaultsManagerDaemon"
+ "_expireOutdatedNotificationsWithHandler:"
+ "_getMainBundleIdentifier"
+ "_isString:equalToString:"
+ "_isSubscribed"
+ "_namedDelegatePort"
+ "_notificationCenter"
+ "_notificationsResumed"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "_started"
+ "_submitWeeklySuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:"
+ "_subscriptionID"
+ "addObserverForName:object:queue:usingBlock:"
+ "analyticsSuggestionTypes"
+ "bundleActionMetadata"
+ "bundleHasPhotoOrMediaResources:"
+ "bundleSuperType == %d"
+ "calculateAverageAgeInDaysForEventBundles:withSubmissionDate:"
+ "calculateMaxAgeInDaysForEventBundles:withSubmissionDate:"
+ "com.apple.Moments.WeeklySuggestionPerformanceAggregatedMetrics"
+ "content"
+ "countActivityBundlesWithSameActionName:"
+ "countEventBundlesWithBirthdayLabel:"
+ "countEventBundlesWithHolidayLabel:"
+ "countEventBundlesWithPersons:"
+ "countEventBundlesWithResourceType:FromEventBudles:"
+ "countEventBundlesWithSamePersons:"
+ "countEventBundlesWithSamePlace:"
+ "countEventBundlesWithSamePlace:locationThreshold:"
+ "countRepetitiveOutingBundles:"
+ "countUniqueAnalyticsSuggestionTypesForEventBundles:"
+ "eventBundleVisibilityCategoryForUIForAnalyticsSuggestionUIVisibilityCategory:"
+ "getDeliveredNotificationsWithCompletionHandler:"
+ "isEventBundleSubType:mappedToAnalyticsSuggestionType:"
+ "isSimilarToPlace:"
+ "isSimilarToPlace:locationThreshold:"
+ "moments-time-to-write"
+ "notificationCenter"
+ "outingSuggestionWithSamePlaceCount"
+ "placeKey"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "repetitiveActivitySuggestionCount"
+ "repetitiveOutingSuggestionCount"
+ "repetitiveTimeAtHomeSuggestionCount"
+ "request"
+ "sensedAnalyticsSuggestionTypes"
+ "setNotificationCenter:"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
+ "shutdown"
+ "stop"
+ "subscribeWithSubscriptionID:completion:"
+ "suggestionUIVisibilityCategories"
+ "suggestionUIVisibilityCategoriesExtended"
+ "suggestionsWithBirthdayLabelCount"
+ "suggestionsWithHolidayLabelCount"
+ "suggestionsWithInviteCount"
+ "suggestionsWithMediaCount"
+ "suggestionsWithPersonsCount"
+ "suggestionsWithPhotoCount"
+ "suggestionsWithStateOfMindLogCount"
+ "timeIdentifier"
+ "uniqueSensedSuggestionTypeCount"
+ "unsubscribeWithSubscriptionID:completion:"
+ "v16@?0@\"NSNotification\"8"
+ "weeklySuggestionAnalyticsPayloadCount"
+ "with_more_than_three_persons"
- " ---  Grouped Interactions Count  :%3lu"
- " ---  Received Interactions Count :%3lu"
- "#PhotoMemory,sortedasset,id,%d,asset,%@"
- "%@, idx, %lu, interaction, %@"
- "%s, media title, %@, event count, %lu"
- "(%f)"
- "@48@0:8Q16@24q32@40"
- "App branded notification unauthorized"
- "App sourced notification posted for time to write, identifer: %@"
- "CLLocation+MOExtensions.m"
- "Clearing Moments notifications"
- "DailyAnnotation: Event, %@"
- "Fallback app repeating trigger scheduled, error: %@"
- "Journal App notifications not authorized"
- "MOAction.m"
- "MOAggregationManager.m"
- "MOAnnotationManager.m"
- "MOBiomeManager.m"
- "MOBookmarkStore.m"
- "MOBundleClusteringManager.m"
- "MOContextAnnotationUtilities.m"
- "MOConversation.m"
- "MODaemonAnalyticsManager.m"
- "MODaemonClient.m"
- "MODaemonUniverse.m"
- "MODailyAnnotationManager.m"
- "MODataDumpFormatter.m"
- "MODefaultsManager.m"
- "MODictionaryEncoder.m"
- "MODictionaryTransformer.m"
- "MODominantBundleCreationManager.m"
- "MOEmbedding.m"
- "MOEngagementHistoryManager.m"
- "MOEvent.m"
- "MOEventBundle.m"
- "MOEventBundleLabelCondition.m"
- "MOEventBundleLabelFormat.m"
- "MOEventBundleLabelLocalizer.m"
- "MOEventBundleLabelTemplate.m"
- "MOEventBundleManager.m"
- "MOEventBundleRanking.m"
- "MOEventBundleStore.m"
- "MOEventBundler.m"
- "MOEventData.m"
- "MOEventExtendedAtrributes.m"
- "MOEventManager.m"
- "MOEventPatternDetector.m"
- "MOEventPatternDetectorFeatureTransformerAggregateEvents.m"
- "MOEventRefreshScheduler.m"
- "MOEventStore.m"
- "MOFSMStore.m"
- "MOGraph.m"
- "MOHealthKitManager.m"
- "MOInteraction+_CDInteraction.m"
- "MOInteraction.m"
- "MOLifeEventManager.m"
- "MOManageServer.m"
- "MOMeasurementTransformer.m"
- "MOMediaPlay.m"
- "MOMediaPlaySession.m"
- "MOMetric.m"
- "MOMotionManager.m"
- "MONotifier.m"
- "MONowPlayingMediaManager.m"
- "MOPOICategoryStore.m"
- "MOPeopleDiscoveryManager.m"
- "MOPersistenceManager.m"
- "MOPhotoManager.m"
- "MOPlace.m"
- "MOProactiveTravelManager.m"
- "MOPromptMetrics.m"
- "MORankingParams+CoreDataTransformable.m"
- "MORankingParamsMO+CoreDataClass.m"
- "MOResource.m"
- "MORoutineServiceManager.m"
- "MOSharedWithYouManager.m"
- "MOSignificantContactManager.m"
- "MOStringArrayTransformer.m"
- "MOSuggestedEventManager.m"
- "MOSummarizationParameters.m"
- "MOSummarizationUtilities.m"
- "MOTime.m"
- "MOTimeAtHomeParams.m"
- "MOTimeContextAnnotationManager.m"
- "MOTopicManager.m"
- "MOTrendBundler.m"
- "MOTrendsAnalyzerOptions.m"
- "MOTripAnnotationManager.m"
- "MOUserData.m"
- "MOXPCContext.m"
- "Media sessions grouped for title and day: %@"
- "Moments Framework not available"
- "Next notification date: %@"
- "No date components set for fallback notifications"
- "No set scheduled stored"
- "PlatformInfoOverrideIsSeedBuild"
- "Soft link Moments framework skipped"
- "TTW notifications allowed=%u"
- "Take a moment to reflect in your journal."
- "Tf,N,V_peopleCountMaxNormalized"
- "Tf,N,V_peopleCountWeightedAverageNormalized"
- "Tf,N,V_peopleCountWeightedSumNormalized"
- "Time to Write"
- "TitleAndDayGrouping: media session with description: %@"
- "UserNotification getPendingNotificationRequest timed-out for analytics"
- "UserNotificationLastScheduledOpportunisticPostingDate"
- "UserNotificationRecentUnscheduledNotificationDate"
- "UserNotificationScheduleInMinutesArray"
- "["
- "[generateThematicSummarizationBundles] bundle subtype=%lu, subbundlecount=%lu, phenotypes=%{private}@"
- "[subscribeWithSubscriptionID] Already subscribing, skipping..."
- "]"
- "_clearAllNotifications"
- "_currentUser"
- "_getArrayScheduledDateComponents"
- "_getAuthorizationNotificationsError"
- "_getCurrentApplicationIcon"
- "_getGenericNotificationErrorWithReason:"
- "_getMomentsFrameworkNotAvailableNotificationsError"
- "_getNextNotificationDateComponentsWithOptions:afterDate:numWeeks:setComponents:"
- "_getSortedArrayScheduledDatesWithOptions:afterDate:numWeeks:setComponents:"
- "_peopleCountMaxNormalized"
- "_peopleCountWeightedAverageNormalized"
- "_peopleCountWeightedSumNormalized"
- "_userConsentCompleted"
- "_usingAppSchedule"
- "addNotificationRequest:withCompletionHandler:"
- "appTimeToWrite"
- "bundleConcurrentMediaActionName"
- "defaultSound"
- "fetchUserRecordIDWithCompletionHandler:"
- "getPendingNotificationRequestsWithCompletionHandler:"
- "iconForApplicationIdentifier:"
- "label confidence, label confidence score, %f, actionNameConfidence, %f, concurrentMediaActionNameConfidence, %f, backgroundActionNameConfidence, %@, placeNameConfidence, %f, bundle, %@"
- "label confidence, label confidence, %f, event bundle, %@"
- "localizedStringForKey:"
- "new conversation created for compound key: %@, for date %@, interaction count, %lu"
- "peopleCountMaxNormalized"
- "peopleCountWeightedAverageNormalized"
- "peopleCountWeightedSumNormalized"
- "recordName"
- "removeAllPendingNotificationRequests"
- "requestWithIdentifier:content:trigger:"
- "scheduledDate, %@"
- "setBody:"
- "setDefaultActionURL:"
- "setPeopleCountMaxNormalized:"
- "setPeopleCountWeightedAverageNormalized:"
- "setPeopleCountWeightedSumNormalized:"
- "setSound:"
- "setupFallbackAppBrandedNotificationsWithDateComponents:handler:"
- "skipping fetching and rehydrating contact events"
- "skipping fetching and rehydrating life events"
- "skipping fetching and rehydrating music"
- "skipping fetching and rehydrating people density events"
- "skipping fetching and rehydrating photo memory"
- "skipping fetching and rehydrating prox"
- "skipping fetching and rehydrating state of mind"
- "skipping fetching and rehydrating workouts"
- "skipping fetching and saving motion events"
- "skipping fetching and saving screentime events"
- "skipping fetching and saving spotlight events"
- "skipping training, fetching and rehydrating visits"
- "spotlight event integration enablement param is set to %d"
- "start fetching and rehydrating contact events"
- "start fetching and rehydrating life events"
- "start fetching and rehydrating motion events"
- "start fetching and rehydrating music"
- "start fetching and rehydrating people density events"
- "start fetching and rehydrating photo memory"
- "start fetching and rehydrating prox"
- "start fetching and rehydrating screentime events"
- "start fetching and rehydrating spotlight events"
- "start fetching and rehydrating state of mind data"
- "start fetching and rehydrating workouts"
- "start training, fetching and rehydrating visits"
- "subscribeWithSubscriptionID:"
- "suggestionUIVisibilityCategoryToMOEventBundleVisibilityCategoryForUIMap"
- "triggerWithDateMatchingComponents:repeats:"
- "v24@?0@\"CKRecordID\"8@\"NSError\"16"
- "with_more_than_two_contacts"

```
