## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x14f67c
+466.0.0.0.0
+  __TEXT.__text: 0x14f69c
   __TEXT.__auth_stubs: 0xfe0
   __TEXT.__delay_helper: 0x478
-  __TEXT.__objc_methlist: 0xbd3c
-  __TEXT.__const: 0xe60
+  __TEXT.__objc_methlist: 0xbd54
+  __TEXT.__const: 0xe68
   __TEXT.__dlopen_cstrs: 0x101
-  __TEXT.__cstring: 0x1585e
-  __TEXT.__gcc_except_tab: 0x9aec
-  __TEXT.__oslogstring: 0x1cc54
-  __TEXT.__unwind_info: 0x42e8
+  __TEXT.__oslogstring: 0x1cd62
+  __TEXT.__gcc_except_tab: 0x9afc
+  __TEXT.__cstring: 0x15887
+  __TEXT.__unwind_info: 0x42c0
   __TEXT.__objc_classname: 0x2850
-  __TEXT.__objc_methname: 0x1e596
-  __TEXT.__objc_methtype: 0x5630
+  __TEXT.__objc_methname: 0x1e594
+  __TEXT.__objc_methtype: 0x5668
   __TEXT.__objc_stubs: 0x152a0
   __DATA_CONST.__got: 0x1358
-  __DATA_CONST.__const: 0x6a60
+  __DATA_CONST.__const: 0x6a40
   __DATA_CONST.__objc_classlist: 0x908
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60c0
+  __DATA_CONST.__objc_selrefs: 0x60c8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x5e0
-  __DATA_CONST.__objc_arraydata: 0x328
+  __DATA_CONST.__objc_arraydata: 0x330
   __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0x11a0
-  __AUTH_CONST.__cfstring: 0xd9e0
-  __AUTH_CONST.__objc_const: 0x16788
-  __AUTH_CONST.__objc_intobj: 0x990
+  __AUTH_CONST.__const: 0x11c0
+  __AUTH_CONST.__cfstring: 0xd960
+  __AUTH_CONST.__objc_const: 0x16790
+  __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1798

   __DATA.__objc_ivar: 0x8e8
   __DATA.__data: 0x2684
   __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x138
   __DATA.__common: 0x48
-  __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_ivar: 0x1b8
   __DATA_DIRTY.__objc_data: 0x42b8
-  __DATA_DIRTY.__common: 0x18
   __DATA_DIRTY.__bss: 0x380
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7E55ED73-5213-382D-83ED-7C0D456EAA85
-  Functions: 4819
-  Symbols:   17419
-  CStrings:  10618
+  UUID: C6AAB0E8-C8C3-365B-B438-EAC13F5995D1
+  Functions: 4822
+  Symbols:   17423
+  CStrings:  10616
 
