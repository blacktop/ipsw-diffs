## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-396.4.1.0.0
-  __TEXT.__text: 0x1545d0
+399.7.0.0.0
+  __TEXT.__text: 0x154ce8
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0xa320
-  __TEXT.__const: 0xce8
-  __TEXT.__gcc_except_tab: 0x76e4
-  __TEXT.__cstring: 0x14f76
-  __TEXT.__oslogstring: 0x1cac1
+  __TEXT.__objc_methlist: 0xa2f0
+  __TEXT.__const: 0xdf8
+  __TEXT.__gcc_except_tab: 0x77b8
+  __TEXT.__cstring: 0x14ff2
+  __TEXT.__oslogstring: 0x1cc02
   __TEXT.__dlopen_cstrs: 0x74
-  __TEXT.__unwind_info: 0x42ac
-  __TEXT.__objc_classname: 0x23ac
-  __TEXT.__objc_methname: 0x1c513
-  __TEXT.__objc_methtype: 0x4fc8
-  __TEXT.__objc_stubs: 0x13940
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x6a08
-  __DATA_CONST.__objc_classlist: 0x878
+  __TEXT.__unwind_info: 0x42d4
+  __TEXT.__objc_classname: 0x235c
+  __TEXT.__objc_methname: 0x1c597
+  __TEXT.__objc_methtype: 0x500b
+  __TEXT.__objc_stubs: 0x13960
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0x6a70
+  __DATA_CONST.__objc_classlist: 0x868
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10690
-  __DATA_CONST.__objc_selrefs: 0x5718
+  __DATA_CONST.__objc_const: 0x105c0
+  __DATA_CONST.__objc_selrefs: 0x5730
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0xda0
+  __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x390
-  __AUTH_CONST.__cfstring: 0xd140
-  __AUTH_CONST.__objc_const: 0x6b38
+  __AUTH_CONST.__cfstring: 0xd1c0
+  __AUTH_CONST.__objc_const: 0x6aa8
   __AUTH_CONST.__const: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x2b8
-  __AUTH_CONST.__objc_intobj: 0x888
+  __AUTH_CONST.__objc_intobj: 0x8a0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x778
-  __AUTH.__objc_data: 0x1928
+  __AUTH.__objc_data: 0x18d8
   __AUTH.__data: 0x870
-  __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0xdc0
-  __DATA.__objc_superrefs: 0x578
-  __DATA.__objc_ivar: 0xa0c
+  __DATA.__objc_ivar: 0x9fc
   __DATA.__data: 0x21a0
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x390
-  __DATA_DIRTY.__objc_data: 0x3b88
+  __DATA_DIRTY.__objc_data: 0x3b38
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: F285B274-6264-31A4-BB1E-7C60B5D7B68C
-  Functions: 4661
-  Symbols:   16564
-  CStrings:  10009
+  UUID: 7B90B562-29B4-3062-9561-3760D8AE9136
+  Functions: 4666
+  Symbols:   16554
+  CStrings:  10017
 
