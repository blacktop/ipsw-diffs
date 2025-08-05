## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-652.0.0.0.0
-  __TEXT.__text: 0x77978
-  __TEXT.__auth_stubs: 0x17e0
-  __TEXT.__objc_methlist: 0x5f0c
-  __TEXT.__const: 0x858
-  __TEXT.__cstring: 0x6461
+2026.0.2.0.0
+  __TEXT.__text: 0x77c00
+  __TEXT.__auth_stubs: 0x17f0
+  __TEXT.__objc_methlist: 0x5f44
+  __TEXT.__const: 0x868
+  __TEXT.__cstring: 0x6551
   __TEXT.__gcc_except_tab: 0x2470
   __TEXT.__oslogstring: 0x8edd
   __TEXT.__swift5_typeref: 0x2f7

   __TEXT.__unwind_info: 0x1f28
   __TEXT.__eh_frame: 0x438
   __TEXT.__objc_classname: 0xbce
-  __TEXT.__objc_methname: 0x1160a
+  __TEXT.__objc_methname: 0x1176c
   __TEXT.__objc_methtype: 0x219b
-  __TEXT.__objc_stubs: 0xa6c0
+  __TEXT.__objc_stubs: 0xa740
   __DATA_CONST.__got: 0x750
-  __DATA_CONST.__const: 0x2740
+  __DATA_CONST.__const: 0x2748
   __DATA_CONST.__objc_classlist: 0x228
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3710
+  __DATA_CONST.__objc_selrefs: 0x3750
   __DATA_CONST.__objc_protorefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x1b8
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0xc00
+  __AUTH_CONST.__auth_got: 0xc08
   __AUTH_CONST.__const: 0xcb8
-  __AUTH_CONST.__cfstring: 0x2be0
-  __AUTH_CONST.__objc_const: 0x11440
-  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__cfstring: 0x2c40
+  __AUTH_CONST.__objc_const: 0x11490
+  __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2d0
-  __AUTH.__data: 0x220
-  __DATA.__objc_ivar: 0x708
-  __DATA.__data: 0xfa0
-  __DATA.__bss: 0xe30
-  __DATA_DIRTY.__objc_data: 0x1360
-  __DATA_DIRTY.__bss: 0xa8
+  __AUTH.__objc_data: 0x280
+  __AUTH.__data: 0xc0
+  __DATA.__objc_ivar: 0x710
+  __DATA.__data: 0xf68
+  __DATA.__bss: 0xdf0
+  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B95DFE7A-DA2C-395A-A7E8-166D80F5AFBE
-  Functions: 2790
-  Symbols:   9072
-  CStrings:  4125
+  UUID: C5E7C0EE-0A52-3C10-A23C-209DEE09F17F
+  Functions: 2795
+  Symbols:   9091
+  CStrings:  4147
 
