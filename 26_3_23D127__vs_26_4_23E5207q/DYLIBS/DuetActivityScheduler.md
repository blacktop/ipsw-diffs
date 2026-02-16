## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-2109.80.9.0.0
-  __TEXT.__text: 0x357ac
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x4170
+2109.100.198.0.0
+  __TEXT.__text: 0x3b338
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0x4470
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x156c
-  __TEXT.__cstring: 0x2694
-  __TEXT.__oslogstring: 0x2fcb
-  __TEXT.__unwind_info: 0xff0
-  __TEXT.__objc_classname: 0x729
-  __TEXT.__objc_methname: 0xa417
-  __TEXT.__objc_methtype: 0x1ae9
-  __TEXT.__objc_stubs: 0x5ae0
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0xeb8
-  __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x28
+  __TEXT.__gcc_except_tab: 0x159c
+  __TEXT.__cstring: 0x2884
+  __TEXT.__oslogstring: 0x31fa
+  __TEXT.__unwind_info: 0x1338
+  __TEXT.__objc_classname: 0x74c
+  __TEXT.__objc_methname: 0xaa77
+  __TEXT.__objc_methtype: 0x1c29
+  __TEXT.__objc_stubs: 0x5fe0
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0xf38
+  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24f8
+  __DATA_CONST.__objc_selrefs: 0x2688
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xf8
-  __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x398
-  __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x3720
-  __AUTH_CONST.__objc_const: 0x7408
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_arraydata: 0x148
+  __AUTH_CONST.__auth_got: 0x3a8
+  __AUTH_CONST.__const: 0x2c0
+  __AUTH_CONST.__cfstring: 0x3aa0
+  __AUTH_CONST.__objc_const: 0x7778
+  __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x460
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x430
+  __DATA.__objc_ivar: 0x44c
   __DATA.__data: 0xdf0
-  __DATA.__bss: 0x60
+  __DATA.__bss: 0x70
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x780
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__objc_data: 0x7d0
+  __DATA_DIRTY.__bss: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C6F72214-A8A9-3F1A-A5FC-B9329DEDA8F1
-  Functions: 1494
-  Symbols:   5207
-  CStrings:  3236
+  UUID: 4CDBF190-1043-391F-9C70-2D442749AADF
+  Functions: 1579
+  Symbols:   5498
+  CStrings:  3380
 
