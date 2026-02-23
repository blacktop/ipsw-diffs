## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-474.2.16.0.0
-  __TEXT.__text: 0x174600
+474.2.17.0.0
+  __TEXT.__text: 0x174504
   __TEXT.__auth_stubs: 0x1c20
   __TEXT.__delay_stubs: 0x80
   __TEXT.__delay_helper: 0x6ac

   __TEXT.__swift5_capture: 0x50
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_types: 0x40
-  __TEXT.__oslogstring: 0x1e83c
+  __TEXT.__oslogstring: 0x1e7f1
   __TEXT.__gcc_except_tab: 0x9508
   __TEXT.__unwind_info: 0x4890
   __TEXT.__eh_frame: 0x3d0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9AE92D98-D6B6-351D-B6BE-4259EC049D60
+  UUID: 4ABE7DD1-1321-3FE0-96FE-BDEF6ADA1F56
   Functions: 5285
   Symbols:   18268
-  CStrings:  11162
+  CStrings:  11160
 
Symbols:
+ ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.366
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.447
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.454
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.459
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.469
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.456
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.461
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.471
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.458
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.378
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.385
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.583
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.586
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.595
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.596
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.584
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.587
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.503
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.505
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.506
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.524
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.538
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.529
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.597
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.599
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.600
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.601
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.598
+ ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.361
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.577
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.579
+ ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.419
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.545
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.547
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.551
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.546
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.553
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.554
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.415
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.416
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.385
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.387
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.393
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.466
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.476
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.472
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.479
+ ___19-[TRIDServer start]_block_invoke.423
+ ___19-[TRIDServer start]_block_invoke.424
+ ___19-[TRIDServer start]_block_invoke.428
+ ___19-[TRIDServer start]_block_invoke.432
+ ___19-[TRIDServer start]_block_invoke.440
+ ___19-[TRIDServer start]_block_invoke_2.441
+ ___34-[TRICancelableMAOperation cancel]_block_invoke.537
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.457
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.467
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.474
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.480
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.494
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.509
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.542
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.545
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.546
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.468
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.475
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.481
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.495
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.510
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.547
+ ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.561
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.445
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.449
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.533
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.535
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.549
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.554
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.556
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.551
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.557
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.494
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.503
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.513
+ ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.443
+ ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.501
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.568
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.572
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.573
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.576
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.581
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.584
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.574
+ ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.442
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.406
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.408
+ ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.437
+ ___block_literal_global.394
+ ___block_literal_global.412
+ ___block_literal_global.430
+ ___block_literal_global.435
+ ___block_literal_global.443
+ ___block_literal_global.470
+ ___block_literal_global.478
+ ___block_literal_global.490
+ ___block_literal_global.508
+ ___block_literal_global.512
+ ___block_literal_global.564
+ ___block_literal_global.604
+ ___block_literal_global.624
+ ___block_literal_global.627
- ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.327
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.408
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.415
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.420
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.430
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.417
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.422
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.432
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.419
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.339
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.346
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.544
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.547
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.556
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.557
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.545
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.548
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.464
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.466
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.467
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.485
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.499
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.490
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.558
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.560
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.561
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.562
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.559
- ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.322
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.538
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.540
- ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.380
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.506
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.508
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.512
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.507
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.514
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.515
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.376
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.377
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.346
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.348
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.354
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.427
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.437
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.433
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.440
- ___19-[TRIDServer start]_block_invoke.384
- ___19-[TRIDServer start]_block_invoke.385
- ___19-[TRIDServer start]_block_invoke.389
- ___19-[TRIDServer start]_block_invoke.393
- ___19-[TRIDServer start]_block_invoke.401
- ___19-[TRIDServer start]_block_invoke_2.402
- ___34-[TRICancelableMAOperation cancel]_block_invoke.498
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.418
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.428
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.435
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.441
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.455
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.470
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.503
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.506
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.507
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.429
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.436
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.442
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.456
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.471
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.508
- ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.522
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.406
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.410
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.471
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.494
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.496
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.515
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.517
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.512
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.518
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.455
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.464
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.474
- ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.404
- ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.462
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.529
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.533
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.534
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.537
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.542
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.545
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.535
- ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.403
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.367
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.369
- ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.398
- ___block_literal_global.355
- ___block_literal_global.391
- ___block_literal_global.396
- ___block_literal_global.404
- ___block_literal_global.419
- ___block_literal_global.431
- ___block_literal_global.439
- ___block_literal_global.451
- ___block_literal_global.469
- ___block_literal_global.473
- ___block_literal_global.525
- ___block_literal_global.565
- ___block_literal_global.585
- ___block_literal_global.588
Functions:
~ +[TRIClientExperimentArtifact usableArtifactFromSource:] : 2320 -> 2412
~ -[TRIClientExperimentArtifact saveWithDatabase:paths:] : 1248 -> 1152
~ -[TRIClientExperimentArtifact hasNamespacesAvailableForExperimentWithDatabase:] : 780 -> 532
CStrings:
+ "Feb 13 2026"
+ "TrialXP-474.2.17"
+ "WKMS key fetch failed for experiment %{public}@: domain=%{public}@, code=%ld, message=%{public}@"
- "Cannot check namespace availability for experiment %@ due to decryption failure"
- "Failed to decrypt artifact for experiment %@"
- "Failed to fetch WKMS key for experiment %@: %@"
- "Jan 31 2026"
- "TrialXP-474.2.16"

```
