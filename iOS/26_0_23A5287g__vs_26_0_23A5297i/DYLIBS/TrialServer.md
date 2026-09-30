## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-468.0.0.0.0
-  __TEXT.__text: 0x14f544
-  __TEXT.__auth_stubs: 0xfc0
-  __TEXT.__delay_helper: 0x6f4
-  __TEXT.__objc_methlist: 0xbd9c
-  __TEXT.__const: 0xe58
-  __TEXT.__cstring: 0x1579b
-  __TEXT.__oslogstring: 0x1cecd
-  __TEXT.__gcc_except_tab: 0x9a50
-  __TEXT.__unwind_info: 0x4358
-  __TEXT.__objc_classname: 0x2850
-  __TEXT.__objc_methname: 0x1e63e
-  __TEXT.__objc_methtype: 0x568d
-  __TEXT.__objc_stubs: 0x15360
-  __DATA_CONST.__got: 0x1378
-  __DATA_CONST.__const: 0x6a40
-  __DATA_CONST.__objc_classlist: 0x908
+472.1.1.0.0
+  __TEXT.__text: 0x1502b4
+  __TEXT.__auth_stubs: 0xfe0
+  __TEXT.__delay_helper: 0x540
+  __TEXT.__objc_methlist: 0xbe64
+  __TEXT.__const: 0xe60
+  __TEXT.__cstring: 0x15830
+  __TEXT.__oslogstring: 0x1d021
+  __TEXT.__gcc_except_tab: 0x9a80
+  __TEXT.__unwind_info: 0x43a0
+  __TEXT.__objc_classname: 0x288b
+  __TEXT.__objc_methname: 0x1e815
+  __TEXT.__objc_methtype: 0x572d
+  __TEXT.__objc_stubs: 0x154a0
+  __DATA_CONST.__got: 0x1370
+  __DATA_CONST.__const: 0x6b30
+  __DATA_CONST.__objc_classlist: 0x918
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60f8
+  __DATA_CONST.__objc_selrefs: 0x6148
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x5e0
+  __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x338
-  __AUTH_CONST.__auth_got: 0x7f0
-  __AUTH_CONST.__const: 0x1240
-  __AUTH_CONST.__cfstring: 0xd880
-  __AUTH_CONST.__objc_const: 0x16798
-  __AUTH_CONST.__objc_intobj: 0x9c0
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__const: 0x12a0
+  __AUTH_CONST.__cfstring: 0xd8a0
+  __AUTH_CONST.__objc_const: 0x169c0
+  __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_arrayobj: 0x318
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1798
+  __AUTH.__objc_data: 0x1838
   __AUTH.__data: 0x690
-  __DATA.__objc_ivar: 0x8e8
-  __DATA.__data: 0x2688
+  __DATA.__objc_ivar: 0x904
+  __DATA.__data: 0x2680
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x120
   __DATA.__common: 0x48

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CacheDelete.framework/CacheDelete
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
-  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
-  - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 8E58B461-13F6-3720-8FF9-A90DBE51707B
-  Functions: 4825
-  Symbols:   17444
-  CStrings:  10608
+  UUID: 7A01FE69-518D-37EE-A537-7CD48A70C6D5
+  Functions: 4850
+  Symbols:   17528
+  CStrings:  10641
 
