## ActivityAchievementsDaemon

> `/System/Library/PrivateFrameworks/ActivityAchievementsDaemon.framework/ActivityAchievementsDaemon`

```diff

-573.2.0.0.0
+573.3.0.0.0
   __TEXT.__text: 0x7bd38
   __TEXT.__auth_stubs: 0x1120
   __TEXT.__objc_methlist: 0x6594

   __TEXT.__oslogstring: 0x9c23
   __TEXT.__unwind_info: 0x21a8
   __TEXT.__objc_classname: 0xd85
-  __TEXT.__objc_methname: 0x13c7d
+  __TEXT.__objc_methname: 0x13c97
   __TEXT.__objc_methtype: 0x27ce
   __TEXT.__objc_stubs: 0xb7e0
   __DATA_CONST.__got: 0x368

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x15278
   __DATA_CONST.__objc_selrefs: 0x3ba0
+  __DATA_CONST.__objc_protorefs: 0x90
+  __DATA_CONST.__objc_classrefs: 0x390
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x198
   __AUTH_CONST.__objc_const: 0x17e0
   __AUTH_CONST.__cfstring: 0x2d80

   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0x8a0
   __AUTH.__objc_data: 0x230
-  __DATA.__objc_protorefs: 0x90
-  __DATA.__objc_classrefs: 0x390
-  __DATA.__objc_superrefs: 0x1e8
   __DATA.__objc_ivar: 0x818
   __DATA.__data: 0x10e0
   __DATA.__bss: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: DD8DCE17-42B1-35F5-AE44-EFF6874E1496
+  UUID: B668CA96-81A4-3E1C-8979-1B504075E180
   Functions: 3117
   Symbols:   10489
-  CStrings:  4488
+  CStrings:  4489
 
Symbols:
+ ___101+[ACHTemplateEntity _insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:]_block_invoke.383
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.253
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.258
+ ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.259
+ ___123-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:databaseContext:evaluationBlock:completion:]_block_invoke.260
+ ___123-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:databaseContext:evaluationBlock:completion:]_block_invoke.261
+ ___30-[ACHMobileAssetProvider init]_block_invoke.240
+ ___30-[ACHMobileAssetProvider init]_block_invoke.240.cold.1
+ ___37-[ACHGizmoAwardingScheduler _startUp]_block_invoke.248
+ ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.251
+ ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.251.cold.1
+ ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.245
+ ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.245.cold.1
+ ___51-[ACHTemplateAssetRegistry registerTemplateSource:]_block_invoke.84
+ ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.252
+ ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.252.cold.1
+ ___56-[ACHTemplateAssetRegistry registerTemplateAssetSource:]_block_invoke.93
+ ___57-[ACHAchievementProgressEngine registerProgressProvider:]_block_invoke.293
+ ___58-[ACHMobileAssetProvider _fetchLocalAssetsWithCompletion:]_block_invoke.249
+ ___58-[ACHTemplateStore initWithClient:assertionClient:device:]_block_invoke.250
+ ___61-[ACHMindfulMinutesAwardingSource _runIncrementalEvaluation:]_block_invoke.263
+ ___62-[ACHTemplateSourceScheduler _listenForSignificantTimeChanges]_block_invoke.328
+ ___63-[ACHCompanionAwardingScheduler _runXPCActivityWithCompletion:]_block_invoke.274
+ ___63-[ACHCompanionAwardingScheduler _runXPCActivityWithCompletion:]_block_invoke.275
+ ___65-[ACHTinkerAwardingScheduler performPeriodicActivity:completion:]_block_invoke.270
+ ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke.260
+ ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke_2.261
+ ___68-[ACHCompanionAwardingScheduler performPeriodicActivity:completion:]_block_invoke.276
+ ___69-[ACHDataStore _queue_daemon_populateFromDatabaseForProviders:error:]_block_invoke.287
+ ___69-[ACHTinkerAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.283
+ ___69-[ACHTinkerAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.290
+ ___69-[ACHTinkerAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.292
+ ___69-[ACHTinkerAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.294
+ ___69-[ACHTinkerAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.295
+ ___71-[ACHEarnedInstanceDuplicateUtility earnedInstancesLimitedByEarnLimit:]_block_invoke.245
+ ___71-[ACHSyncingMonthlyChallengeTemplateCache _daemon_cacheTemplate:error:]_block_invoke.266
+ ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.265
+ ___72-[ACHCompanionAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.289
+ ___72-[ACHCompanionAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.296
+ ___72-[ACHCompanionAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.298
+ ___72-[ACHCompanionAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.300
+ ___72-[ACHCompanionAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.301
+ ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.273
+ ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.278
+ ___73-[ACHEarnedInstanceCleanupUtility _client_historicalEvaluationAdjustment]_block_invoke.325
+ ___74-[ACHBackCompatMonthlyChallengeListener _readAndSaveBackCompatDefinitions]_block_invoke.256
+ ___77-[ACHEarnedInstanceStore _queue_appendOrInsertEarnedInstanceToInMemoryStore:]_block_invoke.259
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.277
+ ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.277.cold.1
+ ___78-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToTemplateEntityToMigrator:]_block_invoke.535
+ ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.351
+ ___82-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:databaseContext:]_block_invoke.269
+ ___84-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToEarnedInstanceEntityToMigrator:]_block_invoke.520
+ ___85-[ACHTemplateStore _queue_addTemplates:provenance:databaseContext:triggerSync:error:]_block_invoke.261
+ ___87-[ACHTinkerAwardingScheduler _daemon_scheduleMaintenanceTaskForAwardingWithCompletion:]_block_invoke.278
+ ___90-[ACHCompanionAwardingScheduler _daemon_scheduleMaintenanceTaskForAwardingWithCompletion:]_block_invoke.284
+ ___90-[ACHTemplateStore _queue_daemon_addTemplatesToDatabase:provenance:databaseContext:error:]_block_invoke.281
+ ___90-[ACHTemplateStore _queue_daemon_addTemplatesToDatabase:provenance:databaseContext:error:]_block_invoke.281.cold.1
+ ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke.259
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.346
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.347
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.348
+ ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.349
+ ___94-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:databaseContext:completion:]_block_invoke.353
+ ___97-[ACHEarnedInstanceAwardingEngine _client_requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.323
+ ___97-[ACHEarnedInstanceAwardingEngine _daemon_requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.327
+ ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.267
+ ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.268
+ ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.268.cold.1
+ ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.268.cold.2
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.249
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.249.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.250
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.250.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.251
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.251.cold.1
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.251.cold.2
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.251.cold.3
+ ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.252
+ ___block_literal_global.245
+ ___block_literal_global.248
+ ___block_literal_global.249
+ ___block_literal_global.253
+ ___block_literal_global.255
+ ___block_literal_global.262
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.267
+ ___block_literal_global.270
+ ___block_literal_global.271
+ ___block_literal_global.274
+ ___block_literal_global.278
+ ___block_literal_global.282
+ ___block_literal_global.292
+ ___block_literal_global.300
+ ___block_literal_global.305
+ ___block_literal_global.310
+ ___block_literal_global.311
+ ___block_literal_global.321
+ ___block_literal_global.325
+ ___block_literal_global.327
+ ___block_literal_global.340
+ ___block_literal_global.354
+ ___block_literal_global.368
+ ___block_literal_global.376
+ ___block_literal_global.391
+ ___block_literal_global.495
+ ___block_literal_global.513
+ ___block_literal_global.531
+ ___block_literal_global.546
+ ___block_literal_global.551
+ ___block_literal_global.556
+ __unnamed_array_storage.300
+ __unnamed_array_storage.461
- ___101+[ACHTemplateEntity _insertTemplates:provenance:useLegacySyncIdentity:profile:databaseContext:error:]_block_invoke.359
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.229
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.234
- ___107-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:evaluationBlock:completion:]_block_invoke.235
- ___123-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:databaseContext:evaluationBlock:completion:]_block_invoke.236
- ___123-[ACHEarnedInstanceAwardingSourceRecord addEvaluationOperationWithDateInterval:databaseContext:evaluationBlock:completion:]_block_invoke.237
- ___30-[ACHMobileAssetProvider init]_block_invoke.216
- ___30-[ACHMobileAssetProvider init]_block_invoke.216.cold.1
- ___37-[ACHGizmoAwardingScheduler _startUp]_block_invoke.224
- ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.227
- ___47-[ACHMobileAssetProvider downloadRemoteCatalog]_block_invoke.227.cold.1
- ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.221
- ___50-[ACHMobileAssetProvider purgeAllDownloadedAssets]_block_invoke.221.cold.1
- ___51-[ACHTemplateAssetRegistry registerTemplateSource:]_block_invoke.83
- ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.228
- ___52-[ACHMindfulMinutesAwardingSource _startSampleQuery]_block_invoke.228.cold.1
- ___56-[ACHTemplateAssetRegistry registerTemplateAssetSource:]_block_invoke.92
- ___57-[ACHAchievementProgressEngine registerProgressProvider:]_block_invoke.268
- ___58-[ACHMobileAssetProvider _fetchLocalAssetsWithCompletion:]_block_invoke.225
- ___58-[ACHTemplateStore initWithClient:assertionClient:device:]_block_invoke.226
- ___61-[ACHMindfulMinutesAwardingSource _runIncrementalEvaluation:]_block_invoke.239
- ___62-[ACHTemplateSourceScheduler _listenForSignificantTimeChanges]_block_invoke.303
- ___63-[ACHCompanionAwardingScheduler _runXPCActivityWithCompletion:]_block_invoke.250
- ___63-[ACHCompanionAwardingScheduler _runXPCActivityWithCompletion:]_block_invoke.251
- ___65-[ACHTinkerAwardingScheduler performPeriodicActivity:completion:]_block_invoke.246
- ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke.236
- ___68-[ACHAwardsServer remote_addTemplates:removingTemplates:completion:]_block_invoke_2.237
- ___68-[ACHCompanionAwardingScheduler performPeriodicActivity:completion:]_block_invoke.252
- ___69-[ACHDataStore _queue_daemon_populateFromDatabaseForProviders:error:]_block_invoke.263
- ___69-[ACHTinkerAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.259
- ___69-[ACHTinkerAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.266
- ___69-[ACHTinkerAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.268
- ___69-[ACHTinkerAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.270
- ___69-[ACHTinkerAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.271
- ___71-[ACHEarnedInstanceDuplicateUtility earnedInstancesLimitedByEarnLimit:]_block_invoke.221
- ___71-[ACHSyncingMonthlyChallengeTemplateCache _daemon_cacheTemplate:error:]_block_invoke.242
- ___72-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:error:]_block_invoke.241
- ___72-[ACHCompanionAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.265
- ___72-[ACHCompanionAwardingScheduler _queue_client_requestAwardingEvaluation]_block_invoke.272
- ___72-[ACHCompanionAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.274
- ___72-[ACHCompanionAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.276
- ___72-[ACHCompanionAwardingScheduler _queue_daemon_requestAwardingEvaluation]_block_invoke.277
- ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.249
- ___73-[ACHDatabaseSchemaProvider _addValidateEarnedInstanceRowStepToMigrator:]_block_invoke.254
- ___73-[ACHEarnedInstanceCleanupUtility _client_historicalEvaluationAdjustment]_block_invoke.301
- ___74-[ACHBackCompatMonthlyChallengeListener _readAndSaveBackCompatDefinitions]_block_invoke.232
- ___77-[ACHEarnedInstanceStore _queue_appendOrInsertEarnedInstanceToInMemoryStore:]_block_invoke.235
- ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.253
- ___77-[ACHWorkoutAwardingSource _lock_startWorkoutQueryWithInitialResultsHandler:]_block_invoke.253.cold.1
- ___78-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToTemplateEntityToMigrator:]_block_invoke.511
- ___78-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:completion:]_block_invoke.326
- ___82-[ACHActivityAwardingSource earnedInstancesForHistoricalInterval:databaseContext:]_block_invoke.245
- ___84-[ACHDatabaseSchemaProvider _addSyncIdentityColumnToEarnedInstanceEntityToMigrator:]_block_invoke.496
- ___85-[ACHTemplateStore _queue_addTemplates:provenance:databaseContext:triggerSync:error:]_block_invoke.237
- ___87-[ACHTinkerAwardingScheduler _daemon_scheduleMaintenanceTaskForAwardingWithCompletion:]_block_invoke.254
- ___90-[ACHCompanionAwardingScheduler _daemon_scheduleMaintenanceTaskForAwardingWithCompletion:]_block_invoke.260
- ___90-[ACHTemplateStore _queue_daemon_addTemplatesToDatabase:provenance:databaseContext:error:]_block_invoke.257
- ___90-[ACHTemplateStore _queue_daemon_addTemplatesToDatabase:provenance:databaseContext:error:]_block_invoke.257.cold.1
- ___91-[ACHActivityAwardingSource _queue_updateDataProvider:forDateInterval:awardingBlock:error:]_block_invoke.235
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.321
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.322
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke.323
- ___91-[ACHEarnedInstanceAwardingEngine _requestHistoricalEvaluationForAllSourcesWithCompletion:]_block_invoke_2.324
- ___94-[ACHEarnedInstanceAwardingEngine _queue_evaluateHistoryForSource:databaseContext:completion:]_block_invoke.328
- ___97-[ACHEarnedInstanceAwardingEngine _client_requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.298
- ___97-[ACHEarnedInstanceAwardingEngine _daemon_requestIncrementalEvaluationForSource:evaluationBlock:]_block_invoke.302
- ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.243
- ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.244
- ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.244.cold.1
- ___97-[ACHEarnedInstanceStore _queue_addEarnedInstances:provenance:databaseContext:triggerSync:error:]_block_invoke.244.cold.2
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.225
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.225.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.226
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.226.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.227
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.227.cold.1
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.227.cold.2
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.227.cold.3
- ___98-[ACHActivityTriggerGenerator _incrementWithInitialState:forGoalType:dataProvider:goalMetHandler:]_block_invoke.228
- ___block_literal_global.219
- ___block_literal_global.220
- ___block_literal_global.221
- ___block_literal_global.222
- ___block_literal_global.223
- ___block_literal_global.224
- ___block_literal_global.225
- ___block_literal_global.226
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.238
- ___block_literal_global.239
- ___block_literal_global.240
- ___block_literal_global.242
- ___block_literal_global.254
- ___block_literal_global.257
- ___block_literal_global.258
- ___block_literal_global.276
- ___block_literal_global.279
- ___block_literal_global.286
- ___block_literal_global.297
- ___block_literal_global.301
- ___block_literal_global.316
- ___block_literal_global.330
- ___block_literal_global.344
- ___block_literal_global.352
- ___block_literal_global.367
- ___block_literal_global.471
- ___block_literal_global.489
- ___block_literal_global.507
- ___block_literal_global.522
- ___block_literal_global.527
- ___block_literal_global.532
- __unnamed_array_storage.276
- __unnamed_array_storage.437
CStrings:
+ "T@\"NSObject<ACHTemplateAssetSourceDelegate>\",?,W,N"
+ "T@\"NSObject<ACHTemplateAssetSourceDelegate>\",?,W,N,VassetSourceDelegate"
+ "T@\"NSObject<ACHTemplateSourceDelegate>\",?,W,N"
+ "T@\"NSObject<ACHTemplateSourceDelegate>\",?,W,N,Vdelegate"
+ "T@\"NSString\",?,R,C"
- "T@\"NSObject<ACHTemplateAssetSourceDelegate>\",W,N"
- "T@\"NSObject<ACHTemplateAssetSourceDelegate>\",W,N,VassetSourceDelegate"
- "T@\"NSObject<ACHTemplateSourceDelegate>\",W,N"
- "T@\"NSObject<ACHTemplateSourceDelegate>\",W,N,Vdelegate"

```