Symbols:
+ -[TRIExperimentRecord(Utils) requiresTreatmentInstall]
+ -[TRIInternalServiceRequestHandler experimentHasMatchingNCV:completion:]
+ GCC_except_table103
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_TRIClientTreatment_$_TRIUtil
+ __OBJC_$_CATEGORY_NSDictionary_$_TRIFunctions
+ __OBJC_$_CATEGORY_NSMutableDictionary_$_TRIFunctions
+ __OBJC_$_CATEGORY_NSString_$_TRIFunctions
+ __OBJC_$_CATEGORY_TRIClientTreatment_$_TRIUtil
+ __OBJC_$_CATEGORY_TRIClient_$_Telemetry
+ __OBJC_$_CLASS_METHODS_NSDictionary(TRIFunctions|TRICloudKit|TRI|TRIDAG)
+ __OBJC_$_CLASS_METHODS_TRIClientRolloutArtifact(CloudKit|Utils)
+ __OBJC_$_CLASS_METHODS_TRIClientTreatment(TRIUtil|CloudKit)
+ __OBJC_$_CLASS_METHODS_TRIExperimentDatabase(SysctlNamespacesProviding|EnvVarNamespacesProviding|CountProviding)
+ __OBJC_$_CLASS_METHODS_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(TRIFunctions|TRICloudKit|TRI|TRIDAG)
+ __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(TRIFunctions|TRI)
+ __OBJC_$_INSTANCE_METHODS_NSString(TRIFunctions|TRITreatmentId)
+ __OBJC_$_INSTANCE_METHODS_TRIClient(Telemetry|Logger)
+ __OBJC_$_INSTANCE_METHODS_TRIClientRolloutArtifact(CloudKit|Utils)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentDatabase(SysctlNamespacesProviding|EnvVarNamespacesProviding|CountProviding)
+ __OBJC_$_INSTANCE_METHODS_TRIExperimentHistoryDatabase(PreviousStateProviding|PostLaunchLogging)
+ __OBJC_$_INSTANCE_METHODS_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentDatabase(SysctlNamespacesProviding|EnvVarNamespacesProviding|CountProviding)
+ __OBJC_CLASS_PROTOCOLS_$_TRIExperimentHistoryDatabase(PreviousStateProviding|PostLaunchLogging)
+ __OBJC_CLASS_PROTOCOLS_$_TRITaskAttributionInternalInsecure(FirstParty|Persistance)
+ ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.318
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.399
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.406
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.411
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.421
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.408
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.413
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.423
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.410
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.330
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.337
+ ___118+[TRIXPCNamespaceManagementRequestHandler usingServerContext:deregisterNamespaceWithName:teamId:taskQueue:completion:]_block_invoke.325
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.538
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.547
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.548
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.539
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.455
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.457
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.458
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.476
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.490
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.481
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.551
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.552
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.553
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.550
+ ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.313
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.529
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.531
+ ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.371
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.497
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.499
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.503
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.498
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.505
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.506
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.367
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.368
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.402
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.407
+ ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.414
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.337
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.339
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.345
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.418
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.428
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.424
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.431
+ ___179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.379
+ ___19-[TRIDServer start]_block_invoke.375
+ ___19-[TRIDServer start]_block_invoke.380
+ ___19-[TRIDServer start]_block_invoke.384
+ ___19-[TRIDServer start]_block_invoke.392
+ ___19-[TRIDServer start]_block_invoke_2.393
+ ___257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.362
+ ___257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.364
+ ___34+[TRISystemInfo _iCloudIdentifier]_block_invoke
+ ___34-[TRICancelableMAOperation cancel]_block_invoke.489
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.408
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.418
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.425
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.431
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.436
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.439
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.451
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.484
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.487
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.419
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.426
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.432
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.437
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.452
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.489
+ ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.513
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.397
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.401
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.462
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.485
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.487
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.501
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.506
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.508
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.503
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.509
+ ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.112
+ ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.113
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.446
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.455
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.465
+ ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.395
+ ___72-[TRIInternalServiceRequestHandler experimentHasMatchingNCV:completion:]_block_invoke
+ ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.453
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.520
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.524
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.528
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.536
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.526
+ ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.394
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.108
+ ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.111
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.358
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.360
+ ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.389
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.235
+ ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.239
+ ___block_descriptor_40_e8_32s_e30_v16?0"NSString<TRIAssetId>"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e33_v24?0"CKRecord"8"CKRecordID"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e57_v32?0"NSString<TRIAssetId>"8"TRISizedCKRecordID"16^B24ls32l8s40l8
+ ___block_descriptor_57_e8_32s40r_e52_v32?0"TRIPurgeableConstruct"8"NSDictionary"16^B24ls32l8r40l8
+ ___block_literal_global.125
+ ___block_literal_global.136
+ ___block_literal_global.153
+ ___block_literal_global.233
+ ___block_literal_global.285
+ ___block_literal_global.294
+ ___block_literal_global.319
+ ___block_literal_global.321
+ ___block_literal_global.364
+ ___block_literal_global.382
+ ___block_literal_global.385
+ ___block_literal_global.387
+ ___block_literal_global.395
+ ___block_literal_global.410
+ ___block_literal_global.421
+ ___block_literal_global.430
+ ___block_literal_global.442
+ ___block_literal_global.449
+ ___block_literal_global.454
+ ___block_literal_global.460
+ ___block_literal_global.512
+ ___block_literal_global.514
+ ___block_literal_global.556
+ ___block_literal_global.566
+ ___block_literal_global.569
+ ___block_literal_global.92
+ __iCloudIdentifier._pasOnceToken17
+ _objc_msgSend$requiresTreatmentInstall
- -[TRIAssetPurger _logPurgedAssetWithFactorNames:namespaceName:purgeabilityLevel:]
- GCC_except_table89
- GCC_except_table90
- _TRIMetricName_OnDemandAssetsPurged
- _TRIMetricName_OnDemandFactorDownloadedByRequest
- _TRIMetricName_OnDemandFactorDownloadedBySubscription
- _TRIMetricName_OnDemandFactorSubscribed
- __OBJC_$_CATEGORY_CLASS_METHODS_NSDictionary_$_TRI
- __OBJC_$_CATEGORY_CLASS_METHODS_TRIClientTreatment_$_CloudKit
- __OBJC_$_CATEGORY_NSDictionary_$_TRI
- __OBJC_$_CATEGORY_NSMutableDictionary_$_TRI
- __OBJC_$_CATEGORY_NSString_$_TRITreatmentId
- __OBJC_$_CATEGORY_TRIClientTreatment_$_CloudKit
- __OBJC_$_CATEGORY_TRIClient_$_Logger
- __OBJC_$_CLASS_METHODS_TRIClientRolloutArtifact(Utils|CloudKit)
- __OBJC_$_CLASS_METHODS_TRIExperimentDatabase(CountProviding|SysctlNamespacesProviding|EnvVarNamespacesProviding)
- __OBJC_$_CLASS_METHODS_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(TRI|TRIDAG|TRIFunctions|TRICloudKit)
- __OBJC_$_INSTANCE_METHODS_NSMutableDictionary(TRI|TRIFunctions)
- __OBJC_$_INSTANCE_METHODS_NSString(TRITreatmentId|TRIFunctions)
- __OBJC_$_INSTANCE_METHODS_TRIClient(Logger|Telemetry)
- __OBJC_$_INSTANCE_METHODS_TRIClientRolloutArtifact(Utils|CloudKit)
- __OBJC_$_INSTANCE_METHODS_TRIClientTreatment(CloudKit|TRIUtil)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentDatabase(CountProviding|SysctlNamespacesProviding|EnvVarNamespacesProviding)
- __OBJC_$_INSTANCE_METHODS_TRIExperimentHistoryDatabase(PostLaunchLogging|PreviousStateProviding)
- __OBJC_$_INSTANCE_METHODS_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
- __OBJC_CLASS_PROTOCOLS_$_TRIExperimentDatabase(CountProviding|SysctlNamespacesProviding|EnvVarNamespacesProviding)
- __OBJC_CLASS_PROTOCOLS_$_TRIExperimentHistoryDatabase(PostLaunchLogging|PreviousStateProviding)
- __OBJC_CLASS_PROTOCOLS_$_TRITaskAttributionInternalInsecure(Persistance|FirstParty)
- ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.315
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.396
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.403
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.408
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.418
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.405
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.410
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.420
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.407
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.327
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.334
- ___118+[TRIXPCNamespaceManagementRequestHandler usingServerContext:deregisterNamespaceWithName:teamId:taskQueue:completion:]_block_invoke.324
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.532
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.544
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.545
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.533
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.452
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.454
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.455
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.473
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.487
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.478
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.546
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.548
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.550
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.547
- ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.310
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.526
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.528
- ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.368
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.494
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.496
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.500
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.495
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.502
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.503
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.364
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.365
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.401
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.406
- ___163+[TRIXPCNamespaceManagementRequestHandler _removeAssetFactors:usingEntitlementWitness:serverContext:taskQueue:namespace:factorsState:removeImmediately:completion:]_block_invoke.413
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.334
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.336
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.342
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.415
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.425
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.421
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.428
- ___179+[TRIXPCNamespaceManagementRequestHandler _immediateDownloadForNamespaceNames:usingEntitlementWitness:serverContext:taskQueue:allowExpensiveNetworking:taskAttribution:completion:]_block_invoke.378
- ___19-[TRIDServer start]_block_invoke.377
- ___19-[TRIDServer start]_block_invoke.381
- ___19-[TRIDServer start]_block_invoke.385
- ___19-[TRIDServer start]_block_invoke.393
- ___19-[TRIDServer start]_block_invoke_2.394
- ___257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.361
- ___257+[TRIXPCNamespaceManagementRequestHandler _startDownloadAssetIndexesByTreatment:usingEntitlementWitness:serverContext:taskQueue:experimentIds:assetIdsByFactorPack:rolloutFactorNames:rolloutDeployments:namespace:taskAttribution:factorsState:notificationKey:]_block_invoke.363
- ___34-[TRICancelableMAOperation cancel]_block_invoke.486
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.409
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.419
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.426
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.432
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.437
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.440
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.452
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.485
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.489
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.420
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.427
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.433
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.438
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.453
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.490
- ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.510
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.394
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.398
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.459
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.482
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.484
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.498
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.503
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.505
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.500
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.506
- ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.110
- ___59-[TRIXPCStatusRequestHandler rolloutRecordsWithCompletion:]_block_invoke.111
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.443
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.452
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.462
- ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.392
- ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.450
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.517
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.521
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.522
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.530
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.523
- ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.391
- ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.106
- ___85-[TRIXPCStatusRequestHandler experimentRecordsWithDeploymentEnvironments:completion:]_block_invoke.109
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.355
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.357
- ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.386
- ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.229
- ___92-[TRIInternalServiceRequestHandler experimentIdsWithActiveStateAndNamespaceName:completion:]_block_invoke.233
- ___block_descriptor_48_e8_32s40s_e30_v16?0"NSString<TRIAssetId>"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e33_v24?0"CKRecord"8"CKRecordID"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e57_v32?0"NSString<TRIAssetId>"8"TRISizedCKRecordID"16^B24ls32l8s40l8s48l8
- ___block_descriptor_61_e8_32s40r_e52_v32?0"TRIPurgeableConstruct"8"NSDictionary"16^B24ls32l8r40l8
- ___block_literal_global.119
- ___block_literal_global.124
- ___block_literal_global.149
- ___block_literal_global.227
- ___block_literal_global.284
- ___block_literal_global.293
- ___block_literal_global.311
- ___block_literal_global.343
- ___block_literal_global.374
- ___block_literal_global.383
- ___block_literal_global.384
- ___block_literal_global.388
- ___block_literal_global.396
- ___block_literal_global.407
- ___block_literal_global.422
- ___block_literal_global.427
- ___block_literal_global.439
- ___block_literal_global.446
- ___block_literal_global.455
- ___block_literal_global.457
- ___block_literal_global.511
- ___block_literal_global.515
- ___block_literal_global.553
- ___block_literal_global.567
- ___block_literal_global.570
- _objc_msgSend$_logPurgedAssetWithFactorNames:namespaceName:purgeabilityLevel:
CStrings:
+ "-[TRIInternalServiceRequestHandler experimentHasMatchingNCV:completion:]_block_invoke"
+ "Asked to check for matching NCVs for deployment %@, but a record couldn't be found!"
+ "Jun 13 2025"
+ "NCV check couldn't be performed because requested experiment record wasn't found"
+ "Saving artifact for deployment %@"
+ "TrialXP-466"
+ "Unable to obtain sandbox extension tokens while device is Class C locked (device has not been unlocked since boot)"
+ "User Settings notification relevancy: %d. Siri locale changed: %d, Siri enablement changed: %d Dictation: %d"
+ "experiment %@ with namespace %@ has compatibility version %u which is incompatible with compability version %u found locally"
+ "experiment %@ with namespace %{public}@ has compatibility version %u which is incompatible with compatibility version %u found locally"
+ "experimentHasMatchingNCV:completion:"
+ "requiresTreatmentInstall"
+ "v32@0:8@\"TRIExperimentDeployment\"16@?<v@?B@\"NSError\">24"
- "May 24 2025"
- "TrialXP-463"
- "User Settings notification relevancy: %d. Siri locale changed: %d, Siri enablement changed: %d Dication: %d"
- "_logPurgedAssetWithFactorNames:namespaceName:purgeabilityLevel:"
- "experiment %@ with namespace %@ has compatibility version %u which is incompatible with %u"
- "experiment %@ with namespace %{public}@ has compatibility version %u which is incompatible with %u"
- "on_demand_assets_purged"
- "on_demand_factor_downloaded_by_request"
- "on_demand_factor_downloaded_by_subscription"
- "on_demand_factor_subscribed"
- "triald_task_queue_length"

```
