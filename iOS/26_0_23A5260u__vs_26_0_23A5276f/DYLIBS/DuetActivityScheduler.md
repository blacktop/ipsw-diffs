## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-2109.0.44.502.1
-  __TEXT.__text: 0x34d50
+2109.0.61.502.1
+  __TEXT.__text: 0x34bc0
   __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__objc_methlist: 0x4138
+  __TEXT.__objc_methlist: 0x4108
   __TEXT.__const: 0x158
   __TEXT.__gcc_except_tab: 0x14e4
-  __TEXT.__cstring: 0x25eb
+  __TEXT.__cstring: 0x2600
   __TEXT.__oslogstring: 0x2ec0
   __TEXT.__unwind_info: 0xf50
   __TEXT.__objc_classname: 0x727
-  __TEXT.__objc_methname: 0xa29d
-  __TEXT.__objc_methtype: 0x1ae0
-  __TEXT.__objc_stubs: 0x5b00
+  __TEXT.__objc_methname: 0xa298
+  __TEXT.__objc_methtype: 0x1ae3
+  __TEXT.__objc_stubs: 0x5a60
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__const: 0xee0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c0
+  __DATA_CONST.__objc_selrefs: 0x24b0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x110
   __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x3660
-  __AUTH_CONST.__objc_const: 0x7398
+  __AUTH_CONST.__cfstring: 0x3680
+  __AUTH_CONST.__objc_const: 0x73a8
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x424
+  __DATA.__objc_ivar: 0x428
   __DATA.__data: 0xdf0
   __DATA.__bss: 0x60
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67AD333F-CCE2-3364-9BEA-6598ECB94F0C
+  UUID: E2CE9F2D-CA4D-3753-B182-DED28ADFBF24
   Functions: 1473
-  Symbols:   5150
-  CStrings:  3204
+  Symbols:   5146
+  CStrings:  3206
 
