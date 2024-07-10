## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/Versions/A/DuetActivityScheduler`

```diff

-1781.0.0.0.5
-  __TEXT.__text: 0x2dd5c
+1770.0.0.0.6
+  __TEXT.__text: 0x2d920
   __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x2a54
+  __TEXT.__objc_methlist: 0x2a4c
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x1e88
-  __TEXT.__oslogstring: 0x2262
-  __TEXT.__gcc_except_tab: 0xff0
-  __TEXT.__unwind_info: 0xc38
+  __TEXT.__cstring: 0x1e2a
+  __TEXT.__oslogstring: 0x21b3
+  __TEXT.__gcc_except_tab: 0xfc4
+  __TEXT.__unwind_info: 0xc30
   __TEXT.__objc_classname: 0x66a
-  __TEXT.__objc_methname: 0x7ba8
-  __TEXT.__objc_methtype: 0x1447
-  __TEXT.__objc_stubs: 0x46e0
+  __TEXT.__objc_methname: 0x7b3e
+  __TEXT.__objc_methtype: 0x13d3
+  __TEXT.__objc_stubs: 0x46c0
   __DATA_CONST.__got: 0x248
   __DATA_CONST.__const: 0x390
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb8
+  __DATA_CONST.__objc_selrefs: 0x1ca8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xc8
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0x2f40
-  __AUTH_CONST.__objc_const: 0x7570
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__cfstring: 0x2f00
+  __AUTH_CONST.__objc_const: 0x7530
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x500
   __DATA.__objc_ivar: 0x334
-  __DATA.__data: 0xd80
+  __DATA.__data: 0xd68
   __DATA.__bss: 0xa8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x500

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/Versions/A/CoreDuetContext
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1187
-  Symbols:   2933
-  CStrings:  416
+  Functions: 1181
+  Symbols:   2922
+  CStrings:  414
 
Symbols:
+ GCC_except_table305
+ GCC_except_table306
+ __25-[_DASScheduler inspect:]_block_invoke.334
+ __25-[_DASScheduler policies]_block_invoke.342
+ __27-[_DASScheduler allBudgets]_block_invoke.337
+ __27-[_DASScheduler clasStatus]_block_invoke.343
+ __27-[_DASScheduler statistics]_block_invoke.329
+ __31-[_DASScheduler runActivities:]_block_invoke.365
+ __33-[_DASScheduler deferActivities:]_block_invoke.315
+ __33-[_DASScheduler getRuntimeLimit:]_block_invoke.402
+ __33-[_DASScheduler getRuntimeLimit:]_block_invoke.402.cold.1
+ __34-[_DASScheduler evaluatePolicies:]_block_invoke.344
+ __35-[_DASScheduler currentPredictions]_block_invoke.325
+ __35-[_DASScheduler submitTaskRequest:]_block_invoke.370
+ __35-[_DASScheduler updateOngoingTask:]_block_invoke.378
+ __35-[_DASScheduler updateOngoingTask:]_block_invoke.378.cold.1
+ __36-[_DASScheduler submittedActivities]_block_invoke.319
+ __37-[_DASScheduler completeTaskRequest:]_block_invoke.377
+ __37-[_DASScheduler completeTaskRequest:]_block_invoke.377.cold.1
+ __37-[_DASScheduler pauseWithParameters:]_block_invoke.360
+ __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.376
+ __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.376.cold.1
+ __40-[_DASScheduler getConditionsPenalties:]_block_invoke.409
+ __40-[_DASScheduler getConditionsPenalties:]_block_invoke.409.cold.1
+ __41-[_DASScheduler addPauseExceptParameter:]_block_invoke.361
+ __42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.338
+ __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.281
+ __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.282
+ __42-[_DASScheduler runProceedableActivities:]_block_invoke.350
+ __43-[_DASScheduler activityContainsOverrides:]_block_invoke.352
+ __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.309
+ __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.309.cold.1
+ __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.359
+ __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.359.cold.1
+ __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.401
+ __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.401.cold.1
+ __47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.335
+ __47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.362
+ __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.379
+ __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.379.cold.1
+ __48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.351
+ __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.375
+ __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.375.cold.1
+ __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.347
+ __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.347.cold.1
+ __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.383
+ __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.383.cold.1
+ __50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.358
+ __50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.330
+ __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.353
+ __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.353.cold.1
+ __51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.336
+ __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.398
+ __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.398.cold.1
+ __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.397
+ __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.397.cold.1
+ __56-[_DASScheduler getElapsedRuntimes:timeFilter:filepath:]_block_invoke.405
+ __56-[_DASScheduler getElapsedRuntimes:timeFilter:filepath:]_block_invoke.405.cold.1
+ __57-[_DASScheduler getFeatureTimelines:timeFilter:filepath:]_block_invoke.410
+ __57-[_DASScheduler getFeatureTimelines:timeFilter:filepath:]_block_invoke.410.cold.1
+ __58-[_DASScheduler getActivityTimelines:timeFilter:filepath:]_block_invoke.411
+ __58-[_DASScheduler getActivityTimelines:timeFilter:filepath:]_block_invoke.411.cold.1
+ __58-[_DASScheduler getEstimatedRuntimes:timeFilter:filepath:]_block_invoke.408
+ __58-[_DASScheduler getEstimatedRuntimes:timeFilter:filepath:]_block_invoke.408.cold.1
+ __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.394
+ __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.394.cold.1
+ __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.399
+ __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.399.cold.1
+ __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.400
+ __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.400.cold.1
+ __61-[_DASScheduler getPendingTaskRequestsWithCompletionHandler:]_block_invoke.372
+ __65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.380
+ __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.381
+ __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.381.cold.1
+ __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.384
+ __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.384.cold.1
+ __block_literal_global.32
+ __block_literal_global.367
- -[_DASScheduler getEstimatedMADCompletionTimes:endDate:filepath:]
- GCC_except_table274
- GCC_except_table308
- GCC_except_table309
- __25-[_DASScheduler inspect:]_block_invoke.336
- __25-[_DASScheduler policies]_block_invoke.344
- __27-[_DASScheduler allBudgets]_block_invoke.339
- __27-[_DASScheduler clasStatus]_block_invoke.345
- __27-[_DASScheduler statistics]_block_invoke.331
- __31-[_DASScheduler runActivities:]_block_invoke.367
- __33-[_DASScheduler deferActivities:]_block_invoke.317
- __33-[_DASScheduler getRuntimeLimit:]_block_invoke.404
- __33-[_DASScheduler getRuntimeLimit:]_block_invoke.404.cold.1
- __34-[_DASScheduler evaluatePolicies:]_block_invoke.346
- __35-[_DASScheduler currentPredictions]_block_invoke.327
- __35-[_DASScheduler submitTaskRequest:]_block_invoke.372
- __35-[_DASScheduler updateOngoingTask:]_block_invoke.380
- __35-[_DASScheduler updateOngoingTask:]_block_invoke.380.cold.1
- __36-[_DASScheduler submittedActivities]_block_invoke.321
- __37-[_DASScheduler completeTaskRequest:]_block_invoke.379
- __37-[_DASScheduler completeTaskRequest:]_block_invoke.379.cold.1
- __37-[_DASScheduler pauseWithParameters:]_block_invoke.362
- __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.378
- __38-[_DASScheduler cancelAllTaskRequests]_block_invoke.378.cold.1
- __40-[_DASScheduler getConditionsPenalties:]_block_invoke.411
- __40-[_DASScheduler getConditionsPenalties:]_block_invoke.411.cold.1
- __41-[_DASScheduler addPauseExceptParameter:]_block_invoke.363
- __42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.340
- __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.283
- __42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.284
- __42-[_DASScheduler runProceedableActivities:]_block_invoke.352
- __43-[_DASScheduler activityContainsOverrides:]_block_invoke.354
- __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.311
- __46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.311.cold.1
- __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.361
- __46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.361.cold.1
- __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.403
- __47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.403.cold.1
- __47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.337
- __47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.364
- __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.381
- __47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.381.cold.1
- __48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.353
- __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.377
- __49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.377.cold.1
- __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.349
- __49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.349.cold.1
- __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.385
- __50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.385.cold.1
- __50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.360
- __50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.332
- __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.355
- __51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.355.cold.1
- __51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.338
- __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.400
- __54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.400.cold.1
- __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.399
- __55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.399.cold.1
- __56-[_DASScheduler getElapsedRuntimes:timeFilter:filepath:]_block_invoke.407
- __56-[_DASScheduler getElapsedRuntimes:timeFilter:filepath:]_block_invoke.407.cold.1
- __57-[_DASScheduler getFeatureTimelines:timeFilter:filepath:]_block_invoke.412
- __57-[_DASScheduler getFeatureTimelines:timeFilter:filepath:]_block_invoke.412.cold.1
- __58-[_DASScheduler getActivityTimelines:timeFilter:filepath:]_block_invoke.413
- __58-[_DASScheduler getActivityTimelines:timeFilter:filepath:]_block_invoke.413.cold.1
- __58-[_DASScheduler getEstimatedRuntimes:timeFilter:filepath:]_block_invoke.410
- __58-[_DASScheduler getEstimatedRuntimes:timeFilter:filepath:]_block_invoke.410.cold.1
- __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.396
- __58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.396.cold.1
- __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.401
- __59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.401.cold.1
- __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.402
- __60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.402.cold.1
- __61-[_DASScheduler getPendingTaskRequestsWithCompletionHandler:]_block_invoke.374
- __65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.382
- __65-[_DASScheduler getEstimatedMADCompletionTimes:endDate:filepath:]_block_invoke.414
- __65-[_DASScheduler getEstimatedMADCompletionTimes:endDate:filepath:]_block_invoke.414.cold.1
- __65-[_DASScheduler getEstimatedMADCompletionTimes:endDate:filepath:]_block_invoke.414.cold.2
- __65-[_DASScheduler getEstimatedMADCompletionTimes:endDate:filepath:]_block_invoke.cold.1
- __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.383
- __74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.383.cold.1
- __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.386
- __82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.386.cold.1
- ___65-[_DASScheduler getEstimatedMADCompletionTimes:endDate:filepath:]_block_invoke
- __block_literal_global.369
- __block_literal_global.38
- _kDASSystemContextGPWorkloadRunningState
- _kDASSystemContextMCWorkloadRunningState
- _kDASSystemContextNonDASCriticalWorkloadRunning
- _objc_msgSend$getEstimatedMADCompletionTimes:endDate:filepath:handler:
CStrings:
+ "Dependencies && Insufficent File Protection"
+ "com.apple.dasd.featurecodes.plist"
- "Dependencies && Insufficient File Protection"
- "_DASSystemContextNonDASCriticalWorkloadRunning"
- "kDASSystemContextGPWorkloadRunningState"
- "kDASSystemContextMCWorkloadRunningState"

```
