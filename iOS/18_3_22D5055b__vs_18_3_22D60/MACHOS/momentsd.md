## momentsd

> `/usr/libexec/momentsd`

```diff

 205.0.1.0.0
-  __TEXT.__text: 0x20e6fc
+  __TEXT.__text: 0x2102fc
   __TEXT.__auth_stubs: 0x15c0
   __TEXT.__objc_stubs: 0x1a420
   __TEXT.__objc_methlist: 0xe188
-  __TEXT.__cstring: 0x20ffd
+  __TEXT.__cstring: 0x2165d
   __TEXT.__objc_classname: 0x1856
   __TEXT.__objc_methtype: 0x2ad3
-  __TEXT.__objc_methname: 0x2c13c
-  __TEXT.__oslogstring: 0x2853f
-  __TEXT.__const: 0xc10
-  __TEXT.__gcc_except_tab: 0x78dc
+  __TEXT.__objc_methname: 0x2c178
+  __TEXT.__oslogstring: 0x28f1f
+  __TEXT.__const: 0xc20
+  __TEXT.__gcc_except_tab: 0x7b04
   __TEXT.__ustring: 0xe
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x150

   __DATA_CONST.__auth_got: 0xaf8
   __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x9578
-  __DATA_CONST.__cfstring: 0x20160
+  __DATA_CONST.__const: 0x9598
+  __DATA_CONST.__cfstring: 0x20b00
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7039
-  Symbols:   50022
-  CStrings:  13718
+  Functions: 7042
+  Symbols:   50039
+  CStrings:  13850
 
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
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1177
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1179
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1179.cold.1
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.800
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.807
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.804
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.808
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.808.cold.1
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.305
+ __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.306
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.410
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.410.cold.1
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.412
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.540
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.448
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.450
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.450.cold.1
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.711
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.711.cold.1
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.626
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.634
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.637
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.387
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.410
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.417
+ __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.415
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.827
+ __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.408
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.478
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.483
+ __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.416
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.355
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.359
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.692
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.692.cold.1
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.693
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.693.cold.1
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.707
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.707.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.738
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.738.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.749
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.749.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.753
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.753.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.754
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.281
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.281.cold.1
+ __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.406
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.466
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.466.cold.1
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.697
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.280
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.280.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1123
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1129
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1130
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1134
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.270
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.271
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1165
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.432
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.433
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.440
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.448
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.452
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.456
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.460
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.828
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.828.cold.1
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.832
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.836
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.840
+ __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.844
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.506
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.511
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.516
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.521
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.526
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.531
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.536
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.541
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.546
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.551
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.556
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.561
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.566
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.571
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.573
+ ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
+ ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
+ __block_literal_global.283
+ __block_literal_global.446
+ __block_literal_global.468
+ __block_literal_global.545
+ __block_literal_global.550
+ __block_literal_global.632
+ __block_literal_global.639
+ __block_literal_global.656
+ __block_literal_global.696
+ __block_literal_global.760
+ __block_literal_global.765
+ __block_literal_global.767
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
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.797
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.804
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.801
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805.cold.1
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.300
- __130-[MOPhotoManager fetchPhotosBetweenStartDate:EndDate:SuggestionID:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.302
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.407
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.407.cold.1
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.409
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.537
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.446
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.448
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.448.cold.1
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708.cold.1
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.623
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.631
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.634
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.384
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.407
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.414
- __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.412
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.821
- __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.405
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.475
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.480
- __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.413
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.352
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.356
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.735
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.735.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.746
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.746.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.751
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.278
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.278.cold.1
- __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.403
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.464
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.464.cold.1
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.694
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.277
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.277.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.267
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.268
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.429
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.430
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.437
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.445
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.449
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.453
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.457
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.825
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.825.cold.1
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.829
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.833
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.837
- __97-[MOEventBundleManager _processClusterBundles:withEmbeddings:onboardingStatus:result:andHandler:]_block_invoke.841
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.503
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.508
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.513
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.518
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.523
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.528
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.533
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.538
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.543
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.548
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.553
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.558
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.563
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.568
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.570
- __block_literal_global.280
- __block_literal_global.444
- __block_literal_global.466
- __block_literal_global.542
- __block_literal_global.547
- __block_literal_global.626
- __block_literal_global.633
- __block_literal_global.653
- __block_literal_global.693
- __block_literal_global.757
- __block_literal_global.762
- __block_literal_global.764
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
+ "skipping fetching and saving contact events"
+ "skipping fetching and saving life events"
+ "skipping fetching and saving mindful sessions"
+ "skipping fetching and saving motion events"
+ "skipping fetching and saving music"
+ "skipping fetching and saving people density events"
+ "skipping fetching and saving photo memory"
+ "skipping fetching and saving prox"
+ "skipping fetching and saving share with you items"
+ "skipping fetching and saving shared p mom"
+ "skipping fetching and saving trips"
+ "skipping fetching and saving visits"
+ "skipping fetching and saving workouts"
+ "skipping training, fetching and rehydrating visits"
+ "start fetching and rehydrating contact events"
+ "start fetching and rehydrating life events"
+ "start fetching and rehydrating motion events"
+ "start fetching and rehydrating music"
+ "start fetching and rehydrating people density events"
+ "start fetching and rehydrating photo memory"
+ "start fetching and rehydrating prox"
+ "start fetching and rehydrating state of mind data"
+ "start fetching and rehydrating workouts"
+ "start fetching and saving contact events"
+ "start fetching and saving life events"
+ "start fetching and saving mindful sessions"
+ "start fetching and saving motion events"
+ "start fetching and saving music"
+ "start fetching and saving people density events"
+ "start fetching and saving photo memory"
+ "start fetching and saving prox"
+ "start fetching and saving share with you items"
+ "start fetching and saving shared p mom"
+ "start fetching and saving trips"
+ "start fetching and saving visits"
+ "start fetching and saving workouts"
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
