## DuetActivityScheduler

> `/System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler`

```diff

-2109.120.16.0.0
-  __TEXT.__text: 0x3b3e8
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x4480
-  __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0x159c
-  __TEXT.__cstring: 0x2884
-  __TEXT.__oslogstring: 0x3248
-  __TEXT.__unwind_info: 0x1338
-  __TEXT.__objc_classname: 0x74c
-  __TEXT.__objc_methname: 0xaa95
-  __TEXT.__objc_methtype: 0x1c29
-  __TEXT.__objc_stubs: 0x5fe0
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0xf38
-  __DATA_CONST.__objc_classlist: 0x138
+2463.0.0.502.1
+  __TEXT.__text: 0x3f134
+  __TEXT.__objc_methlist: 0x4990
+  __TEXT.__const: 0x208
+  __TEXT.__gcc_except_tab: 0x156c
+  __TEXT.__cstring: 0x413c
+  __TEXT.__oslogstring: 0x3306
+  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xf30
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2690
+  __DATA_CONST.__objc_selrefs: 0x2948
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x3a8
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x3aa0
-  __AUTH_CONST.__objc_const: 0x7778
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_arraydata: 0x180
+  __DATA_CONST.__got: 0x338
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x5080
+  __AUTH_CONST.__objc_const: 0x7f18
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x460
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x690
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x44c
-  __DATA.__data: 0xdf8
-  __DATA.__bss: 0x70
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x7d0
-  __DATA_DIRTY.__bss: 0x128
+  __DATA.__objc_ivar: 0x49c
+  __DATA.__data: 0xd68
+  __DATA.__bss: 0xe8
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AC426D8B-52B5-3709-9C61-36A275E6333A
-  Functions: 1580
-  Symbols:   5502
-  CStrings:  3382
+  UUID: 05F0A4A8-5AE9-356F-BA04-7AD8092E52EA
+  Functions: 1683
+  Symbols:   5841
+  CStrings:  1632
 
Symbols:
+ +[_DASActivity validateBGTaskRequestWithActivity:error:]
+ +[_DASActivityExpirationEvent supportsSecureCoding]
+ +[_DASActivityExpirationEvent unknownReasonsForActivities:]
+ +[_DASActivityLifecycleEvent defaultForActivities:]
+ +[_DASActivityLifecycleEvent defaultForExpirationEvents:]
+ +[_DASActivityLifecycleEvent defaultForSuspensionEvents:]
+ +[_DASActivityLifecycleEvent supportsSecureCoding]
+ +[_DASActivityScorecard _configForActivity:timelines:]
+ +[_DASActivityScorecard _formatter]
+ +[_DASActivityScorecard _formatter].cold.1
+ +[_DASActivityScorecard _lookupKey:inDict:]
+ +[_DASActivityScorecard _maxActivityDuration:timelines:]
+ +[_DASActivityScorecard _resultWithCategory:name:grade:detail:]
+ +[_DASActivityScorecard _resultWithCategory:name:grade:detail:evidence:]
+ +[_DASActivityScorecard _runtimeCount:timelines:overThreshold:validRuns:]
+ +[_DASActivityScorecard _scoreActivityIsBGST:timelines:activity:]
+ +[_DASActivityScorecard _scoreAdoptsFeatureCodes:activity:]
+ +[_DASActivityScorecard _scoreAvoidsCompletionWithMinimalProgress:timelines:]
+ +[_DASActivityScorecard _scoreAvoidsExcessiveYielding:timelines:]
+ +[_DASActivityScorecard _scoreAvoidsSubmissionAfterCompletion:timelines:]
+ +[_DASActivityScorecard _scoreCommonCriteriaAntiPatterns:timelines:activity:]
+ +[_DASActivityScorecard _scoreNoClientDisconnects:timelines:]
+ +[_DASActivityScorecard _scoreNoExcessiveSubmission:timelines:]
+ +[_DASActivityScorecard _scoreNoFailedToLaunch:timelines:]
+ +[_DASActivityScorecard _scoreNoFrequentCancellations:timelines:]
+ +[_DASActivityScorecard _scoreNoLaunchAcknowledgmentDenied:timelines:]
+ +[_DASActivityScorecard _scoreNoRegistrationTimeouts:timelines:]
+ +[_DASActivityScorecard _scoreNoSuboptimalConfiguration:timelines:]
+ +[_DASActivityScorecard _scoreReportsFeatureCheckpoints:activity:featureTimelines:fromListOfCheckpoints:withTitle:]
+ +[_DASActivityScorecard _scoreReportsFeatureUsageCheckpoints:activity:featureTimelines:]
+ +[_DASActivityScorecard _scoreReportsThroughputOrProgress:timelines:]
+ +[_DASActivityScorecard _scoreSuspendsImmediately:timelines:]
+ +[_DASActivityScorecard _scoreUsesWorkloadCategorization:timelines:activity:]
+ +[_DASActivityScorecard _scoreValidConfiguration:timelines:]
+ +[_DASActivityScorecard scorecardForActivity:timelines:activity:featureTimelines:]
+ +[_DASActivitySuspensionEvent supportsSecureCoding]
+ -[NSArray(_DASHashing) das_avalancheHash]
+ -[NSArray(_DASHashing) das_polynomialHash]
+ -[NSString(_DASHashing) das_avalancheHash]
+ -[NSString(_DASHashing) das_polynomialHash]
+ -[_DASActivity _computeSpecialCasedFromName:]
+ -[_DASActivity _hashFinalize:]
+ -[_DASActivity _hashMix:array:]
+ -[_DASActivity _hashMix:flag:]
+ -[_DASActivity _hashMix:string:]
+ -[_DASActivity _hashMix:value:]
+ -[_DASActivity cancelAndClearTimeoutBlocks]
+ -[_DASActivity endUptimeRawTime]
+ -[_DASActivity evaluations]
+ -[_DASActivity highLevelDenialReason]
+ -[_DASActivity isAVAssetDownloadActivity]
+ -[_DASActivity launchAcknowledgmentTimeoutBlock]
+ -[_DASActivity prerunningStuckTimeoutBlock]
+ -[_DASActivity primaryDomain]
+ -[_DASActivity purpose]
+ -[_DASActivity secondaryDomains]
+ -[_DASActivity setEndUptimeRawTime:]
+ -[_DASActivity setEvaluations:]
+ -[_DASActivity setHighLevelDenialReason:]
+ -[_DASActivity setLaunchAcknowledgmentTimeoutBlock:]
+ -[_DASActivity setPrerunningStuckTimeoutBlock:]
+ -[_DASActivity setPrimaryDomain:]
+ -[_DASActivity setPurpose:]
+ -[_DASActivity setSecondaryDomains:]
+ -[_DASActivity setStartUptimeRawTime:]
+ -[_DASActivity setSuspendRequestUptimeRawTime:]
+ -[_DASActivity setWakesCaused:]
+ -[_DASActivity specialCased]
+ -[_DASActivity startUptimeRawTime]
+ -[_DASActivity suspendRequestUptimeRawTime]
+ -[_DASActivity wakesCaused]
+ -[_DASActivityExpirationEvent .cxx_destruct]
+ -[_DASActivityExpirationEvent activity]
+ -[_DASActivityExpirationEvent description]
+ -[_DASActivityExpirationEvent encodeWithCoder:]
+ -[_DASActivityExpirationEvent expirationReasons]
+ -[_DASActivityExpirationEvent initWithActivity:expirationReason:]
+ -[_DASActivityExpirationEvent initWithActivity:expirationReasonRawValue:]
+ -[_DASActivityExpirationEvent initWithCoder:]
+ -[_DASActivityLifecycleEvent .cxx_destruct]
+ -[_DASActivityLifecycleEvent activity]
+ -[_DASActivityLifecycleEvent description]
+ -[_DASActivityLifecycleEvent encodeWithCoder:]
+ -[_DASActivityLifecycleEvent expiration]
+ -[_DASActivityLifecycleEvent initWithCoder:]
+ -[_DASActivityLifecycleEvent initWithExpiration:]
+ -[_DASActivityLifecycleEvent initWithSuspension:]
+ -[_DASActivityLifecycleEvent suspension]
+ -[_DASActivityLifecycleEvent type]
+ -[_DASActivitySuspensionEvent .cxx_destruct]
+ -[_DASActivitySuspensionEvent activity]
+ -[_DASActivitySuspensionEvent description]
+ -[_DASActivitySuspensionEvent encodeWithCoder:]
+ -[_DASActivitySuspensionEvent initWithActivity:]
+ -[_DASActivitySuspensionEvent initWithCoder:]
+ -[_DASContinuedProcessingWrapper isBackgroundedSubmissionContext]
+ -[_DASPlistParser detailLoggedActivities]
+ -[_DASPlistParser isDetailLoggedActivity:]
+ -[_DASPlistParser loadDetailLoggedActivities]
+ -[_DASPlistParser loadDetailLoggedActivities].cold.1
+ -[_DASPlistParser loadDetailLoggedActivities].cold.2
+ -[_DASPlistParser setDetailLoggedActivities:]
+ -[_DASScheduler acknowledgeTaskPause:]
+ -[_DASScheduler expireWithEvents:]
+ -[_DASScheduler frozenActivities]
+ -[_DASScheduler getDoItNowRuntimeLimits:]
+ -[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:error:]
+ -[_DASScheduler submitTaskRequest:completionHandler:]
+ -[_DASScheduler unregisterSystemTaskWithIdentifier:cancellationReason:completionHandler:]
+ -[_DASScheduler willHandleBGTaskLifecycleEvents:]
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table123
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table156
+ GCC_except_table189
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table226
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table235
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
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table302
+ GCC_except_table305
+ GCC_except_table308
+ GCC_except_table311
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table61
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table86
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table95
+ _NSInternalInconsistencyException
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$__DASActivityExpirationEvent
+ _OBJC_CLASS_$__DASActivityLifecycleEvent
+ _OBJC_CLASS_$__DASActivityScorecard
+ _OBJC_CLASS_$__DASActivitySuspensionEvent
+ _OBJC_IVAR_$__DASActivity._endUptimeRawTime
+ _OBJC_IVAR_$__DASActivity._evaluations
+ _OBJC_IVAR_$__DASActivity._highLevelDenialReason
+ _OBJC_IVAR_$__DASActivity._launchAcknowledgmentTimeoutBlock
+ _OBJC_IVAR_$__DASActivity._prerunningStuckTimeoutBlock
+ _OBJC_IVAR_$__DASActivity._primaryDomain
+ _OBJC_IVAR_$__DASActivity._purpose
+ _OBJC_IVAR_$__DASActivity._secondaryDomains
+ _OBJC_IVAR_$__DASActivity._specialCased
+ _OBJC_IVAR_$__DASActivity._startUptimeRawTime
+ _OBJC_IVAR_$__DASActivity._suspendRequestUptimeRawTime
+ _OBJC_IVAR_$__DASActivity._timeoutBlockLock
+ _OBJC_IVAR_$__DASActivity._wakesCaused
+ _OBJC_IVAR_$__DASActivityExpirationEvent._activity
+ _OBJC_IVAR_$__DASActivityExpirationEvent._expirationReasons
+ _OBJC_IVAR_$__DASActivityLifecycleEvent._expiration
+ _OBJC_IVAR_$__DASActivityLifecycleEvent._suspension
+ _OBJC_IVAR_$__DASActivityLifecycleEvent._type
+ _OBJC_IVAR_$__DASActivitySuspensionEvent._activity
+ _OBJC_IVAR_$__DASPlistParser._detailLoggedActivities
+ _OBJC_METACLASS_$__DASActivityExpirationEvent
+ _OBJC_METACLASS_$__DASActivityLifecycleEvent
+ _OBJC_METACLASS_$__DASActivityScorecard
+ _OBJC_METACLASS_$__DASActivitySuspensionEvent
+ __OBJC_$_CLASS_METHODS_NSArray(_DASInterning|_DASHashing|_DASEnumerable|_DASAdditions)
+ __OBJC_$_CLASS_METHODS__DASActivityExpirationEvent
+ __OBJC_$_CLASS_METHODS__DASActivityLifecycleEvent
+ __OBJC_$_CLASS_METHODS__DASActivityScorecard
+ __OBJC_$_CLASS_METHODS__DASActivitySuspensionEvent
+ __OBJC_$_CLASS_PROP_LIST__DASActivityExpirationEvent
+ __OBJC_$_CLASS_PROP_LIST__DASActivityLifecycleEvent
+ __OBJC_$_CLASS_PROP_LIST__DASActivitySuspensionEvent
+ __OBJC_$_INSTANCE_METHODS_NSArray(_DASInterning|_DASHashing|_DASEnumerable|_DASAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSString(_DASInterning|_DASHashing)
+ __OBJC_$_INSTANCE_METHODS__DASActivityExpirationEvent
+ __OBJC_$_INSTANCE_METHODS__DASActivityLifecycleEvent
+ __OBJC_$_INSTANCE_METHODS__DASActivitySuspensionEvent
+ __OBJC_$_INSTANCE_VARIABLES__DASActivityExpirationEvent
+ __OBJC_$_INSTANCE_VARIABLES__DASActivityLifecycleEvent
+ __OBJC_$_INSTANCE_VARIABLES__DASActivitySuspensionEvent
+ __OBJC_$_PROP_LIST__DASActivityExpirationEvent
+ __OBJC_$_PROP_LIST__DASActivityLifecycleEvent
+ __OBJC_$_PROP_LIST__DASActivitySuspensionEvent
+ __OBJC_CLASS_PROTOCOLS_$_NSArray(_DASInterning|_DASHashing|_DASEnumerable|_DASAdditions)
+ __OBJC_CLASS_PROTOCOLS_$__DASActivityExpirationEvent
+ __OBJC_CLASS_PROTOCOLS_$__DASActivityLifecycleEvent
+ __OBJC_CLASS_PROTOCOLS_$__DASActivitySuspensionEvent
+ __OBJC_CLASS_RO_$__DASActivityExpirationEvent
+ __OBJC_CLASS_RO_$__DASActivityLifecycleEvent
+ __OBJC_CLASS_RO_$__DASActivityScorecard
+ __OBJC_CLASS_RO_$__DASActivitySuspensionEvent
+ __OBJC_METACLASS_RO_$__DASActivityExpirationEvent
+ __OBJC_METACLASS_RO_$__DASActivityLifecycleEvent
+ __OBJC_METACLASS_RO_$__DASActivityScorecard
+ __OBJC_METACLASS_RO_$__DASActivitySuspensionEvent
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.425
+ ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.425.cold.1
+ ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.310
+ ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.310.cold.1
+ ___147-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:error:]_block_invoke
+ ___147-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.424
+ ___147-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.424.cold.1
+ ___147-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.cold.1
+ ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.327
+ ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.327.cold.1
+ ___25-[_DASScheduler policies]_block_invoke.380
+ ___27-[_DASScheduler allBudgets]_block_invoke.377
+ ___27-[_DASScheduler statistics]_block_invoke.371
+ ___31-[_DASScheduler runActivities:]_block_invoke.391
+ ___33-[_DASScheduler deferActivities:]_block_invoke.363
+ ___33-[_DASScheduler frozenActivities]_block_invoke
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.429
+ ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.429.cold.1
+ ___34-[_DASScheduler evaluatePolicies:]_block_invoke.381
+ ___34-[_DASScheduler expireWithEvents:]_block_invoke
+ ___34-[_DASScheduler inspect:criteria:]_block_invoke.374
+ ___35+[_DASActivityScorecard _formatter]_block_invoke
+ ___35-[_DASBMHistogramBuilder histogram]_block_invoke.70
+ ___35-[_DASScheduler currentPredictions]_block_invoke.368
+ ___35-[_DASScheduler submitTaskRequest:]_block_invoke.396
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.407
+ ___35-[_DASScheduler updateOngoingTask:]_block_invoke.407.cold.1
+ ___36-[_DASScheduler submittedActivities]_block_invoke.365
+ ___37-[_DASScheduler pauseWithParameters:]_block_invoke.388
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.399
+ ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.399.cold.1
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.433
+ ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.433.cold.1
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.434
+ ___40-[_DASScheduler getContentionPenalties:]_block_invoke.434.cold.1
+ ___41-[_DASScheduler activityForActivityName:]_block_invoke.450
+ ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.389
+ ___41-[_DASScheduler delayedRunningActivities]_block_invoke.367
+ ___41-[_DASScheduler getDoItNowRuntimeLimits:]_block_invoke
+ ___41-[_DASScheduler getDoItNowRuntimeLimits:]_block_invoke.430
+ ___41-[_DASScheduler getDoItNowRuntimeLimits:]_block_invoke.cold.1
+ ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.378
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.442
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.442.cold.1
+ ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.442.cold.2
+ ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.339
+ ___42-[_DASScheduler runProceedableActivities:]_block_invoke.382
+ ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.384
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.443
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.443.cold.1
+ ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.443.cold.2
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.441
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.441.cold.1
+ ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.441.cold.2
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.448
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.448.cold.1
+ ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.448.cold.2
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.361
+ ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.361.cold.1
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.387
+ ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.387.cold.1
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.428
+ ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.428.cold.1
+ ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.375
+ ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.390
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.408
+ ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.408.cold.1
+ ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.383
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.398
+ ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.398.cold.1
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.406
+ ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.406.cold.1
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.413
+ ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.413.cold.1
+ ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.386
+ ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.372
+ ___50-[_DASWidgetRefreshScheduler sanitizeWidgetViews:]_block_invoke.243
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.385
+ ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.385.cold.1
+ ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.376
+ ___53-[_DASScheduler submitTaskRequest:completionHandler:]_block_invoke
+ ___53-[_DASScheduler submitTaskRequest:completionHandler:]_block_invoke.397
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.423
+ ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.423.cold.1
+ ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.409
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.422
+ ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.422.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.449
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.449.cold.1
+ ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.449.cold.2
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.370
+ ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.370.cold.1
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.431
+ ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.431.cold.1
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.439
+ ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.439.cold.1
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.435
+ ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.435.cold.1
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.426
+ ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.426.cold.1
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.436
+ ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.436.cold.1
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.432
+ ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.432.cold.1
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.427
+ ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.427.cold.1
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.437
+ ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.437.cold.1
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.444
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.444.cold.1
+ ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.444.cold.2
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.445
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.445.cold.1
+ ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.445.cold.2
+ ___65+[_DASActivityScorecard _scoreAvoidsExcessiveYielding:timelines:]_block_invoke
+ ___65+[_DASActivityScorecard _scoreNoFrequentCancellations:timelines:]_block_invoke
+ ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.411
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.446
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.446.cold.1
+ ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.446.cold.2
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.421
+ ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.421.cold.1
+ ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.438
+ ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.438.cold.1
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.447
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.447.cold.1
+ ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.447.cold.2
+ ___73+[_DASActivityScorecard _scoreAvoidsSubmissionAfterCompletion:timelines:]_block_invoke
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.412
+ ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.412.cold.1
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.440
+ ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.440.cold.1
+ ___77+[_DASActivityScorecard _scoreAvoidsCompletionWithMinimalProgress:timelines:]_block_invoke
+ ___77+[_DASActivityScorecard _scoreAvoidsCompletionWithMinimalProgress:timelines:]_block_invoke_2
+ ___77+[_DASActivityScorecard _scoreAvoidsCompletionWithMinimalProgress:timelines:]_block_invoke_3
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.414
+ ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.414.cold.1
+ ___89-[_DASScheduler unregisterSystemTaskWithIdentifier:cancellationReason:completionHandler:]_block_invoke
+ ___89-[_DASScheduler unregisterSystemTaskWithIdentifier:cancellationReason:completionHandler:]_block_invoke.cold.1
+ ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
+ ___block_literal_global.144
+ ___block_literal_global.242
+ ___block_literal_global.245
+ ___block_literal_global.269
+ ___block_literal_global.313
+ ___block_literal_global.324
+ ___block_literal_global.330
+ ___block_literal_global.393
+ ___block_literal_global.482
+ ___block_literal_global.489
+ ___block_literal_global.67
+ __formatter.formatter
+ __formatter.onceToken
+ _dispatch_block_cancel
+ _highLevelDenialReasonStringFromMask
+ _objc_claimAutoreleasedReturnValue
+ _objc_exception_throw
+ _objc_msgSend$_computeSpecialCasedFromName:
+ _objc_msgSend$_configForActivity:timelines:
+ _objc_msgSend$_formatter
+ _objc_msgSend$_hashFinalize:
+ _objc_msgSend$_hashMix:array:
+ _objc_msgSend$_hashMix:flag:
+ _objc_msgSend$_hashMix:string:
+ _objc_msgSend$_hashMix:value:
+ _objc_msgSend$_lookupKey:inDict:
+ _objc_msgSend$_maxActivityDuration:timelines:
+ _objc_msgSend$_resultWithCategory:name:grade:detail:
+ _objc_msgSend$_resultWithCategory:name:grade:detail:evidence:
+ _objc_msgSend$_scoreActivityIsBGST:timelines:activity:
+ _objc_msgSend$_scoreAdoptsFeatureCodes:activity:
+ _objc_msgSend$_scoreAvoidsCompletionWithMinimalProgress:timelines:
+ _objc_msgSend$_scoreAvoidsExcessiveYielding:timelines:
+ _objc_msgSend$_scoreAvoidsSubmissionAfterCompletion:timelines:
+ _objc_msgSend$_scoreCommonCriteriaAntiPatterns:timelines:activity:
+ _objc_msgSend$_scoreNoClientDisconnects:timelines:
+ _objc_msgSend$_scoreNoExcessiveSubmission:timelines:
+ _objc_msgSend$_scoreNoFailedToLaunch:timelines:
+ _objc_msgSend$_scoreNoFrequentCancellations:timelines:
+ _objc_msgSend$_scoreNoLaunchAcknowledgmentDenied:timelines:
+ _objc_msgSend$_scoreNoRegistrationTimeouts:timelines:
+ _objc_msgSend$_scoreNoSuboptimalConfiguration:timelines:
+ _objc_msgSend$_scoreReportsFeatureCheckpoints:activity:featureTimelines:fromListOfCheckpoints:withTitle:
+ _objc_msgSend$_scoreReportsFeatureUsageCheckpoints:activity:featureTimelines:
+ _objc_msgSend$_scoreReportsThroughputOrProgress:timelines:
+ _objc_msgSend$_scoreSuspendsImmediately:timelines:
+ _objc_msgSend$_scoreUsesWorkloadCategorization:timelines:activity:
+ _objc_msgSend$_scoreValidConfiguration:timelines:
+ _objc_msgSend$activity
+ _objc_msgSend$clientName
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$currentLocale
+ _objc_msgSend$das_avalancheHash
+ _objc_msgSend$das_polynomialHash
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$defaultForExpirationEvents:
+ _objc_msgSend$evaluations
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$expiration
+ _objc_msgSend$expirationReasons
+ _objc_msgSend$expireWithEvents:
+ _objc_msgSend$featureCodes
+ _objc_msgSend$frozenActivitiesWithHandler:
+ _objc_msgSend$getDoItNowRuntimeLimits:handler:
+ _objc_msgSend$highLevelDenialReason
+ _objc_msgSend$initWithActivity:
+ _objc_msgSend$initWithActivity:expirationReason:
+ _objc_msgSend$initWithExpiration:
+ _objc_msgSend$initWithSuspension:
+ _objc_msgSend$loadDetailLoggedActivities
+ _objc_msgSend$null
+ _objc_msgSend$primaryDomain
+ _objc_msgSend$purpose
+ _objc_msgSend$reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:withHandler:
+ _objc_msgSend$scheduler:handleLifecycleEvents:
+ _objc_msgSend$secondaryDomains
+ _objc_msgSend$setEvaluations:
+ _objc_msgSend$setHighLevelDenialReason:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$setLocalizedDateFormatFromTemplate:
+ _objc_msgSend$setStartUptimeRawTime:
+ _objc_msgSend$setStartedInIdle:
+ _objc_msgSend$setStartedOnBattery:
+ _objc_msgSend$setSuspendRequestUptimeRawTime:
+ _objc_msgSend$setWakesCaused:
+ _objc_msgSend$startUptimeRawTime
+ _objc_msgSend$startedInIdle
+ _objc_msgSend$startedOnBattery
+ _objc_msgSend$string
+ _objc_msgSend$suspendRequestUptimeRawTime
+ _objc_msgSend$suspension
+ _objc_msgSend$type
+ _objc_msgSend$unknownReasonsForActivities:
+ _objc_msgSend$unregisterSystemTaskWithIdentifier:cancellationReason:completionHandler:
+ _objc_msgSend$wakesCaused
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x8
- +[_DASActivity convertUUIDToUint64:]
- +[_DASActivity validateBGTaskRequestWithActivity:]
- -[_DASActivity hashArrayOfString:]
- -[_DASActivity hashString:]
- -[_DASScheduler evaluateAllActivitiesWithHandle:]
- -[_DASScheduler getDeviceConditionTimelines:bgsqlData:]
- -[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]
- -[_DASScheduler willExpireBGTaskActivities:]
- GCC_except_table102
- GCC_except_table106
- GCC_except_table109
- GCC_except_table112
- GCC_except_table115
- GCC_except_table116
- GCC_except_table118
- GCC_except_table124
- GCC_except_table130
- GCC_except_table136
- GCC_except_table139
- GCC_except_table157
- GCC_except_table186
- GCC_except_table216
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
- GCC_except_table298
- GCC_except_table301
- GCC_except_table304
- GCC_except_table307
- GCC_except_table310
- GCC_except_table313
- GCC_except_table348
- GCC_except_table349
- GCC_except_table65
- GCC_except_table68
- GCC_except_table71
- GCC_except_table74
- GCC_except_table77
- GCC_except_table84
- GCC_except_table87
- GCC_except_table90
- GCC_except_table93
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSString_$__DASInterning
- __OBJC_$_CLASS_METHODS_NSArray(_DASInterning|_DASEnumerable|_DASAdditions)
- __OBJC_$_INSTANCE_METHODS_NSArray(_DASInterning|_DASEnumerable|_DASAdditions)
- __OBJC_CLASS_PROTOCOLS_$_NSArray(_DASInterning|_DASEnumerable|_DASAdditions)
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.415
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.415.cold.1
- ___128-[_DASScheduler reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:]_block_invoke.cold.1
- ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.416
- ___132-[_DASScheduler reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:]_block_invoke.416.cold.1
- ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.311
- ___138-[_DASWidgetRefreshScheduler createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.311.cold.1
- ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.328
- ___188-[_DASWidgetRefreshScheduler createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:]_block_invoke.328.cold.1
- ___25-[_DASScheduler policies]_block_invoke.371
- ___27-[_DASScheduler allBudgets]_block_invoke.368
- ___27-[_DASScheduler statistics]_block_invoke.362
- ___31-[_DASScheduler runActivities:]_block_invoke.383
- ___33-[_DASScheduler deferActivities:]_block_invoke.354
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.420
- ___33-[_DASScheduler getRuntimeLimit:]_block_invoke.420.cold.1
- ___34-[_DASScheduler evaluatePolicies:]_block_invoke.372
- ___34-[_DASScheduler inspect:criteria:]_block_invoke.365
- ___35-[_DASBMHistogramBuilder histogram]_block_invoke.71
- ___35-[_DASScheduler currentPredictions]_block_invoke.359
- ___35-[_DASScheduler submitTaskRequest:]_block_invoke.388
- ___35-[_DASScheduler suspendActivities:]_block_invoke
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.398
- ___35-[_DASScheduler updateOngoingTask:]_block_invoke.398.cold.1
- ___36-[_DASScheduler submittedActivities]_block_invoke.356
- ___37-[_DASScheduler pauseWithParameters:]_block_invoke.380
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.390
- ___38-[_DASScheduler cancelAllTaskRequests]_block_invoke.390.cold.1
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.423
- ___40-[_DASScheduler getConditionsPenalties:]_block_invoke.423.cold.1
- ___40-[_DASScheduler getContentionPenalties:]_block_invoke.424
- ___40-[_DASScheduler getContentionPenalties:]_block_invoke.424.cold.1
- ___41-[_DASScheduler activityForActivityName:]_block_invoke.441
- ___41-[_DASScheduler addPauseExceptParameter:]_block_invoke.381
- ___41-[_DASScheduler delayedRunningActivities]_block_invoke.358
- ___42-[_DASScheduler balanceForBudgetWithName:]_block_invoke.369
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.433
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.433.cold.1
- ___42-[_DASScheduler getBuddyEvents:bgsqlData:]_block_invoke.433.cold.2
- ___42-[_DASScheduler initWithListenerEndpoint:]_block_invoke.330
- ___42-[_DASScheduler runProceedableActivities:]_block_invoke.374
- ___43-[_DASScheduler activityContainsOverrides:]_block_invoke.376
- ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.434
- ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.434.cold.1
- ___43-[_DASScheduler getRebootEvents:bgsqlData:]_block_invoke.434.cold.2
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.432
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.432.cold.1
- ___46-[_DASScheduler getInstallTimeline:bgsqlData:]_block_invoke.432.cold.2
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.439
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.439.cold.1
- ___46-[_DASScheduler getSortedCandidateActivities:]_block_invoke.439.cold.2
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.352
- ___46-[_DASScheduler submitActivity:inGroup:error:]_block_invoke.352.cold.1
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.379
- ___46-[_DASScheduler submitRateLimitConfiguration:]_block_invoke.379.cold.1
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.419
- ___47-[_DASScheduler getLimiterResponseForActivity:]_block_invoke.419.cold.1
- ___47-[_DASScheduler queryStatusOfResultIdentifier:]_block_invoke.366
- ___47-[_DASScheduler runActivitiesWithDelayedStart:]_block_invoke.382
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.399
- ___47-[_DASScheduler updateProgress:forOngoingTask:]_block_invoke.399.cold.1
- ___48-[_DASScheduler blockingPoliciesWithParameters:]_block_invoke.375
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.389
- ___49-[_DASScheduler cancelTaskRequestWithIdentifier:]_block_invoke.389.cold.1
- ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.397
- ___49-[_DASScheduler completeTaskRequest:withSuccess:]_block_invoke.397.cold.1
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.373
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.373.cold.1
- ___49-[_DASScheduler evaluateAllActivitiesWithHandle:]_block_invoke.cold.1
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.404
- ___50-[_DASScheduler completeSystemTaskWithIdentifier:]_block_invoke.404.cold.1
- ___50-[_DASScheduler enableTaskRegistryMode:processes:]_block_invoke.378
- ___50-[_DASScheduler resetFastPassActivities:resetAll:]_block_invoke.363
- ___50-[_DASWidgetRefreshScheduler sanitizeWidgetViews:]_block_invoke.244
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.377
- ___51-[_DASScheduler enterTestModeWithParameters:reset:]_block_invoke.377.cold.1
- ___51-[_DASScheduler queryDependenciesOfTaskIdentifier:]_block_invoke.367
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.414
- ___54-[_DASScheduler reportCustomCheckpoint:forTask:error:]_block_invoke.414.cold.1
- ___55-[_DASScheduler continuedProcessingDeviceCapabilities:]_block_invoke.400
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.428
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.428.cold.1
- ___55-[_DASScheduler getDeviceConditionTimelines:bgsqlData:]_block_invoke.cold.1
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.413
- ___55-[_DASScheduler reportSystemWorkload:ofCategory:error:]_block_invoke.413.cold.1
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.440
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.440.cold.1
- ___56-[_DASScheduler triggerScoreEvaluationAndRunActivities:]_block_invoke.440.cold.2
- ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.361
- ___57-[_DASScheduler currentAllocations:timeFilter:bgsqlData:]_block_invoke.361.cold.1
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.421
- ___57-[_DASScheduler getElapsedRuntimes:timeFilter:bgsqlData:]_block_invoke.421.cold.1
- ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.430
- ___57-[_DASScheduler getSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.430.cold.1
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.425
- ___58-[_DASScheduler getFeatureTimelines:timeFilter:bgsqlData:]_block_invoke.425.cold.1
- ___58-[_DASScheduler setMinimumBackgroundFetchInterval:forApp:]_block_invoke
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.417
- ___59-[_DASScheduler deleteLimitForActivity:forLimiterWithName:]_block_invoke.417.cold.1
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.426
- ___59-[_DASScheduler getActivityTimelines:timeFilter:bgsqlData:]_block_invoke.426.cold.1
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.422
- ___59-[_DASScheduler getEstimatedRuntimes:timeFilter:bgsqlData:]_block_invoke.422.cold.1
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.418
- ___60-[_DASScheduler updateLimit:forActivity:forLimiterWithName:]_block_invoke.418.cold.1
- ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.427
- ___62-[_DASScheduler getEligibilityTimelines:timeFilter:bgsqlData:]_block_invoke.427.cold.1
- ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.435
- ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.435.cold.1
- ___62-[_DASScheduler getTaskDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.435.cold.2
- ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.436
- ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.436.cold.1
- ___64-[_DASScheduler getTaskLatencyProjections:timeFilter:bgsqlData:]_block_invoke.436.cold.2
- ___65-[_DASScheduler acknowledgeSystemTaskLaunchWithIdentifier:error:]_block_invoke.402
- ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.437
- ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.437.cold.1
- ___65-[_DASScheduler getFeatureDependencyGraphs:timeFilter:bgsqlData:]_block_invoke.437.cold.2
- ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.412
- ___65-[_DASScheduler reportFeatureCheckpoint:forFeature:atDate:error:]_block_invoke.412.cold.1
- ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.429
- ___66-[_DASScheduler getSystemConditionsTimeline:timeFilter:bgsqlData:]_block_invoke.429.cold.1
- ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.438
- ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.438.cold.1
- ___67-[_DASScheduler getFeatureLatencyProjections:timeFilter:bgsqlData:]_block_invoke.438.cold.2
- ___70-[_DASScheduler unregisterSystemTaskWithIdentifier:completionHandler:]_block_invoke
- ___70-[_DASScheduler unregisterSystemTaskWithIdentifier:completionHandler:]_block_invoke.cold.1
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.403
- ___74-[_DASScheduler acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:]_block_invoke.403.cold.1
- ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.431
- ___75-[_DASScheduler getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:]_block_invoke.431.cold.1
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.405
- ___82-[_DASScheduler resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:]_block_invoke.405.cold.1
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
- ___block_literal_global.243
- ___block_literal_global.385
- ___block_literal_global.419
- ___block_literal_global.426
- ___block_literal_global.68
- _objc_msgSend$evaluateAllActivities:handler:
- _objc_msgSend$getDeviceConditionTimelines:bgsqlData:handler:
- _objc_msgSend$getUUIDBytes:
- _objc_msgSend$hashArrayOfString:
- _objc_msgSend$hashString:
- _objc_msgSend$reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:withHandler:
- _objc_msgSend$scheduler:willExpireActivities:
- _objc_msgSend$setMinimumBackgroundFetchInterval:forApp:
- _objc_msgSend$unregisterSystemTaskWithIdentifier:completionHandler:
CStrings:
+ "\n    Last offending completion: %@"
+ "\n  Average runtime before yielding: %.1f seconds"
+ "\n  Last excessive yield-resubmit: %@"
+ " and "
+ " and is intensive"
+ " and max duration is %.1f seconds (>= 10 minutes)"
+ " and max duration is %.4f seconds (< 10 minutes)"
+ "%d"
+ "%lu rate-limited submission(s) detected"
+ ","
+ ", "
+ ", OnBattery Runtime State: %d"
+ ", so categorization is not required"
+ "-empty-"
+ "Activity Checkpoints"
+ "Activity does not report progress or throughput"
+ "Activity does not use workload categorization (missing Purpose or PrimaryDomain)"
+ "Activity does not use workload categorization, but is not intensive"
+ "Activity has adopted feature code(s): %@"
+ "Activity is not intensive."
+ "Activity is scheduled with another framework: %@"
+ "Activity reports "
+ "Activity uses BackgroundSystemTasks"
+ "Activity uses XPC Activity instead of BackgroundSystemTasks"
+ "Activity uses workload categorization with "
+ "ActivityExpirationEvent(activity: %@, reasons: %@)"
+ "ActivitySuspensionEvent(activity: %@)"
+ "Adopts feature codes"
+ "Avoids completion with minimal progress"
+ "Avoids excessive yielding"
+ "Avoids submission-after-completion pattern"
+ "Battery Life,"
+ "Can't load allowlist plist for DetailLoggedActivities"
+ "Cell Data,"
+ "CheckpointState"
+ "Client failed to suspend within threshold %lu time(s) out of %lu expiry request(s)"
+ "Client suspended immediately in all %lu expiry request(s)"
+ "Client took %.0fs to respond to %lu suspension request(s)"
+ "ClientName"
+ "Configurations"
+ "Continued processing task is missing required %@."
+ "Couldn't find %@ in the list of started activities"
+ "DASRequestedExpiry checkpoints: %lu, FailedToExpire checkpoints: %lu"
+ "DetailLoggedActivities"
+ "DetailLoggedActivities key missing or not an array"
+ "Device Activity,"
+ "Device Idle,"
+ "Disk Space,"
+ "Error getting doItNow runtime limits for %@: %@"
+ "FailedToExpire: %lu, DASRequestedExpiry: %lu"
+ "Feature Checkponts"
+ "File Protection,"
+ "First progress report after completion was %.1f%% (within 12 hours)"
+ "Found %lu cancellation(s) within 5 minutes of submission (before task started) out of %lu total submission(s) (%.1f%%) - below 10%% threshold"
+ "Found %lu cancellation(s) within 5 minutes of submission (before task started) out of %lu total submission(s) (%.1f%%) - exceeds 10%% threshold\n    Last cancellation: %@"
+ "Found %lu client disconnect(s) - client process was torn down\n    Last disconnect: %@"
+ "Found %lu excessive yielding cycle(s) over %.1f day(s) (average: %.1f cycles/day) - below threshold of 4 cycles/day"
+ "Found %lu excessive yielding cycle(s) over %.1f day(s) (average: %.1f cycles/day) - exceeds threshold of 4 cycles/day"
+ "Found %lu failed launch attempt(s)\n    Last failed launch: %@"
+ "Found %lu invalid configuration(s) - submission was rejected\n    Last invalid configuration: %@"
+ "Found %lu launch acknowledgment denial(s) - client denied the launch request\n    Last denial: %@"
+ "Found %lu registration timeout(s)\n    Last timeout: %@"
+ "Found %lu submission(s) within 5 minutes of completion out of %lu total submission(s) (%.1f%%)\n    Last submission-after-completion: %@"
+ "Found %lu submission(s) within 5 minutes of completion out of %lu total submission(s) (%.1f%%) - below 10%% threshold"
+ "Found %lu suboptimal configuration(s) - configuration should be improved\n    Last suboptimal configuration: %@"
+ "Found progress report of %.1f%% within 4 hours after completion"
+ "Game Mode,"
+ "Identifier"
+ "Interval"
+ "IsIntensive"
+ "LDM,"
+ "LPM,"
+ "Last failed: %@"
+ "Last rate-limited: %@"
+ "Launch Reason"
+ "Missing Field"
+ "NW Availability,"
+ "NW Conditions,"
+ "No checkpoint data available for activity"
+ "No client disconnects"
+ "No client disconnects detected"
+ "No criteria anti-patterns"
+ "No excessive submissions"
+ "No excessive yielding cycles detected"
+ "No expiry requests found in activity timeline"
+ "No failed launch attempts detected"
+ "No failed launches"
+ "No feature checkpoints in list %@ reported for activity."
+ "No feature codes associated with activity so feature usage cannot be determined."
+ "No feature codes found."
+ "No frequent cancellations after submission"
+ "No frequent cancellations detected"
+ "No instances of completion with minimal progress detected across %lu completion(s)"
+ "No invalid configuration issues detected"
+ "No launch acknowledgment denials"
+ "No launch acknowledgment denials detected"
+ "No progress or throughput data available to evaluate"
+ "No rate-limited submissions detected"
+ "No registration timeouts"
+ "No registration timeouts detected"
+ "No submission checkpoints found in activity timeline"
+ "No submissions within 5 minutes of completion detected"
+ "No suboptimal configuration"
+ "No suboptimal configuration issues detected"
+ "No task completions found in timeline"
+ "No valid feature checkpoints reported for feature codes associated with activity."
+ "Plugin State,"
+ "PrimaryDomain"
+ "PrimaryDomain: %ld"
+ "Progress Checkpoints"
+ "Purpose"
+ "Purpose: %ld"
+ "Rate-limited submissions: %lu"
+ "Received expiration events: %@"
+ "Reports feature checkpoints"
+ "Reports feature usage checkpoints"
+ "Reports throughput or progress"
+ "Requires live activity data (use dastool scorecard for full evaluation)"
+ "Runtime Expired,"
+ "STARTED: %@"
+ "STARTED: %{public}@"
+ "Submitting task request activity with completion handler: %@"
+ "Summary"
+ "Suspends immediately when asked"
+ "SuspensionDelayCount"
+ "SuspensionReason"
+ "SuspensionReason: %@"
+ "System Load,"
+ "Task Identifier"
+ "Task identifier exceeds maximum length of 128 characters (length: %lu)."
+ "Task identifier is empty."
+ "Task is intensive and configured to run every %d seconds"
+ "Task is intensive and non-repeating"
+ "Thermals,"
+ "Throughput Reports"
+ "Throughput report shows %.0f items within 4 hours after completion (median was %.0f)"
+ "Timeline span too short to calculate daily average"
+ "TotalSuspensionDelay"
+ "TotalSuspensionDelay: %.1fs"
+ "TotalSuspensionDelay: %.1fs across %lu request(s)"
+ "Totals"
+ "Transparency"
+ "Unable to determine scheduling framework"
+ "Unable to find activity"
+ "Unable to retrieve timeline data for activity"
+ "Unhandled case in _DASActivityLifecycleEvent"
+ "Unsupported or missing launch reason for task."
+ "Uses BackgroundSystemTasks"
+ "Uses Workload Categorization"
+ "Valid configuration"
+ "Valid feature checkpoint %@ reported for %@"
+ "Verify: dastool compute activityTimeline %@ --last 48"
+ "Will handle BGTask lifecycle events: %@"
+ "YY-MM-dd HH:mm:ss Z"
+ "_DASActivityLifecycleEvent(type: expiration, expiration: %@)"
+ "_DASActivityLifecycleEvent(type: suspension, suspension: %@)"
+ "category"
+ "com.apple.assetsd.backgroundjobservice.discretionaryresourceduration"
+ "com.apple.assetsd.backgroundjobservice.urgentresource"
+ "com.apple.cloudphotod.sync.discretionary"
+ "detail"
+ "epoch"
+ "evaluations"
+ "evidence"
+ "expiration"
+ "expireWithEvents: %@ activities were not running: %@"
+ "failed"
+ "grade"
+ "highLevelSuspension"
+ "itemCount"
+ "na"
+ "nil"
+ "nsurl-av"
+ "passed"
+ "primaryDomain"
+ "progress (%lu checkpoint(s))"
+ "purpose"
+ "q24@?0@\"NSNumber\"8@\"NSNumber\"16"
+ "reasonOptions"
+ "secondaryDomains"
+ "suspension"
+ "throughput (%lu report(s))"
+ "title and subtitle"
+ "type"
+ "wakesCaused"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<_CDContext>\""
- "@\"<_CDLocalContext>\""
- "@\"<_DASActivityBackgroundTasksSchedulerDelegate>\""
- "@\"<_DASExtensionRunner>\""
- "@\"BPSPublisher\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"24@0:8@\"NSDictionary\"16"
- "@\"NSArray\"24@0:8@\"NSSet\"16"
- "@\"NSArray\"24@0:8@\"NSString\"16"
- "@\"NSArray\"28@0:8@\"NSMutableArray\"16B24"
- "@\"NSArray\"32@0:8@\"NSDateInterval\"16@\"NSData\"24"
- "@\"NSArray\"32@0:8@\"NSString\"16@\"NSString\"24"
- "@\"NSArray\"40@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32"
- "@\"NSCountedSet\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"24@0:8@\"NSOrderedSet\"16"
- "@\"NSDictionary\"24@0:8@\"NSSet\"16"
- "@\"NSDictionary\"24@0:8@\"NSString\"16"
- "@\"NSDictionary\"32@0:8@\"NSDateInterval\"16@\"NSData\"24"
- "@\"NSDictionary\"40@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32"
- "@\"NSDictionary\"40@0:8Q16@\"NSDateInterval\"24@\"NSData\"32"
- "@\"NSError\"24@0:8@\"_DASActivity\"16"
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableDictionary\"16@0:8"
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSProgress\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSUserDefaults\""
- "@\"NSXPCConnection\""
- "@\"NSXPCListenerEndpoint\""
- "@\"_CDContextualKeyPath\""
- "@\"_DASActivity\""
- "@\"_DASActivity\"24@0:8@\"NSString\"16"
- "@\"_DASAssertion\""
- "@\"_DASBMMinimumSpanConfiguration\""
- "@\"_DASContinuedProcessingWrapper\""
- "@\"_DASExtensionRemoteContext\""
- "@\"_DASFastPass\""
- "@\"_DASFileProtection\""
- "@\"_DASHistogram\"16@0:8"
- "@\"_DASScheduler\""
- "@\"_DASSubmissionManager\""
- "@\"_DASSubmissionRateLimiter\""
- "@104@0:8@16@24@32@40q48q56q64{?=[8I]}72"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8Q16d24"
- "@36@0:8@16@24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16d24@32"
- "@40@0:8Q16@24@32"
- "@40@0:8d16@?24@?32"
- "@40@0:8d16q24q32"
- "@44@0:8@16@24@32B40"
- "@48@0:8@16@24@?32@?40"
- "@48@0:8Q16@24d32@40"
- "@52@0:8@16@24@32@40B48"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24@32@40q48"
- "@56@0:8@16@24@32@?40@?48"
- "@56@0:8@16Q24Q32@40@48"
- "@64@0:8@16@24@32@40@48@?56"
- "@64@0:8@16Q24Q32@40@48@56"
- "@64@0:8@16Q24Q32B40B44@48@56"
- "@68@0:8@16Q24Q32Q40B48@52@60"
- "@72@0:8@16@24@32@40@48@56@64"
- "@72@0:8@16Q24@32@40Q48@56@64"
- "@80@0:8@16@24@32@40@48@56@64@?72"
- "@80@0:8@16Q24@32@40@48Q56@64@72"
- "@88@0:8@16@24q32q40q48{?=[8I]}56"
- "@?"
- "@?16@0:8"
- "App"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSArray\"16"
- "B24@0:8@\"NSFileHandle\"16"
- "B24@0:8@\"NSSet\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"_DASActivity\"16"
- "B24@0:8@16"
- "B24@0:8d16"
- "B24@0:8q16"
- "B28@0:8B16@\"NSSet\"20"
- "B28@0:8B16@20"
- "B32@0:8@\"NSString\"16@24"
- "B32@0:8@\"NSString\"16^@24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@\"_DASActivity\"16@\"NSArray\"24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8@16^B24"
- "B32@0:8Q16@24"
- "B32@0:8Q16@?24"
- "B40@0:8@\"_DASActivity\"16@\"_DASActivityGroup\"24^@32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16Q24@32"
- "B40@0:8@16Q24^B32"
- "B40@0:8Q16@\"NSString\"24^@32"
- "B40@0:8Q16@24^@32"
- "B40@0:8Q16Q24^@32"
- "B40@0:8d16@\"NSString\"24@\"NSString\"32"
- "B40@0:8d16@24@32"
- "B44@0:8@16Q24B32^d36"
- "B48@0:8Q16Q24@\"NSDate\"32^@40"
- "B48@0:8Q16Q24@32^@40"
- "B80@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48Q56@\"NSNumber\"64^@72"
- "B80@0:8@\"NSString\"16@\"NSString\"24Q32d40@\"NSNumber\"48Q56@\"NSNumber\"64^@72"
- "B80@0:8@16@24@32@40@48Q56@64^@72"
- "B80@0:8@16@24Q32d40@48Q56@64^@72"
- "C16@0:8"
- "DASAdditions"
- "Dastool"
- "Error evaluating all activities"
- "Error evaluating all activities: %@"
- "Error setting minimum fetch interval: %@"
- "I"
- "I16@0:8"
- "InFocus"
- "NSCoding"
- "NSCopying"
- "NSExtensionRequestHandling"
- "NSFastEnumeration"
- "NSMutableCopying"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q24@0:8Q16"
- "Q40@0:8^{?=Q^@^Q[5Q]}16^@24Q32"
- "Refresh"
- "STARTING: %@"
- "STARTING: %{public}@"
- "T#,R"
- "T@\"<_CDContext>\",&,N,V_context"
- "T@\"<_CDLocalContext>\",&,N,V_context"
- "T@\"<_DASActivityBackgroundTasksSchedulerDelegate>\",W,N,V_backgroundTaskSchedulerDelegate"
- "T@\"<_DASExtensionRunner>\",&,N,V_runner"
- "T@\"BPSPublisher\",&,N,V_publisher"
- "T@\"NSArray\",&,N,V_involvedProcesses"
- "T@\"NSArray\",&,N,V_rateLimits"
- "T@\"NSArray\",&,N,V_relatedApplications"
- "T@\"NSArray\",&,N,V_schedulerRecommendedApplications"
- "T@\"NSArray\",&,V_previousExclusiveIdentifiers"
- "T@\"NSArray\",C,N,V_featureCodes"
- "T@\"NSArray\",C,N,V_processingTaskIdentifiers"
- "T@\"NSArray\",R,N,V_transitionDates"
- "T@\"NSArray\",R,N,V_values"
- "T@\"NSCountedSet\",&,N,V_penaltyTracker"
- "T@\"NSCountedSet\",&,N,V_submittedActivityTracker"
- "T@\"NSCountedSet\",R,C,N,V_counts"
- "T@\"NSDate\",&,N"
- "T@\"NSDate\",&,N,V_refreshAfterDate"
- "T@\"NSDate\",&,N,V_refreshBeforeDate"
- "T@\"NSDate\",&,N,V_startTime"
- "T@\"NSDate\",&,N,V_submitDate"
- "T@\"NSDate\",&,V_endTime"
- "T@\"NSDate\",&,V_lastScored"
- "T@\"NSDate\",&,V_predictedOptimalStartDate"
- "T@\"NSDate\",&,V_startAfter"
- "T@\"NSDate\",&,V_startBefore"
- "T@\"NSDate\",&,V_startDate"
- "T@\"NSDate\",&,V_suspendRequestDate"
- "T@\"NSDate\",R,N"
- "T@\"NSDate\",R,N,V_endDate"
- "T@\"NSDate\",R,N,V_refreshDate"
- "T@\"NSDate\",R,N,V_startDate"
- "T@\"NSDictionary\",&,N,V_overrideActivities"
- "T@\"NSDictionary\",&,V_remoteAppLaunchCount"
- "T@\"NSDictionary\",&,V_startConditions"
- "T@\"NSDictionary\",C,N"
- "T@\"NSDictionary\",R,C,N,V_countsDictionary"
- "T@\"NSMapTable\",&,N,V_internedStrings"
- "T@\"NSMutableArray\",&,N,V_limitationResponse"
- "T@\"NSMutableArray\",&,N,V_majorPenaltyActivities"
- "T@\"NSMutableArray\",&,N,V_minorPenaltyActivities"
- "T@\"NSMutableArray\",&,N,V_registrations"
- "T@\"NSMutableArray\",&,N,V_testingOverride"
- "T@\"NSMutableDictionary\",&,N,V_activityGroupQueue"
- "T@\"NSMutableDictionary\",&,N,V_activityGroups"
- "T@\"NSMutableDictionary\",&,N,V_activityToDataMap"
- "T@\"NSMutableDictionary\",&,N,V_delayedStartTasks"
- "T@\"NSMutableDictionary\",&,N,V_lastWidgetViewCache"
- "T@\"NSMutableDictionary\",&,N,V_objects"
- "T@\"NSMutableDictionary\",&,N,V_plistToDictionaryMap"
- "T@\"NSMutableDictionary\",&,N,V_policyResponseMetadata"
- "T@\"NSMutableDictionary\",&,N,V_recentlyBackgroundedApps"
- "T@\"NSMutableDictionary\",&,N,V_startedActivities"
- "T@\"NSMutableDictionary\",&,N,V_submittedActivities"
- "T@\"NSMutableDictionary\",&,N,V_watchKitAppStatus"
- "T@\"NSMutableDictionary\",&,V_launchedAppCount"
- "T@\"NSMutableSet\",&,N,V_previousForegroundApps"
- "T@\"NSNumber\",&,N,V_balance"
- "T@\"NSNumber\",&,N,V_highestPriority"
- "T@\"NSNumber\",&,N,V_lowestPriority"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_callbackQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_connectionCreationQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_handlerQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_runQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_appUsageRefreshTimer"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_submissionTimer"
- "T@\"NSObject<OS_os_log>\",&,N,V_dasFrameworkLog"
- "T@\"NSObject<OS_os_log>\",&,N,V_dasSystemContextLog"
- "T@\"NSObject<OS_os_log>\",&,N,V_log"
- "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
- "T@\"NSProgress\",&,N"
- "T@\"NSProgress\",&,N,V_progress"
- "T@\"NSSet\",C,N"
- "T@\"NSSet\",C,N,V_dependencies"
- "T@\"NSSet\",C,N,V_producedResultIdentifiers"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_activityType"
- "T@\"NSString\",&,N,V_appIdentifier"
- "T@\"NSString\",&,N,V_bundleId"
- "T@\"NSString\",&,N,V_clientDataBudgetName"
- "T@\"NSString\",&,N,V_clientName"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_limitationName"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_ratelimitConfigurationName"
- "T@\"NSString\",&,N,V_rationale"
- "T@\"NSString\",&,N,V_remoteDevice"
- "T@\"NSString\",&,N,V_remoteDeviceIdentifier"
- "T@\"NSString\",&,N,V_widgetBudgetID"
- "T@\"NSString\",&,N,V_widgetBudgetIdentifier"
- "T@\"NSString\",&,N,V_widgetID"
- "T@\"NSString\",&,N,V_widgetIdentifier"
- "T@\"NSString\",&,V_clientName"
- "T@\"NSString\",&,V_foregroundWatchApp"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N"
- "T@\"NSString\",C,N,V_diskVolume"
- "T@\"NSString\",C,N,V_extensionIdentifier"
- "T@\"NSString\",C,N,V_fileProtection"
- "T@\"NSString\",C,N,V_groupName"
- "T@\"NSString\",C,N,V_iconUTI"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_launchReason"
- "T@\"NSString\",C,N,V_linkToBundleIdentifier"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_pairedDeviceIdentifier"
- "T@\"NSString\",C,N,V_rateLimitConfigurationName"
- "T@\"NSString\",C,N,V_refreshReason"
- "T@\"NSString\",C,N,V_serviceName"
- "T@\"NSString\",C,N,V_subtitle"
- "T@\"NSString\",C,N,V_title"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_budgetID"
- "T@\"NSString\",R,C,N,V_extensionBundleID"
- "T@\"NSString\",R,C,N,V_viewID"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_limiterName"
- "T@\"NSString\",R,N,V_rateLimitConfigurationName"
- "T@\"NSUUID\",&,N,V_uuid"
- "T@\"NSUserDefaults\",&,N,V_persistence"
- "T@\"NSXPCConnection\",&,V_xpcConnection"
- "T@\"NSXPCListenerEndpoint\",&,N,V_endpoint"
- "T@\"_CDContextualKeyPath\",&,N,V_widgetOverrideKeypath"
- "T@\"_DASActivity\",&,N,V_activity"
- "T@\"_DASAssertion\",&,N,V_assertion"
- "T@\"_DASBMMinimumSpanConfiguration\",C,N,V_minimumSpanConfiguration"
- "T@\"_DASContinuedProcessingWrapper\",&,N,V_continuedProcessingWrapper"
- "T@\"_DASExtension\",R"
- "T@\"_DASExtensionRemoteContext\",&,N,V_context"
- "T@\"_DASFastPass\",C,N,V_fastPass"
- "T@\"_DASFileProtection\",C,N"
- "T@\"_DASScheduler\",&,N,V_dasScheduler"
- "T@\"_DASSubmissionManager\",&,N,V_submissionManager"
- "T@\"_DASSubmissionRateLimiter\",&,N,V_rateLimiter"
- "T@?,C,N,V_aggregationKeyBlock"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_filter"
- "T@?,C,N,V_onApplicationStateChange"
- "T@?,C,N,V_onConditionsChange"
- "T@?,C,N,V_spanMarkerBlock"
- "T@?,C,N,V_startHandler"
- "T@?,C,N,V_suspendHandler"
- "T@?,C,N,V_transform"
- "TB,N"
- "TB,N,V_afterUserIsInactive"
- "TB,N,V_aneIntensive"
- "TB,N,V_backlogged"
- "TB,N,V_beforeDaysFirstActivity"
- "TB,N,V_beforeUserIsActive"
- "TB,N,V_budgeted"
- "TB,N,V_bypassesPredictions"
- "TB,N,V_cancelAfterDeadline"
- "TB,N,V_cpuIntensive"
- "TB,N,V_darkWakeEligible"
- "TB,N,V_dataBudgeted"
- "TB,N,V_deferred"
- "TB,N,V_delayedStart"
- "TB,N,V_dependenciesPreCleared"
- "TB,N,V_diskIntensive"
- "TB,N,V_gpuIntensive"
- "TB,N,V_inStack"
- "TB,N,V_indeedCPUIntensive"
- "TB,N,V_indeedMemoryIntensive"
- "TB,N,V_interrupted"
- "TB,N,V_isDASInitiated"
- "TB,N,V_isMLBackgroundActivity"
- "TB,N,V_isUpload"
- "TB,N,V_memoryIntensive"
- "TB,N,V_postInstall"
- "TB,N,V_preventDeviceSleep"
- "TB,N,V_previousPluginStatus"
- "TB,N,V_requestsApplicationLaunch"
- "TB,N,V_requestsExtensionLaunch"
- "TB,N,V_requiresBuddyComplete"
- "TB,N,V_requiresDeviceInactivity"
- "TB,N,V_requiresInexpensiveNetworking"
- "TB,N,V_requiresNetwork"
- "TB,N,V_requiresPlugin"
- "TB,N,V_requiresRemoteDeviceWake"
- "TB,N,V_requiresUnconstrainedNetworking"
- "TB,N,V_runOnAppForeground"
- "TB,N,V_runWhenAppLaunchUnlikely"
- "TB,N,V_saveSpans"
- "TB,N,V_shouldBePersisted"
- "TB,N,V_shouldWakeDevice"
- "TB,N,V_startedInIdle"
- "TB,N,V_startedOnBattery"
- "TB,N,V_successful"
- "TB,N,V_supportsAnyApplication"
- "TB,N,V_suspendable"
- "TB,N,V_testing"
- "TB,N,V_thermalLevelElevated"
- "TB,N,V_triggersRestart"
- "TB,N,V_wasForceRun"
- "TB,R"
- "TB,R,N"
- "TI,N,V_userIdentifier"
- "TQ,N"
- "TQ,N,V_budgetingToken"
- "TQ,N,V_count"
- "TQ,N,V_dailyMaxBudget"
- "TQ,N,V_downloadSize"
- "TQ,N,V_duration"
- "TQ,N,V_immediateRuntimeState"
- "TQ,N,V_interns"
- "TQ,N,V_lookups"
- "TQ,N,V_majorPenaltyTimerCount"
- "TQ,N,V_maxConcurrent"
- "TQ,N,V_maximum"
- "TQ,N,V_minorPenaltyTimerCount"
- "TQ,N,V_onBatteryRuntimeState"
- "TQ,N,V_schedulingPriority"
- "TQ,N,V_systemAddedWidgetMaxBudget"
- "TQ,N,V_uploadSize"
- "TQ,N,V_widgetMaxBudget"
- "TQ,R"
- "TQ,R,N,V_decision"
- "TQ,V_lastDenialValue"
- "Td,N,V_billedEnergy"
- "Td,N,V_cpuCycleConsumed"
- "Td,N,V_cpuTimeConsumed"
- "Td,N,V_dataConsumed"
- "Td,N,V_diskIOConsumed"
- "Td,N,V_diskIOWrites"
- "Td,N,V_interval"
- "Td,N,V_lastComputedScore"
- "Td,N,V_minimumSpanDuration"
- "Td,N,V_percentCompleted"
- "Td,N,V_predictedOptimalScore"
- "Td,N,V_previousBatteryLevel"
- "Td,N,V_previousDefaultThreshold"
- "Td,N,V_previousSyncThreshold"
- "Td,N,V_score"
- "Td,N,V_timeUntilContentExpiration"
- "Td,N,V_window"
- "Td,R,N,V_validityDuration"
- "Ti,N,V_dastoolToken"
- "Ti,N,V_pid"
- "Ti,N,V_previousMaxThermalPressure"
- "Ti,N,V_recentTrafficSyncRequests"
- "Ti,N,V_remoteForecastDeletionToken"
- "Ti,N,V_resubmitToken"
- "Ti,N,V_token"
- "Tq,N,V_completionStatus"
- "Tq,N,V_decision"
- "Tq,N,V_executionContext"
- "Tq,N,V_inexpensiveNetworkPathStatus"
- "Tq,N,V_maximumRuntime"
- "Tq,N,V_motionState"
- "Tq,N,V_networkPathStatus"
- "Tq,N,V_pageID"
- "Tq,N,V_preClearedMode"
- "Tq,N,V_reason"
- "Tq,N,V_resources"
- "Tq,N,V_semanticVersion"
- "Tq,N,V_staticPriority"
- "Tq,N,V_submissionStrategy"
- "Tq,N,V_targetDevice"
- "Tq,N,V_uninterruptibleDuration"
- "Tq,N,V_urgencyLevel"
- "Tq,V_batchSize"
- "Tq,V_count"
- "T{?=[8I]},N,V_hostAppAuditToken"
- "T{os_unfair_lock_s=I},N,V_lastWidgetViewLock"
- "T{os_unfair_lock_s=I},N,V_penaltyLock"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Viewed"
- "Vv16@0:8"
- "Widgets"
- "Will expire BGTask activities: %@"
- "^{_NSZone=}16@0:8"
- "_DASActivity"
- "_DASActivityBackgroundLaunchScheduler"
- "_DASActivityBackgroundTaskSchedulerServer"
- "_DASActivityBackgroundTasksScheduler"
- "_DASActivityDependency"
- "_DASActivityDependencyManagerIntrospecting"
- "_DASActivityDependencyManagerIntrospectingServer"
- "_DASActivityGroup"
- "_DASActivityGroupScheduler"
- "_DASActivityMetering"
- "_DASActivityOmnibusScheduling"
- "_DASActivityProgressWrapper"
- "_DASActivityRateLimit"
- "_DASActivityRateLimitConfiguration"
- "_DASActivityResult"
- "_DASActivityScheduler"
- "_DASActivitySchedulerClient"
- "_DASActivitySchedulerIntrospecting"
- "_DASActivitySchedulerIntrospectingServer"
- "_DASActivitySchedulerServer"
- "_DASAdditions"
- "_DASBGSystemTaskDataCollection"
- "_DASBGSystemTaskDataCollectionServer"
- "_DASBGSystemTaskScheduler"
- "_DASBGSystemTaskSchedulerServer"
- "_DASBMHistogramBuilder"
- "_DASBMMinimumSpanConfiguration"
- "_DASConfigurationLimiter"
- "_DASContinuedProcessingWrapper"
- "_DASEnumerable"
- "_DASExtension"
- "_DASExtensionRemoteContext"
- "_DASExtensionRunner"
- "_DASFastPass"
- "_DASFileProtection"
- "_DASHistogram"
- "_DASHistogramBuilder"
- "_DASHostExtensionContextProtocol"
- "_DASInternalPolicyEvaluationMetadata"
- "_DASInterning"
- "_DASLimiterResponse"
- "_DASLimits"
- "_DASLimitsUtilities"
- "_DASPairedSystemContext"
- "_DASPlistParser"
- "_DASPredictionTimeline"
- "_DASPriorityQueue"
- "_DASRemoteExtensionContextProtocol"
- "_DASScheduler"
- "_DASStringInterning"
- "_DASStrings"
- "_DASSubmissionManager"
- "_DASSubmissionRateLimiter"
- "_DASSystemConstraintsUpdating"
- "_DASSystemContext"
- "_DASWidgetBudget"
- "_DASWidgetBudgetMigration"
- "_DASWidgetBudgetMigrationHelper"
- "_DASWidgetBudgetParameters"
- "_DASWidgetInfo"
- "_DASWidgetRefresh"
- "_DASWidgetRefreshParameters"
- "_DASWidgetRefreshScheduler"
- "_DASWidgetView"
- "_DASWigetBudgetDecrementRequestResult"
- "_DAS_addOrReplaceObject:"
- "_DAS_addOrReplaceObjectsFromArray:"
- "_DAS_unionSetOverridingExisting:"
- "_OSPrewarmScheduler"
- "_OSPrewarmScheduling"
- "_activity"
- "_activityCompletedWithStatus:"
- "_activityGroupQueue"
- "_activityGroups"
- "_activityToDataMap"
- "_activityType"
- "_afterUserIsInactive"
- "_aggregationKeyBlock"
- "_aneIntensive"
- "_appIdentifier"
- "_appUsageRefreshTimer"
- "_assertion"
- "_auxiliaryConnection"
- "_backgroundTaskSchedulerDelegate"
- "_backlogged"
- "_balance"
- "_batchSize"
- "_beforeDaysFirstActivity"
- "_beforeUserIsActive"
- "_billedEnergy"
- "_budgetID"
- "_budgeted"
- "_budgetingToken"
- "_bundleId"
- "_bypassesPredictions"
- "_callbackQueue"
- "_cancelAfterDeadline"
- "_clientDataBudgetName"
- "_clientName"
- "_completionHandler"
- "_completionStatus"
- "_connectionCreationQueue"
- "_context"
- "_continuedProcessingWrapper"
- "_count"
- "_counts"
- "_countsDictionary"
- "_cpuCycleConsumed"
- "_cpuIntensive"
- "_cpuTimeConsumed"
- "_dailyMaxBudget"
- "_darkWakeEligible"
- "_dasFrameworkLog"
- "_dasScheduler"
- "_dasSystemContextLog"
- "_dastoolToken"
- "_dataBudgeted"
- "_dataConsumed"
- "_decision"
- "_deferred"
- "_delayedStart"
- "_delayedStartTasks"
- "_dependencies"
- "_dependenciesPreCleared"
- "_diskIOConsumed"
- "_diskIOWrites"
- "_diskIntensive"
- "_diskVolume"
- "_downloadSize"
- "_duration"
- "_endDate"
- "_endTime"
- "_endpoint"
- "_executionContext"
- "_extensionAuxiliaryHostProtocol"
- "_extensionAuxiliaryVendorProtocol"
- "_extensionBundleID"
- "_extensionIdentifier"
- "_fastPass"
- "_featureCodes"
- "_fileProtection"
- "_filter"
- "_foregroundWatchApp"
- "_gpuIntensive"
- "_groupName"
- "_handlerQueue"
- "_highestPriority"
- "_hostAppAuditToken"
- "_iconUTI"
- "_identifier"
- "_immediateRuntimeState"
- "_inStack"
- "_indeedCPUIntensive"
- "_indeedMemoryIntensive"
- "_inexpensiveNetworkPathStatus"
- "_initWithBudgetID:extensionBundleID:"
- "_internalGroupLock"
- "_internalGroupNames"
- "_internedStrings"
- "_interns"
- "_interrupted"
- "_interval"
- "_involvedProcesses"
- "_isDASInitiated"
- "_isMLBackgroundActivity"
- "_isUpload"
- "_lastComputedScore"
- "_lastDenialValue"
- "_lastScored"
- "_lastWidgetViewCache"
- "_lastWidgetViewLock"
- "_launchReason"
- "_launchedAppCount"
- "_limitationName"
- "_limitationResponse"
- "_limiterName"
- "_linkToBundleIdentifier"
- "_log"
- "_lookups"
- "_lowestPriority"
- "_majorPenaltyActivities"
- "_majorPenaltyTimerCount"
- "_maxConcurrent"
- "_maximum"
- "_maximumRuntime"
- "_memoryIntensive"
- "_minimumSpanConfiguration"
- "_minimumSpanDuration"
- "_minorPenaltyActivities"
- "_minorPenaltyTimerCount"
- "_motionState"
- "_name"
- "_networkPathStatus"
- "_objects"
- "_onApplicationStateChange"
- "_onBatteryRuntimeState"
- "_onConditionsChange"
- "_overrideActivities"
- "_pageID"
- "_pairedDeviceIdentifier"
- "_penaltyLock"
- "_penaltyTracker"
- "_percentCompleted"
- "_persistence"
- "_pid"
- "_plistToDictionaryMap"
- "_policyResponseMetadata"
- "_postInstall"
- "_preClearedMode"
- "_predictedOptimalScore"
- "_predictedOptimalStartDate"
- "_preventDeviceSleep"
- "_previousBatteryLevel"
- "_previousDefaultThreshold"
- "_previousExclusiveIdentifiers"
- "_previousForegroundApps"
- "_previousMaxThermalPressure"
- "_previousPluginStatus"
- "_previousSyncThreshold"
- "_principalObject"
- "_processingTaskIdentifiers"
- "_producedResultIdentifiers"
- "_progress"
- "_publisher"
- "_queue"
- "_rateLimitConfigurationName"
- "_rateLimiter"
- "_rateLimits"
- "_ratelimitConfigurationName"
- "_rationale"
- "_reason"
- "_recentTrafficSyncRequests"
- "_recentlyBackgroundedApps"
- "_refreshAfterDate"
- "_refreshBeforeDate"
- "_refreshDate"
- "_refreshReason"
- "_registrations"
- "_relatedApplications"
- "_remoteAppLaunchCount"
- "_remoteDevice"
- "_remoteDeviceIdentifier"
- "_remoteForecastDeletionToken"
- "_requestsApplicationLaunch"
- "_requestsExtensionLaunch"
- "_requiresBuddyComplete"
- "_requiresDeviceInactivity"
- "_requiresDeviceInactivityIsSetByUser"
- "_requiresInexpensiveNetworking"
- "_requiresNetwork"
- "_requiresPlugin"
- "_requiresRemoteDeviceWake"
- "_requiresUnconstrainedNetworking"
- "_resetWidgetBudgets"
- "_resources"
- "_resubmitToken"
- "_runOnAppForeground"
- "_runQueue"
- "_runWhenAppLaunchUnlikely"
- "_runner"
- "_saveSpans"
- "_schedulerRecommendedApplications"
- "_schedulingPriority"
- "_score"
- "_semanticVersion"
- "_serviceName"
- "_setQueue:"
- "_shouldBePersisted"
- "_shouldWakeDevice"
- "_spanMarkerBlock"
- "_startAfter"
- "_startBefore"
- "_startConditions"
- "_startDate"
- "_startHandler"
- "_startTime"
- "_startedActivities"
- "_startedInIdle"
- "_startedOnBattery"
- "_staticPriority"
- "_submissionManager"
- "_submissionStrategy"
- "_submissionTimer"
- "_submitDate"
- "_submittedActivities"
- "_submittedActivityTracker"
- "_subtitle"
- "_successful"
- "_supportsAnyApplication"
- "_suspendHandler"
- "_suspendRequestDate"
- "_suspendable"
- "_systemAddedWidgetMaxBudget"
- "_targetDevice"
- "_testing"
- "_testingOverride"
- "_thermalLevelElevated"
- "_timeUntilContentExpiration"
- "_title"
- "_token"
- "_transaction"
- "_transform"
- "_transitionDates"
- "_triggersRestart"
- "_uninterruptibleDuration"
- "_uploadSize"
- "_urgencyLevel"
- "_userIdentifier"
- "_userInfo"
- "_userInfoLock"
- "_uuid"
- "_validityDuration"
- "_values"
- "_viewID"
- "_wasForceRun"
- "_watchKitAppStatus"
- "_widgetBudgetID"
- "_widgetBudgetIdentifier"
- "_widgetID"
- "_widgetIdentifier"
- "_widgetMaxBudget"
- "_widgetOverrideKeypath"
- "_window"
- "_xpcConnection"
- "acknowledgeSystemTaskLaunchWithIdentifier:completionHandler:"
- "acknowledgeSystemTaskLaunchWithIdentifier:error:"
- "acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:"
- "acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:completionHandler:"
- "activity:blockedOnPolicies:"
- "activity:runWithoutHonoringPolicies:"
- "activityCanceled:"
- "activityCanceled:withScheduler:"
- "activityCanceledWithReason:expirationReason:"
- "activityCompleted:"
- "activityCompleted:withScheduler:"
- "activityCompletedWithStatus:"
- "activityContainsOverrides:"
- "activityContainsOverrides:handler:"
- "activityForActivityName:"
- "activityForActivityName:handler:"
- "activityGroupQueue"
- "activityGroups"
- "activityStarted:"
- "activityStartedWithParameters:"
- "activityStoppedWithParameters:"
- "activityToDataMap"
- "activityWithName:priority:duration:startingAfter:startingBefore:"
- "activityWithName:priority:duration:startingAfter:startingBefore:userInfo:"
- "addNotificationHandlerForTaskName:withPriority:withParameters:withHandler:"
- "addObject:"
- "addObject:withPriority:"
- "addObjectsFromArray:"
- "addPauseExceptParameter:"
- "addPauseExceptParameter:handler:"
- "addToPenaltyBox:"
- "addToTracker:"
- "admitNextActivityAfterCompletionOf:withScheduler:"
- "afterUserIsInactive"
- "aggregationKeyBlock"
- "allBudgets"
- "allBudgetsWithHandler:"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "allowDiscretionaryWorkForBackgroundTask:withParameters:"
- "allowDiscretionaryWorkForUtilityTask:withParameters:"
- "allowSyncTrafficForRecentlyBackgroundedApp"
- "allowsCompanionExpensiveNetworking"
- "allowsDiscretionaryWorkForTask:withPriority:withParameters:"
- "allowsSendingTrafficeForServiceIdentifiers:atPriorityLevel:isReunionOrInitialSync:responseValidityDuration:"
- "allowsUnrestrictedBackgroundLaunches"
- "aneIntensive"
- "anyApplicationActivityWithName:priority:duration:startingAfter:startingBefore:limitedToApplications:"
- "anyItemsIntersectArray:"
- "appIdentifier"
- "appUsageBundleID"
- "appUsageRefreshTimer"
- "appendFormat:"
- "appendString:"
- "applicationLaunchActivityWithName:priority:forApplication:withReason:duration:startingAfter:startingBefore:"
- "array"
- "array:withItemsIn:"
- "arrayWithCapacity:"
- "arrayWithIntersectionOf:and:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "arrayWithObjectsFrom:"
- "arrayWithUnionOf:and:"
- "assertion"
- "autorelease"
- "backgroundAppRefreshEnabledForApp:withHandler:"
- "backgroundTaskSchedulerDelegate"
- "balanceForBudgetWithName:"
- "balanceForBudgetWithName:withHandler:"
- "batteryLevelsAllowSendingTrafficeForServiceIdentifiers:atPriorityLevel:"
- "beforeApplicationLaunch"
- "beforeDaysFirstActivity"
- "beforeUserIsActive"
- "beginRequestWithExtensionContext:"
- "billedEnergy"
- "bitmaskForLimitationName:"
- "bitmaskFromResponses:"
- "blockRebootActivitiesForSU"
- "blockingPoliciesWithParameters:"
- "blockingPoliciesWithParameters:handler:"
- "boolForUserInfoKey:"
- "boolValue"
- "budgetID"
- "budgeted"
- "budgetingToken"
- "builderWithPublisher:"
- "builderWithPublisher:saveSpans:"
- "bundle"
- "bundleId"
- "bypassesPredictions"
- "callbackQueue"
- "cancel"
- "cancelActivities:"
- "cancelActivitiesWithReason:cancellationReason:"
- "cancelActivity:"
- "cancelAfterDeadline"
- "cancelAllTaskRequests"
- "cancelAllTaskRequestsWithCompletionHandler:"
- "cancelTaskRequestWithIdentifier:"
- "cancelTaskRequestWithIdentifier:completionHandler:"
- "capacityForGroupName:"
- "characterAtIndex:"
- "ckPushContentMatches:"
- "clasStatus"
- "clasStatusWithHandler:"
- "class"
- "cleanDuration:"
- "cleanSchedulingPriority:"
- "cleanTransferSize:"
- "clientDataBudgetName"
- "clientFailedtoExpireTaskWithIdentifier:"
- "clientProvidedIdentifier"
- "clientProvidedStartDate"
- "collect"
- "compare:"
- "compatibilityWith:"
- "complete"
- "completeSystemTaskWithIdentifier:"
- "completeSystemTaskWithIdentifier:completionHandler:"
- "completeTaskRequest:withSuccess:"
- "completeTaskRequest:withSuccess:completionHandler:"
- "completeUnlessOpen"
- "completeUntilFirstUserAuthentication"
- "completeWhenUserInactive"
- "completedUnitCount"
- "completionHandler"
- "components:fromDate:"
- "componentsSeparatedByString:"
- "configurationWithMinimumDuration:aggregationKey:spanMarker:"
- "conformsToProtocol:"
- "connectToDaemon:"
- "connectionCreationQueue"
- "containsObject:"
- "containsOverrideForActivity:withLimitation:"
- "containsString:"
- "containsValueForKey:"
- "context"
- "contextWithClientIdentifier:callbackQueue:systemConditionChangeCallback:trafficCancelationHandler:"
- "continuedProcessingActivityWithName:"
- "continuedProcessingDeviceCapabilities:"
- "convertUUIDToUint64:"
- "cooccurrencesWith:"
- "copy"
- "copyWithZone:"
- "correlationWith:"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "counts"
- "countsDictionary"
- "cpuCycleConsumed"
- "cpuIntensive"
- "cpuTimeConsumed"
- "createActivityGroup:"
- "createExtensionRunnerWithClassName:"
- "createRateLimitConfigurationWithName:rateLimits:"
- "createRefreshActivityForWidgetBudgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:"
- "createRefreshActivityForWidgetID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:"
- "createRefreshActivityWithRateLimitConfigurationName:forWidgetBudgetID:withRemoteDeviceID:containingAppID:refreshAfter:refreshBefore:widgetInfo:refreshHandler:"
- "createRefreshActivityWithWidgetParameters:"
- "createRefreshActivityWithWidgetParameters:refreshHandler:"
- "createRefreshActivityWithWidgetParameters:withRefreshHandler:"
- "currentAllocations:timeFilter:bgsqlData:"
- "currentAllocations:timeFilter:bgsqlData:withHandler:"
- "currentConnection"
- "currentPredictions"
- "currentPredictionsWithHandler:"
- "d"
- "d16@0:8"
- "d24@0:8@\"NSString\"16"
- "d24@0:8@16"
- "d24@0:8d16"
- "d32@0:8Q16i24B28"
- "dailyMaxBudget"
- "darkWakeEligible"
- "dasFrameworkLog"
- "dasScheduler"
- "dasSystemContextLog"
- "das_dedup"
- "das_interningStatistics"
- "das_purgeInterned"
- "dastoolToken"
- "dataBudgetingEnabled"
- "dataConsumed"
- "dataWithBytes:length:"
- "dateByAddingTimeInterval:"
- "dateFromAbsoluteTime:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decrementBudgetForWidgetID:by:"
- "decrementBy:forBudgetWithName:"
- "defaultInexpensivePathEvaluator"
- "defaultPathEvaluator"
- "deferActivities:"
- "deferActivities:withHandler:"
- "delayedRunningActivities"
- "delayedRunningActivitiesWithHandler:"
- "delayedStartActivities:"
- "delayedStartTasks"
- "deleteLimitForActivity:"
- "deleteLimitForActivity:forLimiterWithName:"
- "deleteLimitForActivity:forLimiterWithName:handler:"
- "deleteRemoteHistogram"
- "dependenciesPreCleared"
- "dependencyForIdentifier:"
- "deregisterCallback:"
- "deriveSpanTuplesWithMinimumDurationOnStream:"
- "deriveSpansWithMinimumDurationOnStream:"
- "deriveSpansWithMinimumDurationOnStream_array:"
- "deriveSpansWithMinimumDurationOnStream_heap:"
- "description"
- "dictionary"
- "dictionaryForPlist:"
- "dictionaryRepresentation"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "didHandleExclusiveAppChange"
- "disableAppRefreshForApps:"
- "diskIOConsumed"
- "diskIOWrites"
- "diskIntensive"
- "distantPast"
- "doubleValue"
- "downloadSize"
- "earlierDate:"
- "enableTaskRegistryMode:processes:"
- "enableTaskRegistryMode:processes:handler:"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endDate"
- "endLaunchWithReason:forApp:"
- "endTime"
- "endpoint"
- "enterTestModeWithParameters:reset:"
- "enterTestModeWithParameters:reset:handler:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsInChunksOfSize:block:"
- "enumerateObjectsUsingBlock:"
- "error"
- "errorWithDomain:code:userInfo:"
- "establishConnection:"
- "evaluateAllActivities:handler:"
- "evaluateAllActivitiesWithHandle:"
- "evaluateBytesConsumed:withPreviousParameters:"
- "evaluatePolicies:"
- "evaluatePolicies:handler:"
- "eventBody"
- "extendUpdateActivityDictionary:"
- "extensionBundleID"
- "extensionIdentifier"
- "extensionLaunchActivityWithName:priority:forApplication:forExtensionIdentifier:withReason:duration:startingAfter:startingBefore:"
- "extensionLaunchActivityWithName:priority:forApplication:withReason:duration:startingAfter:startingBefore:"
- "extensionLaunchActivityWithName:priority:forExtensionIdentifier:withReason:duration:startingAfter:startingBefore:"
- "extensionRunnerClassAllowList"
- "fetchInfoForApplicationWithBundleID:forPairedDevice:completion:"
- "fileHandleForReadingAtPath:"
- "fileProtectionStringNone"
- "filter"
- "filterWithIsIncluded:"
- "filteredArrayUsingPredicate:"
- "first"
- "firstObject"
- "forceResetOfResultIdentifier:"
- "forceRunActivities:"
- "foregroundApplicationsAllowSendingTrafficForServiceIdentifiers:atPriorityLevel:furtherChecksNecessary:"
- "foregroundWatchApp"
- "getActivePairedDevice"
- "getActivityTimelines:timeFilter:bgsqlData:"
- "getActivityTimelines:timeFilter:bgsqlData:handler:"
- "getBuddyEvents:bgsqlData:"
- "getBuddyEvents:bgsqlData:handler:"
- "getBytes:length:"
- "getConditionsPenalties:"
- "getConditionsPenalties:handler:"
- "getContentionPenalties:"
- "getContentionPenalties:handler:"
- "getDeviceConditionTimelines:bgsqlData:"
- "getDeviceConditionTimelines:bgsqlData:handler:"
- "getElapsedRuntimes:timeFilter:bgsqlData:"
- "getElapsedRuntimes:timeFilter:bgsqlData:handler:"
- "getEligibilityTimelines:timeFilter:bgsqlData:"
- "getEligibilityTimelines:timeFilter:bgsqlData:handler:"
- "getEstimatedRuntimes:timeFilter:bgsqlData:"
- "getEstimatedRuntimes:timeFilter:bgsqlData:handler:"
- "getFeatureDependencyGraphs:timeFilter:bgsqlData:"
- "getFeatureDependencyGraphs:timeFilter:bgsqlData:handler:"
- "getFeatureLatencyProjections:timeFilter:bgsqlData:"
- "getFeatureLatencyProjections:timeFilter:bgsqlData:handler:"
- "getFeatureTimelines:timeFilter:bgsqlData:"
- "getFeatureTimelines:timeFilter:bgsqlData:handler:"
- "getInstallTimeline:bgsqlData:"
- "getInstallTimeline:bgsqlData:handler:"
- "getLimiterResponseForActivity:"
- "getLimiterResponseForActivity:handler:"
- "getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:"
- "getOvernightIntensiveSchedulerEfficiencyMetrics:bgsqlData:handler:"
- "getPendingTaskRequestsWithCompletionHandler:"
- "getRebootEvents:bgsqlData:"
- "getRebootEvents:bgsqlData:handler:"
- "getRuntimeLimit:"
- "getRuntimeLimit:handler:"
- "getSchedulerEfficiencyMetrics:bgsqlData:"
- "getSchedulerEfficiencyMetrics:bgsqlData:handler:"
- "getSortedCandidateActivities:"
- "getSortedCandidateActivities:handler:"
- "getSubmittedSystemTaskRequestsWithCompletionHandler:"
- "getSystemConditionsTimeline:timeFilter:bgsqlData:"
- "getSystemConditionsTimeline:timeFilter:bgsqlData:handler:"
- "getTaskDependencyGraphs:timeFilter:bgsqlData:"
- "getTaskDependencyGraphs:timeFilter:bgsqlData:handler:"
- "getTaskLatencyProjections:timeFilter:bgsqlData:"
- "getTaskLatencyProjections:timeFilter:bgsqlData:handler:"
- "getUUIDBytes:"
- "gpuIntensive"
- "groupNameForActivity:"
- "groupWithName:maxConcurrent:"
- "handleAppStateChange"
- "handleCanceledActivity:withGroupName:"
- "handleClientFailedtoExpireTaskWithIdentifier:completionHandler:"
- "handleClientLedSystemTaskExpirationWithIdentifier:retryAfter:completionHandler:"
- "handleConditionChange"
- "handleEligibleActivities:"
- "handleForAuditToken:error:"
- "handleLaunchFromDaemonForActivities:"
- "handleNoLongerRunningActivities:"
- "handleWatchAppBackgrounded"
- "handlerQueue"
- "hasMagneticSensitivity"
- "hasManyConstraints"
- "hasPrefix:"
- "hasSuffix:"
- "hash"
- "hashArrayOfString:"
- "hashString:"
- "haveNSecondsElapsed:"
- "highestPriority"
- "histogram"
- "histogramOnResponseQueue:withCompletion:"
- "hostContextWithError:"
- "i16@0:8"
- "idsDeviceIdentifier"
- "indeedCPUIntensive"
- "indeedMemoryIntensive"
- "indeterminateProgress"
- "indicatesProtection"
- "inexpensiveNetworkPathStatus"
- "infoDictionary"
- "init"
- "initActivityCompletionDependencyWithIdentifier:"
- "initResultDependencyWithIdentifier:batchSize:"
- "initWithBudgetID:bundleID:endDate:extensionBundleID:inStack:pageID:startDate:timeUntilExpiration:viewID:"
- "initWithBudgetID:extensionBundleID:isDASInitiated:refreshDate:refreshReason:"
- "initWithBudgetID:extensionBundleID:refreshDate:"
- "initWithCapacity:"
- "initWithClientIdentifier:context:callbackQueue:systemConditionChangeCallback:trafficCancelationHander:"
- "initWithCoder:"
- "initWithContext:"
- "initWithDecision:withLimiter:validityDuration:rationale:"
- "initWithEndpoint:parameters:"
- "initWithEvents:"
- "initWithFirst:second:"
- "initWithIdentifier:"
- "initWithIdentifier:count:"
- "initWithIdentifier:withBudgetIdentifier:withRateLimitConfigurationName:withRemoteDeviceIdentifier:withAppIdentifier:refreshAfter:refreshBefore:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:options:"
- "initWithMaximum:perWindow:"
- "initWithName:andLimits:"
- "initWithName:maxConcurrent:"
- "initWithName:priority:duration:startingAfter:startingBefore:userInfo:"
- "initWithProgress:"
- "initWithProtection:"
- "initWithPublisher:saveSpans:"
- "initWithRateLimitConfigurationName:budgetID:extensionBundleID:refreshDate:initiatedByDAS:"
- "initWithScore:reason:decision:"
- "initWithSequence:"
- "initWithStartDate:endDate:"
- "initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:"
- "initWithTitle:subtitle:iconUTI:linkToBundleIdentifier:resources:submissionStrategy:executionContext:hostAppAuditToken:"
- "initWithTitle:subtitle:resources:submissionStrategy:executionContext:hostAppAuditToken:"
- "initWithValues:eachWithDuration:startingAt:"
- "initWithValues:forDurations:startingAt:"
- "initWithValues:startDate:transitionDates:"
- "initWithViewID:budgetID:extensionBundleID:from:to:"
- "initialize"
- "inspect:criteria:"
- "inspect:criteria:withHandler:"
- "intValue"
- "integerForKey:"
- "integerValue"
- "interfaceWithProtocol:"
- "internString:"
- "internalGroupNames"
- "internedStrings"
- "interrupted"
- "intervalLimiterResponseForActivity:"
- "invalidate"
- "isANEIntensive"
- "isActivityCompletionBased"
- "isAfter:"
- "isAnyThirdPartyApp:"
- "isApplicationFocalForPushTask:"
- "isBackgroundTaskActivity"
- "isBefore:"
- "isCPUIntensive"
- "isCancelled"
- "isContactTracingBackgroundActivity"
- "isContinuedProcessingTask"
- "isDaemon"
- "isDiskIntensive"
- "isEmergencySOSActivity"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToString:"
- "isForegroundAppProxy"
- "isGPUIntensive"
- "isIdenticalLaunchTo:"
- "isIndeedIntensive"
- "isInexpensiveNetworkAvailable"
- "isIntensive"
- "isKindOfClass:"
- "isLowPriorityIdleStackTask"
- "isMLBackgroundActivity"
- "isMemberOfClass:"
- "isMemoryIntensive"
- "isNetworkAvailable"
- "isPartOfCustomGroup"
- "isPluggedIn:"
- "isPrioritizedIdleStackTasks"
- "isProxy"
- "isRunning"
- "isSameDayOfWeekAs:withCalendar:"
- "isSatisfiedByAvailableResultCount:"
- "isSatisfiedByResult:"
- "isSilentPush"
- "isSoftwareUpdateActivity"
- "isValidSuspensionExemptions:"
- "isWatchPluggedIn"
- "keepsPrevious"
- "keyPathForActiveComplications"
- "keyPathForAppUsageDataDictionaries"
- "keyPathForBatteryLevel"
- "keyPathForDefaultPairedDeviceBatteryLevel"
- "keyPathForDefaultPairedDeviceForegroundApp"
- "keyPathForDefaultPairedDevicePluginStatus"
- "keyPathForDefaultPairedDeviceThermalPressureLevel"
- "keyPathForDefaultPairedServicesAppearingForeground"
- "keyPathForForegroundApp"
- "keyPathForPluginStatus"
- "keyPathForPriority:"
- "keyPathForServicesAppearingForeground"
- "keyPathForThermalPressureLevel"
- "keyPathWithKey:"
- "lastComputedScore"
- "lastObject"
- "lastWidgetViewCache"
- "lastWidgetViewLock"
- "laterDate:"
- "launchForRemoteNotificationWithTopic:withPayload:highPriority:"
- "launchWithTopic:forReason:withPayload:highPriority:"
- "launchedAppCount"
- "length"
- "limitResponseWithDecision:withLimiter:validityDuration:rationale:"
- "limitationName"
- "limitationResponse"
- "limitedActivity:withLimitsResponses:"
- "limitsApplyToActivity:"
- "listener:shouldAcceptNewConnection:"
- "loadOverrides"
- "loadPlist:"
- "localNonWakingRegistrationWithIdentifier:contextualPredicate:callback:"
- "localNonWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
- "localTimeZone"
- "log"
- "lowLikelihoodPeriod"
- "lowercaseString"
- "lowestPriority"
- "mainBundle"
- "majorPenaltyActivities"
- "majorPenaltyTimerCount"
- "mapTableWithKeyOptions:valueOptions:"
- "mapWithTransform:"
- "maxConcurrent"
- "maximumRuntime"
- "mean"
- "memoryIntensive"
- "metadataWithScore:"
- "minimumSpanConfiguration"
- "minimumSpanDuration"
- "minorPenaltyActivities"
- "minorPenaltyTimerCount"
- "minusSet:"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nameString"
- "networkPathStatus"
- "networkingActivityWithName:priority:downloadSize:uploadSize:expensiveNetworkingAllowed:startingAfter:startingBefore:"
- "networkingActivityWithName:priority:transferSize:isUpload:expensiveNetworkingAllowed:startingAfter:startingBefore:"
- "noTransferSizeSpecified"
- "none"
- "now"
- "ns"
- "numberFromString:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectForUserInfoKey:"
- "objects"
- "onApplicationStateChange"
- "onConditionsChange"
- "orderedSetWithArray:"
- "overdueAtDate:"
- "overrideActivities"
- "overwritesPrevious"
- "pairedDeviceIdentifier"
- "path"
- "pauseWithParameters:"
- "pauseWithParameters:handler:"
- "penaltyLock"
- "penaltyTracker"
- "performActivity:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "persistence"
- "plistToDictionaryMap"
- "pluginGroupNameForGroupName:"
- "policies"
- "policiesWithHandler:"
- "policyResponseMetadata"
- "policyScores"
- "popFirst"
- "popLast"
- "preClearedMode"
- "predicateForChangeAtKeyPath:"
- "predicateForChangeAtKeyPaths:"
- "predicateForKeyPath:withFormat:"
- "predicateWithFormat:"
- "predictedOptimalScore"
- "predictedOptimalStartDate"
- "prepareForActivity:"
- "prettySchedulingPriorityDescription:"
- "preventDeviceSleep"
- "previousBatteryLevel"
- "previousDefaultThreshold"
- "previousExclusiveIdentifiers"
- "previousForegroundApps"
- "previousMaxThermalPressure"
- "previousPluginStatus"
- "previousSyncThreshold"
- "prewarmApplication:"
- "prewarmSuspend"
- "prewarmSuspendWithHandler:"
- "priorityQueue"
- "propertyListWithData:options:format:error:"
- "protectionType"
- "protectionWithType:"
- "publisher"
- "publisherForDevice:withUseCase:options:"
- "publisherWithSpansMeetingMinimumDuration:"
- "purge"
- "q16@0:8"
- "q24@0:8@16"
- "queryActivityDecision:fromResponses:"
- "queryDependenciesOfTaskIdentifier:"
- "queryDependenciesOfTaskIdentifier:withHandler:"
- "queryStatusOfResultIdentifier:"
- "queryStatusOfResultIdentifier:withHandler:"
- "queue"
- "rateLimitConfigurationName"
- "rateLimitConfigurationWithName:andLimits:"
- "rateLimitWithMaximum:perWindow:"
- "rateLimiter"
- "ratelimitConfigurationName"
- "readBudgetForRecentlyBackgroundedAppSyncTraffic"
- "readDataToEndOfFile"
- "reason"
- "recentTrafficSyncRequests"
- "recentlyBackgroundedApps"
- "reconcileWithActivity:"
- "recordWidgetRefreshes:"
- "recordWidgetViews:"
- "rectifyExecutionContextWithClientProcessHandle:hostAppProcHandle:"
- "refreshAfterDate"
- "refreshAt:forWidgetID:"
- "refreshBeforeDate"
- "refreshDate"
- "registerCallback:"
- "registerForContextChanges"
- "registrations"
- "regularExpressionWithPattern:options:error:"
- "relatedApplications"
- "release"
- "remoteAppLaunchCount"
- "remoteDevice"
- "remoteDeviceIdentifier"
- "remoteDevicesWithError:"
- "remoteForecastDeletionToken"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeAll"
- "removeAllFromActivityTracker"
- "removeAllObjects"
- "removeLastObject"
- "removeNotificationHandlerForTaskName:"
- "removeObject:"
- "removeObject:atPriority:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "reportCustomCheckpoint:forTask:error:"
- "reportCustomCheckpoint:forTask:withHandler:"
- "reportFeatureCheckpoint:forFeature:atDate:error:"
- "reportFeatureCheckpoint:forFeature:atDate:withHandler:"
- "reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:"
- "reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:withHandler:"
- "reportSystemTaskWithIdentifier:consumedResults:completionHandler:"
- "reportSystemTaskWithIdentifier:producedResults:completionHandler:"
- "reportSystemWorkload:ofCategory:error:"
- "reportSystemWorkload:ofCategory:withHandler:"
- "reportTaskWorkloadProgress:target:completed:category:subCategory:completionHandler:"
- "reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:"
- "reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:withHandler:"
- "reportingName"
- "reportingServiceName"
- "requestsApplicationLaunch"
- "requestsExtensionLaunch"
- "requestsImmediateRuntime"
- "requestsNewsstandLaunch"
- "requiresBuddyComplete"
- "requiresDeviceInactivity"
- "requiresInexpensiveNetworking"
- "requiresNetwork"
- "requiresPlugin"
- "requiresRemoteDeviceWake"
- "requiresSignificantUserInactivity"
- "requiresUnconstrainedNetworking"
- "resetBudgetForRecentlyBackgroundedAppSyncTraffic"
- "resetFastPassActivities:resetAll:"
- "resetFastPassActivities:resetAll:withHandler:"
- "resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:"
- "resetWidgetBudgets"
- "respondsToSelector:"
- "responseWithActivityConfigurations:"
- "resubmitPendingActivities"
- "resubmitPendingStartActivities"
- "resubmitRunningActivities"
- "resubmitRunningActivities:"
- "resubmitRunningTasks:"
- "resubmitToken"
- "resume"
- "resumeTaskSchedulingWithIdentifier:completionHandler:"
- "retain"
- "retainCount"
- "runActivities:"
- "runActivitiesWithDelayedStart:"
- "runActivitiesWithUrgency:activities:"
- "runOnAppForeground"
- "runProceedableActivities:"
- "runProceedableActivities:handler:"
- "runQueue"
- "runWhenAppLaunchUnlikely"
- "runner"
- "runner:performActivity:"
- "runningActivities"
- "runningActivitiesWithHandler:"
- "runningGroupActivities"
- "runningGroupActivitiesWithHandler:"
- "sanitizeWidgetViews:"
- "saveSpans"
- "scheduler"
- "scheduler:handleLaunchForActivities:"
- "scheduler:willExpireActivities:"
- "schedulerRecommendedApplications"
- "schedulerWithClientName:"
- "schedulerWithEndpoint:"
- "schedulerWithEndpoint:withClientName:"
- "schedulingPriority"
- "score"
- "second"
- "self"
- "semanticVersion"
- "sendEvent:"
- "serviceName"
- "set"
- "setActivity:"
- "setActivityGroupQueue:"
- "setActivityGroups:"
- "setActivityToDataMap:"
- "setActivityType:"
- "setAfterUserIsInactive:"
- "setAggregationKeyBlock:"
- "setAllowsCompanionExpensiveNetworking:"
- "setAneIntensive:"
- "setAppIdentifier:"
- "setAppUsageRefreshTimer:"
- "setAssertion:"
- "setBackgroundTaskSchedulerDelegate:"
- "setBackgroundTasksSchedulerDelegate:"
- "setBacklogged:"
- "setBalance:"
- "setBalance:forBudgetWithName:"
- "setBatchSize:"
- "setBeforeApplicationLaunch:"
- "setBeforeDaysFirstActivity:"
- "setBeforeUserIsActive:"
- "setBilledEnergy:"
- "setBlockRebootActivitiesForSU:"
- "setBool:forUserInfoKey:"
- "setBudget:"
- "setBudgeted:"
- "setBudgetingToken:"
- "setBundleId:"
- "setBypassesPredictions:"
- "setCallbackQueue:"
- "setCancelAfterDeadline:"
- "setCapacity:forBudgetWithName:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setClientDataBudgetName:"
- "setClientName:"
- "setClientProvidedIdentifier:"
- "setClientProvidedStartDate:"
- "setCompletedUnitCount:"
- "setCompletionHandler:"
- "setCompletionStatus:"
- "setConnectionCreationQueue:"
- "setConstraintsWithXPCDictionary:"
- "setContext:"
- "setContinuedProcessingWrapper:"
- "setCount:"
- "setCpuCycleConsumed:"
- "setCpuIntensive:"
- "setCpuTimeConsumed:"
- "setDailyMaxBudget:"
- "setDarkWakeEligible:"
- "setDasFrameworkLog:"
- "setDasScheduler:"
- "setDasSystemContextLog:"
- "setDastoolToken:"
- "setDataBudgeted:"
- "setDataConsumed:"
- "setDateStyle:"
- "setDecision:"
- "setDeferred:"
- "setDelayedStart:"
- "setDelayedStartTasks:"
- "setDependencies:"
- "setDependenciesPreCleared:"
- "setDiskIOConsumed:"
- "setDiskIOWrites:"
- "setDiskIntensive:"
- "setDiskVolume:"
- "setDownloadSize:"
- "setDuration:"
- "setEndDate:"
- "setEndTime:"
- "setEndpoint:"
- "setExecutionContext:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtensionIdentifier:"
- "setFastPass:"
- "setFeatureCodes:"
- "setFileProtection:"
- "setFilter:"
- "setForegroundWatchApp:"
- "setGpuIntensive:"
- "setGroupName:"
- "setHandlerQueue:"
- "setHasMagneticSensitivity:"
- "setHighestPriority:"
- "setHostAppAuditToken:"
- "setIconUTI:"
- "setIdentifier:"
- "setImmediateRuntimeState:"
- "setInStack:"
- "setIndeedCPUIntensive:"
- "setIndeedMemoryIntensive:"
- "setInexpensiveNetworkPathStatus:"
- "setInteger:forKey:"
- "setInternalGroupNames:"
- "setInternedStrings:"
- "setInterns:"
- "setInterrupted:"
- "setInterruptionHandler:"
- "setInterval:"
- "setInvolvedProcesses:"
- "setIsContactTracingBackgroundActivity:"
- "setIsDASInitiated:"
- "setIsMLBackgroundActivity:"
- "setIsUpload:"
- "setLastComputedScore:"
- "setLastDenialValue:"
- "setLastScored:"
- "setLastWidgetViewCache:"
- "setLastWidgetViewLock:"
- "setLaunchReason:"
- "setLaunchedAppCount:"
- "setLimitForActivity:"
- "setLimitationName:"
- "setLimitationResponse:"
- "setLinkToBundleIdentifier:"
- "setLog:"
- "setLookups:"
- "setLowestPriority:"
- "setMajorPenaltyActivities:"
- "setMajorPenaltyTimerCount:"
- "setMaxConcurrent:"
- "setMaximum:"
- "setMaximumRuntime:"
- "setMemoryIntensive:"
- "setMinimumBGTaskRequestDelay:"
- "setMinimumBackgroundFetchInterval:forApp:"
- "setMinimumSpanConfiguration:"
- "setMinimumSpanDuration:"
- "setMinorPenaltyActivities:"
- "setMinorPenaltyTimerCount:"
- "setMotionState:"
- "setName:"
- "setNetworkPathStatus:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObject:forUserInfoKey:"
- "setObjects:"
- "setOnApplicationStateChange:"
- "setOnBatteryRuntimeState:"
- "setOnConditionsChange:"
- "setOverrideActivities:"
- "setOverridesForWidgetBudgetIDs:"
- "setOverridesForWidgetIDs:"
- "setPageID:"
- "setPairedDeviceIdentifier:"
- "setPenaltyLock:"
- "setPenaltyTracker:"
- "setPercentCompleted:"
- "setPersistence:"
- "setPid:"
- "setPlistToDictionaryMap:"
- "setPolicyResponseMetadata:"
- "setPostInstall:"
- "setPreClearedMode:"
- "setPredictedOptimalScore:"
- "setPredictedOptimalStartDate:"
- "setPreventDeviceSleep:"
- "setPreviousBatteryLevel:"
- "setPreviousDefaultThreshold:"
- "setPreviousExclusiveIdentifiers:"
- "setPreviousForegroundApps:"
- "setPreviousMaxThermalPressure:"
- "setPreviousPluginStatus:"
- "setPreviousSyncThreshold:"
- "setProcessingTaskIdentifiers:"
- "setProducedResultIdentifiers:"
- "setProgress:"
- "setProhibitExpensivePaths:"
- "setPublisher:"
- "setQueue:"
- "setRateLimitConfigurationName:"
- "setRateLimiter:"
- "setRateLimits:"
- "setRatelimitConfigurationName:"
- "setRationale:"
- "setReason:"
- "setRecentTrafficSyncRequests:"
- "setRecentlyBackgroundedApps:"
- "setRefreshAfterDate:"
- "setRefreshBeforeDate:"
- "setRefreshReason:"
- "setRegistrations:"
- "setRelatedApplications:"
- "setRemoteAppLaunchCount:"
- "setRemoteDevice:"
- "setRemoteDeviceIdentifier:"
- "setRemoteForecastDeletionToken:"
- "setRemoteObjectInterface:"
- "setRequestsApplicationLaunch:"
- "setRequestsExtensionLaunch:"
- "setRequestsImmediateRuntime:"
- "setRequestsNewsstandLaunch:"
- "setRequiresBuddyComplete:"
- "setRequiresDeviceInactivity:"
- "setRequiresInexpensiveNetworking:"
- "setRequiresNetwork:"
- "setRequiresPlugin:"
- "setRequiresRemoteDeviceWake:"
- "setRequiresSignificantUserInactivity:"
- "setRequiresUnconstrainedNetworking:"
- "setResources:"
- "setResubmitToken:"
- "setRunOnAppForeground:"
- "setRunQueue:"
- "setRunWhenAppLaunchUnlikely:"
- "setRunner:"
- "setSaveSpans:"
- "setSchedulerRecommendedApplications:"
- "setSchedulingPriority:"
- "setScore:"
- "setSemanticVersion:"
- "setServiceName:"
- "setShouldBePersisted:"
- "setShouldWakeDevice:"
- "setSpanMarkerBlock:"
- "setStartAfter:"
- "setStartBefore:"
- "setStartConditions:"
- "setStartDate:"
- "setStartHandler:"
- "setStartTime:"
- "setStartedActivities:"
- "setStartedInIdle:"
- "setStartedOnBattery:"
- "setStaticPriority:"
- "setSubmissionManager:"
- "setSubmissionStrategy:"
- "setSubmissionTimer:"
- "setSubmitDate:"
- "setSubmittedActivities:"
- "setSubmittedActivityTracker:"
- "setSubtitle:"
- "setSuccessful:"
- "setSupportsAnyApplication:"
- "setSuspendHandler:"
- "setSuspendRequestDate:"
- "setSuspendable:"
- "setSystemAddedWidgetBudgetIDs:"
- "setSystemAddedWidgetMaxBudget:"
- "setTargetDevice:"
- "setTesting:"
- "setTestingOverride:"
- "setThermalLevelElevated:"
- "setTimeStyle:"
- "setTimeUntilContentExpiration:"
- "setTimeZone:"
- "setTitle:"
- "setToken:"
- "setTotalUnitCount:"
- "setTransaction:"
- "setTransferSize:"
- "setTransform:"
- "setTriggersRestart:"
- "setUninterruptibleDuration:"
- "setUploadSize:"
- "setUrgencyLevel:"
- "setUseStatisticalModelForTriggersRestart:"
- "setUserIdentifier:"
- "setUserInfo:"
- "setUserInfoObject:forKey:"
- "setUserRequestedBackupTask:"
- "setUuid:"
- "setWasForceRun:"
- "setWatchKitAppStatus:"
- "setWatchKitStatus:forApplication:"
- "setWidgetBudgetID:"
- "setWidgetBudgetIdentifier:"
- "setWidgetID:"
- "setWidgetIdentifier:"
- "setWidgetMaxBudget:"
- "setWidgetOverrideKeypath:"
- "setWindow:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setWithObjectsFrom:"
- "setXPCType:forSelector:argumentIndex:ofReply:"
- "setXpcConnection:"
- "setupXPCConnectionWithEndpoint:"
- "sharedDateFormatter"
- "sharedDefaultEvaluator"
- "sharedDeviceConnection"
- "sharedInstance"
- "sharedLimiter"
- "sharedScheduler"
- "shortDescription"
- "shouldBePersisted"
- "shouldBypassApplicationUsage:"
- "shouldDelayGroupSubmissionOfActivity:"
- "shouldImposeDeviceInactivity"
- "shouldLimitActivityAtSubmission:"
- "shouldQueueActivity:"
- "shouldReplaceActivity:andKeepsSubmitted:"
- "significantlyOverdueAtDate:"
- "sinkWithCompletion:receiveInput:"
- "skipEvaluationIfUnplugged"
- "sortUsingComparator:"
- "sortedArrayUsingComparator:"
- "sortedArrayUsingSelector:"
- "source"
- "spanMarkerBlock"
- "standardDeviation"
- "standardDeviationWithMean:"
- "standardUserDefaults"
- "start"
- "startAfter"
- "startBefore"
- "startConditions"
- "startHandler"
- "startTime"
- "startedActivities"
- "startedActivities:"
- "startedInIdle"
- "startedOnBattery"
- "starting"
- "state"
- "staticPriority"
- "statistics"
- "statisticsWithHandler:"
- "status"
- "stop"
- "stringByAppendingString:"
- "stringByReplacingMatchesInString:options:range:withTemplate:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringForPriority:"
- "stringForThermalLevel:"
- "stringFromDate:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "submissionTimer"
- "submitActivities:"
- "submitActivities:withScheduler:"
- "submitActivitiesInternal:"
- "submitActivity:"
- "submitActivity:inGroup:"
- "submitActivity:inGroup:error:"
- "submitActivity:inGroup:withHandler:"
- "submitActivity:inGroup:withScheduler:"
- "submitActivity:inGroupWithName:"
- "submitActivity:withScheduler:"
- "submitActivityInternal:"
- "submitRateLimitConfiguration:"
- "submitRateLimitConfiguration:handler:"
- "submitRefreshActivity:"
- "submitTaskRequest:"
- "submitTaskRequest:withHandler:"
- "submitTaskRequestWithIdentifier:descriptor:completionHandler:"
- "submittedActivities"
- "submittedActivitiesWithHandler:"
- "submittedActivityTracker"
- "submittedFileProtection"
- "submittedTaskState"
- "substringFromIndex:"
- "substringToIndex:"
- "successful"
- "superclass"
- "supportsAnyApplication"
- "supportsSecureCoding"
- "suspend"
- "suspendActivities:"
- "suspendActivities: %@ activities were not running: %@"
- "suspendHandler"
- "suspendRequestDate"
- "suspensionExemptionsForActivity:"
- "suspensionThreshold"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemAddedWidgetMaxBudget"
- "targetDevice"
- "taskID"
- "testing"
- "testingOverride"
- "thermalLevelElevated"
- "thermalLevelsAllowSendingTrafficeForServiceIdentifiers:atPriorityLevel:"
- "thirdPartyAppPolicyAllowsSendingTrafficForServiceIdentifiers:atPriorityLevel:furtherChecksNecessary:"
- "timeIntervalSince1970"
- "timeIntervalSince1970WithTimeZoneOffset:"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeUntilContentExpiration"
- "timerHandler"
- "timestamp"
- "timewiseEligibleAtDate:"
- "token"
- "totalUnitCount"
- "trackActivity:"
- "transaction"
- "transferSize"
- "transferSizeType"
- "transform"
- "triggerScoreEvaluationAndRunActivities:"
- "triggerScoreEvaluationAndRunActivities:handler:"
- "triggersRestart"
- "uninterruptibleDuration"
- "unionSet:"
- "unprotectedEstablishDaemonConnectionIfInterrupted"
- "unregisterSystemTaskWithIdentifier:completionHandler:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "updateActivity:withLimitResponse:"
- "updateActivity:withParameters:"
- "updateAppUsageHistory"
- "updateBytesConsumedForActivity:withParameters:"
- "updateCapacity:forGroupName:"
- "updateGroupIfNecessary"
- "updateInternalGroups"
- "updateLimit:forActivity:forLimiterWithName:"
- "updateLimit:forActivity:forLimiterWithName:handler:"
- "updateOngoingTask:"
- "updateOngoingTask:completionHandler:"
- "updateProgress:forOngoingTask:"
- "updateProgressForOngoingTask:completionHandler:"
- "updateSystemConstraintsWithParameters:"
- "updateTaskRequestWithIdentifier:descriptor:completionHandler:"
- "uploadSize"
- "urgencyLevel"
- "usageLikelihoodForApplication:"
- "usageThresholdForPriority:batteryLevel:isPluggedIn:"
- "useStatisticalModelForTriggersRestart"
- "userContext"
- "userRequestedBackupTask"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@\"<_DASActivityBackgroundTasksSchedulerDelegate>\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSExtensionContext\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"_DASActivity\"16"
- "v24@0:8@\"_DASActivityGroup\"16"
- "v24@0:8@\"_DASActivityRateLimitConfiguration\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSObject<OS_xpc_object>\"@\"NSError\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"NSDictionary\"16B24"
- "v28@0:8@\"_DASActivity\"16B24"
- "v28@0:8@16B24"
- "v28@0:8B16@20"
- "v32@0:8@\"NSArray\"16@?<v@?B>24"
- "v32@0:8@\"NSDictionary\"16@?<v@?B>24"
- "v32@0:8@\"NSFileHandle\"16@?<v@?B>24"
- "v32@0:8@\"NSObject<OS_dispatch_queue>\"16@?<v@?@\"_DASHistogram\">24"
- "v32@0:8@\"NSOrderedSet\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSProgress\"16@\"_DASActivity\"24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSSet\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSSet\"16@?<v@?B>24"
- "v32@0:8@\"NSSet\"16q24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"_DASActivity\">24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?BB>24"
- "v32@0:8@\"NSString\"16@?<v@?d>24"
- "v32@0:8@\"NSString\"16d24"
- "v32@0:8@\"_DASActivity\"16@\"NSArray\"24"
- "v32@0:8@\"_DASActivity\"16@\"NSDictionary\"24"
- "v32@0:8@\"_DASActivity\"16@\"NSString\"24"
- "v32@0:8@\"_DASActivity\"16@\"_DASActivityGroup\"24"
- "v32@0:8@\"_DASActivity\"16@?<v@?>24"
- "v32@0:8@\"_DASActivity\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"_DASActivity\"16q24"
- "v32@0:8@\"_DASActivityRateLimitConfiguration\"16@?<v@?B>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16@?<v@?@\"NSArray\">24"
- "v32@0:8@16Q24"
- "v32@0:8@16d24"
- "v32@0:8@16q24"
- "v32@0:8Q16@24"
- "v32@0:8d16@\"NSString\"24"
- "v32@0:8d16@24"
- "v32@0:8q16@\"NSArray\"24"
- "v32@0:8q16@24"
- "v36@0:8@\"NSArray\"16B24@?<v@?@\"NSMutableArray\">28"
- "v36@0:8@\"NSDictionary\"16B24@?<v@?B>28"
- "v36@0:8@\"_DASActivity\"16B24@?<v@?>28"
- "v36@0:8@16B24@?28"
- "v36@0:8B16@\"NSSet\"20@?<v@?B>28"
- "v36@0:8B16@20@?28"
- "v40@0:8@\"NSDateInterval\"16@\"NSData\"24@?<v@?@\"NSArray\">32"
- "v40@0:8@\"NSDateInterval\"16@\"NSData\"24@?<v@?@\"NSDictionary\">32"
- "v40@0:8@\"NSString\"16@\"NSObject<OS_xpc_object>\"24@?<v@?B>32"
- "v40@0:8@\"NSString\"16@\"NSSet\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@24@?<v@?B>32"
- "v40@0:8@\"NSString\"16d24@?<v@?>32"
- "v40@0:8@\"NSString\"16d24@?<v@?B>32"
- "v40@0:8@\"_DASActivity\"16@\"_DASActivityGroup\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16d24@?32"
- "v40@0:8Q16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8Q16@24@?32"
- "v40@0:8Q16Q24@?32"
- "v40@0:8Q16Q24@?<v@?B@\"NSError\">32"
- "v48@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32@?<v@?@\"NSArray\">40"
- "v48@0:8@\"NSSet\"16@\"NSDateInterval\"24@\"NSData\"32@?<v@?@\"NSDictionary\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8Q16@\"NSDateInterval\"24@\"NSData\"32@?<v@?@\"NSDictionary\">40"
- "v48@0:8Q16@24@32@?40"
- "v48@0:8Q16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40"
- "v48@0:8Q16Q24@32@?40"
- "v48@0:8d16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
- "v48@0:8d16@24@32@?40"
- "v48@0:8{?=[8I]}16"
- "v64@0:8@\"NSString\"16Q24Q32Q40@\"NSString\"48@?<v@?B>56"
- "v64@0:8@16Q24Q32Q40@48@?56"
- "v80@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48Q56@\"NSNumber\"64@?<v@?B@\"NSError\">72"
- "v80@0:8@\"NSString\"16@\"NSString\"24Q32d40@\"NSNumber\"48Q56@\"NSNumber\"64@?<v@?B@\"NSError\">72"
- "v80@0:8@16@24@32@40@48Q56@64@?72"
- "v80@0:8@16@24Q32d40@48Q56@64@?72"
- "validClassesForUserInfoSerialization"
- "validateBGTaskRequestWithActivity:"
- "valueAtDate:"
- "valueForKey:"
- "valuesUntilEndDate:withIntervalDuration:"
- "viewFrom:to:forWidgetID:"
- "wasActivityAllowedToRun:"
- "wasForceRun"
- "watchBatteryLevel"
- "watchKitAppStatus"
- "weekday"
- "widgetBudgetIdentifier"
- "widgetIdentifier"
- "widgetMaxBudget"
- "widgetOverrideKeypath"
- "willExpireBGTaskActivities:"
- "xpcConnection"
- "zone"
- "{?=\"val\"[8I]}"
- "{?=[8I]}16@0:8"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"

```
