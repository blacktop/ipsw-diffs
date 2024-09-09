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
+ __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.542
+ __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.415
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.281.cold.1
+ __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.407
+ __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.281
+ ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.800
+ __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.697
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.808
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.546
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.483
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1130
+ ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.807
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.440
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.450
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.692.cold.1
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.738
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.521
+ __133-[MOPhotoManager _fetchCuratedPhotosFromHighlights:StartDate:EndDate:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.357
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.561
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.804
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.409
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.833
+ __block_literal_global.656
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.828
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.634
+ __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.409.cold.1
+ _objc_msgSend$peopleCountMaxNormalized
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.271
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.516
+ _objc_msgSend$setPeopleCountMaxNormalized:
+ -[MOSignificantContactManager _conversationsFromInteractions:].cold.2
+ __block_literal_global.639
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.448
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.456
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.637
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1177
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.837
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742.cold.1
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1179.cold.1
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.566
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.707
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.571
+ __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.626
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.417
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.738.cold.1
+ __block_literal_global.765
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.452
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.742
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.359
+ _objc_retain_x11
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.749.cold.1
+ __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.270
+ __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.808.cold.1
+ __block_literal_global.767
+ __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.411
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1179
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.541
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.466.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1129
+ __block_literal_global.696
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.753
+ __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.707.cold.1
+ __block_literal_global.632
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.693.cold.1
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.280.cold.1
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.433
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1165
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.506
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.845
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.711
+ __block_literal_global.283
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.410
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.749
+ -[MOSignificantContactManager _conversationsFromInteractions:].cold.1
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.531
+ __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.355
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.460
+ __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.432
+ __block_literal_global.446
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.829
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.511
+ __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.280
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1123
+ __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.387
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.693
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.405
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.448
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.526
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.753.cold.1
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
+ __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.692
+ __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.466
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.841
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.573
+ __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.450.cold.1
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.556
+ __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.414
+ __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.754
+ __block_literal_global.547
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.824
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.536
+ __block_literal_global.552
+ __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.478
+ __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.829.cold.1
+ __block_literal_global.760
+ __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.711.cold.1
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.551
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1134
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.503
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.384
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.437
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.751
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.449
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.429
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.746.cold.1
- __block_literal_global.653
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.356
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.623
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.430
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.804
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.543
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.448
- __75-[MOPhotoManager fetchAndSaveSharedPhotosBetweenStartDate:EndDate:handler:]_block_invoke.402
- _objc_msgSend$setPCountMaxNormalized:
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.834
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739
- __block_literal_global.280
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.805
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708.cold.1
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.842
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.277
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.267
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.406
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.548
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826.cold.1
- __71-[MOEventBundleManager _computeEvergreenScoreParams:withRankingParams:]_block_invoke.352
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.735
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke.797
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690.cold.1
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.563
- __block_literal_global.764
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.568
- __block_literal_global.549
- __115-[MOEventBundleManager fetchAndSaveBundlingDataForTrigger:withFeedback:additionalMetadata:shouldUpload:andHandler:]_block_invoke_2.801
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.513
- __88-[MONowPlayingMediaManager fetchAndSaveMediaPlayEventsBetweenStartDate:EndDate:handler:]_block_invoke.268
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.528
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke.631
- __133-[MOPhotoManager _fetchCuratedPhotosFromHighlights:StartDate:EndDate:BundleInterfaceType:Locations:IsLocationCheckMandatory:handler:]_block_invoke.354
- __81-[MONowPlayingMediaManager _updateMediaPlaySessionEventsDeletedAtSource:handler:]_block_invoke.277.cold.1
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.407
- _objc_msgSend$pCountMaxNormalized
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.533
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.278
- -[MOEventBundleRankingInput pCountMaxNormalized]
- _objc_msgSend$setPCountWeightedAverageNormalized:
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.826
- __block_literal_global.626
- __64-[MOEventBundleManager associateEventBundles:effectiveInterval:]_block_invoke_2.634
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
- __67-[MOEventBundleManager _bundleEventsWithRefreshVariant:andHandler:]_block_invoke.414
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.464.cold.1
- __block_literal_global.444
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke.446
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.553
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689
- __50-[MOPhotoManager _rehydratePhotoMemories:handler:]_block_invoke.408
- _objc_msgSend$pCountWeightedSumNormalized
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.457
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- _objc_msgSend$pCountWeightedAverageNormalized
- __56-[MODaemonClient printEvergreenBundlesWithSeed:handler:]_block_invoke.539
- __74-[MONowPlayingMediaManager _updateMediaPlayEventsDeletedAtSource:handler:]_block_invoke.278.cold.1
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.735.cold.1
- __70-[MOPhotoManager _updatePhotoMemoriesDeletedAtSource:library:handler:]_block_invoke.412
- __75-[MOSignificantContactManager _updateConversationsDeletedAtSource:handler:]_block_invoke.464
- __58-[MOSignificantContactManager _saveConversations:handler:]_block_invoke_2.448.cold.1
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.558
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.838
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.508
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.830
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.445
- _objc_msgSend$setPCountWeightedSumNormalized:
- __96-[MOEventBundleManager _bundleEvents:startDate:endDate:submitMetricsFlg:refreshVariant:handler:]_block_invoke.453
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.750.cold.1
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.690
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.821
- __block_literal_global.544
- __59-[MOEventBundleManager _rehydrateEventBundles:withHandler:]_block_invoke.708
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.518
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.570
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.480
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.523
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- __69-[MOEventBundleManager _generateClusterAndAnomalyBundlesWithHandler:]_block_invoke.822
- __47-[MOPhotoManager _saveEvents:category:handler:]_block_invoke.406.cold.1
- __72-[MOEventBundleManager _fetchEventBundlesWithOptions:CompletionHandler:]_block_invoke.704.cold.1
- __block_literal_global.633
- __block_literal_global.693
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.739.cold.1
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- __70-[MOEventBundleManager _fetchPreviousBundlesWithDateInterval:handler:]_block_invoke.475
- __74-[MOEventBundleManager _cleanUpEventBundlesWithRefreshVariant:andHandler:]_block_invoke.746
- __69-[MOPhotoManager fetchAndSavePhotoMemoriesStartDate:EndDate:handler:]_block_invoke.404
- __block_literal_global.762
- __98-[MOEventBundleManager _annotateEventBundlesWithStartDate:endDate:allEvents:eventBundles:handler:]_block_invoke.538
- __68-[MOPhotoManager _updatePhotoEventsDeletedAtSource:library:handler:]_block_invoke.411
- __81-[MOEventBundleManager fetchRehydratedEventBundlesWithOptions:CompletionHandler:]_block_invoke.694
- __block_literal_global.757
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- __71-[MOEventBundleManager saveEventBundles:withStartDate:endDate:handler:]_block_invoke.689.cold.1
CStrings:
+ "MONotifier.m"
+ "Media sessions grouped for title and day: %!@(MISSING)"
+ "label confidence, label confidence, %!f(MISSING), event bundle, %!@(MISSING)"
+ "skipping fetching and rehydrating contact events"
+ "MODominantBundleCreationManager.m"
+ "MOTime.m"
+ "skipping fetching and saving motion events"
+ "MOTimeContextAnnotationManager.m"
+ "MOPlace.m"
+ "%!s(MISSING), media title, %!@(MISSING), event count, %!l(MISSING)u"
+ "MOEventBundleStore.m"
+ "MORoutineServiceManager.m"
+ "skipping fetching and saving workouts"
+ "start fetching and rehydrating life events"
+ "MODaemonAnalyticsManager.m"
+ "MOBiomeManager.m"
+ "peopleCountWeightedSumNormalized"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
+ "["
+ "setPeopleCountWeightedAverageNormalized:"
+ "start fetching and rehydrating contact events"
+ "MOAggregationManager.m"
+ "skipping fetching and saving mindful sessions"
+ "skipping fetching and saving visits"
+ "setPeopleCountWeightedSumNormalized:"
+ "PlatformInfoOverrideIsSeedBuild"
+ "MODictionaryEncoder.m"
+ "MORankingParamsMO+CoreDataClass.m"
+ "MOUserData.m"
+ "MOSuggestedEventManager.m"
+ "MOResource.m"
+ "MOInteraction+_CDInteraction.m"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "MOTopicManager.m"
+ "#PhotoMemory,sortedasset,id,%!d(MISSING),asset,%!@(MISSING)"
+ "MOMeasurementTransformer.m"
+ "start fetching and rehydrating workouts"
+ "MOEventPatternDetector.m"
+ "MODataDumpFormatter.m"
+ "MOHealthKitManager.m"
+ "skipping fetching and rehydrating photo memory"
+ "peopleCountWeightedAverageNormalized"
+ "MOEventExtendedAtrributes.m"
+ "skipping fetching and saving music"
+ "MOSummarizationParameters.m"
+ "MOManageServer.m"
+ "skipping fetching and rehydrating workouts"
+ "_peopleCountWeightedSumNormalized"
+ "MOPromptMetrics.m"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "start fetching and saving share with you items"
+ "start fetching and rehydrating state of mind data"
+ "start fetching and rehydrating motion events"
+ "%!@(MISSING), idx, %!l(MISSING)u, interaction, %!@(MISSING)"
+ "MOSharedWithYouManager.m"
+ "skipping fetching and saving people density events"
+ "MOPeopleDiscoveryManager.m"
+ "peopleCountMaxNormalized"
+ "MOGraph.m"
+ "MOEventBundle.m"
+ "start fetching and saving mindful sessions"
+ "MOEventBundleManager.m"
+ "start fetching and saving prox"
+ "start fetching and saving trips"
+ "MOAction.m"
+ "skipping fetching and saving prox"
+ "MOMediaPlaySession.m"
+ "MOEventBundleLabelLocalizer.m"
+ "MOEventData.m"
+ "skipping fetching and saving shared p mom"
+ "MOPhotoManager.m"
+ "MOEventStore.m"
+ "MOSignificantContactManager.m"
+ "(%!f(MISSING))"
+ "start fetching and saving visits"
+ "start fetching and saving photo memory"
+ "MOEventBundleLabelFormat.m"
+ "start fetching and rehydrating music"
+ "start fetching and saving shared p mom"
+ "start fetching and rehydrating prox"
+ "MOEventBundleRanking.m"
+ "MODaemonUniverse.m"
+ "start fetching and saving workouts"
+ "MOEventPatternDetectorFeatureTransformerAggregateEvents.m"
+ "start fetching and saving people density events"
+ "MOAnnotationManager.m"
+ "skipping fetching and saving contact events"
+ "start fetching and rehydrating photo memory"
+ "MODailyAnnotationManager.m"
+ "MODefaultsManager.m"
+ "skipping fetching and rehydrating people density events"
+ "skipping fetching and saving photo memory"
+ "MOEventManager.m"
+ "MODictionaryTransformer.m"
+ "MOStringArrayTransformer.m"
+ "start fetching and saving contact events"
+ "skipping fetching and rehydrating life events"
+ "new conversation created for compound key: %!@(MISSING), for date %!@(MISSING), interaction count, %!l(MISSING)u"
+ "MOPersistenceManager.m"
+ "MOEventBundleLabelTemplate.m"
+ "MOInteraction.m"
+ "_peopleCountWeightedAverageNormalized"
+ "start fetching and rehydrating people density events"
+ "MOContextAnnotationUtilities.m"
+ " ---  Received Interactions Count :%!l(MISSING)u"
+ "skipping training, fetching and rehydrating visits"
+ "start fetching and saving motion events"
+ "start fetching and saving music"
+ "MOTrendBundler.m"
+ "MOLifeEventManager.m"
+ "MONowPlayingMediaManager.m"
+ "skipping fetching and rehydrating music"
+ "MOMediaPlay.m"
+ "skipping fetching and saving share with you items"
+ "MOMotionManager.m"
+ "MOEmbedding.m"
+ "setPeopleCountMaxNormalized:"
+ "MOEventBundleLabelCondition.m"
+ "MOConversation.m"
+ "start training, fetching and rehydrating visits"
+ "MOSummarizationUtilities.m"
+ "TitleAndDayGrouping: media session with description: %!@(MISSING)"
+ "_peopleCountMaxNormalized"
+ "MOTripAnnotationManager.m"
+ "MOEngagementHistoryManager.m"
+ "skipping fetching and saving life events"
+ "CLLocation+MOExtensions.m"
+ " ---  Grouped Interactions Count  :%!l(MISSING)u"
+ "MOMetric.m"
+ "MODaemonClient.m"
+ "skipping fetching and rehydrating state of mind"
+ "MOEventBundler.m"
+ "skipping fetching and saving trips"
+ "start fetching and saving life events"
+ "MOProactiveTravelManager.m"
+ "DailyAnnotation: Event, %!@(MISSING)"
+ "label confidence, label confidence score, %!f(MISSING), actionNameConfidence, %!f(MISSING), concurrentMediaActionNameConfidence, %!f(MISSING), backgroundActionNameConfidence, %!@(MISSING), placeNameConfidence, %!f(MISSING), bundle, %!@(MISSING)"
+ "MORankingParams+CoreDataTransformable.m"
+ "MOEvent.m"
+ "MOTrendsAnalyzerOptions.m"
+ "skipping fetching and rehydrating prox"
+ "]"
+ "MOFSMStore.m"
+ "MOXPCContext.m"
- "setPCountWeightedAverageNormalized:"
- "_pCountWeightedAverageNormalized"
- "Tf,N,V_pCountMaxNormalized"
- "setPCountMaxNormalized:"
- "_pCountWeightedSumNormalized"
- "_pCountMaxNormalized"
- "Tf,N,V_pCountWeightedAverageNormalized"
- "setPCountWeightedSumNormalized:"
- "Tf,N,V_pCountWeightedSumNormalized"

```
