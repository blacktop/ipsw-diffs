## deleted

> `/System/Library/PrivateFrameworks/CacheDelete.framework/deleted`

```diff

-819.120.2.0.0
-  __TEXT.__text: 0x46d34
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__objc_stubs: 0x5120
-  __TEXT.__objc_methlist: 0x24f4
-  __TEXT.__const: 0x178
-  __TEXT.__gcc_except_tab: 0x2090
-  __TEXT.__objc_methname: 0x5bc3
-  __TEXT.__cstring: 0x3408
-  __TEXT.__oslogstring: 0x62f4
-  __TEXT.__objc_classname: 0x392
-  __TEXT.__objc_methtype: 0xcd0
-  __TEXT.__unwind_info: 0xc90
-  __DATA_CONST.__auth_got: 0x730
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x18e0
-  __DATA_CONST.__cfstring: 0x31e0
-  __DATA_CONST.__objc_classlist: 0xf0
+901.0.0.0.1
+  __TEXT.__text: 0x5a154
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_stubs: 0x6780
+  __TEXT.__objc_methlist: 0x2f24
+  __TEXT.__const: 0x190
+  __TEXT.__gcc_except_tab: 0x28f8
+  __TEXT.__cstring: 0x48b5
+  __TEXT.__objc_methname: 0x7c09
+  __TEXT.__oslogstring: 0xab17
+  __TEXT.__objc_classname: 0x3f1
+  __TEXT.__objc_methtype: 0xe73
+  __TEXT.__unwind_info: 0xde8
+  __DATA_CONST.__const: 0x1ce8
+  __DATA_CONST.__cfstring: 0x4ac0
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__objc_intobj: 0x120
-  __DATA_CONST.__objc_arraydata: 0x2e8
-  __DATA_CONST.__objc_dictobj: 0x280
-  __DATA_CONST.__objc_arrayobj: 0x198
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0x568
+  __DATA_CONST.__objc_arrayobj: 0x1c8
+  __DATA_CONST.__objc_intobj: 0x1e0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA.__objc_const: 0x3868
-  __DATA.__objc_selrefs: 0x1860
-  __DATA.__objc_ivar: 0x280
-  __DATA.__objc_data: 0x960
+  __DATA_CONST.__objc_dictobj: 0x320
+  __DATA_CONST.__auth_got: 0x7a0
+  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x48a8
+  __DATA.__objc_selrefs: 0x1e90
+  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_data: 0xb40
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x1a0
+  __DATA.__common: 0x1
+  __DATA.__bss: 0x1f8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 79FDB005-CEE1-3E06-BBCF-1D6C5F406432
-  Functions: 956
-  Symbols:   2567
-  CStrings:  2734
+  UUID: 7B26A2FF-69DA-37C2-B59E-65F29703F8E4
+  Functions: 1222
+  Symbols:   3156
+  CStrings:  3770
 
Symbols:
+ +[AppContainerCaches deleteAppCaches:urgency:telemetry:group:]
+ +[AppContainerCaches deleteAppCaches:urgency:telemetry:group:fairPurgeMode:]
+ +[CDAppClassifier loadAndClassifyDataWithCompletion:]
+ +[CDAppClassifier loadAndClassifyData]
+ +[CDAppClassifier sharedClassifier]
+ +[CDFairPurgeState sharedState]
+ +[CDPurgeableAppInfo supportsSecureCoding]
+ +[CacheDeleteFairPurgeOperation criticalSystemPluginExemptions]
+ +[CacheDeleteFairPurgeOperation isServiceIDExempted:]
+ -[AppContainerCaches _serviceCancelPurgeImmediate:]
+ -[CDAppClassifier .cxx_destruct]
+ -[CDAppClassifier _loadHardcodedPluginMappingData]
+ -[CDAppClassifier _loadPlistPluginMappingData]
+ -[CDAppClassifier _updateWithMappingData:]
+ -[CDAppClassifier allHiddenAppBundleIDs]
+ -[CDAppClassifier allVisibleAppBundleIDs]
+ -[CDAppClassifier appBundleIDForPlugin:]
+ -[CDAppClassifier appsData]
+ -[CDAppClassifier buildAppInfoForBundleIDs:]
+ -[CDAppClassifier bundleToPluginsMap]
+ -[CDAppClassifier classifierQueue]
+ -[CDAppClassifier dirStatIDToBundleMap]
+ -[CDAppClassifier hiddenAppsData]
+ -[CDAppClassifier init]
+ -[CDAppClassifier internalHiddenAppBundleIDs]
+ -[CDAppClassifier internalVisibleAppBundleIDs]
+ -[CDAppClassifier isVisibleApp:]
+ -[CDAppClassifier pluginToBundleMap]
+ -[CDAppClassifier pluginsForApp:]
+ -[CDAppClassifier setAppsData:]
+ -[CDAppClassifier setBundleToPluginsMap:]
+ -[CDAppClassifier setClassifierQueue:]
+ -[CDAppClassifier setHiddenAppsData:]
+ -[CDAppClassifier setInternalHiddenAppBundleIDs:]
+ -[CDAppClassifier setInternalVisibleAppBundleIDs:]
+ -[CDAppClassifier setPluginToBundleMap:]
+ -[CDAppClassifier setTagHashToBundleID:]
+ -[CDAppClassifier setTimestamp:]
+ -[CDAppClassifier setVersion:]
+ -[CDAppClassifier tagHashToBundleID]
+ -[CDAppClassifier timestamp]
+ -[CDAppClassifier version]
+ -[CDFairPurgeOperationResult .cxx_destruct]
+ -[CDFairPurgeOperationResult appTelemetryData]
+ -[CDFairPurgeOperationResult completionStatus]
+ -[CDFairPurgeOperationResult executedPhase]
+ -[CDFairPurgeOperationResult initWithVolumes:requestedBytes:mainVolume:clientProcName:]
+ -[CDFairPurgeOperationResult phase1Step1EndTime]
+ -[CDFairPurgeOperationResult phase1Step1PluginsReported]
+ -[CDFairPurgeOperationResult phase1Step1StartTime]
+ -[CDFairPurgeOperationResult phase1Step2ContainersReported]
+ -[CDFairPurgeOperationResult phase1Step2EndTime]
+ -[CDFairPurgeOperationResult phase1Step2StartTime]
+ -[CDFairPurgeOperationResult phase1Step3EndTime]
+ -[CDFairPurgeOperationResult phase1Step3FSPurgeableReported]
+ -[CDFairPurgeOperationResult phase1Step3StartTime]
+ -[CDFairPurgeOperationResult phase2CacheReported]
+ -[CDFairPurgeOperationResult phase2FSPurgeableEndTime]
+ -[CDFairPurgeOperationResult phase2FSPurgeableReported]
+ -[CDFairPurgeOperationResult phase2FSPurgeableStartTime]
+ -[CDFairPurgeOperationResult phase2PluginsEndTime]
+ -[CDFairPurgeOperationResult phase2PluginsReported]
+ -[CDFairPurgeOperationResult phase2PluginsStartTime]
+ -[CDFairPurgeOperationResult safDataLoadSuccess]
+ -[CDFairPurgeOperationResult setAppTelemetryData:]
+ -[CDFairPurgeOperationResult setCompletionStatus:]
+ -[CDFairPurgeOperationResult setExecutedPhase:]
+ -[CDFairPurgeOperationResult setPhase1Step1EndTime:]
+ -[CDFairPurgeOperationResult setPhase1Step1PluginsReported:]
+ -[CDFairPurgeOperationResult setPhase1Step1StartTime:]
+ -[CDFairPurgeOperationResult setPhase1Step2ContainersReported:]
+ -[CDFairPurgeOperationResult setPhase1Step2EndTime:]
+ -[CDFairPurgeOperationResult setPhase1Step2StartTime:]
+ -[CDFairPurgeOperationResult setPhase1Step3EndTime:]
+ -[CDFairPurgeOperationResult setPhase1Step3FSPurgeableReported:]
+ -[CDFairPurgeOperationResult setPhase1Step3StartTime:]
+ -[CDFairPurgeOperationResult setPhase2CacheReported:]
+ -[CDFairPurgeOperationResult setPhase2FSPurgeableEndTime:]
+ -[CDFairPurgeOperationResult setPhase2FSPurgeableReported:]
+ -[CDFairPurgeOperationResult setPhase2FSPurgeableStartTime:]
+ -[CDFairPurgeOperationResult setPhase2PluginsEndTime:]
+ -[CDFairPurgeOperationResult setPhase2PluginsReported:]
+ -[CDFairPurgeOperationResult setPhase2PluginsStartTime:]
+ -[CDFairPurgeOperationResult setSafDataLoadSuccess:]
+ -[CDFairPurgeOperationResult setTotalHiddenAppsAnalyzed:]
+ -[CDFairPurgeOperationResult setTotalVisibleAppsAnalyzed:]
+ -[CDFairPurgeOperationResult totalHiddenAppsAnalyzed]
+ -[CDFairPurgeOperationResult totalReportedBytes]
+ -[CDFairPurgeOperationResult totalVisibleAppsAnalyzed]
+ -[CDFairPurgeState .cxx_destruct]
+ -[CDFairPurgeState currentPhase]
+ -[CDFairPurgeState init]
+ -[CDFairPurgeState isFirstPhase]
+ -[CDFairPurgeState lastRunTimestamp]
+ -[CDFairPurgeState load]
+ -[CDFairPurgeState markPhaseComplete]
+ -[CDFairPurgeState reset]
+ -[CDFairPurgeState save]
+ -[CDFairPurgeState setCurrentPhase:]
+ -[CDFairPurgeState setLastRunTimestamp:]
+ -[CDFairPurgeState setStateFileURL:]
+ -[CDFairPurgeState stateFileURL]
+ -[CDPurgeOperationResult isCriticalRelinquishPurge]
+ -[CDPurgeOperationResult setCriticalRelinquishPurge:]
+ -[CDPurgeWeightCalculator _calculateAverageLastUseTimeForEntry:recentlyUsedApps:]
+ -[CDPurgeWeightCalculator _calculateWeightForApp:alpha:recentlyUsedApps:]
+ -[CDPurgeWeightCalculator calculateWeightsForAppInfo:alpha:recentlyUsedOverride:]
+ -[CDPurgeableAppInfo .cxx_destruct]
+ -[CDPurgeableAppInfo bundlesKey]
+ -[CDPurgeableAppInfo bundles]
+ -[CDPurgeableAppInfo cachePurgedSize]
+ -[CDPurgeableAppInfo cacheSize]
+ -[CDPurgeableAppInfo dataSize]
+ -[CDPurgeableAppInfo description]
+ -[CDPurgeableAppInfo encodeWithCoder:]
+ -[CDPurgeableAppInfo fsPurgeableSize]
+ -[CDPurgeableAppInfo fsPurgedSize]
+ -[CDPurgeableAppInfo initWithBundles:dataSize:cacheSize:isVisible:]
+ -[CDPurgeableAppInfo initWithCoder:]
+ -[CDPurgeableAppInfo isVisible]
+ -[CDPurgeableAppInfo lastUseTimeInDays]
+ -[CDPurgeableAppInfo pluginServices]
+ -[CDPurgeableAppInfo pluginsPurgeableSize]
+ -[CDPurgeableAppInfo pluginsPurgedSize]
+ -[CDPurgeableAppInfo setCachePurgedSize:]
+ -[CDPurgeableAppInfo setFsPurgeableSize:]
+ -[CDPurgeableAppInfo setFsPurgedSize:]
+ -[CDPurgeableAppInfo setLastUseTimeInDays:]
+ -[CDPurgeableAppInfo setPluginsPurgeableSize:]
+ -[CDPurgeableAppInfo setPluginsPurgedSize:]
+ -[CDPurgeableAppInfo setWeight:]
+ -[CDPurgeableAppInfo weight]
+ -[CDService _serviceCancelPurgeImmediate:]
+ -[CDService serviceCancelPurgeImmediate:]
+ -[CDService setSupportsCriticalRelinquishPurge:]
+ -[CDService supportsCriticalRelinquishPurge]
+ -[CDXPCService _serviceCancelPurgeImmediate:]
+ -[CacheDelete clientPerformFairPurgeOperation:replyBlock:]
+ -[CacheDelete processFSEventsNotificationFromResult:tokenString:]
+ -[CacheDelete shouldTriggerFairPurge:]
+ -[CacheDeleteAnalytics processFairPurgeOperationResult:]
+ -[CacheDeleteAnalytics reportFairPurge:]
+ -[CacheDeleteFairPurgeOperation .cxx_destruct]
+ -[CacheDeleteFairPurgeOperation _analyzeAndSortAppsByWeight:]
+ -[CacheDeleteFairPurgeOperation _calculatePluginSizesForApps:]
+ -[CacheDeleteFairPurgeOperation _purgeCachePathForApp:]
+ -[CacheDeleteFairPurgeOperation _purgePluginsForApp:]
+ -[CacheDeleteFairPurgeOperation _purgeSpecificApplications:forVolume:purgeLimit:]
+ -[CacheDeleteFairPurgeOperation _updateFSPurgeableSizesForApps:forVolume:]
+ -[CacheDeleteFairPurgeOperation allAppInfoObjects]
+ -[CacheDeleteFairPurgeOperation allServices]
+ -[CacheDeleteFairPurgeOperation appClassifier]
+ -[CacheDeleteFairPurgeOperation beforePurgeEventID]
+ -[CacheDeleteFairPurgeOperation checkCancellationAndAbortIfNeeded:]
+ -[CacheDeleteFairPurgeOperation collectStatistics]
+ -[CacheDeleteFairPurgeOperation completeWithResultAndReport:]
+ -[CacheDeleteFairPurgeOperation executeFirstPhase:]
+ -[CacheDeleteFairPurgeOperation executeSecondPhase:]
+ -[CacheDeleteFairPurgeOperation fairPurgeResult]
+ -[CacheDeleteFairPurgeOperation forceHiddenPhase]
+ -[CacheDeleteFairPurgeOperation forceVisiblePhase]
+ -[CacheDeleteFairPurgeOperation getStatistics]
+ -[CacheDeleteFairPurgeOperation goalMet:]
+ -[CacheDeleteFairPurgeOperation initWithInfo:services:volumes:]
+ -[CacheDeleteFairPurgeOperation loadSAFDataSynchronously]
+ -[CacheDeleteFairPurgeOperation mustRescan]
+ -[CacheDeleteFairPurgeOperation parseTestParameters]
+ -[CacheDeleteFairPurgeOperation purgeNonVisibleAppContainers:completion:]
+ -[CacheDeleteFairPurgeOperation purgeNonVisibleFSPurgeable:completion:]
+ -[CacheDeleteFairPurgeOperation purgeNonVisiblePlugins:completion:]
+ -[CacheDeleteFairPurgeOperation purgeSentinel:outInode:]
+ -[CacheDeleteFairPurgeOperation purgeState]
+ -[CacheDeleteFairPurgeOperation purgedVolumeUUIDs]
+ -[CacheDeleteFairPurgeOperation recentlyUsedOverride]
+ -[CacheDeleteFairPurgeOperation remainingAmountToPurge:]
+ -[CacheDeleteFairPurgeOperation reportTelemetry]
+ -[CacheDeleteFairPurgeOperation roundRobinPurgeServices:amount:batchSize:completion:]
+ -[CacheDeleteFairPurgeOperation serializeTelemetry]
+ -[CacheDeleteFairPurgeOperation setAllAppInfoObjects:]
+ -[CacheDeleteFairPurgeOperation setAllServices:]
+ -[CacheDeleteFairPurgeOperation setAppClassifier:]
+ -[CacheDeleteFairPurgeOperation setBeforePurgeEventID:]
+ -[CacheDeleteFairPurgeOperation setCollectStatistics:]
+ -[CacheDeleteFairPurgeOperation setFairPurgeResult:]
+ -[CacheDeleteFairPurgeOperation setForceHiddenPhase:]
+ -[CacheDeleteFairPurgeOperation setForceVisiblePhase:]
+ -[CacheDeleteFairPurgeOperation setMustRescan:]
+ -[CacheDeleteFairPurgeOperation setPurgeState:]
+ -[CacheDeleteFairPurgeOperation setPurgedVolumeUUIDs:]
+ -[CacheDeleteFairPurgeOperation setRecentlyUsedOverride:]
+ -[CacheDeleteFairPurgeOperation setReportTelemetry:]
+ -[CacheDeleteFairPurgeOperation setWeightCalculator:]
+ -[CacheDeleteFairPurgeOperation startOperation:]
+ -[CacheDeleteFairPurgeOperation waitForGroup:withTimeout:operationName:]
+ -[CacheDeleteFairPurgeOperation waitForSemaphore:withTimeout:operationName:]
+ -[CacheDeleteFairPurgeOperation waitWithDeferralCheck:waitBlock:operationName:]
+ -[CacheDeleteFairPurgeOperation weightCalculator]
+ -[CacheDeletePurgeOperation cachedTokenString]
+ -[CacheDeletePurgeOperation createAndStartFSEventStreamForSentinel:path:semaphore:outRescan:]
+ -[CacheDeletePurgeOperation createFSPurgeNotificationWithEventID:volumes:mustRescan:]
+ -[CacheDeletePurgeOperation executePurgeWithFSEventsMonitoring:volume:timeout:outEventID:outMustRescan:]
+ -[CacheDeletePurgeOperation oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:signpostID:]
+ -[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:]
+ -[CacheDeletePurgeOperation setCachedTokenString:]
+ -[CacheDeletePurgeOperation setTimedOutServices:]
+ -[CacheDeletePurgeOperation timedOutServices]
+ -[CacheDeletePurgeOperation tokenString]
+ -[CacheDeletePurgeOperation tryFSPurgeBatchAllVolumes:atUrgency:signpostID:orderedServices:completion:]
+ -[CacheDeletePurgeableOperation _queryFSPurgeableBatchAllVolumes:urgency:infoCopy:refreshAll:]
+ -[PurgeStatsReporter appendBatchAndSaveStats:]
+ GCC_except_table104
+ GCC_except_table134
+ GCC_except_table145
+ GCC_except_table148
+ GCC_except_table159
+ GCC_except_table16
+ GCC_except_table19
+ GCC_except_table23
+ GCC_except_table246
+ GCC_except_table26
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table48
+ GCC_except_table51
+ GCC_except_table56
+ GCC_except_table60
+ GCC_except_table63
+ GCC_except_table71
+ GCC_except_table79
+ GCC_except_table89
+ GCC_except_table9
+ GCC_except_table95
+ OBJC_IVAR_$_CDAppClassifier._appsData
+ OBJC_IVAR_$_CDAppClassifier._bundleToPluginsMap
+ OBJC_IVAR_$_CDAppClassifier._classifierQueue
+ OBJC_IVAR_$_CDAppClassifier._hiddenAppsData
+ OBJC_IVAR_$_CDAppClassifier._internalHiddenAppBundleIDs
+ OBJC_IVAR_$_CDAppClassifier._internalVisibleAppBundleIDs
+ OBJC_IVAR_$_CDAppClassifier._pluginToBundleMap
+ OBJC_IVAR_$_CDAppClassifier._tagHashToBundleID
+ OBJC_IVAR_$_CDAppClassifier._timestamp
+ OBJC_IVAR_$_CDAppClassifier._version
+ OBJC_IVAR_$_CDFairPurgeState._currentPhase
+ OBJC_IVAR_$_CDFairPurgeState._lastRunTimestamp
+ OBJC_IVAR_$_CDFairPurgeState._stateFileURL
+ OBJC_IVAR_$_CDPurgeOperationResult._criticalRelinquishPurge
+ OBJC_IVAR_$_CDPurgeableAppInfo._bundles
+ OBJC_IVAR_$_CDPurgeableAppInfo._cachePurgedSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._cacheSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._dataSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._fsPurgeableSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._fsPurgedSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._isVisible
+ OBJC_IVAR_$_CDPurgeableAppInfo._lastUseTimeInDays
+ OBJC_IVAR_$_CDPurgeableAppInfo._pluginServices
+ OBJC_IVAR_$_CDPurgeableAppInfo._pluginsPurgeableSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._pluginsPurgedSize
+ OBJC_IVAR_$_CDPurgeableAppInfo._weight
+ OBJC_IVAR_$_CDService._supportsCriticalRelinquishPurge
+ OBJC_IVAR_$_CacheDeleteFairPurgeOperation._collectStatistics
+ OBJC_IVAR_$_CacheDeleteFairPurgeOperation._forceHiddenPhase
+ OBJC_IVAR_$_CacheDeleteFairPurgeOperation._forceVisiblePhase
+ OBJC_IVAR_$_CacheDeleteFairPurgeOperation._reportTelemetry
+ _CDGetPurgeSignpostLogHandle
+ _MergedGlobals.3
+ _NSLocalizedDescriptionKey
+ _OBJC_$_PROP_LIST_CDService.282
+ _OBJC_$_PROP_LIST_CacheDeleteOperation.241
+ _OBJC_CLASS_$_CDAppClassifier
+ _OBJC_CLASS_$_CDFairPurgeOperationResult
+ _OBJC_CLASS_$_CDFairPurgeState
+ _OBJC_CLASS_$_CDPurgeWeightCalculator
+ _OBJC_CLASS_$_CDPurgeableAppInfo
+ _OBJC_CLASS_$_CacheDeleteFairPurgeOperation
+ _OBJC_CLASS_$_NSJSONSerialization
+ _OBJC_METACLASS_$_CDAppClassifier
+ _OBJC_METACLASS_$_CDFairPurgeOperationResult
+ _OBJC_METACLASS_$_CDFairPurgeState
+ _OBJC_METACLASS_$_CDPurgeWeightCalculator
+ _OBJC_METACLASS_$_CDPurgeableAppInfo
+ _OBJC_METACLASS_$_CacheDeleteFairPurgeOperation
+ __112-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:]_block_invoke.149
+ __112-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:]_block_invoke.151
+ __112-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:]_block_invoke.154
+ __28-[CDService drainPurgeQueue]_block_invoke.64
+ __30-[CacheDelete totalAvailable:]_block_invoke.337
+ __30-[CacheDelete totalAvailable:]_block_invoke.338
+ __30-[CacheDelete totalAvailable:]_block_invoke.341
+ __30-[CacheDelete totalAvailable:]_block_invoke.344
+ __30-[CacheDelete updateFollowup:]_block_invoke.190
+ __33-[CacheDelete clientCancelPurge:]_block_invoke.586
+ __34-[CacheDelete clientSetState:key:]_block_invoke.721
+ __36-[CDXPCService doWithProxy:failure:]_block_invoke.21
+ __36-[CDXPCService doWithProxy:failure:]_block_invoke.39
+ __36-[CacheDelete applicationExtensions]_block_invoke.237
+ __36-[CacheDelete applicationExtensions]_block_invoke.245
+ __36-[CacheDelete startPersistenceTimer]_block_invoke.226
+ __37-[CacheDelete checkNotificationState]_block_invoke.192
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.379
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.381
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.382
+ __37-[CacheDelete purge:volume:callback:]_block_invoke.414
+ __37-[CacheDelete purge:volume:callback:]_block_invoke_2.383
+ __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.580
+ __39-[CacheDelete handleVFSStreamXPCEvent:]_block_invoke.211
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.134
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.136
+ __40-[CacheDelete processLowDiskVolume:key:]_block_invoke_2.135
+ __41-[CacheDelete notifyFollowup:completion:]_block_invoke.183
+ __45-[CDXPCService _serviceCancelPurgeImmediate:]_block_invoke.19
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.446
+ __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.447
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.108
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.109
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.111
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.112
+ __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.98
+ __46-[CDService servicePurgeable:info:replyBlock:]_block_invoke.67
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.433
+ __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.434
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.525
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.526
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.527
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.528
+ __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.529
+ __49-[CacheDeletePurgeableOperation _startOperation:]_block_invoke.44
+ __49-[CacheDeletePurgeableOperation _startOperation:]_block_invoke.46
+ __49-[CacheDeletePurgeableOperation _startOperation:]_block_invoke.85
+ __51-[CacheDeleteFairPurgeOperation executeFirstPhase:]_block_invoke.58
+ __51-[CacheDeleteFairPurgeOperation executeFirstPhase:]_block_invoke.68
+ __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.597
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.436
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.441
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.443
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.437
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.442
+ __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.444
+ __71-[CacheDeleteFairPurgeOperation purgeNonVisibleFSPurgeable:completion:]_block_invoke.128
+ __73-[CDDaemonPurgeableResultCache updateRecentInfoForServiceID:volume:info:]_block_invoke.58
+ __73-[CacheDeleteFairPurgeOperation purgeNonVisibleAppContainers:completion:]_block_invoke.112
+ __73-[CacheDeleteFairPurgeOperation purgeNonVisibleAppContainers:completion:]_block_invoke.120
+ __73-[CacheDeleteFairPurgeOperation purgeNonVisibleAppContainers:completion:]_block_invoke.121
+ __74-[CacheDeleteFairPurgeOperation _updateFSPurgeableSizesForApps:forVolume:]_block_invoke.314
+ __81-[CacheDeleteFairPurgeOperation _purgeSpecificApplications:forVolume:purgeLimit:]_block_invoke.323
+ __85-[CacheDeleteFairPurgeOperation roundRobinPurgeServices:amount:batchSize:completion:]_block_invoke.104
+ __85-[CacheDeleteFairPurgeOperation roundRobinPurgeServices:amount:batchSize:completion:]_block_invoke.108
+ __85-[CacheDeleteFairPurgeOperation roundRobinPurgeServices:amount:batchSize:completion:]_block_invoke.97
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.308
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.310
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.318
+ __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.322
+ __94-[CacheDeletePurgeableOperation _queryFSPurgeableBatchAllVolumes:urgency:infoCopy:refreshAll:]_block_invoke.106
+ __OBJC_$_CLASS_METHODS_CDAppClassifier
+ __OBJC_$_CLASS_METHODS_CDFairPurgeState
+ __OBJC_$_CLASS_METHODS_CDPurgeableAppInfo
+ __OBJC_$_CLASS_METHODS_CacheDeleteFairPurgeOperation
+ __OBJC_$_CLASS_PROP_LIST_CDPurgeableAppInfo
+ __OBJC_$_INSTANCE_METHODS_CDAppClassifier
+ __OBJC_$_INSTANCE_METHODS_CDFairPurgeOperationResult
+ __OBJC_$_INSTANCE_METHODS_CDFairPurgeState
+ __OBJC_$_INSTANCE_METHODS_CDPurgeWeightCalculator
+ __OBJC_$_INSTANCE_METHODS_CDPurgeableAppInfo
+ __OBJC_$_INSTANCE_METHODS_CacheDeleteFairPurgeOperation
+ __OBJC_$_INSTANCE_VARIABLES_CDAppClassifier
+ __OBJC_$_INSTANCE_VARIABLES_CDFairPurgeOperationResult
+ __OBJC_$_INSTANCE_VARIABLES_CDFairPurgeState
+ __OBJC_$_INSTANCE_VARIABLES_CDPurgeableAppInfo
+ __OBJC_$_INSTANCE_VARIABLES_CacheDeleteFairPurgeOperation
+ __OBJC_$_PROP_LIST_CDAppClassifier
+ __OBJC_$_PROP_LIST_CDFairPurgeOperationResult
+ __OBJC_$_PROP_LIST_CDFairPurgeState
+ __OBJC_$_PROP_LIST_CDPurgeableAppInfo
+ __OBJC_$_PROP_LIST_CacheDeleteFairPurgeOperation
+ __OBJC_CLASS_PROTOCOLS_$_CDPurgeableAppInfo
+ __OBJC_CLASS_RO_$_CDAppClassifier
+ __OBJC_CLASS_RO_$_CDFairPurgeOperationResult
+ __OBJC_CLASS_RO_$_CDFairPurgeState
+ __OBJC_CLASS_RO_$_CDPurgeWeightCalculator
+ __OBJC_CLASS_RO_$_CDPurgeableAppInfo
+ __OBJC_CLASS_RO_$_CacheDeleteFairPurgeOperation
+ __OBJC_METACLASS_RO_$_CDAppClassifier
+ __OBJC_METACLASS_RO_$_CDFairPurgeOperationResult
+ __OBJC_METACLASS_RO_$_CDFairPurgeState
+ __OBJC_METACLASS_RO_$_CDPurgeWeightCalculator
+ __OBJC_METACLASS_RO_$_CDPurgeableAppInfo
+ __OBJC_METACLASS_RO_$_CacheDeleteFairPurgeOperation
+ ___103-[CacheDeletePurgeOperation tryFSPurgeBatchAllVolumes:atUrgency:signpostID:orderedServices:completion:]_block_invoke
+ ___112-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:]_block_invoke
+ ___122-[CacheDeletePurgeOperation oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:signpostID:]_block_invoke
+ ___122-[CacheDeletePurgeOperation oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:signpostID:]_block_invoke_2
+ ___31+[CDFairPurgeState sharedState]_block_invoke
+ ___32-[CDAppClassifier isVisibleApp:]_block_invoke
+ ___33-[CDAppClassifier pluginsForApp:]_block_invoke
+ ___35+[CDAppClassifier sharedClassifier]_block_invoke
+ ___38-[CacheDelete shouldTriggerFairPurge:]_block_invoke
+ ___39-[CDAppClassifier dirStatIDToBundleMap]_block_invoke
+ ___39-[CDAppClassifier dirStatIDToBundleMap]_block_invoke_2
+ ___40-[CDAppClassifier allHiddenAppBundleIDs]_block_invoke
+ ___40-[CDAppClassifier appBundleIDForPlugin:]_block_invoke
+ ___40-[CacheDeleteAnalytics reportFairPurge:]_block_invoke
+ ___41-[CDAppClassifier allVisibleAppBundleIDs]_block_invoke
+ ___42-[CDAppClassifier _updateWithMappingData:]_block_invoke
+ ___44-[CDAppClassifier buildAppInfoForBundleIDs:]_block_invoke
+ ___44-[CDAppClassifier buildAppInfoForBundleIDs:]_block_invoke_2
+ ___45-[CDXPCService _serviceCancelPurgeImmediate:]_block_invoke
+ ___46-[CDAppClassifier _loadPlistPluginMappingData]_block_invoke
+ ___47-[CacheDelete _purge:volume:services:callback:]_block_invoke_2
+ ___48-[CacheDeleteFairPurgeOperation startOperation:]_block_invoke
+ ___50-[CDAppClassifier _loadHardcodedPluginMappingData]_block_invoke
+ ___51-[CacheDeleteFairPurgeOperation executeFirstPhase:]_block_invoke
+ ___52-[CacheDeleteFairPurgeOperation executeSecondPhase:]_block_invoke
+ ___53+[CDAppClassifier loadAndClassifyDataWithCompletion:]_block_invoke
+ ___53-[CacheDeleteFairPurgeOperation _purgePluginsForApp:]_block_invoke
+ ___56-[CacheDeleteAnalytics processFairPurgeOperationResult:]_block_invoke
+ ___57-[CacheDeleteFairPurgeOperation loadSAFDataSynchronously]_block_invoke
+ ___58-[CacheDelete clientPerformFairPurgeOperation:replyBlock:]_block_invoke
+ ___61-[CacheDeleteFairPurgeOperation _analyzeAndSortAppsByWeight:]_block_invoke
+ ___63+[CacheDeleteFairPurgeOperation criticalSystemPluginExemptions]_block_invoke
+ ___65-[CacheDelete processFSEventsNotificationFromResult:tokenString:]_block_invoke
+ ___67-[CacheDeleteFairPurgeOperation purgeNonVisiblePlugins:completion:]_block_invoke
+ ___71-[CacheDeleteFairPurgeOperation purgeNonVisibleFSPurgeable:completion:]_block_invoke
+ ___72-[CacheDeleteFairPurgeOperation waitForGroup:withTimeout:operationName:]_block_invoke
+ ___73-[CacheDeleteFairPurgeOperation purgeNonVisibleAppContainers:completion:]_block_invoke
+ ___74-[CacheDeleteFairPurgeOperation _updateFSPurgeableSizesForApps:forVolume:]_block_invoke
+ ___76-[CacheDeleteFairPurgeOperation waitForSemaphore:withTimeout:operationName:]_block_invoke
+ ___81-[CacheDeleteFairPurgeOperation _purgeSpecificApplications:forVolume:purgeLimit:]_block_invoke
+ ___85-[CacheDeleteFairPurgeOperation roundRobinPurgeServices:amount:batchSize:completion:]_block_invoke
+ ___93-[CacheDeletePurgeOperation createAndStartFSEventStreamForSentinel:path:semaphore:outRescan:]_block_invoke
+ ___94-[CacheDeletePurgeableOperation _queryFSPurgeableBatchAllVolumes:urgency:infoCopy:refreshAll:]_block_invoke
+ ___block_descriptor_100_e8_32s40s48s56r64r72r80r_e17_B16?0"NSArray"8lr56l8r64l8s32l8s40l8s48l8r72l8r80l8
+ ___block_descriptor_100_e8_32s40s48s56r64r72r80r_e17_v16?0"NSArray"8lr56l8r64l8r72l8s32l8s40l8r80l8s48l8
+ ___block_descriptor_100_e8_32s40s48s56s64s72s80w_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8w80l8s56l8s64l8s72l8
+ ___block_descriptor_108_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s80l8s72l8
+ ___block_descriptor_116_e8_32s40s48s56s64s72bs80r88w_e22_v16?0"NSDictionary"8lw88l8r80l8s32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_116_e8_32s40s48s56s64s72s80s88s96r104w_e37_v16?0"CDPurgeServiceRequestResult"8lw104l8s32l8s40l8s48l8s56l8s64l8s72l8r96l8s80l8s88l8
+ ___block_descriptor_132_e8_32s40s48s56s64s72s80s88s96s104w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8w104l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_32_e51_q24?0"CDPurgeableAppInfo"8"CDPurgeableAppInfo"16l
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
+ ___block_descriptor_40_e8_32s_e31_q24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32s_e8_B16?0d8ls32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e22_v16?0"NSDictionary"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e20_v20?0"NSArray"8B16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e38_v32?0"NSString"8"<CDService>"16^B24ls32l8s40l8
+ ___block_descriptor_49_e8_32s_e44_v32?0"CDPurgeServiceRequestResult"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e22_v16?0"NSDictionary"8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e22_v16?0"NSDictionary"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_56_e8_32s40s48r_e8_v16?0Q8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e22_v16?0"NSDictionary"8ls48l8r56l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56s_e20_v16?0^{__CFArray=}8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e5_Q8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_76_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e8_B12?0i8ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r72r_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80r_e8_B12?0i8ls32l8r80l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8r80l8s64l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72r80r_e8_B12?0i8lr72l8s32l8s40l8s48l8s56l8s64l8r80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88w_e37_v16?0"CDPurgeServiceRequestResult"8lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ __block_literal_global.1039
+ __block_literal_global.1046
+ __block_literal_global.1096
+ __block_literal_global.1103
+ __block_literal_global.1106
+ __block_literal_global.1109
+ __block_literal_global.1111
+ __block_literal_global.1113
+ __block_literal_global.1117
+ __block_literal_global.1123
+ __block_literal_global.1127
+ __block_literal_global.1131
+ __block_literal_global.127
+ __block_literal_global.176
+ __block_literal_global.194
+ __block_literal_global.204
+ __block_literal_global.280
+ __block_literal_global.303
+ __block_literal_global.316
+ __block_literal_global.325
+ __block_literal_global.327
+ __block_literal_global.340
+ __block_literal_global.343
+ __block_literal_global.60
+ __block_literal_global.92
+ __main_block_invoke.1036
+ __main_block_invoke.1044
+ __main_block_invoke.1076
+ __main_block_invoke.1078
+ __main_block_invoke.1083
+ __main_block_invoke.1084
+ __main_block_invoke.1092
+ __main_block_invoke.1094
+ __main_block_invoke.1100
+ __main_block_invoke.1101
+ __main_block_invoke.1115
+ __main_block_invoke_2.1080
+ __main_block_invoke_2.1088
+ __main_block_invoke_2.1098
+ __main_block_invoke_2.1104
+ __main_block_invoke_2.1119
+ __main_block_invoke_3.1099
+ __main_block_invoke_3.1107
+ __siginfo_handler_block_invoke.1124
+ __siginfo_handler_block_invoke.1128
+ _createCacheDeleteToken
+ _g_fair_purge_should_defer
+ _getSiblings
+ _hasUserVolume
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$_analyzeAndSortAppsByWeight:
+ _objc_msgSend$_calculateAverageLastUseTimeForEntry:recentlyUsedApps:
+ _objc_msgSend$_calculatePluginSizesForApps:
+ _objc_msgSend$_calculateWeightForApp:alpha:recentlyUsedApps:
+ _objc_msgSend$_loadHardcodedPluginMappingData
+ _objc_msgSend$_purgeCachePathForApp:
+ _objc_msgSend$_purgePluginsForApp:
+ _objc_msgSend$_purgeSpecificApplications:forVolume:purgeLimit:
+ _objc_msgSend$_queryFSPurgeableBatchAllVolumes:urgency:infoCopy:refreshAll:
+ _objc_msgSend$_serviceCancelPurgeImmediate:
+ _objc_msgSend$_updateFSPurgeableSizesForApps:forVolume:
+ _objc_msgSend$_updateWithMappingData:
+ _objc_msgSend$allAppInfoObjects
+ _objc_msgSend$allHiddenAppBundleIDs
+ _objc_msgSend$allServices
+ _objc_msgSend$allVisibleAppBundleIDs
+ _objc_msgSend$appBundleIDForPlugin:
+ _objc_msgSend$appClassifier
+ _objc_msgSend$appTelemetryData
+ _objc_msgSend$appendBatchAndSaveStats:
+ _objc_msgSend$appsData
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$beforePurgeEventID
+ _objc_msgSend$buildAppInfoForBundleIDs:
+ _objc_msgSend$bundleToPluginsMap
+ _objc_msgSend$bundles
+ _objc_msgSend$bundlesKey
+ _objc_msgSend$cachePurgedSize
+ _objc_msgSend$cacheSize
+ _objc_msgSend$cachedTokenString
+ _objc_msgSend$calculateWeightsForAppInfo:alpha:recentlyUsedOverride:
+ _objc_msgSend$checkCancellationAndAbortIfNeeded:
+ _objc_msgSend$classifierQueue
+ _objc_msgSend$clientPerformFairPurgeOperation:replyBlock:
+ _objc_msgSend$collectStatistics
+ _objc_msgSend$completeWithResultAndReport:
+ _objc_msgSend$completionStatus
+ _objc_msgSend$createAndStartFSEventStreamForSentinel:path:semaphore:outRescan:
+ _objc_msgSend$criticalSystemPluginExemptions
+ _objc_msgSend$dataSize
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$deleteAppCaches:urgency:telemetry:group:
+ _objc_msgSend$deleteAppCaches:urgency:telemetry:group:fairPurgeMode:
+ _objc_msgSend$dirStatIDToBundleMap
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$executeFirstPhase:
+ _objc_msgSend$executePurgeWithFSEventsMonitoring:volume:timeout:outEventID:outMustRescan:
+ _objc_msgSend$executeSecondPhase:
+ _objc_msgSend$executedPhase
+ _objc_msgSend$fairPurgeResult
+ _objc_msgSend$forceHiddenPhase
+ _objc_msgSend$forceVisiblePhase
+ _objc_msgSend$fsPurgeableSize
+ _objc_msgSend$fsPurgedSize
+ _objc_msgSend$getStatistics
+ _objc_msgSend$goalMet:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hiddenAppsData
+ _objc_msgSend$initWithBundles:dataSize:cacheSize:isVisible:
+ _objc_msgSend$internalHiddenAppBundleIDs
+ _objc_msgSend$internalVisibleAppBundleIDs
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isCriticalRelinquishPurge
+ _objc_msgSend$isFirstPhase
+ _objc_msgSend$isServiceIDExempted:
+ _objc_msgSend$isVisible
+ _objc_msgSend$isVisibleApp:
+ _objc_msgSend$lastUseTimeInDays
+ _objc_msgSend$loadAndClassifyDataWithCompletion:
+ _objc_msgSend$loadSAFDataSynchronously
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$markPhaseComplete
+ _objc_msgSend$mustRescan
+ _objc_msgSend$oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:signpostID:
+ _objc_msgSend$parseTestParameters
+ _objc_msgSend$phase1Step1EndTime
+ _objc_msgSend$phase1Step1PluginsReported
+ _objc_msgSend$phase1Step1StartTime
+ _objc_msgSend$phase1Step2ContainersReported
+ _objc_msgSend$phase1Step2EndTime
+ _objc_msgSend$phase1Step2StartTime
+ _objc_msgSend$phase1Step3EndTime
+ _objc_msgSend$phase1Step3FSPurgeableReported
+ _objc_msgSend$phase1Step3StartTime
+ _objc_msgSend$phase2CacheReported
+ _objc_msgSend$phase2FSPurgeableEndTime
+ _objc_msgSend$phase2FSPurgeableReported
+ _objc_msgSend$phase2FSPurgeableStartTime
+ _objc_msgSend$phase2PluginsEndTime
+ _objc_msgSend$phase2PluginsReported
+ _objc_msgSend$phase2PluginsStartTime
+ _objc_msgSend$pluginServices
+ _objc_msgSend$pluginToBundleMap
+ _objc_msgSend$pluginsPurgeableSize
+ _objc_msgSend$pluginsPurgedSize
+ _objc_msgSend$processFSEventsNotificationFromResult:tokenString:
+ _objc_msgSend$processFairPurgeOperationResult:
+ _objc_msgSend$purgeNonVisibleAppContainers:completion:
+ _objc_msgSend$purgeNonVisibleFSPurgeable:completion:
+ _objc_msgSend$purgeNonVisiblePlugins:completion:
+ _objc_msgSend$purgeState
+ _objc_msgSend$purgedVolumeUUIDs
+ _objc_msgSend$recentlyUsedOverride
+ _objc_msgSend$remainingAmountToPurge:
+ _objc_msgSend$reportFairPurge:
+ _objc_msgSend$reportTelemetry
+ _objc_msgSend$roundRobinPurgeServices:amount:batchSize:completion:
+ _objc_msgSend$safDataLoadSuccess
+ _objc_msgSend$serializeTelemetry
+ _objc_msgSend$serviceCancelPurgeImmediate:
+ _objc_msgSend$serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:
+ _objc_msgSend$setAppTelemetryData:
+ _objc_msgSend$setAppsData:
+ _objc_msgSend$setBeforePurgeEventID:
+ _objc_msgSend$setBundleToPluginsMap:
+ _objc_msgSend$setCachePurgedSize:
+ _objc_msgSend$setCachedTokenString:
+ _objc_msgSend$setCollectStatistics:
+ _objc_msgSend$setCompletionStatus:
+ _objc_msgSend$setCriticalRelinquishPurge:
+ _objc_msgSend$setExecutedPhase:
+ _objc_msgSend$setFairPurgeResult:
+ _objc_msgSend$setForceHiddenPhase:
+ _objc_msgSend$setForceVisiblePhase:
+ _objc_msgSend$setFsPurgeableSize:
+ _objc_msgSend$setFsPurgedSize:
+ _objc_msgSend$setHiddenAppsData:
+ _objc_msgSend$setLastUseTimeInDays:
+ _objc_msgSend$setMustRescan:
+ _objc_msgSend$setPhase1Step1EndTime:
+ _objc_msgSend$setPhase1Step1PluginsReported:
+ _objc_msgSend$setPhase1Step1StartTime:
+ _objc_msgSend$setPhase1Step2ContainersReported:
+ _objc_msgSend$setPhase1Step2EndTime:
+ _objc_msgSend$setPhase1Step2StartTime:
+ _objc_msgSend$setPhase1Step3EndTime:
+ _objc_msgSend$setPhase1Step3FSPurgeableReported:
+ _objc_msgSend$setPhase1Step3StartTime:
+ _objc_msgSend$setPhase2CacheReported:
+ _objc_msgSend$setPhase2FSPurgeableEndTime:
+ _objc_msgSend$setPhase2FSPurgeableReported:
+ _objc_msgSend$setPhase2FSPurgeableStartTime:
+ _objc_msgSend$setPhase2PluginsEndTime:
+ _objc_msgSend$setPhase2PluginsReported:
+ _objc_msgSend$setPhase2PluginsStartTime:
+ _objc_msgSend$setPluginToBundleMap:
+ _objc_msgSend$setPluginsPurgeableSize:
+ _objc_msgSend$setPluginsPurgedSize:
+ _objc_msgSend$setRecentlyUsedOverride:
+ _objc_msgSend$setReportTelemetry:
+ _objc_msgSend$setSafDataLoadSuccess:
+ _objc_msgSend$setTagHashToBundleID:
+ _objc_msgSend$setTimedOutServices:
+ _objc_msgSend$setTotalHiddenAppsAnalyzed:
+ _objc_msgSend$setTotalVisibleAppsAnalyzed:
+ _objc_msgSend$setVersion:
+ _objc_msgSend$setWeight:
+ _objc_msgSend$sharedClassifier
+ _objc_msgSend$sharedState
+ _objc_msgSend$shouldTriggerFairPurge:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:
+ _objc_msgSend$stateFileURL
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$supportsCriticalRelinquishPurge
+ _objc_msgSend$tagHashToBundleID
+ _objc_msgSend$tokenString
+ _objc_msgSend$totalHiddenAppsAnalyzed
+ _objc_msgSend$totalVisibleAppsAnalyzed
+ _objc_msgSend$tryFSPurgeBatchAllVolumes:atUrgency:signpostID:orderedServices:completion:
+ _objc_msgSend$waitForGroup:withTimeout:operationName:
+ _objc_msgSend$waitForSemaphore:withTimeout:operationName:
+ _objc_msgSend$waitWithDeferralCheck:waitBlock:operationName:
+ _objc_msgSend$weight
+ _objc_msgSend$weightCalculator
+ _objc_msgSend$writeToURL:options:error:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
+ _objc_sync_enter
+ _objc_sync_exit
+ _os_signpost_id_make_with_pointer
+ _tokenStringForToken
- -[CacheDeletePurgeOperation oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:]
- -[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]
- -[CacheDeletePurgeOperation tryFSPurge:atUrgency:onVolume:orderedServices:completion:]
- GCC_except_table129
- GCC_except_table13
- GCC_except_table140
- GCC_except_table143
- GCC_except_table154
- GCC_except_table239
- GCC_except_table33
- GCC_except_table49
- GCC_except_table54
- GCC_except_table58
- GCC_except_table61
- GCC_except_table67
- GCC_except_table75
- GCC_except_table85
- GCC_except_table91
- GCC_except_table99
- OBJC_IVAR_$_CacheDeletePurgeOperation._purgeResult
- _OBJC_$_PROP_LIST_CDService.270
- _OBJC_$_PROP_LIST_CacheDeleteOperation.242
- __101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke.132
- __28-[CDService drainPurgeQueue]_block_invoke.62
- __30-[CacheDelete totalAvailable:]_block_invoke.316
- __30-[CacheDelete totalAvailable:]_block_invoke.317
- __30-[CacheDelete totalAvailable:]_block_invoke.320
- __30-[CacheDelete totalAvailable:]_block_invoke.323
- __30-[CacheDelete updateFollowup:]_block_invoke.185
- __33-[CacheDelete clientCancelPurge:]_block_invoke.563
- __34-[CacheDelete clientSetState:key:]_block_invoke.673
- __36-[CDXPCService doWithProxy:failure:]_block_invoke.20
- __36-[CDXPCService doWithProxy:failure:]_block_invoke.35
- __36-[CacheDelete applicationExtensions]_block_invoke.232
- __36-[CacheDelete applicationExtensions]_block_invoke.240
- __36-[CacheDelete startPersistenceTimer]_block_invoke.221
- __37-[CacheDelete checkNotificationState]_block_invoke.187
- __37-[CacheDelete purge:volume:callback:]_block_invoke.345
- __37-[CacheDelete purge:volume:callback:]_block_invoke.361
- __37-[CacheDelete purge:volume:callback:]_block_invoke.362
- __37-[CacheDelete purge:volume:callback:]_block_invoke_2.364
- __38-[CacheDelete clientPurge:replyBlock:]_block_invoke.557
- __39-[CacheDelete handleVFSStreamXPCEvent:]_block_invoke.206
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.130
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke.131
- __40-[CacheDelete processLowDiskVolume:key:]_block_invoke_2.132
- __41-[CacheDelete notifyFollowup:completion:]_block_invoke.178
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.440
- __45-[CacheDelete _notifyRecipients:value:force:]_block_invoke.441
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.72
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.77
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.92
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.95
- __45-[CacheDeletePurgeOperation _startOperation:]_block_invoke.96
- __46-[CDService servicePurgeable:info:replyBlock:]_block_invoke.65
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.410
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.417
- __47-[CacheDelete _purge:volume:services:callback:]_block_invoke.428
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.520
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.521
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.522
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.523
- __49-[CacheDelete clientCheckin:endpoint:info:reply:]_block_invoke.524
- __49-[CacheDeletePurgeableOperation _startOperation:]_block_invoke.31
- __49-[CacheDeletePurgeableOperation _startOperation:]_block_invoke.33
- __49-[CacheDeletePurgeableOperation _startOperation:]_block_invoke.74
- __57-[CacheDelete clientPerformPeriodicsWithInfo:completion:]_block_invoke.574
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.429
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.430
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke.437
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.431
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.436
- __68-[CacheDelete processPurgeNotification:forService:info:group:force:]_block_invoke_2.438
- __73-[CDDaemonPurgeableResultCache updateRecentInfoForServiceID:volume:info:]_block_invoke.60
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.287
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.289
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.297
- __89-[CacheDelete updateRecentResultsForVolumes:fsPurgeableOnly:withInfo:qos:receiveResults:]_block_invoke.301
- ___101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke
- ___101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke_2
- ___101-[CacheDeletePurgeOperation serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:]_block_invoke_3
- ___102-[AppContainerCaches processContainerCachesForVolume:bytesNeeded:urgency:calculate:verbose:telemetry:]_block_invoke
- ___111-[CacheDeletePurgeOperation oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:]_block_invoke
- ___111-[CacheDeletePurgeOperation oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:]_block_invoke_2
- ___86-[CacheDeletePurgeOperation tryFSPurge:atUrgency:onVolume:orderedServices:completion:]_block_invoke
- ___89-[AppContainerCaches cachesForInstalledApps:bytesNeeded:volume:sortForUrgency:telemetry:]_block_invoke
- ___89-[AppContainerCaches cachesForInstalledApps:bytesNeeded:volume:sortForUrgency:telemetry:]_block_invoke_2
- ___89-[AppContainerCaches cachesForInstalledApps:bytesNeeded:volume:sortForUrgency:telemetry:]_block_invoke_3
- ___block_descriptor_108_e8_32s40s48s56s64r72r80r88r_e37_v16?0"CDPurgeServiceRequestResult"8lr64l8r72l8r80l8s32l8s40l8s48l8r88l8s56l8
- ___block_descriptor_108_e8_32s40s48s56s64s72bs80r88w_e22_v16?0"NSDictionary"8lw88l8r80l8s32l8s40l8s72l8s48l8s56l8s64l8
- ___block_descriptor_108_e8_32s40s48s56s64s72s80s88r96w_e37_v16?0"CDPurgeServiceRequestResult"8lw96l8s32l8s40l8s48l8s56l8r88l8s64l8s72l8s80l8
- ___block_descriptor_124_e8_32s40s48s56s64s72s80s88s96s104w_e5_v8?0ls32l8s40l8s48l8s56l8s64l8w104l8s72l8s80l8s88l8s96l8
- ___block_descriptor_32_e11_q24?0816l
- ___block_descriptor_56_e8_32s40bs48r_e22_v16?0"NSDictionary"8ls40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e20_v16?0^{__CFArray=}8ls32l8s40l8s48l8
- ___block_descriptor_57_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_68_e8_32s40s48s56s_e28_B24?0"NSString"8"NSURL"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56r64r_e22_v16?0"NSDictionary"8ls32l8s40l8r56l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e8_B12?0i8ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_77_e8_32s40s48s56s64s_e18_B16?0"AppCache"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e8_B12?0i8lr72l8s32l8s40l8s48l8s56l8s64l8r80l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e8_B12?0i8ls32l8r80l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80w_e37_v16?0"CDPurgeServiceRequestResult"8lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_92_e8_32s40s48s56r64r72r80r_e17_B16?0"NSArray"8lr56l8r64l8s32l8s40l8s48l8r72l8r80l8
- ___block_descriptor_92_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8
- __block_literal_global.1028
- __block_literal_global.1038
- __block_literal_global.1041
- __block_literal_global.1045
- __block_literal_global.1049
- __block_literal_global.1055
- __block_literal_global.1059
- __block_literal_global.1063
- __block_literal_global.171
- __block_literal_global.189
- __block_literal_global.199
- __block_literal_global.259
- __block_literal_global.282
- __block_literal_global.319
- __block_literal_global.322
- __block_literal_global.50
- __block_literal_global.62
- __block_literal_global.985
- __block_literal_global.989
- __block_literal_global.993
- __block_literal_global.996
- __main_block_invoke.1026
- __main_block_invoke.1032
- __main_block_invoke.1033
- __main_block_invoke.1047
- __main_block_invoke.986
- __main_block_invoke.994
- __main_block_invoke_2.1030
- __main_block_invoke_2.1036
- __main_block_invoke_2.1051
- __main_block_invoke_3.1031
- __main_block_invoke_3.1039
- __siginfo_handler_block_invoke.1056
- __siginfo_handler_block_invoke.1060
- _objc_msgSend$oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:
- _objc_msgSend$serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:
- _objc_msgSend$setLastUsedTime:
- _objc_msgSend$tmp:purge:all:
- _objc_msgSend$tryFSPurge:atUrgency:onVolume:orderedServices:completion:
CStrings:
+ " tryFSPurgeBatchAllVolumes goal %@"
+ "%@ %d\t%@"
+ "%@ %d %s purge, info: %@"
+ "%@ %d %s purge, result: %@"
+ "%@ %d : Timeout reached for (%@) - stopping purge urgency loop."
+ "%@ %d Final Purge Result: %@ "
+ "%@ %d calling batchServicesForVolume: \"%@\", atUrgency: %d, with services:"
+ "%@ %d proceed: %s, batch:"
+ "%@ %d proceed: %s, numPlayers: %lu"
+ "%@ %{public}@ : %{public}@"
+ "%@ %{public}@ took %f seconds, purged %llu bytes on volume: %{public}@"
+ "%@ %{public}s PURGE callback, cdVol: %{public}@"
+ "%@ %{public}s PURGE result: [u:%d] %{public}@ : %{public}@"
+ "%@ ** %{public}@ is disqualified from purging at urgency %d on volume: %{public}@"
+ "%@ ** %{public}@ will continue purging at urgency %d on volume: %{public}@"
+ "%@ <<<Purge Result: %{public}@ measured bytes (%{public}@ reported) on volume: \"%{public}@\""
+ "%@ Added %@ to purgeOperations"
+ "%@ Batch FSPurge noting purge on %@ : %@"
+ "%@ Batch FSPurge reports %llu purged (%llu total reported, %llu measured) of %llu needed on main volume: %{public}@ at urgency: %d, ET: %f"
+ "%@ Batch FSPurge satisfied request: %llu purged (%llu measured) of %llu needed on volume: %@, ET: %f"
+ "%@ CacheDeleteEnumerateRemovedFiles callback, events: %@"
+ "%@ CancelPurge Start "
+ "%@ CancelPurge complete (service=%{public}@)"
+ "%@ Created FSEventStream with: %@"
+ "%@ FSEvents monitoring - Created FSEventStream for sentinel inode %llu"
+ "%@ FSEvents monitoring - FSEventStream stopped and released"
+ "%@ FSEvents monitoring - Failed to create FSEventStream"
+ "%@ FSEvents monitoring - Failed to create sentinel file"
+ "%@ FSEvents monitoring - Sentinel wait timed out after %f seconds"
+ "%@ FSEvents monitoring - beforePurgeEventID: %llu"
+ "%@ FSPurge begin"
+ "%@ FSPurge timed out waiting for deleted_helper after %llu seconds"
+ "%@ FSpurge finished"
+ "%@ Forcing purge notification for volumes: %@"
+ "%@ No FS purge notification data in result"
+ "%@ Notifying recipients with %lu directories"
+ "%@ Purge Result: %{public}llu bytes on: %{public}@"
+ "%@ Purge Result>>> (%{public}@ measured bytes on volume: \"%{public}@\")"
+ "%@ Purge satisfied, skipping batch FSPurge %@"
+ "%@ Purge: goal %@ freespace %llu"
+ "%@ PurgeOperation on volume %@, registered services:"
+ "%@ Purging %{public}@ at urgency = %d"
+ "%@ Removed %@ from purgeOperations "
+ "%@ Services purge begin"
+ "%@ Services purge finished"
+ "%@ Skipping %{public}@ at urgency %d - service timed out at operation level (%d sec) and is still in-flight at XPC level"
+ "%@ VOLUMES: %@"
+ "%@ [No normal services to process for %{public}@, skipping services loop]"
+ "%@ [Purge Cleanup](Volume: %{public}@, Urgency %d : Round %d) Begin"
+ "%@ [Purge Cleanup](Volume: %{public}@, Urgency %d : Round %d) End"
+ "%@ [Purge End](Volume %{public}@, Urgency %d) finished after %d Rounds (%llu bytes left)"
+ "%@ [Purge Main](Volume: %{public}@, Urgency %d : Round %d) %{public}@ request %llu bytes"
+ "%@ [Purge Main](Volume: %{public}@, Urgency %d : Round %d) Begin"
+ "%@ [Purge Main](Volume: %{public}@, Urgency %d : Round %d) Timed out waiting for %llu seconds: %{public}@"
+ "%@ [Purge Main](Volume: %{public}@, Urgency %d : Round %d) Waiting for end of round: %llu seconds"
+ "%@ [Purge OneShot] (Volume: %{public}@, Urgency %d) Timed out waiting for: %{public}@"
+ "%@ [Purge OneShot](Volume: %{public}@, Urgency %d) Begin"
+ "%@ [Purge OneShot](Volume: %{public}@, Urgency %d) End"
+ "%@ [Purge Result (oneShot)] %{public}@ purged (%llu / %llu) bytes on volume: %{public}@ in %lf seconds"
+ "%@ [Purge Result(tardy!)](Volume: %{public}@, Urgency %d : Round %d) %{public}@ purged (%llu / %llu) bytes : elapsed time %lfs"
+ "%@ [Purge Result](Volume: %{public}@, Urgency %d : Round %d) %{public}@ purged (%llu / %llu) bytes : elapsed time %lfs"
+ "%@ [Purge Start] aborting, (_donation <= 0), roundGoal: %llu"
+ "%@ [Purge Start] aborting, (roundGoal <= 0): %llu, purge_amount_needed: %llu, amountPurged: %llu"
+ "%@ [Purge Start](Urgency %d : Round %d) Volume = %{public}@, Goal = %llu, Donation = %llu, Remaining Services:"
+ "%@ [Purge VERY_LOWDISK]: asking snapshot holders for %llu bytes from %{public}@"
+ "%@ [Purge goal satisfied by fsPurge for %{public}@, skipping cleanup and services loop]"
+ "%@ [Purge goal satisfied for %{public}@, skipping services loop]"
+ "%@ attempted to directly use kCacheDeleteUrgencyCriticalRelinquish in purge operation. This urgency is reserved for internal purgeable query caching only."
+ "%@ attempted to directly use kCacheDeleteUrgencyCriticalRelinquish without CACHE_DELETE_CRITICAL_RELINQUISH_PURGE_KEY. This urgency is reserved for internal use only."
+ "%@ beforePurgeEventID: %llu"
+ "%@ cache_delete FS purge did NOT satisfy the request %llu bytes short"
+ "%@ cache_delete FS purge satisfied the request amountPurged %lld requested %lld"
+ "%@ cache_delete purge cancelled"
+ "%@ cache_delete purge cancelled (FS purge)"
+ "%@ cache_delete purge: fsPurge did NOT satisfy the request"
+ "%@ cache_delete purge: fsPurge did satisfy the request as the freespace increased now"
+ "%@ clientCancelPurge called %@ "
+ "%@ clientPurge called with info: %@"
+ "%@ clientPurge completed with result: %@"
+ "%@ fsPurgeNotify mountPoint: %@"
+ "%@ is not entitled to query critical relinquish purge purgeable space. Requires com.apple.cache_delete.critical_level_relinquish_purge entitlement."
+ "%@ is not entitled to use critical relinquish purge mode. Requires com.apple.cache_delete.critical_level_relinquish_purge entitlement."
+ "%@ mainVolume: %{public}@, freespace:%lld initialfreespace:%lld"
+ "%@ mainVolume: %{public}@, fstype: %{public}@ freespace:%lld "
+ "%@ signalling historyDone"
+ "%@ signalling rescan"
+ "%@ supports critical relinquish purge mode"
+ "%@ trying fsPurge on volume: %@, with info: %@, services: %@"
+ "%@ urgencyLimit: %d, info at start: %{public}@"
+ "%@: _serviceCancelPurgeImmediate - no connection available, nothing to cancel"
+ "%@: _serviceCancelPurgeImmediate XPC error: %@"
+ "%@: _serviceCancelPurgeImmediate bypassing all serialization for Fair Purge deferral"
+ "%@: _serviceCancelPurgeImmediate completed successfully"
+ "%@: serviceCancelPurgeImmediate bypassing request queue for Fair Purge deferral"
+ "%d tryFSPurgeBatchAllVolumes WARNING: Calculating goal (missing from info dict: %@)"
+ "%{public}@ batch fsPurgeable took %f seconds for %lu volumes"
+ "%{public}@ returned %llu an invalid CACHE_DELETE_AMOUNT, using zero"
+ "%{public}s: PURGE CANCEL IMMEDIATE callback (Fair Purge)"
+ ".*"
+ "/System/Library/SpaceAttribution/SpaceAttributionFramework_PathList.plist"
+ "/private/var"
+ "/private/var/mobile"
+ "/var/db/spaceattribution/CDMapping.json"
+ "3"
+ "@\"CDAppClassifier\""
+ "@\"CDFairPurgeOperationResult\""
+ "@\"CDFairPurgeState\""
+ "@\"CDPurgeWeightCalculator\""
+ "@\"NSDate\""
+ "@\"NSNumber\""
+ "@36@0:8Q16@24B32"
+ "@44@0:8@16Q24Q32B40"
+ "@44@0:8@16i24@28@36"
+ "@48@0:8@16i24@28@36B44"
+ "APP_PURGEABLE_SIZES"
+ "App Container Deletion"
+ "App Container Purge"
+ "AppCache for %@ : urgency %d <= %d, will purge (%@)"
+ "AppCache for %@ : urgency %d > %d, skipping"
+ "B16@?0d8"
+ "B40@0:8@16d24@32"
+ "B40@0:8d16@?24@32"
+ "BUNDLE_IDS"
+ "Batch Group"
+ "Batch fsPurge: info: %@"
+ "Batch fsPurge: result: %@"
+ "Batch fsPurgeable timed out for volumes: %@"
+ "CACHE_DELETE_CRITICAL_RELINQUISH_PURGE"
+ "CACHE_DELETE_CRITICAL_RELINQUISH_PURGE_SUPPORT"
+ "CACHE_DELETE_VOLUME_RESULTS"
+ "CDAppClassifier"
+ "CDAppClassifier: %@ not found or invalid in plist"
+ "CDAppClassifier: Failed to load SpaceAttributionFramework_PathList.plist from %@"
+ "CDAppClassifier: Failed to parse SAF mapping JSON: %@"
+ "CDAppClassifier: Failed to read SAF mapping data from %@: %@"
+ "CDAppClassifier: Initialized"
+ "CDAppClassifier: Loaded hardcoded plugin mapping data - %lu bundles with plugins, %lu total plugins"
+ "CDAppClassifier: Loaded plist plugin mapping data - %lu bundles with plugins, %lu total plugins"
+ "CDAppClassifier: SAF data is too stale (%.2f hours old, max allowed: %.2f hours). Bailing out to wait for fresh data."
+ "CDAppClassifier: SAF data timestamp is %@ (%.2f hours old)"
+ "CDAppClassifier: Update complete. Version: %@, Timestamp: %@"
+ "CDAppClassifier: Updating classifier with new SAF data"
+ "CDAppClassifierErrorDomain"
+ "CDFairPurgeOperationResult"
+ "CDFairPurgeState"
+ "CDPurgeWeightCalculator"
+ "CDPurgeWeightCalculator: Using recently used override with %lu apps"
+ "CDPurgeableAppInfo"
+ "CDPurgeableAppInfo{bundles=%@, isVisible=%@, dataSize=%llu, cacheSize=%llu, pluginsSize=%llu, fsPurgeable=%llu, weight=%.3f, pluginsPurged=%llu, cachePurged=%llu, fsPurged=%llu}"
+ "CRITICAL_RELINQUISH_PURGE_ENTITLEMENT"
+ "CacheDeleteFairPurgeInProgress"
+ "CacheDeleteFairPurgeOperation"
+ "Calculated weight for %@: %.3f (lastUse=%.1f, totalPurgeable=%.2f MB, totalData=%.2f MB, ratio=%.3f)"
+ "Critical relinquish purge mode enabled for %@"
+ "Critical relinquish purge purgeable query enabled for %@"
+ "Critical relinquish purgeable query: filtered to %lu critical-supporting services"
+ "Critical relinquish purgeable query: filtered to %lu stale critical-supporting services"
+ "Critical relinquish purgeable query: using urgency=%d for cache isolation"
+ "CurrentPhase"
+ "DIR_STAT_ID_TO_BUNDLE_MAP"
+ "Daily Activity: Deferring execution per DAS recommendation (during loop)"
+ "Daily Activity: Deferring execution per DAS recommendation (pre-start)"
+ "Daily Activity: Deferring execution per DAS recommendation (pre-start) failed"
+ "Deferred_"
+ "Deferred_Phase1_Step1"
+ "Deferred_Phase1_Step2"
+ "Deferred_Phase1_Step3"
+ "Deferred_Phase2_FSPurgeable"
+ "Deferred_Phase2_Plugins"
+ "Deferred_PreStart"
+ "FAIR_PURGE"
+ "FAIR_PURGE_COLLECT_STATISTICS"
+ "FAIR_PURGE_FORCE_HIDDEN_PHASE"
+ "FAIR_PURGE_FORCE_VISIBLE_PHASE"
+ "FAIR_PURGE_OPERATION"
+ "FAIR_PURGE_RECENTLY_USED_OVERRIDE"
+ "FAIR_PURGE_REPORT_TELEMETRY"
+ "FAIR_PURGE_TELEMETRY"
+ "FS Purge"
+ "FSPurgeOperation"
+ "FSPurgeable Purge"
+ "Failed to get CacheDelete caches directory for FairPurge state"
+ "Failed to get recently used apps dictionary - cannot calculate weights accurately"
+ "Failed to parse SAF mapping JSON"
+ "Failed to read SAF mapping data"
+ "Failed_"
+ "Failed_AppAnalysis"
+ "Failed_NoVolume"
+ "Failed_SAFLoad"
+ "Fair Purge Activity: Activity was deferred, not setting DONE state"
+ "Fair Purge Activity: Deferring execution per DAS recommendation (pre-start)"
+ "Fair Purge Activity: Deferring execution per DAS recommendation (pre-start) failed"
+ "Fair Purge Activity: Failed to defer during timer check"
+ "Fair Purge Activity: Found %lu sibling volumes using getSiblings"
+ "Fair Purge Activity: No purge needed (current free space: %llu >= goal: %llu)"
+ "Fair Purge Activity: No sibling volumes found"
+ "Fair Purge Activity: No valid volumes found after validation"
+ "Fair Purge Activity: Operation completed with result: %@"
+ "Fair Purge Activity: Should not trigger (see shouldTriggerFairPurge logs for reason)"
+ "Fair Purge Activity: Started deferral check timer"
+ "Fair Purge Activity: Starting"
+ "Fair Purge Activity: Timer detected activity finished, suspending timer"
+ "Fair Purge Activity: Timer detected should_defer = YES, suspending timer"
+ "Fair Purge Activity: Triggering fair purge operation for %lu volumes: %@"
+ "Fair Purge Activity: Volume %@ failed validation"
+ "Fair Purge Activity: should_defer: %s"
+ "Fair Purge Analytics: Completed telemetry submission - phase: %lu, totalEvents: %lu (1 overall + %lu breakdowns + %lu services + %lu timeouts + %lu apps)"
+ "Fair Purge Analytics: Processing telemetry for phase %lu with completion status: %@"
+ "Fair Purge Analytics: Submitted %lu per-app events"
+ "Fair Purge Analytics: Submitted Phase 1 Step 1 breakdown event to CA - reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted Phase 1 Step 2 breakdown event to CA - reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted Phase 1 Step 3 breakdown event to CA - reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted Phase 2 Cache breakdown event to CA - reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted Phase 2 FSPurgeable breakdown event to CA - reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted Phase 2 Plugins breakdown event to CA - reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted overall event to CA - serviceName: %@, serviceLevel: %ld, reported: %llu bytes, measured: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: Submitted per-service event to CA - serviceName: %@, reported: %llu bytes, time: %.2f ms"
+ "Fair Purge Analytics: events sent to CA view purgeStats"
+ "Fair Purge Operation: %@ timed out after %f seconds"
+ "Fair Purge Operation: Added FS purge notification to result (eventID: %llu, volumes: %lu, rescan: %s)"
+ "Fair Purge Operation: All batches processed, total purged: %llu"
+ "Fair Purge Operation: Analyzing FSPurgeable data for %lu hidden apps"
+ "Fair Purge Operation: App '%@' has no purgeable data - Skipping"
+ "Fair Purge Operation: App caches deletion cancelled or timed out"
+ "Fair Purge Operation: App container caches purged %llu bytes for hidden apps"
+ "Fair Purge Operation: App containers purged %llu bytes (measured: %llu)"
+ "Fair Purge Operation: Batch %lu cancelled or timed out"
+ "Fair Purge Operation: Batch %lu complete, purged %llu bytes (total: %llu)"
+ "Fair Purge Operation: Cancellation requested during %@, aborting"
+ "Fair Purge Operation: Cancelling purge_specific_apps due to timeout/deferral during FS purge"
+ "Fair Purge Operation: Cancelling purge_specific_apps due to timeout/deferral during purgeable analysis"
+ "Fair Purge Operation: Collecting statistics for %lu apps"
+ "Fair Purge Operation: Deferral requested before start, aborting"
+ "Fair Purge Operation: Executing both phases, forced by test parameters"
+ "Fair Purge Operation: Executing first phase (hidden apps)"
+ "Fair Purge Operation: Executing first phase (hidden apps) - forced by test parameter"
+ "Fair Purge Operation: Executing second phase (visible apps)"
+ "Fair Purge Operation: Executing second phase (visible apps) - forced by test parameter"
+ "Fair Purge Operation: FSPurgeable purged %llu bytes (measured: %llu)"
+ "Fair Purge Operation: Failed to analyze FS purgeable data for hidden apps on one or more volumes"
+ "Fair Purge Operation: Failed to analyze FS purgeable data for hidden apps on volume: %@"
+ "Fair Purge Operation: Failed to analyze FS purgeable data for visible apps on one or more volumes"
+ "Fair Purge Operation: Failed to analyze FS purgeable data for visible apps on volume: %@"
+ "Fair Purge Operation: Failed to analyze and sort apps"
+ "Fair Purge Operation: Failed to calculate weights for apps"
+ "Fair Purge Operation: Failed to get SAF data: %@"
+ "Fair Purge Operation: Failed to get purgeable sizes from service"
+ "Fair Purge Operation: First phase - need to purge %llu bytes, initial free space: %llu bytes"
+ "Fair Purge Operation: First phase complete (needed: %llu, purged: %llu)"
+ "Fair Purge Operation: Forced hidden phase mode enabled"
+ "Fair Purge Operation: Forced visible phase mode enabled"
+ "Fair Purge Operation: Found %lu apps with FSPurgeable data"
+ "Fair Purge Operation: Found %lu non-visible plugins to purge"
+ "Fair Purge Operation: Found %lu plugin services to purge for app %@"
+ "Fair Purge Operation: Goal met after app container purge (needed: %llu, purged: %llu)"
+ "Fair Purge Operation: Goal met after plugin purge (needed: %llu, purged: %llu)"
+ "Fair Purge Operation: Goal met after purging plugins for %@, skipping cache purge"
+ "Fair Purge Operation: Goal met during plugin purge (batch %lu, needed: %llu, purged: %llu)"
+ "Fair Purge Operation: Goal met during visible app purge."
+ "Fair Purge Operation: Invalid override date value for %@: %@"
+ "Fair Purge Operation: Multiple bundles (%lu) for app %@ - placeholder implementation"
+ "Fair Purge Operation: No APP_PURGEABLE_SIZES found in service response"
+ "Fair Purge Operation: No FS purge performed, no notification data to add"
+ "Fair Purge Operation: No apps provided for purging"
+ "Fair Purge Operation: No apps selected for purging"
+ "Fair Purge Operation: No apps selected for purging in second phase"
+ "Fair Purge Operation: No bundle IDs found for FS purgeable analysis"
+ "Fair Purge Operation: No hidden apps found for app container purging"
+ "Fair Purge Operation: No hidden apps found to analyze for FSPurgeable data"
+ "Fair Purge Operation: No non-visible plugins found"
+ "Fair Purge Operation: No parent app found for plugin %@ - treating as non-visible"
+ "Fair Purge Operation: No plugin services to purge for app %@"
+ "Fair Purge Operation: No visible apps found to process"
+ "Fair Purge Operation: No volume available for FSPurgeable purge"
+ "Fair Purge Operation: No volume available for second phase"
+ "Fair Purge Operation: No volumes available for plugin purging"
+ "Fair Purge Operation: Override recently used date for %@: %@"
+ "Fair Purge Operation: Per-service amount: %llu bytes"
+ "Fair Purge Operation: Phase 1 - Purge target met, skipping volume %@"
+ "Fair Purge Operation: Phase 1 - Tracked volume %@ : %@ (rescan: %s)"
+ "Fair Purge Operation: Phase 2 - Purge target met, skipping volume %@"
+ "Fair Purge Operation: Phase 2 - Tracked volume %@ : %@ (rescan: %s)"
+ "Fair Purge Operation: Plugin %@ (parent: %@) has %llu bytes purgeable on volume %@"
+ "Fair Purge Operation: Plugin %@ has %llu bytes purgeable (total: %llu)"
+ "Fair Purge Operation: Plugin service purge cancelled or timed out on volume %@"
+ "Fair Purge Operation: Plugin service purged %llu bytes on volume %@"
+ "Fair Purge Operation: Plugins purged %llu bytes (measured: %llu)"
+ "Fair Purge Operation: Processing FS purgeable analysis for volume: %@"
+ "Fair Purge Operation: Processing batch %lu/%lu with %lu services"
+ "Fair Purge Operation: Processing plugin service for app %@ on volume: %@"
+ "Fair Purge Operation: Processing service %@ for volume: %@"
+ "Fair Purge Operation: Purged %llu bytes from %lu selected apps"
+ "Fair Purge Operation: Purged %llu bytes of cache for app %@"
+ "Fair Purge Operation: Purging FS purgeable files for %lu selected apps"
+ "Fair Purge Operation: Purging app containers for %lu hidden apps"
+ "Fair Purge Operation: Purging cache path for app %@"
+ "Fair Purge Operation: Purging plugins and cache for visible app: %@"
+ "Fair Purge Operation: Purging plugins for app %@"
+ "Fair Purge Operation: Recently used date override enabled for %lu apps"
+ "Fair Purge Operation: Round-robin purging %lu services (batch size: %lu)"
+ "Fair Purge Operation: SAF data loaded successfully"
+ "Fair Purge Operation: Selected %lu apps to meet remaining target of %llu bytes (total purgeable: %llu)"
+ "Fair Purge Operation: Selected %lu apps to meet target of %llu bytes (total: %llu)"
+ "Fair Purge Operation: Selected app '%@' for purging (plugins: %llu, cache: %llu, FS: %llu, total: %llu)"
+ "Fair Purge Operation: Serialized telemetry for %lu apps"
+ "Fair Purge Operation: Service %@ not found in services dictionary"
+ "Fair Purge Operation: Service %@ purged %llu bytes on volume %@"
+ "Fair Purge Operation: Service %@ timed out on volume %@ after %f seconds"
+ "Fair Purge Operation: Skipping %@ service in plugin purge loop (handled separately for FS purgeable)"
+ "Fair Purge Operation: Skipping %@ service in plugin size calculation (not a regular plugin)"
+ "Fair Purge Operation: Skipping critical system plugin %@ (exempted from fair purge)"
+ "Fair Purge Operation: Skipping critical system plugin %@ in size calculation (exempted from fair purge)"
+ "Fair Purge Operation: Skipping plugin %@ (belongs to visible app %@)"
+ "Fair Purge Operation: Skipping plugin service %@ on volume %@ (no purgeable data)"
+ "Fair Purge Operation: Skipping service %@ purge on volume %@"
+ "Fair Purge Operation: Starting"
+ "Fair Purge Operation: Statistics collected for %lu apps"
+ "Fair Purge Operation: Statistics collection mode enabled"
+ "Fair Purge Operation: Statistics mode - skipping FSPurgeable purging for hidden apps"
+ "Fair Purge Operation: Statistics mode - skipping plugin purging"
+ "Fair Purge Operation: Statistics mode - skipping visible app purging"
+ "Fair Purge Operation: Step 1 - No amount to purge, skipping non-visible plugins"
+ "Fair Purge Operation: Step 1 - Purging non-visible plugins"
+ "Fair Purge Operation: Step 2 - No amount to purge, skipping non-visible app containers"
+ "Fair Purge Operation: Step 2 - Purging non-visible app containers"
+ "Fair Purge Operation: Step 3 - Analyzing and purging non-visible FSPurgeable"
+ "Fair Purge Operation: Step 3 - No amount to purge, skipping non-visible FSPurgeable"
+ "Fair Purge Operation: Total plugins purged for app %@: %llu bytes"
+ "Fair Purge Operation: Updated app '%@' with %llu bytes of FS purgeable data on volume %@ (total: %llu)"
+ "Fair Purge Operation: Will purge %@ (%llu bytes)"
+ "Fair Purge Operation: Will purge app group '%@' (%llu bytes, total: %llu)"
+ "Fair Purge Operation: beforePurgeEventID: %llu"
+ "Fair Purge Operation: purge specific apps service not available"
+ "Fair Purge Operation: purge specific apps service not available for FS purgeable analysis"
+ "Fair Purge Operation: purge specific apps service not available for purging"
+ "Fair Purge Operation: purge_specific_apps cancellation complete during FS purge"
+ "Fair Purge Operation: purge_specific_apps cancellation complete during purgeable analysis"
+ "Fair Purge Operation: self.services has %lu services"
+ "Fair Purge State: Failed to deserialize state: %@"
+ "Fair Purge State: Failed to serialize state: %@"
+ "Fair Purge State: Failed to write state to disk: %@"
+ "Fair Purge State: Loaded state (phase=%ld, lastRun=%@)"
+ "Fair Purge State: No existing state file, using defaults"
+ "Fair Purge State: No state file URL available"
+ "Fair Purge State: No state file URL available for loading"
+ "Fair Purge State: Saved state (phase=%ld) to %@"
+ "Fair Purge operation: invalid volume %@"
+ "Fair Purge operation: invalid volume %@ in array"
+ "Fair Purge operation: no valid volumes found in array"
+ "Fair Purge operation: volume info must be NSString or NSArray, got %@"
+ "Fair Purge purgeSentinel Created %s"
+ "Fair Purge purgeSentinel Unable to fstat %@ : %s"
+ "Fair Purge purgeSentinel ino: %llu"
+ "Fair Purge purgeSentinel mkdir failed for %s : %s"
+ "Fair Purge purgeSentinel unable to open %s : %s"
+ "Fair Purge purgeSentinel unlink'd %s : %s"
+ "Fair Purge: First phase complete, moving to second phase"
+ "Fair Purge: Operation completed with result: %@"
+ "Fair Purge: Reset deferral flag for client-initiated operation"
+ "Fair Purge: Second phase complete, resetting to first phase"
+ "Fair Purge: Skipping - freespace (%llu) above threshold (%llu)"
+ "Fair Purge: Skipping - freespace (%llu) below desired threshold (%llu), low disk purge should handle this"
+ "Fair Purge: Skipping - volume %@ already has purge in progress"
+ "Fair Purge: State reset to first phase"
+ "Fair Purge: Threshold check triggered (freeSpace: %llu < threshold: %llu)"
+ "FairPurge"
+ "FairPurgeState.plist"
+ "FairPurge_%@"
+ "FairPurge_Phase1_Step1"
+ "FairPurge_Phase1_Step2"
+ "FairPurge_Phase1_Step3"
+ "FairPurge_Phase2_Cache"
+ "FairPurge_Phase2_FSPurgeable"
+ "FairPurge_Phase2_Plugins"
+ "FairPurging"
+ "First Phase results: %@"
+ "Invalid volume"
+ "Invalid volume info type"
+ "JSONObjectWithData:options:error:"
+ "LastRunTimestamp"
+ "No valid volumes found"
+ "Phase1_"
+ "Phase1_Overall"
+ "Phase1_Step1"
+ "Phase1_Step2"
+ "Phase1_Step3"
+ "Phase2_"
+ "Phase2_Cache"
+ "Phase2_FSPurgeable"
+ "Phase2_Overall"
+ "Phase2_Plugins"
+ "Plugin Purge"
+ "Plugin Service"
+ "PluginPurgeRequest"
+ "PluginTimeout"
+ "PurgeOperation"
+ "PurgeOperation: Skipping %@ service (only for Fair Purge operations)"
+ "PurgeOperation: Skipping %@ service in FS filter (only for Fair Purge operations)"
+ "Purgeable Analysis"
+ "PurgeableOperation: Calling service %@ with urgency=%d, volume=%@, CACHE_DELETE_CRITICAL_RELINQUISH_PURGE_KEY=%@"
+ "PurgeableOperation: Skipping %@ service (only for Fair Purge operations)"
+ "PurgeableOperation: Skipping %@ service in query loop (only for Fair Purge operations)"
+ "PurgeableOperation: isCriticalQuery=%d, CACHE_DELETE_CRITICAL_RELINQUISH_PURGE_KEY=%@"
+ "Q24@0:8@16"
+ "Q40@0:8@16@24Q32"
+ "Q56@0:8@?16@24d32^Q40^B48"
+ "Q8@?0"
+ "SAF Loading"
+ "SAF data is too stale (%.2f hours old)"
+ "SAF mapping data is nil"
+ "SPACE_ATTRIBUTION_DAEMON_MAP"
+ "Step 2"
+ "Step 3"
+ "T@\"CDAppClassifier\",&,N,V_appClassifier"
+ "T@\"CDFairPurgeOperationResult\",&,N,V_fairPurgeResult"
+ "T@\"CDFairPurgeState\",&,N,V_purgeState"
+ "T@\"CDPurgeWeightCalculator\",&,N,V_weightCalculator"
+ "T@\"NSArray\",&,N,V_appTelemetryData"
+ "T@\"NSArray\",C,N,V_appsData"
+ "T@\"NSArray\",C,N,V_hiddenAppsData"
+ "T@\"NSArray\",R,C,N,V_bundles"
+ "T@\"NSDate\",&,N,V_lastRunTimestamp"
+ "T@\"NSDictionary\",&,N,V_allServices"
+ "T@\"NSDictionary\",&,N,V_recentlyUsedOverride"
+ "T@\"NSDictionary\",C,N,V_bundleToPluginsMap"
+ "T@\"NSDictionary\",C,N,V_pluginToBundleMap"
+ "T@\"NSDictionary\",C,N,V_tagHashToBundleID"
+ "T@\"NSMutableArray\",&,N,V_purgedVolumeUUIDs"
+ "T@\"NSMutableArray\",R,N,V_pluginServices"
+ "T@\"NSMutableDictionary\",&,N,V_allAppInfoObjects"
+ "T@\"NSMutableSet\",&,N,V_internalHiddenAppBundleIDs"
+ "T@\"NSMutableSet\",&,N,V_internalVisibleAppBundleIDs"
+ "T@\"NSMutableSet\",&,N,V_timedOutServices"
+ "T@\"NSNumber\",C,N,V_timestamp"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_classifierQueue"
+ "T@\"NSSet\",R,C,N"
+ "T@\"NSString\",&,N,V_cachedTokenString"
+ "T@\"NSString\",C,N,V_completionStatus"
+ "T@\"NSString\",C,N,V_version"
+ "T@\"NSURL\",&,N,V_stateFileURL"
+ "TAG_HASH_TO_BUNDLE_ID_MAP"
+ "TB,N,GisCriticalRelinquishPurge,V_criticalRelinquishPurge"
+ "TB,N,V_collectStatistics"
+ "TB,N,V_forceHiddenPhase"
+ "TB,N,V_forceVisiblePhase"
+ "TB,N,V_mustRescan"
+ "TB,N,V_reportTelemetry"
+ "TB,N,V_safDataLoadSuccess"
+ "TB,N,V_supportsCriticalRelinquishPurge"
+ "TB,R,N,V_isVisible"
+ "TQ,N,V_beforePurgeEventID"
+ "TQ,N,V_cachePurgedSize"
+ "TQ,N,V_executedPhase"
+ "TQ,N,V_fsPurgeableSize"
+ "TQ,N,V_fsPurgedSize"
+ "TQ,N,V_phase1Step1EndTime"
+ "TQ,N,V_phase1Step1PluginsReported"
+ "TQ,N,V_phase1Step1StartTime"
+ "TQ,N,V_phase1Step2ContainersReported"
+ "TQ,N,V_phase1Step2EndTime"
+ "TQ,N,V_phase1Step2StartTime"
+ "TQ,N,V_phase1Step3EndTime"
+ "TQ,N,V_phase1Step3FSPurgeableReported"
+ "TQ,N,V_phase1Step3StartTime"
+ "TQ,N,V_phase2CacheReported"
+ "TQ,N,V_phase2FSPurgeableEndTime"
+ "TQ,N,V_phase2FSPurgeableReported"
+ "TQ,N,V_phase2FSPurgeableStartTime"
+ "TQ,N,V_phase2PluginsEndTime"
+ "TQ,N,V_phase2PluginsReported"
+ "TQ,N,V_phase2PluginsStartTime"
+ "TQ,N,V_pluginsPurgeableSize"
+ "TQ,N,V_pluginsPurgedSize"
+ "TQ,N,V_totalHiddenAppsAnalyzed"
+ "TQ,N,V_totalVisibleAppsAnalyzed"
+ "TQ,R,N,V_cacheSize"
+ "TQ,R,N,V_dataSize"
+ "Td,N,V_lastUseTimeInDays"
+ "Td,N,V_weight"
+ "Tq,N,V_currentPhase"
+ "Unknown"
+ "Weight for %@: -1 (no purgeable data)"
+ "[Fair Purge]"
+ "[Purge]"
+ "^{__FSEventStream=}48@0:8Q16@24@32^B40"
+ "_allAppInfoObjects"
+ "_allServices"
+ "_analyzeAndSortAppsByWeight:"
+ "_appClassifier"
+ "_appTelemetryData"
+ "_appsData"
+ "_beforePurgeEventID"
+ "_bundleToPluginsMap"
+ "_bundles"
+ "_cachePurgedSize"
+ "_cacheSize"
+ "_cachedTokenString"
+ "_calculateAverageLastUseTimeForEntry:recentlyUsedApps:"
+ "_calculatePluginSizesForApps:"
+ "_calculateWeightForApp:alpha:recentlyUsedApps:"
+ "_classifierQueue"
+ "_collectStatistics"
+ "_completionStatus"
+ "_criticalRelinquishPurge"
+ "_currentPhase"
+ "_dataSize"
+ "_executedPhase"
+ "_fairPurgeResult"
+ "_forceHiddenPhase"
+ "_forceVisiblePhase"
+ "_fsPurgeableSize"
+ "_fsPurgedSize"
+ "_hiddenAppsData"
+ "_internalHiddenAppBundleIDs"
+ "_internalVisibleAppBundleIDs"
+ "_isVisible"
+ "_lastRunTimestamp"
+ "_lastUseTimeInDays"
+ "_loadHardcodedPluginMappingData"
+ "_loadPlistPluginMappingData"
+ "_mustRescan"
+ "_phase1Step1EndTime"
+ "_phase1Step1PluginsReported"
+ "_phase1Step1StartTime"
+ "_phase1Step2ContainersReported"
+ "_phase1Step2EndTime"
+ "_phase1Step2StartTime"
+ "_phase1Step3EndTime"
+ "_phase1Step3FSPurgeableReported"
+ "_phase1Step3StartTime"
+ "_phase2CacheReported"
+ "_phase2FSPurgeableEndTime"
+ "_phase2FSPurgeableReported"
+ "_phase2FSPurgeableStartTime"
+ "_phase2PluginsEndTime"
+ "_phase2PluginsReported"
+ "_phase2PluginsStartTime"
+ "_pluginServices"
+ "_pluginToBundleMap"
+ "_pluginsPurgeableSize"
+ "_pluginsPurgedSize"
+ "_purgeCachePathForApp:"
+ "_purgePluginsForApp:"
+ "_purgeSpecificApplications:forVolume:purgeLimit:"
+ "_purgeState"
+ "_purgedVolumeUUIDs"
+ "_queryFSPurgeableBatchAllVolumes:urgency:infoCopy:refreshAll:"
+ "_recentlyUsedOverride"
+ "_reportTelemetry"
+ "_safDataLoadSuccess"
+ "_serviceCancelPurgeImmediate:"
+ "_stateFileURL"
+ "_supportsCriticalRelinquishPurge"
+ "_tagHashToBundleID"
+ "_timestamp"
+ "_totalHiddenAppsAnalyzed"
+ "_totalVisibleAppsAnalyzed"
+ "_updateFSPurgeableSizesForApps:forVolume:"
+ "_updateWithMappingData:"
+ "_version"
+ "_weight"
+ "_weightCalculator"
+ "after FSPurgeable purge"
+ "after app container purge"
+ "after plugin purge"
+ "allAppInfoObjects"
+ "allHiddenAppBundleIDs"
+ "allServices"
+ "allVisibleAppBundleIDs"
+ "app container deletion"
+ "appBundleIDForPlugin:"
+ "appClassifier"
+ "appTelemetryData"
+ "appendBatchAndSaveStats:"
+ "apps"
+ "appsData"
+ "arrayWithCapacity:"
+ "batch processing"
+ "before FS analysis"
+ "before FS purgeable purge"
+ "before plugin size calculation"
+ "beforePurgeEventID"
+ "buildAppInfoForBundleIDs:"
+ "bundleIDs"
+ "bundleKey"
+ "bundleToPluginsMap"
+ "bundles"
+ "bundlesKey"
+ "cache purge"
+ "cachePurgedSize"
+ "cacheSize"
+ "cachedTokenString"
+ "calculateWeightsForAppInfo:alpha:recentlyUsedOverride:"
+ "checkCancellationAndAbortIfNeeded:"
+ "classifierQueue"
+ "clientPerformFairPurgeOperation:replyBlock:"
+ "collectStatistics"
+ "com.apple.CDTests.HiddenApp"
+ "com.apple.CDTests.HiddenApp.CacheDelete.TestService"
+ "com.apple.CacheDelete.CDAppClassifier"
+ "com.apple.CacheDelete.fairpurge"
+ "com.apple.FileProvider"
+ "com.apple.Maps"
+ "com.apple.Music"
+ "com.apple.Spotlight"
+ "com.apple.TextInput"
+ "com.apple.TextInput.CacheDelete"
+ "com.apple.WebBookmarks"
+ "com.apple.WebBookmarks.CacheDelete"
+ "com.apple.abm"
+ "com.apple.abm.cache-delete"
+ "com.apple.appstored"
+ "com.apple.appstored.CacheDelete"
+ "com.apple.assetsd"
+ "com.apple.assetsd.cacheDelete"
+ "com.apple.cache_delete.CDService.serviceCancelPurgeImmediate"
+ "com.apple.cache_delete.fair_purge.completed"
+ "com.apple.cache_delete.fair_purge.should_defer"
+ "com.apple.cache_delete.fair_purge.started"
+ "com.apple.cache_delete.fairpurge_activity"
+ "com.apple.cloudd"
+ "com.apple.cloudd.cache-delete"
+ "com.apple.deleted_helper.purge_specific_apps"
+ "com.apple.geod.cachedelete"
+ "com.apple.healthd"
+ "com.apple.healthd.cache-delete"
+ "com.apple.imagent"
+ "com.apple.imagent.cache-delete"
+ "com.apple.installcoordinationd"
+ "com.apple.installcoordinationd.CacheDelete"
+ "com.apple.itunesstored"
+ "com.apple.itunesstored.CacheDelete"
+ "com.apple.logd"
+ "com.apple.logd.cachedelete"
+ "com.apple.medialibraryd.cacheDelete"
+ "com.apple.mobileassetd"
+ "com.apple.mobileassetd.cache-delete"
+ "com.apple.mobilenotes"
+ "com.apple.mobilenotes.CacheDelete.TestService"
+ "com.apple.pasteboard"
+ "com.apple.pasteboard.cache-delete"
+ "com.apple.quicklook.ThumbnailsAgent"
+ "com.apple.quicklook.ThumbnailsAgent.CacheDelete"
+ "com.apple.replayd"
+ "com.apple.replayd-cache-delete"
+ "com.apple.revisiond"
+ "com.apple.revisiond.cache-delete"
+ "com.apple.searchd.cachedelete"
+ "com.apple.sensorkitd"
+ "com.apple.sensorkitd.CacheDelete"
+ "com.apple.seymour"
+ "com.apple.seymour.cache-delete"
+ "com.apple.symptomsd-diag"
+ "com.apple.symptomsd-diag.CacheDelete"
+ "com.apple.symptomsd-diag.CacheDelete_Anonymous"
+ "com.apple.sysdiagnose"
+ "com.apple.sysdiagnose.CacheDelete"
+ "com.apple.taptoradard"
+ "com.apple.taptoradard.CacheDelete"
+ "com.apple.triald"
+ "com.apple.triald.cache-delete"
+ "completeWithResultAndReport:"
+ "completionStatus"
+ "createAndStartFSEventStreamForSentinel: Created and started FSEventStream for sentinel inode %llu"
+ "createAndStartFSEventStreamForSentinel: Failed to allocate context"
+ "createAndStartFSEventStreamForSentinel: Failed to create FSEventStream: %s"
+ "createAndStartFSEventStreamForSentinel: Failed to get sentinel directory"
+ "createAndStartFSEventStreamForSentinel: Failed to start FSEventStream"
+ "createAndStartFSEventStreamForSentinel: Invalid parameters (inode: %llu, path: %@, semaphore: %p)"
+ "createAndStartFSEventStreamForSentinel: statfs failed for \"%{public}s\" : %s"
+ "createAndStartFSEventStreamForSentinel:path:semaphore:outRescan:"
+ "createFSPurgeNotificationWithEventID: Created notification (eventID: %llu, volumes: %@)"
+ "createFSPurgeNotificationWithEventID: No purged volumes provided"
+ "createFSPurgeNotificationWithEventID: Rescan required (eventID: %llu, volumes: %@)"
+ "createFSPurgeNotificationWithEventID:volumes:mustRescan:"
+ "criticalRelinquishPurge"
+ "criticalSystemPluginExemptions"
+ "currentPhase"
+ "d32@0:8@16@24"
+ "dataSize"
+ "dataWithContentsOfURL:options:error:"
+ "dateWithTimeIntervalSince1970:"
+ "dateWithTimeIntervalSinceNow:"
+ "decodeBoolForKey:"
+ "decodeDoubleForKey:"
+ "decodeObjectOfClass:forKey:"
+ "decodeObjectOfClasses:forKey:"
+ "deleteAppCaches: Operation cancelled due to Fair Purge deferral, aborting"
+ "deleteAppCaches: Purged %llu bytes from %@ (clearAll=%d)"
+ "deleteAppCaches: Purging %lu apps at urgency %d"
+ "deleteAppCaches: Total purged %llu bytes at urgency %d"
+ "deleteAppCaches:urgency:telemetry:group:"
+ "deleteAppCaches:urgency:telemetry:group:fairPurgeMode:"
+ "dirStatIDToBundleMap"
+ "dirStatIDs"
+ "encodeBool:forKey:"
+ "encodeDouble:forKey:"
+ "executeFirstPhase:"
+ "executePurgeWithFSEventsMonitoring:volume:timeout:outEventID:outMustRescan:"
+ "executeSecondPhase:"
+ "executedPhase"
+ "fairPurgeResult"
+ "forceHiddenPhase"
+ "forceVisiblePhase"
+ "fsPurgeableSize"
+ "fsPurgedSize"
+ "getStatistics"
+ "goalMet:"
+ "hasSuffix:"
+ "hiddenAppsData"
+ "initWithBundles:dataSize:cacheSize:isVisible:"
+ "internalHiddenAppBundleIDs"
+ "internalVisibleAppBundleIDs"
+ "intersectsSet:"
+ "isCriticalRelinquishPurge"
+ "isFirstPhase"
+ "isServiceIDExempted:"
+ "isVisible"
+ "isVisibleApp:"
+ "lastRunTimestamp"
+ "lastUseTimeInDays"
+ "loadAndClassifyData"
+ "loadAndClassifyDataWithCompletion:"
+ "loadSAFDataSynchronously"
+ "localizedDescription"
+ "markPhaseComplete"
+ "mustRescan"
+ "none"
+ "oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:signpostID:"
+ "parseTestParameters"
+ "phase1Step1EndTime"
+ "phase1Step1PluginsReported"
+ "phase1Step1StartTime"
+ "phase1Step2ContainersReported"
+ "phase1Step2EndTime"
+ "phase1Step2StartTime"
+ "phase1Step3EndTime"
+ "phase1Step3FSPurgeableReported"
+ "phase1Step3StartTime"
+ "phase2CacheReported"
+ "phase2FSPurgeableEndTime"
+ "phase2FSPurgeableReported"
+ "phase2FSPurgeableStartTime"
+ "phase2PluginsEndTime"
+ "phase2PluginsReported"
+ "phase2PluginsStartTime"
+ "plugin processing"
+ "plugin service processing"
+ "pluginServices"
+ "pluginToBundleMap"
+ "pluginsForApp:"
+ "pluginsPurgeableSize"
+ "pluginsPurgedSize"
+ "processFSEventsNotificationFromResult:tokenString:"
+ "processFairPurgeOperationResult:"
+ "purgeAppCachePurgeable"
+ "purgeAppCachePurged"
+ "purgeAppFSPurgeable"
+ "purgeAppFSPurged"
+ "purgeAppLastUseDays"
+ "purgeAppNonPurgeable"
+ "purgeAppPhase"
+ "purgeAppPluginsPurgeable"
+ "purgeAppPluginsPurged"
+ "purgeAppTotalPurgeable"
+ "purgeAppTotalPurged"
+ "purgeAppVisibility"
+ "purgeAppWeight"
+ "purgeBundleID"
+ "purgeNonVisibleAppContainers:completion:"
+ "purgeNonVisibleFSPurgeable:completion:"
+ "purgeNonVisiblePlugins:completion:"
+ "purgeState"
+ "purged=%{public}llu success=%{public}d error=%{public}s begin_freespace=%{public}llu end_freespace=%{public}llu freespace_delta=%{public}lld"
+ "purged=%{public}llu success=%{public}d satisfied=%{public}d cancelled=%{public}d error=%{public}s"
+ "purgedVolumeUUIDs"
+ "q24@?0@\"CDPurgeableAppInfo\"8@\"CDPurgeableAppInfo\"16"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "recentlyUsedOverride"
+ "remainingAmountToPurge:"
+ "reportFairPurge:"
+ "reportTelemetry"
+ "reset"
+ "roundRobinPurgeServices:amount:batchSize:completion:"
+ "safDataLoadSuccess"
+ "serializeTelemetry"
+ "service=%{public}s urgency=%{public}d reported=%{public}llu success=%{public}d error=%{public}s elapsed_ms=%{public}llu"
+ "service=%{public}s volume=%{public}s urgency=%{public}d requested=%{public}llu"
+ "serviceCancelPurgeImmediate:"
+ "serviceRequest: Batch request preserved %lu volumes"
+ "serviceRequest: Deducted %llu bytes from %@ cache"
+ "serviceRequest:volume:urgency:donation:info:optionalTestInfo:signpostID:completion:"
+ "setAllAppInfoObjects:"
+ "setAllServices:"
+ "setAppClassifier:"
+ "setAppTelemetryData:"
+ "setAppsData:"
+ "setBeforePurgeEventID:"
+ "setBundleToPluginsMap:"
+ "setCachePurgedSize:"
+ "setCachedTokenString:"
+ "setClassifierQueue:"
+ "setCollectStatistics:"
+ "setCompletionStatus:"
+ "setCriticalRelinquishPurge:"
+ "setCurrentPhase:"
+ "setExecutedPhase:"
+ "setFairPurgeResult:"
+ "setForceHiddenPhase:"
+ "setForceVisiblePhase:"
+ "setFsPurgeableSize:"
+ "setFsPurgedSize:"
+ "setHiddenAppsData:"
+ "setInternalHiddenAppBundleIDs:"
+ "setInternalVisibleAppBundleIDs:"
+ "setLastRunTimestamp:"
+ "setLastUseTimeInDays:"
+ "setMustRescan:"
+ "setPhase1Step1EndTime:"
+ "setPhase1Step1PluginsReported:"
+ "setPhase1Step1StartTime:"
+ "setPhase1Step2ContainersReported:"
+ "setPhase1Step2EndTime:"
+ "setPhase1Step2StartTime:"
+ "setPhase1Step3EndTime:"
+ "setPhase1Step3FSPurgeableReported:"
+ "setPhase1Step3StartTime:"
+ "setPhase2CacheReported:"
+ "setPhase2FSPurgeableEndTime:"
+ "setPhase2FSPurgeableReported:"
+ "setPhase2FSPurgeableStartTime:"
+ "setPhase2PluginsEndTime:"
+ "setPhase2PluginsReported:"
+ "setPhase2PluginsStartTime:"
+ "setPluginToBundleMap:"
+ "setPluginsPurgeableSize:"
+ "setPluginsPurgedSize:"
+ "setPurgeState:"
+ "setPurgedVolumeUUIDs:"
+ "setRecentlyUsedOverride:"
+ "setReportTelemetry:"
+ "setSafDataLoadSuccess:"
+ "setStateFileURL:"
+ "setSupportsCriticalRelinquishPurge:"
+ "setTagHashToBundleID:"
+ "setTotalHiddenAppsAnalyzed:"
+ "setTotalVisibleAppsAnalyzed:"
+ "setVersion:"
+ "setWeight:"
+ "setWeightCalculator:"
+ "sharedClassifier"
+ "sharedState"
+ "shouldTriggerFairPurge:"
+ "sortedArrayUsingSelector:"
+ "sortedCachesForInstalledAppsOnVolume:urgency:calculate:bytesNeeded:telemetry:"
+ "start of second phase"
+ "stateFileURL"
+ "subarrayWithRange:"
+ "supportsCriticalRelinquishPurge"
+ "tagHashToBundleID"
+ "tokenString"
+ "totalHiddenAppsAnalyzed"
+ "totalVisibleAppsAnalyzed"
+ "tryFSPurgeBatchAllVolumes:atUrgency:signpostID:orderedServices:completion:"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0Q8"
+ "v20@?0@\"NSArray\"8B16"
+ "v32@0:8Q16@?24"
+ "v40@0:8@16d24@32"
+ "v40@0:8@16i24@28B36"
+ "v48@0:8@16Q24Q32@?40"
+ "v52@0:8Q16i24Q28@36@?44"
+ "v76@0:8@16@24i32Q36@44@52Q60@?68"
+ "v84@0:8@16@24i32Q36@44Q52@60@68Q76"
+ "visible app purge"
+ "volume=%{public}s urgency=%{public}d requested=%{public}llu"
+ "volume=%{public}s urgency=%{public}d round=%{public}d timeout_seconds=%{public}llu service_count=%{public}lu services=%{public}s"
+ "waitForGroup:withTimeout:operationName:"
+ "waitForSemaphore:withTimeout:operationName:"
+ "waitWithDeferralCheck:waitBlock:operationName:"
+ "weight"
+ "weightCalculator"
+ "writeToURL:options:error:"
+ "|%@|%@|%@|%@"
- " clientCancelPurge called %@ "
- " tryFSPurge goal %@"
- "%d\t%@"
- "%d %s purge, info: %@"
- "%d %s purge, result: %@"
- "%d : Timeout reached for (%@) - stopping purge urgency loop."
- "%d Purge Result: %@ "
- "%d cache_delete FS purge did NOT satisfy the request %llu bytes short"
- "%d cache_delete purge cancelled"
- "%d cache_delete purge satisfied the request amountPurged %lld requested %lld"
- "%d calling batchServicesForVolume: \"%@\", atUrgency: %d, with services:"
- "%d proceed: %s, batch:"
- "%d proceed: %s, numPlayers: %lu"
- "%d tryFSPurge WARNING: Calculating goal (missing from info dict: %@)"
- "%{public}@ returned an invalid CACHE_DELETE_AMOUNT, using zero"
- "%{public}@ took %f seconds, purged %llu bytes on volume: %{public}@"
- "%{public}s PURGE result: [u:%d] %{public}@ : %{public}@"
- "%{public}s: PURGE callback, cdVol: %{public}@"
- "** %{public}@ is disqualified from purging at urgency %d on volume: %{public}@"
- "** %{public}@ will continue purging at urgency %d on volume: %{public}@"
- "<<<Purge Result: %{public}@ measured bytes (%{public}@ reported) on volume: \"%{public}@\""
- "Added %@ to purgeOperations"
- "AppCache for %@ : (%@) %@"
- "CacheDeleteEnumerateRemovedFiles callback, events: %@"
- "CancelPurge Start "
- "CancelPurge complete (service=%{public}@)"
- "Created FSEventStream with: %@"
- "Purge Result: %{public}llu bytes on: %{public}@"
- "Purge Result>>> (%{public}@ measured bytes on volume: \"%{public}@\")"
- "Purge satisfied, skipping %@"
- "Purge: goal %@ freespace %llu"
- "PurgeOperation on volume %@, registered services:"
- "Purging %{public}@ at urgency = %d"
- "Removed %@ from purgeOperations "
- "VOLUMES: %@"
- "[Purge Cleanup](Volume: %{public}@, Urgency %d : Round %d) Begin"
- "[Purge Cleanup](Volume: %{public}@, Urgency %d : Round %d) End"
- "[Purge End](Volume %{public}@, Urgency %d) finished after %d Rounds (%llu bytes left)"
- "[Purge Main](Volume: %{public}@, Urgency %d : Round %d) %{public}@ request %llu bytes"
- "[Purge Main](Volume: %{public}@, Urgency %d : Round %d) Begin"
- "[Purge Main](Volume: %{public}@, Urgency %d : Round %d) Timed out waiting for %llu seconds: %{public}@"
- "[Purge Main](Volume: %{public}@, Urgency %d : Round %d) Waiting for end of round: %llu seconds"
- "[Purge OneShot] (Volume: %{public}@, Urgency %d) Timed out waiting for: %{public}@"
- "[Purge OneShot](Volume: %{public}@, Urgency %d) Begin"
- "[Purge OneShot](Volume: %{public}@, Urgency %d) End"
- "[Purge Result (oneShot)] %{public}@ purged (%llu / %llu) bytes on volume: %{public}@ in %lf seconds"
- "[Purge Result(tardy!)](Volume: %{public}@, Urgency %d : Round %d) %{public}@ purged (%llu / %llu) bytes : elapsed time %lfs"
- "[Purge Result](Volume: %{public}@, Urgency %d : Round %d) %{public}@ purged (%llu / %llu) bytes : elapsed time %lfs"
- "[Purge Start] aborting, (_donation <= 0), roundGoal: %llu"
- "[Purge Start] aborting, (roundGoal <= 0): %llu, purge_amount_needed: %llu, amountPurged: %llu"
- "[Purge Start](Urgency %d : Round %d) Volume = %{public}@, Goal = %llu, Donation = %llu, Remaining Services:"
- "[Purge VERY_LOWDISK]: asking snapshot holders for %llu bytes from %{public}@"
- "[Purge goal satisfied by fsPurge for %{public}@, skipping cleanup and services loop"
- "[Purge goal satisfied for %{public}@, skipping services loop"
- "beforePurgeEventID: %llu"
- "cache_delete purge: fsPurge did NOT satisfy the request"
- "cache_delete purge: fsPurge did satisfy the request as the freespace increased now"
- "com.apple.Safari.WebApp"
- "fsPurge noting purge on %@ : %@"
- "fsPurge reports %llu purged (%llu total reported, %llu measured) of %llu needed on volume: %{public}@ at urgency: %d by purging volume: %@, ET: %f"
- "fsPurge satisfied request: %llu purged (%llu measured) of %llu needed on volume: %@, ET: %f"
- "fsPurge: result: %@"
- "fsPurgeNotify mountPoint: %@"
- "mainVolume: %{public}@, freespace:%lld initialfreespace:%lld"
- "mainVolume: %{public}@, fstype: %{public}@ freespace:%lld "
- "oneShot:volume:urgency:donation:currentRoundResults:timeout:info:optionalTestInfo:"
- "serviceRequest:volume:urgency:donation:info:optionalTestInfo:completion:"
- "setLastUsedTime:"
- "signalling historyDone"
- "signalling rescan"
- "tmp:purge:all:"
- "tryFSPurge:atUrgency:onVolume:orderedServices:completion:"
- "trying fsPurge on volume: %@, with info: %@, services: %@"
- "urgencyLimit: %d, info at start: %{public}@"
- "v52@0:8Q16i24@28@36@?44"
- "v68@0:8@16@24i32Q36@44@52@?60"
- "v76@0:8@16@24i32Q36@44Q52@60@68"

```
