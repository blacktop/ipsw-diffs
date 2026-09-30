## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-1837.120.23.0.0
-  __TEXT.__text: 0x291950
-  __TEXT.__auth_stubs: 0x21e0
+1837.122.1.0.0
+  __TEXT.__text: 0x2919d0
+  __TEXT.__auth_stubs: 0x21f0
   __TEXT.__objc_methlist: 0x1298c
   __TEXT.__const: 0x187a
-  __TEXT.__cstring: 0x3ed6d
+  __TEXT.__cstring: 0x3ed9d
   __TEXT.__oslogstring: 0x5e116
   __TEXT.__gcc_except_tab: 0xeb94
   __TEXT.__dlopen_cstrs: 0x5a

   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xd50
-  __AUTH_CONST.__auth_got: 0x1100
+  __AUTH_CONST.__auth_got: 0x1108
   __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x32680
+  __AUTH_CONST.__cfstring: 0x326c0
   __AUTH_CONST.__objc_const: 0x18848
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_intobj: 0x13c8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 359B2424-00F8-3575-A819-2A948FA82BB9
+  UUID: 96A59D0D-9542-3444-8FF1-4E2F72BD94F3
   Functions: 7216
-  Symbols:   24157
-  CStrings:  26216
+  Symbols:   24158
+  CStrings:  26220
 
