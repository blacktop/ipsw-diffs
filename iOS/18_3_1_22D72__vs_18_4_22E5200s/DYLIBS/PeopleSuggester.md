## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x10c7bc
-  __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0xa96c
-  __TEXT.__const: 0x728
-  __TEXT.__gcc_except_tab: 0x3970
-  __TEXT.__cstring: 0xb0d8
-  __TEXT.__oslogstring: 0xd09a
-  __TEXT.__dlopen_cstrs: 0x1caf
+1892.14.0.4.0
+  __TEXT.__text: 0x10d5cc
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0xad2c
+  __TEXT.__const: 0x738
+  __TEXT.__gcc_except_tab: 0x3950
+  __TEXT.__cstring: 0xb2f3
+  __TEXT.__oslogstring: 0xd23a
+  __TEXT.__dlopen_cstrs: 0x1cb5
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2db8
-  __TEXT.__objc_classname: 0x1355
-  __TEXT.__objc_methname: 0x2455d
-  __TEXT.__objc_methtype: 0x2b00
-  __TEXT.__objc_stubs: 0x15ce0
-  __DATA_CONST.__got: 0x978
-  __DATA_CONST.__const: 0x3238
+  __TEXT.__unwind_info: 0x2ec0
+  __TEXT.__eh_frame: 0x50
+  __TEXT.__objc_classname: 0x1358
+  __TEXT.__objc_methname: 0x248f7
+  __TEXT.__objc_methtype: 0x2b20
+  __TEXT.__objc_stubs: 0x15f60
+  __DATA_CONST.__got: 0x970
+  __DATA_CONST.__const: 0x32b8
   __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d30
+  __DATA_CONST.__objc_selrefs: 0x6ed8
   __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0xe00
-  __AUTH_CONST.__auth_got: 0x778
+  __DATA_CONST.__objc_arraydata: 0xe60
+  __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1aa0
-  __AUTH_CONST.__cfstring: 0xb120
-  __AUTH_CONST.__objc_const: 0x15df8
+  __AUTH_CONST.__const: 0x1ac0
+  __AUTH_CONST.__cfstring: 0xb440
+  __AUTH_CONST.__objc_const: 0x15838
   __AUTH_CONST.__objc_intobj: 0x1290
-  __AUTH_CONST.__objc_arrayobj: 0x918
-  __AUTH_CONST.__objc_doubleobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0xa20
+  __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0xf68
+  __DATA.__objc_ivar: 0xf6c
   __DATA.__data: 0x428
   __DATA.__bss: 0x620
   __DATA_DIRTY.__objc_data: 0x3200

   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/CoreEmoji.framework/CoreEmoji
+  - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary
   - /System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5031
-  Symbols:   6319
-  CStrings:  8396
+  Functions: 5086
+  Symbols:   6381
+  CStrings:  8446
 