Symbols:
+ +[NSString(_DASInterning) das_interningStatistics]
+ +[NSString(_DASInterning) das_purgeInterned]
+ +[_DASActivity convertUUIDToUint64:]
+ +[_DASStringInterning sharedInstance]
+ -[NSArray(_DASInterning) das_dedup]
+ -[NSDictionary(_DASInterning) das_dedup]
+ -[NSMutableArray(_DASInterning) das_dedup]
+ -[NSMutableDictionary(_DASInterning) das_dedup]
+ -[NSMutableSet(_DASInterning) das_dedup]
+ -[NSSet(_DASInterning) das_dedup]
+ -[NSString(_DASInterning) das_dedup]
+ -[_DASActivity hashString:]
+ -[_DASActivity immediateRuntimeState]
+ -[_DASActivity onBatteryRuntimeState]
+ -[_DASActivity postInstall]
+ -[_DASActivity reportingName]
+ -[_DASActivity reportingName].cold.1
+ -[_DASActivity reportingServiceName]
+ -[_DASActivity setImmediateRuntimeState:]
+ -[_DASActivity setOnBatteryRuntimeState:]
+ -[_DASActivity setPostInstall:]
+ -[_DASActivity shouldImposeDeviceInactivity]
+ -[_DASContinuedProcessingWrapper executionContext]
+ -[_DASContinuedProcessingWrapper hostAppAuditToken]
+ -[_DASContinuedProcessingWrapper iconUTI]
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:]
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:submissionStrategy:executionContext:hostAppAuditToken:]
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:resources:submissionStrategy:executionContext:hostAppAuditToken:]
+ -[_DASContinuedProcessingWrapper rectifyExecutionContextWithClientProcessHandle:hostAppProcHandle:]
+ -[_DASContinuedProcessingWrapper setExecutionContext:]
+ -[_DASContinuedProcessingWrapper setHostAppAuditToken:]
+ -[_DASContinuedProcessingWrapper setIconUTI:]
+ -[_DASPlistParser isValidSuspensionExemptions:]
+ -[_DASPlistParser suspensionExemptionsForActivity:]
+ -[_DASPlistParser suspensionExemptionsForActivity:].cold.1
+ -[_DASPlistParser suspensionExemptionsForActivity:].cold.2
+ -[_DASPlistParser suspensionThreshold].cold.1
+ -[_DASScheduler activityForActivityName:]
+ -[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]
+ -[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]
+ -[_DASScheduler getRebootEvents:bgsqlData:]
+ -[_DASScheduler getSubmittedSystemTaskRequestsWithCompletionHandler:]
+ -[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]
+ -[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]
+ -[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]
+ -[_DASScheduler inspect:criteria:]
+ -[_DASStringInterning .cxx_destruct]
+ -[_DASStringInterning init]
+ -[_DASStringInterning internString:]
+ -[_DASStringInterning internedStrings]
+ -[_DASStringInterning interns]
+ -[_DASStringInterning lookups]
+ -[_DASStringInterning purge]
+ -[_DASStringInterning setInternedStrings:]
+ -[_DASStringInterning setInterns:]
+ -[_DASStringInterning setLookups:]
+ -[_DASStringInterning statistics]
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table241
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table256
+ GCC_except_table259
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table292
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table348
+ GCC_except_table349
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$__DASStringInterning
+ _OBJC_IVAR_$__DASActivity._immediateRuntimeState
+ _OBJC_IVAR_$__DASActivity._onBatteryRuntimeState
+ _OBJC_IVAR_$__DASActivity._postInstall
+ _OBJC_IVAR_$__DASActivity._requiresDeviceInactivityIsSetByUser
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._executionContext
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._hostAppAuditToken
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._iconUTI
+ _OBJC_IVAR_$__DASStringInterning._internedStrings
+ _OBJC_IVAR_$__DASStringInterning._interns
+ _OBJC_IVAR_$__DASStringInterning._lookups
+ _OBJC_METACLASS_$__DASStringInterning
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$__DASInterning
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$__DASInterning
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableArray_$__DASInterning
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableDictionary_$__DASInterning
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$__DASInterning
+ __OBJC_$_CATEGORY_NSArray_$__DASInterning
+ __OBJC_$_CATEGORY_NSDictionary_$__DASInterning
+ __OBJC_$_CATEGORY_NSMutableArray_$__DASInterning
+ __OBJC_$_CATEGORY_NSMutableDictionary_$__DASInterning
+ __OBJC_$_CATEGORY_NSMutableSet_$__DASInterning
+ __OBJC_$_CATEGORY_NSSet_$__DASInterning
+ __OBJC_$_CATEGORY_NSString_$__DASInterning
+ __OBJC_$_CLASS_METHODS_NSArray(_DASInterning|_DASEnumerable|_DASAdditions)
+ __OBJC_$_CLASS_METHODS_NSSet(_DASInterning|_DASEnumerable|_DASAdditions)
+ __OBJC_$_CLASS_METHODS__DASStringInterning
+ __OBJC_$_INSTANCE_METHODS_NSArray(_DASInterning|_DASEnumerable|_DASAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSMutableSet(_DASInterning|_DASAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSSet(_DASInterning|_DASEnumerable|_DASAdditions)
+ __OBJC_$_INSTANCE_METHODS__DASStringInterning
+ __OBJC_$_INSTANCE_VARIABLES__DASStringInterning
+ __OBJC_$_PROP_LIST__DASStringInterning
+ __OBJC_CLASS_PROTOCOLS_$_NSArray(_DASInterning|_DASEnumerable|_DASAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_NSSet(_DASInterning|_DASEnumerable|_DASAdditions)
+ __OBJC_CLASS_RO_$__DASStringInterning
+ __OBJC_METACLASS_RO_$__DASStringInterning
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.415
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.415.cold.1
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.416
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.416.cold.1
+ ___25-[_DASScheduler policies]_block_invoke.371
+ ___27-[_DASScheduler allBudgets]_block_invoke.368
+ ___27-[_DASScheduler statistics]_block_invoke.362
+ ___29-[_DASActivity reportingName]_block_invoke
+ ___31-[_DASScheduler runActivities:]_block_invoke.383
+ ___33-[_DASScheduler deferActivities:]_block_invoke.354
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.420
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.420.cold.1
+ ___34-[_DASScheduler evaluatePolicies:]_block_invoke.372
+ ___34-[_DASScheduler inspect:criteria:]_block_invoke
+ ___34-[_DASScheduler inspect:criteria:]_block_invoke.365
+ ___34-[_DASScheduler inspect:criteria:]_block_invoke.cold.1
+ ___35-[_DASBMHistogramBuilder histogram]_block_invoke.71
+ ___35-[_DASScheduler currentPredictions]_block_invoke.359
+ ___35-[_DASScheduler submitTaskRequest:]_block_invoke.388
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.398
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.398.cold.1
+ ___36-[_DASScheduler submittedActivities]_block_invoke.356
+ ___37+[_DASStringInterning sharedInstance]_block_invoke
+ ___37-[_DASScheduler pauseWithParameters:]_block_invoke.380
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.390
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.390.cold.1
+ ___40-[NSDictionary(_DASInterning) das_dedup]_block_invoke
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.423
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.423.cold.1
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.424
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.424.cold.1
+ ___41-[_DASScheduler activityForActivityName:]_block_invoke
+ ___41-[_DASScheduler activityForActivityName:]_block_invoke.441
+ ___41-[_DASScheduler activityForActivityName:]_block_invoke.cold.1
+ ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.381
+ ___41-[_DASScheduler delayedRunningActivities]_block_invoke.358
+ ___42-[NSMutableArray(_DASInterning) das_dedup]_block_invoke
+ ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.369
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.433
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.433.cold.1
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.433.cold.2
+ ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.330
+ ___42-[_DASScheduler runProceedableActivities:]_block_invoke.374
+ ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.376
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.434
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.434.cold.1
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.434.cold.2
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.cold.1
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.432
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.432.cold.1
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.432.cold.2
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.439
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.439.cold.1
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.439.cold.2
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.352
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.352.cold.1
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.379
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.379.cold.1
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.419
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.419.cold.1
+ ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.366
+ ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.382
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.399
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.399.cold.1
+ ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.375
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.389
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.389.cold.1
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.397
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.397.cold.1
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.373
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.373.cold.1
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.404
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.404.cold.1
+ ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.378
+ ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.363
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.377
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.377.cold.1
+ ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.367
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.414
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.414.cold.1
+ ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.400
+ ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.428
+ ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.428.cold.1
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.413
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.413.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.440
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.440.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.440.cold.2
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.361
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.361.cold.1
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.421
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.421.cold.1
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.430
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.430.cold.1
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.425
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.425.cold.1
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.417
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.417.cold.1
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.426
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.426.cold.1
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.422
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.422.cold.1
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.418
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.418.cold.1
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.427
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.427.cold.1
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.435
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.435.cold.1
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.435.cold.2
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.436
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.436.cold.1
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.436.cold.2
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.402
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.437
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.437.cold.1
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.437.cold.2
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.412
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.412.cold.1
+ ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke
+ ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.429
+ ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.429.cold.1
+ ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.438
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.438.cold.1
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.438.cold.2
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___69-[_DASScheduler getSubmittedSystemTaskRequestsWithCompletionHandler:]_block_invoke
+ ___69-[_DASScheduler getSubmittedSystemTaskRequestsWithCompletionHandler:]_block_invoke.cold.1
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.403
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.403.cold.1
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.431
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.431.cold.1
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.405
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.405.cold.1
+ ____das_xpc_array_string_interned_block_invoke
+ ____das_xpc_dictionary_string_interned_block_invoke
+ ____das_xpc_object_string_interned_block_invoke
+ ___block_descriptor_40_e8_32r_e22_v16?0"_DASActivity"8lr32l8
+ ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
+ ___block_literal_global.385
+ ___block_literal_global.419
+ ___block_literal_global.426
+ ___block_literal_global.68
+ __das_internStringsInMutableObject
+ __das_internStringsInObject
+ __das_xpc_object_string_interned
+ __das_xpc_object_string_interned.cold.1
+ __das_xpc_object_string_interned.onceToken
+ __das_xpc_object_string_interned.stringCache
+ __xpc_type_array
+ __xpc_type_string
+ _kDASOnBatteryRuntimeLimitationName
+ _kReportingNamePrefixes
+ _objc_msgSend$activityForActivityName:handler:
+ _objc_msgSend$allowsCompanionExpensiveNetworking
+ _objc_msgSend$beforeApplicationLaunch
+ _objc_msgSend$beforeDaysFirstActivity
+ _objc_msgSend$bundle
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$darkWakeEligible
+ _objc_msgSend$das_dedup
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$getFeatureDependencyGraphs:timeFilter:bgsqlData:handler:
+ _objc_msgSend$getFeatureLatencyProjections:timeFilter:bgsqlData:handler:
+ _objc_msgSend$getRebootEvents:bgsqlData:handler:
+ _objc_msgSend$getSubmittedSystemTaskRequestsWithCompletionHandler:
+ _objc_msgSend$getSystemConditionsTimeline:timeFilter:bgsqlData:handler:
+ _objc_msgSend$getTaskDependencyGraphs:timeFilter:bgsqlData:handler:
+ _objc_msgSend$getTaskLatencyProjections:timeFilter:bgsqlData:handler:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$handleForAuditToken:error:
+ _objc_msgSend$hashString:
+ _objc_msgSend$immediateRuntimeState
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:submissionStrategy:executionContext:hostAppAuditToken:
+ _objc_msgSend$inspect:criteria:withHandler:
+ _objc_msgSend$internString:
+ _objc_msgSend$isDaemon
+ _objc_msgSend$isValidSuspensionExemptions:
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$motionState
+ _objc_msgSend$onBatteryRuntimeState
+ _objc_msgSend$postInstall
+ _objc_msgSend$purge
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$reportingName
+ _objc_msgSend$reportingServiceName
+ _objc_msgSend$requiresBuddyComplete
+ _objc_msgSend$runOnAppForeground
+ _objc_msgSend$serviceName
+ _objc_msgSend$setImmediateRuntimeState:
+ _objc_msgSend$setOnBatteryRuntimeState:
+ _objc_msgSend$shouldImposeDeviceInactivity
+ _objc_msgSend$statistics
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$userIdentifier
+ _reportingName.onceToken
+ _xpc_array_append_value
+ _xpc_array_apply
+ _xpc_array_create_empty
+ _xpc_dictionary_create_empty
+ _xpc_dictionary_set_value
+ _xpc_get_type
+ _xpc_string_cache_create
+ _xpc_string_create_cached
- -[_DASActivity taskInstanceID]
- -[_DASContinuedProcessingWrapper iconBundleIdentifier]
- -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:]
- -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:submissionStrategy:isForegroundAppProxy:]
- -[_DASContinuedProcessingWrapper initWithTitle:subtitle:resources:submissionStrategy:]
- -[_DASContinuedProcessingWrapper setIconBundleIdentifier:]
- -[_DASContinuedProcessingWrapper setIsForegroundAppProxy:]
- -[_DASPlistParser suspensionDelayMitigationsForActivity:]
- -[_DASPlistParser suspensionDelayMitigationsForActivity:].cold.1
- -[_DASPlistParser suspensionDelayMitigationsForActivity:].cold.2
- -[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]
- -[_DASScheduler inspect:]
- GCC_except_table126
- GCC_except_table131
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table226
- GCC_except_table229
- GCC_except_table239
- GCC_except_table242
- GCC_except_table245
- GCC_except_table248
- GCC_except_table251
- GCC_except_table254
- GCC_except_table257
- GCC_except_table260
- GCC_except_table263
- GCC_except_table266
- GCC_except_table269
- GCC_except_table272
- GCC_except_table275
- GCC_except_table278
- GCC_except_table281
- GCC_except_table284
- GCC_except_table287
- GCC_except_table290
- GCC_except_table293
- GCC_except_table328
- GCC_except_table329
- _OBJC_IVAR_$__DASActivity._requestsImmediateRuntime
- _OBJC_IVAR_$__DASContinuedProcessingWrapper._iconBundleIdentifier
- _OBJC_IVAR_$__DASContinuedProcessingWrapper._isForegroundAppProxy
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableSet_$__DASAdditions
- __OBJC_$_CATEGORY_NSArray_$__DASEnumerable
- __OBJC_$_CATEGORY_NSMutableSet_$__DASAdditions
- __OBJC_$_CATEGORY_NSSet_$__DASEnumerable
- __OBJC_$_CLASS_METHODS_NSArray(_DASEnumerable|_DASAdditions)
- __OBJC_$_CLASS_METHODS_NSSet(_DASEnumerable|_DASAdditions)
- __OBJC_$_INSTANCE_METHODS_NSArray(_DASEnumerable|_DASAdditions)
- __OBJC_$_INSTANCE_METHODS_NSSet(_DASEnumerable|_DASAdditions)
- __OBJC_$_PROP_LIST_NSArray_$__DASEnumerable
- __OBJC_$_PROP_LIST_NSSet_$__DASEnumerable
- __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$__DASEnumerable
- __OBJC_CATEGORY_PROTOCOLS_$_NSSet_$__DASEnumerable
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.403
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.403.cold.1
- ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.404
- ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.404.cold.1
- ___25-[_DASScheduler inspect:]_block_invoke
- ___25-[_DASScheduler inspect:]_block_invoke.353
- ___25-[_DASScheduler inspect:]_block_invoke.cold.1
- ___25-[_DASScheduler policies]_block_invoke.359
- ___27-[_DASScheduler allBudgets]_block_invoke.356
- ___27-[_DASScheduler statistics]_block_invoke.350
- ___31-[_DASScheduler runActivities:]_block_invoke.371
- ___33-[_DASScheduler deferActivities:]_block_invoke.342
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.408
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.408.cold.1
- ___34-[_DASScheduler evaluatePolicies:]_block_invoke.360
- ___35-[_DASBMHistogramBuilder histogram]_block_invoke.72
- ___35-[_DASScheduler currentPredictions]_block_invoke.347
- ___35-[_DASScheduler submitTaskRequest:]_block_invoke.376
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.386
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.386.cold.1
- ___36-[_DASScheduler submittedActivities]_block_invoke.344
- ___37-[_DASScheduler pauseWithParameters:]_block_invoke.368
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.378
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.378.cold.1
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.411
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.411.cold.1
- ___40-[_DASScheduler getContentionPenalties:]_block_invoke.412
- ___40-[_DASScheduler getContentionPenalties:]_block_invoke.412.cold.1
- ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.369
- ___41-[_DASScheduler delayedRunningActivities]_block_invoke.346
- ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.357
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.420
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.420.cold.1
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.420.cold.2
- ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.318
- ___42-[_DASScheduler runProceedableActivities:]_block_invoke.362
- ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.364
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.419
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.419.cold.1
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.419.cold.2
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.422
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.422.cold.1
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.422.cold.2
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.340
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.340.cold.1
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.367
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.367.cold.1
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.407
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.407.cold.1
- ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.354
- ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.370
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.387
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.387.cold.1
- ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.363
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.377
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.377.cold.1
- ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.385
- ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.385.cold.1
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.361
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.361.cold.1
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.392
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.392.cold.1
- ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.366
- ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.351
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.365
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.365.cold.1
- ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.355
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.402
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.402.cold.1
- ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.388
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.416
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.416.cold.1
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.401
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.401.cold.1
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.423
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.423.cold.1
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.423.cold.2
- ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.349
- ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.349.cold.1
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.409
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.409.cold.1
- ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.417
- ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.417.cold.1
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.413
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.413.cold.1
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.405
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.405.cold.1
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.414
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.414.cold.1
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.410
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.410.cold.1
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.406
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.406.cold.1
- ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.415
- ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.415.cold.1
- ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.390
- ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.400
- ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.400.cold.1
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.421
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.421.cold.1
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.421.cold.2
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.cold.1
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.391
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.391.cold.1
- ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.418
- ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.418.cold.1
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.393
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.393.cold.1
- ___block_literal_global.373
- ___block_literal_global.410
- ___block_literal_global.69
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$dk_dedup
- _objc_msgSend$getEstimatedMADCompletionTimes:endDate:bgsqlData:handler:
- _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:submissionStrategy:isForegroundAppProxy:
- _objc_msgSend$inspect:withHandler:
- _objc_msgSend$setRequestsImmediateRuntime:
- _objc_msgSend$string
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x8
CStrings:
+ "%u:"
+ "(\\[[^\\]]+\\])+$"
+ "*"
+ ", Immediate Runtime State: %d"
+ "@\"NSArray\"32@0:8@\"NSString\"16@\"NSString\"24"
+ "@\"NSArray\"40@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32"
+ "@\"NSMapTable\""
+ "@\"_DASActivity\"24@0:8@\"NSString\"16"
+ "@104@0:8@16@24@32@40q48q56q64{?=[8I]}72"
+ "@88@0:8@16@24q32q40q48{?=[8I]}56"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "Can't load config plist"
+ "Error getting client name for activity %@: %@"
+ "Error getting feature dependency graphs for %@: %@"
+ "Error getting reboot events and timeline: %@"
+ "Error getting system conditions timeline: %@"
+ "Error getting task dependency graphs for %@: %@"
+ "Error trying to get feature dependency graphs for %@"
+ "Error trying to get system conditions timeline."
+ "Error trying to get task dependency graphs for %@"
+ "Error trying to retreive reboot events and timeline"
+ "Major"
+ "Minor"
+ "OnBatteryRuntime"
+ "Successfully retrieved feature dependency graphs for %@"
+ "Successfully retrieved reboot events and timeline"
+ "Successfully retrieved system conditions timeline"
+ "Successfully retrieved task dependency graphs for %@"
+ "SuspensionExemptions"
+ "SuspensionThreshold"
+ "T@\"NSMapTable\",&,N,V_internedStrings"
+ "T@\"NSString\",C,N,V_iconUTI"
+ "T@\"_DASFileProtection\",C,N"
+ "TB,N,V_postInstall"
+ "TQ,N,V_immediateRuntimeState"
+ "TQ,N,V_interns"
+ "TQ,N,V_lookups"
+ "TQ,N,V_onBatteryRuntimeState"
+ "Threshold"
+ "Tq,N,V_executionContext"
+ "T{?=[8I]},N,V_hostAppAuditToken"
+ "UIKitApplication:"
+ "_DASInterning"
+ "_DASStringInterning"
+ "_executionContext"
+ "_hostAppAuditToken"
+ "_iconUTI"
+ "_immediateRuntimeState"
+ "_internedStrings"
+ "_interns"
+ "_lookups"
+ "_onBatteryRuntimeState"
+ "_postInstall"
+ "_requiresDeviceInactivityIsSetByUser"
+ "activityForActivityName:"
+ "activityForActivityName:handler:"
+ "bundle"
+ "characterAtIndex:"
+ "ckdiscretionaryd.com.apple"
+ "com.apple"
+ "com.apple.CFNetwork-cc"
+ "com.apple.CloudKit.SyncEngine"
+ "com.apple.URLSession"
+ "com.apple.coredata.cloudkit.activity.export"
+ "com.apple.coredata.cloudkit.activity.import"
+ "com.apple.dasd.config.plist"
+ "com.apple.duetactivityscheduler.stringcache"
+ "convertUUIDToUint64:"
+ "das_dedup"
+ "das_interningStatistics"
+ "das_purgeInterned"
+ "dataWithBytes:length:"
+ "dictionaryRepresentation"
+ "enumerateObjectsUsingBlock:"
+ "executionContext"
+ "getBytes:length:"
+ "getFeatureDependencyGraphs:timeFilter:bgsqlData:"
+ "getFeatureDependencyGraphs:timeFilter:bgsqlData:handler:"
+ "getFeatureLatencyProjections:timeFilter:bgsqlData:"
+ "getFeatureLatencyProjections:timeFilter:bgsqlData:handler:"
+ "getRebootEvents:bgsqlData:"
+ "getRebootEvents:bgsqlData:handler:"
+ "getSubmittedSystemTaskRequestsWithCompletionHandler Failed: %@"
+ "getSubmittedSystemTaskRequestsWithCompletionHandler:"
+ "getSystemConditionsTimeline:timeFilter:bgsqlData:"
+ "getSystemConditionsTimeline:timeFilter:bgsqlData:handler:"
+ "getTaskDependencyGraphs:timeFilter:bgsqlData:"
+ "getTaskDependencyGraphs:timeFilter:bgsqlData:handler:"
+ "getTaskLatencyProjections:timeFilter:bgsqlData:"
+ "getTaskLatencyProjections:timeFilter:bgsqlData:handler:"
+ "getUUIDBytes:"
+ "handleForAuditToken:error:"
+ "hashString:"
+ "hitRate"
+ "hits"
+ "hostAppAuditToken"
+ "iconUTI"
+ "immediateRuntimeState"
+ "initWithCapacity:"
+ "initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:"
+ "initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:submissionStrategy:executionContext:hostAppAuditToken:"
+ "initWithTitle:subtitle:resources:submissionStrategy:executionContext:hostAppAuditToken:"
+ "inspect:criteria:"
+ "inspect:criteria:withHandler:"
+ "internString:"
+ "internedStrings"
+ "interns"
+ "isDaemon"
+ "isValidSuspensionExemptions:"
+ "lookups"
+ "mapTableWithKeyOptions:valueOptions:"
+ "misses"
+ "nsurl-AV"
+ "onBatteryRuntimeState"
+ "postInstall"
+ "purge"
+ "rectifyExecutionContextWithClientProcessHandle:hostAppProcHandle:"
+ "regularExpressionWithPattern:options:error:"
+ "reportingName"
+ "reportingServiceName"
+ "setExecutionContext:"
+ "setHostAppAuditToken:"
+ "setIconUTI:"
+ "setImmediateRuntimeState:"
+ "setInternedStrings:"
+ "setInterns:"
+ "setLookups:"
+ "setOnBatteryRuntimeState:"
+ "setPostInstall:"
+ "shouldImposeDeviceInactivity"
+ "size"
+ "stringByReplacingMatchesInString:options:range:withTemplate:"
+ "suspensionExemptionsForActivity:"
+ "v24@0:8@?<v@?@\"NSObject<OS_xpc_object>\"@\"NSError\">16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"_DASActivity\">24"
+ "v32@?0@8Q16^B24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
+ "v48@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32@?<v@?@\"NSArray\">40"
+ "v48@0:8{?=[8I]}16"
+ "{?=\"val\"[8I]}"
+ "{?=[8I]}16@0:8"
- "@\"NSDictionary\"40@0:8@\"NSSet\"16@\"NSDate\"24@\"NSData\"32"
- "@48@0:8@16@24q32q40"
- "@68@0:8@16@24@32@40q48q56B64"
- "Error getting estimated MAD completion times for %@: %@"
- "Error trying to get estimated MAD completion times for %@"
- "Successfully retrieved estimated MAD completion times for %@"
- "SuspensionDelayMitigations"
- "T@\"NSString\",C,N,V_iconBundleIdentifier"
- "T@\"_DASFileProtection\",C,N,V_fileProtection"
- "TB,N,V_isForegroundAppProxy"
- "TB,N,V_requestsImmediateRuntime"
- "_iconBundleIdentifier"
- "_isForegroundAppProxy"
- "_requestsImmediateRuntime"
- "com.apple.DuetActivityScheduler"
- "dk_dedup"
- "getEstimatedMADCompletionTimes:endDate:bgsqlData:"
- "getEstimatedMADCompletionTimes:endDate:bgsqlData:handler:"
- "iconBundleIdentifier"
- "initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:"
- "initWithTitle:subtitle:iconBundleIdentifier:linkToBundleIdentifier:resources:submissionStrategy:isForegroundAppProxy:"
- "initWithTitle:subtitle:resources:submissionStrategy:"
- "inspect:"
- "inspect:withHandler:"
- "requestsimmediateRuntime"
- "setIconBundleIdentifier:"
- "setIsForegroundAppProxy:"
- "string"
- "suspensionDelayMitigationsForActivity:"
- "taskInstanceID"
- "v48@0:8@\"NSSet\"16@\"NSDate\"24@\"NSData\"32@?<v@?@\"NSDictionary\">40"

```
