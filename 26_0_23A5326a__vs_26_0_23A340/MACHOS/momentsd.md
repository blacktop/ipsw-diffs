## momentsd

> `/usr/libexec/momentsd`

```diff

 297.0.0.0.0
-  __TEXT.__text: 0x24b2ec
+  __TEXT.__text: 0x24ca00
   __TEXT.__auth_stubs: 0x1ad0
   __TEXT.__objc_stubs: 0x1d240
   __TEXT.__objc_methlist: 0x111e0
-  __TEXT.__cstring: 0x260ef
+  __TEXT.__cstring: 0x267cf
   __TEXT.__objc_classname: 0x1b58
   __TEXT.__objc_methtype: 0x315e
-  __TEXT.__objc_methname: 0x36cb9
-  __TEXT.__oslogstring: 0x2f09b
+  __TEXT.__objc_methname: 0x36cf5
+  __TEXT.__oslogstring: 0x2f7fb
   __TEXT.__const: 0x1231
-  __TEXT.__gcc_except_tab: 0x7dec
+  __TEXT.__gcc_except_tab: 0x7f2c
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__constg_swiftt: 0x5ec

   __TEXT.__swift_as_entry: 0x44
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_proto: 0xc
-  __TEXT.__unwind_info: 0x4e50
+  __TEXT.__unwind_info: 0x4e58
   __TEXT.__eh_frame: 0xa68
   __DATA_CONST.__auth_got: 0xd80
   __DATA_CONST.__got: 0xba8
   __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0xb4a0
-  __DATA_CONST.__cfstring: 0x24e80
+  __DATA_CONST.__const: 0xb4e0
+  __DATA_CONST.__cfstring: 0x258a0
   __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x128

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5F48B5EE-E302-371F-9965-E241A2159E5C
-  Functions: 8406
-  Symbols:   59639
-  CStrings:  20621
+  UUID: 4EFB8BD8-AFED-397E-B3FA-BBD2799B37BF
+  Functions: 8411
+  Symbols:   59668
+  CStrings:  20820
 
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
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.843
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.850
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.847
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.851
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.851.cold.1
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.316
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.317
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.427
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.427.cold.1
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.430
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.578
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.337
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.339
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.339.cold.1
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.755
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.755.cold.1
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.669
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.677
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.680
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.422
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.445
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.459
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.870
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.521
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.526
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.391
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.395
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.735
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.735.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.736
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.736.cold.1
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.750
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.750.cold.1
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.904
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.905
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.911
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.923
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.925
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.930
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.934
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.938
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.939
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.924
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.926
+ __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.926.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.782
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.782.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.786
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.786.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.793
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.793.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.797
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.797.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.798
+ __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.751
+ __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.751.cold.1
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.943
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.943.cold.1
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.943.cold.2
+ __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.945
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.740
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
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.474
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.475
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.482
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.484
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.492
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.496
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.500
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.504
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.871
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.871.cold.1
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.875
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.879
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.883
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.887
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.549
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.554
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.559
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.564
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.569
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.574
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.579
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.584
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.589
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.594
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.599
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.604
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.609
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.614
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.616
+ ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
+ ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
+ __block_literal_global.287
+ __block_literal_global.335
+ __block_literal_global.356
+ __block_literal_global.583
+ __block_literal_global.588
+ __block_literal_global.675
+ __block_literal_global.682
+ __block_literal_global.699
+ __block_literal_global.739
+ __block_literal_global.803
+ __block_literal_global.808
+ __block_literal_global.810
+ __block_literal_global.917
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
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.840
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.847
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.844
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.848
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.848.cold.1
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.311
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.313
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.424
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.424.cold.1
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.427
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.575
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.335
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.337.cold.1
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.752
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.752.cold.1
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.666
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.674
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.677
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.419
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.442
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.456
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.864
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.518
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.523
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.388
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.392
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.732
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.732.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.733
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.733.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.747
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.747.cold.1
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.901
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.902
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.908
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.920
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.922
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.927
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.931
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.935
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke.936
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.921
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.923
- __73-[MOEventBundleManager _generateThematicSummarizationBundlesWithHandler:]_block_invoke_2.923.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.779
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.779.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.783
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.783.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.790
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.790.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.794
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.794.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.795
- __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.748
- __74-[MOEventBundleManager _fetchEventBundlesWithPredicate:completionHandler:]_block_invoke.748.cold.1
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.940
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.940.cold.1
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.940.cold.2
- __74-[MOEventBundleManager _generatePersonalizedReflectionBundlesWithHandler:]_block_invoke.942
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.737
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
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.471
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.472
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.479
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.481
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.489
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.493
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.497
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.501
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.868
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.868.cold.1
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.872
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.876
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.880
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.884
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.546
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.551
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.556
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.561
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.566
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.571
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.576
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.581
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.586
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.591
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.596
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.601
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.606
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.611
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.613
- __block_literal_global.284
- __block_literal_global.333
- __block_literal_global.580
- __block_literal_global.585
- __block_literal_global.669
- __block_literal_global.676
- __block_literal_global.696
- __block_literal_global.736
- __block_literal_global.800
- __block_literal_global.805
- __block_literal_global.807
- __block_literal_global.914
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
