## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1924.7.1.0.0
-  __TEXT.__text: 0xed570
+1924.8.0.1.0
+  __TEXT.__text: 0xef5c8
   __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x982c
+  __TEXT.__objc_methlist: 0x9964
   __TEXT.__const: 0x8b8
-  __TEXT.__gcc_except_tab: 0x2e1c
-  __TEXT.__cstring: 0xa996
-  __TEXT.__oslogstring: 0xb8ec
+  __TEXT.__gcc_except_tab: 0x2e68
+  __TEXT.__cstring: 0xb0f7
+  __TEXT.__oslogstring: 0xb9a5
   __TEXT.__dlopen_cstrs: 0x17f0
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2a98
+  __TEXT.__unwind_info: 0x2ab8
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1127
-  __TEXT.__objc_methname: 0x21232
-  __TEXT.__objc_methtype: 0x26b6
-  __TEXT.__objc_stubs: 0x12960
-  __DATA_CONST.__got: 0x8d8
-  __DATA_CONST.__const: 0x36c0
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __TEXT.__objc_classname: 0x1146
+  __TEXT.__objc_methname: 0x215a9
+  __TEXT.__objc_methtype: 0x26d8
+  __TEXT.__objc_stubs: 0x12c40
+  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__const: 0x36f0
+  __DATA_CONST.__objc_classlist: 0x4c0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62e0
-  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_selrefs: 0x63a8
+  __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0xcb8
   __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x19e0
-  __AUTH_CONST.__cfstring: 0xb660
-  __AUTH_CONST.__objc_const: 0x12b90
+  __AUTH_CONST.__const: 0x19c0
+  __AUTH_CONST.__cfstring: 0xbb20
+  __AUTH_CONST.__objc_const: 0x12da0
   __AUTH_CONST.__objc_intobj: 0x1128
   __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0xd38
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0xd58
   __DATA.__data: 0x3c8
   __DATA.__bss: 0x600
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x8b0
+  - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 960CE527-EFBD-3262-9A2D-7D5D4C6550F1
-  Functions: 4534
-  Symbols:   15851
-  CStrings:  9066
+  UUID: 668A79CA-565D-3964-8C7B-3124BCCBD21F
+  Functions: 4560
+  Symbols:   15943
+  CStrings:  9185
 