Symbols:
+ +[TRITaskUtils updateExperimentHistoryDatabaseWithAllocationStatus:forExperiment:treatment:deployment:experimentRecord:isBecomingObsolete:categoricalMetric:context:]
+ -[TRIAggregateFetchRecordsProgress initWithProgressBlockForTesting:guardedData:lock:dispatchQueue:]
+ -[TRIDServer _logMetrics:]
+ -[TRIExperimentDatabase enumerateExperimentRecordsMatchingNamespaceName:block:]
+ -[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]
+ -[TRINamespaceResolverStorage promoteFactorPackId:forNamespaceName:rolloutDeployment:error:]
+ -[TRINamespaceResolverStorage rejectFactorPackId:forNamespaceName:rolloutDeployment:error:]
+ -[TRIRetargetAllTask _shouldRetargetWithRecord:]
+ -[TRISqliteErrorHandler initWithStorageManagement:defaultErrorHandler:]
+ -[TRIUrgentRollbackScheduler _validRollbackDeploymentsForRollbackExperiment:deploymentIds:]
+ -[TRIUrgentRollbackScheduler experimentDatabase]
+ -[TRIUrgentRollbackScheduler initWithExperimentDatabase:taskQueue:]
+ -[TRIUrgentRollbackScheduler scheduleUrgentRollbackForExperiment:deploymentIds:]
+ -[TRIXPCInternalServiceClient activeExperimentIdsForNamespaceName:error:]
+ _OBJC_IVAR_$_TRIUrgentRollbackScheduler._experimentDatabase
+ _TRIMetricName_RetargetingByDynamicEnrollment
+ ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.252
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.321
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.328
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.333
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.343
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.330
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.335
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.345
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.332
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.264
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.271
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.461
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.464
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.473
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.474
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.462
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.465
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.389
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.391
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.392
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.398
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.406
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.416
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.408
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.475
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.477
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.478
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.479
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.476
+ ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.253
+ ___136-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:taskQueue:completion:]_block_invoke.173
+ ___136-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:taskQueue:completion:]_block_invoke.188
+ ___136-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:taskQueue:completion:]_block_invoke_2.194
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.455
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.457
+ ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.309
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.423
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.425
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.429
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.424
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.431
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.432
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.298
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.299
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.368
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.373
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.379
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.271
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.273
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.279
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.319
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.329
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.325
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.332
+ ___179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.345
+ ___19-[TRIDServer start]_block_invoke.305
+ ___19-[TRIDServer start]_block_invoke.308
+ ___19-[TRIDServer start]_block_invoke.311
+ ___19-[TRIDServer start]_block_invoke.315
+ ___19-[TRIDServer start]_block_invoke.319
+ ___26-[TRIDServer _logMetrics:]_block_invoke
+ ___34-[TRICancelableMAOperation cancel]_block_invoke.420
+ ___42-[TRIDatabase migration_addTaskCapability]_block_invoke.292
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.337
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.344
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.357
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.384
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.345
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.358
+ ___46-[TRITaskQueue _registerRetryActivityForDate:]_block_invoke.277
+ ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.196
+ ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.198
+ ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.279
+ ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.280
+ ___52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.27
+ ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.444
+ ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.322
+ ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.328
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.335
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.339
+ ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke.339
+ ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke_2.340
+ ___58-[TRIPushNotificationHandler _handleRollbackNotification:]_block_invoke
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.376
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.379
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.381
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.395
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.396
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.410
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.415
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.417
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.375
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.380
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.412
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.418
+ ___59-[TRITaskQueue activeActivityDescriptorGrantingCapability:]_block_invoke.297
+ ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.336
+ ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.337
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.368
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.377
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.387
+ ___63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.271
+ ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.293
+ ___72-[TRIXPCActivityManager _scheduleFetchTaskWithActivityDescriptor:label:]_block_invoke.300
+ ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.354
+ ___73-[TRIXPCInternalServiceClient activeExperimentIdsForNamespaceName:error:]_block_invoke
+ ___73-[TRIXPCInternalServiceClient activeExperimentIdsForNamespaceName:error:]_block_invoke_2
+ ___75-[TRIExperimentDatabase hasRecordReferencingTreatmentId:withReferenceType:]_block_invoke.200
+ ___78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.52
+ ___78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.55
+ ___78-[TRIXPCActivityManager _scheduleMaintenanceTaskWithActivityDescriptor:label:]_block_invoke.306
+ ___79-[TRIExperimentDatabase enumerateExperimentRecordsMatchingNamespaceName:block:]_block_invoke
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.451
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.455
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.456
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.459
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.464
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.467
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.457
+ ___81-[TRITaskQueue _addTask:options:guardedData:taskIdOut:accumulatedNewTaskRecords:]_block_invoke.262
+ ___81-[TRIXPCActivityManager _registerPostUpgradeActivityRequireInexpensiveNetworking]_block_invoke.329
+ ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.235
+ ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.236
+ ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.315
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.289
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.291
+ ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.317
+ ___91-[TRIUrgentRollbackScheduler _validRollbackDeploymentsForRollbackExperiment:deploymentIds:]_block_invoke
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.267
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.274
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke_2
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke_3
+ ___92-[TRINamespaceResolverStorage promoteFactorPackId:forNamespaceName:rolloutDeployment:error:]_block_invoke
+ ___92-[TRINamespaceResolverStorage promoteFactorPackId:forNamespaceName:rolloutDeployment:error:]_block_invoke_2
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.178
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.181
+ ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.192
+ ___98-[TRIInternalServiceRequestHandler activeExperimentInformationWithPrivacyFilterPolicy:completion:]_block_invoke.219
+ ___block_descriptor_48_e8_32r40r_e37_{_PASDBIterAction_=B}16?0"NSError"8lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v24?0"TRIExperimentRecord"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e8_v12?0i8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e22_v24?0"NSString"8^B16ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e28_v16?0^{TRIFlockWitness_=i}8ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.103
+ ___block_literal_global.105
+ ___block_literal_global.111
+ ___block_literal_global.113
+ ___block_literal_global.172
+ ___block_literal_global.214
+ ___block_literal_global.222
+ ___block_literal_global.241
+ ___block_literal_global.255
+ ___block_literal_global.265
+ ___block_literal_global.268
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.310
+ ___block_literal_global.317
+ ___block_literal_global.322
+ ___block_literal_global.344
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.376
+ ___block_literal_global.383
+ ___block_literal_global.394
+ ___block_literal_global.415
+ ___block_literal_global.447
+ ___block_literal_global.449
+ ___block_literal_global.452
+ ___block_literal_global.476
+ ___block_literal_global.73
+ __unnamed_array_storage.255
+ __unnamed_array_storage.278
+ __unnamed_array_storage.281
+ __unnamed_array_storage.283
+ __unnamed_array_storage.355
+ __unnamed_array_storage.372
+ __unnamed_array_storage.65
+ _objc_msgSend$_logMetrics:
+ _objc_msgSend$_shouldRetargetWithRecord:
+ _objc_msgSend$_validRollbackDeploymentsForRollbackExperiment:deploymentIds:
+ _objc_msgSend$deploymentIdArray
+ _objc_msgSend$deploymentIdArray_Count
+ _objc_msgSend$enumerateExperimentRecordsMatchingNamespaceName:block:
+ _objc_msgSend$experimentIdsWithActiveStateAndNamespaceName:completion:
+ _objc_msgSend$filename
+ _objc_msgSend$initWithExperimentDatabase:taskQueue:
+ _objc_msgSend$initWithProgressBlockForTesting:guardedData:lock:dispatchQueue:
+ _objc_msgSend$initWithStorageManagement:defaultErrorHandler:
+ _objc_msgSend$object
+ _objc_msgSend$promoteFactorPackId:forNamespaceName:rolloutDeployment:error:
+ _objc_msgSend$rejectFactorPackId:forNamespaceName:rolloutDeployment:error:
+ _objc_msgSend$scheduleUrgentRollbackForExperiment:deploymentIds:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$typeString
+ _objc_msgSend$updateExperimentHistoryDatabaseWithAllocationStatus:forExperiment:treatment:deployment:experimentRecord:isBecomingObsolete:categoricalMetric:context:
- +[TRILaunchDaemonActivityDescriptor(Initializers) bmltDescriptor]
- +[TRIXPCActivityCriteria fetchBMLTCriteria]
- -[TRIDServer _logMetrics:stopwatch:]
- -[TRIImmediateDownloadTelemetryGenerator .cxx_destruct]
- -[TRIImmediateDownloadTelemetryGenerator initWithLatencyMilliseconds:allowExpensiveNetworking:existingTelemetry:]
- -[TRIImmediateDownloadTelemetryGenerator latencyMetric]
- -[TRIImmediateDownloadTelemetryGenerator rolloutSystemTelemetry]
- -[TRINamespaceResolverStorage _logPromotionMetric:forFactorPackId:namespaceName:rolloutDeployment:withServerContext:]
- -[TRINamespaceResolverStorage promoteFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:]
- -[TRINamespaceResolverStorage rejectFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:]
- -[TRISetupAssistantFetchTelemetryGenerator .cxx_destruct]
- -[TRISetupAssistantFetchTelemetryGenerator initWithDeadlineTimestamp:referenceDate:existingTelemetry:]
- -[TRISetupAssistantFetchTelemetryGenerator latencyMetric]
- -[TRISetupAssistantFetchTelemetryGenerator rolloutSystemTelemetry]
- -[TRIUrgentRollbackScheduler initWithTaskQueue:]
- -[TRIUrgentRollbackScheduler scheduleUrgentRollbackForExperiment:]
- -[TRIXPCActivityManager _registerFetchBMLTActivity]
- -[TRIXPCActivityManager _scheduleBMLTFetchTaskWithActivityDescriptor:label:]
- GCC_except_table46
- GCC_except_table49
- _OBJC_CLASS_$_TRIImmediateDownloadTelemetryGenerator
- _OBJC_CLASS_$_TRISetupAssistantFetchTelemetryGenerator
- _OBJC_CLASS_$_TRIStopwatch
- _OBJC_CLASS_$_TRITrialDownloadSettingsFields
- _OBJC_IVAR_$_TRIImmediateDownloadTelemetryGenerator._allowExpensiveNetworking
- _OBJC_IVAR_$_TRIImmediateDownloadTelemetryGenerator._latencyMilliseconds
- _OBJC_IVAR_$_TRIImmediateDownloadTelemetryGenerator._telemetry
- _OBJC_IVAR_$_TRISetupAssistantFetchTelemetryGenerator._latencyMilliseconds
- _OBJC_IVAR_$_TRISetupAssistantFetchTelemetryGenerator._telemetry
- _OBJC_METACLASS_$_TRIImmediateDownloadTelemetryGenerator
- _OBJC_METACLASS_$_TRISetupAssistantFetchTelemetryGenerator
- _TRIMetricName_BuddyDownloadLatency
- _TRIMetricName_FactorPackPromotion
- _TRIMetricName_FactorPackRejection
- _TRIMetricName_ImmediateDownloadLatency
- _XPC_ACTIVITY_GROUP_NAME
- __OBJC_$_INSTANCE_METHODS_TRIImmediateDownloadTelemetryGenerator
- __OBJC_$_INSTANCE_METHODS_TRISetupAssistantFetchTelemetryGenerator
- __OBJC_$_INSTANCE_VARIABLES_TRIImmediateDownloadTelemetryGenerator
- __OBJC_$_INSTANCE_VARIABLES_TRISetupAssistantFetchTelemetryGenerator
- __OBJC_CLASS_RO_$_TRIImmediateDownloadTelemetryGenerator
- __OBJC_CLASS_RO_$_TRISetupAssistantFetchTelemetryGenerator
- __OBJC_METACLASS_RO_$_TRIImmediateDownloadTelemetryGenerator
- __OBJC_METACLASS_RO_$_TRISetupAssistantFetchTelemetryGenerator
- ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.228
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.297
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.304
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.309
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.319
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.306
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.311
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.321
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.308
- ___110-[TRINamespaceResolverStorage promoteFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:]_block_invoke
- ___110-[TRINamespaceResolverStorage promoteFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:]_block_invoke_2
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.240
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.247
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.437
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.440
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.449
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.450
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.438
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.441
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.365
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.367
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.368
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.374
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.382
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.392
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.384
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.451
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.453
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.454
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.455
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.452
- ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.229
- ___136-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:taskQueue:completion:]_block_invoke.170
- ___136-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:taskQueue:completion:]_block_invoke.185
- ___136-[TRIInternalServiceRequestHandler _experimentRecordsWithDeploymentEnvironments:privacyFilterPolicy:serverContext:taskQueue:completion:]_block_invoke_2.191
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.431
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.433
- ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.285
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.399
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.401
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.405
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.400
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.407
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.408
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.274
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.275
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.371
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.376
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.382
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.247
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.249
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.255
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.295
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.305
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.301
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.308
- ___179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.346
- ___19-[TRIDServer start]_block_invoke.285
- ___19-[TRIDServer start]_block_invoke.288
- ___19-[TRIDServer start]_block_invoke.291
- ___19-[TRIDServer start]_block_invoke.295
- ___19-[TRIDServer start]_block_invoke.300
- ___34-[TRICancelableMAOperation cancel]_block_invoke.395
- ___36-[TRIDServer _logMetrics:stopwatch:]_block_invoke
- ___42-[TRIDatabase migration_addTaskCapability]_block_invoke.288
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.318
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.325
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.338
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.365
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.326
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.339
- ___46-[TRITaskQueue _registerRetryActivityForDate:]_block_invoke.280
- ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.195
- ___47-[TRITaskQueue _finalizeTask:withId:runResult:]_block_invoke.197
- ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.282
- ___50-[TRITaskQueue _registerTaskQueueActivityForDate:]_block_invoke.283
- ___51-[TRIXPCActivityManager _registerFetchBMLTActivity]_block_invoke
- ___51-[TRIXPCActivityManager _registerFetchBMLTActivity]_block_invoke_2
- ___52-[TRIRetargetAllTask runUsingContext:withTaskQueue:]_block_invoke.25
- ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.419
- ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.318
- ___53-[TRIXPCActivityManager _registerPostUpgradeActivity]_block_invoke.324
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.311
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.315
- ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke.336
- ___57-[TRIXPCActivityManager _registerHotfixTargetingActivity]_block_invoke_2.337
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.348
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.352
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.355
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.357
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.371
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.386
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.391
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.393
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.351
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.356
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.388
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.394
- ___59-[TRITaskQueue activeActivityDescriptorGrantingCapability:]_block_invoke.300
- ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.331
- ___60-[TRIXPCActivityManager registerSetupAssistantFetchActivity]_block_invoke.332
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.344
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.353
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.363
- ___63-[TRITaskQueue enumerateTasksWithTagsIntersectingTagSet:block:]_block_invoke.274
- ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.269
- ___72-[TRIXPCActivityManager _scheduleFetchTaskWithActivityDescriptor:label:]_block_invoke.288
- ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.330
- ___75-[TRIExperimentDatabase hasRecordReferencingTreatmentId:withReferenceType:]_block_invoke.197
- ___76-[TRIXPCActivityManager _scheduleBMLTFetchTaskWithActivityDescriptor:label:]_block_invoke
- ___76-[TRIXPCActivityManager _scheduleBMLTFetchTaskWithActivityDescriptor:label:]_block_invoke.296
- ___78-[TRIDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.51
- ___78-[TRIXPCActivityManager _scheduleMaintenanceTaskWithActivityDescriptor:label:]_block_invoke.299
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.426
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.430
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.431
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.434
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.439
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.442
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.432
- ___81-[TRITaskQueue _addTask:options:guardedData:taskIdOut:accumulatedNewTaskRecords:]_block_invoke.265
- ___81-[TRIXPCActivityManager _registerPostUpgradeActivityRequireInexpensiveNetworking]_block_invoke.325
- ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.238
- ___83-[TRITaskQueue _startImmediateTasksIfNotAlreadyQueued:guardedData:didStartNewWork:]_block_invoke.239
- ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.291
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.265
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.267
- ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.293
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.170
- ___92-[TRITargetingTask runTaskUsingContext:withTaskQueue:systemCovariates:userCovariates:error:]_block_invoke.188
- ___98-[TRIInternalServiceRequestHandler activeExperimentInformationWithPrivacyFilterPolicy:completion:]_block_invoke.216
- ___block_descriptor_72_e8_32s40s48s56s64r_e22_v24?0"NSString"8^B16ls32l8s40l8r64l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e28_v16?0^{TRIFlockWitness_=i}8ls32l8s40l8r64l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56bs64r_e8_v12?0i8ls32l8s40l8s48l8s56l8r64l8
- ___block_literal_global.106
- ___block_literal_global.108
- ___block_literal_global.110
- ___block_literal_global.112
- ___block_literal_global.169
- ___block_literal_global.211
- ___block_literal_global.219
- ___block_literal_global.238
- ___block_literal_global.244
- ___block_literal_global.258
- ___block_literal_global.260
- ___block_literal_global.271
- ___block_literal_global.288
- ___block_literal_global.290
- ___block_literal_global.297
- ___block_literal_global.302
- ___block_literal_global.303
- ___block_literal_global.304
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.330
- ___block_literal_global.340
- ___block_literal_global.341
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.359
- ___block_literal_global.370
- ___block_literal_global.393
- ___block_literal_global.422
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.458
- ___block_literal_global.72
- __unnamed_array_storage.251
- __unnamed_array_storage.257
- __unnamed_array_storage.259
- __unnamed_array_storage.260
- __unnamed_array_storage.336
- __unnamed_array_storage.353
- __unnamed_array_storage.61
- _objc_msgSend$_logMetrics:stopwatch:
- _objc_msgSend$_logPromotionMetric:forFactorPackId:namespaceName:rolloutDeployment:withServerContext:
- _objc_msgSend$_registerFetchBMLTActivity
- _objc_msgSend$_scheduleBMLTFetchTaskWithActivityDescriptor:label:
- _objc_msgSend$bmltDescriptor
- _objc_msgSend$elapsed_ms
- _objc_msgSend$fetchBMLTCriteria
- _objc_msgSend$initWithDeadlineTimestamp:referenceDate:existingTelemetry:
- _objc_msgSend$initWithLatencyMilliseconds:allowExpensiveNetworking:existingTelemetry:
- _objc_msgSend$latencyMetric
- _objc_msgSend$pathForTargetedFactorPackSetWithDeployment:
- _objc_msgSend$promoteFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:
- _objc_msgSend$rejectFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:
- _objc_msgSend$rolloutSystemTelemetry
- _objc_msgSend$scheduleUrgentRollbackForExperiment:
- _objc_msgSend$setAllowAnyNetworking:
- _objc_msgSend$setDownloadSettingsFields:
CStrings:
+ " WHERE n.name = :namespace_name"
+ "(%d) %{public}@ %p: %s experimentIdsWithActiveStateAndNamespaceName:completion:"
+ "@48@0:8@?16@24@32@40"
+ "Asset store has no asset with identifier: %{public}@. Tried to link to %{public}@"
+ "B68@0:8C16@20@28i36@40B48@52@60"
+ "CREATE TABLE IF NOT EXISTS integrityCheck (inconsequential STRING)"
+ "Checking for asset in path %@"
+ "Could not find experiment record for experiment deployment with experiment id: %{public}@ & deployment id:  %d"
+ "Decoded valid and device-compatible BMLT catalog notification. This means we are ack’ing the CK notification, not acting on it."
+ "Decoded valid and device-compatible BMLT notification: %{public}@. This means we are ack’ing the CK notification, not acting on it."
+ "Decoded valid and device-compatible rollout notification: %{public}@.  This means we are ack’ing the CK notification, not acting on it."
+ "Encountered corrupt db (%@), attempting to reinitialize"
+ "Feb 16 2024"
+ "Parameter 'namespace-name' must be non-nil."
+ "Scheduling Hotfix for deployment %{public}@ (any network + battery allowed: %{public}d)"
+ "Scheduling Urgent Rollback for experiment: %{public}@ deployments: %{public}@"
+ "T@\"NSString\",?,R,C"
+ "TRIUrgentRollbackScheduler.m"
+ "TrialXP-399.7"
+ "_experimentIdsWithActiveStateAndNamespaceName: %{public}@"
+ "_logMetrics:"
+ "_shouldRetargetWithRecord:"
+ "_validRollbackDeploymentsForRollbackExperiment:deploymentIds:"
+ "activeExperimentIdsForNamespaceName:error:"
+ "deploymentIdArray"
+ "deploymentIdArray_Count"
+ "deploymentIds"
+ "dynamicEnrollment"
+ "enumerateExperimentRecordsMatchingNamespaceName:block:"
+ "experimentIdsWithActiveStateAndNamespaceName:completion:"
+ "failed to update experiment database"
+ "filename"
+ "ineligible "
+ "ineligible  "
+ "initWithExperimentDatabase:taskQueue:"
+ "initWithProgressBlockForTesting:guardedData:lock:dispatchQueue:"
+ "initWithStorageManagement:defaultErrorHandler:"
+ "levelValue"
+ "object"
+ "opt-out-trial-tool-rollback"
+ "promoteFactorPackId:forNamespaceName:rolloutDeployment:error:"
+ "rejectFactorPackId:forNamespaceName:rolloutDeployment:error:"
+ "retargeting_by_dynamic_enrollment"
+ "scheduleUrgentRollbackForExperiment:deploymentIds:"
+ "setWithCapacity:"
+ "typeString"
+ "updateExperimentHistoryDatabaseWithAllocationStatus:forExperiment:treatment:deployment:experimentRecord:isBecomingObsolete:categoricalMetric:context:"
+ "v32@0:8@\"NSString\"16@\"NSSet\"24"
- "@36@0:8q16B24@28"
- "Asset store has no asset with identifier: %{public}@"
- "Can't add fetch BMLT task to queue for BMLT fetch activity, descriptor is nil."
- "Dec 20 2023"
- "Decoded valid and device-compatible BMLT catalog notification"
- "Decoded valid and device-compatible BMLT notification: %{public}@"
- "Decoded valid and device-compatible rollout notification: %{public}@"
- "Failed to move local asset to global asset store: %{public}@ to %{public}@ with error:%@"
- "Not logging event %{public}@ for factorPackId %{public}@ with namespaceName %{public}@ as rolloutDeployment"
- "TRIImmediateDownloadTelemetryGenerator"
- "TRISetupAssistantFetchTelemetryGenerator"
- "TrialXP-396.4.1"
- "_allowExpensiveNetworking"
- "_latencyMilliseconds"
- "_logMetrics:stopwatch:"
- "_logPromotionMetric:forFactorPackId:namespaceName:rolloutDeployment:withServerContext:"
- "_registerFetchBMLTActivity"
- "_scheduleBMLTFetchTaskWithActivityDescriptor:label:"
- "_telemetry"
- "bmltDescriptor"
- "buddy_download_latency_ms"
- "com.apple.triald.bmlt.fetch_activity_group"
- "com.apple.triald.fetch-BMLT"
- "elapsed_ms"
- "factorpack_promotion"
- "factorpack_rejection"
- "fetch-BMLT"
- "fetchBMLTCriteria"
- "immediate_download_latency_ms"
- "initWithDeadlineTimestamp:referenceDate:existingTelemetry:"
- "initWithLatencyMilliseconds:allowExpensiveNetworking:existingTelemetry:"
- "latencyMetric"
- "promoteFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:"
- "pureBMLT"
- "rejectFactorPackId:forNamespaceName:rolloutDeployment:withServerContext:error:"
- "rolloutSystemTelemetry"
- "scheduleUrgentRollbackForExperiment:"
- "server_start"
- "setAllowAnyNetworking:"
- "setDownloadSettingsFields:"
- "task queue completed for immediateDownload in %lli ms"
- "task queue completed for setup-assistant-fetch in %lli ms"
- "triald_wake_time_ms: %llu"

```
