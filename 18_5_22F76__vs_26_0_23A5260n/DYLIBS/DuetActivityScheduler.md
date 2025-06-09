## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-1856.120.12.0.0
-  __TEXT.__text: 0x30bd0
-  __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x3c58
-  __TEXT.__const: 0x150
-  __TEXT.__gcc_except_tab: 0x131c
-  __TEXT.__cstring: 0x239e
-  __TEXT.__oslogstring: 0x2c29
-  __TEXT.__unwind_info: 0xe18
-  __TEXT.__objc_classname: 0x6e3
-  __TEXT.__objc_methname: 0x94cb
-  __TEXT.__objc_methtype: 0x16a3
-  __TEXT.__objc_stubs: 0x54e0
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0xe90
-  __DATA_CONST.__objc_classlist: 0x120
-  __DATA_CONST.__objc_catlist: 0x20
+2109.0.44.502.1
+  __TEXT.__text: 0x34d50
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x4138
+  __TEXT.__const: 0x158
+  __TEXT.__gcc_except_tab: 0x14e4
+  __TEXT.__cstring: 0x25eb
+  __TEXT.__oslogstring: 0x2ec0
+  __TEXT.__unwind_info: 0xf50
+  __TEXT.__objc_classname: 0x727
+  __TEXT.__objc_methname: 0xa29d
+  __TEXT.__objc_methtype: 0x1ae0
+  __TEXT.__objc_stubs: 0x5b00
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__const: 0xee0
+  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2240
+  __DATA_CONST.__objc_selrefs: 0x24c0
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x358
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__cfstring: 0x3380
-  __AUTH_CONST.__objc_const: 0x6b70
+  __AUTH_CONST.__auth_got: 0x368
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__cfstring: 0x3660
+  __AUTH_CONST.__objc_const: 0x7398
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x3cc
-  __DATA.__data: 0xde0
-  __DATA.__bss: 0x50
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x424
+  __DATA.__data: 0xdf0
+  __DATA.__bss: 0x60
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x8c0
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8BBA061D-41DC-3655-8473-4CAD2B028396
-  Functions: 1368
-  Symbols:   4794
-  CStrings:  2989
+  UUID: 67AD333F-CCE2-3364-9BEA-6598ECB94F0C
+  Functions: 1473
+  Symbols:   5150
+  CStrings:  3204
 