Symbols:
+ +[_PSBackgroundProcessingMetrics sendAnalyticsEvent:]
+ -[_PSBackgroundProcessingMetrics analyticsPayload]
+ -[_PSBackgroundProcessingMetrics fetchedInteractionCount]
+ -[_PSBackgroundProcessingMetrics init]
+ -[_PSBackgroundProcessingMetrics processedInteractionCount]
+ -[_PSBackgroundProcessingMetrics processingTime]
+ -[_PSBackgroundProcessingMetrics setFetchedInteractionCount:]
+ -[_PSBackgroundProcessingMetrics setProcessedInteractionCount:]
+ -[_PSBackgroundProcessingMetrics setProcessingTime:]
+ -[_PSBackgroundProcessingMetrics setStatus:]
+ -[_PSBackgroundProcessingMetrics setUpdatedInteractionCount:]
+ -[_PSBackgroundProcessingMetrics status]
+ -[_PSBackgroundProcessingMetrics updatedInteractionCount]
+ -[_PSBackgroundProcessingTask handleRepeatingTask:].cold.6
+ -[_PSEnsembleModel canonicalIdentifierForSuggestion:]
+ -[_PSEnsembleModel engineStatsMapFromAllSuggestions:]
+ -[_PSEnsembleModel enrichSuggestions:withStatsMap:]
+ -[_PSEnsembleModel statsDictionaryForSuggestions:withStatsMap:]
+ -[_PSHeuristics updateSuggestionProxies:withReasonType:andReason:]
+ -[_PSPredictionContext madTimeOut]
+ -[_PSPredictionContext setMadTimeOut:]
+ -[_PSSuggestion reasonTypeList]
+ -[_PSSuggestion setReasonTypeList:]
+ -[_PSSuggestionProxy setReason:]
+ -[_PSSuggestionProxy setReasonType:]
+ GCC_except_table100
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table168
+ GCC_except_table37
+ GCC_except_table69
+ GCC_except_table74
+ GCC_except_table98
+ GCC_except_table99
+ _OBJC_CLASS_$_NSEntityDescription
+ _OBJC_CLASS_$__PSBackgroundProcessingMetrics
+ _OBJC_IVAR_$__PSBackgroundProcessingMetrics._fetchedInteractionCount
+ _OBJC_IVAR_$__PSBackgroundProcessingMetrics._processedInteractionCount
+ _OBJC_IVAR_$__PSBackgroundProcessingMetrics._processingTime
+ _OBJC_IVAR_$__PSBackgroundProcessingMetrics._status
+ _OBJC_IVAR_$__PSBackgroundProcessingMetrics._updatedInteractionCount
+ _OBJC_IVAR_$__PSBackgroundProcessingTask._metrics
+ _OBJC_IVAR_$__PSPredictionContext._madTimeOut
+ _OBJC_IVAR_$__PSSuggestion._reasonTypeList
+ _OBJC_METACLASS_$__PSBackgroundProcessingMetrics
+ __OBJC_$_CLASS_METHODS__PSBackgroundProcessingMetrics
+ __OBJC_$_INSTANCE_METHODS__PSBackgroundProcessingMetrics
+ __OBJC_$_INSTANCE_VARIABLES__PSBackgroundProcessingMetrics
+ __OBJC_$_PROP_LIST__PSBackgroundProcessingMetrics
+ __OBJC_CLASS_RO_$__PSBackgroundProcessingMetrics
+ __OBJC_METACLASS_RO_$__PSBackgroundProcessingMetrics
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.884
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.885
+ ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.957
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.776
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.694
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.694.cold.1
+ ___132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke.177
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.873
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.873.cold.1
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.102
+ ___63-[_PSEnsembleModel statsDictionaryForSuggestions:withStatsMap:]_block_invoke
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.747
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.609
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.147
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.152
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.156
+ ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.930
+ ___block_descriptor_40_e8_32r_e25_B16?0"NSManagedObject"8lr32l8
+ ___block_descriptor_40_e8_32r_e25_v32?0"NSString"8Q16^B24lr32l8
+ ___block_descriptor_56_e8_32s40s48s_e30_v32?0"_PSSuggestion"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.151
+ ___block_literal_global.159
+ ___block_literal_global.269
+ ___block_literal_global.547
+ ___block_literal_global.592
+ ___block_literal_global.623
+ ___block_literal_global.685
+ ___block_literal_global.786
+ ___block_literal_global.789
+ ___block_literal_global.792
+ ___block_literal_global.795
+ ___block_literal_global.866
+ ___block_literal_global.959
+ _objc_msgSend$analyticsPayload
+ _objc_msgSend$canonicalIdentifierForSuggestion:
+ _objc_msgSend$engineStatsMapFromAllSuggestions:
+ _objc_msgSend$enrichSuggestions:withStatsMap:
+ _objc_msgSend$fetchedInteractionCount
+ _objc_msgSend$hasChanges
+ _objc_msgSend$insertNewObjectForEntityForName:inManagedObjectContext:
+ _objc_msgSend$madTimeOut
+ _objc_msgSend$managedObjectContext
+ _objc_msgSend$mutableSetValueForKey:
+ _objc_msgSend$processedInteractionCount
+ _objc_msgSend$processingTime
+ _objc_msgSend$sendAnalyticsEvent:
+ _objc_msgSend$setFetchedInteractionCount:
+ _objc_msgSend$setMadTimeOut:
+ _objc_msgSend$setProcessedInteractionCount:
+ _objc_msgSend$setProcessingTime:
+ _objc_msgSend$setStatus:
+ _objc_msgSend$setUpdatedInteractionCount:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$statsDictionaryForSuggestions:withStatsMap:
+ _objc_msgSend$updateSuggestionProxies:withReasonType:andReason:
+ _objc_msgSend$updatedInteractionCount
+ _psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:._pasOnceToken269
- GCC_except_table129
- GCC_except_table130
- GCC_except_table131
- GCC_except_table153
- GCC_except_table60
- GCC_except_table68
- GCC_except_table93
- GCC_except_table94
- GCC_except_table95
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.842
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.849
- ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.918
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.737
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.653
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.653.cold.1
- ___132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke.155
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.837
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.837.cold.1
- ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.40
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.708
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.597
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.134
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.139
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.143
- ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.891
- ___block_descriptor_32_e25_B16?0"NSManagedObject"8l
- ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
- ___block_literal_global.133
- ___block_literal_global.267
- ___block_literal_global.538
- ___block_literal_global.580
- ___block_literal_global.611
- ___block_literal_global.644
- ___block_literal_global.747
- ___block_literal_global.750
- ___block_literal_global.753
- ___block_literal_global.756
- ___block_literal_global.830
- ___block_literal_global.920
- _psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:._pasOnceToken267
CStrings:
+ "%.3f"
+ "%@\n\nFullReasonTypeList: [%@]"
+ "%@\n\nPASS heuristics might not be generated because the request for face tags to MediaAnalysisd has exceeded its allocated time budget."
+ "%@ (Rank %@)"
+ "%@:[%@]"
+ "%@:unknown"
+ "@\"_PSBackgroundProcessingMetrics\""
+ "Attachment"
+ "Background processing metrics: %@"
+ "CoversationId: %@ \nScore: %@\n%@"
+ "Final Candidate Stats Dictionary: %@"
+ "Hyper-recent-call"
+ "Hyper-recent-inMsg"
+ "Hyper-recent-opened-thread"
+ "Hyper-recent-outMsg"
+ "In-call-collaboration-heuristic"
+ "In-call-heuristic"
+ "Mismatch in number of interactions to update (%lu) and retrieved object ids (%lu)"
+ "PASSv1"
+ "PASSv2"
+ "PastSharesHeuristic"
+ "PastSharesOfTopDomainURL"
+ "PastSharesWithCurrentApp"
+ "Reason: %@\n\nDescription: The model includes frequency, recency, and content-based features...\n"
+ "Reason: %@ \n\nDescription: This contact is currently in active call session"
+ "Reason: %@ \n\nDescription: This file was received from this conversation"
+ "Reason: Hyper-recent-call Heuristic\n\nDescription: There are recent calls with this contact"
+ "Reason: Hyper-recent-inMsg Heuristic\n\nDescription: There are recent incomming-messaging interaction with this contact(s) person"
+ "Reason: Hyper-recent-opened-thread Heuristic\n\nDescription: There is recent opened messaging thread with this contact(s) person"
+ "Reason: Hyper-recent-outMsg Heuristic\n\nDescription: There are recent outgoing-messaging interaction with this contact(s) person"
+ "Reason: PASSv1 Heuristic\n\nDescription: One of the faces in the shared photo has been matched to this contact"
+ "Reason: PASSv2 Heuristic\n\nDescription: face(s) detected in the shared photo have been shared to this conversation in the past"
+ "Reason: PastSharesHeuristic \n\nDescription: There have been many shares to this conersation in the past"
+ "Reason: PastSharesOfTopDomainURL Heuristic\n\nDescription: shares originating from this url domain are frequently sent to this conversation"
+ "Reason: PastSharesWithCurrentApp Heuristic\n\nDescription: shares originating from this app are frequently sent to this conversation"
+ "Reason: SASS Heuristic\n\nDescription: Similar scene tags has been shared to this contact(s) in the past"
+ "Reason: SharePlayHeuristic \n\nDescription: Prioritize eligible shareplay contact(s) person"
+ "SASS"
+ "SharePlayHeuristic"
+ "T@\"NSString\",C,N,V_reasonTypeList"
+ "TB,N,V_madTimeOut"
+ "TQ,N,V_fetchedInteractionCount"
+ "TQ,N,V_processedInteractionCount"
+ "TQ,N,V_updatedInteractionCount"
+ "Td,N,V_processingTime"
+ "Tq,N,V_status"
+ "_PSBackgroundProcessingMetrics"
+ "_fetchedInteractionCount"
+ "_madTimeOut"
+ "_metrics"
+ "_processedInteractionCount"
+ "_processingTime"
+ "_reasonTypeList"
+ "_status"
+ "_updatedInteractionCount"
+ "analyticsPayload"
+ "candid_%lu"
+ "canonicalIdentifierForSuggestion:"
+ "com.apple.PeopleSuggester.BackgroundProcessing"
+ "engineStatsMapFromAllSuggestions:"
+ "enrichSuggestions:withStatsMap:"
+ "fetchedInteractionCount"
+ "handle:%@"
+ "hasChanges"
+ "insertNewObjectForEntityForName:inManagedObjectContext:"
+ "madExecutionDuration"
+ "madTimeOut"
+ "managedObjectContext"
+ "mutableSetValueForKey:"
+ "name:%@"
+ "photoBasedFeaturesTimeout"
+ "processedInteractionCount"
+ "processingTime"
+ "reasonTypeList"
+ "sendAnalyticsEvent:"
+ "setFetchedInteractionCount:"
+ "setMadTimeOut:"
+ "setProcessedInteractionCount:"
+ "setProcessingTime:"
+ "setReasonTypeList:"
+ "setStatus:"
+ "setUpdatedInteractionCount:"
+ "sortUsingSelector:"
+ "statsDictionaryForSuggestions:withStatsMap:"
+ "updateSuggestionProxies:withReasonType:andReason:"
+ "updatedInteractionCount"
- "Hyper-recent opened thread - PS Rewrite"
- "In-call collaboration heuristic"
- "In-call heuristic"
- "PASS heuristic v1 - PS Rewrite"
- "PASS heuristic v2 - PS Rewrite"
- "PastSharesHeuristic - PS Rewrite"
- "PastSharesOfTopDomainURLHeuristic - PS Rewrite"
- "PastSharesWithCurrentApp heuristic - PS Rewrite"
- "SASS heuristic - PS Rewrite"
- "Score: %@\n%@"
- "T@\"NSString\",R,C,N,V_reason"
- "T@\"NSString\",R,C,N,V_reasonType"

```
