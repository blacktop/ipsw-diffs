## momentsd

> `/usr/libexec/momentsd`

```diff

 197.0.0.0.0
-  __TEXT.__text: 0x20b288
-  __TEXT.__auth_stubs: 0x15c0
+  __TEXT.__text: 0x20cea8
+  __TEXT.__auth_stubs: 0x15d0
   __TEXT.__objc_stubs: 0x1a240
   __TEXT.__objc_methlist: 0xe0d8
-  __TEXT.__cstring: 0x20add
+  __TEXT.__cstring: 0x2114d
   __TEXT.__objc_classname: 0x1857
   __TEXT.__objc_methtype: 0x2a94
-  __TEXT.__objc_methname: 0x2bda7
-  __TEXT.__oslogstring: 0x280df
+  __TEXT.__objc_methname: 0x2bde3
+  __TEXT.__oslogstring: 0x28acf
   __TEXT.__const: 0xbe0
-  __TEXT.__gcc_except_tab: 0x78d8
+  __TEXT.__gcc_except_tab: 0x7b00
   __TEXT.__ustring: 0xe
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x150

   __TEXT.__swift5_reflstr: 0x30
   __TEXT.__unwind_info: 0x4360
   __TEXT.__eh_frame: 0x388
-  __DATA_CONST.__auth_got: 0xaf8
+  __DATA_CONST.__auth_got: 0xb00
   __DATA_CONST.__got: 0x9b0
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x93b8
-  __DATA_CONST.__cfstring: 0x1fb80
+  __DATA_CONST.__const: 0x93d8
+  __DATA_CONST.__cfstring: 0x20520
   __DATA_CONST.__objc_classlist: 0x6a0
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0xe0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7013
-  Symbols:   49768
-  CStrings:  13634
+  Functions: 7016
+  Symbols:   49786
+  CStrings:  13766
 
Symbols:
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.693.cold.1
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.808
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.692
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.448
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.808.cold.1
+ -[MOSignificantContactManager _conversationsFromInteractions:].cold.1
+ __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.414
+ ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.807
+ __block_literal_global.656
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.824
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.546
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.411
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.280.cold.1
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.841
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1130
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742.cold.1
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.551
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.753.cold.1
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.432
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.711.cold.1
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.450
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.829.cold.1
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.483
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.387
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.270
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.511
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.536
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.749.cold.1
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.573
+ __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.407
+ __block_literal_global.552
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1177
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.828
+ ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
+ _objc_msgSend$setPeopleCountMaxNormalized:
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.450.cold.1
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.833
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.692.cold.1
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.466
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.637
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1129
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.829
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.526
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.355
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.707
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.409
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.448
+ -[MOSignificantContactManager _conversationsFromInteractions:].cold.2
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.845
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.800
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.837
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1179
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.738
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.281.cold.1
+ __block_literal_global.639
+ _objc_msgSend$peopleCountMaxNormalized
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.280
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.521
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.417
+ __block_literal_global.696
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.516
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.754
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.707.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.738.cold.1
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1165
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.456
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.478
+ __block_literal_global.632
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.440
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.693
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.433
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.542
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.531
+ __133-[MOPhotoManager _fetchCuratedPhotosFromHighlights:StartDate:EndDate:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.357
+ __block_literal_global.760
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.561
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.359
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1134
+ __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.405
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.466.cold.1
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.410
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.753
+ __block_literal_global.767
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1179.cold.1
+ __block_literal_global.765
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.626
+ _objc_retain_x11
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.571
+ __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.415
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1123
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.281
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.409.cold.1
+ __block_literal_global.547
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.452
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.711
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.506
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.749
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.697
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.804
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.460
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.556
+ __block_literal_global.446
+ __block_literal_global.283
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.541
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.271
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.634
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.566
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.735.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.553
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.277
- _objc_msgSend$setPCountWeightedAverageNormalized:
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.623
- _objc_msgSend$setPCountMaxNormalized:
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.735
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.694
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.448.cold.1
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.548
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.449
- _objc_msgSend$pCountWeightedAverageNormalized
- __block_literal_global.544
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.543
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.834
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.634
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.407
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.822
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.804
- __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.402
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.838
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.464.cold.1
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.278
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.445
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.821
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.437
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.278.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704.cold.1
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.430
- __block_literal_global.762
- __133-[MOPhotoManager _fetchCuratedPhotosFromHighlights:StartDate:EndDate:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.354
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.539
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.384
- _objc_msgSend$pCountMaxNormalized
- __block_literal_global.280
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.513
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.842
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.746
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
- __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.411
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.408
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.448
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.453
- __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.404
- __block_literal_global.757
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.406.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.475
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.801
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.631
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.277.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.751
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690.cold.1
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.268
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.538
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.267
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689.cold.1
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.480
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.429
- __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.412
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.518
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.563
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.414
- __block_literal_global.764
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.356
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.352
- _objc_msgSend$pCountWeightedSumNormalized
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.528
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.457
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- -[MOEventBundleRankingInput pCountMaxNormalized]
- __block_literal_global.693
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- __block_literal_global.653
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739.cold.1
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.464
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.797
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.503
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.830
- _objc_msgSend$setPCountWeightedSumNormalized:
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750
- __block_literal_global.549
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.558
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- __block_literal_global.444
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.406
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.533
- __block_literal_global.633
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.570
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739
- __block_literal_global.626
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.508
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.746.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.523
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.446
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.568
CStrings:
+ "MOHealthKitManager.m"
+ "]"
+ "MOUserData.m"
+ "peopleCountMaxNormalized"
+ "MOEventPatternDetector.m"
+ "%!@(MISSING), idx, %!l(MISSING)u, interaction, %!@(MISSING)"
+ "new conversation created for compound key: %!@(MISSING), for date %!@(MISSING), interaction count, %!l(MISSING)u"
+ "start fetching and rehydrating life events"
+ "start fetching and saving shared p mom"
+ "start fetching and saving trips"
+ "start fetching and saving photo memory"
+ "MODaemonUniverse.m"
+ "MOFSMStore.m"
+ "MODaemonClient.m"
+ "MOMotionManager.m"
+ "start fetching and rehydrating motion events"
+ "MONowPlayingMediaManager.m"
+ "#PhotoMemory,sortedasset,id,%!d(MISSING),asset,%!@(MISSING)"
+ "start fetching and rehydrating music"
+ "MOPhotoManager.m"
+ "MOAnnotationManager.m"
+ "_peopleCountWeightedAverageNormalized"
+ "MOEventBundleLabelFormat.m"
+ "start fetching and saving workouts"
+ "start fetching and saving visits"
+ "start fetching and saving prox"
+ "start fetching and saving life events"
+ "label confidence, label confidence score, %!f(MISSING), actionNameConfidence, %!f(MISSING), concurrentMediaActionNameConfidence, %!f(MISSING), backgroundActionNameConfidence, %!@(MISSING), placeNameConfidence, %!f(MISSING), bundle, %!@(MISSING)"
+ "MOSummarizationParameters.m"
+ "start fetching and rehydrating people density events"
+ "MORankingParams+CoreDataTransformable.m"
+ "skipping fetching and rehydrating workouts"
+ "skipping fetching and saving visits"
+ "MOSummarizationUtilities.m"
+ "MOConversation.m"
+ "setPeopleCountWeightedAverageNormalized:"
+ "skipping fetching and saving mindful sessions"
+ "skipping fetching and rehydrating state of mind"
+ "MONotifier.m"
+ "MOEventBundleStore.m"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
+ "MOTime.m"
+ "MOResource.m"
+ "MODaemonAnalyticsManager.m"
+ "MODefaultsManager.m"
+ "skipping fetching and saving photo memory"
+ "MODictionaryEncoder.m"
+ "MOGraph.m"
+ "start fetching and saving motion events"
+ "["
+ "MORoutineServiceManager.m"
+ "MOEventBundleLabelTemplate.m"
+ "MODictionaryTransformer.m"
+ "MOPlace.m"
+ "start training, fetching and rehydrating visits"
+ "start fetching and rehydrating workouts"
+ "setPeopleCountWeightedSumNormalized:"
+ "MOEvent.m"
+ "Media sessions grouped for title and day: %!@(MISSING)"
+ "MOMediaPlay.m"
+ "MOContextAnnotationUtilities.m"
+ "MOEventBundleLabelCondition.m"
+ "skipping fetching and saving trips"
+ "MOAggregationManager.m"
+ "start fetching and saving mindful sessions"
+ "peopleCountWeightedAverageNormalized"
+ "MOSuggestedEventManager.m"
+ "skipping fetching and rehydrating photo memory"
+ "MOEventManager.m"
+ "skipping fetching and rehydrating contact events"
+ "MOEventBundleLabelLocalizer.m"
+ "skipping training, fetching and rehydrating visits"
+ "MOEventBundleRanking.m"
+ "MOBiomeManager.m"
+ "start fetching and saving share with you items"
+ "start fetching and saving music"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "MOTopicManager.m"
+ "MOMetric.m"
+ "MOSharedWithYouManager.m"
+ "MOMeasurementTransformer.m"
+ "MOEventExtendedAtrributes.m"
+ "MODataDumpFormatter.m"
+ "MOEmbedding.m"
+ " ---  Grouped Interactions Count  :%!l(MISSING)u"
+ "MOTripAnnotationManager.m"
+ "start fetching and rehydrating photo memory"
+ "skipping fetching and saving music"
+ "TitleAndDayGrouping: media session with description: %!@(MISSING)"
+ "MODominantBundleCreationManager.m"
+ "MOEventData.m"
+ "start fetching and rehydrating contact events"
+ "skipping fetching and saving contact events"
+ "skipping fetching and rehydrating prox"
+ "MOAction.m"
+ "skipping fetching and saving motion events"
+ "MOTrendBundler.m"
+ "start fetching and rehydrating state of mind data"
+ "MOEventBundleManager.m"
+ "MOLifeEventManager.m"
+ "PlatformInfoOverrideIsSeedBuild"
+ "setPeopleCountMaxNormalized:"
+ "MOTimeContextAnnotationManager.m"
+ "skipping fetching and saving workouts"
+ "MOInteraction.m"
+ "MOEventBundler.m"
+ "MOPersistenceManager.m"
+ "label confidence, label confidence, %!f(MISSING), event bundle, %!@(MISSING)"
+ "MOXPCContext.m"
+ "start fetching and saving contact events"
+ "_peopleCountWeightedSumNormalized"
+ "MOStringArrayTransformer.m"
+ "skipping fetching and rehydrating life events"
+ "peopleCountWeightedSumNormalized"
+ "_peopleCountMaxNormalized"
+ "skipping fetching and saving life events"
+ "MOMediaPlaySession.m"
+ " ---  Received Interactions Count :%!l(MISSING)u"
+ "MOPromptMetrics.m"
+ "%!s(MISSING), media title, %!@(MISSING), event count, %!l(MISSING)u"
+ "MODailyAnnotationManager.m"
+ "MORankingParamsMO+CoreDataClass.m"
+ "start fetching and rehydrating prox"
+ "MOEventPatternDetectorFeatureTransformerAggregateEvents.m"
+ "skipping fetching and saving prox"
+ "MOTrendsAnalyzerOptions.m"
+ "(%!f(MISSING))"
+ "MOSignificantContactManager.m"
+ "skipping fetching and saving share with you items"
+ "skipping fetching and rehydrating people density events"
+ "MOPeopleDiscoveryManager.m"
+ "MOEventBundle.m"
+ "start fetching and saving people density events"
+ "MOEventStore.m"
+ "DailyAnnotation: Event, %!@(MISSING)"
+ "skipping fetching and saving shared p mom"
+ "skipping fetching and rehydrating music"
+ "MOInteraction+_CDInteraction.m"
+ "MOEngagementHistoryManager.m"
+ "MOManageServer.m"
+ "skipping fetching and saving people density events"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "CLLocation+MOExtensions.m"
+ "MOProactiveTravelManager.m"
- "setPCountMaxNormalized:"
- "Tf,N,V_pCountMaxNormalized"
- "setPCountWeightedAverageNormalized:"
- "Tf,N,V_pCountWeightedSumNormalized"
- "_pCountWeightedSumNormalized"
- "_pCountWeightedAverageNormalized"
- "_pCountMaxNormalized"
- "setPCountWeightedSumNormalized:"
- "Tf,N,V_pCountWeightedAverageNormalized"

```
