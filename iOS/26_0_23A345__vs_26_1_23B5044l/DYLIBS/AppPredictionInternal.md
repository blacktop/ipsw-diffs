## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-619.1.0.2.0
-  __TEXT.__text: 0x48985c
-  __TEXT.__auth_stubs: 0x4140
-  __TEXT.__objc_methlist: 0x38eac
+619.5.1.0.0
+  __TEXT.__text: 0x4858e8
+  __TEXT.__auth_stubs: 0x4130
+  __TEXT.__objc_methlist: 0x38c64
   __TEXT.__const: 0x3d4a
-  __TEXT.__cstring: 0x5ab01
-  __TEXT.__oslogstring: 0x3af49
-  __TEXT.__gcc_except_tab: 0xff78
+  __TEXT.__cstring: 0x5a3d1
+  __TEXT.__oslogstring: 0x3ad99
+  __TEXT.__gcc_except_tab: 0x10064
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x13ae

   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xe4d0
+  __TEXT.__unwind_info: 0xe420
   __TEXT.__eh_frame: 0x2a2c
-  __TEXT.__objc_classname: 0x8ca2
-  __TEXT.__objc_methname: 0xae6bc
-  __TEXT.__objc_methtype: 0x1807d
-  __TEXT.__objc_stubs: 0x4d100
-  __DATA_CONST.__got: 0x3a20
-  __DATA_CONST.__const: 0xbf00
-  __DATA_CONST.__objc_classlist: 0x1fb0
-  __DATA_CONST.__objc_catlist: 0x140
+  __TEXT.__objc_classname: 0x8c15
+  __TEXT.__objc_methname: 0xae2a2
+  __TEXT.__objc_methtype: 0x18004
+  __TEXT.__objc_stubs: 0x4cf40
+  __DATA_CONST.__got: 0x39c0
+  __DATA_CONST.__const: 0xbf48
+  __DATA_CONST.__objc_classlist: 0x1f88
+  __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bea0
+  __DATA_CONST.__objc_selrefs: 0x1be08
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x1538
-  __DATA_CONST.__objc_arraydata: 0x13a0
-  __AUTH_CONST.__auth_got: 0x20b8
-  __AUTH_CONST.__const: 0x8a80
-  __AUTH_CONST.__cfstring: 0x3aae0
-  __AUTH_CONST.__objc_const: 0x83f50
-  __AUTH_CONST.__objc_intobj: 0x3450
-  __AUTH_CONST.__objc_arrayobj: 0x10b0
+  __DATA_CONST.__objc_superrefs: 0x1518
+  __DATA_CONST.__objc_arraydata: 0x1378
+  __AUTH_CONST.__auth_got: 0x20b0
+  __AUTH_CONST.__const: 0x8ae0
+  __AUTH_CONST.__cfstring: 0x3a780
+  __AUTH_CONST.__objc_const: 0x83b78
+  __AUTH_CONST.__objc_intobj: 0x33c0
+  __AUTH_CONST.__objc_arrayobj: 0x1098
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x70
+  __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0x54d0
   __AUTH.__data: 0x2198
-  __DATA.__objc_ivar: 0x4b04
+  __DATA.__objc_ivar: 0x4ae0
   __DATA.__data: 0x3d98
-  __DATA.__bss: 0x28f8
+  __DATA.__bss: 0x2908
   __DATA.__common: 0x128
-  __DATA_DIRTY.__objc_data: 0xf028
-  __DATA_DIRTY.__data: 0xad8
-  __DATA_DIRTY.__bss: 0xb88
+  __DATA_DIRTY.__objc_data: 0xee98
+  __DATA_DIRTY.__data: 0xa58
+  __DATA_DIRTY.__bss: 0xb60
   __DATA_DIRTY.__common: 0x98
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8BEA1CF1-198D-32A0-9A4E-C8F405F888D0
-  Functions: 25639
-  Symbols:   77046
-  CStrings:  42998
+  UUID: 072BF011-6820-3FB5-A138-238D8501DCF2
+  Functions: 25561
+  Symbols:   76842
+  CStrings:  42897
 
