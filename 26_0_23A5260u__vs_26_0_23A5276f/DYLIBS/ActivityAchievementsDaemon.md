## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-643.0.1.0.0
-  __TEXT.__text: 0x7806c
+646.0.0.0.0
+  __TEXT.__text: 0x780e8
   __TEXT.__auth_stubs: 0x17e0
   __TEXT.__objc_methlist: 0x6024
   __TEXT.__const: 0x858
   __TEXT.__cstring: 0x6481
-  __TEXT.__gcc_except_tab: 0x2448
+  __TEXT.__gcc_except_tab: 0x2450
   __TEXT.__oslogstring: 0x8fad
   __TEXT.__swift5_typeref: 0x2f7
   __TEXT.__swift5_capture: 0x24

   __TEXT.__objc_methtype: 0x222a
   __TEXT.__objc_stubs: 0xa740
   __DATA_CONST.__got: 0x740
-  __DATA_CONST.__const: 0x2758
+  __DATA_CONST.__const: 0x2738
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x140

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A0B400F5-0CEC-39CA-8823-4CBE44E68F04
+  UUID: D2F9F696-4DF8-3D4B-88BC-042D0AA0FDA0
   Functions: 2821
-  Symbols:   9200
+  Symbols:   9192
   CStrings:  4155
 
Symbols:
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
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.344
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.344.cold.1
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
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ActivityAchievementsDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ActivityAchievementsDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ActivityAchievementsDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ActivityAchievementsDaemon
Functions:
~ -[ACHMonthlyChallengeAwardingSource _earnedInstancesForInterval:] : 1872 -> 1896
~ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.301 -> ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.304 : 1616 -> 1644
~ -[ACHWorkoutIterator _runQueryForDateInterval:lastCursor:completion:] : 808 -> 824
~ -[ACHAchievementStore _performWithLock:] : 88 -> 116
~ ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke : 832 -> 856
~ ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.310 -> ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.313 : 268 -> 272

```