Symbols:
+ -[ACHBackCompatRemoteAchievementAvailabilityKeyWriter keyValueDomain]
+ -[ACHBackCompatRemoteAchievementAvailabilityKeyWriter setKeyValueDomain:]
+ -[ACHRemoteTemplateAvailabilityKeyProvider keyValueDomain]
+ -[ACHRemoteTemplateAvailabilityKeyProvider setKeyValueDomain:]
+ -[ACHWorkoutAwardingSource _unit_test_setHistoricalRunCompleteVersion:]
+ -[ACHWorkoutAwardingSource isTinkerPaired]
+ -[ACHWorkoutAwardingSource overrideIsTinkerPaired]
+ -[ACHWorkoutAwardingSource setIsTinkerPaired:]
+ -[ACHWorkoutAwardingSource setOverrideIsTinkerPaired:]
+ _ACHWorkoutHistoricalRunCompleteVersion
+ _ACHWorkoutHistoricalRunCompleteVersionKey
+ _FIIsActivePairedDeviceSatellitePaired
+ _OBJC_IVAR_$_ACHBackCompatRemoteAchievementAvailabilityKeyWriter._keyValueDomain
+ _OBJC_IVAR_$_ACHRemoteTemplateAvailabilityKeyProvider._keyValueDomain
+ _OBJC_IVAR_$_ACHWorkoutAwardingSource._isTinkerPaired
+ _OBJC_IVAR_$_ACHWorkoutAwardingSource._overrideIsTinkerPaired
+ ___101+[ACHTemplateEntity _insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:]_block_invoke.434
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.304
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.309
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.310
+ ___30-[ACHMobileAssetProvider init]_block_invoke.297
+ ___30-[ACHMobileAssetProvider init]_block_invoke.297.cold.1
+ ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.308
+ ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.308.cold.1
+ ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.302
+ ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.302.cold.1
+ ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.303
+ ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.303.cold.1
+ ___56-[ACHTemplateAssetRegistry registerTemplateAssetSource:]_block_invoke.360
+ ___57-[ACHAchievementProgressEngine registerProgressProvider:]_block_invoke.344
+ ___58-[ACHMobileAssetProvider _fetchLocalAssetsWithCompletion:]_block_invoke.306
+ ___58-[ACHTemplateStore _queue_addTemplates:triggerSync:error:]_block_invoke.315
+ ___58-[ACHTemplateStore initWithClient:assertionClient:device:]_block_invoke.305
+ ___61-[ACHMindfulMinutesAwardingSource _runIncrementalEvaluation:]_block_invoke.314
+ ___62-[ACHTemplateSourceScheduler _listenForSignificantTimeChanges]_block_invoke.360
+ ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.326
+ ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.333
+ ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.328
+ ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.335
+ ___65-[ACHMonthlyChallengeTemplateSource templatesForDate:completion:]_block_invoke.306
+ ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.323
+ ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.324
+ ___66-[ACHEarnedInstanceCleanupUtility _historicalEvaluationAdjustment]_block_invoke.378
+ ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke.314
+ ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke_2.315
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.309
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.309.cold.1
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.309.cold.2
+ ___71-[ACHEarnedInstanceDuplicateUtility earnedInstancesLimitedByEarnLimit:]_block_invoke.296
+ ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.316
+ ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.327
+ ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.332
+ ___74-[ACHBackCompatMonthlyChallengeListener _readAndSaveBackCompatDefinitions]_block_invoke.310
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.350
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.350.cold.1
+ ___78-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToTemplateEntityToMigrator:]_block_invoke.589
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.405
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.406
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.406.cold.1
+ ___80-[ACHMonthlyChallengeEvaluationEnvironment eligibleSpecificWorkoutChallengeType]_block_invoke.292
+ ___84-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToEarnedInstanceEntityToMigrator:]_block_invoke.574
+ ___89-[ACHEarnedInstanceAwardingEngine requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.359
+ ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.374
+ ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.374.cold.1
+ ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.374.cold.2
+ ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke.309
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.381
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.382
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.402
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.403
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.307.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.308
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.308.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.309
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.309.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.309.cold.2
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.309.cold.3
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.310
+ ___block_literal_global.302
+ ___block_literal_global.303
+ ___block_literal_global.304
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.319
+ ___block_literal_global.320
+ ___block_literal_global.324
+ ___block_literal_global.328
+ ___block_literal_global.335
+ ___block_literal_global.336
+ ___block_literal_global.341
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.364
+ ___block_literal_global.365
+ ___block_literal_global.379
+ ___block_literal_global.381
+ ___block_literal_global.394
+ ___block_literal_global.408
+ ___block_literal_global.422
+ ___block_literal_global.430
+ ___block_literal_global.445
+ ___block_literal_global.549
+ ___block_literal_global.567
+ ___block_literal_global.585
+ ___block_literal_global.600
+ ___block_literal_global.605
+ ___block_literal_global.610
+ _objc_msgSend$initWithDomain:code:userInfo:
+ _objc_msgSend$isTinkerPaired
+ _objc_msgSend$keyValueDomain
+ _objc_msgSend$overrideIsTinkerPaired
- -[ACHBackCompatRemoteAchievementAvailabilityKeyWriter healthStore]
- -[ACHBackCompatRemoteAchievementAvailabilityKeyWriter setHealthStore:]
- -[ACHRemoteTemplateAvailabilityKeyProvider healthStore]
- -[ACHRemoteTemplateAvailabilityKeyProvider setHealthStore:]
- _OBJC_IVAR_$_ACHBackCompatRemoteAchievementAvailabilityKeyWriter._healthStore
- _OBJC_IVAR_$_ACHRemoteTemplateAvailabilityKeyProvider._healthStore
- ___101+[ACHTemplateEntity _insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:]_block_invoke.431
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.301
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.306
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.307
- ___30-[ACHMobileAssetProvider init]_block_invoke.294
- ___30-[ACHMobileAssetProvider init]_block_invoke.294.cold.1
- ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.305
- ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.305.cold.1
- ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.299
- ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.299.cold.1
- ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.300
- ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.300.cold.1
- ___56-[ACHTemplateAssetRegistry registerTemplateAssetSource:]_block_invoke.357
- ___57-[ACHAchievementProgressEngine registerProgressProvider:]_block_invoke.341
- ___58-[ACHMobileAssetProvider _fetchLocalAssetsWithCompletion:]_block_invoke.303
- ___58-[ACHTemplateStore _queue_addTemplates:triggerSync:error:]_block_invoke.312
- ___58-[ACHTemplateStore initWithClient:assertionClient:device:]_block_invoke.302
- ___61-[ACHMindfulMinutesAwardingSource _runIncrementalEvaluation:]_block_invoke.311
- ___62-[ACHTemplateSourceScheduler _listenForSignificantTimeChanges]_block_invoke.357
- ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.323
- ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.330
- ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.325
- ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.332
- ___65-[ACHMonthlyChallengeTemplateSource templatesForDate:completion:]_block_invoke.303
- ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.320
- ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.321
- ___66-[ACHEarnedInstanceCleanupUtility _historicalEvaluationAdjustment]_block_invoke.375
- ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke.311
- ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke_2.312
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.303
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.306.cold.1
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.306.cold.2
- ___71-[ACHEarnedInstanceDuplicateUtility earnedInstancesLimitedByEarnLimit:]_block_invoke.293
- ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.310
- ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.324
- ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.329
- ___74-[ACHBackCompatMonthlyChallengeListener _readAndSaveBackCompatDefinitions]_block_invoke.307
- ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.341
- ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.341.cold.1
- ___78-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToTemplateEntityToMigrator:]_block_invoke.586
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.402
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.403
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.403.cold.1
- ___80-[ACHMonthlyChallengeEvaluationEnvironment eligibleSpecificWorkoutChallengeType]_block_invoke.289
- ___84-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToEarnedInstanceEntityToMigrator:]_block_invoke.571
- ___89-[ACHEarnedInstanceAwardingEngine requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.356
- ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.371
- ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.371.cold.1
- ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.371.cold.2
- ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke.306
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.378
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.379
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.399
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.400
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.304
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.304.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.305
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.305.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.306
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.306.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.306.cold.2
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.306.cold.3
- ___block_literal_global.291
- ___block_literal_global.292
- ___block_literal_global.293
- ___block_literal_global.306
- ___block_literal_global.307
- ___block_literal_global.314
- ___block_literal_global.315
- ___block_literal_global.316
- ___block_literal_global.325
- ___block_literal_global.326
- ___block_literal_global.333
- ___block_literal_global.338
- ___block_literal_global.340
- ___block_literal_global.345
- ___block_literal_global.351
- ___block_literal_global.356
- ___block_literal_global.361
- ___block_literal_global.362
- ___block_literal_global.376
- ___block_literal_global.378
- ___block_literal_global.391
- ___block_literal_global.405
- ___block_literal_global.419
- ___block_literal_global.427
- ___block_literal_global.442
- ___block_literal_global.546
- ___block_literal_global.564
- ___block_literal_global.582
- ___block_literal_global.597
- ___block_literal_global.602
- ___block_literal_global.607
CStrings:
+ "1["
+ "T@\"HKKeyValueDomain\",&,N,V_keyValueDomain"
+ "T@\"NSNumber\",&,N,V_overrideIsTinkerPaired"
+ "TB,N,V_isTinkerPaired"
+ "Unable to run historical run on watch because minimum version for phone historical run (%ld) is lower than expected version (%ld)"
+ "WorkoutHistoricalRunCompleteVersion"
+ "_isTinkerPaired"
+ "_keyValueDomain"
+ "_overrideIsTinkerPaired"
+ "_unit_test_setHistoricalRunCompleteVersion:"
+ "com.apple.Achievements.workout-awarding-source"
+ "initWithDomain:code:userInfo:"
+ "isTinkerPaired"
+ "keyValueDomain"
+ "overrideIsTinkerPaired"
+ "setIsTinkerPaired:"
+ "setKeyValueDomain:"
+ "setOverrideIsTinkerPaired:"
- "1Z"

```
