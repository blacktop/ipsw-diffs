## momentsd

> `/usr/libexec/momentsd`

```diff

-202.0.6.0.0
-  __TEXT.__text: 0x20e50c
+202.0.7.0.0
+  __TEXT.__text: 0x20e694
   __TEXT.__auth_stubs: 0x15c0
-  __TEXT.__objc_stubs: 0x1a3e0
-  __TEXT.__objc_methlist: 0xe180
-  __TEXT.__cstring: 0x20f6d
+  __TEXT.__objc_stubs: 0x1a400
+  __TEXT.__objc_methlist: 0xe188
+  __TEXT.__cstring: 0x20fed
   __TEXT.__objc_classname: 0x1856
   __TEXT.__objc_methtype: 0x2ad3
-  __TEXT.__objc_methname: 0x2c0fd
-  __TEXT.__oslogstring: 0x2843f
+  __TEXT.__objc_methname: 0x2c125
+  __TEXT.__oslogstring: 0x2844f
   __TEXT.__const: 0xbf0
-  __TEXT.__gcc_except_tab: 0x78c0
+  __TEXT.__gcc_except_tab: 0x78d0
   __TEXT.__ustring: 0xe
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x150

   __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x68
   __DATA_CONST.__const: 0x9578
-  __DATA_CONST.__cfstring: 0x20120
+  __DATA_CONST.__cfstring: 0x20160
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_doubleobj: 0x310
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA.__objc_const: 0x193c8
-  __DATA.__objc_selrefs: 0x7bd8
+  __DATA.__objc_selrefs: 0x7be0
   __DATA.__objc_ivar: 0x12cc
   __DATA.__objc_data: 0x4480
   __DATA.__data: 0x1280

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7038
-  Symbols:   50015
-  CStrings:  13714
+  Functions: 7039
+  Symbols:   50021
+  CStrings:  13716
 
Symbols:
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.657
+ __block_literal_global.474
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.431.cold.1
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.651
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.434
+ +[MOEngagementAndSuggestionAnalyticsParams aggregatedEngagementAnalyticsAddressMap]
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2.202
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.418
+ __82-[MOHealthKitManager fetchAndSaveMindfulSessionsBetweenStartDate:EndDate:handler:]_block_invoke.436
+ __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.644
+ _objc_msgSend$aggregatedEngagementAnalyticsAddressMap
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.204
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.667
+ __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.648
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.422
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.421.cold.1
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.430.cold.1
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.430
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104r112r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8s56l8r104l8s64l8s72l8s80l8s88l8s96l8r112l8
+ __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.429
+ __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.652
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.237
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.419
+ __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.581
+ __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.188
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.253
+ __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1906
+ __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.427
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.433
+ __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.418.cold.1
+ __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.433.cold.1
+ __95-[MOHealthKitManager _fetchStateOfMindEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.462
+ __75-[MOHealthKitManager fetchAndSaveWorkoutsBetweenStartDate:EndDate:handler:]_block_invoke.435
+ __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.421
+ __136-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.112
+ __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.682
+ __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.461
+ __62-[MOBiomeManager donateEvents:andBundles:andOnboardingStatus:]_block_invoke.628
+ __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.255
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.430
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.430.cold.1
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.428
- __66-[MOHealthKitManager _rehydrateStoredEvents:fromWorkouts:handler:]_block_invoke.424
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke.648
- __61-[MOHealthKitManager _updateWorkoutsDeletedAtSource:handler:]_block_invoke.428.cold.1
- __75-[MOHealthKitManager fetchAndSaveWorkoutsBetweenStartDate:EndDate:handler:]_block_invoke.432
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.679
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.240
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.664
- __62-[MOBiomeManager donateEvents:andBundles:andOnboardingStatus:]_block_invoke.625
- __37-[MOPromptMetrics getAndSetAgeGender]_block_invoke.1903
- __136-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAndSuggestionPerformanceAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.115
- __95-[MOHealthKitManager _fetchStateOfMindEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.459
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.427
- ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96r104r_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8r96l8s56l8s64l8s72l8s80l8s88l8r104l8
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.418
- __69-[MOBiomeManager fetchMomentsEngagementForBundles:CompletionHandler:]_block_invoke.645
- __82-[MOHealthKitManager fetchAndSaveMindfulSessionsBetweenStartDate:EndDate:handler:]_block_invoke.433
- __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.256
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.426
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.418.cold.1
- __64-[MOBiomeManager _fetchAndSetDemographicsWithCompletionHandler:]_block_invoke.654
- __140-[MOEngagementAndSuggestionAnalyticsManager _submitSuggestionPerformanceAnalyticsFromEventBundles:WithOnboardingStatus:andCompletionResult:]_block_invoke.258
- __82-[MOBiomeManager fetchMomentsEventDataBetweenStartDate:EndDate:CompletionHandler:]_block_invoke_2.649
- __52-[MOHealthKitManager _rehydrateStateOfMind:handler:]_block_invoke.419
- __91-[MOHealthKitManager _fetchWorkoutEventsBetweenStartDate:endDate:withStoredEvents:handler:]_block_invoke.458
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.415.cold.1
- __50-[MOHealthKitManager _fetchLocationsFrom:handler:]_block_invoke.427.cold.1
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.191
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke.207
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.416
- __112-[MOEngagementAndSuggestionAnalyticsManager submitEngagementAnalyticsWithOnboardingStatus:AndCompletionHandler:]_block_invoke_2.205
- __45-[MOTrendsAnalyzer(Metrics) setCommonFields:]_block_invoke.578
- __49-[MOHealthKitManager _rehydrateWorkouts:handler:]_block_invoke.415
- __49-[MOBiomeManager _updateDataStreamWithEngagement]_block_invoke.641
CStrings:
+ "aggregatedEngagementAnalyticsAddressMap"
+ "Journal entry engagement analytics result was submitted to: %!@(MISSING), Analytics event: %!@(MISSING)"
+ "com.apple.Moments.EngagementAggregatedMetricsTwentyEightDay"
+ "Engagement and suggestion analytics were never submitted. Setting analyticsSubmissionDate to now to hold out for the next 28 days"
+ "com.apple.Moments.EngagementAggregatedMetricsOneDay"
+ "com.apple.Moments.EngagementAggregatedMetricsSevenDay"
- "Engagement and suggestion analytics were never submitted. Attempting to submit new analytics"
- "com.apple.Moments.EngagementAggregatedMetrics"
- "Journal entry engagement analytics result was submitted: %!@(MISSING)"
- "Suggestion engagement analytics result was submitted: %!@(MISSING)"

```
