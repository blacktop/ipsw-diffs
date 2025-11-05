## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler`

```diff

-1786.80.10.0.0
-  __TEXT.__text: 0x2e060
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x2ab4
+1856.101.1.0.0
+  __TEXT.__text: 0x3081c
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x38d0
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x1e9c
-  __TEXT.__oslogstring: 0x2384
-  __TEXT.__gcc_except_tab: 0x107c
-  __TEXT.__unwind_info: 0xcb0
-  __TEXT.__objc_classname: 0x66b
-  __TEXT.__objc_methname: 0x7d0a
-  __TEXT.__objc_methtype: 0x1533
-  __TEXT.__objc_stubs: 0x47a0
-  __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x398
-  __DATA_CONST.__objc_classlist: 0x100
+  __TEXT.__cstring: 0x2007
+  __TEXT.__oslogstring: 0x2487
+  __TEXT.__gcc_except_tab: 0x10c8
+  __TEXT.__unwind_info: 0xd80
+  __TEXT.__objc_classname: 0x6c8
+  __TEXT.__objc_methname: 0x8463
+  __TEXT.__objc_methtype: 0x15fa
+  __TEXT.__objc_stubs: 0x4c20
+  __DATA_CONST.__got: 0x278
+  __DATA_CONST.__const: 0x3f8
+  __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d20
+  __DATA_CONST.__objc_selrefs: 0x1f68
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x258
-  __AUTH_CONST.__const: 0xaf0
-  __AUTH_CONST.__cfstring: 0x2f60
-  __AUTH_CONST.__objc_const: 0x7650
+  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__cfstring: 0x2fa0
+  __AUTH_CONST.__objc_const: 0x6680
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x338
-  __DATA.__data: 0xd80
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x370
+  __DATA.__data: 0xde0
   __DATA.__bss: 0xa8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x500

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Network.framework/Versions/A/Network
+  - /System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub
+  - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/A/CoreDuetContext
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7404F2AD-EB2A-3951-8E93-4CC4ACE2B341
-  Functions: 1207
-  Symbols:   2971
-  CStrings:  2634
+  UUID: C8D4FBA5-67D8-3762-9170-8B22A8DCDA73
+  Functions: 1289
+  Symbols:   3158
+  CStrings:  2746
 
Symbols:
+ +[NSDate(_DASAdditions) dateFromAbsoluteTime:]
+ +[_DASActivity sharedDateFormatter].cold.1
+ +[_DASActivity validClassesForUserInfoSerialization].cold.1
+ +[_DASBMHistogramBuilder builderWithPublisher:]
+ +[_DASBMHistogramBuilder builderWithPublisher:saveSpans:]
+ +[_DASBMMinimumSpanConfiguration configurationWithMinimumDuration:aggregationKey:spanMarker:]
+ +[_DASExtensionRemoteContext _extensionAuxiliaryHostProtocol].cold.1
+ +[_DASExtensionRemoteContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[_DASFileProtection none].cold.1
+ +[_DASScheduler log].cold.1
+ +[_DASScheduler sharedScheduler].cold.1
+ +[_DASSystemContext defaultInexpensivePathEvaluator].cold.1
+ +[_DASSystemContext defaultPathEvaluator].cold.1
+ +[_DASWidgetRefreshScheduler sharedScheduler].cold.1
+ -[NSDate(_DASAdditions) isAfter:]
+ -[NSDate(_DASAdditions) isBefore:]
+ -[NSDate(_DASAdditions) isSameDayOfWeekAs:withCalendar:]
+ -[_DASActivity runWhenAppLaunchUnlikely]
+ -[_DASActivity setRunWhenAppLaunchUnlikely:]
+ -[_DASBMHistogramBuilder .cxx_destruct]
+ -[_DASBMHistogramBuilder filter]
+ -[_DASBMHistogramBuilder histogramOnResponseQueue:withCompletion:]
+ -[_DASBMHistogramBuilder histogram]
+ -[_DASBMHistogramBuilder initWithPublisher:saveSpans:]
+ -[_DASBMHistogramBuilder log]
+ -[_DASBMHistogramBuilder minimumSpanConfiguration]
+ -[_DASBMHistogramBuilder publisher]
+ -[_DASBMHistogramBuilder saveSpans]
+ -[_DASBMHistogramBuilder setFilter:]
+ -[_DASBMHistogramBuilder setLog:]
+ -[_DASBMHistogramBuilder setMinimumSpanConfiguration:]
+ -[_DASBMHistogramBuilder setPublisher:]
+ -[_DASBMHistogramBuilder setSaveSpans:]
+ -[_DASBMHistogramBuilder setTransform:]
+ -[_DASBMHistogramBuilder transform]
+ -[_DASBMMinimumSpanConfiguration .cxx_destruct]
+ -[_DASBMMinimumSpanConfiguration aggregationKeyBlock]
+ -[_DASBMMinimumSpanConfiguration copyWithZone:]
+ -[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]
+ -[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]
+ -[_DASBMMinimumSpanConfiguration init]
+ -[_DASBMMinimumSpanConfiguration log]
+ -[_DASBMMinimumSpanConfiguration minimumSpanDuration]
+ -[_DASBMMinimumSpanConfiguration publisherWithSpansMeetingMinimumDuration:]
+ -[_DASBMMinimumSpanConfiguration publisherWithSpansMeetingMinimumDuration:].cold.1
+ -[_DASBMMinimumSpanConfiguration setAggregationKeyBlock:]
+ -[_DASBMMinimumSpanConfiguration setLog:]
+ -[_DASBMMinimumSpanConfiguration setMinimumSpanDuration:]
+ -[_DASBMMinimumSpanConfiguration setSpanMarkerBlock:]
+ -[_DASBMMinimumSpanConfiguration spanMarkerBlock]
+ -[_DASHistogram .cxx_destruct]
+ -[_DASHistogram countsDictionary]
+ -[_DASHistogram counts]
+ -[_DASHistogram initWithEvents:]
+ -[_DASScheduler activityCanceledWithReason:expirationReason:]
+ -[_DASScheduler clientFailedtoExpireTaskWithIdentifier:]
+ -[_DASScheduler handleClientFailedtoExpireTaskWithIdentifier:completionHandler:]
+ -[_DASSystemContext allowDiscretionaryWorkForBackgroundTask:withParameters:].cold.1
+ -[_DASSystemContext allowDiscretionaryWorkForUtilityTask:withParameters:].cold.1
+ -[_DASWidgetRefreshScheduler lastWidgetViewCache]
+ -[_DASWidgetRefreshScheduler lastWidgetViewLock]
+ -[_DASWidgetRefreshScheduler sanitizeWidgetViews:]
+ -[_DASWidgetRefreshScheduler setLastWidgetViewCache:]
+ -[_DASWidgetRefreshScheduler setLastWidgetViewLock:]
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table196
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table247
+ GCC_except_table252
+ GCC_except_table255
+ GCC_except_table260
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table278
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table287
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table42
+ GCC_except_table51
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table61
+ GCC_except_table68
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table85
+ GCC_except_table94
+ GCC_except_table97
+ OBJC_IVAR_$__DASActivity._runWhenAppLaunchUnlikely
+ OBJC_IVAR_$__DASBMHistogramBuilder._filter
+ OBJC_IVAR_$__DASBMHistogramBuilder._log
+ OBJC_IVAR_$__DASBMHistogramBuilder._minimumSpanConfiguration
+ OBJC_IVAR_$__DASBMHistogramBuilder._publisher
+ OBJC_IVAR_$__DASBMHistogramBuilder._saveSpans
+ OBJC_IVAR_$__DASBMHistogramBuilder._transform
+ OBJC_IVAR_$__DASBMMinimumSpanConfiguration._aggregationKeyBlock
+ OBJC_IVAR_$__DASBMMinimumSpanConfiguration._log
+ OBJC_IVAR_$__DASBMMinimumSpanConfiguration._minimumSpanDuration
+ OBJC_IVAR_$__DASBMMinimumSpanConfiguration._spanMarkerBlock
+ OBJC_IVAR_$__DASHistogram._counts
+ OBJC_IVAR_$__DASHistogram._countsDictionary
+ OBJC_IVAR_$__DASWidgetRefreshScheduler._lastWidgetViewCache
+ OBJC_IVAR_$__DASWidgetRefreshScheduler._lastWidgetViewLock
+ _OBJC_CLASS_$_BPSSequence
+ _OBJC_CLASS_$_BPSTuple
+ _OBJC_CLASS_$__DASBMHistogramBuilder
+ _OBJC_CLASS_$__DASBMMinimumSpanConfiguration
+ _OBJC_CLASS_$__DASHistogram
+ _OBJC_METACLASS_$__DASBMHistogramBuilder
+ _OBJC_METACLASS_$__DASBMMinimumSpanConfiguration
+ _OBJC_METACLASS_$__DASHistogram
+ __138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.318
+ __138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.318.cold.1
+ __188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.337
+ __188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.337.cold.1
+ __25-[_DASScheduler inspect:]_block_invoke.346
+ __25-[_DASScheduler policies]_block_invoke.354
+ __27-[_DASScheduler allBudgets]_block_invoke.349
+ __27-[_DASScheduler clasStatus]_block_invoke.355
+ __27-[_DASScheduler statistics]_block_invoke.341
+ __31-[_DASScheduler runActivities:]_block_invoke.377
+ __33-[_DASScheduler deferActivities:]_block_invoke.327
+ __33-[_DASScheduler getRuntimeLimit:]_block_invoke.414
+ __33-[_DASScheduler getRuntimeLimit:]_block_invoke.414.cold.1
+ __34-[_DASScheduler evaluatePolicies:]_block_invoke.356
+ __35-[_DASBMHistogramBuilder histogram]_block_invoke.75
+ __35-[_DASBMHistogramBuilder histogram]_block_invoke_2.cold.1
+ __35-[_DASScheduler currentPredictions]_block_invoke.337
+ __35-[_DASScheduler submitTaskRequest:]_block_invoke.382
+ __35-[_DASScheduler updateOngoingTask:]_block_invoke.390
+ __35-[_DASScheduler updateOngoingTask:]_block_invoke.390.cold.1
+ __36-[_DASScheduler submittedActivities]_block_invoke.331
+ __37-[_DASScheduler completeTaskRequest:]_block_invoke.389
+ __37-[_DASScheduler completeTaskRequest:]_block_invoke.389.cold.1
+ __37-[_DASScheduler pauseWithParameters:]_block_invoke.372
+ __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.388
+ __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.388.cold.1
+ __40-[_DASScheduler getConditionsPenalties:]_block_invoke.421
+ __40-[_DASScheduler getConditionsPenalties:]_block_invoke.421.cold.1
+ __41-[_DASScheduler addPauseExceptParameter:]_block_invoke.373
+ __42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.350
+ __42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.428
+ __42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.428.cold.1
+ __42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.428.cold.2
+ __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.293
+ __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.294
+ __42-[_DASScheduler runProceedableActivities:]_block_invoke.362
+ __43-[_DASScheduler activityContainsOverrides:]_block_invoke.364
+ __46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.427
+ __46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.427.cold.1
+ __46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.427.cold.2
+ __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.321
+ __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.321.cold.1
+ __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.371
+ __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.371.cold.1
+ __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.413
+ __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.413.cold.1
+ __47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.347
+ __47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.374
+ __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.391
+ __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.391.cold.1
+ __48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.363
+ __48-[_DASWidgetRefreshScheduler recordWidgetViews:]_block_invoke.279
+ __48-[_DASWidgetRefreshScheduler recordWidgetViews:]_block_invoke.279.cold.1
+ __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.387
+ __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.387.cold.1
+ __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.359
+ __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.359.cold.1
+ __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.395
+ __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.395.cold.1
+ __50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.370
+ __50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.342
+ __50-[_DASWidgetRefreshScheduler sanitizeWidgetViews:]_block_invoke.245
+ __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.365
+ __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.365.cold.1
+ __51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.348
+ __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.410
+ __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.410.cold.1
+ __55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.424
+ __55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.424.cold.1
+ __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.409
+ __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.409.cold.1
+ __57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.417
+ __57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.417.cold.1
+ __58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.422
+ __58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.422.cold.1
+ __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.406
+ __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.406.cold.1
+ __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.411
+ __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.411.cold.1
+ __59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.423
+ __59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.423.cold.1
+ __59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.420
+ __59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.420.cold.1
+ __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.412
+ __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.412.cold.1
+ __61-[_DASScheduler getPendingTaskRequestsWithCompletionHandler:]_block_invoke.384
+ __65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.392
+ __66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.429
+ __66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.429.cold.1
+ __66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.429.cold.2
+ __73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke.11
+ __73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke.15
+ __73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke.cold.1
+ __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.393
+ __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.393.cold.1
+ __75-[_DASBMMinimumSpanConfiguration publisherWithSpansMeetingMinimumDuration:]_block_invoke.6
+ __75-[_DASBMMinimumSpanConfiguration publisherWithSpansMeetingMinimumDuration:]_block_invoke.cold.1
+ __78-[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]_block_invoke.19
+ __78-[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]_block_invoke.20
+ __78-[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]_block_invoke.cold.1
+ __80-[_DASScheduler handleClientFailedtoExpireTaskWithIdentifier:completionHandler:]_block_invoke.cold.1
+ __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.396
+ __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.396.cold.1
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSDate_$__DASAdditions
+ __OBJC_$_CLASS_METHODS__DASBMHistogramBuilder
+ __OBJC_$_CLASS_METHODS__DASBMMinimumSpanConfiguration
+ __OBJC_$_INSTANCE_METHODS__DASBMHistogramBuilder
+ __OBJC_$_INSTANCE_METHODS__DASBMMinimumSpanConfiguration
+ __OBJC_$_INSTANCE_METHODS__DASHistogram
+ __OBJC_$_INSTANCE_VARIABLES__DASBMHistogramBuilder
+ __OBJC_$_INSTANCE_VARIABLES__DASBMMinimumSpanConfiguration
+ __OBJC_$_INSTANCE_VARIABLES__DASHistogram
+ __OBJC_$_PROP_LIST__DASBMHistogramBuilder
+ __OBJC_$_PROP_LIST__DASBMMinimumSpanConfiguration
+ __OBJC_$_PROP_LIST__DASHistogram
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__DASHistogramBuilder
+ __OBJC_$_PROTOCOL_METHOD_TYPES__DASHistogramBuilder
+ __OBJC_CLASS_PROTOCOLS_$__DASBMHistogramBuilder
+ __OBJC_CLASS_PROTOCOLS_$__DASBMMinimumSpanConfiguration
+ __OBJC_CLASS_RO_$__DASBMHistogramBuilder
+ __OBJC_CLASS_RO_$__DASBMMinimumSpanConfiguration
+ __OBJC_CLASS_RO_$__DASHistogram
+ __OBJC_LABEL_PROTOCOL_$__DASHistogramBuilder
+ __OBJC_METACLASS_RO_$__DASBMHistogramBuilder
+ __OBJC_METACLASS_RO_$__DASBMMinimumSpanConfiguration
+ __OBJC_METACLASS_RO_$__DASHistogram
+ __OBJC_PROTOCOL_$__DASHistogramBuilder
+ ___35-[_DASBMHistogramBuilder histogram]_block_invoke
+ ___35-[_DASBMHistogramBuilder histogram]_block_invoke_2
+ ___50-[_DASWidgetRefreshScheduler sanitizeWidgetViews:]_block_invoke
+ ___66-[_DASBMHistogramBuilder histogramOnResponseQueue:withCompletion:]_block_invoke
+ ___73-[_DASBMMinimumSpanConfiguration deriveSpansWithMinimumDurationOnStream:]_block_invoke
+ ___75-[_DASBMMinimumSpanConfiguration publisherWithSpansMeetingMinimumDuration:]_block_invoke
+ ___78-[_DASBMMinimumSpanConfiguration deriveSpanTuplesWithMinimumDurationOnStream:]_block_invoke
+ ___80-[_DASScheduler handleClientFailedtoExpireTaskWithIdentifier:completionHandler:]_block_invoke
+ ___block_descriptor_32_e22_B16?0"BMStoreEvent"8l
+ ___block_descriptor_32_e31_q24?0"BPSTuple"8"BPSTuple"16l
+ ___block_descriptor_32_e39_q24?0"BMStoreEvent"8"BMStoreEvent"16l
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8l
+ ___block_descriptor_40_e8_32s_e18_B16?0"BPSTuple"8l
+ ___block_descriptor_40_e8_32s_e23_v16?0"BPSCompletion"8l
+ ___block_descriptor_40_e8_32s_e41_v32?0"NSString"8"NSMutableArray"16^B24l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e23_v16?0"BPSCompletion"8l
+ ___block_descriptor_48_e8_32s40s_e32_"BPSTuple"16?0"BMStoreEvent"8l
+ __block_literal_global.23
+ __block_literal_global.244
+ __block_literal_global.379
+ __block_literal_global.70
+ _objc_msgSend$activityCanceledWithReason:expirationReason:
+ _objc_msgSend$aggregationKeyBlock
+ _objc_msgSend$clientFailedtoExpireTaskWithIdentifier:
+ _objc_msgSend$collect
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$configurationWithMinimumDuration:aggregationKey:spanMarker:
+ _objc_msgSend$dateFromAbsoluteTime:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$deriveSpansWithMinimumDurationOnStream:
+ _objc_msgSend$error
+ _objc_msgSend$eventBody
+ _objc_msgSend$filterWithIsIncluded:
+ _objc_msgSend$first
+ _objc_msgSend$handleClientFailedtoExpireTaskWithIdentifier:completionHandler:
+ _objc_msgSend$histogram
+ _objc_msgSend$initWithEvents:
+ _objc_msgSend$initWithFirst:second:
+ _objc_msgSend$initWithPublisher:saveSpans:
+ _objc_msgSend$initWithSequence:
+ _objc_msgSend$mapWithTransform:
+ _objc_msgSend$maximumRuntime
+ _objc_msgSend$minimumSpanDuration
+ _objc_msgSend$performSelector:
+ _objc_msgSend$publisher
+ _objc_msgSend$publisherWithSpansMeetingMinimumDuration:
+ _objc_msgSend$runWhenAppLaunchUnlikely
+ _objc_msgSend$sanitizeWidgetViews:
+ _objc_msgSend$second
+ _objc_msgSend$setAggregationKeyBlock:
+ _objc_msgSend$setMinimumSpanDuration:
+ _objc_msgSend$setSpanMarkerBlock:
+ _objc_msgSend$sinkWithCompletion:receiveInput:
+ _objc_msgSend$sortUsingComparator:
+ _objc_msgSend$spanMarkerBlock
+ _objc_msgSend$state
+ _objc_msgSend$timestamp
+ _objc_msgSend$weekday
+ _objc_opt_respondsToSelector
- -[_DASActivity relevancy]
- -[_DASActivity setRelevancy:]
- GCC_except_table101
- GCC_except_table110
- GCC_except_table113
- GCC_except_table116
- GCC_except_table119
- GCC_except_table122
- GCC_except_table125
- GCC_except_table128
- GCC_except_table134
- GCC_except_table146
- GCC_except_table149
- GCC_except_table154
- GCC_except_table157
- GCC_except_table167
- GCC_except_table194
- GCC_except_table226
- GCC_except_table227
- GCC_except_table232
- GCC_except_table235
- GCC_except_table243
- GCC_except_table248
- GCC_except_table251
- GCC_except_table256
- GCC_except_table259
- GCC_except_table262
- GCC_except_table265
- GCC_except_table268
- GCC_except_table271
- GCC_except_table274
- GCC_except_table277
- GCC_except_table280
- GCC_except_table283
- GCC_except_table317
- GCC_except_table318
- GCC_except_table40
- GCC_except_table49
- GCC_except_table53
- GCC_except_table56
- GCC_except_table59
- GCC_except_table62
- GCC_except_table74
- GCC_except_table77
- GCC_except_table80
- GCC_except_table83
- GCC_except_table92
- GCC_except_table95
- GCC_except_table98
- OBJC_IVAR_$__DASActivity._relevancy
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- __138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.311
- __138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.311.cold.1
- __188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.330
- __188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.330.cold.1
- __25-[_DASScheduler inspect:]_block_invoke.341
- __25-[_DASScheduler policies]_block_invoke.349
- __27-[_DASScheduler allBudgets]_block_invoke.344
- __27-[_DASScheduler clasStatus]_block_invoke.350
- __27-[_DASScheduler statistics]_block_invoke.336
- __31-[_DASScheduler runActivities:]_block_invoke.372
- __33-[_DASScheduler deferActivities:]_block_invoke.322
- __33-[_DASScheduler getRuntimeLimit:]_block_invoke.409
- __33-[_DASScheduler getRuntimeLimit:]_block_invoke.409.cold.1
- __34-[_DASScheduler evaluatePolicies:]_block_invoke.351
- __35-[_DASScheduler currentPredictions]_block_invoke.332
- __35-[_DASScheduler submitTaskRequest:]_block_invoke.377
- __35-[_DASScheduler updateOngoingTask:]_block_invoke.385
- __35-[_DASScheduler updateOngoingTask:]_block_invoke.385.cold.1
- __36-[_DASScheduler submittedActivities]_block_invoke.326
- __37-[_DASScheduler completeTaskRequest:]_block_invoke.384
- __37-[_DASScheduler completeTaskRequest:]_block_invoke.384.cold.1
- __37-[_DASScheduler pauseWithParameters:]_block_invoke.367
- __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.383
- __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.383.cold.1
- __40-[_DASScheduler getConditionsPenalties:]_block_invoke.416
- __40-[_DASScheduler getConditionsPenalties:]_block_invoke.416.cold.1
- __41-[_DASScheduler addPauseExceptParameter:]_block_invoke.368
- __42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.345
- __42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.423
- __42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.423.cold.1
- __42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.423.cold.2
- __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.288
- __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.289
- __42-[_DASScheduler runProceedableActivities:]_block_invoke.357
- __43-[_DASScheduler activityContainsOverrides:]_block_invoke.359
- __46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.422
- __46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.422.cold.1
- __46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.422.cold.2
- __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.316
- __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.316.cold.1
- __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.366
- __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.366.cold.1
- __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.408
- __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.408.cold.1
- __47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.342
- __47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.369
- __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.386
- __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.386.cold.1
- __48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.358
- __48-[_DASWidgetRefreshScheduler recordWidgetViews:]_block_invoke.272
- __48-[_DASWidgetRefreshScheduler recordWidgetViews:]_block_invoke.272.cold.1
- __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.382
- __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.382.cold.1
- __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.354
- __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.354.cold.1
- __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.390
- __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.390.cold.1
- __50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.365
- __50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.337
- __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.360
- __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.360.cold.1
- __51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.343
- __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.405
- __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.405.cold.1
- __55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.419
- __55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.419.cold.1
- __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.404
- __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.404.cold.1
- __57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.412
- __57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.412.cold.1
- __58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.417
- __58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.417.cold.1
- __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.401
- __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.401.cold.1
- __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.406
- __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.406.cold.1
- __59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.418
- __59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.418.cold.1
- __59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.415
- __59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.415.cold.1
- __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.407
- __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.407.cold.1
- __61-[_DASScheduler getPendingTaskRequestsWithCompletionHandler:]_block_invoke.379
- __65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.387
- __66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.424
- __66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.424.cold.1
- __66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.424.cold.2
- __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.388
- __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.388.cold.1
- __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.391
- __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.391.cold.1
- __block_literal_global.374
- _objc_msgSend$relevancy
CStrings:
+ ", Maximum Runtime: %ld"
+ ", Run When App Launch Unlikely: %d"
+ "@\"BPSPublisher\""
+ "@\"BPSTuple\"16@?0@\"BMStoreEvent\"8"
+ "@\"_DASBMMinimumSpanConfiguration\""
+ "@\"_DASHistogram\"16@0:8"
+ "@40@0:8d16@?24@?32"
+ "B16@?0@\"BMStoreEvent\"8"
+ "B16@?0@\"BPSTuple\"8"
+ "BiomeHistogramBuilder"
+ "Coalescing view for %@ at %@"
+ "Coalescing view for %@ at %@ (Cache)"
+ "Failed to open sink for %@: %@"
+ "MinimumSpanConfiguration"
+ "T@\"BPSPublisher\",&,N,V_publisher"
+ "T@\"NSCountedSet\",R,C,N,V_counts"
+ "T@\"NSDictionary\",R,C,N,V_countsDictionary"
+ "T@\"NSMutableDictionary\",&,N,V_lastWidgetViewCache"
+ "T@\"_DASBMMinimumSpanConfiguration\",C,N,V_minimumSpanConfiguration"
+ "T@?,C,N,V_aggregationKeyBlock"
+ "T@?,C,N,V_filter"
+ "T@?,C,N,V_spanMarkerBlock"
+ "T@?,C,N,V_transform"
+ "TB,N,V_runWhenAppLaunchUnlikely"
+ "TB,N,V_saveSpans"
+ "Td,N,V_minimumSpanDuration"
+ "Tried to derive spans with an invalid configuration; bailing"
+ "T{os_unfair_lock_s=I},N,V_lastWidgetViewLock"
+ "_DASBMHistogramBuilder"
+ "_DASBMMinimumSpanConfiguration"
+ "_DASHistogram"
+ "_DASHistogramBuilder"
+ "_aggregationKeyBlock"
+ "_counts"
+ "_countsDictionary"
+ "_filter"
+ "_lastWidgetViewCache"
+ "_lastWidgetViewLock"
+ "_minimumSpanConfiguration"
+ "_minimumSpanDuration"
+ "_publisher"
+ "_runWhenAppLaunchUnlikely"
+ "_saveSpans"
+ "_spanMarkerBlock"
+ "_transform"
+ "activityCanceledWithReason:expirationReason:"
+ "aggregationKeyBlock"
+ "builderWithPublisher:"
+ "builderWithPublisher:saveSpans:"
+ "clientFailedtoExpireTaskWithIdentifier:"
+ "collect"
+ "com.apple.DuetActivityScheduler"
+ "components:fromDate:"
+ "configurationWithMinimumDuration:aggregationKey:spanMarker:"
+ "counts"
+ "countsDictionary"
+ "dateFromAbsoluteTime:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "deriveSpanTuplesWithMinimumDurationOnStream:"
+ "deriveSpansWithMinimumDurationOnStream:"
+ "error"
+ "eventBody"
+ "filter"
+ "filterWithIsIncluded:"
+ "first"
+ "handleClientFailedtoExpireTaskWithIdentifier [taskIdentifier: %@] Failed: %@"
+ "handleClientFailedtoExpireTaskWithIdentifier:completionHandler:"
+ "histogram"
+ "histogramOnResponseQueue:withCompletion:"
+ "initWithEvents:"
+ "initWithFirst:second:"
+ "initWithPublisher:saveSpans:"
+ "initWithSequence:"
+ "isAfter:"
+ "isBefore:"
+ "isSameDayOfWeekAs:withCalendar:"
+ "lastWidgetViewCache"
+ "lastWidgetViewLock"
+ "mapWithTransform:"
+ "minimumSpanConfiguration"
+ "minimumSpanDuration"
+ "nil key returned for %@"
+ "publisher"
+ "publisherWithSpansMeetingMinimumDuration:"
+ "q24@?0@\"BMStoreEvent\"8@\"BMStoreEvent\"16"
+ "q24@?0@\"BPSTuple\"8@\"BPSTuple\"16"
+ "runWhenAppLaunchUnkely"
+ "runWhenAppLaunchUnlikely"
+ "sanitizeWidgetViews:"
+ "saveSpans"
+ "second"
+ "setAggregationKeyBlock:"
+ "setFilter:"
+ "setLastWidgetViewCache:"
+ "setLastWidgetViewLock:"
+ "setMinimumSpanConfiguration:"
+ "setMinimumSpanDuration:"
+ "setPublisher:"
+ "setRunWhenAppLaunchUnlikely:"
+ "setSaveSpans:"
+ "setSpanMarkerBlock:"
+ "setTransform:"
+ "sinkWithCompletion:receiveInput:"
+ "sortUsingComparator:"
+ "spanMarkerBlock"
+ "starting"
+ "state"
+ "timestamp"
+ "transform"
+ "v16@?0@\"BPSCompletion\"8"
+ "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"_DASHistogram\">24"
+ "v32@0:8@\"_DASActivity\"16q24"
+ "v32@0:8@16q24"
+ "v32@?0@\"NSString\"8@\"NSMutableArray\"16^B24"
+ "weekday"
- "Tq,N,V_relevancy"
- "_relevancy"
- "relevancy"
- "setRelevancy:"

```
