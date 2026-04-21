## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-1837.120.20.0.0
-  __TEXT.__text: 0x2918a8
+1837.120.23.0.0
+  __TEXT.__text: 0x291950
   __TEXT.__auth_stubs: 0x21e0
   __TEXT.__objc_methlist: 0x1298c
   __TEXT.__const: 0x187a
-  __TEXT.__cstring: 0x3ed1d
-  __TEXT.__oslogstring: 0x5e166
-  __TEXT.__gcc_except_tab: 0xec44
+  __TEXT.__cstring: 0x3ed6d
+  __TEXT.__oslogstring: 0x5e116
+  __TEXT.__gcc_except_tab: 0xeb94
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__unwind_info: 0x55b8
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_classname: 0x116e
-  __TEXT.__objc_methname: 0x47287
+  __TEXT.__objc_methname: 0x472a9
   __TEXT.__objc_methtype: 0x4824
-  __TEXT.__objc_stubs: 0x27340
-  __DATA_CONST.__got: 0x1000
+  __TEXT.__objc_stubs: 0x27380
+  __DATA_CONST.__got: 0x1008
   __DATA_CONST.__const: 0x3268
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad88
+  __DATA_CONST.__objc_selrefs: 0xad98
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xd50
   __AUTH_CONST.__auth_got: 0x1100
-  __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x32620
+  __AUTH_CONST.__const: 0xfa0
+  __AUTH_CONST.__cfstring: 0x32680
   __AUTH_CONST.__objc_const: 0x18848
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_intobj: 0x13c8

   __DATA.__objc_ivar: 0x17a4
   __DATA.__data: 0x1158
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xa80
+  __DATA.__bss: 0xa90
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B42DE8A6-6576-376A-8D8C-93F2FBF687F9
-  Functions: 7214
-  Symbols:   24148
-  CStrings:  26209
+  UUID: 359B2424-00F8-3575-A819-2A948FA82BB9
+  Functions: 7216
+  Symbols:   24157
+  CStrings:  26216
 
