## momentsd

> `/usr/libexec/momentsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 502.0.8.0.0
-  __TEXT.__text: 0x26f798
+  __TEXT.__text: 0x270f40
   __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x1eec0
+  __TEXT.__objc_stubs: 0x1eee0
   __TEXT.__objc_methlist: 0xf4c4
-  __TEXT.__cstring: 0x2580e
+  __TEXT.__cstring: 0x25ebe
   __TEXT.__objc_classname: 0x2025
   __TEXT.__objc_methtype: 0x32ae
-  __TEXT.__objc_methname: 0x37265
-  __TEXT.__oslogstring: 0x34bcb
-  __TEXT.__const: 0x1e80
-  __TEXT.__gcc_except_tab: 0x8678
+  __TEXT.__objc_methname: 0x37305
+  __TEXT.__oslogstring: 0x3539b
+  __TEXT.__const: 0x1e70
+  __TEXT.__gcc_except_tab: 0x8750
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x51
   __TEXT.__swift5_typeref: 0x808

   __TEXT.__swift_as_cont: 0x78
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x71d0
+  __TEXT.__unwind_info: 0x71e8
   __TEXT.__eh_frame: 0x17e8
-  __DATA_CONST.__const: 0xc2e0
-  __DATA_CONST.__cfstring: 0x23180
+  __DATA_CONST.__const: 0xc340
+  __DATA_CONST.__cfstring: 0x23b00
   __DATA_CONST.__objc_classlist: 0x7d8
   __DATA_CONST.__objc_catlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x158

   __DATA_CONST.__got: 0x12b0
   __DATA_CONST.__auth_ptr: 0x330
   __DATA.__objc_const: 0x1aca8
-  __DATA.__objc_selrefs: 0x9ab0
+  __DATA.__objc_selrefs: 0x9ab8
   __DATA.__objc_ivar: 0x1410
   __DATA.__objc_data: 0x5ce0
   __DATA.__data: 0x2168

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8618
-  Symbols:   20070
-  CStrings:  15375
+  Functions: 8625
+  Symbols:   20073
+  CStrings:  15493
 
Symbols:
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ ___62-[MOSignificantContactManager _conversationsFromInteractions:]_block_invoke
+ ___block_descriptor_40_e30_v32?0"MOInteraction"8Q16^B24l
+ _objc_msgSend$localizedStringFromDate:dateStyle:timeStyle:
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
+ "MODwellAtHomeManager.m"
+ "MOEmbedding.m"
+ "MOEngagementHistoryManager.m"
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
+ "MOProactiveTravelManager.m"
+ "MOPromptMetrics.m"
+ "MORankingParams+CoreDataTransformable.m"
+ "MORankingParamsMO+CoreDataClass.m"
+ "MORoutineServiceManager.m"
+ "MOSharedWithYouManager.m"
+ "MOSignificantContactManager.m"
+ "MOStringArrayTransformer.m"
+ "MOSuggestedEventManager.m"
+ "MOSummarizationParameters.m"
+ "MOSummarizationUtilities.m"
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
+ "[generateBehavioralPatternBundles] bundle subtype=%lu, subbundlecount=%lu, phenotypes=%{private}@"
+ "[generateThematicSummarizationBundles] bundle subtype=%lu, subbundlecount=%lu, phenotypes=%{private}@"
+ "]"
+ "_peopleCountMaxNormalized"
+ "_peopleCountWeightedAverageNormalized"
+ "_peopleCountWeightedSumNormalized"
+ "label confidence, label confidence score, %f, actionNameConfidence, %f, concurrentMediaActionNameConfidence, %f, backgroundActionNameConfidence, %@, placeNameConfidence, %f, bundle, %@"
+ "label confidence, label confidence, %f, event bundle, %@"
+ "localizedStringFromDate:dateStyle:timeStyle:"
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
