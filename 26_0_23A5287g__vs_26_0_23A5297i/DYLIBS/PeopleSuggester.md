## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1919.0.0.0.0
-  __TEXT.__text: 0xdfd58
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x91fc
-  __TEXT.__const: 0x708
-  __TEXT.__gcc_except_tab: 0x2d34
-  __TEXT.__cstring: 0xa0c3
-  __TEXT.__oslogstring: 0xab83
+1922.0.2.0.0
+  __TEXT.__text: 0xec30c
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_methlist: 0x9804
+  __TEXT.__const: 0x8b8
+  __TEXT.__gcc_except_tab: 0x2d80
+  __TEXT.__cstring: 0xa8cb
+  __TEXT.__oslogstring: 0xb715
   __TEXT.__dlopen_cstrs: 0x17a6
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x28c0
+  __TEXT.__unwind_info: 0x2a40
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x10a7
-  __TEXT.__objc_methname: 0x1f6b9
-  __TEXT.__objc_methtype: 0x268d
-  __TEXT.__objc_stubs: 0x11c60
-  __DATA_CONST.__got: 0x8a0
-  __DATA_CONST.__const: 0x3128
-  __DATA_CONST.__objc_classlist: 0x4a8
+  __TEXT.__objc_classname: 0x1126
+  __TEXT.__objc_methname: 0x210a9
+  __TEXT.__objc_methtype: 0x26b6
+  __TEXT.__objc_stubs: 0x128a0
+  __DATA_CONST.__got: 0x8d8
+  __DATA_CONST.__const: 0x35f0
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f98
-  __DATA_CONST.__objc_superrefs: 0x378
-  __DATA_CONST.__objc_arraydata: 0xb48
-  __AUTH_CONST.__auth_got: 0x7b8
-  __AUTH_CONST.__const: 0x1740
-  __AUTH_CONST.__cfstring: 0x9d80
-  __AUTH_CONST.__objc_const: 0x12518
-  __AUTH_CONST.__objc_intobj: 0xf60
-  __AUTH_CONST.__objc_arrayobj: 0x768
+  __DATA_CONST.__objc_selrefs: 0x62b0
+  __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_arraydata: 0xcb0
+  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__const: 0x1920
+  __AUTH_CONST.__cfstring: 0xb5e0
+  __AUTH_CONST.__objc_const: 0x12b40
+  __AUTH_CONST.__objc_intobj: 0x1128
+  __AUTH_CONST.__objc_arrayobj: 0x810
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0xccc
+  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH.__objc_data: 0x7d0
+  __DATA.__objc_ivar: 0xd30
   __DATA.__data: 0x3c8
-  __DATA.__bss: 0x528
+  __DATA.__bss: 0x5d8
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x8b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 780EA57A-DC32-3E68-8F7E-A7F32943639B
-  Functions: 4316
-  Symbols:   15101
-  CStrings:  8442
+  UUID: AFB07272-B741-32D2-AFCB-417708311F56
+  Functions: 4512
+  Symbols:   15779
+  CStrings:  9036
 
