## MobileAssetDaemon

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/MobileAssetDaemon`

```diff

-1837.100.235.0.0
-  __TEXT.__text: 0x28acc4
+1837.100.250.0.0
+  __TEXT.__text: 0x28c874
   __TEXT.__auth_stubs: 0x21d0
-  __TEXT.__objc_methlist: 0x1289c
+  __TEXT.__objc_methlist: 0x128bc
   __TEXT.__const: 0x187a
-  __TEXT.__cstring: 0x3e6df
-  __TEXT.__oslogstring: 0x5bce6
-  __TEXT.__gcc_except_tab: 0xe76c
+  __TEXT.__cstring: 0x3e9dd
+  __TEXT.__oslogstring: 0x5c476
+  __TEXT.__gcc_except_tab: 0xe8cc
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xf0
   __TEXT.__swift5_typeref: 0x146

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__unwind_info: 0x5520
+  __TEXT.__unwind_info: 0x5580
   __TEXT.__eh_frame: 0x90
   __TEXT.__objc_classname: 0x116e
-  __TEXT.__objc_methname: 0x46de9
-  __TEXT.__objc_methtype: 0x47f4
-  __TEXT.__objc_stubs: 0x27080
+  __TEXT.__objc_methname: 0x46e26
+  __TEXT.__objc_methtype: 0x4814
+  __TEXT.__objc_stubs: 0x270c0
   __DATA_CONST.__got: 0xff8
-  __DATA_CONST.__const: 0x30c8
+  __DATA_CONST.__const: 0x3230
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xacd8
+  __DATA_CONST.__objc_selrefs: 0xace8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x350
   __DATA_CONST.__objc_arraydata: 0xd50
   __AUTH_CONST.__auth_got: 0x10f8
   __AUTH_CONST.__const: 0xec0
-  __AUTH_CONST.__cfstring: 0x31b20
+  __AUTH_CONST.__cfstring: 0x31e80
   __AUTH_CONST.__objc_const: 0x187a8
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__objc_intobj: 0x1368
+  __AUTH_CONST.__objc_intobj: 0x13b0
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH.__objc_data: 0x2c98
   __AUTH.__data: 0xe8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: B876C17A-9B07-3685-B4C2-D3332B9D3B1F
-  Functions: 7173
-  Symbols:   24017
-  CStrings:  25912
+  UUID: F6339121-12A7-31FE-9542-A13DAACC2EF0
+  Functions: 7187
+  Symbols:   24064
+  CStrings:  25986
 
