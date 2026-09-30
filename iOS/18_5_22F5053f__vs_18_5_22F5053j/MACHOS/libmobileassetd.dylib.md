## libmobileassetd.dylib

> `/usr/lib/libmobileassetd.dylib`

```diff

-1487.120.52.0.0
-  __TEXT.__text: 0x278c0c
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_stubs: 0x22860
-  __TEXT.__objc_methlist: 0x10534
-  __TEXT.__const: 0x489e
-  __TEXT.__cstring: 0x37e0c
-  __TEXT.__objc_methname: 0x3dbb2
-  __TEXT.__objc_classname: 0xe6d
-  __TEXT.__objc_methtype: 0x3ba8
-  __TEXT.__oslogstring: 0x4cb41
-  __TEXT.__gcc_except_tab: 0x3030
+1487.120.62.0.0
+  __TEXT.__text: 0x27a750
+  __TEXT.__auth_stubs: 0x2480
+  __TEXT.__objc_stubs: 0x228c0
+  __TEXT.__objc_methlist: 0x105ac
+  __TEXT.__const: 0x488e
+  __TEXT.__cstring: 0x3810c
+  __TEXT.__objc_methname: 0x3de49
+  __TEXT.__objc_classname: 0xe6b
+  __TEXT.__objc_methtype: 0x3b54
+  __TEXT.__oslogstring: 0x4dae5
+  __TEXT.__gcc_except_tab: 0x3118
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__swift5_typeref: 0x1093
   __TEXT.__constg_swiftt: 0x14fc

   __TEXT.__swift5_protos: 0x60
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4860
+  __TEXT.__unwind_info: 0x4870
   __TEXT.__eh_frame: 0x3284
-  __DATA_CONST.__auth_got: 0x1228
-  __DATA_CONST.__got: 0x680
+  __DATA_CONST.__auth_got: 0x1250
+  __DATA_CONST.__got: 0x690
   __DATA_CONST.__auth_ptr: 0xa20
-  __DATA_CONST.__const: 0x6828
-  __DATA_CONST.__cfstring: 0x2bbe0
+  __DATA_CONST.__const: 0x6850
+  __DATA_CONST.__cfstring: 0x2bda0
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9908
-  __DATA_CONST.__objc_arraydata: 0xb98
+  __DATA_CONST.__objc_selrefs: 0x9940
+  __DATA_CONST.__objc_arraydata: 0xbb8
   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_intobj: 0x570
   __DATA_CONST.__objc_dictobj: 0x118
-  __DATA.__objc_const: 0x15120
+  __DATA.__objc_const: 0x15160
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0x808
   __DATA.__objc_superrefs: 0x2f0
-  __DATA.__objc_ivar: 0x13f0
+  __DATA.__objc_ivar: 0x13f4
   __DATA.__objc_data: 0xdb0
   __DATA.__data: 0x26c8
-  __DATA.__bss: 0x51d0
+  __DATA.__bss: 0x51b0
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x1978
   __DATA_DIRTY.__bss: 0x318

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 8361
-  Symbols:   15446
-  CStrings:  16823
+  Functions: 8370
+  Symbols:   15468
+  CStrings:  16876
 
Symbols:
+ +[MADAutoAssetControlManager preferenceMaxStagerFilesystemMegabytes]
+ +[MADAutoAssetControlManager preferenceStagerInjectAvailableDups]
+ +[MADAutoAssetControlManager preferenceStagerInjectAvailableOlderVersions]
+ +[MADAutoAssetHistory recordOperation:toHistoryType:fromLayer:forTargetOSVersion:forTargetBuildVersion:withAddendumMessage:]
+ -[DownloadManager getBaseURLOverrideForAssetType:].cold.1
+ -[DownloadManager keyManager]
+ -[DownloadManager pallasDelegate]
+ -[DownloadManager setKeyManager:]
+ -[DownloadManager setPallasDelegate:]
+ -[DownloaderSessionDelegate .cxx_destruct]
+ -[DownloaderSessionDelegate keyManagerDelegate]
+ -[DownloaderSessionDelegate queue]
+ -[MADAutoAssetControlManager preferenceMaxStagerFilesystemMegabytes]
+ -[MADAutoAssetControlManager preferenceStagerInjectAvailableDups]
+ -[MADAutoAssetControlManager preferenceStagerInjectAvailableOlderVersions]
+ -[MADAutoAssetControlManager setPreferenceMaxStagerFilesystemMegabytes:]
+ -[MADAutoAssetControlManager setPreferenceStagerInjectAvailableDups:]
+ -[MADAutoAssetControlManager setPreferenceStagerInjectAvailableOlderVersions:]
+ -[MADAutoAssetDescriptor initForAssetType:fromMetadata:fromBaseDescriptor:substitutingAssetVersion:invalidReasons:]
+ -[MADAutoAssetStager considerInjectionIntoAvailableForStaging]
+ -[MADAutoAssetStager dedupAvailableForStaging:dedupingAssetDescriptors:ofContainerName:]
+ -[MAKeyManagerDownloadSessionDelegate baaCertManager]
+ -[MAKeyManagerDownloadSessionDelegate copyKeyAndBAACerificateChain:]
+ -[MAKeyManagerDownloadSessionDelegate copyKeyAndSelfSignedCertificateChain:]
+ -[MAKeyManagerDownloadSessionDelegate initWithName:certType:]
+ -[MAKeyManagerDownloadSessionDelegate refreshBAACertificate]
+ -[MAKeyManagerDownloadSessionDelegate underlyingQueue]
+ -[MobileAssetHealthReport init]
+ -[MobileAssetHealthReport scheduleReport]
+ -[MobileAssetHealthReport setLastReportDate:]
+ -[MobileAssetKeyManager initWithDelegate:]
+ GCC_except_table135
+ GCC_except_table142
+ GCC_except_table174
+ GCC_except_table251
+ GCC_except_table31
+ GCC_except_table420
+ GCC_except_table45
+ GCC_except_table609
+ GCC_except_table611
+ GCC_except_table617
+ GCC_except_table619
+ GCC_except_table633
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table769
+ OBJC_IVAR_$_DownloadManager._keyManager
+ OBJC_IVAR_$_DownloadManager._pallasDelegate
+ OBJC_IVAR_$_DownloaderSessionDelegate._keyManagerDelegate
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceMaxStagerFilesystemMegabytes
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerInjectAvailableDups
+ OBJC_IVAR_$_MADAutoAssetControlManager._preferenceStagerInjectAvailableOlderVersions
+ OBJC_IVAR_$_MAKeyManagerDownloadSessionDelegate._baaCertManager
+ OBJC_IVAR_$_MAKeyManagerDownloadSessionDelegate._underlyingQueue
+ _OBJC_EHTYPE_$_NSException
+ _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
+ __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1206
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1629
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1636
+ __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1637
+ __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2135
+ __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2312
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2241
+ __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2253
+ __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2293
+ __37-[DownloadManager startDownloadTimer]_block_invoke.1719
+ __41-[MobileAssetHealthReport scheduleReport]_block_invoke.1071
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1687
+ __44-[ControlManager handleClientConnection:on:]_block_invoke.1688
+ __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2191
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1874
+ __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1881
+ __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1835
+ __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1919
+ __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1529
+ __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1884
+ __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2322
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2519
+ __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2520
+ ___31-[MobileAssetHealthReport init]_block_invoke
+ ___41-[MobileAssetHealthReport scheduleReport]_block_invoke
+ ___45-[MobileAssetHealthReport setLastReportDate:]_block_invoke
+ ___50-[DownloadManager getBaseURLOverrideForAssetType:]_block_invoke
+ ___68-[MAKeyManagerDownloadSessionDelegate copyKeyAndBAACerificateChain:]_block_invoke
+ ___block_descriptor_40_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ __block_literal_global.1074
+ __block_literal_global.1288
+ __block_literal_global.1293
+ __block_literal_global.1295
+ __block_literal_global.1358
+ __block_literal_global.1380
+ __block_literal_global.2047
+ __block_literal_global.2069
+ __block_literal_global.2241
+ __block_literal_global.2252
+ __block_literal_global.2260
+ __block_literal_global.2268
+ __block_literal_global.2273
+ __block_literal_global.2276
+ __block_literal_global.2284
+ __block_literal_global.2292
+ __block_literal_global.2300
+ __block_literal_global.2308
+ __block_literal_global.2318
+ __block_literal_global.2365
+ __block_literal_global.2367
+ __block_literal_global.2386
+ _dispatch_async_and_wait
+ _kMobileAssetPreferencesAutoAssetStagerFilesystemMaxMegabytes
+ _kMobileAssetPreferencesAutoAssetStagerInjectAvailableDups
+ _kMobileAssetPreferencesAutoAssetStagerInjectAvailableOlderVersions
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$URLSession:didReceiveChallenge:completionHandler:
+ _objc_msgSend$baaCertManager
+ _objc_msgSend$considerInjectionIntoAvailableForStaging
+ _objc_msgSend$copyKeyAndBAACerificateChain:
+ _objc_msgSend$copyKeyAndSelfSignedCertificateChain:
+ _objc_msgSend$dedupAvailableForStaging:dedupingAssetDescriptors:ofContainerName:
+ _objc_msgSend$downloadSessionDelegate
+ _objc_msgSend$initForAssetType:fromMetadata:fromBaseDescriptor:substitutingAssetVersion:invalidReasons:
+ _objc_msgSend$initWithName:certType:
+ _objc_msgSend$keyManager
+ _objc_msgSend$keyManagerDelegate
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$pallasDelegate
+ _objc_msgSend$preferenceMaxStagerFilesystemMegabytes
+ _objc_msgSend$preferenceStagerInjectAvailableDups
+ _objc_msgSend$preferenceStagerInjectAvailableOlderVersions
+ _objc_msgSend$reason
+ _objc_msgSend$recordOperation:toHistoryType:fromLayer:forTargetOSVersion:forTargetBuildVersion:withAddendumMessage:
+ _objc_msgSend$refreshBAACertificate
+ _objc_msgSend$scheduleReport
+ _objc_msgSend$setKeyManager:
+ _objc_msgSend$setPallasDelegate:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_setProperty_atomic_copy
+ _xpc_dictionary_create_empty
+ getBaseURLOverrideForAssetType:.deviceClassSupportsSeaShip
+ getBaseURLOverrideForAssetType:.onceToken
- -[ControlManager downloadManager]
- -[DownloadManager MACopyDawToken:].cold.1
- -[DownloadManager authPallasBAACertManager]
- -[DownloadManager authPallasSessionDelegate]
- -[DownloadManager authPallasSession]
- -[DownloadManager decryptContentEncryptedAssetAtPathIfRequired:].cold.1
- -[DownloadManager downloadNeedsSSO:taskDescriptor:url:].cold.1
- -[DownloadManager setAuthPallasBAACertManager:]
- -[DownloadManager setAuthPallasSession:]
- -[DownloadManager setAuthPallasSessionDelegate:]
- -[DownloadManager setOperationQueue:]
- -[DownloadManager setSplunkOperationQueue:]
- -[MADAutoAssetControlManager _initializePeriodicHealthReport]
- -[MobileAssetHealthReport initWithInterval:leeway:]
- -[MobileAssetHealthReport reportCadance]
- -[MobileAssetHealthReport reportLeeway]
- -[MobileAssetHealthReport reportTimer]
- -[MobileAssetHealthReport scheduleReport:]
- -[MobileAssetHealthReport setLastRerpotDate:]
- -[MobileAssetHealthReport setReportCadance:]
- -[MobileAssetHealthReport setReportLeeway:]
- -[MobileAssetHealthReport setReportTimer:]
- GCC_except_table136
- GCC_except_table143
- GCC_except_table176
- GCC_except_table257
- GCC_except_table28
- GCC_except_table30
- GCC_except_table32
- GCC_except_table34
- GCC_except_table36
- GCC_except_table38
- GCC_except_table421
- GCC_except_table610
- GCC_except_table612
- GCC_except_table618
- GCC_except_table620
- GCC_except_table634
- GCC_except_table75
- GCC_except_table767
- MACopyDawToken:.manager
- MACopyDawToken:.mobileAssetKeyManagerAllocDispatchOnce
- OBJC_IVAR_$_ControlManager._downloadManager
- OBJC_IVAR_$_DownloadManager._authPallasBAACertManager
- OBJC_IVAR_$_DownloadManager._authPallasSession
- OBJC_IVAR_$_DownloadManager._authPallasSessionDelegate
- OBJC_IVAR_$_MobileAssetHealthReport._reportCadance
- OBJC_IVAR_$_MobileAssetHealthReport._reportLeeway
- OBJC_IVAR_$_MobileAssetHealthReport._reportTimer
- __105-[MobileAssetKeyManager requestServerForDecryptionKey:recipientPrivateKey:downloadOptions:disableUI:err:]_block_invoke.1207
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1642
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1649
- __106-[ControlManager respondToCacheDelete:targetingPurgeAmount:cacheDeleteResults:withUrgency:forVolume:then:]_block_invoke.1650
- __110-[DownloadManager pallasRequestV2:normalizedType:withPurpose:options:using:with:autoAssetJob:clientName:then:]_block_invoke.2134
- __149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2311
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2245
- __184-[DownloadManager startDownloadAndUpdateState:for:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:]_block_invoke.2257
- __287-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:]_block_invoke.2292
- __37-[DownloadManager startDownloadTimer]_block_invoke.1720
- __42-[MobileAssetHealthReport scheduleReport:]_block_invoke.1077
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1700
- __44-[ControlManager handleClientConnection:on:]_block_invoke.1701
- __47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2189
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1876
- __51-[DownloadManager queryNSUrlSessiondAndUpdateState]_block_invoke.1882
- __52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1836
- __57-[ControlManager handleUpdateMABrain:message:clientName:]_block_invoke.1932
- __60-[ControlManager removeAssetDir:assetType:clientName:using:]_block_invoke.1542
- __66-[ControlManager moveAssetIntoRepo:forType:forAsset:cleanUp:with:]_block_invoke.1897
- __69-[MADAutoAssetControlManager action_LoadPersistedResumeLocker:error:]_block_invoke.2323
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke.2520
- __71-[MADAutoAssetControlManager action_IssueClientReplyJobResponse:error:]_block_invoke_2.2521
- ___34-[DownloadManager MACopyDawToken:]_block_invoke
- ___42-[MobileAssetHealthReport scheduleReport:]_block_invoke
- ___45-[MobileAssetHealthReport setLastRerpotDate:]_block_invoke
- ___51-[MobileAssetHealthReport initWithInterval:leeway:]_block_invoke
- ___55-[DownloadManager downloadNeedsSSO:taskDescriptor:url:]_block_invoke
- ___64-[DownloadManager decryptContentEncryptedAssetAtPathIfRequired:]_block_invoke
- __block_literal_global.1079
- __block_literal_global.1277
- __block_literal_global.1279
- __block_literal_global.1284
- __block_literal_global.1355
- __block_literal_global.1377
- __block_literal_global.2048
- __block_literal_global.2070
- __block_literal_global.2231
- __block_literal_global.2240
- __block_literal_global.2242
- __block_literal_global.2253
- __block_literal_global.2261
- __block_literal_global.2269
- __block_literal_global.2277
- __block_literal_global.2285
- __block_literal_global.2293
- __block_literal_global.2301
- __block_literal_global.2309
- __block_literal_global.2336
- __block_literal_global.2338
- __block_literal_global.2366
- __block_literal_global.2368
- __block_literal_global.2383
- _objc_msgSend$_initializePeriodicHealthReport
- _objc_msgSend$authPallasBAACertManager
- _objc_msgSend$authPallasSessionDelegate
- _objc_msgSend$getLastReportDate
- _objc_msgSend$initWithInterval:leeway:
- _objc_msgSend$operationQueue
- _objc_msgSend$recordOperation:toHistoryType:fromLayer:fromClient:
- _objc_msgSend$reportCadance
- _objc_msgSend$reportLeeway
- _objc_msgSend$reportTimer
- _objc_msgSend$scheduleReport:
- _objc_msgSend$setAuthPallasBAACertManager:
- _objc_msgSend$setAuthPallasSession:
- _objc_msgSend$setAuthPallasSessionDelegate:
- _objc_msgSend$setCertArray:
- _objc_msgSend$setLastRerpotDate:
- _objc_msgSend$setMaxConcurrentOperationCount:
- _objc_msgSend$setRefKey:
- _objc_msgSend$setReportTimer:
- _objc_msgSend$splunkOperationQueue
- decryptContentEncryptedAssetAtPathIfRequired:.keyManager
- decryptContentEncryptedAssetAtPathIfRequired:.keyManagerDispatchOnce
- downloadNeedsSSO:taskDescriptor:url:.keyManager
- downloadNeedsSSO:taskDescriptor:url:.keyManagerDispatchOnce
CStrings:
+ "\x17\x14I"
+ "\x1f\x02\x1b"
+ "%@:isAnyAvailableForStagingByGroup"
+ "0.0.0.0.0,0"
+ "2.5.0"
+ "@\"MobileAssetKeyManager\""
+ "@56@0:8@16@24@32@40^@48"
+ "AutoAssetStagerFilesystemMaxMegabytes"
+ "AutoAssetStagerInjectAvailableDups"
+ "AutoAssetStagerInjectAvailableOlderVersions"
+ "DETERMINED"
+ "DETERMINE_DONE             "
+ "DETERMINE_DROPPED          "
+ "DownloadSession"
+ "PallasSession"
+ "Starting built-in MobileAsset brain built Apr 13 2025 23:56:00"
+ "Starting downloaded MobileAsset brain (version: %@) built Apr 13 2025 23:56:00"
+ "T@\"MABAACertManager\",R,&,N,V_baaCertManager"
+ "T@\"MAKeyManagerDownloadSessionDelegate\",&,N,V_pallasDelegate"
+ "T@\"MAKeyManagerDownloadSessionDelegate\",R,&,N,V_keyManagerDelegate"
+ "T@\"MobileAssetKeyManager\",&,N,V_keyManager"
+ "T@\"NSArray\",C,V_certArray"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_underlyingQueue"
+ "T@\"NSOperationQueue\",R,&,N"
+ "T@\"NSOperationQueue\",R,N,V_operationQueue"
+ "T@\"NSOperationQueue\",R,N,V_splunkOperationQueue"
+ "T@,&,V_refKey"
+ "TB,N,V_preferenceStagerInjectAvailableDups"
+ "TB,N,V_preferenceStagerInjectAvailableOlderVersions"
+ "Tq,N,V_preferenceMaxStagerFilesystemMegabytes"
+ "Will not prompt user for AppleConnect token for key retrieval due to override on downloadOptions"
+ "[%@](%@) {%@} %@"
+ "[%@](%@) {%@} total size on-disk after extraction too large | availableForStaging:%ld | totalFilesystemBytes:%llu | maxFilesystemBytes:%llu"
+ "[AuthenticatedPallas]: Pallas server(%{public}@) %{public}s authentication"
+ "[BackgroundTaskOverride]: Configuring download for task:%{public}@ overriding Cellular"
+ "[BackgroundTaskOverride]: Configuring download for task:%{public}@ overriding Constrained"
+ "[BackgroundTaskOverride]: Configuring download for task:%{public}@ overriding Expensive"
+ "[BackgroundTaskOverride]: Configuring download for task:%{public}@ overriding:%{public}@"
+ "[BackgroundTaskOverride]: Download already started for task:%{public}@ overriding Cellular:%{public}@ Expensive:%{public}@ Constrained:%{public}@"
+ "[BackgroundTaskOverride]: Download already started for task:%{public}@. Overriding of download properties not supported for in process downloads"
+ "[BackgroundTaskOverride]: Failed to set backgroundTaskOverride for task:%{public}@ ExceptionName:%{public}@ ExceptionReason:%{public}@"
+ "[BackgroundTaskOverride]: Failed to set backgroundTaskOverrides for task:%{public}@ ExceptionName:%{public}@ ExceptionReason:%{public}@"
+ "[BackgroundTaskOverride]: Overriding of parameters not supported for in process downloads. Skipping"
+ "[BaseURLOverride]: inBoxUpdateMode check is not supported for this device type"
+ "[BaseURLOverride]: inBoxUpdateMode check supported for this device type"
+ "[MAKeyManagerDownloadSessionDelegate]: Disabling mTLS - no certificates available"
+ "[MobileAssetHealthReport] Report %@ submitted to CoreAnalytics"
+ "[MobileAssetHealthReport] Report %@ submitted to Splunk"
+ "[MobileAssetHealthReport]: Unknown XPC activity state (%ld) for activity %s"
+ "[MobileAssetHealthReport]: Use existing criteria: %@"
+ "[MobileAssetHealthReport]: Use new criteria: %@"
+ "[MobileAssetHealthReport]: XPC activity %s is checking in"
+ "[MobileAssetHealthReport]: XPC activity %s is running"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@0:8^@16"
+ "__KnoxMTLS"
+ "_baaCertManager"
+ "_keyManager"
+ "_keyManagerDelegate"
+ "_pallasDelegate"
+ "_preferenceMaxStagerFilesystemMegabytes"
+ "_preferenceStagerInjectAvailableDups"
+ "_preferenceStagerInjectAvailableOlderVersions"
+ "_underlyingQueue"
+ "baaCertManager"
+ "com.apple.mobileassetd.health-report"
+ "considerInjectionIntoAvailableForStaging"
+ "copyKeyAndBAACerificateChain:"
+ "copyKeyAndSelfSignedCertificateChain:"
+ "corrupted descriptor (key:%@)"
+ "dedupAvailableForStaging:dedupingAssetDescriptors:ofContainerName:"
+ "device out-of-memory"
+ "does *NOT* require"
+ "dropped all available-for-staging | %@"
+ "finalized available-for-staging | beganFromCount:%ld | duplicateCount:%ld | multipleCount:%ld | notComparableCount:%ld | availableForStaging:%ld | totalFilesystemBytes:%llu"
+ "gdmf.apple.com"
+ "iPad"
+ "initForAssetType:fromMetadata:fromBaseDescriptor:substitutingAssetVersion:invalidReasons:"
+ "initWithName:certType:"
+ "keyManager"
+ "keyManagerDelegate"
+ "lowercaseString"
+ "nothing in trimmed-available-for-staging"
+ "pallasDelegate"
+ "preferenceMaxStagerFilesystemMegabytes"
+ "preferenceStagerInjectAvailableDups"
+ "preferenceStagerInjectAvailableOlderVersions"
+ "reason"
+ "recordOperation:toHistoryType:fromLayer:forTargetOSVersion:forTargetBuildVersion:withAddendumMessage:"
+ "refreshBAACertificate"
+ "requires"
+ "scheduleReport"
+ "setKeyManager:"
+ "setLastReportDate:"
+ "setPallasDelegate:"
+ "setPreferenceMaxStagerFilesystemMegabytes:"
+ "setPreferenceStagerInjectAvailableDups:"
+ "setPreferenceStagerInjectAvailableOlderVersions:"
+ "setUnderlyingQueue:"
+ "underlyingQueue"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] asset-descriptor array validated | availableSummary:%{public}@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] asset-versions not comparable (filtered latest encountered) | droppedDescriptor:%{public}@ | keptDescriptor:%{public}@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] dropped all assets that had been considered as available-for-staging | droppedAllReason:%{public}@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] duplicate descriptor (filtered) | nextAvailableDescriptor:%{public}@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] multiple asset-versions (filtered older) | olderDescriptor:%{public}@ | newerDescriptor:%{public}@"
+ "{%{public}@}\n[%{public}@](%{public}@) [DEDUP-AVAILABLE-FOR-STAGING] potential total byte count issue | totalFilesystemBytes:%llu | miscountedFilesystemBytes:%llu"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] failed set-job that was converted to success (already latest-to-vend) | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] failed set-job that was converted to success (have latest-to-vend) | setConfiguration:%{public}@"
+ "{%{public}@}\n[SET-STATUS-ERROR-CHANGE] failed set-job that was converted to success (matches latest-to-vend) | setConfiguration:%{public}@"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] discrepancy detected while building test available-for-staging array-with-duplicates | nextFromOriginal:%{public}@ | originalAvailableForStaging:%ld | againAvailableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] discrepancy detected while building test available-for-staging array-with-older | nextFromOriginal:%{public}@ | originalAvailableForStaging:%ld | olderAvailableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] empty again-available-for-staging while building test available-for-staging array-with-duplicates | nextFromOriginal:%{public}@ | originalAvailableForStaging:%ld | againAvailableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] empty again-available-for-staging while building test available-for-staging array-with-older | nextFromOriginal:%{public}@ | originalAvailableForStaging:%ld | olderAvailableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] injected available-for-staging array-with-duplicates | availableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] injected available-for-staging array-with-older | availableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] nil nextDescriptor while building test available-for-staging array-with-duplicates | nextFromOriginal:%{public}@ | originalAvailableForStaging:%ld | againAvailableForStaging:%ld"
+ "{considerInjectionIntoAvailableForStaging} [DEDUP-AVAILABLE-FOR-STAGING] nil nextDescriptor while building test available-for-staging array-with-older | nextFromOriginal:%{public}@ | originalAvailableForStaging:%ld | olderAvailableForStaging:%ld"
+ "\x7f\x0f\x03\x11\x1f\b\x11BRh"
- "\x1f\x01\x1d"
- "%"
- "%@%@Queue"
- "%{public}@ user for AppleConnect token for key retrieval due to override on downloadOptions"
- "'\x14I"
- "2.4.3"
- "@32@0:8d16d24"
- "AuthPallasSession"
- "Configuring download for task:%{public}@ overriding Cellular"
- "Configuring download for task:%{public}@ overriding Constrained"
- "Configuring download for task:%{public}@ overriding Expensive"
- "Configuring download for task:%{public}@ overriding:%{public}@"
- "Download already started for task:%{public}@ overriding Cellular:%{public}@ Expensive:%{public}@ Constrained:%{public}@"
- "HealthReportIntervalSec"
- "HealthReportLeewaySec"
- "Knox lookup for decryption key %{public}@"
- "Starting built-in MobileAsset brain built Apr  7 2025 02:53:10"
- "Starting downloaded MobileAsset brain (version: %@) built Apr  7 2025 02:53:10"
- "T@\"MABAACertManager\",&,N,V_authPallasBAACertManager"
- "T@\"MAKeyManagerDownloadSessionDelegate\",&,N,V_authPallasSessionDelegate"
- "T@\"NSArray\",&,N,V_certArray"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_reportTimer"
- "T@\"NSOperationQueue\",&,N,V_operationQueue"
- "T@\"NSOperationQueue\",&,N,V_splunkOperationQueue"
- "T@\"NSURLSession\",&,N,V_authPallasSession"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_refKey"
- "Td,V_reportCadance"
- "Td,V_reportLeeway"
- "Using internal server trust for %{public}@"
- "Will not prompt"
- "Will prompt(if required)"
- "[AuthenticatedPallas]: Pallas server(%{public}@) does *NOT* require authentication"
- "[AuthenticatedPallas]: Pallas server(%{public}@) requires authentication"
- "[MobileAssetHealthReport]: Reporting interval is %lf seconds (leeway = %lf seconds)"
- "[MobileAssetHealthReport]: scheduleReport: Canceling previously scheduled report"
- "[MobileAssetHealthReport]: scheduleReport: LastReportDate: [%{public}@]"
- "[MobileAssetHealthReport]: scheduleReport: Next report delay: %lf seconds"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
- "_authPallasBAACertManager"
- "_authPallasSession"
- "_authPallasSessionDelegate"
- "_initializePeriodicHealthReport"
- "_reportCadance"
- "_reportLeeway"
- "_reportTimer"
- "authPallasBAACertManager"
- "authPallasSession"
- "authPallasSessionDelegate"
- "https://gdmf.apple.com/assets"
- "initWithInterval:leeway:"
- "o\x0f\x03\x11\x1f\b\x112Rh"
- "reportCadance"
- "reportLeeway"
- "reportTimer"
- "scheduleReport:"
- "setAuthPallasBAACertManager:"
- "setAuthPallasSession:"
- "setAuthPallasSessionDelegate:"
- "setLastRerpotDate:"
- "setMaxConcurrentOperationCount:"
- "setOperationQueue:"
- "setReportCadance:"
- "setReportLeeway:"
- "setReportTimer:"
- "setSplunkOperationQueue:"
- "v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"

```
