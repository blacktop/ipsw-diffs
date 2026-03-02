## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-1837.100.250.0.0
-  __TEXT.__text: 0x28c874
-  __TEXT.__auth_stubs: 0x21d0
-  __TEXT.__objc_methlist: 0x128bc
+1837.100.266.0.0
+  __TEXT.__text: 0x291868
+  __TEXT.__auth_stubs: 0x21e0
+  __TEXT.__objc_methlist: 0x1298c
   __TEXT.__const: 0x187a
-  __TEXT.__cstring: 0x3e9dd
-  __TEXT.__oslogstring: 0x5c476
-  __TEXT.__gcc_except_tab: 0xe8cc
+  __TEXT.__cstring: 0x3ed1d
+  __TEXT.__oslogstring: 0x5e166
+  __TEXT.__gcc_except_tab: 0xec44
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x5580
+  __TEXT.__unwind_info: 0x55c0
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_classname: 0x116e
-  __TEXT.__objc_methname: 0x46e26
-  __TEXT.__objc_methtype: 0x4814
-  __TEXT.__objc_stubs: 0x270c0
-  __DATA_CONST.__got: 0xff8
-  __DATA_CONST.__const: 0x3230
+  __TEXT.__objc_methname: 0x47287
+  __TEXT.__objc_methtype: 0x4824
+  __TEXT.__objc_stubs: 0x27340
+  __DATA_CONST.__got: 0x1000
+  __DATA_CONST.__const: 0x3268
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xace8
+  __DATA_CONST.__objc_selrefs: 0xad88
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xd50
-  __AUTH_CONST.__auth_got: 0x10f8
-  __AUTH_CONST.__const: 0xec0
-  __AUTH_CONST.__cfstring: 0x31e80
-  __AUTH_CONST.__objc_const: 0x187a8
+  __AUTH_CONST.__auth_got: 0x1100
+  __AUTH_CONST.__const: 0xf80
+  __AUTH_CONST.__cfstring: 0x32620
+  __AUTH_CONST.__objc_const: 0x18848
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__objc_intobj: 0x13b0
+  __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x2c98
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x1798
+  __DATA.__objc_ivar: 0x17a4
   __DATA.__data: 0x1158
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xa80

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: F6339121-12A7-31FE-9542-A13DAACC2EF0
-  Functions: 7187
-  Symbols:   24064
-  CStrings:  25986
+  UUID: 909E2F89-2799-362D-8E65-789B8F26567B
+  Functions: 7214
+  Symbols:   24148
+  CStrings:  26209
 