Symbols:
+ +[NSProgress(DASAdditions) indeterminateProgress]
+ +[_DASActivity continuedProcessingActivityWithName:]
+ +[_DASContinuedProcessingWrapper supportsSecureCoding]
+ +[_DASFileProtection completeWhenUserInactive]
+ +[_DASFileProtection completeWhenUserInactive].cold.1
+ +[_DASPredictionTimeline supportsSecureCoding]
+ -[NSDate(_DASAdditions) haveNSecondsElapsed:]
+ -[_DASActivity billedEnergy]
+ -[_DASActivity continuedProcessingWrapper]
+ -[_DASActivity cpuCycleConsumed]
+ -[_DASActivity cpuTimeConsumed]
+ -[_DASActivity dataConsumed]
+ -[_DASActivity diskIOConsumed]
+ -[_DASActivity hashArrayOfString:]
+ -[_DASActivity indeedCPUIntensive]
+ -[_DASActivity indeedMemoryIntensive]
+ -[_DASActivity internalGroupNames]
+ -[_DASActivity isEmergencySOSActivity]
+ -[_DASActivity isIndeedIntensive]
+ -[_DASActivity isPartOfCustomGroup]
+ -[_DASActivity isRunning]
+ -[_DASActivity requestsImmediateRuntime]
+ -[_DASActivity setBilledEnergy:]
+ -[_DASActivity setContinuedProcessingWrapper:]
+ -[_DASActivity setCpuCycleConsumed:]
+ -[_DASActivity setCpuTimeConsumed:]
+ -[_DASActivity setDataConsumed:]
+ -[_DASActivity setDiskIOConsumed:]
+ -[_DASActivity setIndeedCPUIntensive:]
+ -[_DASActivity setIndeedMemoryIntensive:]
+ -[_DASActivity setInternalGroupNames:]
+ -[_DASActivity setRequestsImmediateRuntime:]
+ -[_DASActivity setStartedInIdle:]
+ -[_DASActivity setStartedOnBattery:]
+ -[_DASActivity setThermalLevelElevated:]
+ -[_DASActivity setUninterruptibleDuration:]
+ -[_DASActivity startedInIdle]
+ -[_DASActivity startedOnBattery]
+ -[_DASActivity taskID]
+ -[_DASActivity taskInstanceID]
+ -[_DASActivity thermalLevelElevated]
+ -[_DASActivity uninterruptibleDuration]
+ -[_DASActivity updateInternalGroups]
+ -[_DASContinuedProcessingWrapper .cxx_destruct]
+ -[_DASContinuedProcessingWrapper copyWithZone:]
+ -[_DASContinuedProcessingWrapper encodeWithCoder:]
+ -[_DASContinuedProcessingWrapper iconBundleIdentifier]
+ -[_DASContinuedProcessingWrapper initWithCoder:]
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconBundleIdentifier:resources:]
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:]
+ -[_DASContinuedProcessingWrapper initWithTitle:subtitle:resources:submissionStrategy:]
+ -[_DASContinuedProcessingWrapper resources]
+ -[_DASContinuedProcessingWrapper setIconBundleIdentifier:]
+ -[_DASContinuedProcessingWrapper setResources:]
+ -[_DASContinuedProcessingWrapper setSubmissionStrategy:]
+ -[_DASContinuedProcessingWrapper setSubtitle:]
+ -[_DASContinuedProcessingWrapper setTitle:]
+ -[_DASContinuedProcessingWrapper submissionStrategy]
+ -[_DASContinuedProcessingWrapper subtitle]
+ -[_DASContinuedProcessingWrapper title]
+ -[_DASPredictionTimeline .cxx_destruct]
+ -[_DASPredictionTimeline copyWithZone:]
+ -[_DASPredictionTimeline description]
+ -[_DASPredictionTimeline encodeWithCoder:]
+ -[_DASPredictionTimeline endDate]
+ -[_DASPredictionTimeline initWithCoder:]
+ -[_DASPredictionTimeline initWithValues:eachWithDuration:startingAt:]
+ -[_DASPredictionTimeline initWithValues:forDurations:startingAt:]
+ -[_DASPredictionTimeline initWithValues:startDate:transitionDates:]
+ -[_DASPredictionTimeline lowLikelihoodPeriod]
+ -[_DASPredictionTimeline startDate]
+ -[_DASPredictionTimeline transitionDates]
+ -[_DASPredictionTimeline valueAtDate:]
+ -[_DASPredictionTimeline valuesUntilEndDate:withIntervalDuration:]
+ -[_DASPredictionTimeline values]
+ -[_DASScheduler cancelActivitiesWithReason:cancellationReason:]
+ -[_DASScheduler completeTaskRequest:withSuccess:]
+ -[_DASScheduler continuedProcessingDeviceCapabilities:]
+ -[_DASScheduler currentAllocations:timeFilter:bgsqlData:]
+ -[_DASScheduler getContentionPenalties:]
+ -[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]
+ -[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]
+ -[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]
+ -[_DASScheduler getSortedCandidateActivities:]
+ -[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]
+ -[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]
+ -[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]
+ -[_DASScheduler triggerScoreEvaluationAndRunActivities:]
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table129
+ GCC_except_table138
+ GCC_except_table141
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table159
+ GCC_except_table188
+ GCC_except_table218
+ GCC_except_table222
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table231
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
+ GCC_except_table330
+ GCC_except_table331
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table95
+ _NSFileProtectionCompleteWhenUserInactive
+ _OBJC_CLASS_$_BMWidgetsRefresh
+ _OBJC_CLASS_$_BMWidgetsViewed
+ _OBJC_CLASS_$_NSDateInterval
+ _OBJC_CLASS_$_NSOrderedSet
+ _OBJC_CLASS_$__DASContinuedProcessingWrapper
+ _OBJC_CLASS_$__DASPredictionTimeline
+ _OBJC_IVAR_$__DASActivity._billedEnergy
+ _OBJC_IVAR_$__DASActivity._continuedProcessingWrapper
+ _OBJC_IVAR_$__DASActivity._cpuCycleConsumed
+ _OBJC_IVAR_$__DASActivity._cpuTimeConsumed
+ _OBJC_IVAR_$__DASActivity._dataConsumed
+ _OBJC_IVAR_$__DASActivity._diskIOConsumed
+ _OBJC_IVAR_$__DASActivity._indeedCPUIntensive
+ _OBJC_IVAR_$__DASActivity._indeedMemoryIntensive
+ _OBJC_IVAR_$__DASActivity._internalGroupLock
+ _OBJC_IVAR_$__DASActivity._internalGroupNames
+ _OBJC_IVAR_$__DASActivity._requestsImmediateRuntime
+ _OBJC_IVAR_$__DASActivity._startedInIdle
+ _OBJC_IVAR_$__DASActivity._startedOnBattery
+ _OBJC_IVAR_$__DASActivity._thermalLevelElevated
+ _OBJC_IVAR_$__DASActivity._uninterruptibleDuration
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._iconBundleIdentifier
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._resources
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._submissionStrategy
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._subtitle
+ _OBJC_IVAR_$__DASContinuedProcessingWrapper._title
+ _OBJC_IVAR_$__DASPredictionTimeline._startDate
+ _OBJC_IVAR_$__DASPredictionTimeline._transitionDates
+ _OBJC_IVAR_$__DASPredictionTimeline._values
+ _OBJC_METACLASS_$__DASContinuedProcessingWrapper
+ _OBJC_METACLASS_$__DASPredictionTimeline
+ __DASBirdRateLimitConfigurationName
+ __DASContextKey
+ __DASContinuedProcessingTaskAssertionTag
+ __DASDefaultContinuedProcessingGroupName
+ __DASDefaultIntensiveGroupName
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSProgress_$_DASAdditions
+ __OBJC_$_CATEGORY_NSProgress_$_DASAdditions
+ __OBJC_$_CLASS_METHODS__DASContinuedProcessingWrapper
+ __OBJC_$_CLASS_METHODS__DASPredictionTimeline
+ __OBJC_$_CLASS_PROP_LIST__DASContinuedProcessingWrapper
+ __OBJC_$_CLASS_PROP_LIST__DASPredictionTimeline
+ __OBJC_$_INSTANCE_METHODS__DASContinuedProcessingWrapper
+ __OBJC_$_INSTANCE_METHODS__DASPredictionTimeline
+ __OBJC_$_INSTANCE_VARIABLES__DASContinuedProcessingWrapper
+ __OBJC_$_INSTANCE_VARIABLES__DASPredictionTimeline
+ __OBJC_$_PROP_LIST__DASContinuedProcessingWrapper
+ __OBJC_$_PROP_LIST__DASPredictionTimeline
+ __OBJC_CLASS_PROTOCOLS_$__DASContinuedProcessingWrapper
+ __OBJC_CLASS_PROTOCOLS_$__DASPredictionTimeline
+ __OBJC_CLASS_RO_$__DASContinuedProcessingWrapper
+ __OBJC_CLASS_RO_$__DASPredictionTimeline
+ __OBJC_METACLASS_RO_$__DASContinuedProcessingWrapper
+ __OBJC_METACLASS_RO_$__DASPredictionTimeline
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.405
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.405.cold.1
+ ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.cold.1
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.406
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.406.cold.1
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.cold.1
+ ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.311
+ ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.311.cold.1
+ ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.328
+ ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.328.cold.1
+ ___25-[_DASScheduler inspect:]_block_invoke.355
+ ___25-[_DASScheduler policies]_block_invoke.361
+ ___27-[_DASScheduler allBudgets]_block_invoke.358
+ ___27-[_DASScheduler statistics]_block_invoke.352
+ ___31-[_DASScheduler runActivities:]_block_invoke.373
+ ___33-[_DASScheduler deferActivities:]_block_invoke.344
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.410
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.410.cold.1
+ ___34-[_DASScheduler evaluatePolicies:]_block_invoke.362
+ ___35-[_DASScheduler currentPredictions]_block_invoke.349
+ ___35-[_DASScheduler submitTaskRequest:]_block_invoke.378
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.388
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.388.cold.1
+ ___36-[_DASScheduler submittedActivities]_block_invoke.346
+ ___37-[_DASScheduler pauseWithParameters:]_block_invoke.370
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.380
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.380.cold.1
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.413
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.413.cold.1
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.414
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.414.cold.1
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.cold.1
+ ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.371
+ ___41-[_DASScheduler delayedRunningActivities]_block_invoke.348
+ ___41-[_DASScheduler delayedRunningActivities]_block_invoke.cold.1
+ ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.359
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.422
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.422.cold.1
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.422.cold.2
+ ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.319
+ ___42-[_DASScheduler runProceedableActivities:]_block_invoke.364
+ ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.366
+ ___46+[_DASFileProtection completeWhenUserInactive]_block_invoke
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.421
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.421.cold.1
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.421.cold.2
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.424
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.424.cold.1
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.424.cold.2
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.cold.1
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.342
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.342.cold.1
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.369
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.369.cold.1
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.409
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.409.cold.1
+ ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.356
+ ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.372
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.389
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.389.cold.1
+ ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.365
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.379
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.379.cold.1
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.387
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.387.cold.1
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.363
+ ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.363.cold.1
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.394
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.394.cold.1
+ ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.368
+ ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.353
+ ___50-[_DASWidgetRefreshScheduler sanitizeWidgetViews:]_block_invoke.244
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.367
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.367.cold.1
+ ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.357
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.404
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.404.cold.1
+ ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke
+ ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.390
+ ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.cold.1
+ ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.418
+ ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.418.cold.1
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.403
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.403.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.425
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.425.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.425.cold.2
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.cold.1
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.351
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.411
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.411.cold.1
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.419
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.419.cold.1
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.cold.1
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.415
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.415.cold.1
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.407
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.407.cold.1
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.416
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.416.cold.1
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.412
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.412.cold.1
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.408
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.408.cold.1
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.417
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.417.cold.1
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.cold.1
+ ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.392
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.402
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.402.cold.1
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.cold.1
+ ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.423
+ ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.423.cold.1
+ ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.423.cold.2
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.393
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.393.cold.1
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.420
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.420.cold.1
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.cold.1
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.395
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.395.cold.1
+ ___block_descriptor_40_e8_32bs_e8_v16?0q8ls32l8
+ ___block_descriptor_56_e8_32s40s48r_e8_v12?0B8ls32l8s40l8r48l8
+ ___block_literal_global.19
+ ___block_literal_global.21
+ ___block_literal_global.23
+ ___block_literal_global.243
+ ___block_literal_global.25
+ ___block_literal_global.375
+ ___block_literal_global.401
+ __os_feature_enabled_impl
+ _completeWhenUserInactive.fileCompletionCompleteWhenUserInactive
+ _completeWhenUserInactive.onceToken
+ _kDASImmediateRuntimeLimitationName
+ _kDASUninterruptibleRuntimeLimitationName
+ _objc_msgSend$Refresh
+ _objc_msgSend$Viewed
+ _objc_msgSend$Widgets
+ _objc_msgSend$aneIntensive
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$completeTaskRequest:withSuccess:completionHandler:
+ _objc_msgSend$completeWhenUserInactive
+ _objc_msgSend$continuedProcessingDeviceCapabilities:
+ _objc_msgSend$continuedProcessingWrapper
+ _objc_msgSend$cpuIntensive
+ _objc_msgSend$currentAllocations:timeFilter:bgsqlData:withHandler:
+ _objc_msgSend$diskIntensive
+ _objc_msgSend$getContentionPenalties:handler:
+ _objc_msgSend$getEligibilityTimelines:timeFilter:bgsqlData:handler:
+ _objc_msgSend$getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:handler:
+ _objc_msgSend$getSchedulerEfficiencyMetrics:bgsqlData:handler:
+ _objc_msgSend$getSortedCandidateActivities:handler:
+ _objc_msgSend$gpuIntensive
+ _objc_msgSend$hashArrayOfString:
+ _objc_msgSend$iconBundleIdentifier
+ _objc_msgSend$initWithBudgetID:bundleID:endDate:extensionBundleID:inStack:pageID:startDate:timeUntilExpiration:viewID:
+ _objc_msgSend$initWithBudgetID:extensionBundleID:isDASInitiated:refreshDate:refreshReason:
+ _objc_msgSend$initWithStartDate:endDate:
+ _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:
+ _objc_msgSend$initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:
+ _objc_msgSend$initWithTitle:subtitle:resources:submissionStrategy:
+ _objc_msgSend$initWithValues:startDate:transitionDates:
+ _objc_msgSend$integerValue
+ _objc_msgSend$internalGroupNames
+ _objc_msgSend$involvedProcesses
+ _objc_msgSend$isPartOfCustomGroup
+ _objc_msgSend$memoryIntensive
+ _objc_msgSend$orderedSetWithArray:
+ _objc_msgSend$protectionType
+ _objc_msgSend$reportFeatureCheckpoint:forFeature:atDate:withHandler:
+ _objc_msgSend$reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:withHandler:
+ _objc_msgSend$reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:withHandler:
+ _objc_msgSend$requestsImmediateRuntime
+ _objc_msgSend$requiresUnconstrainedNetworking
+ _objc_msgSend$resources
+ _objc_msgSend$sendEvent:
+ _objc_msgSend$setContinuedProcessingWrapper:
+ _objc_msgSend$setInternalGroupNames:
+ _objc_msgSend$setMaximumRuntime:
+ _objc_msgSend$setRequestsImmediateRuntime:
+ _objc_msgSend$setUninterruptibleDuration:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$source
+ _objc_msgSend$string
+ _objc_msgSend$submissionStrategy
+ _objc_msgSend$subtitle
+ _objc_msgSend$title
+ _objc_msgSend$transitionDates
+ _objc_msgSend$triggerScoreEvaluationAndRunActivities:handler:
+ _objc_msgSend$uninterruptibleDuration
+ _objc_msgSend$updateInternalGroups
+ _objc_msgSend$valueAtDate:
+ _objc_msgSend$values
+ _objc_retainAutoreleasedReturnValue
- -[_DASActivity clientProvidedIconBundleIdentifier]
- -[_DASActivity clientProvidedReason]
- -[_DASActivity clientProvidedTitle]
- -[_DASActivity setANEIntensive:]
- -[_DASActivity setClientProvidedReason:]
- -[_DASActivity setClientProvidedTitle:]
- -[_DASActivity setGPUIntensive:]
- -[_DASScheduler completeTaskRequest:]
- -[_DASScheduler reportFeatureCheckpoint:forFeature:error:]
- -[_DASWidgetRefreshScheduler setStore:]
- -[_DASWidgetRefreshScheduler store]
- GCC_except_table100
- GCC_except_table103
- GCC_except_table106
- GCC_except_table109
- GCC_except_table115
- GCC_except_table118
- GCC_except_table121
- GCC_except_table136
- GCC_except_table139
- GCC_except_table142
- GCC_except_table145
- GCC_except_table156
- GCC_except_table182
- GCC_except_table212
- GCC_except_table213
- GCC_except_table216
- GCC_except_table229
- GCC_except_table232
- GCC_except_table235
- GCC_except_table238
- GCC_except_table300
- GCC_except_table301
- GCC_except_table56
- GCC_except_table58
- GCC_except_table66
- GCC_except_table69
- GCC_except_table72
- GCC_except_table75
- GCC_except_table82
- GCC_except_table85
- GCC_except_table88
- GCC_except_table91
- _OBJC_CLASS_$__DKEvent
- _OBJC_CLASS_$__DKEventStream
- _OBJC_CLASS_$__DKKnowledgeStore
- _OBJC_CLASS_$__DKPredictionTimeline
- _OBJC_IVAR_$__DASWidgetRefreshScheduler._store
- ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.313
- ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.313.cold.1
- ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.330
- ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.330.cold.1
- ___25-[_DASScheduler inspect:]_block_invoke.327
- ___25-[_DASScheduler policies]_block_invoke.333
- ___27-[_DASScheduler allBudgets]_block_invoke.330
- ___27-[_DASScheduler clasStatus]_block_invoke
- ___27-[_DASScheduler clasStatus]_block_invoke.334
- ___27-[_DASScheduler clasStatus]_block_invoke.cold.1
- ___27-[_DASScheduler statistics]_block_invoke.324
- ___31-[_DASScheduler runActivities:]_block_invoke.346
- ___33-[_DASScheduler deferActivities:]_block_invoke.318
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.373
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.373.cold.1
- ___34-[_DASScheduler evaluatePolicies:]_block_invoke.335
- ___35-[_DASScheduler currentPredictions]_block_invoke.322
- ___35-[_DASScheduler submitTaskRequest:]_block_invoke.351
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.355
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.355.cold.1
- ___36-[_DASScheduler submittedActivities]_block_invoke.320
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke.354
- ___37-[_DASScheduler completeTaskRequest:]_block_invoke.354.cold.1
- ___37-[_DASScheduler pauseWithParameters:]_block_invoke.343
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.353
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.353.cold.1
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.376
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.376.cold.1
- ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.344
- ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.331
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.381
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.381.cold.1
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.381.cold.2
- ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.293
- ___42-[_DASScheduler runProceedableActivities:]_block_invoke.337
- ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.339
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.380
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.380.cold.1
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.380.cold.2
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.316
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.316.cold.1
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.342
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.342.cold.1
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.372
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.372.cold.1
- ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.328
- ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.345
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.356
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.356.cold.1
- ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.338
- ___48-[_DASWidgetRefreshScheduler recordWidgetViews:]_block_invoke_2
- ___48-[_DASWidgetRefreshScheduler recordWidgetViews:]_block_invoke_2.cold.1
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.352
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.352.cold.1
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.336
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.336.cold.1
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.359
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.359.cold.1
- ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.341
- ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.325
- ___50-[_DASWidgetRefreshScheduler sanitizeWidgetViews:]_block_invoke.245
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.340
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.340.cold.1
- ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.329
- ___52-[_DASWidgetRefreshScheduler recordWidgetRefreshes:]_block_invoke_2
- ___52-[_DASWidgetRefreshScheduler recordWidgetRefreshes:]_block_invoke_2.cold.1
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.369
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.369.cold.1
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.379
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.379.cold.1
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.368
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.368.cold.1
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.374
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.374.cold.1
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.377
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.377.cold.1
- ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke
- ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.367
- ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.367.cold.1
- ___58-[_DASScheduler reportFeatureCheckpoint:forFeature:error:]_block_invoke.cold.1
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.370
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.370.cold.1
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.378
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.378.cold.1
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.375
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.375.cold.1
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.371
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.371.cold.1
- ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.357
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.382
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.382.cold.1
- ___66-[_DASScheduler getEstimatedMADCompletionTimes:endDate:bgsqlData:]_block_invoke.382.cold.2
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.358
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.358.cold.1
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.360
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.360.cold.1
- ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
- ___block_literal_global.16
- ___block_literal_global.18
- ___block_literal_global.20
- ___block_literal_global.244
- ___block_literal_global.348
- ___block_literal_global.387
- _objc_msgSend$clasStatusWithHandler:
- _objc_msgSend$completeTaskRequest:completionHandler:
- _objc_msgSend$eventStreamWithName:
- _objc_msgSend$eventWithStream:startDate:endDate:identifierStringValue:metadata:
- _objc_msgSend$knowledgeStoreWithDirectReadWriteAccess
- _objc_msgSend$null
- _objc_msgSend$reportFeatureCheckpoint:forFeature:withHandler:
- _objc_msgSend$saveObjects:responseQueue:withCompletion:
- _objc_msgSend$store
CStrings:
+ ", Continued Processing Wrapper: %@"
+ ", InternalGroups: %@"
+ ", Requests Immediate Runtime"
+ ", Uninterruptible Runtime: %ld"
+ "<_DASPredictionTimeline: startDate: %@, endDate: %@, transitionDates: %@, valuesCount: %@>"
+ "@\"NSArray\"24@0:8@\"NSSet\"16"
+ "@\"NSDictionary\"40@0:8Q16@\"NSDateInterval\"24@\"NSData\"32"
+ "@\"_DASContinuedProcessingWrapper\""
+ "@40@0:8@16d24@32"
+ "@40@0:8Q16@24@32"
+ "@48@0:8@16@24@32q40"
+ "@48@0:8@16@24q32q40"
+ "@56@0:8@16@24@32q40q48"
+ "B24@0:8@\"NSSet\"16"
+ "B24@0:8d16"
+ "B48@0:8Q16Q24@\"NSDate\"32^@40"
+ "B48@0:8Q16Q24@32^@40"
+ "B80@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48Q56@\"NSNumber\"64^@72"
+ "B80@0:8@\"NSString\"16@\"NSString\"24Q32d40@\"NSNumber\"48Q56@\"NSNumber\"64^@72"
+ "B80@0:8@16@24@32@40@48Q56@64^@72"
+ "B80@0:8@16@24Q32d40@48Q56@64^@72"
+ "BirdConfiguration"
+ "ClassCX"
+ "Complete task request activity: %@ (%@)"
+ "Context"
+ "DAS"
+ "DASAdditions"
+ "Error getting contention penalty for %@: %@"
+ "Error getting sorted candidate activities for %@: %@"
+ "Error getting task eligibility timelines for %@: %@"
+ "Error obtaining allocations from scheduler: %@"
+ "Error obtaining delayed running activities remote object proxy: %@"
+ "Error trying to get contention penalty for %@"
+ "Error trying to get eligibility timelines."
+ "Error trying to get sorted candidate activities for %@"
+ "Failed"
+ "ImmediateRuntime"
+ "Refresh"
+ "Succeeded"
+ "Successfully retrieved contention penalty for %@"
+ "Successfully retrieved eligibility timelines."
+ "Successfully retrieved sorted candidate activities for %@"
+ "SupportsContinuedBackgroundProcessing"
+ "T@\"NSArray\",R,N,V_transitionDates"
+ "T@\"NSArray\",R,N,V_values"
+ "T@\"NSDate\",R,N"
+ "T@\"NSMutableSet\",C,N,V_internalGroupNames"
+ "T@\"NSString\",C,N,V_iconBundleIdentifier"
+ "T@\"NSString\",C,N,V_subtitle"
+ "T@\"NSString\",C,N,V_title"
+ "T@\"_DASContinuedProcessingWrapper\",&,N,V_continuedProcessingWrapper"
+ "TB,N,V_indeedCPUIntensive"
+ "TB,N,V_indeedMemoryIntensive"
+ "TB,N,V_requestsImmediateRuntime"
+ "TB,N,V_startedInIdle"
+ "TB,N,V_startedOnBattery"
+ "TB,N,V_thermalLevelElevated"
+ "Td,N,V_billedEnergy"
+ "Td,N,V_cpuCycleConsumed"
+ "Td,N,V_cpuTimeConsumed"
+ "Td,N,V_dataConsumed"
+ "Td,N,V_diskIOConsumed"
+ "Tq,N,V_resources"
+ "Tq,N,V_submissionStrategy"
+ "Tq,N,V_uninterruptibleDuration"
+ "Unauthorized Use of Requests Immediate Runtime"
+ "UninterruptibleRuntime"
+ "Viewed"
+ "Widgets"
+ "_DASContinuedProcessingWrapper"
+ "_DASPredictionTimeline"
+ "_billedEnergy"
+ "_continuedProcessingWrapper"
+ "_cpuCycleConsumed"
+ "_cpuTimeConsumed"
+ "_dataConsumed"
+ "_diskIOConsumed"
+ "_iconBundleIdentifier"
+ "_indeedCPUIntensive"
+ "_indeedMemoryIntensive"
+ "_internalGroupLock"
+ "_internalGroupNames"
+ "_requestsImmediateRuntime"
+ "_resources"
+ "_startedInIdle"
+ "_startedOnBattery"
+ "_submissionStrategy"
+ "_subtitle"
+ "_thermalLevelElevated"
+ "_title"
+ "_transitionDates"
+ "_uninterruptibleDuration"
+ "_values"
+ "arrayWithObject:"
+ "billedEnergy"
+ "cancelActivitiesWithReason:cancellationReason:"
+ "com.apple.dasd.continuedProcessing"
+ "com.apple.dasd.defaultIntensive"
+ "com.corelocation.eedmediaservice.progress"
+ "completeTaskRequest:withSuccess:"
+ "completeTaskRequest:withSuccess:completionHandler:"
+ "completeWhenUserInactive"
+ "continuedProcessingActivityWithName:"
+ "continuedProcessingDeviceCapabilities:"
+ "continuedProcessingWrapper"
+ "cpuCycleConsumed"
+ "cpuTimeConsumed"
+ "currentAllocations:timeFilter:bgsqlData:"
+ "currentAllocations:timeFilter:bgsqlData:withHandler:"
+ "dataConsumed"
+ "diskIOConsumed"
+ "getContentionPenalties:"
+ "getContentionPenalties:handler:"
+ "getEligibilityTimelines:timeFilter:bgsqlData:"
+ "getEligibilityTimelines:timeFilter:bgsqlData:handler:"
+ "getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:"
+ "getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:handler:"
+ "getSchedulerEfficiencyMetrics:bgsqlData:"
+ "getSchedulerEfficiencyMetrics:bgsqlData:handler:"
+ "getSortedCandidateActivities:"
+ "getSortedCandidateActivities:handler:"
+ "hashArrayOfString:"
+ "haveNSecondsElapsed:"
+ "iconBundleIdentifier"
+ "indeedCPUIntensive"
+ "indeedMemoryIntensive"
+ "indeterminateProgress"
+ "initWithBudgetID:bundleID:endDate:extensionBundleID:inStack:pageID:startDate:timeUntilExpiration:viewID:"
+ "initWithBudgetID:extensionBundleID:isDASInitiated:refreshDate:refreshReason:"
+ "initWithStartDate:endDate:"
+ "initWithTitle:subtitle:iconBundleIdentifier:resources:"
+ "initWithTitle:subtitle:iconBundleIdentifier:resources:submissionStrategy:"
+ "initWithTitle:subtitle:resources:submissionStrategy:"
+ "initWithValues:eachWithDuration:startingAt:"
+ "initWithValues:forDurations:startingAt:"
+ "initWithValues:startDate:transitionDates:"
+ "integerValue"
+ "internalGroupNames"
+ "isEmergencySOSActivity"
+ "isIndeedIntensive"
+ "isPartOfCustomGroup"
+ "isRunning"
+ "lowLikelihoodPeriod"
+ "multi_group_support"
+ "orderedSetWithArray:"
+ "reportFeatureCheckpoint:forFeature:atDate:error:"
+ "reportFeatureCheckpoint:forFeature:atDate:withHandler:"
+ "reportProgressMetricsForIdentifier Failed: %@"
+ "reportProgressMetricsForIdentifier Failed: Server error %@"
+ "reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:"
+ "reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:withHandler:"
+ "reportThroughputMetricsForIdentifier Failed: %@"
+ "reportThroughputMetricsForIdentifier Failed: Server error %@"
+ "reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:"
+ "reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:withHandler:"
+ "requestsImmediateRuntime"
+ "requestsimmediateRuntime"
+ "resources"
+ "sendEvent:"
+ "setBilledEnergy:"
+ "setContinuedProcessingWrapper:"
+ "setCpuCycleConsumed:"
+ "setCpuTimeConsumed:"
+ "setDataConsumed:"
+ "setDiskIOConsumed:"
+ "setIconBundleIdentifier:"
+ "setIndeedCPUIntensive:"
+ "setIndeedMemoryIntensive:"
+ "setInternalGroupNames:"
+ "setRequestsImmediateRuntime:"
+ "setResources:"
+ "setStartedInIdle:"
+ "setStartedOnBattery:"
+ "setSubmissionStrategy:"
+ "setSubtitle:"
+ "setThermalLevelElevated:"
+ "setTitle:"
+ "setUninterruptibleDuration:"
+ "sortedArrayUsingSelector:"
+ "source"
+ "startedInIdle"
+ "startedOnBattery"
+ "string"
+ "submissionStrategy"
+ "subtitle"
+ "taskID"
+ "taskInstanceID"
+ "thermalLevelElevated"
+ "title"
+ "transitionDates"
+ "triggerScoreEvaluationAndRunActivities:"
+ "triggerScoreEvaluationAndRunActivities:handler:"
+ "uninterruptibleDuration"
+ "updateInternalGroups"
+ "v16@?0q8"
+ "v24@0:8@?<v@?q>16"
+ "v28@0:8@\"_DASActivity\"16B24"
+ "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSSet\"16@?<v@?B>24"
+ "v32@0:8@\"NSSet\"16q24"
+ "v36@0:8@\"_DASActivity\"16B24@?<v@?>28"
+ "v48@0:8Q16@\"NSDateInterval\"24@\"NSData\"32@?<v@?@\"NSDictionary\">40"
+ "v48@0:8Q16@24@32@?40"
+ "v48@0:8Q16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40"
+ "v48@0:8Q16Q24@32@?40"
+ "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48Q56@\"NSNumber\"64@?<v@?B@\"NSError\">72"
+ "v80@0:8@\"NSString\"16@\"NSString\"24Q32d40@\"NSNumber\"48Q56@\"NSNumber\"64@?<v@?B@\"NSError\">72"
+ "v80@0:8@16@24@32@40@48Q56@64@?72"
+ "v80@0:8@16@24Q32d40@48Q56@64@?72"
+ "valueAtDate:"
+ "values"
+ "valuesUntilEndDate:withIntervalDuration:"
- "@\"<_DKKnowledgeSaving>\""
- "Complete task request activity: %@"
- "Error in saving widget refresh entries: %@"
- "Error in saving widget views entries: %@"
- "Error obtaining clas status: %@"
- "T@\"<_DKKnowledgeSaving>\",&,N,V_store"
- "_store"
- "clientProvidedIconBundleIdentifier"
- "clientProvidedReason"
- "clientProvidedTitle"
- "completeTaskRequest:"
- "completeTaskRequest:completionHandler:"
- "eventStreamWithName:"
- "eventWithStream:startDate:endDate:identifierStringValue:metadata:"
- "knowledgeStoreWithDirectReadWriteAccess"
- "null"
- "reportFeatureCheckpoint:forFeature:error:"
- "reportFeatureCheckpoint:forFeature:withHandler:"
- "saveObjects:responseQueue:withCompletion:"
- "setANEIntensive:"
- "setClientProvidedReason:"
- "setClientProvidedTitle:"
- "setGPUIntensive:"
- "setStore:"
- "store"

```