Symbols:
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:isForegroundAppProxy:]
+ -[_DASContinuedProcessingWrapper isForegroundAppProxy]
+ -[_DASContinuedProcessingWrapper setIsForegroundAppProxy:]
+ GCC_except_table102
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table136
+ GCC_except_table139
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table157
+ GCC_except_table186
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table239
+ GCC_except_table242
+ GCC_except_table245
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table254
+ GCC_except_table257
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
+ GCC_except_table290
+ GCC_except_table293
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table93
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._isForegroundAppProxy
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.403
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.403.cold.1
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.404
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.404.cold.1
+ ___25-[_DASScheduler inspect:]_block_invoke.353
+ ___25-[_DASScheduler policies]_block_invoke.359
+ ___27-[_DASScheduler allBudgets]_block_invoke.356
+ ___27-[_DASScheduler statistics]_block_invoke.350
+ ___31-[_DASScheduler runActivities:]_block_invoke.371
+ ___33-[_DASScheduler deferActivities:]_block_invoke.342
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.408
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.408.cold.1
+ ___34-[_DASScheduler evaluatePolicies:]_block_invoke.360
+ ___35-[_DASScheduler currentPredictions]_block_invoke.347
+ ___35-[_DASScheduler submitTaskRequest:]_block_invoke.376
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.386
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.386.cold.1
+ ___36-[_DASScheduler submittedActivities]_block_invoke.344
+ ___37-[_DASScheduler pauseWithParameters:]_block_invoke.368
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.378
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.378.cold.1
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.411
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.411.cold.1
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.412
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.412.cold.1
+ ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.369
+ ___41-[_DASScheduler delayedRunningActivities]_block_invoke.346
+ ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.357
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.420
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.420.cold.1
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.420.cold.2
+ ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.318
+ ___42-[_DASScheduler runProceedableActivities:]_block_invoke.362
+ ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.364
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.419
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.419.cold.1
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.419.cold.2
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.422
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.422.cold.1
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.422.cold.2
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.340
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.340.cold.1
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.367
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.367.cold.1
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.407
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.407.cold.1
+ ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.354
+ ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.370
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.387
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.387.cold.1
+ ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.363
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.377
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.377.cold.1
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.385
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.385.cold.1
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.361
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.361.cold.1
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.392
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.392.cold.1
+ ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.366
+ ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.351
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.365
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.365.cold.1
+ ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.355
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.402
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.402.cold.1
+ ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.388
+ ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.416
+ ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.416.cold.1
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.401
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.401.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.423
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.423.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.423.cold.2
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.349
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.409
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.409.cold.1
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.417
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.417.cold.1
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.413
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.413.cold.1
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.405
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.405.cold.1
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.414
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.414.cold.1
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.410
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.410.cold.1
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.406
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.406.cold.1
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.415
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.415.cold.1
+ ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.390
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.400
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.400.cold.1
+ ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.421
+ ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.421.cold.1
+ ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.421.cold.2
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.391
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.391.cold.1
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.418
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.418.cold.1
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.393
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.393.cold.1
+ ___block_literal_global.373
+ _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:isForegroundAppProxy:
- -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:]
- -[_DASScheduler activityRunStatistics]
- -[_DASScheduler scoresForActivityWithName:]
- GCC_except_table104
- GCC_except_table108
- GCC_except_table111
- GCC_except_table114
- GCC_except_table117
- GCC_except_table120
- GCC_except_table126
- GCC_except_table138
- GCC_except_table141
- GCC_except_table147
- GCC_except_table148
- GCC_except_table159
- GCC_except_table188
- GCC_except_table218
- GCC_except_table219
- GCC_except_table222
- GCC_except_table225
- GCC_except_table228
- GCC_except_table231
- GCC_except_table241
- GCC_except_table244
- GCC_except_table247
- GCC_except_table250
- GCC_except_table253
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
- GCC_except_table286
- GCC_except_table289
- GCC_except_table292
- GCC_except_table295
- GCC_except_table330
- GCC_except_table331
- GCC_except_table67
- GCC_except_table70
- GCC_except_table73
- GCC_except_table76
- GCC_except_table79
- GCC_except_table86
- GCC_except_table89
- GCC_except_table92
- GCC_except_table95
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.405
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.405.cold.1
- ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.406
- ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.406.cold.1
- ___25-[_DASScheduler inspect:]_block_invoke.355
- ___25-[_DASScheduler policies]_block_invoke.361
- ___27-[_DASScheduler allBudgets]_block_invoke.358
- ___27-[_DASScheduler statistics]_block_invoke.352
- ___31-[_DASScheduler runActivities:]_block_invoke.373
- ___33-[_DASScheduler deferActivities:]_block_invoke.344
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.410
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.410.cold.1
- ___34-[_DASScheduler evaluatePolicies:]_block_invoke.362
- ___35-[_DASScheduler currentPredictions]_block_invoke.349
- ___35-[_DASScheduler submitTaskRequest:]_block_invoke.378
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.388
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.388.cold.1
- ___36-[_DASScheduler submittedActivities]_block_invoke.346
- ___37-[_DASScheduler pauseWithParameters:]_block_invoke.370
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.380
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.380.cold.1
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.413
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.413.cold.1
- ___40-[_DASScheduler getContentionPenalties:]_block_invoke.414
- ___40-[_DASScheduler getContentionPenalties:]_block_invoke.414.cold.1
- ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.371
- ___41-[_DASScheduler delayedRunningActivities]_block_invoke.348
- ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.359
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.422
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.422.cold.1
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.422.cold.2
- ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.319
- ___42-[_DASScheduler runProceedableActivities:]_block_invoke.364
- ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.366
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.421
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.421.cold.1
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.421.cold.2
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.424
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.424.cold.1
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.424.cold.2
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.342
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.342.cold.1
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.369
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.369.cold.1
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.409
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.409.cold.1
- ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.356
- ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.372
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.389
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.389.cold.1
- ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.365
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.379
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.379.cold.1
- ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.387
- ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.387.cold.1
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.363
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.363.cold.1
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.394
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.394.cold.1
- ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.368
- ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.353
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.367
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.367.cold.1
- ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.357
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.404
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.404.cold.1
- ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.390
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.418
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.418.cold.1
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.403
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.403.cold.1
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.425
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.425.cold.1
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.425.cold.2
- ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.351
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.411
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.411.cold.1
- ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.419
- ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.419.cold.1
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.415
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.415.cold.1
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.407
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.407.cold.1
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.416
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.416.cold.1
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.412
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.412.cold.1
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.408
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.408.cold.1
- ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.417
- ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.417.cold.1
- ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.392
- ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.402
- ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.402.cold.1
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.423
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.423.cold.1
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.423.cold.2
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.393
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.393.cold.1
- ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.420
- ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.420.cold.1
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.395
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.395.cold.1
- ___block_literal_global.375
- _objc_msgSend$iconBundleIdentifier
- _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:
- _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:
- _objc_msgSend$initWithTitle:subtitle:resources:submissionStrategy:
- _objc_msgSend$resources
- _objc_msgSend$submissionStrategy
CStrings:
+ "@60@0:8@16@24@32q40q48B56"
+ "TB,N,V_isForegroundAppProxy"
+ "_isForegroundAppProxy"
+ "initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:isForegroundAppProxy:"
+ "isForegroundAppProxy"
+ "setIsForegroundAppProxy:"
- "@56@0:8@16@24@32q40q48"
- "activityRunStatistics"
- "activityRunStatisticsWithHandler:"
- "initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:"
- "scoresForActivityWithName:"
- "scoresForActivityWithName:withHandler:"

```