Symbols:
+ +[MADownloadServiceClient copyBrainLoadErrorDomainSummaryStringForError:]
+ +[MADownloadServiceClient copyParsedErrorReasonFromBrainLoadError:unmetRequirements:]
+ +[MADownloadServiceClient copySummaryStringForCryptexLoadError:]
+ +[MADownloadServiceClient copySummaryStringForDownloadServiceError:]
+ +[MADownloadServiceClient copySummaryStringForTrustCacheLoadError:]
+ +[MADownloadServiceClient copySummaryStringForUnmetConstraints:]
+ -[ControlManager isWildcardAllowedForCommand:]
+ -[DownloadManager getCurrentDaemonManagedInFlightDownloads:]
+ -[DownloadManager getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:]
+ -[DownloadManager getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:].cold.1
+ -[DownloadManager reportBackportedServiceConnectionSuccessful:brainBuildVersion:loadRequirements:error:]
+ -[DownloadManager retryTask:retryUrl:modified:clientName:ofJobType:]
+ -[DownloadManager shouldUseDaemonSessionForDownload:jobType:downloadURL:]
+ -[DownloadManager startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:]
+ -[MABrainLoader verifyBundle:]
+ -[MADAnalyticsManager recordBackportedBrainConnectAttemptSuccessful:brainBuildVersion:errorString:]
+ -[MADAutoAssetControlManager _setConfigurationIfDownloadedDescriptorPartOfLatestToVend:fromLocation:]
+ -[MADAutoAssetControlManager attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:trackingSecureFlow:]
+ -[MADAutoAssetControlManager handleWaitForStartupActivated:]
+ -[MADAutoAssetTimed initWithTimeout:]
+ -[MADownloadServiceClient connectingToService]
+ -[MADownloadServiceClient isConnected]
+ -[MADownloadServiceClient setConnectingToService:]
+ -[MADownloadServiceClient setStartDownloadRequestsQueue:]
+ -[MADownloadServiceClient startDownloadRequestsQueue]
+ -[MAUnlockMonitor firstUnlockNotificationTokenValid]
+ -[MAUnlockMonitor firstUnlockNotificationToken]
+ -[MAUnlockMonitor lockStateChangedNotificationTokenValid]
+ -[MAUnlockMonitor lockStateChangedNotificationToken]
+ -[MAUnlockMonitor setFirstUnlockNotificationToken:]
+ -[MAUnlockMonitor setFirstUnlockNotificationTokenValid:]
+ -[MAUnlockMonitor setLockStateChangedNotificationToken:]
+ -[MAUnlockMonitor setLockStateChangedNotificationTokenValid:]
+ GCC_except_table192
+ GCC_except_table4
+ GCC_except_table440
+ GCC_except_table519
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table617
+ GCC_except_table623
+ GCC_except_table638
+ GCC_except_table667
+ GCC_except_table799
+ GCC_except_table800
+ GCC_except_table803
+ _MAPreferencesShouldSecureNetworkMonitorInhibitConnected
+ _OBJC_IVAR_$_MADownloadServiceClient._connectingToService
+ _OBJC_IVAR_$_MADownloadServiceClient._startDownloadRequestsQueue
+ _OBJC_IVAR_$_MAUnlockMonitor._firstUnlockNotificationToken
+ _OBJC_IVAR_$_MAUnlockMonitor._firstUnlockNotificationTokenValid
+ _OBJC_IVAR_$_MAUnlockMonitor._lockStateChangedNotificationToken
+ _OBJC_IVAR_$_MAUnlockMonitor._lockStateChangedNotificationTokenValid
+ _STExtractorErrorDomain
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1934
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1935
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1936
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1370
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1382
+ ___101-[MABrainUpdater installAndConnectToServiceForAsset:withSessionID:options:updateCompletedCompletion:]_block_invoke.1388
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1403
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1404
+ ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1406
+ ___105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1417
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1919
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1926
+ ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1927
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2087
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2088
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2090
+ ___117-[DownloadManager getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:]_block_invoke
+ ___118-[DownloadManager(Pallas) pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.1326
+ ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1917
+ ___123-[MADAutoAssetControlManager attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:trackingSecureFlow:]_block_invoke
+ ___123-[MADAutoAssetControlManager attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:trackingSecureFlow:]_block_invoke_2
+ ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1317
+ ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1318
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1340
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1344
+ ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1360
+ ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1326
+ ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1327
+ ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2219
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1413
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1414
+ ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1418
+ ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1933
+ ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1452
+ ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1465
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2150
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2153
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2158
+ ___22-[ControlManager init]_block_invoke.1374
+ ___224-[DownloadManager startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:]_block_invoke
+ ___224-[DownloadManager startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:]_block_invoke_2
+ ___27-[MABrainUpdater schedule:]_block_invoke.1245
+ ___27-[MABrainUpdater schedule:]_block_invoke.1290
+ ___27-[MABrainUpdater schedule:]_block_invoke.1295
+ ___27-[MABrainUpdater schedule:]_block_invoke_2.1291
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2199
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2206
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2208
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2210
+ ___37-[DownloadManager startDownloadTimer]_block_invoke.1823
+ ___42-[MAUnlockMonitor notifyAfterFirstUnlock:]_block_invoke.1218
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1938
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1939
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1940
+ ___44-[ControlManager handleClientConnection:on:]_block_invoke.1979
+ ___44-[ControlManager handleClientConnection:on:]_block_invoke.1980
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1318
+ ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1364
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1835
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1856
+ ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.1847
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2097
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2098
+ ___47-[MADownloadServiceClient registerWithService:]_block_invoke.541
+ ___49-[MADownloadServiceClient getDownloadSessionType]_block_invoke.549
+ ___49-[MADownloadServiceClient syncUpStateWithService]_block_invoke.643
+ ___50-[MADownloadServiceClient getAllDownloadingTasks:]_block_invoke.557
+ ___50-[MADownloadServiceClient setupServiceConnection:]_block_invoke.534
+ ___50-[MADownloadServiceClient setupServiceConnection:]_block_invoke.534.cold.1
+ ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1345
+ ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1346
+ ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.2011
+ ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1662
+ ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1254
+ ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1257
+ ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1433
+ ___55-[MADownloadServiceClient cancelDownloadForTask:error:]_block_invoke.601
+ ___55-[MADownloadServiceClient getAllDownloadingTasksAsync:]_block_invoke.581
+ ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2221
+ ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2226
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1425
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1426
+ ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1427
+ ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1740
+ ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1741
+ ___60-[DownloadManager getCurrentDaemonManagedInFlightDownloads:]_block_invoke
+ ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.612
+ ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.613
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1374
+ ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1396
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2078
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2079
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2084
+ ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2180
+ ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1351
+ ___68-[DownloadManager retryTask:retryUrl:modified:clientName:ofJobType:]_block_invoke
+ ___68-[MADownloadServiceClient startDownloadWithParameters:replyingWith:]_block_invoke.593
+ ___68-[MADownloadServiceClient startDownloadWithParameters:replyingWith:]_block_invoke_2
+ ___70-[MADownloadServiceClient updateDownloadOptionsForTask:options:error:]_block_invoke.620
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1230
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1231
+ ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1232
+ ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2571
+ ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2572
+ ___74-[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:]_block_invoke
+ ___74-[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:]_block_invoke.1268
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1373
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1374
+ ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1375
+ ___77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1367
+ ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1332
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1391
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1398
+ ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1399
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3544
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3545
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1941
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1942
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1943
+ ___assetTypeWithWildcardDisallowedCharacterSet_block_invoke
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s_e18_v20?0"NSURL"8B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
+ ___block_descriptor_152_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8
+ ___block_descriptor_184_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144r152r160r168r_e5_v8?0lr144l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r152l8s96l8s104l8r160l8s112l8s120l8s128l8s136l8r168l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e56_v40?0"NSString"8"NSString"16"NSString"24"NSError"32ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0lr56l8s32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSTimer"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_91_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s80l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1219
+ ___block_literal_global.1222
+ ___block_literal_global.1226
+ ___block_literal_global.1227
+ ___block_literal_global.1234
+ ___block_literal_global.1238
+ ___block_literal_global.1245
+ ___block_literal_global.1252
+ ___block_literal_global.1267
+ ___block_literal_global.1270
+ ___block_literal_global.1271
+ ___block_literal_global.1275
+ ___block_literal_global.1277
+ ___block_literal_global.1280
+ ___block_literal_global.1285
+ ___block_literal_global.1293
+ ___block_literal_global.1309
+ ___block_literal_global.1315
+ ___block_literal_global.1317
+ ___block_literal_global.1336
+ ___block_literal_global.1346
+ ___block_literal_global.1362
+ ___block_literal_global.1372
+ ___block_literal_global.1373
+ ___block_literal_global.1384
+ ___block_literal_global.1390
+ ___block_literal_global.1398
+ ___block_literal_global.1402
+ ___block_literal_global.1480
+ ___block_literal_global.1530
+ ___block_literal_global.1546
+ ___block_literal_global.1551
+ ___block_literal_global.1573
+ ___block_literal_global.1674
+ ___block_literal_global.1710
+ ___block_literal_global.1714
+ ___block_literal_global.1764
+ ___block_literal_global.1812
+ ___block_literal_global.1864
+ ___block_literal_global.1869
+ ___block_literal_global.1872
+ ___block_literal_global.1884
+ ___block_literal_global.1908
+ ___block_literal_global.1934
+ ___block_literal_global.2179
+ ___block_literal_global.2201
+ ___block_literal_global.2228
+ ___block_literal_global.2388
+ ___block_literal_global.2396
+ ___block_literal_global.2404
+ ___block_literal_global.2412
+ ___block_literal_global.2420
+ ___block_literal_global.2428
+ ___block_literal_global.2436
+ ___block_literal_global.2444
+ ___block_literal_global.2497
+ ___block_literal_global.2606
+ ___block_literal_global.2988
+ ___block_literal_global.3001
+ ___block_literal_global.4201
+ ___block_literal_global.5511
+ ___handleCacheDeletePurgeCallbackForVolume_block_invoke.1252
+ ___handleCacheDeletePurgeableCallbackForVolume_block_invoke.1248
+ _assetTypeWithWildcardDisallowedCharacterSet
+ _assetTypeWithWildcardDisallowedCharacterSet.cold.1
+ _assetTypeWithWildcardDisallowedCharacterSet.disallowedSet
+ _assetTypeWithWildcardDisallowedCharacterSet.once
+ _getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:.keyManager
+ _getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:.keyManagerAllocToken
+ _objc_msgSend$_setConfigurationIfDownloadedDescriptorPartOfLatestToVend:fromLocation:
+ _objc_msgSend$attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:trackingSecureFlow:
+ _objc_msgSend$buildGroup
+ _objc_msgSend$connectingToService
+ _objc_msgSend$copyBrainLoadErrorDomainSummaryStringForError:
+ _objc_msgSend$copyParsedErrorReasonFromBrainLoadError:unmetRequirements:
+ _objc_msgSend$copySummaryStringForCryptexLoadError:
+ _objc_msgSend$copySummaryStringForDownloadServiceError:
+ _objc_msgSend$copySummaryStringForTrustCacheLoadError:
+ _objc_msgSend$copySummaryStringForUnmetConstraints:
+ _objc_msgSend$firstUnlockNotificationToken
+ _objc_msgSend$firstUnlockNotificationTokenValid
+ _objc_msgSend$getCurrentDaemonManagedInFlightDownloads:
+ _objc_msgSend$getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:
+ _objc_msgSend$handleWaitForStartupActivated:
+ _objc_msgSend$initWithTimeout:
+ _objc_msgSend$isConnected
+ _objc_msgSend$isWildcardAllowedForCommand:
+ _objc_msgSend$lockStateChangedNotificationToken
+ _objc_msgSend$lockStateChangedNotificationTokenValid
+ _objc_msgSend$recordBackportedBrainConnectAttemptSuccessful:brainBuildVersion:errorString:
+ _objc_msgSend$reportBackportedServiceConnectionSuccessful:brainBuildVersion:loadRequirements:error:
+ _objc_msgSend$retryTask:retryUrl:modified:clientName:ofJobType:
+ _objc_msgSend$setConnectingToService:
+ _objc_msgSend$setFirstUnlockNotificationToken:
+ _objc_msgSend$setFirstUnlockNotificationTokenValid:
+ _objc_msgSend$setLockAtomicRequests:
+ _objc_msgSend$setLockStateChangedNotificationToken:
+ _objc_msgSend$setLockStateChangedNotificationTokenValid:
+ _objc_msgSend$shouldUseDaemonSessionForDownload:jobType:downloadURL:
+ _objc_msgSend$startDownloadRequestsQueue
+ _objc_msgSend$startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:
+ _objc_msgSend$verifyBundle:
+ _setClass
- +[MADownloadServiceClient getParsedErrorReasonFromBrainLoadError:unmetRequirements:]
- -[DownloadManager reportBackportedDownloadServiceLoadFailure:brainBuildVersion:loadRequirements:error:]
- -[DownloadManager retryTask:retryUrl:modified:clientName:]
- -[DownloadManager startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadInfo:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:]
- -[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:].cold.3
- -[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:].cold.4
- -[MABrainLoader loadBrainFromBundleAtPath:brainLoadRequirements:outError:].cold.5
- -[MADAutoAssetControlManager attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:]
- -[MADAutoAssetStager _stagingClientRequestDetermineLocate:forStagingTargetName:]
- -[MADAutoAssetStager _stagingClientRequestDownloadCurrent:forStagingTargetName:]
- -[MADAutoAssetTimed initForRequest:withTimeout:]
- -[MADAutoAssetTimed requestBeingTimed]
- -[MAUnlockMonitor notificationTokenValid]
- -[MAUnlockMonitor notificationToken]
- -[MAUnlockMonitor notifyAfterFirstUnlock:].cold.1
- -[MAUnlockMonitor setNotificationToken:]
- -[MAUnlockMonitor setNotificationTokenValid:]
- GCC_except_table194
- GCC_except_table36
- GCC_except_table515
- GCC_except_table574
- GCC_except_table575
- GCC_except_table613
- GCC_except_table621
- GCC_except_table636
- GCC_except_table665
- GCC_except_table795
- GCC_except_table796
- GCC_except_table801
- _NOTIFICATION_INTERVAL_KEY_block_invoke_2.keyManager
- _NOTIFICATION_INTERVAL_KEY_block_invoke_2.keyManagerAllocToken
- _OBJC_IVAR_$_MADAutoAssetTimed._requestBeingTimed
- _OBJC_IVAR_$_MAUnlockMonitor._notificationToken
- _OBJC_IVAR_$_MAUnlockMonitor._notificationTokenValid
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1916
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1917
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1918
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1394
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1395
- ___104+[MADAutoAssetSecure personalizeGraftDownloaded:forDescriptor:setDescriptor:allowingNetwork:completion:]_block_invoke.1397
- ___104-[MADAutoAssetControlManager attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:]_block_invoke
- ___104-[MADAutoAssetControlManager attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:]_block_invoke_2
- ___105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1411
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1904
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1911
- ___106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1912
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2071
- ___118-[DownloadManager(Pallas) pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.1317
- ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1899
- ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1308
- ___143-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseSuspendAutoJobsWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1309
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1331
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1335
- ___145+[MADAutoAssetSecure personalizeDownloaded:personalizingDescriptor:allowingNetwork:committingPersonalization:reportingPromotionState:completion:]_block_invoke.1351
- ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1317
- ___148-[MADAutoAssetControlManager(Relinquish) _relinquishSuspend_phaseEvictAtomicInstancesWithNonce:sortedKeys:setConfigurationsToEvict:completionBlock:]_block_invoke.1318
- ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2202
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1404
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1405
- ___152+[MADAutoAssetSecure personalizeSetDownloaded:forSetDescriptor:shouldGraft:allowingNetwork:withAutoAssetDescriptors:reportingPromotionState:completion:]_block_invoke.1409
- ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1915
- ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1443
- ___176-[MADAutoAssetSecure _personalizeGraftSetDownloaded:forSetDescriptor:allowingNetwork:requiringPersonalization:requiringGrafting:shouldGraft:reportingPromotionState:completion:]_block_invoke.1456
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2131
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2134
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2139
- ___22-[ControlManager init]_block_invoke.1365
- ___237-[DownloadManager startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadInfo:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:]_block_invoke
- ___24-[MABrainUpdater commit]_block_invoke
- ___27-[MABrainUpdater schedule:]_block_invoke.1235
- ___27-[MABrainUpdater schedule:]_block_invoke.1280
- ___27-[MABrainUpdater schedule:]_block_invoke.1285
- ___27-[MABrainUpdater schedule:]_block_invoke_2.1281
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2167
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2174
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2176
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2176.cold.1
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2192
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke_2.2193
- ___37-[DownloadManager startDownloadTimer]_block_invoke.1814
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1920
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1921
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1922
- ___44-[ControlManager handleClientConnection:on:]_block_invoke.1964
- ___44-[ControlManager handleClientConnection:on:]_block_invoke.1965
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1309
- ___45+[MADAutoAssetScheduler resumeFromPersisted:]_block_invoke.1355
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1825
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke.1833
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.1835
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.cold.1
- ___46-[DownloadManager setupDownloadManagerService]_block_invoke_2.cold.2
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2078
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2079
- ___47-[MADownloadServiceClient registerWithService:]_block_invoke.540
- ___49-[MADownloadServiceClient getDownloadSessionType]_block_invoke.548
- ___49-[MADownloadServiceClient syncUpStateWithService]_block_invoke.636
- ___50-[MADownloadServiceClient getAllDownloadingTasks:]_block_invoke.556
- ___50-[MADownloadServiceClient setupServiceConnection:]_block_invoke.533
- ___50-[MADownloadServiceClient setupServiceConnection:]_block_invoke.533.cold.1
- ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1336
- ___51-[MABrainUpdater install:asset:options:completion:]_block_invoke.1337
- ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1994
- ___53-[ControlManager getStateOfAsset:incoming:assetType:]_block_invoke.1653
- ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1245
- ___53-[MobileAssetHealthReport scheduleReportWithReports:]_block_invoke.1248
- ___54-[MADAutoAssetScheduler _registerForAndStartActivity:]_block_invoke.1424
- ___55-[MADownloadServiceClient cancelDownloadForTask:error:]_block_invoke.597
- ___55-[MADownloadServiceClient getAllDownloadingTasksAsync:]_block_invoke.573
- ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2206
- ___57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.2211
- ___58-[DownloadManager retryTask:retryUrl:modified:clientName:]_block_invoke
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1416
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1417
- ___60+[MADAutoAssetSecure mapToExclave:forDescriptor:completion:]_block_invoke.1418
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1725
- ___60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1726
- ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.608
- ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.609
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1365
- ___65+[MADAutoAssetLocker resumeFromPersistedWithDownloadedSelectors:]_block_invoke.1387
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2061
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2062
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2067
- ___66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.2165
- ___66-[SecureMobileAssetBundle personalize:completionQueue:completion:]_block_invoke.1342
- ___68-[MADownloadServiceClient startDownloadWithParameters:replyingWith:]_block_invoke.589
- ___70-[MADownloadServiceClient updateDownloadOptionsForTask:options:error:]_block_invoke.616
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1221
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1222
- ___70-[MAPushNotificationServiceDaemon listener:shouldAcceptNewConnection:]_block_invoke.1223
- ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2559
- ___71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2560
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1364
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1365
- ___75+[MADAutoAssetSecure commitPrePersonalized:committingSelectors:completion:]_block_invoke.1366
- ___77-[ControlManager updateSpaceAttributionForBundleID:assetPath:doRegistration:]_block_invoke.1358
- ___77-[MADownloadServiceClient connectToServiceOfType:unmetRequirements:outError:]_block_invoke
- ___79-[MobileAssetHealthReport _submitReportToCoreAnalytics:commonFields:sessionId:]_block_invoke.1323
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1382
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke.1389
- ___82+[MADAutoAssetSecure graftDownloaded:graftingDescriptor:setDescriptor:completion:]_block_invoke_2.1390
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3529
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3530
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1924
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1925
- ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1926
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e18_v20?0"NSURL"8B16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
- ___block_descriptor_184_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s152r160r168r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r152l8s104l8s112l8r160l8s120l8s128l8s136l8s144l8r168l8
- ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_56_e8_32s40s48bs_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSTimer"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56r_e17_v16?0"NSError"8ls32l8s48l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48s56s_e56_v40?0"NSString"8"NSString"16"NSString"24"NSError"32ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e44_v24?0"MADAutoAssetDescriptor"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_83_e8_32s40s48s56s64bs72r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s64l8s48l8s56l8r72l8
- ___block_descriptor_99_e8_32s40s48s56s64s72s80bs88r_e5_v8?0ls32l8s40l8s80l8s48l8s56l8s64l8s72l8r88l8
- ___block_literal_global.1210
- ___block_literal_global.1213
- ___block_literal_global.1217
- ___block_literal_global.1218
- ___block_literal_global.1225
- ___block_literal_global.1229
- ___block_literal_global.1236
- ___block_literal_global.1243
- ___block_literal_global.1246
- ___block_literal_global.1249
- ___block_literal_global.1250
- ___block_literal_global.1253
- ___block_literal_global.1262
- ___block_literal_global.1268
- ___block_literal_global.1269
- ___block_literal_global.1283
- ___block_literal_global.1298
- ___block_literal_global.1306
- ___block_literal_global.1308
- ___block_literal_global.1327
- ___block_literal_global.1337
- ___block_literal_global.1353
- ___block_literal_global.1364
- ___block_literal_global.1389
- ___block_literal_global.1391
- ___block_literal_global.1471
- ___block_literal_global.1513
- ___block_literal_global.1519
- ___block_literal_global.1540
- ___block_literal_global.1562
- ___block_literal_global.1665
- ___block_literal_global.1704
- ___block_literal_global.1705
- ___block_literal_global.1755
- ___block_literal_global.1806
- ___block_literal_global.1855
- ___block_literal_global.1860
- ___block_literal_global.1863
- ___block_literal_global.1866
- ___block_literal_global.1899
- ___block_literal_global.1925
- ___block_literal_global.2169
- ___block_literal_global.2181
- ___block_literal_global.2213
- ___block_literal_global.2376
- ___block_literal_global.2384
- ___block_literal_global.2390
- ___block_literal_global.2392
- ___block_literal_global.2400
- ___block_literal_global.2408
- ___block_literal_global.2416
- ___block_literal_global.2424
- ___block_literal_global.2432
- ___block_literal_global.2488
- ___block_literal_global.2590
- ___block_literal_global.2974
- ___block_literal_global.2987
- ___block_literal_global.4180
- ___block_literal_global.5457
- ___handleCacheDeletePurgeCallbackForVolume_block_invoke.1243
- ___handleCacheDeletePurgeableCallbackForVolume_block_invoke.1239
- _commit.onceToke
- _objc_msgSend$_stagingClientRequestDetermineLocate:forStagingTargetName:
- _objc_msgSend$_stagingClientRequestDownloadCurrent:forStagingTargetName:
- _objc_msgSend$attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:
- _objc_msgSend$getParsedErrorReasonFromBrainLoadError:unmetRequirements:
- _objc_msgSend$initForRequest:withTimeout:
- _objc_msgSend$notificationToken
- _objc_msgSend$notificationTokenValid
- _objc_msgSend$reportBackportedDownloadServiceLoadFailure:brainBuildVersion:loadRequirements:error:
- _objc_msgSend$requestBeingTimed
- _objc_msgSend$retryTask:retryUrl:modified:clientName:
- _objc_msgSend$setNotificationToken:
- _objc_msgSend$setNotificationTokenValid:
- _objc_msgSend$startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadInfo:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:
CStrings:
+ "\""
+ "#"
+ "%@:_setConfigurationIfDownloadedDescriptorPartOfLatestToVend"
+ "%@:personalizeSetDownloaded"
+ "-[DownloadManager getCurrentDaemonManagedInFlightDownloads:]_block_invoke"
+ "/System/Library/CoreServices/RestoreVersion.plist"
+ "0123456789.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-*"
+ "3.5.4"
+ ":AllConstraintsMet"
+ ":BrainLoadSubErrorCode_%ld"
+ ":BundleAssetParseErrorIdentifier"
+ ":BundleAssetParseErrorInfo"
+ ":BundleAssetParseErrorProperties"
+ ":BundleInvalid"
+ ":ConnectionInvalidated"
+ ":ErrorCode_%ld"
+ ":GetServiceProxyFail"
+ ":InitializationFail"
+ ":LoadFailure"
+ ":MABrainLoadErrorBundleAllocFail"
+ ":NotConnected"
+ ":RemoteProxyInvalid"
+ ":TasksDetermineFail"
+ ":TrustCacheInvalid"
+ ":TrustCacheNotPersonalized"
+ ":UnlockRegistrationFail"
+ ":UnsupportedEnvironment"
+ "Allocating extractor for daemon managed task | AssetType:%{public}@"
+ "Asset properties could not be loaded from bundle"
+ "Async"
+ "Backported service cannot be loaded due to bundle verification failure"
+ "BrainBuildVersion"
+ "BrainLoadError"
+ "BrainLoadError:UnmetConstraints"
+ "Creating asset download task | taskDescriptor:%{public}@ | assetType:%{public}@ | autoJobIdentifier:%{public}@"
+ "DEL_AI_LATEST_LST_PERSONALZ"
+ "Download failed due to an error from the Streaming Extractor framework"
+ "Download service client is nil"
+ "Download service client is not connected"
+ "DownloadInfo taskDescriptor: %@ . task: %@ taskState: %@ statusCode: %lld downloadSize: %lld%@ progress: %lld / %lld isStalled: %@ numStalls: %lld numNoLongerStalls: %lld backtracks: %lld callbackCount: %lld hasExtractor: %@ extractorRequired: %@ originalUrl: %@ cacheServerUrl: %@ assetType: %@ purpose: %@ shouldRetry: %@ ifModifiedDate: %@ options: %@%@%@ nsurlsessiontaskID:%@ serviceManaged:%@"
+ "Failed"
+ "Failed to connect to backported service and failed to fall back to builtin. DownloadService not operational"
+ "Failed to connect to backported service and fell back to builtin"
+ "Failed to determine downloading tasks - proxy error"
+ "Failed to determine downloading tasks - service error"
+ "Failed to get downloading tasks - no connection"
+ "Failed to open path: %@ with errno: %d"
+ "Failed to set protection class D on destination folder %@"
+ "IN_PROG_BEGIN_ACCESS       "
+ "IN_PROG_BEGIN_MAP_TO_EXCLAV"
+ "IN_PROG_COMMIT_PRE_PERSNLZD"
+ "IN_PROG_DEPERSONALIZE      "
+ "IN_PROG_END_ACCESS         "
+ "IN_PROG_END_MAP_TO_EXCLAVES"
+ "IN_PROG_PERSONALIZE        "
+ "IN_PROG_PRE_PERSONALIZE    "
+ "Loaded built-in MobileAssetDaemon_Framework Feb 23 2026 04:31:33"
+ "MA-AUTO-CONTROL:WAIT_FOR_STARTUP_ACTIVATED"
+ "MADAutoControl:handleWaitForStartupActivated"
+ "MADownloadSTExtractorError"
+ "Progressed beyond startup activated."
+ "RemaingAttemptCount++|"
+ "Reporting failed backported brain connection | Reason:%{public}@"
+ "Reporting successful backported brain connection"
+ "RestoreLongVersion"
+ "STARTUP personalization failure for asset-descriptor part of latest-to-vend"
+ "Service cryptex requires personalization"
+ "ServiceSetupError"
+ "ServiceType"
+ "Successfully set up extractor for daemon managed asset download | AssetType:%{public}@"
+ "Successfully started download but job no longer exists | TaskDescriptor:%{public}@ | AutoJobIdentifier:%{public}@"
+ "Sync"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_startDownloadRequestsQueue"
+ "TB,R,D,N"
+ "TB,V_connectingToService"
+ "TB,V_firstUnlockNotificationTokenValid"
+ "TB,V_lockStateChangedNotificationTokenValid"
+ "Task will be daemon managed | taskDescriptor:%{public}@"
+ "Ti,V_firstUnlockNotificationToken"
+ "Ti,V_lockStateChangedNotificationToken"
+ "Unable to fetch brainAssetIdentifier from asset properties"
+ "Unable to fetch currently downloading tasks: %{public}@"
+ "Unable to register asset download job (unable to create extractor) | autoAssetJobID:%@, assetType:%@, purpose:%@, assetId:%@ | baseURL:%@, relativeURL:%@ error:%@"
+ "Unable to register asset download job | Invalid Extractor | assetId:%{public}@ | Error:%{public}@"
+ "UnexpectedDomain_%@:ErrorCode_%ld"
+ "UnknownError"
+ "UnknownFailure:"
+ "[%{public}s] Tasks currently tracked via daemon in process session | Count:%lu"
+ "[ANOMALY]:Downloaded brain bundle was invalid"
+ "[AUTO-SECURE-MONITOR] {%{public}@:manageMonitoringOfSecureServer} default-based trigger to ignore connected indication"
+ "[AUTO-SECURE-MONITOR] {secureMonitorNetworkConnected} default-based trigger to ignore connected indication"
+ "[BaseURLOverride]: Overriding baseURL for asset | AssetType:%{public}@ | Override:%{public}@ | type:%{public}@"
+ "[CancelAllDownloading]: Canceling task | ClientName:%{public}@ | TaskDescriptor:%{public}@"
+ "[CancelAllDownloading]: Cancelled successfully| ClientName:%{public}@ | TaskDescription:%{public}@"
+ "[CancelAllDownloading]: Cancelling daemon managed tasks"
+ "[CancelAllDownloading]: Cancelling service managed tasks"
+ "[CancelAllDownloading]: downloadServiceClient unavailable | ClientName:%{public}@"
+ "[CancelAllDownloading]:Failed to determine downloading tasks for cancelAllDownloading | ClientName:%{public}@ | error:%{public}@"
+ "[ConfigAssetDownloadJob]: Updating discretionary config for daemon managed job | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@ | Discretionary:%{public}@"
+ "[ConfigAssetDownload]: Updating config for daemon managed task | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@ | Discretionary:%{public}@"
+ "[ConfigAssetDownload]: Updating config for service managed task | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@ | Discretionary:%{public}@"
+ "[ConnectToServiceOfType]: Already using requested service | serviceName:%{public}@"
+ "[ConnectToServiceOfType]: Attempt to connect to service already in progress"
+ "[ConnectToServiceOfType]: Failed to connect to service | Attempt:%{public}@"
+ "[ConnectToServiceOfType]: Failed to connect to service | serviceName:%{public}@ | Error:%{public}@"
+ "[ConnectToServiceOfType]: Handling request to switch download services | CurrentService:%{public}@ | NewService:%{public}@"
+ "[ConnectToServiceOfType]: Invalidating connection to previous service"
+ "[ConnectToServiceOfType]: Loading of brain failed due to unmet requirements | Located:%{public}@ | NeedsUnlock:%{public}@ | NeedsDaemonRestart:%{public}@ | NeedsPersonalization:%{public}@"
+ "[ConnectToServiceOfType]: Loading of brain failed with error | error:%{public}@"
+ "[ConnectToServiceOfType]: No downloaded brain was found"
+ "[ConnectToServiceOfType]: Successfully connected to service | Attempt:%{public}@"
+ "[ConnectToService]: Already connected to service"
+ "[ConnectToService]: Creating service connection object"
+ "[ConnectToService]: Failed to register with service | Error:%{public}@"
+ "[ConnectToService]: Failed to setup service connection | Error:%{public}@"
+ "[ConnectToService]: Registration with service complete"
+ "[ConnectToService]: Unable to establish connection to remote service"
+ "[GetAllDownloadingTasks]: Failed to get remoteObjectProxy for service: %{public}@"
+ "[GetFinalURL]: Determining URL for Asset | AssetType:%{public}@ | KnoxURL:%{public}@ | DecryptionKey:%{public}@ | BaseURL:%{public}@ | relativeURL:%{public}@@"
+ "[GetFinalURL]: Error determining if decryption key exists in asset metadata. Assuming NO | Error:%{public}@"
+ "[GetFinalURL]: Found decryption key in asset metadata | AssetType:%{public}@"
+ "[MAB] Done purging brain after cryptex load failure"
+ "[MAB] Done purging brain after cryptex load failure | Error:%{public}@ "
+ "[MAB] Done purging brain after invalid bundle found"
+ "[MAB] Done purging brain after invalid bundle found | Error:%{public}@ "
+ "[MAB] Error committing MobileAssetBrain | No bundle passed to commit"
+ "[MAB] Failed to determine brainAssetIdentifier from asset properties | Path:%{public}@"
+ "[MAB] Failed to fallback to builtin service after brain connection error. ****DownloadService NOT operational**** | Error:%{public}@"
+ "[MAB] Failed to read brainInfo from bundle | Path:%{public}@"
+ "[MAB] Fell back to builtin service after backported service connection failure"
+ "[MAB] MobileAssetBrain install failed | Error:%{public}@"
+ "[MAB] No current MobileAssetBrain set"
+ "[MAB] Performing garbage collection before scheduling MABrain scan"
+ "[MAB] Performing garbageCollect after commit of new MobileAssetBrain"
+ "[MAB] Purge of asset completed | Error:%{public}@"
+ "[MAB] Purge of brain completed | Error:%{public}@"
+ "[MAB] Purging asset due to inability to connect to the service"
+ "[MAB] Purging brain on cryptex load failure | AssetIdentifier:%{public}@"
+ "[MAB] Purging invalid brain bundle | AssetIdentifier:%{public}@"
+ "[MAB] Successfully staged proposed brain bundle: %{public}@"
+ "[MAB] Unable to connect to service due to invalid personalization. Purging brain"
+ "[MAB] Unable to connect to service(Purging brain) | Constraints unmet | Constraints:%lx "
+ "[MAB] Unable to load asset properties from bundle | Path:%{public}@"
+ "[MAB] [ScanForBrain]: Attempting to compare local and remote restore versions | LocalRestoreVersion:%{public}@ | RemoteRestoreVersion:%{public}@"
+ "[MAB] [ScanForBrain]: Available brain doesn't have any declared features.  Asset requires: %@"
+ "[MAB] [ScanForBrain]: Local and remote restore versions are not comparable and cross build group brains are not allowed"
+ "[MAB] [ScanForBrain]: Local and remote restore versions are not comparable but cross build group brains are allowed"
+ "[MAB] [ScanForBrain]: Located brain is older than or same as the current brain | LocalRestoreVersion:%{public}@ | RemoteRestoreVersion:%{public}@"
+ "[MAB] [ScanForBrain]: Located newer brain | RemoteRestoreVersion:%{public}@"
+ "[MAB] [ScanForBrain]: New brain doesn't meet requirements: %@"
+ "[MAB] [ScanForBrain]: New brain features: %@"
+ "[MAB] [ScanForBrain]: New brain meets asset requirements - going forward with the update"
+ "[MAB] [ScanForBrain]: Using restoreVersion from current OS | RestoreVersion:%{public}@"
+ "[MAB] [ScanForBrain]: Using restoreVersion of current brain | RestoreVersion:%{public}@"
+ "[MAB] [ScanForBrain]: Using restoreVersion passed in via options | RestoreVersion:%{public}@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ RestoreVersion string is invalid: %@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ RestoreVersion.plist could not be loaded: %@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ is from a different build group than the OS, but cross build group brains are allowed. (%ld -> %ld)"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ is from a different build group than the OS. (%ld -> %ld)"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ is newer than the current OS: %@ > %@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ is older than current OS: %@ < %@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ is same as the current OS,but same version brains are allowed: %@ == %@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle %@ is the same as the current OS and same version brains are not allowed: %@ == %@"
+ "[MAB] [VerifyBundle]: MobileAssetBrain bundle is valid | BundleName:%{public}@ | BrainRestoreVersion:%{public}@"
+ "[MAB] [VerifyBundle]: System RestoreVersion string is invalid: %@"
+ "[MAB] [VerifyBundle]: Validating bundle | BrainRestoreVersion:%{public}@ | OSRestoreVersion:%{public}@"
+ "[MAUnlockMonitor]: Failed to register for first unlock notification"
+ "[MAUnlockMonitor]: Failed to register for lock state changed notifications"
+ "[MAUnlockMonitor]: FirstUnlockNotification: Handling notification"
+ "[MAUnlockMonitor]: FirstUnlockNotification: Object invalid"
+ "[MAUnlockMonitor]: LockStateChanged notification received | state:%{public}d"
+ "[MAUnlockMonitor]: LockStateChanged: Device unlocked | KeybagState:%{public}d"
+ "[MAUnlockMonitor]: LockStateChanged: Object invalid"
+ "[MAUnlockMonitor]: Notifying client about beyond first unlock | BeyondFirstUnlock:%{public}@ | Error:%{public}@"
+ "[RegisterWithService]: MADownloadService registered successfully | Features:%{public}@"
+ "[RetryServiceConnect]: *****DownloadService NOT operational after max retries(connection failed)******"
+ "[RetryServiceConnect]: Backported service connection needs daemon restart. Falling back to builtin"
+ "[RetryServiceConnect]: Failed to connect to download service even after max retries exhausted"
+ "[RetryServiceConnect]: Fell back to builtin download service after max retries"
+ "[RetryServiceConnect]: Retrying connection to service | serviceType:%{public}lu"
+ "[RetryServiceConnect]: Successfully connected to service on retry | serviceType:%{public}lu"
+ "[RetryServiceConnect]: Unable to connect to service on retry |Error:%{public}@ | UnmetConstraints:%{public}lu | RetriesRemaining:%{public}lu"
+ "[RetryTask]: Retrying daemon managed task | taskDescriptor:%{public}@"
+ "[RetryTask]: Retrying service managed task | taskDescriptor:%{public}@"
+ "[ServiceConnect]: Connection lost during registration"
+ "[ServiceConnect]: Connection to service lost immediately after successful connection attempt"
+ "[ServiceConnect]: Failed to connect to service: %{public}@"
+ "[ServiceConnect]: Unable to register with service: %{public}@"
+ "[ServiceConnectionInterrupted]: Ignoring connection interrupted since service setup is ongoing"
+ "[ServiceInitialization]: Attempting to reconnect to inbuilt service after failed initialization"
+ "[ServiceInitialization]: Backported brain personalization invalid. Falling back to builtin"
+ "[ServiceInitialization]: Backported service bundle invalid. Falling back to builtin"
+ "[ServiceInitialization]: Failed to initialize DownloadService: %{public}@"
+ "[ServiceInitialization]: Failed to setup backported service. Falling back to builtin | error:%{public}@"
+ "[ServiceInitialization]: Successfully connected to backported service after device unlock"
+ "[ServiceInitialization]: Successfully connected to backported service on initial attempt"
+ "[ServiceInitialization]: Successfully connected to builtin download service"
+ "[ServiceInitialization]: SyncedWithDownloadService:(%@) - FetchedSessionType:(%@): %{public}@"
+ "[StartDownloadWithParameters]: Failed to get remoteObjectProxy for service | error:%{public}@"
+ "[StartDownload]: Failed to start daemon managed download | taskDescriptor:%{public}@"
+ "[StartDownload]: Starting daemon managed asset download | assetType:%{public}@"
+ "[StartDownload]: Starting service managed asset download | assetType:%{public}@"
+ "[StartDownload]: The in process download taskID is: %{public}@ and url is: %{public}@ and %{public}@. task %{public}@ options %{public}@"
+ "[StartDownload]: Updating daemon managed task to non discretionary | TaskDecriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[StartDownload]: Updating options for service managed task | TaskDecriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "_connectingToService"
+ "_firstUnlockNotificationToken"
+ "_firstUnlockNotificationTokenValid"
+ "_lockStateChangedNotificationToken"
+ "_lockStateChangedNotificationTokenValid"
+ "_setConfigurationIfDownloadedDescriptorPartOfLatestToVend:fromLocation:"
+ "_startDownloadRequestsQueue"
+ "added-check-atomic(eventInfo:%@)|"
+ "added-lock-atomic(eventInfo:%@)|"
+ "already-attempting|"
+ "attemptSetPersonalization called|"
+ "attemptSetPersonalization:%@|"
+ "attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:trackingSecureFlow:"
+ "begin-attempt(eventInfo:%@)|"
+ "buildGroup"
+ "com.apple.MobileAsset.MADownloadServiceStartDownloadRequestsQueue"
+ "com.apple.mobileassetd.DownloadService.Connect"
+ "connectingToService"
+ "copyBrainLoadErrorDomainSummaryStringForError:"
+ "copyParsedErrorReasonFromBrainLoadError:unmetRequirements:"
+ "copySummaryStringForCryptexLoadError:"
+ "copySummaryStringForDownloadServiceError:"
+ "copySummaryStringForTrustCacheLoadError:"
+ "copySummaryStringForUnmetConstraints:"
+ "firstUnlockNotificationToken"
+ "firstUnlockNotificationTokenValid"
+ "getCurrentDaemonManagedInFlightDownloads:"
+ "getFinalURLForAssetType:withBase:relativeTo:downloadOptions:catalogMetadata:extractor:withPurpose:"
+ "handleWaitForStartupActivated"
+ "handleWaitForStartupActivated:"
+ "initWithTimeout:"
+ "isConnected"
+ "isWildcardAllowedForCommand:"
+ "lockStateChangedNotificationToken"
+ "lockStateChangedNotificationTokenValid"
+ "missing:%@|"
+ "recordBackportedBrainConnectAttemptSuccessful:brainBuildVersion:errorString:"
+ "reportBackportedServiceConnectionSuccessful:brainBuildVersion:loadRequirements:error:"
+ "response(missing)|"
+ "response-unsupported-request(eventInfo:%@)|"
+ "retryTask:retryUrl:modified:clientName:ofJobType:"
+ "setConnectingToService:"
+ "setFirstUnlockNotificationToken:"
+ "setFirstUnlockNotificationTokenValid:"
+ "setLockStateChangedNotificationToken:"
+ "setLockStateChangedNotificationTokenValid:"
+ "setStartDownloadRequestsQueue:"
+ "shouldUseDaemonSessionForDownload:jobType:downloadURL:"
+ "startDownloadRequestsQueue"
+ "startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:"
+ "v116@0:8@16@24@32@40q48@56@64@72@80@88B96@100@108"
+ "v36@0:8B16@20@28"
+ "v44@0:8B16@20Q28@36"
+ "verifyBundle:"
+ "{%{public}@} secureFlow:%{public}@"
+ "{cancelAssetDownloadJob} Canceling job for daemon managed task | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadJob} Canceling job for service managed task | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTaskWithResponse} Canceling daemon managed task | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTask} Canceling daemon managed task | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTask} Canceling service managed task | taskDescriptor:%{public}@"
+ "{removeAssetDir} Failed to cancel task within timeout | TaskDescriptor:%{public}@"
+ "{removeAssetDir} Scheduling task cancel | TaskDescriptor:%{public}@ | ClientCallType:%{public}@"
+ "{removeAssetDir} Unable to cancel download for task | TaskDescriptor:%{public}@ Error:%{public}@"
+ "|timeout:%ld|timerUUID:%@|instance:%@|invalidated:%@|"
- "%@:personalizeGraftSetDownloaded"
- "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] | LOCATE-NOT-TRACKED | DetermineRequests:%ld"
- "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DETERMINE)] | LOCATED | DetermineRequests:%ld | locatedRequest:%{public}@"
- "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DOWNLOAD)] | LOCATE-NOT-TRACKED"
- "%{public}@\n[%{public}@] {%{public}@} [STAGING-CLIENT-REQUEST(DOWNLOAD)] | LOCATED | locatedRequest:%{public}@"
- "3.5.3"
- ":BrainLoadFail"
- ":BrainLoadFail:UnmetConstraints"
- ":BundleAllocFail"
- ":ServiceProxyFail"
- ":TrustCacheLoadFailAMFI"
- ":UnknownError_%ld"
- ":UnknownFailure"
- "@"
- "AAError"
- "Already using requested service | serviceName:%{public}@"
- "Assertion failed: (brainAssetIdentifier != nil), Should always be able to obtain a BrainAssetIdentifier from asset properties"
- "Assertion failed: (brainAssetProperties != nil), Should always be able to load asset properties from downloaded brain bundle"
- "Assertion failed: (brainInfo != nil), Should always be able to load contents of MobileAssetBrain.plist from bundle"
- "Assertion failed: (sessionType != MADownloadSessionTypeUnknown), Failed to get session type for MAdownloadService"
- "Assertion failed: (status == NOTIFY_STATUS_OK), Should be able to register for first unlock notification"
- "BUG IN MobileAsset: Assertion failed: (brainAssetIdentifier != nil), Should always be able to obtain a BrainAssetIdentifier from asset properties"
- "BUG IN MobileAsset: Assertion failed: (brainAssetProperties != nil), Should always be able to load asset properties from downloaded brain bundle"
- "BUG IN MobileAsset: Assertion failed: (brainInfo != nil), Should always be able to load contents of MobileAssetBrain.plist from bundle"
- "BUG IN MobileAsset: Assertion failed: (sessionType != MADownloadSessionTypeUnknown), Failed to get session type for MAdownloadService"
- "BUG IN MobileAsset: Assertion failed: (status == NOTIFY_STATUS_OK), Should be able to register for first unlock notification"
- "BUG IN MobileAsset: Failure during initial sync with MAdownloadService"
- "Canceling task | ClientName:%{public}@ | TaskDescriptor:%{public}@"
- "Cancelled successfully| ClientName:%{public}@ | TaskDescription:%{public}@"
- "Creating asset download task for: %{public}@, %{public}@"
- "Determining URL for Asset(Type: %@ ID: %@): KnoxURL: %@ DecryptionKey: %@ BaseURL: %@ relativeURL: %@"
- "DownloadInfo taskDescriptor: %@ . task: %@ taskState: %@ statusCode: %lld downloadSize: %lld%@ progress: %lld / %lld isStalled: %@ numStalls: %lld numNoLongerStalls: %lld backtracks: %lld callbackCount: %lld hasExtractor: %@ extractorRequired: %@ originalUrl: %@ cacheServerUrl: %@ assetType: %@ purpose: %@ shouldRetry: %@ ifModifiedDate: %@ options: %@%@%@ nsurlsessiontaskID:%@"
- "Error determining if decryption key exists in asset metadata. Assuming NO | Error:%{public}@"
- "Failed to connect to download service even after max retries exhausted"
- "Failed to determine downloading tasks for cancelAllDownloading | ClientName:%{public}@ | error:%{public}@"
- "Failed to get downloading tasks"
- "Failure during initial sync with MAdownloadService"
- "Found decryption key in asset metadata | AssetType:%{public}@"
- "Full URL is %{public}@"
- "Loaded built-in MobileAssetDaemon_Framework Feb 16 2026 02:16:24"
- "Loading of brain failed due to unmet requirements | Located:%{public}@ | NeedsUnlock:%{public}@ | NeedsDaemonRestart:%{public}@ | NeedsPersonalization:%{public}@"
- "Loading of brain failed with error | error:%{public}@"
- "No downloaded brain was found"
- "Recording failure to load brain: %{public}@"
- "Shutdown of previously running service completed successfully"
- "T@,R,&,N,V_requestBeingTimed"
- "TB,V_notificationTokenValid"
- "Ti,V_notificationToken"
- "Unable to fetch currently downloading tasks | Error:%{public}@"
- "Unable to register asset download job (unable to create catalog-based extractor) | autoAssetJobID:%@, assetType:%@, purpose:%@, assetId:%@ | baseURL:%@, relativeURL:%@ error:%@"
- "UnknownSubFailure_%ld"
- "[BaseURLOverride]: Final baseURLOverride for asset(%@) is %@"
- "[ConfigAssetDownload]: Updating config for download | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
- "[ConnectToService]: Failed to connect to service | Attempt:%{public}@"
- "[ConnectToService]: Failed to connect to service | serviceName:%{public}@ | Error:%{public}@"
- "[ConnectToService]: Handling request to switch download services | CurrentService:%{public}@ | NewService:%{public}@"
- "[ConnectToService]: Successfully connected to service | Attempt:%{public}@"
- "[GetAllDownloadingTasks]: Failed to get remoteObjectProxy for service | error:%{public}@"
- "[GetDownloadSessionType]: Failed to get remoteObjectProxy for service | error:%{public}@"
- "[MAB] Available brain doesn't have any declared features.  Asset requires: %@"
- "[MAB] New brain doesn't meet requirements: %@"
- "[MAB] New brain features: %@"
- "[MAB] New brain meets asset requirements - going forward with the update"
- "[MAB] No proposed or current brain found"
- "[MAB] Unable to connect to service | Constraints unmet | Constraints:%lx "
- "[ServiceConnect]: Already connected to service"
- "[ServiceConnect]: Connection to service lost after successful connection attempt"
- "[ServiceConnect]: Creating service connection object"
- "[ServiceConnect]: Failed to register with service | Error:%{public}@"
- "[ServiceConnect]: Failed to setup service connection | Error:%{public}@"
- "[ServiceConnect]: MADownloadService registered successfully | Features:%{public}@"
- "[ServiceConnect]: Registration with service complete"
- "[ServiceConnect]: Unable to connect to service | Error:%{public}@"
- "[ServiceConnect]: Unable to establish connection to remote service"
- "[ServiceConnect]: Unable to register with service"
- "[ServiceInitialization]: *****DownloadService NOT operational after max retries(connection failed)******"
- "[ServiceInitialization]: Attemting to reconnect to inbuilt service after failed initialization"
- "[ServiceInitialization]: Failed to initialize DownloadService | Error: %{public}@"
- "[ServiceInitialization]: Failed to load brain/backported service on initial attempt. Will retry | error:%{public}@"
- "[ServiceInitialization]: Fell back to builtin download service after max retries"
- "[ServiceInitialization]: Loading of backported service requires brain personalization. Using builtin service"
- "[ServiceInitialization]: Retrying connection to service | serviceType:%{public}lu"
- "[ServiceInitialization]: Successfully connected to inbuilt download service"
- "[ServiceInitialization]: Successfully connected to service on retry | serviceType:%{public}lu"
- "[ServiceInitialization]: Sync with DownloadService failed | Error:%{public}@"
- "[ServiceInitialization]: Unable to connect to service on retry |Error:%{public}@ | UnmetConstraints:%{public}lu | RetriesRemaining:%{public}lu"
- "_notificationToken"
- "_notificationTokenValid"
- "_requestBeingTimed"
- "_stagingClientRequestDetermineLocate:forStagingTargetName:"
- "_stagingClientRequestDownloadCurrent:forStagingTargetName:"
- "attemptSetPersonalization:forSPIMethodName:forSetDescriptor:withEventInfo:"
- "getParsedErrorReasonFromBrainLoadError:unmetRequirements:"
- "initForRequest:withTimeout:"
- "notificationToken"
- "notificationTokenValid"
- "reportBackportedDownloadServiceLoadFailure:brainBuildVersion:loadRequirements:error:"
- "requestBeingTimed"
- "retryTask:retryUrl:modified:clientName:"
- "setNotificationToken:"
- "setNotificationTokenValid:"
- "startDownloadTaskUsingMADownloadService:taskDescriptor:autoAssetJobIdentifier:downloadOptions:downloadInfo:downloadSize:startingAt:withLength:extractWith:catalogMetadata:modified:isCachingServer:originalURL:clientName:"
- "v124@0:8@16@24@32@40@48q56@64@72@80@88@96B104@108@116"
- "v48@0:8Q16@24Q32@40"
- "{removeAssetDir} Failed to cancel download for task within timeout | TaskDescriptor:%{public}@"
- "{removeAssetDir} Failed to cancel download for task | TaskDescriptor:%{public}@ Error:%{public}@"
- "|request:%@|timeout:%ld|timerUUID:%@|instance:%@|invalidated:%@|"

```
