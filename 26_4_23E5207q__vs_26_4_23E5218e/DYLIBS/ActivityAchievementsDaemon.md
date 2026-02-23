## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-2026.4.9.0.0
-  __TEXT.__text: 0x7eef8
+2026.4.10.0.0
+  __TEXT.__text: 0x7efd0
   __TEXT.__auth_stubs: 0x1880
   __TEXT.__objc_methlist: 0x60b4
   __TEXT.__const: 0x958

   __TEXT.__objc_methtype: 0x2341
   __TEXT.__objc_stubs: 0xab00
   __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0x2720
+  __DATA_CONST.__const: 0x2718
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x140

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 66F8CD1B-2E91-3715-BB03-6E85D2042051
+  UUID: 539B7EB1-DD34-39DF-BA36-3DCD8142A534
   Functions: 2834
-  Symbols:   9359
+  Symbols:   9357
   CStrings:  4187
 
Symbols:
+ ___101+[ACHTemplateEntity _insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:]_block_invoke.482
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.352
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.357
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.358
+ ___30-[ACHMobileAssetProvider init]_block_invoke.352
+ ___30-[ACHMobileAssetProvider init]_block_invoke.352.cold.1
+ ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.363
+ ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.363.cold.1
+ ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.357
+ ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.357.cold.1
+ ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.351
+ ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.351.cold.1
+ ___56-[ACHTemplateAssetRegistry registerTemplateAssetSource:]_block_invoke.408
+ ___57-[ACHAchievementProgressEngine registerProgressProvider:]_block_invoke.392
+ ___58-[ACHMobileAssetProvider _fetchLocalAssetsWithCompletion:]_block_invoke.361
+ ___58-[ACHTemplateStore _queue_addTemplates:triggerSync:error:]_block_invoke.363
+ ___58-[ACHTemplateStore initWithClient:assertionClient:device:]_block_invoke.353
+ ___61-[ACHMindfulMinutesAwardingSource _runIncrementalEvaluation:]_block_invoke.362
+ ___62-[ACHTemplateSourceScheduler _listenForSignificantTimeChanges]_block_invoke.408
+ ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.374
+ ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.381
+ ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.376
+ ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.383
+ ___65-[ACHMonthlyChallengeTemplateSource templatesForDate:completion:]_block_invoke.354
+ ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.371
+ ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.372
+ ___66-[ACHEarnedInstanceCleanupUtility _historicalEvaluationAdjustment]_block_invoke.426
+ ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke.362
+ ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke_2.363
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.354
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.357
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.357.cold.1
+ ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.357.cold.2
+ ___71-[ACHEarnedInstanceDuplicateUtility earnedInstancesLimitedByEarnLimit:]_block_invoke.344
+ ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.361
+ ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.364
+ ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.375
+ ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.380
+ ___74-[ACHBackCompatMonthlyChallengeListener _readAndSaveBackCompatDefinitions]_block_invoke.358
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.398
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.398.cold.1
+ ___78-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToTemplateEntityToMigrator:]_block_invoke.637
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.453
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.454
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.455
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.455.cold.1
+ ___80-[ACHMonthlyChallengeEvaluationEnvironment eligibleSpecificWorkoutChallengeType]_block_invoke.340
+ ___84-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToEarnedInstanceEntityToMigrator:]_block_invoke.622
+ ___89-[ACHEarnedInstanceAwardingEngine requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.407
+ ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.422
+ ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.422.cold.1
+ ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.422.cold.2
+ ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke.357
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.429
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.430
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.450
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.451
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.355
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.355.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.356
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.356.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.357
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.357.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.357.cold.2
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.357.cold.3
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.358
+ ___block_literal_global.342
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.372
+ ___block_literal_global.376
+ ___block_literal_global.377
+ ___block_literal_global.380
+ ___block_literal_global.383
+ ___block_literal_global.384
+ ___block_literal_global.389
+ ___block_literal_global.391
+ ___block_literal_global.394
+ ___block_literal_global.396
+ ___block_literal_global.402
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.412
+ ___block_literal_global.413
+ ___block_literal_global.427
+ ___block_literal_global.429
+ ___block_literal_global.442
+ ___block_literal_global.456
+ ___block_literal_global.470
+ ___block_literal_global.478
+ ___block_literal_global.493
+ ___block_literal_global.597
+ ___block_literal_global.615
+ ___block_literal_global.633
+ ___block_literal_global.648
+ ___block_literal_global.653
+ ___block_literal_global.658
- ___101+[ACHTemplateEntity _insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:]_block_invoke.443
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.313
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.318
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.319
- ___30-[ACHMobileAssetProvider init]_block_invoke.313
- ___30-[ACHMobileAssetProvider init]_block_invoke.313.cold.1
- ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.324
- ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.324.cold.1
- ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.318
- ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.318.cold.1
- ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.312
- ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.312.cold.1
- ___56-[ACHTemplateAssetRegistry registerTemplateAssetSource:]_block_invoke.369
- ___57-[ACHAchievementProgressEngine registerProgressProvider:]_block_invoke.353
- ___58-[ACHMobileAssetProvider _fetchLocalAssetsWithCompletion:]_block_invoke.322
- ___58-[ACHTemplateStore _queue_addTemplates:triggerSync:error:]_block_invoke.324
- ___58-[ACHTemplateStore initWithClient:assertionClient:device:]_block_invoke.314
- ___61-[ACHMindfulMinutesAwardingSource _runIncrementalEvaluation:]_block_invoke.323
- ___62-[ACHTemplateSourceScheduler _listenForSignificantTimeChanges]_block_invoke.369
- ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.335
- ___62-[ACHTinkerAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.342
- ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.337
- ___65-[ACHCompanionAwardingScheduler _queue_requestAwardingEvaluation]_block_invoke.344
- ___65-[ACHMonthlyChallengeTemplateSource templatesForDate:completion:]_block_invoke.315
- ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.332
- ___66-[ACHCompanionAwardingScheduler _runBackgroundTaskWithCompletion:]_block_invoke.333
- ___66-[ACHEarnedInstanceCleanupUtility _historicalEvaluationAdjustment]_block_invoke.387
- ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke.323
- ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke_2.324
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.315
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.318
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.318.cold.1
- ___70-[ACHEarnedInstanceStore _queue_addEarnedInstances:triggerSync:error:]_block_invoke.318.cold.2
- ___71-[ACHEarnedInstanceDuplicateUtility earnedInstancesLimitedByEarnLimit:]_block_invoke.305
- ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.322
- ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.325
- ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.336
- ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.341
- ___74-[ACHBackCompatMonthlyChallengeListener _readAndSaveBackCompatDefinitions]_block_invoke.319
- ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.359
- ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.359.cold.1
- ___78-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToTemplateEntityToMigrator:]_block_invoke.598
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.414
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.415
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.416
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.416.cold.1
- ___80-[ACHMonthlyChallengeEvaluationEnvironment eligibleSpecificWorkoutChallengeType]_block_invoke.301
- ___84-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToEarnedInstanceEntityToMigrator:]_block_invoke.583
- ___89-[ACHEarnedInstanceAwardingEngine requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.368
- ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.383
- ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.383.cold.1
- ___90-[ACHEarnedInstanceAwardingEngine requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.383.cold.2
- ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke.318
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.390
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.391
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.411
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.412
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.316
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.316.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.317
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.317.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.318
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.318.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.318.cold.2
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.318.cold.3
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.319
- ___block_literal_global.303
- ___block_literal_global.304
- ___block_literal_global.305
- ___block_literal_global.306
- ___block_literal_global.307
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.311
- ___block_literal_global.312
- ___block_literal_global.313
- ___block_literal_global.316
- ___block_literal_global.318
- ___block_literal_global.321
- ___block_literal_global.326
- ___block_literal_global.327
- ___block_literal_global.328
- ___block_literal_global.329
- ___block_literal_global.330
- ___block_literal_global.333
- ___block_literal_global.334
- ___block_literal_global.337
- ___block_literal_global.338
- ___block_literal_global.341
- ___block_literal_global.363
- ___block_literal_global.374
- ___block_literal_global.388
- ___block_literal_global.390
- ___block_literal_global.403
- ___block_literal_global.417
- ___block_literal_global.431
- ___block_literal_global.439
- ___block_literal_global.454
- ___block_literal_global.558
- ___block_literal_global.576
- ___block_literal_global.594
- ___block_literal_global.609
- ___block_literal_global.614
- ___block_literal_global.619
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_ActivityAchievementsDaemon
Functions:
~ sub_228d98c10 -> sub_228e13bc8 : 876 -> 932
~ sub_228d9a208 -> sub_228e151f8 : 6568 -> 6524
~ sub_228da5074 -> sub_228e20038 : 11560 -> 11764

```
