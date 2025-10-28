## momentsd

> `/usr/libexec/momentsd`

```diff

 302.0.13.0.0
-  __TEXT.__text: 0x2589f0
+  __TEXT.__text: 0x25a0d8
   __TEXT.__auth_stubs: 0x1b80
   __TEXT.__objc_stubs: 0x1dd00
   __TEXT.__objc_methlist: 0x115c4
-  __TEXT.__cstring: 0x26d9b
+  __TEXT.__cstring: 0x2747b
   __TEXT.__objc_classname: 0x1ba6
   __TEXT.__objc_methtype: 0x31fd
-  __TEXT.__objc_methname: 0x37f8a
-  __TEXT.__oslogstring: 0x3012b
+  __TEXT.__objc_methname: 0x37fc6
+  __TEXT.__oslogstring: 0x3088b
   __TEXT.__const: 0x13c1
-  __TEXT.__gcc_except_tab: 0x8388
+  __TEXT.__gcc_except_tab: 0x84c8
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x628

   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift5_reflstr: 0x13d
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x50e0
+  __TEXT.__unwind_info: 0x50e8
   __TEXT.__eh_frame: 0xb38
   __DATA_CONST.__auth_got: 0xdd8
   __DATA_CONST.__got: 0xbc0
   __DATA_CONST.__auth_ptr: 0x168
-  __DATA_CONST.__const: 0xbb50
-  __DATA_CONST.__cfstring: 0x25ae0
+  __DATA_CONST.__const: 0xbb90
+  __DATA_CONST.__cfstring: 0x26500
   __DATA_CONST.__objc_classlist: 0x7d0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x128

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F7DE939D-B9EE-3596-9D80-5F5551DB460C
-  Functions: 8607
-  Symbols:   61065
-  CStrings:  21041
+  UUID: B9822C2F-0C93-3631-BE1F-47D6C48FE2F2
+  Functions: 8612
+  Symbols:   61094
+  CStrings:  21240
 
Symbols:
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ -[MOSignificantContactManager _conversationsFromInteractions:].cold.1
+ -[MOSignificantContactManager _conversationsFromInteractions:].cold.2
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.775
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.777
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.777.cold.1
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.852
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.859
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.856
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.860
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.860.cold.1
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.316
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.317
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.427
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.427.cold.1
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.430
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.597
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.337
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.339
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.339.cold.1
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.764
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.764.cold.1
+ __64-[MOEventBundleManager _expireOutdatedNotificationsWithHandler:]_block_invoke.958
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.678
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.686
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.689
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.431
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.454
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.468
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.879
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.530
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.535
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.400
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.404
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.744
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.744.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.745
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.745.cold.1
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.759
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.759.cold.1
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.913
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.914
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.920
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.932
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.934
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.939
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.943
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.947
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.948
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.933
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.935
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.935.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.791
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.791.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.795
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.795.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.802
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.802.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.806
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.806.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.807
+ __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.760
+ __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.760.cold.1
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.952
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.952.cold.1
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.952.cold.2
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.954
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.749
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.706
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.706.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.710
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.710.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.717
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.718
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.722
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.732
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.733
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.761
+ __94-[MOThematicSummarizationManager generateThematicSummarizationBundles:withEmbeddings:handler:]_block_invoke.118
+ __94-[MOThematicSummarizationManager generateThematicSummarizationBundles:withEmbeddings:handler:]_block_invoke.118.cold.1
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.483
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.484
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.491
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.493
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.501
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.505
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.509
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.513
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.880
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.880.cold.1
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.884
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.888
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.892
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.896
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.558
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.563
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.568
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.573
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.578
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.583
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.588
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.593
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.598
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.603
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.608
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.613
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.618
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.623
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.625
+ ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
+ ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
+ __block_literal_global.287
+ __block_literal_global.335
+ __block_literal_global.356
+ __block_literal_global.602
+ __block_literal_global.607
+ __block_literal_global.684
+ __block_literal_global.691
+ __block_literal_global.708
+ __block_literal_global.748
+ __block_literal_global.812
+ __block_literal_global.817
+ __block_literal_global.819
+ __block_literal_global.926
+ _objc_msgSend$peopleCountMaxNormalized
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ _objc_msgSend$setPeopleCountMaxNormalized:
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
- -[MOEventBundleRankingInput pCountMaxNormalized]
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.772
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774.cold.1
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.849
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.856
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.853
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.857
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.857.cold.1
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.311
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.313
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.424
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.424.cold.1
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.427
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.594
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.335
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337.cold.1
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.761
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.761.cold.1
- __64-[MOEventBundleManager _expireOutdatedNotificationsWithHandler:]_block_invoke.955
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.675
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.683
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.686
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.428
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.451
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.465
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.873
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.527
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.532
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.397
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.401
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.741
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.741.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.742
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.742.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.756
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.756.cold.1
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.910
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.911
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.917
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.929
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.931
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.936
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.940
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.944
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.945
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.930
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.932
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.932.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.788
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.788.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.792
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.792.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.799
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.799.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.803
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.803.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.804
- __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.757
- __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.757.cold.1
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.949
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.949.cold.1
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.949.cold.2
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.951
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.746
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.711
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.715
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.719
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.729
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.730
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.758
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.480
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.481
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.488
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.490
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.498
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.502
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.506
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.510
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.877
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.877.cold.1
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.881
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.885
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.889
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.893
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.555
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.560
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.565
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.570
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.575
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.580
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.585
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.590
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.595
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.600
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.605
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.610
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.615
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.620
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.622
- __block_literal_global.284
- __block_literal_global.333
- __block_literal_global.599
- __block_literal_global.604
- __block_literal_global.678
- __block_literal_global.685
- __block_literal_global.705
- __block_literal_global.745
- __block_literal_global.809
- __block_literal_global.814
- __block_literal_global.816
- __block_literal_global.923
- _objc_msgSend$pCountMaxNormalized
- _objc_msgSend$pCountWeightedAverageNormalized
- _objc_msgSend$pCountWeightedSumNormalized
- _objc_msgSend$setPCountMaxNormalized:
- _objc_msgSend$setPCountWeightedAverageNormalized:
- _objc_msgSend$setPCountWeightedSumNormalized:
CStrings:
+ " ---  Grouped Interactions Count  :%3lu"
+ " ---  Received Interactions Count :%3lu"
+ "#PhotoMemory,sortedasset,id,%d,asset,%@"
+ "%@, idx, %lu, interaction, %@"
+ "%s, media title, %@, event count, %lu"
+ "(%f)"
+ "CLLocation+MOExtensions.m"
+ "DailyAnnotation: Event, %@"
+ "MOAction.m"
+ "MOAggregationManager.m"
+ "MOAnnotationManager.m"
+ "MOBiomeManager.m"
+ "MOBookmarkStore.m"
+ "MOBundleClusteringManager.m"
+ "MOContextAnnotationUtilities.m"
+ "MOConversation.m"
+ "MODaemonAnalyticsManager.m"
+ "MODaemonClient.m"
+ "MODaemonUniverse.m"
+ "MODailyAnnotationManager.m"
+ "MODataDumpFormatter.m"
+ "MODefaultsManager.m"
+ "MODictionaryEncoder.m"
+ "MODictionaryTransformer.m"
+ "MODominantBundleCreationManager.m"
+ "MOEmbedding.m"
+ "MOEngagementHistoryManager.m"
+ "MOEvent.m"
+ "MOEventBundle.m"
+ "MOEventBundleLabelCondition.m"
+ "MOEventBundleLabelFormat.m"
+ "MOEventBundleLabelLocalizer.m"
+ "MOEventBundleLabelTemplate.m"
+ "MOEventBundleManager.m"
+ "MOEventBundleRanking.m"
+ "MOEventBundleStore.m"
+ "MOEventBundler.m"
+ "MOEventData.m"
+ "MOEventExtendedAtrributes.m"
+ "MOEventManager.m"
+ "MOEventPatternDetector.m"
+ "MOEventPatternDetectorFeatureTransformerAggregateEvents.m"
+ "MOEventRefreshScheduler.m"
+ "MOEventStore.m"
+ "MOFSMStore.m"
+ "MOGraph.m"
+ "MOHealthKitManager.m"
+ "MOInteraction+_CDInteraction.m"
+ "MOInteraction.m"
+ "MOLifeEventManager.m"
+ "MOManageServer.m"
+ "MOMeasurementTransformer.m"
+ "MOMediaPlay.m"
+ "MOMediaPlaySession.m"
+ "MOMetric.m"
+ "MOMotionManager.m"
+ "MONotifier.m"
+ "MONowPlayingMediaManager.m"
+ "MOPOICategoryStore.m"
+ "MOPeopleDiscoveryManager.m"
+ "MOPersistenceManager.m"
+ "MOPhotoManager.m"
+ "MOPlace.m"
+ "MOProactiveTravelManager.m"
+ "MOPromptMetrics.m"
+ "MORankingParams+CoreDataTransformable.m"
+ "MORankingParamsMO+CoreDataClass.m"
+ "MOResource.m"
+ "MORoutineServiceManager.m"
+ "MOSharedWithYouManager.m"
+ "MOSignificantContactManager.m"
+ "MOStringArrayTransformer.m"
+ "MOSuggestedEventManager.m"
+ "MOSummarizationParameters.m"
+ "MOSummarizationUtilities.m"
+ "MOTime.m"
+ "MOTimeAtHomeParams.m"
+ "MOTimeContextAnnotationManager.m"
+ "MOTopicManager.m"
+ "MOTrendBundler.m"
+ "MOTrendsAnalyzerOptions.m"
+ "MOTripAnnotationManager.m"
+ "MOUserData.m"
+ "MOXPCContext.m"
+ "Media sessions grouped for title and day: %@"
+ "PlatformInfoOverrideIsSeedBuild"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
+ "TitleAndDayGrouping: media session with description: %@"
+ "["
+ "[generateThematicSummarizationBundles] bundle subtype=%lu, subbundlecount=%lu, phenotypes=%{private}@"
+ "]"
+ "_peopleCountMaxNormalized"
+ "_peopleCountWeightedAverageNormalized"
+ "_peopleCountWeightedSumNormalized"
+ "label confidence, label confidence score, %f, actionNameConfidence, %f, concurrentMediaActionNameConfidence, %f, backgroundActionNameConfidence, %@, placeNameConfidence, %f, bundle, %@"
+ "label confidence, label confidence, %f, event bundle, %@"
+ "new conversation created for compound key: %@, for date %@, interaction count, %lu"
+ "peopleCountMaxNormalized"
+ "peopleCountWeightedAverageNormalized"
+ "peopleCountWeightedSumNormalized"
+ "setPeopleCountMaxNormalized:"
+ "setPeopleCountWeightedAverageNormalized:"
+ "setPeopleCountWeightedSumNormalized:"
+ "skipping fetching and rehydrating contact events"
+ "skipping fetching and rehydrating life events"
+ "skipping fetching and rehydrating music"
+ "skipping fetching and rehydrating people density events"
+ "skipping fetching and rehydrating photo memory"
+ "skipping fetching and rehydrating prox"
+ "skipping fetching and rehydrating state of mind"
+ "skipping fetching and rehydrating workouts"
+ "skipping fetching and saving motion events"
+ "skipping fetching and saving screentime events"
+ "skipping fetching and saving spotlight events"
+ "skipping training, fetching and rehydrating visits"
+ "spotlight event integration enablement param is set to %d"
+ "start fetching and rehydrating contact events"
+ "start fetching and rehydrating life events"
+ "start fetching and rehydrating motion events"
+ "start fetching and rehydrating music"
+ "start fetching and rehydrating people density events"
+ "start fetching and rehydrating photo memory"
+ "start fetching and rehydrating prox"
+ "start fetching and rehydrating screentime events"
+ "start fetching and rehydrating spotlight events"
+ "start fetching and rehydrating state of mind data"
+ "start fetching and rehydrating workouts"
+ "start training, fetching and rehydrating visits"
- "Tf,N,V_pCountMaxNormalized"
- "Tf,N,V_pCountWeightedAverageNormalized"
- "Tf,N,V_pCountWeightedSumNormalized"
- "_pCountMaxNormalized"
- "_pCountWeightedAverageNormalized"
- "_pCountWeightedSumNormalized"
- "setPCountMaxNormalized:"
- "setPCountWeightedAverageNormalized:"
- "setPCountWeightedSumNormalized:"

```