Symbols:
+ +[_PSConstants messagesBundleId]
+ +[_PSEnsembleModel popFeedbackForSession:]
+ +[_PSEnsembleModel saveFeedback:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:]
+ +[_PSPETMessageBuilder getPETMessageWithInteractionsStatistics:predictionContext:deviceIdentifier:trialIdentifier:peopleSuggesterDefaults:]
+ -[_Feedback setTransportBundleId:]
+ -[_Feedback transportBundleId]
+ -[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]
+ -[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]
+ -[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:].cold.1
+ -[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:].cold.2
+ -[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:].cold.3
+ -[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:].cold.4
+ -[_PSEnsembleModel _fallbackPredictionWithPredictionContext:config:parentSpanId:]
+ -[_PSEnsembleModel _fallbackPredictionWithPredictionContext:config:parentSpanId:].cold.1
+ -[_PSEnsembleModel _fallbackPredictionWithPredictionContext:config:parentSpanId:].cold.2
+ -[_PSEnsembleModel _reMapContentTypes:count:]
+ -[_PSEnsembleModel _remapSingleContentTypeValue:]
+ -[_PSEnsembleModel _updateInteractionStatisticsForExplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:]
+ -[_PSEnsembleModel _updateInteractionStatisticsForExplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:].cold.1
+ -[_PSEnsembleModel _updateInteractionStatisticsForExplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:].cold.2
+ -[_PSEnsembleModel _updateInteractionStatisticsForImplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:]
+ -[_PSEnsembleModel _updateInteractionStatisticsForImplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:].cold.1
+ -[_PSEnsembleModel _updateInteractionStatisticsForImplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:].cold.2
+ -[_PSEnsembleModel _updateInteractionStatisticsForSpeculativeEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:]
+ -[_PSEnsembleModel initWithInteractionStore:knowledgeStore:]
+ -[_PSEnsembleModel init].cold.2
+ -[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]
+ -[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:].cold.1
+ -[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:].cold.2
+ -[_PSEnsembleModel sendDataCollectionMessageWith:]
+ -[_PSFeedback shareSheetFeedbackEngagementType]
+ -[_PSInteractionsStatistics .cxx_destruct]
+ -[_PSInteractionsStatistics _updatePropertiesFromRecord:forConversationId:]
+ -[_PSInteractionsStatistics addConversationId:]
+ -[_PSInteractionsStatistics appsSharedFromByConversationId]
+ -[_PSInteractionsStatistics bundleIdForConversationId:]
+ -[_PSInteractionsStatistics computeContentBasedFeaturesForPersonIdsDetectedInPhoto:sceneCategoriesDetectedInPhoto:]
+ -[_PSInteractionsStatistics computeDynamicFeatureWithOperatorName:forArguments:]
+ -[_PSInteractionsStatistics computeDynamicFeatures]
+ -[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]
+ -[_PSInteractionsStatistics computeStatisticsWithInteractionStore:].cold.1
+ -[_PSInteractionsStatistics config]
+ -[_PSInteractionsStatistics containsConversationId:]
+ -[_PSInteractionsStatistics conversationIds]
+ -[_PSInteractionsStatistics descriptionRedacted:]
+ -[_PSInteractionsStatistics description]
+ -[_PSInteractionsStatistics dispatchComputationForBatchFeature:]
+ -[_PSInteractionsStatistics dispatchComputationForContentFeature:personIdsDetectedInPhoto:sceneCategoriesDetectedInPhoto:]
+ -[_PSInteractionsStatistics dispatchComputationForIncrementalFeature:conversationId:interactionRecord:]
+ -[_PSInteractionsStatistics features]
+ -[_PSInteractionsStatistics incrementValueForFeature:andConversationId:]
+ -[_PSInteractionsStatistics initFeature:withValue:]
+ -[_PSInteractionsStatistics initWithConfig:]
+ -[_PSInteractionsStatistics isUsingDefaultValue:forConversationId:]
+ -[_PSInteractionsStatistics mostRecentInteractionTimestampByConversationId]
+ -[_PSInteractionsStatistics nonNilFeaturesForConversationId:]
+ -[_PSInteractionsStatistics personsIdsInPhotosForPastShareInteractions]
+ -[_PSInteractionsStatistics personsIdsInPhotosForPastSyntheticShareInteractions]
+ -[_PSInteractionsStatistics privatizedConversationId:]
+ -[_PSInteractionsStatistics processInteractionRecord:]
+ -[_PSInteractionsStatistics processInteractionRecord:].cold.1
+ -[_PSInteractionsStatistics properties]
+ -[_PSInteractionsStatistics queryStats]
+ -[_PSInteractionsStatistics redactedDescription]
+ -[_PSInteractionsStatistics removeConversationIds:]
+ -[_PSInteractionsStatistics removeFeature:andConversation:]
+ -[_PSInteractionsStatistics savePastSharedPhotoDetectedPersonIds:forConversationId:forSyntheticInteraction:]
+ -[_PSInteractionsStatistics setAppsSharedFromByConversationId:]
+ -[_PSInteractionsStatistics setMostRecentInteractionTimestampByConversationId:]
+ -[_PSInteractionsStatistics setPersonsIdsInPhotosForPastShareInteractions:]
+ -[_PSInteractionsStatistics setPersonsIdsInPhotosForPastSyntheticShareInteractions:]
+ -[_PSInteractionsStatistics setQueryStats:]
+ -[_PSInteractionsStatistics setValue:forFeature:andConversationId:]
+ -[_PSInteractionsStatistics setValue:forProperty:andConversationId:]
+ -[_PSInteractionsStatistics valueForFeature:forConversationId:]
+ -[_PSInteractionsStatistics valueForProperty:forConversationId:]
+ -[_PSInteractionsStatistics valueOrDefaultValueForFeature:forConversationId:]
+ -[_PSInteractionsStatistics(DynamicFeatures) aggregateSumForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) aggregateSumForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) copyFeatureForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) copyFeatureForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) divideWithDivisorForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) divideWithDivisorForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) exponentialWithMultiplierForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) exponentialWithMultiplierForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) imputeFeatureForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) imputeFeatureForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) laplaceProbabilityWithAlphaForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) laplaceProbabilityWithAlphaForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) logWithBaseForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) logWithBaseForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) multiplyWithKeyForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) multiplyWithKeyForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) mutliplyWithScalarForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) mutliplyWithScalarForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) powerWithExponentForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) powerWithExponentForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) reciprocalWithOffsetForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) reciprocalWithOffsetForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) renameFeatureForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) renameFeatureForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) sumWithAddendForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) sumWithAddendForArguments:].cold.1
+ -[_PSInteractionsStatistics(DynamicFeatures) sumWithKeyForArguments:]
+ -[_PSInteractionsStatistics(DynamicFeatures) sumWithKeyForArguments:].cold.1
+ -[_PSInteractionsStatistics(PrivacyMitigation) privacyMitigatedFeatureValueFromName:forConversationId:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeAppsSharedFromForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeHasEverSharePlayedWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeIsFirstPartyAppForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeMaxIoUOfSharesOfPeopleInPhotoForPeopleDetectedInPhoto:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeMaxIoUOfSharesOfPeopleInPhotoForPeopleDetectedInPhoto:].cold.1
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfAppsSharedFromWithConversation]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfEngagedSuggestionsFromCurrentAppWithConversationForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfEngagedSuggestionsOfDetectedPeopleForPeopleDetectedInPhoto:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfEngagedSuggestionsOfPeopleInPhoto]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfEngagedSuggestionsOfTopDomainURLWithConversationForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfEngagedSuggestionsToTargetApp]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfEngagedSuggestionsWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfFacesSharedWithConversation]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfIncomingInteractionsWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:].cold.1
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfOutgoingInteractionsWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfRecentOutgoingInteractionsWithConversationForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesFromCurrentAppWithConversationForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesOfDetectedPeopleForPeopleDetectedInPhoto:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesOfDetectedScenesInPhotoForSceneCategoriesDetectedInPhoto:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesOfPeopleInPhoto]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesOfScenesInPhoto]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesOfTopDomainURLWithConversationForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesToTargetApp]
+ -[_PSInteractionsStatistics(StaticFeatures) computeNumberOfSharesWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computePhotoFeaturesForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeScenesBasedFeaturesForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastIncomingInteractionForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastOutgoingInteractionForConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastPhotoShareWithConversationId:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastShareWithConversation:interactionRecord:]
+ -[_PSInteractionsStatistics(StaticFeatures) computeTimeSinceLastUIEngagementForConversationId:interactionRecord:]
+ -[_PSInteractionsStatisticsConfig .cxx_destruct]
+ -[_PSInteractionsStatisticsConfig _appBundleIdForAppExtBundleId:]
+ -[_PSInteractionsStatisticsConfig anchorDate]
+ -[_PSInteractionsStatisticsConfig anchorTimeStamp]
+ -[_PSInteractionsStatisticsConfig appBundleIdForRecord:]
+ -[_PSInteractionsStatisticsConfig communicationInteractionPredicate]
+ -[_PSInteractionsStatisticsConfig configuredSceneCategoryTagNames]
+ -[_PSInteractionsStatisticsConfig defaultValues]
+ -[_PSInteractionsStatisticsConfig detectedSceneCategoryNamesFromSceneNetTags:]
+ -[_PSInteractionsStatisticsConfig dynamicFeatureRecipe]
+ -[_PSInteractionsStatisticsConfig fetchLimit]
+ -[_PSInteractionsStatisticsConfig initWithSourceBundleId:anchorDate:leftBoundDate:fetchLimit:maxComputationTime:shouldUseSuggestionEngaged:sortOrderFeatureNames:statsDefaultValues:sceneCategoryTagMapping:sceneCategoryTagThresholds:]
+ -[_PSInteractionsStatisticsConfig isFallbackFetch]
+ -[_PSInteractionsStatisticsConfig isWeekendShare]
+ -[_PSInteractionsStatisticsConfig leftBoundDate]
+ -[_PSInteractionsStatisticsConfig maxComputationTime]
+ -[_PSInteractionsStatisticsConfig rightBoundDate]
+ -[_PSInteractionsStatisticsConfig sceneCategoryTagMapping]
+ -[_PSInteractionsStatisticsConfig sceneTagThresholdForSceneCategoryName:]
+ -[_PSInteractionsStatisticsConfig setAnchorDate:]
+ -[_PSInteractionsStatisticsConfig setDefaultValues:]
+ -[_PSInteractionsStatisticsConfig setDynamicFeatureRecipe:]
+ -[_PSInteractionsStatisticsConfig setFetchLimit:]
+ -[_PSInteractionsStatisticsConfig setIsFallbackFetch:]
+ -[_PSInteractionsStatisticsConfig setLookBackTimeInterval:]
+ -[_PSInteractionsStatisticsConfig setMaxComputationTime:]
+ -[_PSInteractionsStatisticsConfig setSceneCategoryTagMapping:]
+ -[_PSInteractionsStatisticsConfig setSceneCategoryTagThresholds:]
+ -[_PSInteractionsStatisticsConfig setShouldUseSuggestionEngaged:]
+ -[_PSInteractionsStatisticsConfig setSortOrderFeatureNames:]
+ -[_PSInteractionsStatisticsConfig setSourceBundleId:]
+ -[_PSInteractionsStatisticsConfig setStaticFeatures:]
+ -[_PSInteractionsStatisticsConfig setTopDomainURL:]
+ -[_PSInteractionsStatisticsConfig shareSheetCommunicationInteractionsSelectionPredicateWithStartDate:endDate:]
+ -[_PSInteractionsStatisticsConfig shareSheetSharingInteractionsSelectionPredicateWithStartDate:endDate:]
+ -[_PSInteractionsStatisticsConfig sharingInteractionPredicate]
+ -[_PSInteractionsStatisticsConfig shouldUseSuggestionEngaged]
+ -[_PSInteractionsStatisticsConfig sortOrderFeatureNames]
+ -[_PSInteractionsStatisticsConfig sourceBundleId]
+ -[_PSInteractionsStatisticsConfig staticFeatures]
+ -[_PSInteractionsStatisticsConfig topDomainURL]
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:].cold.1
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:].cold.2
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:].cold.3
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:].cold.4
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:].cold.5
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:].cold.6
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:]
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:].cold.1
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:].cold.2
+ -[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:].cold.3
+ -[_PSSuggester _stringFromValue:]
+ -[_PSSuggester convertCoreAnalyticsEvent2BiomeEvent:]
+ -[_PSSuggester donateCA2Biome:]
+ -[_PSSuggester donateCA2Biome:].cold.1
+ -[_PSTrialClient arrayForKey:]
+ -[_PSTrialClient arrayForKey:].cold.1
+ -[_PSTrialClient arrayForKey:].cold.2
+ -[_PSTrialClient arrayOfArraysForKey:]
+ -[_PSTrialClient arrayOfArraysForKey:].cold.1
+ -[_PSTrialClient arrayOfArraysForKey:].cold.2
+ -[_PSTrialClient boolForKey:]
+ -[_PSTrialClient boolForKey:].cold.1
+ -[_PSTrialClient boolForKey:].cold.2
+ -[_PSTrialClient containsKey:]
+ -[_PSTrialClient doubleForKey:]
+ -[_PSTrialClient doubleForKey:].cold.1
+ -[_PSTrialClient doubleForKey:].cold.2
+ -[_PSTrialClient integerForKey:]
+ -[_PSTrialClient integerForKey:].cold.1
+ -[_PSTrialClient integerForKey:].cold.2
+ -[_PSTrialClient mutableDictionaryForKey:]
+ -[_PSTrialClient mutableDictionaryForKey:].cold.1
+ -[_PSTrialClient mutableDictionaryForKey:].cold.2
+ -[_PSTrialClient mutableDictionaryOfSetsForKey:]
+ -[_PSTrialClient mutableDictionaryOfSetsForKey:].cold.1
+ -[_PSTrialClient mutableDictionaryOfSetsForKey:].cold.2
+ -[_PSTrialClient mutableDictionaryOfSetsForKey:].cold.3
+ -[_PSTrialClient mutableDictionaryOfSetsForKey:].cold.4
+ -[_PSTrialClient updateConfigWithTrialOverrides:]
+ GCC_except_table105
+ GCC_except_table130
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table80
+ GCC_except_table93
+ GCC_except_table94
+ GCC_except_table97
+ _CFStringCompare
+ _OBJC_CLASS_$_BMMLSEShareSheetFeedback
+ _OBJC_CLASS_$_BMMLSEShareSheetInferencePeopleSuggestions
+ _OBJC_CLASS_$_BMMLSEShareSheetMetricsSystemResourceUsage
+ _OBJC_CLASS_$_BMPeopleSuggesterEventLevelMetrics
+ _OBJC_CLASS_$_BMShareEvent
+ _OBJC_CLASS_$__PSInteractionsStatistics
+ _OBJC_CLASS_$__PSInteractionsStatisticsConfig
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$__Feedback._transportBundleId
+ _OBJC_IVAR_$__PSInteractionsStatistics._appsSharedFromByConversationId
+ _OBJC_IVAR_$__PSInteractionsStatistics._config
+ _OBJC_IVAR_$__PSInteractionsStatistics._features
+ _OBJC_IVAR_$__PSInteractionsStatistics._mostRecentInteractionTimestampByConversationId
+ _OBJC_IVAR_$__PSInteractionsStatistics._personsIdsInPhotosForPastShareInteractions
+ _OBJC_IVAR_$__PSInteractionsStatistics._personsIdsInPhotosForPastSyntheticShareInteractions
+ _OBJC_IVAR_$__PSInteractionsStatistics._properties
+ _OBJC_IVAR_$__PSInteractionsStatistics._queryStats
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._anchorDate
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._anchorTimeStamp
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._defaultValues
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._dynamicFeatureRecipe
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._fetchLimit
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._isFallbackFetch
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._isWeekendShare
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._leftBoundDate
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._maxComputationTime
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._rightBoundDate
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._sceneCategoryTagMapping
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._sceneCategoryTagThresholds
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._shareExtToAppBundleIdMapping
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._shouldUseSuggestionEngaged
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._sortOrderFeatureNames
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._sourceBundleId
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._staticFeatures
+ _OBJC_IVAR_$__PSInteractionsStatisticsConfig._topDomainURL
+ _OBJC_METACLASS_$__PSInteractionsStatistics
+ _OBJC_METACLASS_$__PSInteractionsStatisticsConfig
+ _OUTLINED_FUNCTION_8
+ _PSDynamicFeatureOperatorAsString
+ _PSDynamicFeatureOperatorFromString
+ _PSInteractionsStatisticsDynamicFeatureOperatorSortedEnums
+ _PSInteractionsStatisticsDynamicFeatureOperatorSortedStrings
+ _PSInteractionsStatisticsDynamicFeatureOperatorSortedStringsCount
+ _PSStaticFeatureAsString
+ _PSStaticFeatureFromString
+ __MergedGlobals
+ __OBJC_$_INSTANCE_METHODS__PSInteractionsStatistics(StaticFeatures|DynamicFeatures|PrivacyMitigation)
+ __OBJC_$_INSTANCE_METHODS__PSInteractionsStatisticsConfig(DefaultConfig)
+ __OBJC_$_INSTANCE_VARIABLES__PSInteractionsStatistics
+ __OBJC_$_INSTANCE_VARIABLES__PSInteractionsStatisticsConfig
+ __OBJC_$_PROP_LIST__PSInteractionsStatistics
+ __OBJC_$_PROP_LIST__PSInteractionsStatisticsConfig
+ __OBJC_CLASS_RO_$__PSInteractionsStatistics
+ __OBJC_CLASS_RO_$__PSInteractionsStatisticsConfig
+ __OBJC_METACLASS_RO_$__PSInteractionsStatistics
+ __OBJC_METACLASS_RO_$__PSInteractionsStatisticsConfig
+ ___101-[_PSInteractionsStatistics(StaticFeatures) computePhotoFeaturesForConversationId:interactionRecord:]_block_invoke
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.421
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.422
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.842
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.849
+ ___107-[_PSInteractionsStatistics(StaticFeatures) computeScenesBasedFeaturesForConversationId:interactionRecord:]_block_invoke
+ ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke
+ ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.918
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.737
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.653
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.653.cold.1
+ ___139-[_PSEnsembleModel _updateInteractionStatisticsForSpeculativeEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:]_block_invoke
+ ___139-[_PSEnsembleModel _updateInteractionStatisticsForSpeculativeEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:]_block_invoke.cold.1
+ ___140-[_PSInteractionsStatistics(StaticFeatures) computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:]_block_invoke
+ ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.52
+ ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.57
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.254
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.254.cold.1
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.270
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.296
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.298
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.300
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.302
+ ___24-[_PSEnsembleModel init]_block_invoke_4
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.72
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.72.cold.1
+ ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.290
+ ___42+[_PSEnsembleModel popFeedbackForSession:]_block_invoke
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.70
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.70.cold.1
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.74
+ ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.433
+ ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.471
+ ___47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.87
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.269
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.270
+ ___49-[_PSInteractionsStatistics descriptionRedacted:]_block_invoke
+ ___49-[_PSInteractionsStatistics descriptionRedacted:]_block_invoke_2
+ ___49-[_PSInteractionsStatistics descriptionRedacted:]_block_invoke_3
+ ___49-[_PSInteractionsStatisticsConfig setAnchorDate:]_block_invoke
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.837
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.837.cold.1
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.40
+ ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.248
+ ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.121
+ ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.124
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.39
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.43
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.45
+ ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.260
+ ___58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.115
+ ___60-[_PSKNNModel rankedMapsShareEtaSuggestions:maxSuggestions:]_block_invoke.357
+ ___61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.104
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.529
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.529.cold.1
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.281
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.281.cold.1
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.284
+ ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.263
+ ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke
+ ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke.80
+ ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke_2
+ ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke_2.84
+ ___67-[_PSMediaAnalysisProcessingTask executeTaskWithCompletionHandler:]_block_invoke.239
+ ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.296
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.708
+ ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.287
+ ___68-[_PSSuggester showNotificationToFileARadarForUserStudyParticipants]_block_invoke.153
+ ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.293
+ ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.490
+ ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.299
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.371
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.376
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.379
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.394
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.400
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.407
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.404
+ ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.305
+ ___77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.44
+ ___78-[_PSInteractionsStatisticsConfig detectedSceneCategoryNamesFromSceneNetTags:]_block_invoke
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.204
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.221
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.228
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.228.cold.1
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.235
+ ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.194
+ ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.194.cold.1
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.596
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.252
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.255
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.256
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.257
+ ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.266
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.134
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.139
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.143
+ ___90-[_PSInteractionsStatistics(StaticFeatures) computeNumberOfAppsSharedFromWithConversation]_block_invoke
+ ___91-[_PSContactSuggester contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.22
+ ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke
+ ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.891
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke.84
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke_2
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke_2.581
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke_3
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke_4
+ ___92-[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:]_block_invoke
+ ___92-[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:]_block_invoke_2
+ ___92-[_PSInteractionsStatisticsConfig(DefaultConfig) initFallbackConfigWithBundleId:anchorDate:]_block_invoke_3
+ ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke
+ ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.460
+ ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke_2
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.52
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.55
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.59
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.59.cold.1
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.59.cold.2
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.71
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.71.cold.1
+ ___96-[_PSSuggester(InteractionInformation) interactionCountForHandle:fetchLimit:interactionStoreDB:]_block_invoke.138
+ ___99+[_PSEnsembleModel saveFeedback:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:]_block_invoke
+ ___99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.224
+ ___Block_byref_object_copy_.202
+ ___Block_byref_object_copy_.303
+ ___Block_byref_object_dispose_.203
+ ___Block_byref_object_dispose_.304
+ ___PSDynamicFeatureOperatorFromString_block_invoke
+ ___PSStaticFeatureFromString_block_invoke
+ ____PSShareSheetSuggestionBundleIDMapping_block_invoke.41
+ ___block_descriptor_32_e29_16?0"_CDAttachmentRecord"8l
+ ___block_descriptor_40_e8_32r_e37_v28?0"_CDInteractionRecord"8i16^B20lr32l8
+ ___block_descriptor_40_e8_32s_e31_v24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32s_e37_v28?0"_CDInteractionRecord"8i16^B20ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSMutableSet"16^B24ls32l8
+ ___block_descriptor_49_e8_32s40s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e37_v28?0"_CDInteractionRecord"8i16^B20ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48s_e32_v32?0"NSString"8"NSSet"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8s48l8
+ ___block_literal_global.103
+ ___block_literal_global.106
+ ___block_literal_global.127
+ ___block_literal_global.133
+ ___block_literal_global.138
+ ___block_literal_global.142
+ ___block_literal_global.146
+ ___block_literal_global.147
+ ___block_literal_global.230
+ ___block_literal_global.231
+ ___block_literal_global.239
+ ___block_literal_global.247
+ ___block_literal_global.251
+ ___block_literal_global.262
+ ___block_literal_global.268
+ ___block_literal_global.272
+ ___block_literal_global.279
+ ___block_literal_global.283
+ ___block_literal_global.286
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.298
+ ___block_literal_global.304
+ ___block_literal_global.32
+ ___block_literal_global.329
+ ___block_literal_global.334
+ ___block_literal_global.336
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.350
+ ___block_literal_global.356
+ ___block_literal_global.374
+ ___block_literal_global.378
+ ___block_literal_global.38
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.397
+ ___block_literal_global.403
+ ___block_literal_global.406
+ ___block_literal_global.409
+ ___block_literal_global.42
+ ___block_literal_global.432
+ ___block_literal_global.437
+ ___block_literal_global.45
+ ___block_literal_global.456
+ ___block_literal_global.462
+ ___block_literal_global.48
+ ___block_literal_global.488
+ ___block_literal_global.500
+ ___block_literal_global.503
+ ___block_literal_global.51
+ ___block_literal_global.528
+ ___block_literal_global.537
+ ___block_literal_global.54
+ ___block_literal_global.579
+ ___block_literal_global.583
+ ___block_literal_global.610
+ ___block_literal_global.643
+ ___block_literal_global.72
+ ___block_literal_global.73
+ ___block_literal_global.747
+ ___block_literal_global.75
+ ___block_literal_global.750
+ ___block_literal_global.753
+ ___block_literal_global.756
+ ___block_literal_global.77
+ ___block_literal_global.830
+ ___block_literal_global.86
+ ___block_literal_global.89
+ ___block_literal_global.91
+ ___block_literal_global.920
+ ___block_literal_global.97
+ __defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:._pasExprOnceResult
+ __defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:._pasOnceToken117
+ __feedbackDictionary
+ __suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken161
+ _bsearch_b
+ _computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:._pasExprOnceResult
+ _computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:._pasOnceToken2
+ _init._pasExprOnceResult
+ _init._pasOnceToken8
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.40
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.43
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.580
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.70
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.83
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken10
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken11
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken12
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken13
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken22
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken23
+ _initFallbackConfigWithBundleId:anchorDate:._pasExprOnceResult
+ _initFallbackConfigWithBundleId:anchorDate:._pasExprOnceResult.11
+ _initFallbackConfigWithBundleId:anchorDate:._pasExprOnceResult.14
+ _initFallbackConfigWithBundleId:anchorDate:._pasOnceToken7
+ _initFallbackConfigWithBundleId:anchorDate:._pasOnceToken8
+ _initFallbackConfigWithBundleId:anchorDate:._pasOnceToken9
+ _kAggregateSum
+ _kCopyTo
+ _kDefaultMaxComputationTime
+ _kDivideWithDivisorKey
+ _kExponentialWithMultiplier
+ _kImputeWithConstant
+ _kLaplaceProbabilityWithAlphaKey
+ _kLogWithBase
+ _kMultiplyWithKey
+ _kMultiplyWithScalar
+ _kPSBaggageFeatureCoreMLModelScore
+ _kPSBaggageFeatureSuggestedRank
+ _kPSBaggageFeatureUserFeedback
+ _kPSPropertyNameConversationBundleId
+ _kPSPropertyNameConversationGroupName
+ _kPSPropertyNameConversationINImageURL
+ _kPSPropertyNamePrivatizedConversationIdentifier
+ _kPSPropertyNameRecipientListConversationId
+ _kPSStaticBatchFeatureNumberOfDifferentFacesSharedWithConversationAsString
+ _kPSStaticBatchFeatureNumberOfEngagedSuggestionsOfPeopleInPhotoWithConversationAsString
+ _kPSStaticBatchFeatureNumberOfEngagedSuggestionsToTargetAppAsString
+ _kPSStaticBatchFeatureNumberOfSharesOfPeopleInPhotoWithConversationAsString
+ _kPSStaticBatchFeatureNumberOfSharesOfScenesInPhotoWithConversationAsString
+ _kPSStaticBatchFeatureNumberOfTotalSharesToTargetAppAsString
+ _kPSStaticContentFeatureMaxIoUOfSharesOfPeopleInPhotoWithConversationAsString
+ _kPSStaticContentFeatureNumberOfEngagedSuggestionsOfDetectedPeopleWithConversationAsString
+ _kPSStaticContentFeatureNumberOfSharesOfDetectedPeopleWithConversationAsString
+ _kPSStaticContentFeatureNumberOfSharesOfDetectedScenesInPhotoWithConversationAsString
+ _kPSStaticFeatureSortedEnums
+ _kPSStaticFeatureSortedStrings
+ _kPSStaticFeatureSortedStringsCount
+ _kPSStaticFeatureUnknownAsString
+ _kPSStaticIncrementalFeatureHasEverSharePlayedWithConversationAsString
+ _kPSStaticIncrementalFeatureIsFirstPartyAppAsString
+ _kPSStaticIncrementalFeatureNumberOfAppsSharedFromWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfEngagedSuggestionsFromCurrentAppWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfEngagedSuggestionsOfTopDomainURLWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfEngagedSuggestionsWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfIncomingInteractionsWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfInteractionsDuringTimePeriodWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfOutgoingInteractionsWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfRecentOutgoingInteractionsWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfSharesFromCurrentAppWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfSharesOfTopDomainURLWithConversationAsString
+ _kPSStaticIncrementalFeatureNumberOfSharesWithConversationAsString
+ _kPSStaticIncrementalFeaturePhotoFeaturesForConversationIdAsString
+ _kPSStaticIncrementalFeatureScenesBasedFeaturesAsString
+ _kPSStaticIncrementalFeatureTimeSinceLastIncomingInteractionAsString
+ _kPSStaticIncrementalFeatureTimeSinceLastOutgoingInteractionAsString
+ _kPSStaticIncrementalFeatureTimeSinceLastPhoneCallWithConversationAsString
+ _kPSStaticIncrementalFeatureTimeSinceLastPhotoShareWithConversationAsString
+ _kPSStaticIncrementalFeatureTimeSinceLastShareWithConversationAsString
+ _kPSStaticIncrementalFeatureTimeSinceLastUIEngagementAsString
+ _kPowerWithExponentKey
+ _kReciprocalWithOffsetKey
+ _kRenameKey
+ _kSumWithAddend
+ _kSumWithKey
+ _kUnknownOperator
+ _log
+ _objc_msgSend$Inference
+ _objc_msgSend$Metrics
+ _objc_msgSend$PeopleSuggestions
+ _objc_msgSend$SystemResourceUsage
+ _objc_msgSend$_conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:
+ _objc_msgSend$_defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:
+ _objc_msgSend$_fallbackPredictionWithPredictionContext:config:parentSpanId:
+ _objc_msgSend$_reMapContentTypes:count:
+ _objc_msgSend$_remapSingleContentTypeValue:
+ _objc_msgSend$_stringFromValue:
+ _objc_msgSend$_updateInteractionStatisticsForExplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:
+ _objc_msgSend$_updateInteractionStatisticsForImplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:
+ _objc_msgSend$_updateInteractionStatisticsForSpeculativeEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:
+ _objc_msgSend$_updatePropertiesFromRecord:forConversationId:
+ _objc_msgSend$addConversationId:
+ _objc_msgSend$aggregateSumForArguments:
+ _objc_msgSend$anchorDate
+ _objc_msgSend$anchorTimeStamp
+ _objc_msgSend$appBundleIdForRecord:
+ _objc_msgSend$appSharedFrom
+ _objc_msgSend$appsSharedFromByConversationId
+ _objc_msgSend$arrayOfArraysForKey:
+ _objc_msgSend$autoupdatingCurrentCalendar
+ _objc_msgSend$candidates
+ _objc_msgSend$communicationInteractionPredicate
+ _objc_msgSend$computeAppsSharedFromForConversationId:interactionRecord:
+ _objc_msgSend$computeContentBasedFeaturesForPersonIdsDetectedInPhoto:sceneCategoriesDetectedInPhoto:
+ _objc_msgSend$computeDynamicFeatures
+ _objc_msgSend$computeHasEverSharePlayedWithConversationId:interactionRecord:
+ _objc_msgSend$computeIsFirstPartyAppForConversationId:interactionRecord:
+ _objc_msgSend$computeMaxIoUOfSharesOfPeopleInPhotoForPeopleDetectedInPhoto:
+ _objc_msgSend$computeNumberOfEngagedSuggestionsFromCurrentAppWithConversationForConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfEngagedSuggestionsOfDetectedPeopleForPeopleDetectedInPhoto:
+ _objc_msgSend$computeNumberOfEngagedSuggestionsOfPeopleInPhoto
+ _objc_msgSend$computeNumberOfEngagedSuggestionsOfTopDomainURLWithConversationForConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfEngagedSuggestionsToTargetApp
+ _objc_msgSend$computeNumberOfEngagedSuggestionsWithConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfFacesSharedWithConversation
+ _objc_msgSend$computeNumberOfIncomingInteractionsWithConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfOutgoingInteractionsWithConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfRecentOutgoingInteractionsWithConversationForConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfSharesFromCurrentAppWithConversationForConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfSharesOfDetectedPeopleForPeopleDetectedInPhoto:
+ _objc_msgSend$computeNumberOfSharesOfDetectedScenesInPhotoForSceneCategoriesDetectedInPhoto:
+ _objc_msgSend$computeNumberOfSharesOfPeopleInPhoto
+ _objc_msgSend$computeNumberOfSharesOfScenesInPhoto
+ _objc_msgSend$computeNumberOfSharesOfTopDomainURLWithConversationForConversationId:interactionRecord:
+ _objc_msgSend$computeNumberOfSharesToTargetApp
+ _objc_msgSend$computeNumberOfSharesWithConversationId:interactionRecord:
+ _objc_msgSend$computePhotoFeaturesForConversationId:interactionRecord:
+ _objc_msgSend$computeScenesBasedFeaturesForConversationId:interactionRecord:
+ _objc_msgSend$computeStatisticsWithInteractionStore:
+ _objc_msgSend$computeTimeSinceLastIncomingInteractionForConversationId:interactionRecord:
+ _objc_msgSend$computeTimeSinceLastOutgoingInteractionForConversationId:interactionRecord:
+ _objc_msgSend$computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:
+ _objc_msgSend$computeTimeSinceLastPhotoShareWithConversationId:interactionRecord:
+ _objc_msgSend$computeTimeSinceLastShareWithConversation:interactionRecord:
+ _objc_msgSend$computeTimeSinceLastUIEngagementForConversationId:interactionRecord:
+ _objc_msgSend$containsConversationId:
+ _objc_msgSend$containsKey:
+ _objc_msgSend$convertCoreAnalyticsEvent2BiomeEvent:
+ _objc_msgSend$copyFeatureForArguments:
+ _objc_msgSend$defaultValues
+ _objc_msgSend$dictionaryForKey:
+ _objc_msgSend$divideWithDivisorForArguments:
+ _objc_msgSend$donateCA2Biome:
+ _objc_msgSend$dynamicFeatureRecipe
+ _objc_msgSend$exponentialWithMultiplierForArguments:
+ _objc_msgSend$feedbackEvents
+ _objc_msgSend$fetchLimit
+ _objc_msgSend$generateConversationIdFromInteractionRecipientRecords:
+ _objc_msgSend$getPETMessageWithInteractionsStatistics:predictionContext:deviceIdentifier:trialIdentifier:peopleSuggesterDefaults:
+ _objc_msgSend$imputeFeatureForArguments:
+ _objc_msgSend$incrementValueForFeature:andConversationId:
+ _objc_msgSend$initDefaultConfigWithBundleId:anchorDate:
+ _objc_msgSend$initFallbackConfigWithBundleId:anchorDate:
+ _objc_msgSend$initWithConfig:
+ _objc_msgSend$initWithDeviceIdentifier:sessionId:trialIdentifiers:version:candidates:testKey:madResponseStatus:isFallbackFetch:isSharePlayAvailable:appSharedFrom:feedbackEvents:typeOfContent:isInPhoneCall:timeSinceLastShare:isScreenShot:photoFeatures:
+ _objc_msgSend$initWithIdentifier:engagementType:engagementIdentifier:visiblePeopleSuggestionCount:visibleAppSuggestionCount:airdropPeopleSuggestionShown:inferenceSource:trialIdentifier:timeouts:productInsights:
+ _objc_msgSend$initWithIdentifier:sourceBundleId:peopleSuggestions:responseType:trainingDataCollection:
+ _objc_msgSend$initWithIndexSelected:engagedSuggestionProxyReason:engagedSuggestionProxy:engagedSuggestionProxyDebug:airdropShown:airdropEngaged:sharePlayAvailable:sharePlayEngaged:appSharingIntent:engagementType:suggestionAvailable:suggestionNumber:numberOfVisibleSuggestions:peopleSuggestionsSetting:transportApp:sourceApp:contentShared:sessionId:userExperienceFlow:sessionLatency:modelTimeout:suggestionPath:suggestionPathDebug:trialDeploymentId:trialExperimentId:trialTreatmentId:isPhotos:PSRActive:sessionDelayInMilliseconds:datestamp:
+ _objc_msgSend$initWithSoftwareTracing:
+ _objc_msgSend$initWithSourceBundleId:anchorDate:leftBoundDate:fetchLimit:maxComputationTime:shouldUseSuggestionEngaged:sortOrderFeatureNames:statsDefaultValues:sceneCategoryTagMapping:sceneCategoryTagThresholds:
+ _objc_msgSend$isInPhoneCall
+ _objc_msgSend$isScreenShot
+ _objc_msgSend$isWeekendShare
+ _objc_msgSend$iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:
+ _objc_msgSend$laplaceProbabilityWithAlphaForArguments:
+ _objc_msgSend$leftBoundDate
+ _objc_msgSend$logWithBaseForArguments:
+ _objc_msgSend$madResponseStatus
+ _objc_msgSend$multiplyWithKeyForArguments:
+ _objc_msgSend$mutableDictionaryForKey:
+ _objc_msgSend$mutableDictionaryOfSetsForKey:
+ _objc_msgSend$mutliplyWithScalarForArguments:
+ _objc_msgSend$personsIdsInPhotosForPastShareInteractions
+ _objc_msgSend$personsIdsInPhotosForPastSyntheticShareInteractions
+ _objc_msgSend$photoFeatures
+ _objc_msgSend$photoSceneDescriptor
+ _objc_msgSend$popFeedbackForSession:
+ _objc_msgSend$powerWithExponentForArguments:
+ _objc_msgSend$processInteractionRecord:
+ _objc_msgSend$psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:
+ _objc_msgSend$reciprocalWithOffsetForArguments:
+ _objc_msgSend$removeFeature:andConversation:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$renameFeatureForArguments:
+ _objc_msgSend$saveFeedbackInCoreDuetd:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:reply:
+ _objc_msgSend$savePastSharedPhotoDetectedPersonIds:forConversationId:forSyntheticInteraction:
+ _objc_msgSend$sceneCategoryTagMapping
+ _objc_msgSend$sceneTagThresholdForSceneCategoryName:
+ _objc_msgSend$sendDataCollectionMessageWith:
+ _objc_msgSend$sessionId
+ _objc_msgSend$setDefaultValues:
+ _objc_msgSend$setDynamicFeatureRecipe:
+ _objc_msgSend$setLookBackTimeInterval:
+ _objc_msgSend$setMaxComputationTime:
+ _objc_msgSend$setSceneCategoryTagMapping:
+ _objc_msgSend$setSceneCategoryTagThresholds:
+ _objc_msgSend$setShouldUseSuggestionEngaged:
+ _objc_msgSend$setSortOrderFeatureNames:
+ _objc_msgSend$setStaticFeatures:
+ _objc_msgSend$setTransportBundleId:
+ _objc_msgSend$setValue:forProperty:andConversationId:
+ _objc_msgSend$shareSheetFeedbackEngagementType
+ _objc_msgSend$sharingInteractionPredicate
+ _objc_msgSend$shouldUseSuggestionEngaged
+ _objc_msgSend$sortOrderFeatureNames
+ _objc_msgSend$sourceBundleId
+ _objc_msgSend$staticFeatures
+ _objc_msgSend$sumWithAddendForArguments:
+ _objc_msgSend$sumWithKeyForArguments:
+ _objc_msgSend$testKey
+ _objc_msgSend$timeSinceLastShare
+ _objc_msgSend$topDomainURL
+ _objc_msgSend$transportBundleId
+ _objc_msgSend$typeOfContents
+ _objc_msgSend$updateConfigWithTrialOverrides:
+ _pow
+ _psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:._pasExprOnceResult
+ _psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:._pasOnceToken267
- +[_PSEnsembleModel feedbackDictionary]
- +[_PSEnsembleModel feedbackDictionary].cold.1
- +[_PSEnsembleModel forgetSession:]
- +[_PSEnsembleModel saveFeedback:forSessionId:feedbackActionType:isFallbackFetch:]
- -[_PSEnsembleModel addAdditionalStatsSignalsToCandidates:withTrialClient:]
- -[_PSEnsembleModel enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:]
- -[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:].cold.4
- -[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:].cold.5
- -[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:].cold.6
- -[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]
- -[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:].cold.1
- -[_PSPETMessageBuilder .cxx_destruct]
- -[_PSPETMessageBuilder addFeedbackEvents:]
- -[_PSPETMessageBuilder getPETMessage]
- -[_PSPETMessageBuilder initWithInteractionsStatistics:andConfig:andContext:andDeviceIdentifier:andTrialIdentifier:andDefaults:]
- -[_PSPETMessageBuilder privacyMitigatedFeatureValueFromName:forConversationId:]
- -[_PSTrialClient additionalFeaturesToCompute]
- -[_PSTrialClient arrayForKey:withDefaultValue:]
- -[_PSTrialClient arrayOfArraysForKey:withDefaultValue:]
- -[_PSTrialClient boolForKey:withDefaultValue:]
- -[_PSTrialClient configWithAnchorDate:]
- -[_PSTrialClient doubleForKey:withDefaultValue:]
- -[_PSTrialClient integerForKey:withDefaultValue:]
- -[_PSTrialClient mutableDictionaryForKey:withDefaultValue:]
- -[_PSTrialClient scenesBasedFeatures]
- -[_PSTrialClient scenesBasedFeatures].cold.1
- -[_PSTrialClient scenesMinimumNumberOfTags]
- -[_PSTrialClient stringForKey:withDefaultValue:]
- -[_PSTrialClient userDefaultArrayValueForKey:defaultToValue:]
- -[_PSTrialClient userDefaultBoolValueForKey:defaultToValue:]
- -[_PSTrialClient userDefaultDoubleValueForKey:defaultToValue:]
- -[_PSTrialClient userDefaultIntegerValueForKey:defaultToValue:]
- -[_PSTrialClient userDefaultMutableDictionaryForKey:defaultToValue:]
- -[_PSTrialClient userDefaultStringValueForKey:defaultToValue:]
- GCC_except_table102
- GCC_except_table127
- GCC_except_table146
- GCC_except_table153
- GCC_except_table156
- GCC_except_table78
- GCC_except_table90
- GCC_except_table91
- _OBJC_CLASS_$__CDInteractionsStatisticsConfig
- _OBJC_IVAR_$__PSPETMessageBuilder._interactionsStatistics
- _OBJC_IVAR_$__PSPETMessageBuilder._shareEvent
- __OBJC_$_INSTANCE_METHODS__PSPETMessageBuilder
- __OBJC_$_INSTANCE_VARIABLES__PSPETMessageBuilder
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.546
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.547
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.970
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.977
- ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke
- ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke.1009
- ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke_2
- ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke_3
- ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke_4
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.866
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.782
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.782.cold.1
- ___127-[_PSPETMessageBuilder initWithInteractionsStatistics:andConfig:andContext:andDeviceIdentifier:andTrialIdentifier:andDefaults:]_block_invoke
- ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.220
- ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.225
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.422
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.422.cold.1
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.438
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.464
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.466
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.468
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.470
- ___34+[_PSEnsembleModel forgetSession:]_block_invoke
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.240
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.240.cold.1
- ___37-[_PSTrialClient scenesBasedFeatures]_block_invoke
- ___38+[_PSEnsembleModel feedbackDictionary]_block_invoke
- ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.458
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.238
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.238.cold.1
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.242
- ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.601
- ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.639
- ___47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.255
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.437
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.438
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.965
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.965.cold.1
- ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.208
- ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.416
- ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.289
- ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.292
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.207
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.211
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.213
- ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.428
- ___58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.283
- ___60-[_PSKNNModel rankedMapsShareEtaSuggestions:maxSuggestions:]_block_invoke.525
- ___61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.272
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.682
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.682.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.449
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.449.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.452
- ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.431
- ___67-[_PSMediaAnalysisProcessingTask executeTaskWithCompletionHandler:]_block_invoke.407
- ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.464
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.837
- ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.455
- ___68-[_PSSuggester showNotificationToFileARadarForUserStudyParticipants]_block_invoke.321
- ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.461
- ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.643
- ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.467
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.542
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.547
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.550
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.565
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.571
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.578
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.575
- ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.473
- ___77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.212
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.372
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.389
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.396
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.396.cold.1
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.403
- ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.362
- ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.362.cold.1
- ___81+[_PSEnsembleModel saveFeedback:forSessionId:feedbackActionType:isFallbackFetch:]_block_invoke
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.726
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.615
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.631
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.704
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_3
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.420
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.423
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.424
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.425
- ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.434
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.302
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.307
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.311
- ___91-[_PSContactSuggester contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.190
- ___92-[_PSEnsembleModel enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:]_block_invoke
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.220
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.223
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.227
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.227.cold.1
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.227.cold.2
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.239
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.239.cold.1
- ___96-[_PSSuggester(InteractionInformation) interactionCountForHandle:fetchLimit:interactionStoreDB:]_block_invoke.306
- ___99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.392
- ___Block_byref_object_copy_.370
- ___Block_byref_object_copy_.471
- ___Block_byref_object_dispose_.371
- ___Block_byref_object_dispose_.472
- ____PSShareSheetSuggestionBundleIDMapping_block_invoke.209
- ___block_descriptor_40_e8_32r_e29_v16?0"NSMutableDictionary"8lr32l8
- ___block_descriptor_48_e8_32bs40r_e15_"NSString"8?0ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e17_"_PASTuple2"8?0ls32l8s40l8
- ___block_descriptor_57_e8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e25_v32?0"NSString"8Q16^B24ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_68_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.1000
- ___block_literal_global.1002
- ___block_literal_global.206
- ___block_literal_global.216
- ___block_literal_global.219
- ___block_literal_global.222
- ___block_literal_global.225
- ___block_literal_global.237
- ___block_literal_global.241
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.257
- ___block_literal_global.269
- ___block_literal_global.271
- ___block_literal_global.274
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.310
- ___block_literal_global.314
- ___block_literal_global.315
- ___block_literal_global.317
- ___block_literal_global.398
- ___block_literal_global.399
- ___block_literal_global.407
- ___block_literal_global.410
- ___block_literal_global.412
- ___block_literal_global.415
- ___block_literal_global.419
- ___block_literal_global.422
- ___block_literal_global.427
- ___block_literal_global.430
- ___block_literal_global.433
- ___block_literal_global.440
- ___block_literal_global.447
- ___block_literal_global.451
- ___block_literal_global.454
- ___block_literal_global.457
- ___block_literal_global.460
- ___block_literal_global.463
- ___block_literal_global.466
- ___block_literal_global.472
- ___block_literal_global.497
- ___block_literal_global.502
- ___block_literal_global.504
- ___block_literal_global.509
- ___block_literal_global.511
- ___block_literal_global.518
- ___block_literal_global.524
- ___block_literal_global.545
- ___block_literal_global.549
- ___block_literal_global.551
- ___block_literal_global.552
- ___block_literal_global.562
- ___block_literal_global.568
- ___block_literal_global.574
- ___block_literal_global.577
- ___block_literal_global.580
- ___block_literal_global.600
- ___block_literal_global.604
- ___block_literal_global.612
- ___block_literal_global.624
- ___block_literal_global.641
- ___block_literal_global.653
- ___block_literal_global.656
- ___block_literal_global.681
- ___block_literal_global.690
- ___block_literal_global.709
- ___block_literal_global.740
- ___block_literal_global.773
- ___block_literal_global.876
- ___block_literal_global.879
- ___block_literal_global.882
- ___block_literal_global.885
- ___block_literal_global.958
- __suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken140
- _feedbackDictionary._pasExprOnceResult
- _feedbackDictionary._pasOnceToken8
- _objc_msgSend$addAdditionalStatsSignalsToCandidates:withTrialClient:
- _objc_msgSend$additionalFeaturesToCompute
- _objc_msgSend$arrayForKey:withDefaultValue:
- _objc_msgSend$arrayOfArraysForKey:withDefaultValue:
- _objc_msgSend$boolForKey:withDefaultValue:
- _objc_msgSend$computeCandidateLevelSignals
- _objc_msgSend$computeFeaturesForRecipe:
- _objc_msgSend$computePASSFeatureWithPeopleDetectedInPhoto:
- _objc_msgSend$computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:
- _objc_msgSend$configWithAnchorDate:
- _objc_msgSend$dataWithContentsOfFile:
- _objc_msgSend$doubleForKey:withDefaultValue:
- _objc_msgSend$enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:
- _objc_msgSend$featureNamesToSortWith
- _objc_msgSend$feedBack
- _objc_msgSend$feedbackDictionary
- _objc_msgSend$first
- _objc_msgSend$forgetSession:
- _objc_msgSend$getInteractionsStatisticsForConfig:
- _objc_msgSend$getPETMessage
- _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:
- _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:
- _objc_msgSend$initWithFirst:second:
- _objc_msgSend$initWithInteractionsStatistics:andConfig:andContext:andDeviceIdentifier:andTrialIdentifier:andDefaults:
- _objc_msgSend$integerForKey:withDefaultValue:
- _objc_msgSend$mutableDictionaryForKey:withDefaultValue:
- _objc_msgSend$psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:
- _objc_msgSend$psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:
- _objc_msgSend$saveFeedbackInCoreDuetd:forSessionId:feedbackActionType:isFallbackFetch:reply:
- _objc_msgSend$scenesBasedFeatures
- _objc_msgSend$scenesMinimumNumberOfTags
- _objc_msgSend$setAppToAppExtMapping:
- _objc_msgSend$setFeatureNamesToSortWith:
- _objc_msgSend$setFoundInChunk:
- _objc_msgSend$setStatsToCompute:
- _objc_msgSend$setUpdatedInChunk:
- _objc_msgSend$userDefaultArrayValueForKey:defaultToValue:
- _objc_msgSend$userDefaultBoolValueForKey:defaultToValue:
- _objc_msgSend$userDefaultDoubleValueForKey:defaultToValue:
- _objc_msgSend$userDefaultIntegerValueForKey:defaultToValue:
- _objc_msgSend$userDefaultMutableDictionaryForKey:defaultToValue:
- _predictWithPredictionContext:maxSuggestions:contactKeysToFetch:._pasOnceToken102
- _predictWithPredictionContext:maxSuggestions:contactKeysToFetch:.getMeContactIdentifierPrefetchQueue
- _predictWithPredictionContext:maxSuggestions:contactKeysToFetch:.trialRankingModelPrefetchQueue
- _psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:._pasExprOnceResult
- _psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:._pasOnceToken226
CStrings:
+ "\t\t%@: %@\n"
+ "\t\t%@: %@ \n"
+ "\tnumberOfFeatures: %tu \n"
+ "\tnumberOfProperties: %tu \n"
+ "%.2f"
+ "(startDate >= %@) && (startDate <= %@)"
+ "(unknown: %tu)"
+ ")"
+ "--- Converted Data Contents and Types for BMPeopleSuggesterEventLevelMetrics Init ---"
+ "----------------------------------------------------------------------------------"
+ "10058"
+ "10100"
+ "1037"
+ "10433"
+ "1067"
+ "10950"
+ "114"
+ "1175"
+ "12"
+ "12017"
+ "12031"
+ "1213"
+ "12221"
+ "12291"
+ "12384"
+ "12398"
+ "1245"
+ "12456"
+ "1252"
+ "1256"
+ "12669"
+ "1270"
+ "1271"
+ "12735"
+ "12795"
+ "12841"
+ "12906"
+ "12944"
+ "1307"
+ "13179"
+ "1334"
+ "13568"
+ "1366"
+ "1436"
+ "14599"
+ "14798"
+ "14852"
+ "1501"
+ "1503"
+ "1510"
+ "15119"
+ "15122"
+ "15123"
+ "15124"
+ "15635"
+ "159"
+ "16134"
+ "16406"
+ "16904"
+ "17197"
+ "17199"
+ "17209"
+ "17212"
+ "17635"
+ "1770"
+ "178"
+ "18195"
+ "18303"
+ "186"
+ "253"
+ "297"
+ "32"
+ "343"
+ "454"
+ "462"
+ "493"
+ "545"
+ "571"
+ "588"
+ "624"
+ "648"
+ "670"
+ "683"
+ "698"
+ "889"
+ "899"
+ "906"
+ "927"
+ "985"
+ "@\"_PSInteractionsStatisticsConfig\""
+ "@16@?0@\"_CDAttachmentRecord\"8"
+ "@32@0:8^i16Q24"
+ "@92@0:8@16@24@32Q40d48B56@60@68@76@84"
+ "Aerobatics"
+ "Air Sports"
+ "Athletics"
+ "Attempted to compute invalid batch statName %@"
+ "Attempted to compute invalid incremental statName %@"
+ "Attempted to compute unknown operator: %@"
+ "Attempting to send BMMLSEShareSheetFeedback event..."
+ "Auto Racing"
+ "B48@0:8@16@24@32@40"
+ "Ball"
+ "Basketball"
+ "Beagle"
+ "Bodybuilding"
+ "Brass Music"
+ "Candidates after pruning %{private}@"
+ "Candidates with content-based features %{private}@"
+ "Canine"
+ "Cat"
+ "Cheerleading"
+ "Completed processing sharing interactions"
+ "Concert"
+ "Contact Sport"
+ "Cooking"
+ "Culinary Art"
+ "Cycling"
+ "Dancesport"
+ "Dancing"
+ "Datestamp string generated: %@"
+ "DefaultConfig"
+ "Detected interaction after explicit engagement in session %@ with unranked conversation %{private}@"
+ "Detected interaction after implicit engagement in session %@ with unranked conversation %{private}@"
+ "Detected messaging interaction after share session %@ with unranked conversation %{private}@"
+ "Detected messaging interaction after share session with %{private}@ via bundleID %@"
+ "Detected share interaction with app extension after share session with %{private}@ via bundleID %@"
+ "Digital Piano"
+ "Dinner"
+ "Dog"
+ "Dog Walking"
+ "DynamicFeatures"
+ "ERROR: Bad happens when sending event: %@"
+ "Electrophone"
+ "Element of array for key %@ was not a string %@"
+ "Equestrian Sport"
+ "Extreme Sport"
+ "Fallback candidates after pruning %{private}@"
+ "Fast Food"
+ "Feline"
+ "Figure Skating"
+ "Final configuration dynamic features: %@"
+ "Final configuration is: timeInterval %f, fetchLimit %lu,  maxComputationTimeInSeconds %.2f, sortOrderFeatureNames %@, shouldUseSuggestionEngaged %@, statsDefaultValues %@"
+ "Finished pruning candidates. %tu candidates removed: %{private}@"
+ "Fish as Food"
+ "Flute"
+ "Food"
+ "Fried Food"
+ "Frisbee"
+ "Golf"
+ "Guitar"
+ "Gym"
+ "Headphones"
+ "Hockey"
+ "Hound"
+ "Inference"
+ "Insufficient number of arguments %@"
+ "InteractionStatistics Candidates %{private}@"
+ "InteractionStatistics Candidates with Features %{private}@"
+ "IoU –\u00a0union of shared people sets had cardinality zero"
+ "Key: %@, Value: %@, Class: %@"
+ "Loading %@ from Trial recipe %@"
+ "Loading %@ from recipe %@"
+ "Loading %@ from user defaults %@"
+ "Loading %@ from user defaults %lf"
+ "Loading %@ from user defaults %lu"
+ "Looking for interactions from target bundleId %@ for session %@"
+ "Looking for share interactions from target bundleId %@ for session %@"
+ "Lunch"
+ "MM/dd/yyyy"
+ "Meal"
+ "Menu"
+ "Metrics"
+ "Motor Sport"
+ "Music"
+ "Music Venue"
+ "Musical"
+ "Musical Ensemble"
+ "Musical Instrument"
+ "Musical Keyboard"
+ "NOT (bundleId IN %@)"
+ "Nascar"
+ "No conversationId found for explicit engagement in session %@"
+ "No conversationId found for implicit engagement in session %@"
+ "Orchestra"
+ "PeopleSuggestions"
+ "Percussion Instrument"
+ "Photo based features disabled by Trial"
+ "Piano"
+ "Poultry"
+ "Prediction context query start date was nil %{private}@ –\u00a0starting it now"
+ "PrivacyMitigation"
+ "Processing communication interactions"
+ "Processing implicit positive engagement (app extension share) for session %@ from transport bundleId %@"
+ "Processing sharing interactions"
+ "Processing speculative engagement (manual interactions after ShareSheet closed) for session %@"
+ "Racing"
+ "Racquet"
+ "Ran the features through the coreML model"
+ "Reading interaction stats for fallback request sessionID %@"
+ "Reading interaction stats for request sessionID %@"
+ "Restaurant"
+ "Roller Sport"
+ "Seafood"
+ "Searching for message interactions from bundleId %@"
+ "Searching for share interactions from for share extension %@ for session"
+ "Singer"
+ "Singing"
+ "Skipping interaction with nil conversationId: %{private}@"
+ "Soccer"
+ "Soup"
+ "Spaniel"
+ "Sport"
+ "Sport Climbing"
+ "Sports Equipment"
+ "Sports Uniform"
+ "Sports Venue"
+ "Sportscar"
+ "Sportswear"
+ "StaticFeatures"
+ "Storing feedback for app extension sharing interaction (implicit positive engagement – bottom row share) with %{private}@ for session %@"
+ "Storing feedback for explicit positive engagement (top row share) with %{private}@ for session %@"
+ "Storing feedback for speculative interaction after share session %@ with %{private}@ via bundleID %@"
+ "String Instrument"
+ "Successfully sent BMMLSEShareSheetFeedback event."
+ "Swimming"
+ "SystemResourceUsage"
+ "T@\"NSArray\",&,N,V_dynamicFeatureRecipe"
+ "T@\"NSArray\",&,N,V_sortOrderFeatureNames"
+ "T@\"NSArray\",&,N,V_staticFeatures"
+ "T@\"NSDate\",R,N,V_anchorDate"
+ "T@\"NSDate\",R,N,V_leftBoundDate"
+ "T@\"NSDate\",R,N,V_rightBoundDate"
+ "T@\"NSDictionary\",&,N,V_defaultValues"
+ "T@\"NSDictionary\",&,N,V_queryStats"
+ "T@\"NSDictionary\",&,N,V_sceneCategoryTagMapping"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSMutableDictionary\",&,N,V_appsSharedFromByConversationId"
+ "T@\"NSMutableDictionary\",&,N,V_mostRecentInteractionTimestampByConversationId"
+ "T@\"NSMutableDictionary\",&,N,V_personsIdsInPhotosForPastShareInteractions"
+ "T@\"NSMutableDictionary\",&,N,V_personsIdsInPhotosForPastSyntheticShareInteractions"
+ "T@\"NSPredicate\",R,N"
+ "T@\"NSString\",&,N,V_sourceBundleId"
+ "T@\"NSString\",&,N,V_topDomainURL"
+ "T@\"NSString\",&,N,V_transportBundleId"
+ "T@\"_PSInteractionsStatisticsConfig\",R,N,V_config"
+ "TB,N,V_shouldUseSuggestionEngaged"
+ "TB,R,N,V_isWeekendShare"
+ "TQ,N,V_fetchLimit"
+ "Td,N,V_maxComputationTime"
+ "Td,R,N,V_anchorTimeStamp"
+ "Team Sport"
+ "Tennis"
+ "Ukulele"
+ "Unable to resolve main app bundleId from sharing interaction because the sharing extension bundleId was nil."
+ "Unable to resolve main app bundleId from sharing interaction because there was no main bundleId associated with the sharing extension bundleId."
+ "Unexpected type for value of class %@. Converting to string via -description."
+ "Value for key %@ was not an array %@"
+ "Volleyball"
+ "Weight Training"
+ "Wine"
+ "Winter Sport"
+ "Woodwind"
+ "_PSEnsemble: Log PET data to Biome"
+ "_PSEnsemble: No valid feedback event found for sessionId: %@"
+ "_PSEnsemble: Waiting %d seconds for feedback events from ShareSheet UI for sessionId: %@"
+ "_PSEnsemble: aborting data logging – sessionId is nil"
+ "_PSEnsemble: logged data for sessionId: %@"
+ "_PSEnsemble: processing feedback for sessionId: %@"
+ "_PSEnsemble: registering data logging for sessionId: %@"
+ "_PSEnsemble: sessionId %@ did not produce any viable feedback"
+ "_PSEnsembleModel_addDynamicFeaturesToCandidates"
+ "_PSEnsembleModel_defaultPredictionPipeline"
+ "_PSEnsembleModel_fallbackPredictionPipeline"
+ "_PSInteractionsStatistics"
+ "_PSInteractionsStatistics(\n"
+ "_PSInteractionsStatisticsConfig"
+ "_anchorDate"
+ "_anchorTimeStamp"
+ "_appsSharedFromByConversationId"
+ "_conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:"
+ "_defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:"
+ "_defaultValues"
+ "_dynamicFeatureRecipe"
+ "_fallbackPredictionWithPredictionContext:config:parentSpanId:"
+ "_fetchLimit"
+ "_isWeekendShare"
+ "_leftBoundDate"
+ "_maxComputationTime"
+ "_mostRecentInteractionTimestampByConversationId"
+ "_personsIdsInPhotosForPastShareInteractions"
+ "_personsIdsInPhotosForPastSyntheticShareInteractions"
+ "_properties"
+ "_queryStats"
+ "_reMapContentTypes:count:"
+ "_remapSingleContentTypeValue:"
+ "_rightBoundDate"
+ "_sceneCategoryTagMapping"
+ "_sceneCategoryTagThresholds"
+ "_shareExtToAppBundleIdMapping"
+ "_shouldUseSuggestionEngaged"
+ "_sortOrderFeatureNames"
+ "_sourceBundleId"
+ "_staticFeatures"
+ "_stringFromValue:"
+ "_topDomainURL"
+ "_transportBundleId"
+ "_updateInteractionStatisticsForExplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:"
+ "_updateInteractionStatisticsForImplicitEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:"
+ "_updateInteractionStatisticsForSpeculativeEngagement:interactionStatisticsConfig:interactionStatistics:sessionFeedback:"
+ "_updatePropertiesFromRecord:forConversationId:"
+ "addConversationId:"
+ "aggregateSum:"
+ "aggregateSumForArguments:"
+ "anchorDate"
+ "anchorTimeStamp"
+ "appBundleIdForRecord:"
+ "appsSharedFromByConversationId"
+ "arrayOfArraysForKey:"
+ "asyncPSRDataCollection"
+ "autoupdatingCurrentCalendar"
+ "com.apple."
+ "communicationInteractionPredicate"
+ "communicationInteractions.%@"
+ "computeAppsSharedFromForConversationId:interactionRecord:"
+ "computeContentBasedFeaturesForPersonIdsDetectedInPhoto:sceneCategoriesDetectedInPhoto:"
+ "computeDynamicFeatures"
+ "computeHasEverSharePlayedWithConversationId:interactionRecord:"
+ "computeIsFirstPartyAppForConversationId:interactionRecord:"
+ "computeMaxIoUOfSharesOfPeopleInPhotoForPeopleDetectedInPhoto:"
+ "computeNumberOfAppsSharedFromWithConversation"
+ "computeNumberOfEngagedSuggestionsFromCurrentAppWithConversationForConversationId:interactionRecord:"
+ "computeNumberOfEngagedSuggestionsOfDetectedPeopleForPeopleDetectedInPhoto:"
+ "computeNumberOfEngagedSuggestionsOfPeopleInPhoto"
+ "computeNumberOfEngagedSuggestionsOfTopDomainURLWithConversationForConversationId:interactionRecord:"
+ "computeNumberOfEngagedSuggestionsToTargetApp"
+ "computeNumberOfEngagedSuggestionsWithConversationId:interactionRecord:"
+ "computeNumberOfFacesSharedWithConversation"
+ "computeNumberOfIncomingInteractionsWithConversationId:interactionRecord:"
+ "computeNumberOfInteractionsDuringTimePeriodWithConversationForConversationId:interactionRecord:"
+ "computeNumberOfOutgoingInteractionsWithConversationId:interactionRecord:"
+ "computeNumberOfRecentOutgoingInteractionsWithConversationForConversationId:interactionRecord:"
+ "computeNumberOfSharesFromCurrentAppWithConversationForConversationId:interactionRecord:"
+ "computeNumberOfSharesOfDetectedPeopleForPeopleDetectedInPhoto:"
+ "computeNumberOfSharesOfDetectedScenesInPhotoForSceneCategoriesDetectedInPhoto:"
+ "computeNumberOfSharesOfPeopleInPhoto"
+ "computeNumberOfSharesOfScenesInPhoto"
+ "computeNumberOfSharesOfTopDomainURLWithConversationForConversationId:interactionRecord:"
+ "computeNumberOfSharesToTargetApp"
+ "computeNumberOfSharesWithConversationId:interactionRecord:"
+ "computePhotoFeaturesForConversationId:interactionRecord:"
+ "computeScenesBasedFeaturesForConversationId:interactionRecord:"
+ "computeStatisticsWithInteractionStore:"
+ "computeTimeSinceLastIncomingInteractionForConversationId:interactionRecord:"
+ "computeTimeSinceLastOutgoingInteractionForConversationId:interactionRecord:"
+ "computeTimeSinceLastPhoneCallWithConversationId:interactionRecord:"
+ "computeTimeSinceLastPhotoShareWithConversationId:interactionRecord:"
+ "computeTimeSinceLastShareWithConversation:interactionRecord:"
+ "computeTimeSinceLastUIEngagementForConversationId:interactionRecord:"
+ "containsConversationId:"
+ "containsKey:"
+ "conversationId: %@ \n"
+ "convertCoreAnalyticsEvent2BiomeEvent:"
+ "copy:to:"
+ "copyFeatureForArguments:"
+ "datestamp"
+ "defaultValues"
+ "dictionaryForKey:"
+ "direction == %@"
+ "divide:withDivisor:"
+ "divideWithDivisorForArguments:"
+ "donateCA2Biome:"
+ "dynamicFeatureComputationSpan"
+ "dynamicFeatureRecipe"
+ "dynamicFeaturesToCompute"
+ "engagedSuggestionProxyDebug"
+ "exponential:withMultiplier:"
+ "exponentialWithMultiplierForArguments:"
+ "generateConversationIdFromInteractionRecipientRecords:"
+ "getPETMessageWithInteractionsStatistics:predictionContext:deviceIdentifier:trialIdentifier:peopleSuggesterDefaults:"
+ "impute:withConstant:"
+ "imputeFeatureForArguments:"
+ "incrementValueForFeature:andConversationId:"
+ "initDefaultConfigWithBundleId:anchorDate:"
+ "initFallbackConfigWithBundleId:anchorDate:"
+ "initWithConfig:"
+ "initWithDeviceIdentifier:sessionId:trialIdentifiers:version:candidates:testKey:madResponseStatus:isFallbackFetch:isSharePlayAvailable:appSharedFrom:feedbackEvents:typeOfContent:isInPhoneCall:timeSinceLastShare:isScreenShot:photoFeatures:"
+ "initWithIdentifier:engagementType:engagementIdentifier:visiblePeopleSuggestionCount:visibleAppSuggestionCount:airdropPeopleSuggestionShown:inferenceSource:trialIdentifier:timeouts:productInsights:"
+ "initWithIdentifier:sourceBundleId:peopleSuggestions:responseType:trainingDataCollection:"
+ "initWithIndexSelected:engagedSuggestionProxyReason:engagedSuggestionProxy:engagedSuggestionProxyDebug:airdropShown:airdropEngaged:sharePlayAvailable:sharePlayEngaged:appSharingIntent:engagementType:suggestionAvailable:suggestionNumber:numberOfVisibleSuggestions:peopleSuggestionsSetting:transportApp:sourceApp:contentShared:sessionId:userExperienceFlow:sessionLatency:modelTimeout:suggestionPath:suggestionPathDebug:trialDeploymentId:trialExperimentId:trialTreatmentId:isPhotos:PSRActive:sessionDelayInMilliseconds:datestamp:"
+ "initWithInteractionStore:knowledgeStore:"
+ "initWithSoftwareTracing:"
+ "initWithSourceBundleId:anchorDate:leftBoundDate:fetchLimit:maxComputationTime:shouldUseSuggestionEngaged:sortOrderFeatureNames:statsDefaultValues:sceneCategoryTagMapping:sceneCategoryTagThresholds:"
+ "isWeekendShare"
+ "iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:updateTelemetry:withBlock:"
+ "laplaceProbabilityWithAlphaForArguments:"
+ "leftBoundDate"
+ "logWithBaseForArguments:"
+ "maxIoUIoUSharesOfPeopleInPhotoWithConversation"
+ "mechanism == %@"
+ "messagesBundleId"
+ "mostRecentInteractionTimestampByConversationId"
+ "multiply:with:"
+ "multiply:withScalar:"
+ "multiplyWithKeyForArguments:"
+ "mutableDictionaryForKey:"
+ "mutableDictionaryOfSetsForKey:"
+ "mutliplyWithScalarForArguments:"
+ "personsIdsInPhotosForPastShareInteractions"
+ "personsIdsInPhotosForPastSyntheticShareInteractions"
+ "photoFeaturesForConversationId"
+ "popFeedbackForSession:"
+ "power:withExponent:"
+ "powerWithExponentForArguments:"
+ "privatizedConversationIdentifier"
+ "processInteractionRecord:"
+ "psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:"
+ "reciprocal:withOffset:"
+ "reciprocalWithOffsetForArguments:"
+ "removeFeature:andConversation:"
+ "removeObjectsForKeys:"
+ "rename:with:"
+ "renameFeatureForArguments:"
+ "saveFeedback:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:"
+ "saveFeedbackInCoreDuetd:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:reply:"
+ "savePastSharedPhotoDetectedPersonIds:forConversationId:forSyntheticInteraction:"
+ "sceneCategoryTagMapping"
+ "sceneTagCategoryMapping"
+ "sceneTagThresholdForSceneCategoryName:"
+ "sceneTagThresholds"
+ "sendDataCollectionMessageWith:"
+ "setAppsSharedFromByConversationId:"
+ "setDefaultValues:"
+ "setDynamicFeatureRecipe:"
+ "setLookBackTimeInterval:"
+ "setMaxComputationTime:"
+ "setMostRecentInteractionTimestampByConversationId:"
+ "setPersonsIdsInPhotosForPastShareInteractions:"
+ "setPersonsIdsInPhotosForPastSyntheticShareInteractions:"
+ "setQueryStats:"
+ "setSceneCategoryTagMapping:"
+ "setSceneCategoryTagThresholds:"
+ "setShouldUseSuggestionEngaged:"
+ "setSortOrderFeatureNames:"
+ "setSourceBundleId:"
+ "setStaticFeatures:"
+ "setTransportBundleId:"
+ "setValue:forProperty:andConversationId:"
+ "shareSheetFeedbackEngagementType"
+ "sharingInteractionPredicate"
+ "sharingInteractions.%@"
+ "sortOrderFeatureNames"
+ "staticFeatures"
+ "staticFeaturesToCompute"
+ "suggestionPathDebug"
+ "sum:withAddend:"
+ "sumWithAddendForArguments:"
+ "sumWithKeyForArguments:"
+ "targetBundleId == %@"
+ "timeSinceLastUIEngagement"
+ "topDomainURL"
+ "transportBundleId"
+ "unknown:"
+ "unknownFeature"
+ "updateConfigWithTrialOverrides:"
+ "v24@?0@\"NSString\"8@\"NSString\"16"
+ "v28@?0@\"_CDInteractionRecord\"8i16^B20"
+ "v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSMutableSet\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSSet\"16^B24"
+ "v36@0:8@16@24B32"
+ "v44@0:8@16i24@28@36"
+ "v52@0:8@16@24q32@40B48"
- "16634"
- "@\"PeopleSuggesterShareEvent\""
- "@\"_CDInteractionsStatistics\""
- "@\"_PASTuple2\"8@?0"
- "Feedback reesolved for session %@ resolved to %@ as %@"
- "Feedback resolved for session %@ resolved to %@ as %ld"
- "Finished pruning candidates. Candidates removed: %@"
- "No scene tag mapping specified in recipe–using default values."
- "PSRFeatureFlag"
- "Q32@0:8@16Q24"
- "Scene tag mapping: %@"
- "TimeSinceLastUIEngagement"
- "UIResolutionTime: UI resolution has taken %fs, isUsingLegacyUI %@"
- "_PSEnsemble: Candidate Features with additional features %{private}@"
- "_PSEnsemble: Candidates after pruning %{private}@"
- "_PSEnsemble: Finished computing additional features %@"
- "_PSEnsemble: InteractionStatistics Candidates %{private}@"
- "_PSEnsemble: InteractionStatistics Candidates with Features %{private}@"
- "_PSEnsemble: Ran the features through the coreML model"
- "_PSEnsemble: Skipped additional stats signals"
- "_PSEnsemble: Skipped photo based signals"
- "_PSEnsemble: async Wait until the feedback call populates chosenSuggestion: %d seconds"
- "_PSEnsemble: logged data from PSR"
- "_PSEnsemble: skipped coreML model"
- "_PSEnsembleModel_addAdditionalNonStatsSignalsToCandidates"
- "_PSTrialClient: Final configuration is: timeInterval %f, fetchLimit %lu,  maxComputationTimeInSeconds %.2f, featureNamesToSortWith %@, shouldUseSuggestionEngaged %@, statsDefaultValues %@"
- "_interactionsStatistics"
- "_shareEvent"
- "addAdditionalStatsSignalsToCandidates:withTrialClient:"
- "additionalFeaturesToCompute"
- "arrayForKey:withDefaultValue:"
- "arrayOfArraysForKey:withDefaultValue:"
- "asyncPSRDataCollectionForContext"
- "boolForKey:withDefaultValue:"
- "computeCandidateLevelSignals"
- "computeFeaturesForRecipe:"
- "computePASSFeatureWithPeopleDetectedInPhoto:"
- "computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:"
- "configWithAnchorDate:"
- "d32@0:8@16d24"
- "dataWithContentsOfFile:"
- "doubleForKey:withDefaultValue:"
- "enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:"
- "feedbackDictionary"
- "first"
- "forgetSession:"
- "foundInInteractionStoreChunk"
- "getInteractionsStatisticsForConfig:"
- "getPETMessage"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:"
- "initWithFirst:second:"
- "initWithInteractionsStatistics:andConfig:andContext:andDeviceIdentifier:andTrialIdentifier:andDefaults:"
- "integerForKey:withDefaultValue:"
- "mutableDictionaryForKey:withDefaultValue:"
- "numberOfSharesOfDetectedScenesWithConversation"
- "psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:"
- "saveFeedback:forSessionId:feedbackActionType:isFallbackFetch:"
- "saveFeedbackInCoreDuetd:forSessionId:feedbackActionType:isFallbackFetch:reply:"
- "scenesMinimumNumberOfTags"
- "setAppToAppExtMapping:"
- "setFeatureNamesToSortWith:"
- "setStatsToCompute:"
- "stringForKey:withDefaultValue:"
- "updatedInInteractionStoreChunk"
- "userDefaultArrayValueForKey:defaultToValue:"
- "userDefaultBoolValueForKey:defaultToValue:"
- "userDefaultDoubleValueForKey:defaultToValue:"
- "userDefaultIntegerValueForKey:defaultToValue:"
- "userDefaultMutableDictionaryForKey:defaultToValue:"
- "userDefaultStringValueForKey:defaultToValue:"
- "v44@0:8@16@24q32B40"
- "v44@0:8@16i24d28@?36"

```