Symbols:
+ __MobileAssetVerifyAssetMapSignature.cold.1
+ __MobileAssetVerifyAssetMapSignature.isDevSignedCapable
+ __MobileAssetVerifyAssetMapSignature.onceToken
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1940
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1941
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1942
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1376
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1394
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1409
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1410
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1412
+ ___105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1423
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1925
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1932
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1933
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2093
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2094
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2096
+ ___118-[DownloadManager(Pallas) pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.1332
+ ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1923
+ ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1323
+ ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1324
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1346
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1350
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1366
+ ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1332
+ ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1333
+ ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2225
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1419
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1420
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1424
+ ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1939
+ ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1458
+ ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1471
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2156
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2159
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2164
+ ___22-[ControlManager init]_block_invoke.1380
+ ___27-[MABrainUpdater schedule:]_block_invoke.1251
+ ___27-[MABrainUpdater schedule:]_block_invoke.1296
+ ___27-[MABrainUpdater schedule:]_block_invoke.1301
+ ___27-[MABrainUpdater schedule:]_block_invoke_2.1297
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2205
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2212
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2214
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2216
+ ___37-[DownloadManager startDownloadTimer]_block_invoke.1829
+ ___42-[MAUnlockMonitor notifyAfterFirstUnlock:]_block_invoke.1224
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1944
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1945
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1946
+ ___44-[ControlManager handleClientConnection:on:]_block_invoke.1985
+ ___44-[ControlManager handleClientConnection:on:]_block_invoke.1986
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1324
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1370
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1841
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1851
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1862
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.1853
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2103
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2104
+ ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1351
+ ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1352
+ ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.2017
+ ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1668
+ ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1260
+ ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1263
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1439
+ ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2227
+ ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2232
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1431
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1432
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1433
+ ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1746
+ ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1747
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1380
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1402
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2085
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2090
+ ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2186
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1357
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1236
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1237
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1238
+ ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2577
+ ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2578
+ ___74-[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:]_block_invoke.1274
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1379
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1380
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1381
+ ___77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1373
+ ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1338
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1397
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1404
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1405
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3550
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3551
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1947
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1948
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1949
+ ____MobileAssetVerifyAssetMapSignature_block_invoke
+ ___block_literal_global.1225
+ ___block_literal_global.1228
+ ___block_literal_global.1232
+ ___block_literal_global.1233
+ ___block_literal_global.1240
+ ___block_literal_global.1244
+ ___block_literal_global.1251
+ ___block_literal_global.1261
+ ___block_literal_global.1273
+ ___block_literal_global.1276
+ ___block_literal_global.1281
+ ___block_literal_global.1283
+ ___block_literal_global.1286
+ ___block_literal_global.1291
+ ___block_literal_global.1299
+ ___block_literal_global.1321
+ ___block_literal_global.1323
+ ___block_literal_global.1342
+ ___block_literal_global.1352
+ ___block_literal_global.1368
+ ___block_literal_global.1378
+ ___block_literal_global.1379
+ ___block_literal_global.1396
+ ___block_literal_global.1404
+ ___block_literal_global.1408
+ ___block_literal_global.1486
+ ___block_literal_global.1536
+ ___block_literal_global.1541
+ ___block_literal_global.1552
+ ___block_literal_global.1557
+ ___block_literal_global.1579
+ ___block_literal_global.1680
+ ___block_literal_global.1716
+ ___block_literal_global.1720
+ ___block_literal_global.1770
+ ___block_literal_global.1818
+ ___block_literal_global.1870
+ ___block_literal_global.1875
+ ___block_literal_global.1878
+ ___block_literal_global.1890
+ ___block_literal_global.1914
+ ___block_literal_global.1940
+ ___block_literal_global.2185
+ ___block_literal_global.2207
+ ___block_literal_global.2234
+ ___block_literal_global.2394
+ ___block_literal_global.2402
+ ___block_literal_global.2410
+ ___block_literal_global.2418
+ ___block_literal_global.2426
+ ___block_literal_global.2434
+ ___block_literal_global.2442
+ ___block_literal_global.2450
+ ___block_literal_global.2503
+ ___block_literal_global.2612
+ ___block_literal_global.2994
+ ___block_literal_global.3007
+ ___block_literal_global.4207
+ ___block_literal_global.5517
+ ___handleCacheDeletePurgeCallbackForVolume_block_invoke.1258
+ ___handleCacheDeletePurgeableCallbackForVolume_block_invoke.1254
+ _kMobileAssetEnforceProductionSigning
+ _objc_msgSend$majorDelayPeriod
+ _objc_msgSend$minorDelayPeriod
- GCC_except_table192
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1934
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1935
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1936
- ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1370
- ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1382
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1403
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1404
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1406
- ___105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1417
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1919
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1926
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1927
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2087
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2088
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2090
- ___118-[DownloadManager(Pallas) pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.1326
- ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1917
- ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1317
- ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1318
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1340
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1344
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1360
- ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1326
- ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1327
- ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2219
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1413
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1414
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1418
- ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1933
- ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1452
- ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1465
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2150
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2153
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2158
- ___22-[ControlManager init]_block_invoke.1374
- ___27-[MABrainUpdater schedule:]_block_invoke.1245
- ___27-[MABrainUpdater schedule:]_block_invoke.1290
- ___27-[MABrainUpdater schedule:]_block_invoke.1295
- ___27-[MABrainUpdater schedule:]_block_invoke_2.1291
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2199
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2206
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2208
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2210
- ___37-[DownloadManager startDownloadTimer]_block_invoke.1823
- ___42-[MAUnlockMonitor notifyAfterFirstUnlock:]_block_invoke.1218
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1938
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1939
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1940
- ___44-[ControlManager handleClientConnection:on:]_block_invoke.1979
- ___44-[ControlManager handleClientConnection:on:]_block_invoke.1980
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1318
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1364
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1835
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1845
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1856
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.1847
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2097
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2098
- ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1345
- ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1346
- ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.2011
- ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1662
- ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1254
- ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1257
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1433
- ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2221
- ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2226
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1425
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1426
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1427
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1740
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1741
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1374
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1396
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2078
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2079
- ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2180
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1351
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1230
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1231
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1232
- ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2571
- ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2572
- ___74-[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:]_block_invoke.1268
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1373
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1374
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1375
- ___77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1367
- ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1332
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1391
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1398
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1399
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3544
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3545
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1941
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1942
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1943
- ___block_literal_global.1219
- ___block_literal_global.1222
- ___block_literal_global.1226
- ___block_literal_global.1227
- ___block_literal_global.1234
- ___block_literal_global.1238
- ___block_literal_global.1245
- ___block_literal_global.1252
- ___block_literal_global.1255
- ___block_literal_global.1259
- ___block_literal_global.1267
- ___block_literal_global.1274
- ___block_literal_global.1275
- ___block_literal_global.1285
- ___block_literal_global.1293
- ___block_literal_global.1309
- ___block_literal_global.1317
- ___block_literal_global.1336
- ___block_literal_global.1346
- ___block_literal_global.1362
- ___block_literal_global.1372
- ___block_literal_global.1373
- ___block_literal_global.1384
- ___block_literal_global.1398
- ___block_literal_global.1402
- ___block_literal_global.1480
- ___block_literal_global.1524
- ___block_literal_global.1535
- ___block_literal_global.1546
- ___block_literal_global.1551
- ___block_literal_global.1573
- ___block_literal_global.1674
- ___block_literal_global.1710
- ___block_literal_global.1714
- ___block_literal_global.1764
- ___block_literal_global.1812
- ___block_literal_global.1864
- ___block_literal_global.1869
- ___block_literal_global.1872
- ___block_literal_global.1884
- ___block_literal_global.1908
- ___block_literal_global.1934
- ___block_literal_global.2179
- ___block_literal_global.2201
- ___block_literal_global.2228
- ___block_literal_global.2388
- ___block_literal_global.2396
- ___block_literal_global.2404
- ___block_literal_global.2412
- ___block_literal_global.2420
- ___block_literal_global.2428
- ___block_literal_global.2436
- ___block_literal_global.2444
- ___block_literal_global.2497
- ___block_literal_global.2606
- ___block_literal_global.2988
- ___block_literal_global.3001
- ___block_literal_global.4201
- ___block_literal_global.5511
- ___handleCacheDeletePurgeCallbackForVolume_block_invoke.1252
- ___handleCacheDeletePurgeableCallbackForVolume_block_invoke.1248
CStrings:
+ "Device is a serverOS BMC, allowing Development signed metadata"
+ "IsComputeController"
+ "Loaded built-in MobileAssetDaemon_Framework Apr 14 2026 23:52:50"
+ "MajorDelayPeriod"
+ "MinorDelayPeriod"
+ "finalized available-for-staging | beganFromCount:%ld | duplicateCount:%ld | multipleCount:%ld | notComparableCount:%ld | availableForStaging:%ld | totalFilesystemBytes:%llu | maxFilesystemBytes:%llu"
+ "majorDelayPeriod"
+ "minorDelayPeriod"
- "Loaded built-in MobileAssetDaemon_Framework Apr  6 2026 00:47:26"
- "Timed out waiting for downlad to cancel | TaskDescriptor:%{public}@"
- "finalized available-for-staging | beganFromCount:%ld | duplicateCount:%ld | multipleCount:%ld | notComparableCount:%ld | availableForStaging:%ld | totalFilesystemBytes:%llu"
- "{removeAssetDir} Failed to cancel task within timeout | TaskDescriptor:%{public}@"

```