Symbols:
+ _DRTailspinRequest
+ _SuggestionProxyTypeHyperRecencyCallRewrite
+ _SuggestionProxyTypePASSv1
+ _SuggestionProxyTypeSASS
- _fmod
- _strcmp
CStrings:
+ "\x06\x11"
+ "1006"
+ "114"
+ "117"
+ "1269"
+ "12835"
+ "144"
+ "15"
+ "1635"
+ "16634"
+ "1765"
+ "493"
+ "898"
+ "@\"_PSSuggestionProxy\"24@?0@\"NSString\"8Q16"
+ "@48@0:8@16@24q32q40"
+ "B24@0:8^@16"
+ "CoreDuet: App Suggestions"
+ "CoreDuet: Candidates for Share Sheet Ranking"
+ "CoreDuet: Share Sheet Suggestions"
+ "CoreDuet: _PSContactSuggester Prior Generation"
+ "Error getting IntelligencePlatform visualIdentifierView: %@"
+ "Failed to report timeout to DiagnosticRequest: %{public}@"
+ "Heuristics config: %@"
+ "No config found for heuristic: %@"
+ "No recency margin found for heuristic: %@"
+ "No slot limit found for heuristic: %@"
+ "PASS heuristic v1 - PS Rewrite"
+ "PASS heuristic v2 - PS Rewrite"
+ "Pruning all candidates that the user never sent a message to nor recently engaged with in the sharing UI."
+ "Reported timeout successfully to DiagnosticRequest"
+ "SASS heuristic - PS Rewrite"
+ "Share Sheet Timeout"
+ "ShareSheetTimeout"
+ "SuggestionProxyTypeHyperRecencyCallRewrite"
+ "SuggestionProxyTypePASSv1"
+ "SuggestionProxyTypeSASS"
+ "Td,N,V_pslRecencyMargin"
+ "TimeSinceLastUIEngagement"
+ "_PSHeuristicsPSLBackfillLimit"
+ "_PSHeuristicsPSLMessagesRecencyLimit"
+ "_PSHeuristicsPSLRecencyMargin"
+ "_PSHeuristicsPSLShareSheetRecencyLimit"
+ "_PSTrialClient: Final configuration is: timeInterval %f, fetchLimit %lu,  maxComputationTimeInSeconds %.2f, featureNamesToSortWith %@, shouldUseSuggestionEngaged %@, statsDefaultValues %@"
+ "_pslRecencyMargin"
+ "com.apple.CoreDuet.PeopleSuggester"
+ "computeSASSFeatureWithScenesDetectedInPhoto:"
+ "contactIdentifiers"
+ "currentConnection"
+ "enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:"
+ "featureCountFor_animal"
+ "featureCountFor_car"
+ "featureCountFor_cat"
+ "featureCountFor_dog"
+ "featureCountFor_fashion"
+ "featureCountFor_food"
+ "featureCountFor_music"
+ "featureCountFor_pet"
+ "featureCountFor_plant"
+ "featureCountFor_sport"
+ "featureCountFor_sunset"
+ "hyperRecentCallHeuristicSuggestionProxiesForInteractionStatistics:"
+ "hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:"
+ "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:"
+ "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:"
+ "logJointProbabilityScore"
+ "maxNumberOfSuggestionSlots"
+ "maxNumberOfSuggestionSlotsForHeuristic:"
+ "numberOfRecentOutgoingInteractionsWithConversation"
+ "numberOfSharesOfPeopleInPhotoIoUWithConversation"
+ "pCk"
+ "pPASS|Ck"
+ "pRecentInteractions|Ck"
+ "pSource|Ck"
+ "pTopLevelDomain|Ck"
+ "peopleAwareSuggestionProxiesForDetectedFaces:"
+ "processIdentifier"
+ "pslRecencyMargin"
+ "publisherWithUseCase:options:"
+ "recencyMarginInSeconds"
+ "recencyMarginInSecondsForHeuristic:"
+ "remoteObjectProxyWithErrorHandler:"
+ "reportShareSheetTimeoutWithError:"
+ "reportShareSheetTimeoutWithReply:"
+ "reporting share sheet timeout (requested by pid %{public}@)"
+ "scenesBasedFeatures"
+ "scenesBasedFeaturesAwareSuggestionProxiesForInteractionStatistics:forFeatureNames:"
+ "scenesBasedFeaturesNames"
+ "scenesMinimumNumberOfTags"
+ "setAppToAppExtMapping:"
+ "setPslRecencyMargin:"
+ "sinkWithCompletion:shouldContinue:"
+ "timeSinceLastPhoneCall"
+ "topLevelScenesFromSceneNetTags:"
+ "visualIdentifierViewWithError:"
- "@\"_PSSuggestionProxy\"16@?0@\"NSString\"8"
- "Duet: App Suggestions"
- "Duet: Candidates for Share Sheet Ranking"
- "Duet: Share Sheet Suggestions"
- "Duet: _PSContactSuggester Prior Generation"
- "P1"
- "P2"
- "P3"
- "P4"
- "PASS heuristic - PS Rewrite"
- "Pruning all candidates that the user never sent a message to."
- "Recency margin: %@."
- "Td,N,V_recencyMargin"
- "_CDInteractionsStatisticsConfig"
- "_PSHeuristicsBackfillLimit"
- "_PSHeuristicsMessagesRecencyLimit"
- "_PSHeuristicsRecencyMargin"
- "_PSHeuristicsShareSheetRecencyLimit"
- "_PSTrialClient: Final configuration is: timeInterval %f, fetchLimit %lu, featureNamesToSortWith %@, shouldSortAscending %@, shouldUseSuggestionEngaged %@, statsDefaultValues %@"
- "_recencyMargin"
- "candidates_with_photo_based_features"
- "copy:to:"
- "count1"
- "count2"
- "count3"
- "count4"
- "enrichConfig:withInformationFromPredictionContext:"
- "hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:"
- "impute:withConstant:"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldSortAscending:shouldUseSuggestionEngaged:statsDefaultValues:"
- "logJointProbability"
- "logPipeline_interactionsStatisticsCandidates_with_photo_based_features"
- "log_P1"
- "log_P2"
- "log_P3"
- "log_P4"
- "partialSum1"
- "partialSum2"
- "pass_data_collection_only"
- "recencyMargin"
- "setRecencyMargin:"
- "setShouldSortAscending:"
- "shouldSortAscending"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreDuetFramework.framework/CoreDuetFramework"

```