Symbols:
+ _MGGetSInt64Answer
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1943
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1944
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1945
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1379
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1391
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1397
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1413
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1415
+ ___105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1426
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1928
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1935
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1936
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2097
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2099
+ ___118-[DownloadManager(Pallas) pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.1335
+ ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1926
+ ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1326
+ ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1327
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1349
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1353
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1369
+ ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1335
+ ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1336
+ ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2228
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1422
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1423
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1427
+ ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1942
+ ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1461
+ ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1474
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2162
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2167
+ ___22-[ControlManager init]_block_invoke.1383
+ ___27-[MABrainUpdater schedule:]_block_invoke.1254
+ ___27-[MABrainUpdater schedule:]_block_invoke.1299
+ ___27-[MABrainUpdater schedule:]_block_invoke.1304
+ ___27-[MABrainUpdater schedule:]_block_invoke_2.1300
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2208
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2215
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2217
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2219
+ ___37-[DownloadManager startDownloadTimer]_block_invoke.1832
+ ___42-[MAUnlockMonitor notifyAfterFirstUnlock:]_block_invoke.1227
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1947
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1948
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1949
+ ___44-[ControlManager handleClientConnection:on:]_block_invoke.1988
+ ___44-[ControlManager handleClientConnection:on:]_block_invoke.1989
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1327
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1373
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1844
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1854
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1865
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.1856
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2106
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2107
+ ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1354
+ ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1355
+ ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.2020
+ ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1671
+ ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1266
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1442
+ ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2230
+ ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2235
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1434
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1435
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1436
+ ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1749
+ ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1750
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1383
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1405
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2087
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2088
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2093
+ ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2189
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1360
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1239
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1240
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1241
+ ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2580
+ ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2581
+ ___74-[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:]_block_invoke.1277
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1382
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1383
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1384
+ ___77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1376
+ ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1341
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1400
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1407
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1408
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3553
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3554
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1950
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1951
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1952
+ ___block_literal_global.1231
+ ___block_literal_global.1235
+ ___block_literal_global.1236
+ ___block_literal_global.1243
+ ___block_literal_global.1247
+ ___block_literal_global.1254
+ ___block_literal_global.1267
+ ___block_literal_global.1268
+ ___block_literal_global.1274
+ ___block_literal_global.1279
+ ___block_literal_global.1284
+ ___block_literal_global.1289
+ ___block_literal_global.1294
+ ___block_literal_global.1302
+ ___block_literal_global.1318
+ ___block_literal_global.1324
+ ___block_literal_global.1326
+ ___block_literal_global.1345
+ ___block_literal_global.1355
+ ___block_literal_global.1371
+ ___block_literal_global.1381
+ ___block_literal_global.1382
+ ___block_literal_global.1393
+ ___block_literal_global.1399
+ ___block_literal_global.1407
+ ___block_literal_global.1411
+ ___block_literal_global.1489
+ ___block_literal_global.1533
+ ___block_literal_global.1539
+ ___block_literal_global.1544
+ ___block_literal_global.1555
+ ___block_literal_global.1560
+ ___block_literal_global.1582
+ ___block_literal_global.1686
+ ___block_literal_global.1722
+ ___block_literal_global.1723
+ ___block_literal_global.1773
+ ___block_literal_global.1821
+ ___block_literal_global.1873
+ ___block_literal_global.1881
+ ___block_literal_global.1893
+ ___block_literal_global.1917
+ ___block_literal_global.1943
+ ___block_literal_global.2188
+ ___block_literal_global.2210
+ ___block_literal_global.2237
+ ___block_literal_global.2397
+ ___block_literal_global.2405
+ ___block_literal_global.2413
+ ___block_literal_global.2421
+ ___block_literal_global.2429
+ ___block_literal_global.2437
+ ___block_literal_global.2445
+ ___block_literal_global.2453
+ ___block_literal_global.2506
+ ___block_literal_global.2615
+ ___block_literal_global.2997
+ ___block_literal_global.3010
+ ___block_literal_global.4210
+ ___block_literal_global.5520
+ ___handleCacheDeletePurgeCallbackForVolume_block_invoke.1261
+ ___handleCacheDeletePurgeableCallbackForVolume_block_invoke.1257
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1940
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1941
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1942
- ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1376
- ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1388
- ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1394
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1409
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1410
- ___105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1423
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1925
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1932
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1933
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2093
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2094
- ___118-[DownloadManager(Pallas) pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.1332
- ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1923
- ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1323
- ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1324
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1346
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1350
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1366
- ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1332
- ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1333
- ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2225
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1419
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1420
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1424
- ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1939
- ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1458
- ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1471
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2156
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2164
- ___22-[ControlManager init]_block_invoke.1380
- ___27-[MABrainUpdater schedule:]_block_invoke.1251
- ___27-[MABrainUpdater schedule:]_block_invoke.1296
- ___27-[MABrainUpdater schedule:]_block_invoke.1301
- ___27-[MABrainUpdater schedule:]_block_invoke_2.1297
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2205
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2212
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2214
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2216
- ___37-[DownloadManager startDownloadTimer]_block_invoke.1829
- ___42-[MAUnlockMonitor notifyAfterFirstUnlock:]_block_invoke.1224
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1944
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1945
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1946
- ___44-[ControlManager handleClientConnection:on:]_block_invoke.1985
- ___44-[ControlManager handleClientConnection:on:]_block_invoke.1986
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1324
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1370
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1841
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1851
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1862
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.1853
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2103
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2104
- ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1351
- ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1352
- ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.2017
- ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1668
- ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1260
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1439
- ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2227
- ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2232
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1431
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1432
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1433
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1746
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1747
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1380
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1402
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2084
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2085
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2090
- ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2186
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1357
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1236
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1237
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1238
- ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2577
- ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2578
- ___74-[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:]_block_invoke.1274
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1379
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1380
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1381
- ___77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1373
- ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1338
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1397
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1404
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1405
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3550
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3551
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1947
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1948
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1949
- ___block_literal_global.1225
- ___block_literal_global.1232
- ___block_literal_global.1233
- ___block_literal_global.1240
- ___block_literal_global.1244
- ___block_literal_global.1251
- ___block_literal_global.1258
- ___block_literal_global.1265
- ___block_literal_global.1270
- ___block_literal_global.1271
- ___block_literal_global.1277
- ___block_literal_global.1281
- ___block_literal_global.1291
- ___block_literal_global.1299
- ___block_literal_global.1315
- ___block_literal_global.1321
- ___block_literal_global.1323
- ___block_literal_global.1342
- ___block_literal_global.1352
- ___block_literal_global.1368
- ___block_literal_global.1378
- ___block_literal_global.1379
- ___block_literal_global.1390
- ___block_literal_global.1396
- ___block_literal_global.1404
- ___block_literal_global.1408
- ___block_literal_global.1486
- ___block_literal_global.1530
- ___block_literal_global.1536
- ___block_literal_global.1541
- ___block_literal_global.1552
- ___block_literal_global.1557
- ___block_literal_global.1579
- ___block_literal_global.1680
- ___block_literal_global.1716
- ___block_literal_global.1720
- ___block_literal_global.1770
- ___block_literal_global.1818
- ___block_literal_global.1870
- ___block_literal_global.1875
- ___block_literal_global.1890
- ___block_literal_global.1914
- ___block_literal_global.1940
- ___block_literal_global.2185
- ___block_literal_global.2207
- ___block_literal_global.2234
- ___block_literal_global.2394
- ___block_literal_global.2402
- ___block_literal_global.2410
- ___block_literal_global.2418
- ___block_literal_global.2426
- ___block_literal_global.2434
- ___block_literal_global.2442
- ___block_literal_global.2450
- ___block_literal_global.2503
- ___block_literal_global.2612
- ___block_literal_global.2994
- ___block_literal_global.3007
- ___block_literal_global.4207
- ___block_literal_global.5517
- ___handleCacheDeletePurgeCallbackForVolume_block_invoke.1258
- ___handleCacheDeletePurgeableCallbackForVolume_block_invoke.1254
Functions:
~ ____pallasStringParams_block_invoke : 756 -> 840
~ _OUTLINED_FUNCTION_11 : 28 -> 24
~ _ccaes_arm_decrypt_key : 112 -> 160
CStrings:
+ "DeviceMemorySize"
+ "DeviceMemorySizeGB"
+ "Loaded built-in MobileAssetDaemon_Framework Apr 22 2026 22:59:57"
- "Loaded built-in MobileAssetDaemon_Framework Apr 14 2026 23:52:50"

```
