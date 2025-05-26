## momentsd

> `/usr/libexec/momentsd`

```diff

-127.0.51.0.0
-  __TEXT.__text: 0x1af3c4
-  __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_stubs: 0x161e0
-  __TEXT.__objc_methlist: 0xbcac
+127.0.55.0.0
+  __TEXT.__text: 0x1b076c
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_stubs: 0x16240
+  __TEXT.__objc_methlist: 0xbccc
   __TEXT.__objc_classname: 0x1528
-  __TEXT.__objc_methname: 0x23ccd
+  __TEXT.__objc_methname: 0x23d37
   __TEXT.__objc_methtype: 0x23c2
-  __TEXT.__cstring: 0x1cd64
-  __TEXT.__oslogstring: 0x1ff41
+  __TEXT.__cstring: 0x1cdc4
+  __TEXT.__oslogstring: 0x2085a
   __TEXT.__const: 0x7d2
-  __TEXT.__gcc_except_tab: 0x4e2c
+  __TEXT.__gcc_except_tab: 0x4e20
   __TEXT.__ustring: 0x124
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x118

   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_reflstr: 0x30
-  __TEXT.__unwind_info: 0x3964
+  __TEXT.__unwind_info: 0x3958
   __TEXT.__eh_frame: 0x270
-  __DATA_CONST.__auth_got: 0x860
+  __DATA_CONST.__auth_got: 0x880
   __DATA_CONST.__got: 0x2e0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x77c8
-  __DATA_CONST.__cfstring: 0x1cc60
+  __DATA_CONST.__const: 0x77f0
+  __DATA_CONST.__cfstring: 0x1cd60
   __DATA_CONST.__objc_classlist: 0x5a8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xd8

   __DATA_CONST.__objc_doubleobj: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA.__objc_const: 0x15450
-  __DATA.__objc_selrefs: 0x6848
+  __DATA.__objc_selrefs: 0x6860
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x978
   __DATA.__objc_superrefs: 0x4a8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6156
-  Symbols:   43661
-  CStrings:  11698
+  Functions: 6158
+  Symbols:   43680
+  CStrings:  11730
 
Symbols:
+ +[MOEventBundleMetaDataUtility setMetaDataForTime:startDate:endDate:metaData:].cold.1
+ -[MODaemonClient scheduleInternalClientTask:withName:]
+ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:].cold.4
+ -[MOEventBundleRanking initWithConfigurationManager:].cold.3
+ -[MOEventBundleRanking initWithConfigurationManager:].cold.4
+ -[MORoutineServiceManager _fetchEarliestVisitDateInRoutineWithHandler:]
+ GCC_except_table111
+ GCC_except_table117
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table133
+ GCC_except_table138
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table53
+ GCC_except_table72
+ GCC_except_table80
+ GCC_except_table90
+ __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.501
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.421
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.421.cold.1
+ __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.423
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.383
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.389.cold.1
+ __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.390
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1168
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1170
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1170.cold.1
+ __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.571
+ __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.207
+ __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.215
+ __71-[MORoutineServiceManager _fetchEarliestVisitDateInRoutineWithHandler:]_block_invoke.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1121.cold.1
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.446
+ __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.446.cold.1
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1156
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke_2
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke_3
+ ___70-[MORoutineServiceManager fetchEarliestVisitDateInRoutineWithHandler:]_block_invoke_2
+ ___71-[MORoutineServiceManager _fetchEarliestVisitDateInRoutineWithHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSDate"8"NSError"16ls32l8
+ ___block_descriptor_80_e8_32s40bs48r56r64r_e5_v8?0lr48l8s40l8r56l8s32l8r64l8
+ ___error
+ _getrlimit
+ _objc_msgSend$_fetchEarliestVisitDateInRoutineWithHandler:
+ _objc_msgSend$removeObjectsAtIndexes:
+ _objc_msgSend$scheduleInternalClientTask:withName:
+ _setrlimit
+ _strerror
+ _unnamed_array_storage.1110
+ _unnamed_array_storage.1133
+ _unnamed_array_storage.1139
+ main.cold.3
+ main.cold.4
- -[MODaemonClient softRefreshEventsWithContext:andRefreshVariant:andHandler:].cold.1
- -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.5
- -[MOEventBundleRanking _checkAndUpdateNumericLimits:].cold.1
- -[MOEventBundleRanking _checkAndUpdateNumericLimits:].cold.2
- -[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:].cold.3
- -[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:].cold.4
- -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:].cold.1
- -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:].cold.2
- -[MOEventBundleRanking generateBundleRanking:withMinRecommendedBundleCountRequirement:].cold.3
- GCC_except_table110
- GCC_except_table116
- GCC_except_table120
- GCC_except_table124
- GCC_except_table132
- GCC_except_table149
- GCC_except_table152
- GCC_except_table155
- GCC_except_table158
- GCC_except_table161
- GCC_except_table164
- GCC_except_table19
- GCC_except_table41
- GCC_except_table58
- GCC_except_table71
- GCC_except_table78
- GCC_except_table89
- __101-[MONotificationsManager _getNewTargetTimeToWriteEventBundlesUsingAppSchedule:withCompletionHandler:]_block_invoke.500
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.420
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.420.cold.1
- __101-[MONotificationsManager _serviceSuggestionsNotificationsEnablingTest:withOptions:completionHandler:]_block_invoke.422
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.382
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.388
- __112-[MONotificationsManager _serviceSuggestionsNotificationsInternalUsingTrigger:useAppSchedule:completionHandler:]_block_invoke.388.cold.1
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1169
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1171
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1171.cold.1
- __125-[MONotificationsManager _postTimeToWriteSystemNotificationUsingEventBundles:withTrigger:usingAppSchedule:completionHandler:]_block_invoke.552
- __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.938
- __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.939
- __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.201
- __68-[MOEventBundleStore fetchEventBundleWithOptions:CompletionHandler:]_block_invoke.209
- __70-[MORoutineServiceManager fetchEarliestVisitDateInRoutineWithHandler:]_block_invoke.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1115
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1122.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1123
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.445
- __89-[MONotificationsManager setupFallbackAppBrandedNotificationsWithDateComponents:handler:]_block_invoke.445.cold.1
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1157
- ___block_descriptor_72_e8_32s40bs48r56r64r_e5_v8?0lr48l8s40l8r56l8s32l8r64l8
- _unnamed_array_storage.1111
- _unnamed_array_storage.1134
- _unnamed_array_storage.1140
CStrings:
+ "%@, discard event for visit with wrong start/end date, event, %@ "
+ "%@, discard event with wrong start/end date, event, %@ "
+ "Aggregation for TimeContext: no chance of overlapping so create summary bundles for both outing groups and activity groups"
+ "Aggregation for TimeContext: not all activity mega intervals are looped through, stopping at %d, granularity, %lu"
+ "Aggregation for TimeContext: not all outing mega intervals are looped through, stopping at %d, granularity, %lu"
+ "Attempting softRefresh"
+ "Bundle got rejected since it shares suggestionID(%@) or bundleID(%@) with the other bundle with higher ranking score: %.3f"
+ "Bundle index %lu, BundleID %@, suggestionID %@"
+ "Coarse summary suggestion got rejected due: bundleID %@, suggestionID %@ isBundleOrSubBundlesSelectedOrQuickAdded %d, suppressCoarseSummary %d"
+ "Contact bundle got suppressed from Recommended tab since it shares the same contact id(s) with the other bundle with higher ranking score. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Contact was suppressed from Recent tab since there is a visible suggestion with same contactID in the hold off period. SuggestionID:%@, BundleID:%@, startDate:%@,subType:%@"
+ "Contact/Contact trend suggestion was dismissed from Recommended tab because elapsed time >%.2f days or it was already engaged: bundleID %@, suggestionID %@ elapsedTime %.2f isBundleOrSubBundlesSelectedOrQuickAdded %d"
+ "Eligible to run soft refresh"
+ "Evergreen bundle got rejected since it is the same type as the other evergreen bundle: suggestionID %@ bundleID %@"
+ "Evergreen suggestion got rejected because prompt doesn't exist: bundleID %@, suggestionID %@"
+ "Fine granularity summary suggestion was dismissed from Recommended tab since it was engaged: bundleID %@, suggestionID %@"
+ "Fine granularity summary suggestion was set to present on Recommended tab to enrich Recommended tab: bundleID %@, suggestionID %@"
+ "Fine granularity summary suggestion was set to present only in Recent tab: bundleID %@, suggestionID %@"
+ "Initial No. file rlimits %u ~ %u"
+ "Input bundle count after nil ID filters: %lu"
+ "Input bundle count: %lu, minimumRecommendedBundleRequired:%d"
+ "Internal Client Task Scheduled [%@]"
+ "Internal Client Task Started [%@]"
+ "Internal media bundle got rejected: bundleID %@, suggestionID %@"
+ "Label potentially contains eng text: %@"
+ "Mismatch between bundle count %lu and score array count %lu (in %s:%d)"
+ "Ordinal rank %lu:  SuggestionID:%@, bundleID:%@"
+ "Outing suggestion was rejected because it was either work or short visit (or both) without any photo: bundleID %@, suggestionID %@ isWorkVisit %d isShortVisit %d"
+ "Phone sensed bundle got suppressed from Recommended tab since it shared the same place(s) with more highly ranked bundle and it does not have any photo. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Phone-sensed walk or outing bundle was suppressed from Recent tab since it shares the same place(s) with other bundle(s) with higher goodness score from the same day. SuggestionID:%@, BundleID:%@, startDate:%@,subType:%@"
+ "Phone-sensed walk with no location was suppressed from Recent tab since there is other unsuppressed walking suggestion with higher goodness score. SuggestionID:%@, BundleID:%@, startDate:%@"
+ "Phone-sensed walking bundle got suppressed from Recommended tab since it has the same workout type(s) with the other bundle with higher ranking score. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Phone-sensed walking with no destination or photo got suppressed from Recent tab since richer walking bundle was found in the same day. SuggestionID:%@, BundleID:%@, startDate:%@"
+ "Photo Memory suggestion got rejected due to engagement signal: bundleID %@, suggestionID %@"
+ "RankingDict %@"
+ "Submitted ranking CA message"
+ "Suggestion was dismissed from Recommended tab since it's selected/quick added: bundleID %@, suggestionID %@"
+ "Suggestion was rejected because it/its sub bundle was deleted: bundleID %@, suggestionID %@"
+ "Suggestion was rejected due to goodness score: bundleID %@, suggestionID %@ goodnessScore %.3f suggestionRecommendThreshold %.3f suggestionAcceptThreshold %.3f subtype %lu"
+ "Suggestion was rejected due to isBundleAggregated label: bundleID %@, suggestionID %@ summarizationGranularity %lu"
+ "Suggestion was rejected to goodness score: bundleID %@, suggestionID %@ goodnessScore %.3f suggestionRecommendThreshold %.3f suggestionAcceptThreshold %.3f"
+ "Suggestion was set to present only in Recent tab due to goodness score: bundleID %@, suggestionID %@ goodnessScore %.3f suggestionRecommendThreshold %.3f suggestionAcceptThreshold %.3f"
+ "Unable to getrlimit: [%i] %s"
+ "Unable to setrlimit: [%i] %s"
+ "Visit bundle got suppressed from Recommended tab since it shared the same place(s) with more highly ranked bundle. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Weekly summary bundle got suppressed from Recommended tab since workout routine with the same workout types exists. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Workout bundle got suppressed from Recommended tab since it has the same workout type(s) with the other bundle with higher ranking score. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Workout bundle got suppressed from Recommended tab since weekly workout summary is shown on Recommended tab. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "Workout routine suggestion was rejected because elapsed time >%.2f days or it was already engaged: bundleID %@, suggestionID %@ elapsedTime %.2f isBundleOrSubBundlesSelectedOrQuickAdded %d"
+ "_fetchEarliestVisitDateInRoutineWithHandler:"
+ "build meta, time zone, %@, endDate, %@, localDate, %@"
+ "bundle with nil bundleID or nil suggestionID was filtered out: bundleID %@ suggestionID %@"
+ "bundleIdentifier!=nil"
+ "removeObjectsAtIndexes:"
+ "scheduleInternalClientTask:withName:"
+ "setMetaDataForTime, startDate, %@, endDate, %@, the timestamps are inverted after snapping."
+ "setMetaDataForTime, startDate, %@, endDate, %@, the timestamps are inverted after time zone shifting."
+ "setMetaDataForTime, startDate, %@, endDate, %@, the timestamps are inverted at the end"
+ "suggestionID!=nil"
+ "typeOfDayTagFromStartDate, startDate, %@, endDate, %@, timeZone, %@, the timestamps are inverted after time zone shifting."
+ "typeOfDayTagFromStartDate, startDate, %@, endDate, %@, timeZone, %@, the timestamps are inverted."
+ "{action"
+ "{city"
+ "{date_"
+ "{place"
+ "{time}"
+ "{unique_"
- "Bundle got rejected since it shares suggestionID(%@) or bundleID(%@) with the other bundle with higher ranking score: %@"
- "Bundle index %lu, BundleID %@, suggestionID %@: ranking= %@"
- "Contact bundle got suppressed from Recommended tab since it shares the same contact id(s) with the other bundle with higher ranking score. SuggestionID:%@, bundleID:%@, startDate:%@, workoutType(s):%@"
- "Contact was suppressed from Recent tab since there is a visible suggestion with same contactID in the hold off period. SuggestionID:%@, BundleID:%@, startDate:%@,subType:%@, contactID:%@"
- "Count of bundles for ranking %lu"
- "Count of ranking input %lu"
- "Count of ranking score %lu"
- "Evergreen bundle got rejected since it is the same type as the other evergreen bundle: %@"
- "Evergreen engagement scores are initialized to %@"
- "Mismatch between bundle size, %lu and score array, %lu (in %s:%d)"
- "Ordinal rank %lu: ranking Dict=%@"
- "Phone sensed bundle got suppressed from Recommended tab since it shared the same place(s) with more highly ranked bundle and it does not have any photo. SuggestionID:%@, bundleID:%@, startDate:%@, place(s):%@"
- "Phone-sensed walk or outing bundle was suppressed from Recent tab since it shares the same place(s) with other bundle(s) with higher goodness score from the same day. SuggestionID:%@, BundleID:%@, startDate:%@,subType:%@, places:%@"
- "Phone-sensed walking bundle got suppressed from Recommended tab since it has the same workout type(s) with the other bundle with higher ranking score. SuggestionID:%@, bundleID:%@, startDate:%@, workoutType(s):%@"
- "Phone-sensed walking with no destination or photo got suppressed from Recent tab since richer walking bundle was found in the same day. SuggestionID:%@, BundleID:%@, startDate:%@, places:%@"
- "Phone-sensed walking with no location was suppressed from Recent tab since there is other unsuppressed walking suggestion with higher goodness score. SuggestionID:%@, BundleID:%@, startDate:%@, places:%@"
- "Submitted coreAnalytics messages: %@"
- "Visit bundle got suppressed from Recommended tab since it shared the same place(s) with more highly ranked bundle. SuggestionID:%@, bundleID:%@, startDate:%@, place(s):%@"
- "Weekly summary bundle got suppressed from Recommended tab since workout routine with the same workout types exists. SuggestionID:%@, bundleID:%@, startDate:%@, workoutType(s):%@"
- "Workout bundle got suppressed from Recommended tab since it has the same workout type(s) with the other bundle with higher ranking score. SuggestionID:%@, bundleID:%@, startDate:%@, workoutType(s):%@"
- "Workout bundle got suppressed from Recommended tab since weekly workout summary is shown on Recommended tab. SuggestionID:%@, bundleID:%@, startDate:%@, workoutType(s):%@"
- "Writing contactIdentifiers: BundleID %@, suggesetionID %@, allContactIdentifiers %@,"
- "Writing placeNames: BundleID %@, suggesetionID %@, allPlaceNames %@,"
- "callDurationFeatureNormalized:%f, burstyInteractionCountFeatureNormalized:%f, multipleInteractionTypesFeature:%d, isFamilyContact:%f, isCoworkerContact:%f, isRepetitiveContact:%d, groupConversationFeature:%d"
- "checkAndUpdateNumericLimits:input dict %@"
- "checkAndUpdateNumericLimits:output dict %@"
- "current workoutTypes:%@"
- "isBundleAggregated:%d, summarizationGranularity:%lu"
- "itemFromMeFeature:%d, shareCountFeatureNormalized:%f"
- "mediaScoreFeatureNormalized:%f"
- "peopleCountWeightedAverageNormalized:%f, peopleCountMaxNormalized:%f, peopleCountWeightedSumNormalized:%f, peopleDensityWeightedAverageNormalized:%f, peopleDensityMaxNormalized:%f"
- "poiCategory:%@, interestingPOIFeature:%f, distanceToHomeFeatureNormalized:%f, familiarityIndexFeature:%f"
- "suggestionID:%@, subType:%lu, priorityScoreForResourceTypeDict:%@"
- "uniqueContactIdentifierSet: %@"
- "workoutDurationFeatureNormalized:%f"

```