Symbols:
+ +[TRISystemInfo _appleIntelligenceState:]
+ +[TRISystemInfo _mapsBucketId:]
+ -[TRIDebounceSubscriptionsGuardedData .cxx_destruct]
+ -[TRIPushServiceConnectionMultiplexer _debounceTime]
+ -[TRIPushServiceConnectionMultiplexer _debouncedSubscribeToChannel:]
+ -[TRIPushServiceConnectionMultiplexer _setupDebounceTimerIfNeededWithGuardedData:]
+ -[TRIPushServiceConnectionMultiplexer performQueuedSubscriptions]
+ -[TRIXPCCovariateFetcher .cxx_destruct]
+ -[TRIXPCCovariateFetcher appleIntelligenceStateWithUseCaseIdentifiers:]
+ -[TRIXPCCovariateFetcher appleIntelligenceState]
+ -[TRIXPCCovariateFetcher geoservicesBucketID]
+ -[TRIXPCCovariateFetcher init]
+ -[TRIXPCCovariateFetcher invalidateConnection]
+ -[TRIXPCCovariateFetcher mapsDeviceCountryCode]
+ -[TRIXPCCovariateFetcher sendMessageToRemoteObject:]
+ -[TRIXPCCovariateFetcher setupArchivingServiceXPCConnection]
+ OBJC_IVAR_$_TRIDebounceSubscriptionsGuardedData.debounceTimer
+ OBJC_IVAR_$_TRIDebounceSubscriptionsGuardedData.queuedSubscriptions
+ _OBJC_CLASS_$_TRIDebounceSubscriptionsGuardedData
+ _OBJC_CLASS_$_TRIXPCCovariateFetcher
+ _OBJC_IVAR_$_TRIPushServiceConnectionMultiplexer._lock
+ _OBJC_IVAR_$_TRIPushServiceConnectionMultiplexer._subscriptionQueue
+ _OBJC_IVAR_$_TRIXPCCovariateFetcher.connectionLock
+ _OBJC_IVAR_$_TRIXPCCovariateFetcher.inFlightConnectionQueue
+ _OBJC_IVAR_$_TRIXPCCovariateFetcher.xpcConnection
+ _OBJC_METACLASS_$_TRIDebounceSubscriptionsGuardedData
+ _OBJC_METACLASS_$_TRIXPCCovariateFetcher
+ __OBJC_$_INSTANCE_METHODS_TRIDebounceSubscriptionsGuardedData
+ __OBJC_$_INSTANCE_METHODS_TRIXPCCovariateFetcher
+ __OBJC_$_INSTANCE_VARIABLES_TRIDebounceSubscriptionsGuardedData
+ __OBJC_$_INSTANCE_VARIABLES_TRIXPCCovariateFetcher
+ __OBJC_CLASS_RO_$_TRIDebounceSubscriptionsGuardedData
+ __OBJC_CLASS_RO_$_TRIXPCCovariateFetcher
+ __OBJC_METACLASS_RO_$_TRIDebounceSubscriptionsGuardedData
+ __OBJC_METACLASS_RO_$_TRIXPCCovariateFetcher
+ ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.315
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.396
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.403
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.408
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.418
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.405
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.410
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.420
+ ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.407
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.327
+ ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.334
+ ___115-[TRIRemoteAssetExtractor extractArchiveFromFile:withArchiveName:toEmptyDirectory:postExtractionCompression:error:]_block_invoke.29
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.532
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.544
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.545
+ ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.533
+ ___122-[TRIPushServiceConnectionMultiplexer ensureSubscriptionsExistOnlyForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke.67
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.452
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.454
+ ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.455
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.473
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.487
+ ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.478
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.546
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.548
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.550
+ ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.547
+ ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.310
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.526
+ ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.528
+ ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.368
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.494
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.496
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.500
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.495
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.502
+ ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.503
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.364
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.365
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.334
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.336
+ ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.342
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.415
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.425
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.421
+ ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.428
+ ___19-[TRIDServer start]_block_invoke.372
+ ___19-[TRIDServer start]_block_invoke.373
+ ___19-[TRIDServer start]_block_invoke.377
+ ___19-[TRIDServer start]_block_invoke.381
+ ___19-[TRIDServer start]_block_invoke.389
+ ___19-[TRIDServer start]_block_invoke_2.390
+ ___34-[TRICancelableMAOperation cancel]_block_invoke.486
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.406
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.416
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.423
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.429
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.434
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.447
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.480
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.483
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.417
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.424
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.430
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.435
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.448
+ ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.485
+ ___45-[TRIXPCCovariateFetcher geoservicesBucketID]_block_invoke
+ ___45-[TRIXPCCovariateFetcher geoservicesBucketID]_block_invoke_2
+ ___47-[TRIXPCCovariateFetcher mapsDeviceCountryCode]_block_invoke
+ ___47-[TRIXPCCovariateFetcher mapsDeviceCountryCode]_block_invoke_2
+ ___48-[TRIXPCCovariateFetcher appleIntelligenceState]_block_invoke
+ ___48-[TRIXPCCovariateFetcher appleIntelligenceState]_block_invoke_2
+ ___52-[TRIXPCCovariateFetcher sendMessageToRemoteObject:]_block_invoke
+ ___52-[TRIXPCCovariateFetcher sendMessageToRemoteObject:]_block_invoke.37
+ ___52-[TRIXPCCovariateFetcher sendMessageToRemoteObject:]_block_invoke_2
+ ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.510
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.394
+ ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.398
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.459
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.482
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.484
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.498
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.503
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.505
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.500
+ ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.506
+ ___60-[TRIXPCCovariateFetcher setupArchivingServiceXPCConnection]_block_invoke
+ ___60-[TRIXPCCovariateFetcher setupArchivingServiceXPCConnection]_block_invoke.28
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.443
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.452
+ ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.462
+ ___65-[TRIPushServiceConnectionMultiplexer performQueuedSubscriptions]_block_invoke
+ ___66-[TRIPushServiceConnectionMultiplexer unsubscribeForExperimentId:]_block_invoke
+ ___68-[TRIPushServiceConnectionMultiplexer _debouncedSubscribeToChannel:]_block_invoke
+ ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.392
+ ___71-[TRIXPCCovariateFetcher appleIntelligenceStateWithUseCaseIdentifiers:]_block_invoke
+ ___71-[TRIXPCCovariateFetcher appleIntelligenceStateWithUseCaseIdentifiers:]_block_invoke_2
+ ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.450
+ ___78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.39
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.517
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.521
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.522
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.530
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.523
+ ___82-[TRIPushServiceConnectionMultiplexer _setupDebounceTimerIfNeededWithGuardedData:]_block_invoke
+ ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.391
+ ___87+[TRIRemoteAssetDecrypter decryptAssetWithURL:destinationFilename:namespaceName:error:]_block_invoke.34
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.355
+ ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.357
+ ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.386
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32r_e50_v24?0"<TrialArchivingServiceProtocol>"8?<v?>16lr32l8
+ ___block_descriptor_40_e8_32s_e45_v16?0"TRIDebounceSubscriptionsGuardedData"8ls32l8
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40r_e18_v16?0"NSNumber"8lr40l8s32l8
+ ___block_descriptor_48_e8_32bs40r_e18_v16?0"NSString"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e50_v24?0"<TrialArchivingServiceProtocol>"8?<v?>16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e45_v16?0"TRIDebounceSubscriptionsGuardedData"8ls32l8s40l8
+ ___block_literal_global.111
+ ___block_literal_global.114
+ ___block_literal_global.116
+ ___block_literal_global.30
+ ___block_literal_global.343
+ ___block_literal_global.36
+ ___block_literal_global.379
+ ___block_literal_global.392
+ ___block_literal_global.407
+ ___block_literal_global.419
+ ___block_literal_global.427
+ ___block_literal_global.439
+ ___block_literal_global.44
+ ___block_literal_global.446
+ ___block_literal_global.450
+ ___block_literal_global.457
+ ___block_literal_global.553
+ ___block_literal_global.562
+ ___block_literal_global.565
+ ___block_literal_global.84
+ ___block_literal_global.97
+ __iCloudIdentifier._pasOnceToken13
+ _kTRISubscriptionSkipDebounceOverrideUserDefaultsKey
+ _objc_msgSend$_appleIntelligenceState:
+ _objc_msgSend$_debounceTime
+ _objc_msgSend$_debouncedSubscribeToChannel:
+ _objc_msgSend$_mapsBucketId:
+ _objc_msgSend$_setupDebounceTimerIfNeededWithGuardedData:
+ _objc_msgSend$appleIntelligenceState:
+ _objc_msgSend$appleIntelligenceStateWithUseCaseIDs:handler:
+ _objc_msgSend$appleIntelligenceStateWithUseCaseIdentifiers:
+ _objc_msgSend$autoreleasingSerialQueueWithLabel:
+ _objc_msgSend$geoservicesBucketID
+ _objc_msgSend$geoservicesBucketID:
+ _objc_msgSend$invalidateConnection
+ _objc_msgSend$mapsDeviceCountryCode:
+ _objc_msgSend$performQueuedSubscriptions
+ _objc_msgSend$sendMessageToRemoteObject:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$setupArchivingServiceXPCConnection
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- +[TRISystemInfo _appleIntelligenceState]
- +[TRISystemInfo _mapsBucketId]
- -[TRIPushServiceConnection _subscribeToChannel:]
- -[TRIPushServiceConnection subscribeToChannel:]
- -[TRISandboxedPushServiceConnection subscribeToChannel:]
- _OBJC_CLASS_$_GEOCountryConfiguration
- _OBJC_CLASS_$_GEOExperimentConfiguration
- _OBJC_CLASS_$_GMAvailabilityWrapper
- ___104+[TRIClientFactorPackUtils _enumerateAssetFactorLevelsInFlatBufferStorage:trialAssetBlock:maAssetBlock:]_block_invoke.318
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.399
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.406
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.411
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke.421
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.408
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.413
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_2.423
- ___109-[TRIFBFactorPackStorage _writeFactorPack:futurePath:forFactorNames:aliasToUnaliasMap:assetStore:tempDirRef:]_block_invoke_3.410
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.330
- ___111-[TRIFetchTreatmentTask _saveTreatment:experimentRecord:assetURLs:assetMetadata:context:paths:downloadOptions:]_block_invoke.337
- ___115-[TRIRemoteAssetExtractor extractArchiveFromFile:withArchiveName:toEmptyDirectory:postExtractionCompression:error:]_block_invoke.20
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.538
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.547
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke.548
- ___118-[TRIFetchOnDemandFactorsTask _fetchDiffsFromAssetDiffRecordsWithContext:plan:aggregateProgress:downloadSize:options:]_block_invoke_2.539
- ___122-[TRIPushServiceConnectionMultiplexer ensureSubscriptionsExistOnlyForRolloutDeployments:experimentIds:maxChannelsAllowed:]_block_invoke.49
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke.455
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_2.457
- ___126-[TRISQLiteMADatabase lockContentSync:forAssetSelector:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:]_block_invoke_3.458
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.476
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke.490
- ___127-[TRIFetchOnDemandFactorsTask _planForFetchingAssetsFromTreatmentRecordsWithContext:downloadOptions:updatingAggregateProgress:]_block_invoke_2.481
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.551
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.552
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke.553
- ___128-[TRIFetchOnDemandFactorsTask _asyncFetchCKAssetsFromAssetRecordsWithContext:plan:aggregateProgress:downloadSize:options:group:]_block_invoke_2.550
- ___131-[TRIClientTreatment(TRIUtil) _triRequiredMAAssetsForInstallationWithAssetStore:subscriptionSettings:maProvider:aliasToUnaliasMap:]_block_invoke.313
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke.529
- ___138-[TRIFetchOnDemandFactorsTask _asyncFetchAssetsFromTreatmentRecordsWithContext:plan:aggregateProgress:downloadSize:downloadOptions:group:]_block_invoke_2.531
- ___151-[TRIFetchTreatmentTask _fetchAssetsWithArtifactProvider:recordId:experimentRecord:assetIndexes:downloadOptions:context:assetURLs:treatmentFetchError:]_block_invoke.371
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.497
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.499
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke.503
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.498
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_2.505
- ___154-[TRIFetchOnDemandFactorsTask _planForFetchingAssetDiffsWithContext:downloadOptions:updatingAggregateProgress:nonDiffableAssetIds:unlinkedMAAssetsOnDisk:]_block_invoke_3.506
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.367
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.368
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.337
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.339
- ___164+[TRIClientFactorPackUtils enumerateMetadataForAssetsInFactorPack:flatbufferFactorLevels:assetStore:maProvider:aliasToUnaliasMap:subscribedFactors:ckBlock:maBlock:]_block_invoke.345
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.418
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke.428
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.424
- ___165-[TRIFetchFactorPackSetTask _downloadAndSaveCKAssetsWithMetadata:artifactProvider:options:downloadNotificationKey:context:assetsDownloadSize:errorResult:fetchError:]_block_invoke_2.431
- ___19-[TRIDServer start]_block_invoke.375
- ___19-[TRIDServer start]_block_invoke.376
- ___19-[TRIDServer start]_block_invoke.380
- ___19-[TRIDServer start]_block_invoke.384
- ___19-[TRIDServer start]_block_invoke.392
- ___19-[TRIDServer start]_block_invoke_2.393
- ___30+[TRISystemInfo _mapsBucketId]_block_invoke
- ___34-[TRICancelableMAOperation cancel]_block_invoke.489
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.408
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.418
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.425
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.431
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.436
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.439
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.451
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.487
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke.488
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.419
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.426
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.432
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.437
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.452
- ___44-[TRIDServer _registerXpcStreamEventHandler]_block_invoke_2.489
- ___47-[TRIPushServiceConnection subscribeToChannel:]_block_invoke
- ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.513
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.397
- ___55-[TRIFetchTreatmentTask runUsingContext:withTaskQueue:]_block_invoke.401
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.462
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.485
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.487
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.501
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.506
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke.508
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.503
- ___59-[TRIFetchFactorPackSetTask runUsingContext:withTaskQueue:]_block_invoke_2.509
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.446
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.455
- ___61-[TRIFetchOnDemandFactorsTask runUsingContext:withTaskQueue:]_block_invoke.465
- ___69-[TRIFetchFactorPackSetTask _requiredAssetsForFactorPackSet:context:]_block_invoke.395
- ___73-[TRIFetchFactorPackSetTask _saveFactorPackSet:requiredAssetMap:context:]_block_invoke.453
- ___78-[NSFileManager(TRIServer) triRemoveCachedANEBinariesForModelsFromPath:error:]_block_invoke.30
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.520
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.524
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.528
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.536
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.526
- ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.394
- ___87+[TRIRemoteAssetDecrypter decryptAssetWithURL:destinationFilename:namespaceName:error:]_block_invoke.25
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.358
- ___88-[TRIAssetStoreOperator referenceMAAutoAssetWithId:futurePath:currentPath:isFileFactor:]_block_invoke.360
- ___89-[TRIAssetStore _linkDirectoryAssetWithIdentifier:toCurrentPath:futurePath:flockWitness:]_block_invoke.389
- ___block_descriptor_48_e8_32s40r_e30_v24?0"NSNumber"8"NSError"16lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.103
- ___block_literal_global.113
- ___block_literal_global.120
- ___block_literal_global.122
- ___block_literal_global.364
- ___block_literal_global.382
- ___block_literal_global.387
- ___block_literal_global.395
- ___block_literal_global.410
- ___block_literal_global.421
- ___block_literal_global.430
- ___block_literal_global.442
- ___block_literal_global.449
- ___block_literal_global.454
- ___block_literal_global.460
- ___block_literal_global.556
- ___block_literal_global.566
- ___block_literal_global.569
- ___block_literal_global.90
- __iCloudIdentifier._pasOnceToken17
- _dlopenHelper$GenerativeModels
- _dlopenHelper$GeoServices
- _dlopenHelperFlag$GenerativeModels
- _dlopenHelperFlag$GeoServices
- _gotLoadHelper_x8$_OBJC_CLASS_$_GEOCountryConfiguration
- _gotLoadHelper_x8$_OBJC_CLASS_$_GEOExperimentConfiguration
- _gotLoadHelper_x8$_OBJC_CLASS_$_GMAvailabilityWrapper
- _objc_msgSend$_appleIntelligenceState
- _objc_msgSend$_mapsBucketId
- _objc_msgSend$_subscribeToChannel:
- _objc_msgSend$currentWithUseCaseIdentifiers:
- _objc_msgSend$fetchBucketID:
- _objc_msgSend$sharedConfiguration
- _objc_msgSend$subscribeToChannel:
- _objc_msgSend$subscribeToChannel:forTopic:
CStrings:
+ "@\"NSXPCConnection\""
+ "Covariate fetch connection to TrialArchivingService was interrupted."
+ "Covariate fetch connection to TrialArchivingService was invalidated."
+ "Debouncing will be skipped because the defaults were set"
+ "Jul 14 2025"
+ "Received request to subscribe %@. Queueing for later subscription"
+ "Setting up debounce timer for push channel subscriptions"
+ "Subscribing %lu queued channels"
+ "TRIDebounceSubscriptionsGuardedData"
+ "TRIXPCCovariateFetcher"
+ "TRIXPCCovariateFetcher did not receive a proxy for the remote object."
+ "TRIXPCCovariateFetcher failed to connect to remote object proxy with error: %@"
+ "TRIXPCCovariateFetcher was unable to establish a connection to TrialArchivingService."
+ "TrialXP-472.1.1"
+ "Unable to fetch Maps Bucket Id."
+ "_appleIntelligenceState:"
+ "_debounceTime"
+ "_debouncedSubscribeToChannel:"
+ "_mapsBucketId:"
+ "_setupDebounceTimerIfNeededWithGuardedData:"
+ "_subscriptionQueue"
+ "appleIntelligenceState:"
+ "appleIntelligenceStateWithUseCaseIDs:handler:"
+ "appleIntelligenceStateWithUseCaseIdentifiers:"
+ "autoreleasingSerialQueueWithLabel:"
+ "com.apple.Trial.covariateFetchOperationQueue"
+ "com.apple.trial.push-service-muxer-subscriptions"
+ "com.apple.trial.system.PublishSysctlOnTrialdLaunchComplete"
+ "com.apple.triald.override.subscription-skip-debounce"
+ "connectionLock"
+ "debounceTimer"
+ "geoservicesBucketID"
+ "geoservicesBucketID:"
+ "inFlightConnectionQueue"
+ "invalidateConnection"
+ "mapsDeviceCountryCode:"
+ "performQueuedSubscriptions"
+ "queuedSubscriptions"
+ "sendMessageToRemoteObject:"
+ "setInterruptionHandler:"
+ "setInvalidationHandler:"
+ "setupArchivingServiceXPCConnection"
+ "v16@?0@\"NSNumber\"8"
+ "v16@?0@\"TRIDebounceSubscriptionsGuardedData\"8"
+ "v24@0:8@?<v@?@\"NSNumber\">16"
+ "v24@0:8@?<v@?@\"NSString\">16"
+ "v24@?0@\"<TrialArchivingServiceProtocol>\"8@?<v@?>16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSNumber\">24"
+ "xpcConnection"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "/System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels"
- "/System/Library/PrivateFrameworks/GeoServices.framework/GeoServices"
- "Could not subscribe to channel %@"
- "Jun 28 2025"
- "New subscription denied since we reached the channel limit (%tu >= %tu)"
- "Subscribing to channel %@"
- "TrialXP-468"
- "Unable to fetch Maps Bucket Id: %{public}@"
- "[Sandbox] Subscribing to channel %@"
- "_subscribeToChannel:"
- "currentWithUseCaseIdentifiers:"
- "failed to process %@ - server context is null"
- "fetchBucketID:"
- "maps: bucket id: %@"
- "sharedConfiguration"
- "subscribeToChannel:"
- "subscribeToChannel:forTopic:"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"

```