Symbols:
+ +[ATXMicrolocationVisitAnchor fetchAnchorOccurrencesBetweenStartDate:endDate:]
+ +[ATXMicrolocationVisitAnchor filterBlock]
+ +[ATXMicrolocationVisitDuetEvent mapVisitProbabilitiesByUUID:]
+ -[ATXAnchorModelInferenceEngine unregisterAnchorEventListenerForAnchor:].cold.3
+ -[ATXAnchorModelInferenceEngine unregisterAnchorEventListenerForAnchor:].cold.4
+ -[ATXAppFeaturizer evaluateFeaturesForApps:clipBundleIdsToRank:consumerSubType:intent:scoreLogger:context:featureCache:].cold.2
+ -[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]
+ -[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:].cold.1
+ -[ATXAppLaunchMicroLocation _receivedNotificationOfNewMicroLocation:]
+ -[ATXAppLaunchMicroLocation _subscribeToMicroLocationEvents]
+ -[ATXAppLaunchMicroLocation dealloc]
+ -[ATXAppLaunchMicroLocation initWithMicroLocationStream:appInFocusStream:combinedIntentStream:directory:forTesting:]
+ -[ATXCandidateRelevanceModelServerCoordinator unregisterAnchorEventListenerForAnchor:].cold.3
+ -[ATXCandidateRelevanceModelServerCoordinator unregisterAnchorEventListenerForAnchor:].cold.4
+ -[ATXMicrolocationVisitDuetEvent initWithATXEvent:]
+ -[ATXMicrolocationVisitDuetEvent initWithATXEvent:].cold.1
+ -[ATXMicrolocationVisitDuetEvent initWithATXEvent:].cold.2
+ -[ATXModeEntityScorerServer rankedAppsForMode:options:reply:]
+ -[ATXModeEntityScorerServer rankedContactsForMode:options:reply:]
+ -[ATXModeEntityScorerServer rankedContactsForMode:options:reply:].cold.1
+ -[ATXModeEntityScorerServer rankedNotificationsForMode:options:reply:]
+ -[ATXModeEntityScorerServer rankedNotificationsForMode:options:reply:].cold.1
+ -[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:]
+ -[ATXModeMetricsLogUploader uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:].cold.1
+ -[ATXNotificationAndSuggestionDatabase _makeNotificationTelemetryQueryResultFromDatabaseResult:queryTimeInterval:]
+ -[ATXNotificationManagementSettingsMetric .cxx_destruct]
+ -[ATXNotificationManagementSettingsMetric areHighlightsEnabled]
+ -[ATXNotificationManagementSettingsMetric areSummariesEnabled]
+ -[ATXNotificationManagementSettingsMetric setAreHighlightsEnabled:]
+ -[ATXNotificationManagementSettingsMetric setAreSummariesEnabled:]
+ -[ATXNotificationSettingsLogger _writeMetricsToTemporaryLocation:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsWithBreakthroughFeaturesFromStartTimestamp:toEndTimestamp:withTelemetryQueryResult:withTask:]
+ -[ATXNotificationTelemetryLogger logNotificationMetricsWithTask:]
+ -[ATXNotificationTelemetryQueryResult queryTimeInterval]
+ -[ATXNotificationTelemetryQueryResult setQueryTimeInterval:]
+ -[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]
+ -[_ATXGlobals actionPredictionFirstStageBeamWidthMacOS]
+ -[_ATXInspectionClient triggerBackgroundJobWithIdentifier:configuration:completion:]
+ -[_ATXInspectionServer triggerBackgroundJobWithIdentifier:configuration:completion:]
+ _OBJC_CLASS_$_ATXMicroLocationVisitEvent
+ _OBJC_CLASS_$_ATXMicroLocationVisitScheduler
+ _OBJC_CLASS_$_ATXMicroLocationVisitStream
+ _OBJC_CLASS_$_ATXRelevantShortcutsStream
+ _OBJC_CLASS_$_ATXSleepStream
+ _OBJC_IVAR_$_ATXAnchorModelInferenceEngine._microLocationSchedulerToken
+ _OBJC_IVAR_$_ATXAppLaunchMicroLocation._microLocationSchedulerToken
+ _OBJC_IVAR_$_ATXAppLaunchMicroLocation._microLocationStream
+ _OBJC_IVAR_$_ATXCandidateRelevanceModelServerCoordinator._microLocationSchedulerToken
+ _OBJC_IVAR_$_ATXNotificationManagementSettingsMetric._areHighlightsEnabled
+ _OBJC_IVAR_$_ATXNotificationManagementSettingsMetric._areSummariesEnabled
+ _OBJC_IVAR_$_ATXNotificationTelemetryQueryResult._queryTimeInterval
+ _OBJC_IVAR_$_ATXRSWidgetSuggestionProducer._relevantShortcutsStreamScheduler
+ _OBJC_IVAR_$_ATXRSWidgetSuggestionProducer._relevantShortcutsStreamSink
+ _OBJC_IVAR_$_ATXRSWidgetSuggestionProducer._relevantShortcutsTombstoneScheduler
+ _OBJC_IVAR_$_ATXRSWidgetSuggestionProducer._relevantShortcutsTombstoneSink
+ _OBJC_IVAR_$_ATXRSWidgetSuggestionProducer._targetQueueForBiome
+ __OBJC_$_CLASS_METHODS_ATXMicrolocationVisitDuetEvent
+ __OBJC_$_INSTANCE_METHODS__DKEvent(ATXLocationVisitDuetEvent|ATXMode)
+ ___121-[ATXCandidateRelevanceModelDatasetGenerator initWithConfig:inferredModeStream:computedModeStream:pointOfInterestStream:]_block_invoke_7
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.40
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.40.cold.1
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.42
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.42.cold.1
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.47
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.47.cold.1
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.50
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.50.cold.1
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.54
+ ___201-[ATXRSWidgetSuggestionProducer initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.cold.1
+ ___233-[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]_block_invoke
+ ___39-[ATXSleepSuggestionServer queryEvents]_block_invoke
+ ___42+[ATXMicrolocationVisitAnchor filterBlock]_block_invoke
+ ___44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.81
+ ___44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.81.cold.1
+ ___44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.84
+ ___46-[ATXAppIntentMonitor _listenToActivityStream]_block_invoke.72
+ ___47-[ATXAppLaunchMicroLocation _getHistoricalData]_block_invoke
+ ___48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.91
+ ___48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.91.cold.1
+ ___48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.98
+ ___60-[ATXAppLaunchMicroLocation _subscribeToMicroLocationEvents]_block_invoke
+ ___61-[ATXModeEntityScorerServer rankedAppsForMode:options:reply:]_block_invoke
+ ___63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.55
+ ___63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.55.cold.1
+ ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.89
+ ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.89.cold.1
+ ___66-[ATXAppLaunchMicroLocation tryLoadCorrelationMatricesImmediately]_block_invoke.77
+ ___69-[ATXAppLaunchMicroLocation _receivedNotificationOfNewMicroLocation:]_block_invoke
+ ___70-[ATXAnchorModelInferenceEngine registerAnchorEventListenerForAnchor:]_block_invoke
+ ___71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.84
+ ___71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.84.cold.1
+ ___78+[ATXMicrolocationVisitAnchor fetchAnchorOccurrencesBetweenStartDate:endDate:]_block_invoke
+ ___79-[ATXRSWidgetSuggestionProducer _candidatesFromRelevantShortcutsFromStartDate:]_block_invoke.74
+ ___84-[ATXMicrolocationVisitDuetEvent initWithCurrentContextStoreValuesWithTwoHourLimit:]_block_invoke
+ ___84-[ATXMicrolocationVisitDuetEvent initWithCurrentContextStoreValuesWithTwoHourLimit:]_block_invoke_2
+ ___84-[_ATXInspectionClient triggerBackgroundJobWithIdentifier:configuration:completion:]_block_invoke
+ ___89-[ATXCandidateRelevanceModelServerCoordinator registerAnchorEventNotificationsForAnchor:]_block_invoke
+ ___95-[ATXMicrolocationVisitDuetDataProvider fetchEventsBetweenStartDate:andEndDate:withPredicates:]_block_invoke
+ ___95-[ATXMicrolocationVisitDuetDataProvider fetchEventsBetweenStartDate:andEndDate:withPredicates:]_block_invoke_2
+ ___99-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:]_block_invoke
+ ___99-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:]_block_invoke_2
+ ___block_descriptor_32_e36_B16?0"ATXMicroLocationVisitEvent"8l
+ ___block_descriptor_40_e8_32r_e36_B16?0"ATXMicroLocationVisitEvent"8lr32l8
+ ___block_descriptor_40_e8_32s_e27_v24?0"ATXSleepEvent"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e36_B16?0"ATXMicroLocationVisitEvent"8ls32l8
+ ___block_descriptor_40_e8_32w_e36_v16?0"ATXMicroLocationVisitEvent"8lw32l8
+ ___block_descriptor_48_e8_32s40s_e35_B16?0"ATXRelevantShortcutsEvent"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e49_{_PASDBIterAction_=B}16?0"_PASSqliteStatement"8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.143
+ ___block_literal_global.154
+ ___block_literal_global.412
+ ___block_literal_global.578
+ ___block_literal_global.582
+ ___block_literal_global.593
+ ___block_literal_global.596
+ ___block_literal_global.607
+ ___block_literal_global.610
+ ___block_literal_global.618
+ ___block_literal_global.629
+ ___block_literal_global.633
+ ___block_literal_global.637
+ ___block_literal_global.641
+ ___block_literal_global.645
+ ___block_literal_global.648
+ ___block_literal_global.660
+ ___block_literal_global.666
+ ___block_literal_global.672
+ ___block_literal_global.675
+ ___block_literal_global.679
+ ___block_literal_global.682
+ ___block_literal_global.695
+ ___block_literal_global.698
+ ___block_literal_global.704
+ ___block_literal_global.707
+ ___block_literal_global.711
+ ___block_literal_global.719
+ ___block_literal_global.724
+ ___block_literal_global.729
+ ___block_literal_global.733
+ ___block_literal_global.741
+ ___block_literal_global.75
+ ___registerForCarPlayMetricsBGSTJob_block_invoke.726
+ ___registerForFaceSuggestionsCTSJob_block_invoke.642
+ ___registerForFaceSuggestionsCTSJob_block_invoke.642.cold.1
+ ___registerForNotificationAndSuggestionDatastorePruning_block_invoke.693
+ ___registerForNotificationMetricsBGSTJob_block_invoke
+ _microLocationEventFromATXMicroLocationVisitEvent
+ _objc_msgSend$RelevantShortcuts
+ _objc_msgSend$_makeNotificationTelemetryQueryResultFromDatabaseResult:queryTimeInterval:
+ _objc_msgSend$_receivedNotificationOfNewMicroLocation:
+ _objc_msgSend$_subscribeToMicroLocationEvents
+ _objc_msgSend$_writeMetricsToTemporaryLocation:
+ _objc_msgSend$areHighlightsEnabled
+ _objc_msgSend$areSummariesEnabled
+ _objc_msgSend$enumerateEventsFromStartDate:endDate:limit:block:
+ _objc_msgSend$enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:
+ _objc_msgSend$enumerateSleepEventsFromStartDate:endDate:limit:block:
+ _objc_msgSend$handleAnchorEventForMicrolocationVisitAnchor
+ _objc_msgSend$handleMicrolocationVisitNotification
+ _objc_msgSend$initForTestingWithIdentifier:configuration:
+ _objc_msgSend$initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:
+ _objc_msgSend$initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:
+ _objc_msgSend$initWithMicroLocationStream:appInFocusStream:combinedIntentStream:directory:forTesting:
+ _objc_msgSend$logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:
+ _objc_msgSend$logNotificationMetricsWithBreakthroughFeaturesFromStartTimestamp:toEndTimestamp:withTelemetryQueryResult:withTask:
+ _objc_msgSend$logNotificationMetricsWithTask:
+ _objc_msgSend$logNotificationSettingsMetrics
+ _objc_msgSend$mapVisitProbabilitiesByUUID:
+ _objc_msgSend$maxProbability
+ _objc_msgSend$maxProbabilityMicroLocationIdentifier
+ _objc_msgSend$microLocationIdentifier
+ _objc_msgSend$mostRecentMicroLocationWithinSeconds:
+ _objc_msgSend$probability
+ _objc_msgSend$queryTimeInterval
+ _objc_msgSend$relevantShortcut
+ _objc_msgSend$resultStatusForJob
+ _objc_msgSend$setAreHighlightsEnabled:
+ _objc_msgSend$setAreSummariesEnabled:
+ _objc_msgSend$setQueryTimeInterval:
+ _objc_msgSend$sleepStartTime
+ _objc_msgSend$subscribeWithCallback:
+ _objc_msgSend$subscribeWithCallback:onQueue:
+ _objc_msgSend$temporaryPathForTesting
+ _objc_msgSend$tombstoneDSLPublisherWithUseCase:
+ _objc_msgSend$triggerBackgroundJobWithIdentifier:configuration:completion:
+ _objc_msgSend$unSubscribeWithToken:
+ _objc_msgSend$uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:
+ _objc_msgSend$wakeUpTime
+ _replacementContainerBundleIdForDonationBundleId:._pasOnceToken40
- +[ATXAppClipUsageDuetDataProvider supportedCoreDuetStream]
- +[ATXAppIntentDuetDataProvider supportedCoreDuetStream]
- +[ATXAppLaunchDuetDataProvider supportedCoreDuetStream]
- +[ATXAudioDuetDataProvider supportedCoreDuetStream]
- +[ATXBluetoothDuetDataProvider supportedCoreDuetStream]
- +[ATXCarPlayDuetDataProvider supportedCoreDuetStream]
- +[ATXChargerPluggedInDuetDataProvider supportedCoreDuetStream]
- +[ATXDuetDataProvider atxHelperStreamTypeToATXEventStream:]
- +[ATXDuetDataProvider atxHelperStreamTypeToATXEventStream:].cold.1
- +[ATXDuetDataProvider supportedCoreDuetStream]
- +[ATXDuetKnowledgeStoreManager sharedInstance]
- +[ATXLocationVisitDuetDataProvider supportedCoreDuetStream]
- +[ATXMicrolocationVisitDuetDataProvider supportedCoreDuetStream]
- +[ATXNowPlayingDuetDataProvider supportedCoreDuetStream]
- +[ATXPOICategoryVisitDuetDataProvider supportedCoreDuetStream]
- +[ATXScreenLockStateDuetDataProvider supportedCoreDuetStream]
- +[ATXTripDuetDataProvider supportedCoreDuetStream]
- +[_ATXDuetHelper sharedInstance]
- +[_ATXDuetHelper sharedInstance].cold.1
- -[ATXActionDonationToPETLogger .cxx_destruct]
- -[ATXActionDonationToPETLogger abGroup]
- -[ATXActionDonationToPETLogger actionTypeIsActivity:]
- -[ATXActionDonationToPETLogger initWithDataStore:intentStream:activityStream:currentDate:tracker:]
- -[ATXActionDonationToPETLogger init]
- -[ATXActionDonationToPETLogger logActionDonationMetricsToPET]
- -[ATXActionDonationToPETLogger logDonationCountWithAlogEventCount:forIntents:]
- -[ATXActionDonationToPETLogger logDonationRatioWithDuetEventCount:alogEventCount:forIntents:]
- -[ATXActionDonationToPETLogger setabGroup:]
- -[ATXAppClipUsageDuetEvent initWithDKEvent:]
- -[ATXAppIntentDuetEvent initWithDKEvent:]
- -[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]
- -[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:].cold.1
- -[ATXAppLaunchDuetEvent initWithDKEvent:]
- -[ATXAppLaunchDuetEvent initWithDKEvent:].cold.1
- -[ATXAppLaunchMicroLocation _receivedNotificationOfNewMicroLocation]
- -[ATXAppLaunchMicroLocation _subscribeToDKInsertionEvents]
- -[ATXAppLaunchMicroLocation initWithDuetHelper:appInFocusStream:combinedIntentStream:directory:forTesting:]
- -[ATXAudioDuetEvent initWithDKEvent:]
- -[ATXBluetoothDuetEvent initWithDKEvent:]
- -[ATXBluetoothDuetEvent initWithDKEvent:].cold.1
- -[ATXCarPlayDuetEvent initWithDKEvent:]
- -[ATXChargerPluggedInDuetEvent initWithDKEvent:]
- -[ATXChargerPluggedInDuetEvent initWithDKEvent:].cold.1
- -[ATXDuetCallbackGuardedData .cxx_destruct]
- -[ATXDuetDataProvider assertValidDuetStream]
- -[ATXDuetDataProvider assertValidDuetStream].cold.1
- -[ATXDuetDataProvider assertValidDuetStream].cold.2
- -[ATXDuetDataProvider assertValidDuetStream].cold.3
- -[ATXDuetDataProvider assertValidDuetStream].cold.4
- -[ATXDuetDataProvider assertValidDuetStream].cold.5
- -[ATXDuetDataProvider assertValidDuetStream].cold.6
- -[ATXDuetDataProvider assertValidDuetStream].cold.7
- -[ATXDuetDataProvider assertValidDuetStream].cold.8
- -[ATXDuetDataProvider assertValidDuetStream].cold.9
- -[ATXDuetDataProvider fetchEventIdentifierCountsBetweenStartDate:andEndDate:withPredicates:]
- -[ATXDuetDataProvider fetchEventIdentifierCountsBetweenStartDate:andEndDate:withPredicates:dateBuckets:]
- -[ATXDuetDataProvider filteredEventsWithPredicate:]
- -[ATXDuetDataProvider getUniqueValuesForPropertyKey:]
- -[ATXDuetDataProvider tagEventsWithLocationsFromLocationVisitsArray:]
- -[ATXDuetEvent initWithDKEvent:]
- -[ATXDuetEvent initWithDKEvent:].cold.1
- -[ATXDuetGuardedRootOfAppData .cxx_destruct]
- -[ATXDuetKnowledgeStoreManager .cxx_destruct]
- -[ATXDuetKnowledgeStoreManager _clear]
- -[ATXDuetKnowledgeStoreManager _handleMemoryPressure]
- -[ATXDuetKnowledgeStoreManager dealloc]
- -[ATXDuetKnowledgeStoreManager init]
- -[ATXDuetKnowledgeStoreManager runBlock:]
- -[ATXDuetKnowledgeStoreManager saveEventsAsynchronously:responseQueue:completion:]
- -[ATXMicrolocationVisitDuetDataProvider adjustDatesForMicrolocationEvents:]
- -[ATXMicrolocationVisitDuetEvent initWithCurrentContextStoreValuesWithTwoHourLimit:].cold.1
- -[ATXMicrolocationVisitDuetEvent initWithDKEvent:]
- -[ATXMicrolocationVisitDuetEvent initWithDKEvent:].cold.1
- -[ATXMicrolocationVisitDuetEvent initWithDKEvent:].cold.2
- -[ATXMicrolocationVisitDuetEvent initWithDKEvent:].cold.3
- -[ATXMicrolocationVisitDuetEvent initWithDKEvent:].cold.4
- -[ATXNotificationSettingsLogger logNotificationSettingsMetricsWithXPCActivity:]
- -[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withXPCActivity:]
- -[ATXNotificationTelemetryLogger logNotificationMetricsWithBreakthroughFeaturesFromStartTimestamp:toEndTimestamp:withTelemetryQueryResult:withXPCActivity:]
- -[ATXNotificationTelemetryLogger logNotificationMetricsWithXPCActivity:]
- -[ATXNowPlayingDuetEvent initWithDKEvent:]
- -[ATXNowPlayingDuetEvent initWithDKEvent:].cold.1
- -[ATXProactiveSuggestionFeedbackMetricsLogger(iOS) bookmarkURLPathForConsumerSubType:]
- -[ATXProactiveSuggestionFeedbackMetricsLogger(iOS) logMetricsForiOSUIFeedbackQueries]
- -[ATXRSWidgetSuggestionProducer initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]
- -[ATXScreenLockStateDuetEvent initWithDKEvent:]
- -[ATXScreenLockStateDuetEvent initWithDKEvent:].cold.1
- -[ATXSleepSuggestionServer queryEvents].cold.1
- -[_ATXDuetHelper .cxx_destruct]
- -[_ATXDuetHelper _countDuetStream:startDate:endDate:otherPredicates:limit:]
- -[_ATXDuetHelper _enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:ascending:block:]
- -[_ATXDuetHelper _enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:batchSize:ascending:block:]
- -[_ATXDuetHelper _enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:batchSize:ascending:block:].cold.1
- -[_ATXDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:ascending:block:]
- -[_ATXDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:batchSize:ascending:block:]
- -[_ATXDuetHelper _enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:batchSize:ascending:block:].cold.1
- -[_ATXDuetHelper _queryDuetStream:startDate:endDate:otherPredicates:limit:]
- -[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:]
- -[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:].cold.1
- -[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:].cold.2
- -[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:]
- -[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:].cold.1
- -[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:].cold.2
- -[_ATXDuetHelper enumerateRelevantShortcutsAndBundleIdsBetweenStartDate:endDate:limit:block:]
- -[_ATXDuetHelper getMicroLocationsFromLastMonth]
- -[_ATXDuetHelper getMostRecentMicroLocation]
- -[_ATXDuetHelper getScreenTransitionsBetweenStartDate:endDate:]
- -[_ATXDuetHelper init]
- -[_DKEvent(ATX) atx_efficientRelevantShortcut]
- -[_DKEvent(ATX) atx_efficientRelevantShortcut].cold.1
- -[_DKEvent(ATX) atx_efficientRelevantShortcut].cold.2
- OBJC_IVAR_$_ATXDuetCallbackGuardedData._deletionHandlers
- OBJC_IVAR_$_ATXDuetCallbackGuardedData.nextRegistrationToken
- OBJC_IVAR_$_ATXDuetGuardedRootOfAppData._rootOfAppData
- OBJC_IVAR_$_ATXDuetGuardedRootOfAppData._rootOfAppDataUpdateTime
- _OBJC_CLASS_$_ATXActionDonationToPETLogger
- _OBJC_CLASS_$_ATXDuetCallbackGuardedData
- _OBJC_CLASS_$_ATXDuetGuardedRootOfAppData
- _OBJC_CLASS_$_ATXDuetKnowledgeStoreManager
- _OBJC_CLASS_$_ATXProactiveSuggestionFeedbackMetricsLogger
- _OBJC_CLASS_$_INRelevantShortcut
- _OBJC_CLASS_$__ATXDuetHelper
- _OBJC_CLASS_$__DKEventQuery
- _OBJC_CLASS_$__DKMicroLocationMetadataKey
- _OBJC_CLASS_$__DKRelevantShortcutMetadataKey
- _OBJC_CLASS_$__DKSystemEventStreams
- _OBJC_IVAR_$_ATXActionDonationToPETLogger._abGroup
- _OBJC_IVAR_$_ATXActionDonationToPETLogger._activityStream
- _OBJC_IVAR_$_ATXActionDonationToPETLogger._currentDate
- _OBJC_IVAR_$_ATXActionDonationToPETLogger._dataStore
- _OBJC_IVAR_$_ATXActionDonationToPETLogger._intentStream
- _OBJC_IVAR_$_ATXActionDonationToPETLogger._tracker
- _OBJC_IVAR_$_ATXAppIntentMonitor._duetHelper
- _OBJC_IVAR_$_ATXAppLaunchMicroLocation._duetHelper
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._expirationSource
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._lastUsedDate
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._pressureSource
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._previousPressure
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._queue
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._savingStore
- _OBJC_IVAR_$_ATXDuetKnowledgeStoreManager._store
- _OBJC_IVAR_$_ATXRSWidgetSuggestionProducer._duetHelper
- _OBJC_IVAR_$__ATXDuetHelper._rootOfAppDataLock
- _OBJC_METACLASS_$_ATXActionDonationToPETLogger
- _OBJC_METACLASS_$_ATXDuetCallbackGuardedData
- _OBJC_METACLASS_$_ATXDuetGuardedRootOfAppData
- _OBJC_METACLASS_$_ATXDuetKnowledgeStoreManager
- _OBJC_METACLASS_$__ATXDuetHelper
- __DKKnowledgeStorageDidInsertEventsNotification
- __DKKnowledgeStorageDidInsertLocalEventsNotification
- __DKKnowledgeStorageDidTombstoneEventsNotification
- __OBJC_$_CATEGORY_ATXProactiveSuggestionFeedbackMetricsLogger_$_iOS
- __OBJC_$_CATEGORY_INSTANCE_METHODS_ATXProactiveSuggestionFeedbackMetricsLogger_$_iOS
- __OBJC_$_CLASS_METHODS_ATXDuetKnowledgeStoreManager
- __OBJC_$_CLASS_METHODS__ATXDuetHelper
- __OBJC_$_INSTANCE_METHODS_ATXActionDonationToPETLogger
- __OBJC_$_INSTANCE_METHODS_ATXDuetCallbackGuardedData
- __OBJC_$_INSTANCE_METHODS_ATXDuetGuardedRootOfAppData
- __OBJC_$_INSTANCE_METHODS_ATXDuetKnowledgeStoreManager
- __OBJC_$_INSTANCE_METHODS__ATXDuetHelper
- __OBJC_$_INSTANCE_METHODS__DKEvent(ATXLocationVisitDuetEvent|ATX|ATXMode)
- __OBJC_$_INSTANCE_VARIABLES_ATXActionDonationToPETLogger
- __OBJC_$_INSTANCE_VARIABLES_ATXDuetCallbackGuardedData
- __OBJC_$_INSTANCE_VARIABLES_ATXDuetGuardedRootOfAppData
- __OBJC_$_INSTANCE_VARIABLES_ATXDuetKnowledgeStoreManager
- __OBJC_$_INSTANCE_VARIABLES__ATXDuetHelper
- __OBJC_CLASS_RO_$_ATXActionDonationToPETLogger
- __OBJC_CLASS_RO_$_ATXDuetCallbackGuardedData
- __OBJC_CLASS_RO_$_ATXDuetGuardedRootOfAppData
- __OBJC_CLASS_RO_$_ATXDuetKnowledgeStoreManager
- __OBJC_CLASS_RO_$__ATXDuetHelper
- __OBJC_METACLASS_RO_$_ATXActionDonationToPETLogger
- __OBJC_METACLASS_RO_$_ATXDuetCallbackGuardedData
- __OBJC_METACLASS_RO_$_ATXDuetGuardedRootOfAppData
- __OBJC_METACLASS_RO_$_ATXDuetKnowledgeStoreManager
- __OBJC_METACLASS_RO_$__ATXDuetHelper
- ___101-[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:]_block_invoke
- ___101-[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:]_block_invoke.cold.1
- ___104-[ATXDuetDataProvider fetchEventIdentifierCountsBetweenStartDate:andEndDate:withPredicates:dateBuckets:]_block_invoke
- ___106-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withXPCActivity:]_block_invoke
- ___106-[ATXNotificationTelemetryLogger logNotificationMetricsFromStartTimestamp:toEndTimestamp:withXPCActivity:]_block_invoke_2
- ___117-[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:]_block_invoke
- ___117-[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:]_block_invoke.cold.1
- ___121-[ATXCandidateRelevanceModelDatasetGenerator initWithConfig:inferredModeStream:computedModeStream:pointOfInterestStream:]_block_invoke.136
- ___212-[ATXRSWidgetSuggestionProducer initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke
- ___212-[ATXRSWidgetSuggestionProducer initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.41
- ___212-[ATXRSWidgetSuggestionProducer initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:]_block_invoke.cold.1
- ___244-[ATXAppIntentMonitor initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:]_block_invoke
- ___32+[_ATXDuetHelper sharedInstance]_block_invoke
- ___41-[ATXDuetKnowledgeStoreManager runBlock:]_block_invoke
- ___41-[ATXDuetKnowledgeStoreManager runBlock:]_block_invoke_2
- ___41-[ATXDuetKnowledgeStoreManager runBlock:]_block_invoke_3
- ___44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.82
- ___44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.82.cold.1
- ___44-[ATXAppIntentMonitor _listenToIntentStream]_block_invoke.85
- ___46+[ATXDuetKnowledgeStoreManager sharedInstance]_block_invoke
- ___46-[ATXAppIntentMonitor _listenToActivityStream]_block_invoke.73
- ___48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.92
- ___48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.92.cold.1
- ___48-[ATXAppIntentMonitor _listenToLinkActionStream]_block_invoke.99
- ___48-[_ATXDuetHelper getMicroLocationsFromLastMonth]_block_invoke
- ___53-[ATXDuetKnowledgeStoreManager _handleMemoryPressure]_block_invoke
- ___61-[ATXActionDonationToPETLogger logActionDonationMetricsToPET]_block_invoke
- ___63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.61
- ___63-[ATXSleepSuggestionServer listener:shouldAcceptNewConnection:]_block_invoke.61.cold.1
- ___63-[_ATXDuetHelper getScreenTransitionsBetweenStartDate:endDate:]_block_invoke
- ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.83
- ___64-[ATXModeEntityScorerServer listener:shouldAcceptNewConnection:]_block_invoke.83.cold.1
- ___66-[ATXAppLaunchMicroLocation tryLoadCorrelationMatricesImmediately]_block_invoke.79
- ___68-[ATXAppLaunchMicroLocation _receivedNotificationOfNewMicroLocation]_block_invoke
- ___71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.68
- ___71-[ATXRSWidgetSuggestionProducer _pushSuggestionsToBlendingIfNecessary:]_block_invoke.68.cold.1
- ___75-[ATXMicrolocationVisitDuetDataProvider adjustDatesForMicrolocationEvents:]_block_invoke
- ___75-[_ATXDuetHelper _countDuetStream:startDate:endDate:otherPredicates:limit:]_block_invoke
- ___75-[_ATXDuetHelper _queryDuetStream:startDate:endDate:otherPredicates:limit:]_block_invoke
- ___79-[ATXRSWidgetSuggestionProducer _candidatesFromRelevantShortcutsFromStartDate:]_block_invoke.60
- ___82-[ATXDuetKnowledgeStoreManager saveEventsAsynchronously:responseQueue:completion:]_block_invoke
- ___92-[ATXDuetDataProvider fetchEventIdentifierCountsBetweenStartDate:andEndDate:withPredicates:]_block_invoke
- ___93-[ATXDuetDataProvider fetchEventsBetweenStartDate:andEndDate:withPredicates:limit:ascending:]_block_invoke
- ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
- ___block_descriptor_48_e8_32s40r_e47_v32?0"ATXMicrolocationVisitDuetEvent"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e41_v24?0"INRelevantShortcut"8"NSString"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e32_B32?0q8"NSString"16"NSDate"24ls32l8r40l8r48l8
- ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_73_e8_32s40s48r_e32_v16?0"<_DKKnowledgeQuerying>"8ls32l8s40l8r48l8
- ___block_literal_global.139
- ___block_literal_global.144
- ___block_literal_global.147
- ___block_literal_global.579
- ___block_literal_global.584
- ___block_literal_global.588
- ___block_literal_global.599
- ___block_literal_global.608
- ___block_literal_global.613
- ___block_literal_global.616
- ___block_literal_global.63
- ___block_literal_global.630
- ___block_literal_global.635
- ___block_literal_global.639
- ___block_literal_global.643
- ___block_literal_global.647
- ___block_literal_global.659
- ___block_literal_global.663
- ___block_literal_global.667
- ___block_literal_global.671
- ___block_literal_global.677
- ___block_literal_global.683
- ___block_literal_global.693
- ___block_literal_global.697
- ___block_literal_global.706
- ___block_literal_global.709
- ___block_literal_global.712
- ___block_literal_global.718
- ___block_literal_global.722
- ___block_literal_global.726
- ___block_literal_global.730
- ___block_literal_global.735
- ___block_literal_global.740
- ___block_literal_global.749
- ___block_literal_global.82
- ___block_literal_global.85
- ___registerForCarPlayMetricsBGSTJob_block_invoke.737
- ___registerForFaceSuggestionsCTSJob_block_invoke.653
- ___registerForFaceSuggestionsCTSJob_block_invoke.653.cold.1
- ___registerForFeedbackMetricsLoggingCTSJob_block_invoke
- ___registerForNotificationAndSuggestionDatastorePruning_block_invoke.704
- ___registerForPeriodicLogUploadCTSJob_block_invoke
- __dispatch_source_type_memorypressure
- __enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:batchSize:ascending:block:.duetLock
- __enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:batchSize:ascending:block:.duetLock
- _dispatch_source_get_data
- _kATXDuetHelperBatchSize
- _kATXDuetHelperTrainingJobBatchSize
- _microLocationEventFromDK
- _objc_msgSend$_clear
- _objc_msgSend$_enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:batchSize:ascending:block:
- _objc_msgSend$_enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:ascending:block:
- _objc_msgSend$_enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:batchSize:ascending:block:
- _objc_msgSend$_handleMemoryPressure
- _objc_msgSend$_queryDuetStream:startDate:endDate:otherPredicates:limit:
- _objc_msgSend$_queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:
- _objc_msgSend$_queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:
- _objc_msgSend$_subscribeToDKInsertionEvents
- _objc_msgSend$actionTypeIsActivity:
- _objc_msgSend$appInFocusStream
- _objc_msgSend$appRelevantShortcutsStream
- _objc_msgSend$assertValidDuetStream
- _objc_msgSend$atxHelperStreamTypeToATXEventStream:
- _objc_msgSend$atx_efficientRelevantShortcut
- _objc_msgSend$bookmarkURLPathForConsumerSubType:
- _objc_msgSend$displayIsBacklit
- _objc_msgSend$duetStream
- _objc_msgSend$enumerateActionTypesOlderThan:block:
- _objc_msgSend$enumerateRelevantShortcutsAndBundleIdsBetweenStartDate:endDate:limit:block:
- _objc_msgSend$eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:
- _objc_msgSend$eventStreams
- _objc_msgSend$executeQuery:error:
- _objc_msgSend$flushCountedPredictionUpdatesToLogger
- _objc_msgSend$getMicroLocationsFromLastMonth
- _objc_msgSend$getMostRecentMicroLocation
- _objc_msgSend$initWithATXStream:
- _objc_msgSend$initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:
- _objc_msgSend$initWithDKEvent:
- _objc_msgSend$initWithDataStore:intentStream:activityStream:currentDate:tracker:
- _objc_msgSend$initWithDuetHelper:appInFocusStream:combinedIntentStream:directory:forTesting:
- _objc_msgSend$initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:
- _objc_msgSend$initWithDuetStream:
- _objc_msgSend$initWithHyperParameters:
- _objc_msgSend$knowledgeStoreWithDirectReadOnlyAccess
- _objc_msgSend$logActionDonationMetricsToPET
- _objc_msgSend$logCountedAppLaunchesToEventTracker
- _objc_msgSend$logDonationCountWithAlogEventCount:forIntents:
- _objc_msgSend$logDonationRatioWithDuetEventCount:alogEventCount:forIntents:
- _objc_msgSend$logMetricsForiOSUIFeedbackQueries
- _objc_msgSend$logMetricsWithUIFeedbackQuery:
- _objc_msgSend$logNotificationMetricsFromStartTimestamp:toEndTimestamp:withXPCActivity:
- _objc_msgSend$logNotificationMetricsWithBreakthroughFeaturesFromStartTimestamp:toEndTimestamp:withTelemetryQueryResult:withXPCActivity:
- _objc_msgSend$logNotificationMetricsWithXPCActivity:
- _objc_msgSend$logNotificationSettingsMetricsWithXPCActivity:
- _objc_msgSend$microLocationVisitStream
- _objc_msgSend$numberOfActivityEventsBetweenStartDate:endDate:
- _objc_msgSend$numberOfIntentEventsBetweenStartDate:endDate:
- _objc_msgSend$predicateForEventsWithIntegerValue:
- _objc_msgSend$runBlock:
- _objc_msgSend$saveObjects:responseQueue:withCompletion:
- _objc_msgSend$serializedRelevantShortcut
- _objc_msgSend$setExecuteConcurrently:
- _objc_msgSend$supportedCoreDuetStream
- _objc_msgSend$userIsFirstBacklightOnAfterWakeup
- _replacementContainerBundleIdForDonationBundleId:._pasOnceToken34
- _sharedInstance._pasOnceToken9
CStrings:
+ "%@ - Deferring after notification event metrics logging"
+ "%@ - Deferring after notification telemetry logging"
+ "%@ - Deferring after summary metrics logging"
+ "@\"ATXMicroLocationVisitStream\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "ATXMicrolocationVisitAnchor notification listener has moved to Biome scheduler via ATXMicroLocationVisitScheduler"
+ "ATXMicrolocationVisitAnchor.m"
+ "ATXNotificationManagementSettingsMetric numDailyDigests:%lu\nnumDigestApps:%lu\nnumConfiguredModes:%lu\nhasOfferedDigest:%d\nhasSetupDigest:%d\nareHighlightsEnabled:%@\nareSummariesEnabled:%@"
+ "ATXRSWidgetSuggestionProducer: Got %lu relevant shortcut candidates for widget suggestion"
+ "ATXRSWidgetSuggestionProducer: Triggering coalesced refresh due to BMAppRelevantShortcuts event : %@"
+ "ATXRSWidgetSuggestionProducer: Triggering coalesced refresh due to Tombstone event : %@"
+ "ATXRSWidgetSuggestionProducer: couldn't refresh relevant shortcuts during tombstone event because self is nil"
+ "ATXSleepSuggestionServer: Bedtime counted in the prediction:%@"
+ "ATXSleepSuggestionServer: Failed to retrieve sleep events from ATXSleepStream"
+ "ATXSleepSuggestionServer: Wakeup time counted in the prediction:%@"
+ "ActionPredictionFirstStageBeamWidthMacOS"
+ "App.RelevantShortcuts"
+ "App.RelevantShortcuts.Tombstone"
+ "B16@?0@\"ATXMicroLocationVisitEvent\"8"
+ "B16@?0@\"ATXRelevantShortcutsEvent\"8"
+ "Could not subscribe to App.RelevantShortcuts: %@"
+ "Failed to initialize ATXApp2VecMapping"
+ "Notification metrics logging immediately deferred"
+ "Notification metrics logging task could not be set to DONE"
+ "Notification metrics logging task successfully set to DONE"
+ "NotificationMetricsLogging.Total"
+ "Processing and uploading Notification metrics events to CoreAnalytics"
+ "RelevantShortcuts"
+ "Skipping microlocation event because it’s too old (%.0f seconds ago)"
+ "T@\"NSNumber\",&,N,V_areHighlightsEnabled"
+ "T@\"NSNumber\",&,N,V_areSummariesEnabled"
+ "Td,N,V_queryTimeInterval"
+ "The respective subclass should implement this instead with its own relevant stream"
+ "Unable to observe relevant shortcuts deletion for : %@"
+ "_areHighlightsEnabled"
+ "_areSummariesEnabled"
+ "_makeNotificationTelemetryQueryResultFromDatabaseResult:queryTimeInterval:"
+ "_microLocationSchedulerToken"
+ "_microLocationStream"
+ "_queryTimeInterval"
+ "_receivedNotificationOfNewMicroLocation:"
+ "_relevantShortcutsStreamScheduler"
+ "_relevantShortcutsStreamSink"
+ "_relevantShortcutsTombstoneScheduler"
+ "_relevantShortcutsTombstoneSink"
+ "_subscribeToMicroLocationEvents"
+ "_targetQueueForBiome"
+ "_writeMetricsToTemporaryLocation:"
+ "actionPredictionFirstStageBeamWidthMacOS"
+ "areHighlightsEnabled"
+ "areSummariesEnabled"
+ "com.apple.duetexpertd.RelevantShortcutsObserver"
+ "com.apple.duetexpertd.notificationmetrics"
+ "enumerateEventsFromStartDate:endDate:limit:block:"
+ "enumerateMicroLocationVisitEventsFromStartDate:endDate:filterBlock:limit:ascending:block:"
+ "enumerateSleepEventsFromStartDate:endDate:limit:block:"
+ "initForTestingWithIdentifier:configuration:"
+ "initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:"
+ "initWithDescriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:"
+ "initWithMicroLocationStream:appInFocusStream:combinedIntentStream:directory:forTesting:"
+ "logNotificationMetricsFromStartTimestamp:toEndTimestamp:withTask:"
+ "logNotificationMetricsWithBreakthroughFeaturesFromStartTimestamp:toEndTimestamp:withTelemetryQueryResult:withTask:"
+ "logNotificationMetricsWithTask:"
+ "mapVisitProbabilitiesByUUID:"
+ "maxProbability"
+ "maxProbabilityMicroLocationIdentifier"
+ "microLocationIdentifier"
+ "mostRecentMicroLocationWithinSeconds:"
+ "probability"
+ "queryTimeInterval"
+ "rankedAppsForMode:options:reply:"
+ "rankedContactsForMode:options:reply:"
+ "rankedNotificationsForMode:options:reply:"
+ "relevantShortcut"
+ "resultStatusForJob"
+ "setAreHighlightsEnabled:"
+ "setAreSummariesEnabled:"
+ "setQueryTimeInterval:"
+ "sleepStartTime"
+ "subscribeWithCallback:"
+ "subscribeWithCallback:onQueue:"
+ "temporaryPathForTesting"
+ "tombstoneDSLPublisherWithUseCase:"
+ "triggerBackgroundJobWithIdentifier:configuration:completion:"
+ "unSubscribeWithToken:"
+ "uploadNotificationLogsToCoreAnalyticsWithTask:contactStore:"
+ "v16@?0@\"ATXMicroLocationVisitEvent\"8"
+ "v24@?0@\"ATXSleepEvent\"8^B16"
+ "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@16^f24@32"
+ "wakeUpTime"
- "%@ - has duetIntentCount: %lu duetActivityCount: %lu alogIntentCount: %lu alogActivityCount: %lu"
- "%s: Found nil bundleId for appRelevantShortcutsStream _DKEvent %@"
- "%s: nil relevant shortcut for appRelevantShortcutsStream _DKEvent with bundleId %@"
- "(startDate > %@ AND startDate < %@) OR (endDate > %@ AND endDate < %@)"
- "-[ATXMicrolocationVisitDuetEvent initWithCurrentContextStoreValuesWithTwoHourLimit:]"
- "-[ATXSleepSuggestionServer queryEvents]"
- "-[_ATXDuetHelper _queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:]_block_invoke"
- "-[_ATXDuetHelper _queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:]_block_invoke"
- "-[_ATXDuetHelper enumerateRelevantShortcutsAndBundleIdsBetweenStartDate:endDate:limit:block:]"
- "@\"<_DKKnowledgeQuerying>\""
- "@\"<_DKKnowledgeSaving>\""
- "@\"ATXRootOfAppData\""
- "@\"_ATXDuetHelper\""
- "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "@68@0:8@16@24@32B40@44Q52Q60"
- "ATX"
- "ATXActionDonationToPETLogger"
- "ATXAppClipUsageDuetEvent has moved to ATX event based initialization"
- "ATXAppClipUsageDuetEvent.m"
- "ATXAppIntentDuetEvent has moved to ATX event based initialization"
- "ATXAppIntentDuetEvent.m"
- "ATXAppLaunchDuetEvent has moved to ATX event based initialization"
- "ATXAppLaunchDuetEvent.m"
- "ATXAudioDuetEvent.m"
- "ATXBluetoothDuetEvent has moved to ATX event based initialization"
- "ATXBluetoothDuetEvent.m"
- "ATXCarPlayDuetEvent.m"
- "ATXChargerPluggedInDuetEvent has moved to ATX event based initialization"
- "ATXChargerPluggedInDuetEvent.m"
- "ATXDataProviderStreamTypeAppClipUsage tried to query data via Duet stream"
- "ATXDataProviderStreamTypeAppIntent tried to query data via Duet stream"
- "ATXDataProviderStreamTypeAppLaunch tried to query data via Duet stream"
- "ATXDataProviderStreamTypeAudio tried to query data via Duet stream"
- "ATXDataProviderStreamTypeBluetooth tried to query data via Duet stream"
- "ATXDataProviderStreamTypeCarPlay tried to query data via Duet stream"
- "ATXDataProviderStreamTypeChargerPluggedIn tried to query data via Duet stream"
- "ATXDataProviderStreamTypeNowPlaying tried to query data via Duet stream"
- "ATXDataProviderStreamTypeScreenLockState tried to query data via Duet stream"
- "ATXDuetCallbackGuardedData"
- "ATXDuetGuardedRootOfAppData"
- "ATXDuetKnowledgeStoreManager"
- "ATXMicrolocationVisitDuetEvent.m"
- "ATXModeIsSleepingBasedOnBacklightDataFeaturizer: Bedtime counted in the prediction:%@"
- "ATXModeIsSleepingBasedOnBacklightDataFeaturizer: Error querying Core Duet: %@"
- "ATXModeIsSleepingBasedOnBacklightDataFeaturizer: Wakeup time counted in the prediction:%@"
- "ATXNotificationManagementSettingsMetric numDailyDigests:%lu\nnumDigestApps:%lu\nnumConfiguredModes:%lu\nhasOfferedDigest:%d\nhasSetupDigest:%d"
- "ATXNowPlayingDuetEvent has moved to ATX event based initialization"
- "ATXNowPlayingDuetEvent.m"
- "ATXRSWidgetSuggestionProducer: Refetched CoreDuet. Got %lu relevant shortcut candidates for widget suggestion"
- "ATXScreenLockStateDuetEvent has moved to ATX event based initialization"
- "ATXScreenLockStateDuetEvent.m"
- "ATXSleepSuggestionServer: Failed to retrieve userIsFirstBacklightOnAfterWakeup"
- "AudioDuetEvent has moved to ATX event based initialization"
- "B32@?0q8@\"NSString\"16@\"NSDate\"24"
- "B40@0:8@16^f24@32"
- "CarPlayDuetEvent has moved to ATX event based initialization"
- "Duet query: %{public}@, %s, %@"
- "DuetQuery"
- "Error fetching latest microlocation %@"
- "Error querying Duet: %@"
- "Error unarchiving relevant shortcut: %@"
- "Evicting Duet store"
- "Failure to extract relevant shortcut from event with no serialized data"
- "Finished periodic logging"
- "LOGGED: %@ - ATXMDonationCountTracker with type: %@ count: %lu abGroup: %@"
- "LOGGED: %@ - ATXMPBDonationRatioTracker with type: %@ ratio: %f abGroup: %@"
- "Method is not yet implemented"
- "Q56@0:8@16@24@32@40Q48"
- "Returning nil _DKEventStream for ATXDuetDataProviderStreamType %ld."
- "Running Blending Feedback Metrics logging..."
- "Running periodic logging..."
- "Running periodic logging: Core Duet action log donation metrics"
- "Running periodic logging: counted app launches"
- "Running periodic logging: counted prediction updates"
- "Skipping microlocation event because it happened too long ago (%.2f seconds ago)"
- "Stream=%{public,signpost.telemetry:string1}s  enableTelemetry=YES "
- "Trying to access KnowledgeStore stream for None stream."
- "Value for metadata key for Microlocation 'probabilityVector' is not an NSDictionary, %@"
- "Value of _DKEvent was %@, not %@"
- "_ATXDuetHelper"
- "_ATXDuetHelper.m"
- "_clear"
- "_countDuetStream:startDate:endDate:otherPredicates:limit:"
- "_currentDate"
- "_deletionHandlers"
- "_duetHelper"
- "_enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:ascending:block:"
- "_enumerateBatchesInDuetStream:creationDateStart:creationDateEnd:otherPredicates:limit:batchSize:ascending:block:"
- "_enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:ascending:block:"
- "_enumerateBatchesInDuetStream:startDate:endDate:otherPredicates:limit:batchSize:ascending:block:"
- "_expirationSource"
- "_handleMemoryPressure"
- "_lastUsedDate"
- "_pressureSource"
- "_previousPressure"
- "_queryDuetStream:startDate:endDate:otherPredicates:limit:"
- "_queryDuetStreamUnbatched:creationDateStart:creationDateEnd:ascending:otherPredicates:limit:offset:"
- "_queryDuetStreamUnbatched:startDate:endDate:ascending:otherPredicates:limit:offset:"
- "_receivedNotificationOfNewMicroLocation"
- "_rootOfAppData"
- "_rootOfAppDataLock"
- "_rootOfAppDataUpdateTime"
- "_savingStore"
- "_subscribeToDKInsertionEvents"
- "actionTypeIsActivity:"
- "adjustDatesForMicrolocationEvents:"
- "appRelevantShortcutsStream"
- "assertValidDuetStream"
- "atxHelperStreamTypeToATXEventStream:"
- "atx_efficientRelevantShortcut"
- "bookmarkURLPathForConsumerSubType:"
- "com.apple.duetexpertd.blendingfeedbackmetricslogging"
- "com.apple.duetexpertd.periodiclog"
- "confidence >= %@"
- "creationDate"
- "creationDate > %@ AND creationDate < %@"
- "displayIsBacklit"
- "enumerateRelevantShortcutsAndBundleIdsBetweenStartDate:endDate:limit:block:"
- "eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:"
- "eventStreams"
- "executeQuery:error:"
- "fetchEventIdentifierCountsBetweenStartDate:andEndDate:withPredicates:"
- "fetchEventIdentifierCountsBetweenStartDate:andEndDate:withPredicates:dateBuckets:"
- "filteredEventsWithPredicate:"
- "getMicroLocationsFromLastMonth"
- "getMostRecentMicroLocation"
- "getScreenTransitionsBetweenStartDate:endDate:"
- "getUniqueValuesForPropertyKey:"
- "iOS"
- "initWithAppLaunchHistogramManager:appInfoManager:appActionLaunchSequenceManager:duetHelper:intentStream:activityStream:menuItemStream:toolKitActionStream:dataStore:predictionContextBuilder:userDefaults:safariIntentFilter:"
- "initWithDKEvent:"
- "initWithDataStore:intentStream:activityStream:currentDate:tracker:"
- "initWithDuetHelper:appInFocusStream:combinedIntentStream:directory:forTesting:"
- "initWithDuetHelper:descriptorCache:relevanceMonitor:filter:abuseGuard:featurizer:featureWeights:ranker:confidenceMapper:suggestionReceiver:metadataProvider:widgetRelevanceService:"
- "initWithHyperParameters:"
- "knowledgeStoreWithDirectReadOnlyAccess"
- "limit > 0"
- "logActionDonationMetricsToPET"
- "logCountedAppLaunchesToEventTracker"
- "logDonationCountWithAlogEventCount:forIntents:"
- "logDonationRatioWithDuetEventCount:alogEventCount:forIntents:"
- "logMetricsForiOSUIFeedbackQueries"
- "logMetricsWithUIFeedbackQuery:"
- "logNotificationMetricsFromStartTimestamp:toEndTimestamp:withXPCActivity:"
- "logNotificationMetricsWithBreakthroughFeaturesFromStartTimestamp:toEndTimestamp:withTelemetryQueryResult:withXPCActivity:"
- "logNotificationMetricsWithXPCActivity:"
- "logNotificationSettingsMetricsWithXPCActivity:"
- "microLocationVisitStream"
- "nextRegistrationToken"
- "numberOfActivityEventsBetweenStartDate:endDate:"
- "numberOfIntentEventsBetweenStartDate:endDate:"
- "predicateForEventsWithIntegerValue:"
- "runBlock:"
- "saveEventsAsynchronously:responseQueue:completion:"
- "saveObjects:responseQueue:withCompletion:"
- "searchPredicate"
- "serializedRelevantShortcut"
- "setExecuteConcurrently:"
- "setabGroup:"
- "supportedCoreDuetStream"
- "tagEventsWithLocationsFromLocationVisitsArray:"
- "userIsFirstBacklightOnAfterWakeup"
- "v16@?0@\"<_DKKnowledgeQuerying>\"8"
- "v24@?0@\"INRelevantShortcut\"8@\"NSString\"16"
- "v32@?0@\"ATXMicrolocationVisitDuetEvent\"8Q16^B24"
- "v36@0:8Q16Q24B32"
- "v68@0:8@16@24@32@40Q48B56@?60"
- "v76@0:8@16@24@32@40Q48Q56B64@?68"

```