Symbols:
+ -[ControlManager isClientCallSynchronous:]
+ -[DownloadInfo clientCallbackQueue]
+ -[DownloadInfo dealloc]
+ -[DownloadInfo queuePostServiceTaskIdentifierSetOperation:]
+ -[DownloadInfo serviceTaskIdentifierSetCompletions]
+ -[DownloadInfo setClientCallbackQueue:]
+ -[DownloadInfo setServiceTaskIdentifierSetCompletions:]
+ -[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]
+ -[MADAutoAssetControlManager newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:forceSetLookupResult:notifyClients:forCreationReason:recordingHistoryOperation:]
+ -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:ignoreCurrentSetConfiguration:]
+ -[MADAutoAssetStager logAlreadyDownloadedByAssetType:]
+ -[MADAutoAssetStager splitOutAvailableForStagingByGroup:forGroupDetermine:limitingToRequired:]
+ -[MADownloadServiceClient pendingRequests]
+ -[MADownloadServiceClient performOperations:]
+ -[MADownloadServiceClient performOperations:].cold.1
+ -[MADownloadServiceClient performOperations:].cold.2
+ -[MADownloadServiceClient performOperations:].cold.3
+ -[MADownloadServiceClient setPendingRequests:]
+ GCC_except_table174
+ GCC_except_table574
+ GCC_except_table613
+ GCC_except_table615
+ GCC_except_table621
+ GCC_except_table636
+ GCC_except_table665
+ GCC_except_table795
+ GCC_except_table801
+ _OBJC_IVAR_$_DownloadInfo._clientCallbackQueue
+ _OBJC_IVAR_$_DownloadInfo._serviceTaskIdentifierSetCompletions
+ _OBJC_IVAR_$_MADownloadServiceClient._pendingRequests
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1916
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1917
+ ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke_2.1918
+ ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2071
+ ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke.1899
+ ___121-[DownloadManager configAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:usingDownloadOptions:forAutoAssetName:]_block_invoke_2
+ ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2202
+ ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.1915
+ ___157-[DownloadManager configAssetDownload:withPurpose:matchingAssetId:usingDownloadConfig:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke_2
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2134
+ ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2139
+ ___23-[DownloadInfo dealloc]_block_invoke
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2167
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2174
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2176
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2176.cold.1
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2192
+ ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke_2.2193
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1920
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1921
+ ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke_2.1922
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2078
+ ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2079
+ ___49-[DownloadInfo setDownloadServiceTaskIdentifier:]_block_invoke
+ ___49-[MADownloadServiceClient syncUpStateWithService]_block_invoke.636
+ ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1994
+ ___55-[MADownloadServiceClient cancelDownloadForTask:error:]_block_invoke.597
+ ___55-[MADownloadServiceClient getAllDownloadingTasksAsync:]_block_invoke.577
+ ___59-[DownloadInfo queuePostServiceTaskIdentifierSetOperation:]_block_invoke
+ ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.608
+ ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.609
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2061
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2062
+ ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2067
+ ___68-[MADownloadServiceClient startDownloadWithParameters:replyingWith:]_block_invoke.589
+ ___70-[MADownloadServiceClient updateDownloadOptionsForTask:options:error:]_block_invoke.616
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3529
+ ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3530
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1924
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke.1925
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2
+ ___97-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:]_block_invoke_2.1926
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96w_e8_v12?0B8lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88s96s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r112l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104s112w_e8_v12?0B8lw112l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104s112s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e8_v12?0B8lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e8_v12?0B8lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.2169
+ ___block_literal_global.2181
+ ___block_literal_global.2590
+ ___block_literal_global.4180
+ ___block_literal_global.5457
+ _objc_msgSend$_seaShipAudienceOverride
+ _objc_msgSend$cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:
+ _objc_msgSend$clientCallbackQueue
+ _objc_msgSend$isClientCallSynchronous:
+ _objc_msgSend$logAlreadyDownloadedByAssetType:
+ _objc_msgSend$newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:forceSetLookupResult:notifyClients:forCreationReason:recordingHistoryOperation:
+ _objc_msgSend$pendingRequests
+ _objc_msgSend$performOperations:
+ _objc_msgSend$queuePostServiceTaskIdentifierSetOperation:
+ _objc_msgSend$serviceTaskIdentifierSetCompletions
+ _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:ignoreCurrentSetConfiguration:
+ _objc_msgSend$splitOutAvailableForStagingByGroup:forGroupDetermine:limitingToRequired:
- +[MADAutoAssetLocker newCurrentSetLockUsageForDescriptor:]
- -[DownloadManager cancelDownloadTaskForDescriptorWithResponse:replyingWith:]
- -[MADAutoAssetControlManager newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:]
- -[MADAutoAssetControlManager setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:]
- -[MADAutoAssetControlManager setDescriptorLocked:]
- -[MADAutoAssetStager splitOutAvailableForStagingByGroup:forGroupDetermine:]
- -[MADownloadServiceClient pendingCancelDownloadRequests]
- -[MADownloadServiceClient pendingGetDownloadingTasksRequests]
- -[MADownloadServiceClient pendingStartDownloadRequests]
- -[MADownloadServiceClient serviceInitializationCompleted:error:].cold.1
- -[MADownloadServiceClient serviceInitializationCompleted:error:].cold.2
- -[MADownloadServiceClient serviceInitializationCompleted:error:].cold.3
- -[MADownloadServiceClient setPendingCancelDownloadRequests:]
- -[MADownloadServiceClient setPendingGetDownloadingTasksRequests:]
- -[MADownloadServiceClient setPendingStartDownloadRequests:]
- GCC_except_table576
- GCC_except_table614
- GCC_except_table616
- GCC_except_table622
- GCC_except_table637
- GCC_except_table666
- GCC_except_table799
- GCC_except_table802
- _OBJC_IVAR_$_MADownloadServiceClient._pendingCancelDownloadRequests
- _OBJC_IVAR_$_MADownloadServiceClient._pendingGetDownloadingTasksRequests
- _OBJC_IVAR_$_MADownloadServiceClient._pendingStartDownloadRequests
- ___100-[DownloadManager cancelAssetDownloadJob:forAssetType:withPurpose:matchingAssetId:forAutoAssetName:]_block_invoke.1914
- ___116-[DownloadManager cancelAllDownloading:withPurpose:includingAssets:includingCatalog:includingOther:clientName:then:]_block_invoke.2063
- ___149-[DownloadManager registerCatalogDownloadJob:withPurpose:usingDownloadOptions:usingXPCConnection:withXPCMessage:performingAutoAssetJob:asClientName:]_block_invoke.2194
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2123
- ___211-[DownloadManager startDownloadAndUpdateState:taskDescriptor:startingAt:withLength:extractWith:modified:options:downloadSize:using:with:clientName:autoAssetJob:ofJobType:notify:spaceCheckedUUID:catalogMetadata:]_block_invoke.2126
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2159
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2166
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2168
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2168.cold.1
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke.2184
- ___314-[DownloadManager registerAssetDownloadJob:withPurpose:usingDownloadOptions:forAssetId:withBase:relativeTo:startingAt:withLength:extractWith:allocateExtractorIfNecessary:usingXPCConnection:withXPCMessage:clientName:performingAutoAssetJob:notify:withCatalogMetadata:withSpaceCheckedUUID:retryCount:skipBrainUpdate:]_block_invoke_2.2185
- ___43-[DownloadManager cancelAssetDownloadTask:]_block_invoke.1916
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2070
- ___47-[DownloadManager getCurrentInflightDownloads:]_block_invoke.2071
- ___49-[MADownloadServiceClient syncUpStateWithService]_block_invoke.630
- ___52-[DownloadManager reportDownloadAttemptResult:with:]_block_invoke.1986
- ___55-[MADownloadServiceClient cancelDownloadForTask:error:]_block_invoke.591
- ___55-[MADownloadServiceClient getAllDownloadingTasksAsync:]_block_invoke.569
- ___58+[MADAutoAssetLocker newCurrentSetLockUsageForDescriptor:]_block_invoke
- ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.600
- ___63-[MADownloadServiceClient cancelDownloadForTaskAsync:callback:]_block_invoke.601
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2053
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2054
- ___65-[DownloadManager queryNSUrlSessiondAndUpdateState:fromLocation:]_block_invoke.2059
- ___68-[MADownloadServiceClient startDownloadWithParameters:replyingWith:]_block_invoke.583
- ___70-[MADownloadServiceClient updateDownloadOptionsForTask:options:error:]_block_invoke.608
- ___76-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:replyingWith:]_block_invoke
- ___76-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:replyingWith:]_block_invoke.1918
- ___76-[DownloadManager cancelDownloadTaskForDescriptorWithResponse:replyingWith:]_block_invoke_2
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke.3457
- ___94-[MADAutoAssetControlManager handleClientLockContent:forAutoJob:instance:desire:fromLocation:]_block_invoke_2.3458
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8s72l8s80l8
- ___block_literal_global.2161
- ___block_literal_global.2173
- ___block_literal_global.2582
- ___block_literal_global.4108
- ___block_literal_global.5379
- _objc_msgSend$autoAssetJobIsReadyForAssetDownloads
- _objc_msgSend$cancelDownloadTaskForDescriptorWithResponse:replyingWith:
- _objc_msgSend$newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:
- _objc_msgSend$newCurrentSetLockUsageForDescriptor:
- _objc_msgSend$pendingCancelDownloadRequests
- _objc_msgSend$pendingGetDownloadingTasksRequests
- _objc_msgSend$pendingStartDownloadRequests
- _objc_msgSend$setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:
- _objc_msgSend$setDescriptorLocked:
- _objc_msgSend$splitOutAvailableForStagingByGroup:forGroupDetermine:
CStrings:
+ "!overallInvolvedScheduler|"
+ "!schedulerInvolved(!potentialNetworkFailure)|"
+ "!schedulerInvolved(potentialNetworkFailure)|"
+ "!schedulerInvolved|"
+ "%{public}@ | {%{public}@} stager-job triggered to reply to client-request jobs but stager-jobs never merge with client-triggered jobs so no replies issued"
+ "/Library/Caches/com.apple.xbs/48EAEDF8-59A7-4D48-A3BB-289259413B01/TemporaryDirectory.jjNipy/Sources/MobileAssetDaemon/ControlManager.m"
+ "2.5.5"
+ "@32@0:8@16B24B28"
+ "ANOMALY(missing asset-selector)|"
+ "ANOMALY-AUTO-CONTROL-MANAGER-STARTUP"
+ "ANOMALY:not tracked by UUID or by selector|"
+ "Invalid callback passed to add to post serviceTaskIdentifier set operations | %{public}@"
+ "Loaded built-in MobileAssetDaemon_Framework Feb 16 2026 02:16:24"
+ "RequestType"
+ "T@\"NSMutableArray\",&,N,V_serviceTaskIdentifierSetCompletions"
+ "T@\"NSMutableArray\",&,V_pendingRequests"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_clientCallbackQueue"
+ "[ConfigAssetDownloadJob]: Not reissuing config request(task no longer valid) | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[ConfigAssetDownloadJob]: Queueing up update config request for task | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[ConfigAssetDownloadJob]: Reissuing update config request for task | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[ConfigAssetDownloadJob]: ServiceTaskIdentifier is now set. Reissuing config download request"
+ "[ConfigAssetDownloadJob]: Task object is no longer valid. Not reissuing config download request | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[ConfigAssetDownloadJob]: Updating config for task | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[ConfigAssetDownload]: No serviceTaskIdentifier currently set for task. Queueing up task for async request | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "[ConfigAssetDownload]: Returning error for sync request(downloadServiceTaskIdentifier not yet set) | TaskDescriptor:%{public}@ | autoAssetJobID:%{public}@"
+ "[ServiceConnect]: Failed to getTasksInFlight in initializationCompleted handler | Error:%{public}@"
+ "[ServiceConnect]: Handling pending cancelDownload request | ServiceTaskIdentifier:%{public}@"
+ "[ServiceConnect]: Handling pending startDownload request | TaskDescriptor:%{public}@"
+ "[ServiceConnect]: Handling pending tasksInFlight request"
+ "[ServiceConnect]: Service initialization completed | Ready: %{public}@ | Error: %{public}@"
+ "[ServiceConnect]: Skip handling of unsupported pending request| Request:%{public}@"
+ "_clientCallbackQueue"
+ "_pendingRequests"
+ "_serviceTaskIdentifierSetCompletions"
+ "autoAssetJobUUID:%@|"
+ "autoAssetSetJob:%@|"
+ "autoJobBySelector:%@|"
+ "cancelDownloadTaskForDescriptorWithResponse:shouldQueueIfPending:replyingWith:"
+ "clientCallbackQueue"
+ "com.apple.MobileAsset.DownloadInfo.ClientCallbackQueue"
+ "eliminate(withVersionSelector) eliminatorTrackedJobUUID:%@|"
+ "eliminate(withoutVersionSelector) eliminatorTrackedJobUUID:%@|"
+ "isClientCallSynchronous:"
+ "logAlreadyDownloadedByAssetType:"
+ "more-to-do(!schedulerInvolved)|"
+ "more-to-do(schedulerInvolved)|"
+ "newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:forceSetLookupResult:notifyClients:forCreationReason:recordingHistoryOperation:"
+ "not-already(withVersionSelector):%@|"
+ "not-already(withoutVersionSelector[autoJobByUUID nil version]):%@|"
+ "not-already(withoutVersionSelector[autoJobByUUID with version]):%@|"
+ "pendingRequests"
+ "performOperations:"
+ "queuePostServiceTaskIdentifierSetOperation:"
+ "removedEliminate eliminatorTrackedJobUUID:%@|"
+ "removedEliminateJobUUID:%@|"
+ "requestType"
+ "requestTypeSync"
+ "schedulerInvolved(!potentialNetworkFailure)|"
+ "schedulerInvolved(potentialNetworkFailure)|"
+ "secondary autoJobByUUID:%@|"
+ "serviceTaskIdentifierSetCompletions"
+ "setClientCallbackQueue:"
+ "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:ignoreCurrentSetConfiguration:"
+ "setLockUsageMapForSetDescriptor invoked before setLockUsageMap available."
+ "setLookupResult:%@ | setConfiguration:%@ | discoveredAtomicEntries:%ld | forceSetLookupResult:%@"
+ "setPendingRequests:"
+ "setServiceTaskIdentifierSetCompletions:"
+ "splitOutAvailableForStagingByGroup:forGroupDetermine:limitingToRequired:"
+ "update-set-status|"
+ "v36@0:8@16B24@?28"
+ "withVersionSelector:%@|"
+ "withoutVersionSelector:%@|"
+ "{%{public}@} [%{public}@] removed auto-asset-job from tracking | removalFlow:%{public}@"
+ "{%{public}@} [DETERMINE-RESULTS] | modeName:%{public}@ | setConfiguration:%{public}@ | assetType:%{public}@ | required:%llu(%llu bytes) | optional:%llu(%llu bytes) | already:%llu(%llu bytes) | notStaging:%llu(%llu bytes)"
+ "{LoadPersistedResumeLocker} | Set LockUsageMap | initialUsageMapFromLocker:\n%{public}@"
+ "{LoadPersistedResumeLocker} | Set LockUsageMap | no current set-locks reported by auto-asset-locker"
+ "{cancelAssetDownloadJob} Not reissuing cancel request for task(task no longer valid) | taskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "{cancelAssetDownloadJob} Queueing cancel request for task | taskDescriptor:%{public}@ | autoAssetJobID:%{public}@"
+ "{cancelAssetDownloadJob}: Reissuing cancel request for task | taskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
+ "{cancelAssetDownloadTaskWithResponse} Not reissuing cancel request for task(task no longer valid) | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTaskWithResponse} ServiceTaskID not set. NOT queueing cancel | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTaskWithResponse} ServiceTaskID not set. Queueing cancel | TaskDescriptor:%{public}@"
+ "{cancelAssetDownloadTaskWithResponse}: Reissuing cancel request for task | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTask} Not reissuing cancel request for task(task no longer valid) | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTask} Queueing up cancel request for task | taskDescriptor:%{public}@"
+ "{cancelAssetDownloadTask}: Reissuing cancel request for task | taskDescriptor:%{public}@"
+ "{logAlreadyDownloadedByAssetType} assetType:%{public}@ | count:%llu | bytes:%llu"
- "%{public}@ | {%{public}@} stager-job encountering presumed stale trigger to reply on catalog download"
- "%{public}@ | {newCurrentLockUsageForSelector} no assetLock on locksBySelector for fullAssetSelector:%{public}@"
- "/Library/Caches/com.apple.xbs/C7E64D6F-42D2-4761-A27C-46E9DCB3481C/TemporaryDirectory.6qEOqG/Sources/MobileAssetDaemon/ControlManager.m"
- "2.5.4"
- "Assertion failed: (callback != nil), Callback for pendingGetDownloadingTasksRequests must always be set"
- "BUG IN MobileAsset: Assertion failed: (callback != nil), Callback for pendingGetDownloadingTasksRequests must always be set"
- "Loaded built-in MobileAssetDaemon_Framework Feb  5 2026 01:57:08"
- "T@\"NSMutableArray\",&,V_pendingCancelDownloadRequests"
- "T@\"NSMutableArray\",&,V_pendingGetDownloadingTasksRequests"
- "T@\"NSMutableArray\",&,V_pendingStartDownloadRequests"
- "[ConfigAssetDownloadJob]: Cannot update options. No serviceTaskIdentifier | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
- "[ConfigAssetDownloadJob]: Updating config for download | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
- "[ConfigAssetDownload]: Cannot update options. No serviceTaskIdentifier | TaskDescriptor:%{public}@ | autoAssetJobId:%{public}@"
- "[ServiceConnect]: Handling post-initialization getDownloadingTasksRequest"
- "[ServiceConnect]: Handling post-initialization startDownload for task | TaskDescriptor:%{public}@"
- "[ServiceConnect]: Service initialization complete callback received | Ready: %{public}@ | Error: %{public}@"
- "_pendingCancelDownloadRequests"
- "_pendingGetDownloadingTasksRequests"
- "_pendingStartDownloadRequests"
- "cancelDownloadTaskForDescriptorWithResponse:replyingWith:"
- "newAtomicInstanceAndSetDescriptor:fromSetLookupResult:vendingLatestForConfiguration:inStartup:allowEmpty:notifyClients:forCreationReason:recordingHistoryOperation:"
- "newCurrentSetLockUsageForDescriptor:"
- "pendingCancelDownloadRequests"
- "pendingGetDownloadingTasksRequests"
- "pendingStartDownloadRequests"
- "setConfigurationAdoptLatestToVend:fromSetDescriptor:toSetConfiguration:fromPreSUStaging:allowEmpty:"
- "setDescriptorLocked:"
- "setLookupResult:%@ | setConfiguration:%@ | discoveredAtomicEntries:%ld | allowEmpty:%@"
- "setPendingCancelDownloadRequests:"
- "setPendingGetDownloadingTasksRequests:"
- "setPendingStartDownloadRequests:"
- "splitOutAvailableForStagingByGroup:forGroupDetermine:"
- "unable to perform asset download since DownloadManager is not ready (awaiting sync from NSURLSession layer)"
- "{%{public}@} | Set LockUsageMap | initialUsageMapFromLocker:\n%{public}@"
- "{%{public}@} | Set LockUsageMap | no current set-locks reported by auto-asset-locker"
- "{AUTO-LOCKER:newCurrentSetLockUsageForDescriptor} | lockedSetDescriptor:%{public}@ | %ld current lock-reason%{public}@:%{public}@"
- "{AUTO-LOCKER:newCurrentSetLockUsageForDescriptor} | lockedSetDescriptor:%{public}@ | no current lock-reasons"
- "{AUTO-LOCKER:newCurrentSetLockUsageForDescriptor} | no auto-asset-locker"
- "{cancelAssetDownloadJob} Asked to cancel non existent job(possibly not started) | taskDescriptor:%{public}@"
- "{cancelAssetDownloadTask} Asked to cancel non existent task(possibly not started) | taskDescriptor:%{public}@"

```
