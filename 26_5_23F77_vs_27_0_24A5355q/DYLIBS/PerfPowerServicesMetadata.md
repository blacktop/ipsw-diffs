## PerfPowerServicesMetadata

> `/System/Library/PrivateFrameworks/PerfPowerServicesMetadata.framework/PerfPowerServicesMetadata`

```diff

-3031.122.1.0.0
-  __TEXT.__text: 0x3d41c
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x25d4
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x3db1
-  __TEXT.__oslogstring: 0x13e8
-  __TEXT.__gcc_except_tab: 0x128
+3468.0.0.502.1
+  __TEXT.__text: 0x3e888
+  __TEXT.__objc_methlist: 0x285c
+  __TEXT.__const: 0x108
+  __TEXT.__cstring: 0x46da
+  __TEXT.__oslogstring: 0x18e6
+  __TEXT.__gcc_except_tab: 0x140
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x9c8
-  __TEXT.__objc_classname: 0x464
-  __TEXT.__objc_methname: 0x32e3
-  __TEXT.__objc_methtype: 0x544
-  __TEXT.__objc_stubs: 0x38c0
-  __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x1e0
+  __TEXT.__unwind_info: 0x938
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x260
+  __DATA_CONST.__objc_classlist: 0x1f8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1168
+  __DATA_CONST.__objc_selrefs: 0x1308
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH_CONST.__const: 0x500
-  __AUTH_CONST.__cfstring: 0x7ea0
-  __AUTH_CONST.__objc_const: 0x44b8
+  __DATA_CONST.__got: 0x220
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x8be0
+  __AUTH_CONST.__objc_const: 0x48c8
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_arrayobj: 0xa8
-  __AUTH.__objc_data: 0x2d0
-  __DATA.__objc_ivar: 0x154
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x120
   __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x250
+  __DATA_DIRTY.__bss: 0x270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A5115B4A-901A-3AC5-8245-4A8D0C5D64AA
-  Functions: 999
-  Symbols:   3284
-  CStrings:  2995
+  UUID: 4A62F4C5-4035-37A9-B78D-5A33B6E290CF
+  Functions: 1071
+  Symbols:   3522
+  CStrings:  2418
 
Symbols:
+ +[PPSBacklightMetrics allDeclMetrics]
+ +[PPSBacklightMetrics backlightStateChangeMetrics]
+ +[PPSBacklightMetrics backlightXPCCadence]
+ +[PPSBacklightMetrics subsystem]
+ +[PPSBacklightMetrics systemWakeMetrics]
+ +[PPSBasebandMetrics messageIntelligentConnectivity]
+ +[PPSBasebandMetrics messageQuickSwitch]
+ +[PPSMetric isValidIndexKey:]
+ +[PPSMetric isValidIndexKey:].cold.1
+ +[PPSMetric isValidIndexKey:].cold.2
+ +[PPSMetric isValidIndexKey:].cold.3
+ +[PPSMetric(JSON) isValidMetricJSON:].cold.25
+ +[PPSMetric(JSON) isValidMetricJSON:].cold.26
+ +[PPSMetric(JSON) isValidMetricJSON:].cold.27
+ +[PPSSQLMetadataStore queryCategoriesForFilepath:subsystem:].cold.1
+ +[PPSSQLMetadataStore queryCategoriesForSubsystem:usingConnection:]
+ +[PPSSQLMetadataStore queryMetadataHistoryForFilepath:subsystem:category:].cold.1
+ +[PPSSQLMetadataStore queryMetadataHistoryForFilepath:subsystem:category:name:].cold.1
+ +[PPSSQLMetadataStore queryMetadataHistoryForSubsystem:category:name:usingConnection:]
+ +[PPSSQLMetadataStore queryMetadataHistoryForSubsystem:category:usingConnection:]
+ +[PPSSQLMetadataStore querySubsystemsForFilepath:].cold.1
+ +[PPSSQLMetadataStore querySubsystemsUsingConnection:]
+ +[PPSSQLiteConnectionPool sharedInstance]
+ +[PPSSQLiteConnectionPool sharedInstance].cold.1
+ +[PPSWifiMetrics nanStateLoggingCadence]
+ +[PPSWifiMetrics nanStateMetrics]
+ -[PPSMetric addIndexKey:]
+ -[PPSMetric indexKey]
+ -[PPSPooledConnection .cxx_destruct]
+ -[PPSPooledConnection connection]
+ -[PPSPooledConnection dealloc]
+ -[PPSPooledConnection dealloc].cold.1
+ -[PPSPooledConnection init]
+ -[PPSPooledConnection lastAccessTime]
+ -[PPSPooledConnection lockDepth]
+ -[PPSPooledConnection lock]
+ -[PPSPooledConnection pendingEviction]
+ -[PPSPooledConnection recursiveLock]
+ -[PPSPooledConnection setConnection:]
+ -[PPSPooledConnection setLastAccessTime:]
+ -[PPSPooledConnection setLockDepth:]
+ -[PPSPooledConnection setPendingEviction:]
+ -[PPSPooledConnection setRecursiveLock:]
+ -[PPSPooledConnection tryLock]
+ -[PPSPooledConnection unlock]
+ -[PPSSQLiteConnectionPool .cxx_destruct]
+ -[PPSSQLiteConnectionPool _closeConnectionForPath:]
+ -[PPSSQLiteConnectionPool _evictLRUConnectionLocked]
+ -[PPSSQLiteConnectionPool _evictLRUConnectionLocked].cold.1
+ -[PPSSQLiteConnectionPool _evictLRUConnectionLocked].cold.2
+ -[PPSSQLiteConnectionPool _releaseEntry:forPath:]
+ -[PPSSQLiteConnectionPool _releaseEntry:forPath:].cold.1
+ -[PPSSQLiteConnectionPool _releaseEntry:forPath:].cold.2
+ -[PPSSQLiteConnectionPool connectionEntryForPath:createIfNeeded:]
+ -[PPSSQLiteConnectionPool connections]
+ -[PPSSQLiteConnectionPool dealloc]
+ -[PPSSQLiteConnectionPool entriesLock]
+ -[PPSSQLiteConnectionPool evictIdleConnections]
+ -[PPSSQLiteConnectionPool evictIdleConnections].cold.1
+ -[PPSSQLiteConnectionPool init]
+ -[PPSSQLiteConnectionPool maxPoolSize]
+ -[PPSSQLiteConnectionPool memoryPressureSource]
+ -[PPSSQLiteConnectionPool openConnectionForPath:error:]
+ -[PPSSQLiteConnectionPool openConnectionForPath:error:].cold.1
+ -[PPSSQLiteConnectionPool setConnections:]
+ -[PPSSQLiteConnectionPool setEntriesLock:]
+ -[PPSSQLiteConnectionPool setMaxPoolSize:]
+ -[PPSSQLiteConnectionPool setMemoryPressureSource:]
+ -[PPSSQLiteConnectionPool setupMemoryPressureObserver]
+ -[PPSSQLiteConnectionPool setupMemoryPressureObserver].cold.1
+ -[PPSSQLiteConnectionPool setupMemoryPressureObserver].cold.2
+ -[PPSSQLiteConnectionPool usingConnectionForPath:error:perform:]
+ -[PPSSQLiteConnectionPool usingConnectionForPath:error:perform:].cold.1
+ -[PPSSQLiteConnectionPool usingConnectionForPath:error:perform:].cold.2
+ -[PPSSQLiteConnectionPool usingConnectionForPath:error:perform:].cold.3
+ -[PPSSQLiteConnectionPool validateConnection:forPath:]
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table38
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSRecursiveLock
+ _OBJC_CLASS_$_PPSBacklightMetrics
+ _OBJC_CLASS_$_PPSPooledConnection
+ _OBJC_CLASS_$_PPSSQLiteConnectionPool
+ _OBJC_IVAR_$_PPSMetric._indexKey
+ _OBJC_IVAR_$_PPSPooledConnection._connection
+ _OBJC_IVAR_$_PPSPooledConnection._lastAccessTime
+ _OBJC_IVAR_$_PPSPooledConnection._lockDepth
+ _OBJC_IVAR_$_PPSPooledConnection._pendingEviction
+ _OBJC_IVAR_$_PPSPooledConnection._recursiveLock
+ _OBJC_IVAR_$_PPSSQLiteConnectionPool._connections
+ _OBJC_IVAR_$_PPSSQLiteConnectionPool._entriesLock
+ _OBJC_IVAR_$_PPSSQLiteConnectionPool._maxPoolSize
+ _OBJC_IVAR_$_PPSSQLiteConnectionPool._memoryPressureSource
+ _OBJC_METACLASS_$_PPSBacklightMetrics
+ _OBJC_METACLASS_$_PPSPooledConnection
+ _OBJC_METACLASS_$_PPSSQLiteConnectionPool
+ _PPSConnectionPoolLog
+ _PPSConnectionPoolLog.cold.1
+ _PPSConnectionPoolLog.logObj
+ _PPSConnectionPoolLog.onceToken
+ __OBJC_$_CLASS_METHODS_PPSBacklightMetrics
+ __OBJC_$_CLASS_METHODS_PPSSQLiteConnectionPool
+ __OBJC_$_INSTANCE_METHODS_PPSPooledConnection
+ __OBJC_$_INSTANCE_METHODS_PPSSQLiteConnectionPool
+ __OBJC_$_INSTANCE_VARIABLES_PPSPooledConnection
+ __OBJC_$_INSTANCE_VARIABLES_PPSSQLiteConnectionPool
+ __OBJC_$_PROP_LIST_PPSBacklightMetrics
+ __OBJC_$_PROP_LIST_PPSPooledConnection
+ __OBJC_$_PROP_LIST_PPSSQLiteConnectionPool
+ __OBJC_CLASS_PROTOCOLS_$_PPSBacklightMetrics
+ __OBJC_CLASS_RO_$_PPSBacklightMetrics
+ __OBJC_CLASS_RO_$_PPSPooledConnection
+ __OBJC_CLASS_RO_$_PPSSQLiteConnectionPool
+ __OBJC_METACLASS_RO_$_PPSBacklightMetrics
+ __OBJC_METACLASS_RO_$_PPSPooledConnection
+ __OBJC_METACLASS_RO_$_PPSSQLiteConnectionPool
+ ___41+[PPSSQLiteConnectionPool sharedInstance]_block_invoke
+ ___50+[PPSSQLMetadataStore querySubsystemsForFilepath:]_block_invoke
+ ___54-[PPSSQLiteConnectionPool setupMemoryPressureObserver]_block_invoke
+ ___60+[PPSSQLMetadataStore queryCategoriesForFilepath:subsystem:]_block_invoke
+ ___74+[PPSSQLMetadataStore queryMetadataHistoryForFilepath:subsystem:category:]_block_invoke
+ ___79+[PPSSQLMetadataStore queryMetadataHistoryForFilepath:subsystem:category:name:]_block_invoke
+ ___PPSConnectionPoolLog_block_invoke
+ ___block_descriptor_40_e18_16?0^{sqlite3=}8l
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32s_e18_16?0^{sqlite3=}8ls32l8
+ ___block_descriptor_56_e8_32s40s_e18_16?0^{sqlite3=}8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e18_16?0^{sqlite3=}8ls32l8s40l8s48l8
+ ___block_literal_global.121
+ __dispatch_source_type_memorypressure
+ __os_log_fault_impl
+ _dispatch_get_global_queue
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_get_data
+ _dispatch_source_set_event_handler
+ _objc_autorelease
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_closeConnectionForPath:
+ _objc_msgSend$_evictLRUConnectionLocked
+ _objc_msgSend$_releaseEntry:forPath:
+ _objc_msgSend$addIndexKey:
+ _objc_msgSend$backlightStateChangeMetrics
+ _objc_msgSend$backlightXPCCadence
+ _objc_msgSend$compare:
+ _objc_msgSend$connection
+ _objc_msgSend$connectionEntryForPath:createIfNeeded:
+ _objc_msgSend$date
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$distantPast
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$evictIdleConnections
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$isValidIndexKey:
+ _objc_msgSend$lastAccessTime
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$lock
+ _objc_msgSend$lockBeforeDate:
+ _objc_msgSend$lockDepth
+ _objc_msgSend$memoryPressureSource
+ _objc_msgSend$messageIntelligentConnectivity
+ _objc_msgSend$messageQuickSwitch
+ _objc_msgSend$nanStateLoggingCadence
+ _objc_msgSend$nanStateMetrics
+ _objc_msgSend$openConnectionForPath:error:
+ _objc_msgSend$pendingEviction
+ _objc_msgSend$queryCategoriesForSubsystem:usingConnection:
+ _objc_msgSend$queryMetadataHistoryForSubsystem:category:name:usingConnection:
+ _objc_msgSend$queryMetadataHistoryForSubsystem:category:usingConnection:
+ _objc_msgSend$querySubsystemsUsingConnection:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setLastAccessTime:
+ _objc_msgSend$setPendingEviction:
+ _objc_msgSend$setupMemoryPressureObserver
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$systemWakeMetrics
+ _objc_msgSend$tryLock
+ _objc_msgSend$unlock
+ _objc_msgSend$usingConnectionForPath:error:perform:
+ _objc_msgSend$validateConnection:forPath:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x27
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x7
+ _objc_retain_x8
+ _objc_terminate
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sharedInstance.instance
+ _sharedInstance.onceToken
- +[PPSMetadataStore getMetadataHistoryForFilepath:subsystem:category:name:].cold.1
- -[PPSMetadataStore getMetadataForConcatenatedString:]
- -[PPSMetadataStore setMetadataForConcatenatedString:result:]
- -[PPSMetadataStore setMetadataForConcatenatedString:result:].cold.1
- -[PPSMetadataStore setMetadataHistoryCache:]
- GCC_except_table10
- GCC_except_table11
- GCC_except_table22
- GCC_except_table36
- GCC_except_table61
- GCC_except_table94
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _objc_msgSend$getMetadataForConcatenatedString:
- _objc_msgSend$metadataHistoryCache
- _objc_msgSend$openReadConnection:
- _objc_msgSend$setMetadataForConcatenatedString:result:
- _objc_msgSend$setMetadataHistoryCache:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "\""
+ "@16@?0^{sqlite3=}8"
+ "AWDL"
+ "Attempted to release with nil entry or filepath"
+ "Attempting to evict %lu idle connections"
+ "Backlight"
+ "BacklightStateChange"
+ "Block is nil"
+ "Block parameter is nil"
+ "CPU Coalition-Based"
+ "Charging"
+ "Closing connection due to deferred eviction: %{public}@"
+ "Connection acquisition timeout - possible deadlock"
+ "Connection validation failed for %{public}@: %s"
+ "ConnectionPool"
+ "Created new pool entry for: %{public}@ (pool size: %lu/%lu)"
+ "Database file no longer exists: %{public}@"
+ "Entry deallocated while locked (depth: %ld) - ownership model violated"
+ "Existing connection invalid, reopening: %{public}@"
+ "Failed to create memory pressure source"
+ "Failed to create pool entry"
+ "Failed to open connection for: %{public}@"
+ "Failed to query categories: %@"
+ "Failed to query metadata history: %@"
+ "Failed to query subsystems: %@"
+ "Failed to set cache size: %s"
+ "IndexKey"
+ "IntelligentConnectivity"
+ "LRU eviction: no connections to evict"
+ "LRU eviction: removed entry for %{public}@ (last access: %{public}@), connection close deferred to owning thread or dealloc"
+ "Memory pressure eviction: marking entry for deferred eviction for %{public}@"
+ "Memory pressure observer initialized"
+ "Memory pressure received (level: %lu), evicting idle connections"
+ "Metric json property 'indexKey' conflicts with reserved keywords: %@"
+ "Metric json property 'indexKey' is empty"
+ "Metric json property 'indexKey' is not a %@"
+ "NANDown"
+ "NANState"
+ "PPSSQLiteConnectionPoolErrorDomain"
+ "PRAGMA cache_size=512"
+ "PushTopicLimits"
+ "QuickSwitch"
+ "Released exclusive lock for: %{public}@ (depth: %ld -> %ld)"
+ "SELECT 1"
+ "SystemWakeMetrics"
+ "Thermal"
+ "Timeout acquiring connection for %{public}@ - possible deadlock or hung thread"
+ "Unknown error"
+ "assetloadedfromCacheKB"
+ "averageAPL"
+ "averageAPLDimming"
+ "changedSettingsWhileOffCount"
+ "compactor_major_compactions_bailed"
+ "compactor_major_compactions_bytes_freed"
+ "compactor_major_compactions_bytes_moved"
+ "compactor_major_compactions_completed"
+ "compactor_major_compactions_considered"
+ "compactor_major_compactions_segments_freed"
+ "compactor_major_compactions_slots_moved"
+ "confirmedPossibleCount"
+ "contentIdentifiers"
+ "discardedFramesUpTo2mStale"
+ "discardedFramesUpTo3mStale"
+ "discardedFramesUpTo4mStale"
+ "discardedFramesUpTo5mStale"
+ "discardedFramesUpTo6mStale"
+ "displayOffCount"
+ "displayOnCount"
+ "endContinuousSeconds"
+ "endMachTime"
+ "enteringAOTCount"
+ "expiredPossibleCount"
+ "explanation"
+ "featureEnabled"
+ "fk_id"
+ "flipbookLayoutProfile"
+ "flipbookRenderProfile"
+ "id"
+ "indexKey"
+ "indexKey conflicts with reserved keywords: %@"
+ "indexKey is empty string"
+ "indexKey not a NSString type"
+ "invalidatedFramesUpTo2mStale"
+ "invalidatedFramesUpTo3mStale"
+ "invalidatedFramesUpTo4mStale"
+ "invalidatedFramesUpTo5mStale"
+ "invalidatedFramesUpTo6mStale"
+ "maximumAPL"
+ "maximumAPLDimming"
+ "millisecondsDisplayDimmed"
+ "millisecondsDisplayOff"
+ "millisecondsDisplayOn"
+ "millisecondsShowingAOT"
+ "millisecondsSuppressed"
+ "minimumAPL"
+ "minimumAPLDimming"
+ "noTimeSetCount"
+ "possibleCount"
+ "rejectedPossibleCount"
+ "renderedFrameCount"
+ "renderedFrames1to2Min"
+ "renderedFrames2to3Min"
+ "renderedFrames3to4Min"
+ "renderedFrames4to5Min"
+ "renderedFrames5to6Min"
+ "renderedFramesLessThan1Min"
+ "renderedFramesMoreThan6Min"
+ "renderedPartialMinuteCount"
+ "renderedPresentationSeconds"
+ "rtcAlarmsCount"
+ "settingsAndState"
+ "sleepCount"
+ "sleepOver2mCount"
+ "sleepOver3mCount"
+ "sleepOver4mCount"
+ "sleepOver5mCount"
+ "sleepOver6mCount"
+ "softwareRequestCount"
+ "startContinuousSeconds"
+ "startMachTime"
+ "suppressionChangeType"
+ "suppressionReasons"
+ "swapouts_under_300s"
+ "swapouts_under_30s"
+ "swapouts_under_60s"
+ "timestampMS"
+ "totalExpertSwappedCount"
+ "totalExpertsLoadedFromCacheCount"
+ "totalTimeMS"
+ "userEnabled"
+ "userspaceWakeCount"
+ "wakeups_external_q_throttled"
+ "wakeups_fragmentation_detected"
+ "wakeups_free_below_reserved"
+ "wakeups_minor_compactions"
+ "wakeups_scavenger"
+ "wakeups_swap_threshold_exceeded"
+ "wakeups_target_age"
+ "wakeups_thrashing_detected"
+ "wakeups_total"
- "#16@0:8"
- "%@_%@_%@_%@"
- "++metricsSync++"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUnit\""
- "@\"PPSCadence\""
- "@\"PPSMetricType\""
- "@\"PPSPBCadence\""
- "@\"PPSPBEnumMapping\""
- "@\"PPSPBGroupingDimensions\""
- "@\"PPSPBMetricType\""
- "@\"PPSPBRounding\""
- "@\"PPSPBSource\""
- "@\"PPSPBUnit\""
- "@\"PPSRounding\""
- "@\"PPSUnit\""
- "@108@0:8@16@24@32d40i48@52@60i68i72I76i80i84i88i92i96@100"
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8i16Q20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16^{sqlite3=}24"
- "@32@0:8i16I20@24"
- "@32@0:8q16^{sqlite3=}24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8q16@24^{sqlite3=}32"
- "@48@0:8@16@24@32@40"
- "@60@0:8@16d24i32@36@44@52"
- "@64@0:8@16d24i32@36i44@48@56"
- "ANEStatusMetrics"
- "AppResumeInferredCarryMetrics"
- "B"
- "B16@0:8"
- "B20@0:8I16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8d16"
- "B28@0:8i16Q20"
- "B32@0:8@16^{sqlite3=}24"
- "BBMessageLite"
- "BBMsgAll"
- "BBReport"
- "BuddyDataMetrics"
- "FeatureFlagMetrics"
- "I"
- "I16@0:8"
- "JSON"
- "JSONObjectWithData:options:error:"
- "Metadata cache is hit"
- "NSCopying"
- "NSObject"
- "PPSANEMetrics"
- "PPSAPSDMetrics"
- "PPSAccessibilityMetrics"
- "PPSAccessoryUsageSummaryMetrics"
- "PPSApplicationMetrics"
- "PPSAudioMetrics"
- "PPSBGProcessingCommonMetrics"
- "PPSBackupMetrics"
- "PPSBasebandMetrics"
- "PPSBatteryMetrics"
- "PPSButtonMetrics"
- "PPSCadence"
- "PPSCadenceTuple"
- "PPSCameraCaptureMetrics"
- "PPSClientInterface"
- "PPSConfigMetrics"
- "PPSCoreLocation"
- "PPSCoreRoutineMetrics"
- "PPSDisplayMetrics"
- "PPSDownloadMetrics"
- "PPSFileUtilities"
- "PPSGenerativeFunctionMetrics"
- "PPSIOReportMetrics"
- "PPSLocaleMetrics"
- "PPSMapsMetrics"
- "PPSMessageMetrics"
- "PPSMetadataStore"
- "PPSMetric"
- "PPSMetricDeclProtocol"
- "PPSMetricManager"
- "PPSMetricType"
- "PPSNetworkRelayMetrics"
- "PPSPBCadence"
- "PPSPBCadenceTuple"
- "PPSPBEnumMapping"
- "PPSPBEnumTuple"
- "PPSPBGroupingDimensions"
- "PPSPBMetric"
- "PPSPBMetricHistory"
- "PPSPBMetricStream"
- "PPSPBMetricType"
- "PPSPBRounding"
- "PPSPBSource"
- "PPSPBUnit"
- "PPSPMUMetrics"
- "PPSPerformanceMetrics"
- "PPSRenderMetrics"
- "PPSRounding"
- "PPSSMCMetrics"
- "PPSSQLMetadataStore"
- "PPSSensorsMetrics"
- "PPSSleepMetrics"
- "PPSStatusKitAgentMetrics"
- "PPSStorageMetrics"
- "PPSSysctlMetrics"
- "PPSUIKitMetrics"
- "PPSUnit"
- "PPSUtilities"
- "PPSWidgetMetrics"
- "PPSWifiMetrics"
- "PPSXPCMetrics"
- "Plist"
- "Protobuf"
- "Q"
- "Q16@0:8"
- "RebootEventsMetrics"
- "T#,R"
- "T@\"NSArray\",R,V_cadenceTuples"
- "T@\"NSArray\",R,V_groupBy"
- "T@\"NSDictionary\",R,V_enumMapping"
- "T@\"NSMutableArray\",&,N,V_cadences"
- "T@\"NSMutableArray\",&,N,V_enumMaps"
- "T@\"NSMutableArray\",&,N,V_groupBys"
- "T@\"NSMutableArray\",&,N,V_metricHistorys"
- "T@\"NSMutableArray\",&,N,V_metrics"
- "T@\"NSMutableDictionary\",&,N,V_metadataHistoryCache"
- "T@\"NSMutableDictionary\",&,N,V_metricsByID"
- "T@\"NSString\",&,N,V_build"
- "T@\"NSString\",&,N,V_category"
- "T@\"NSString\",&,N,V_exampleValue"
- "T@\"NSString\",&,N,V_key"
- "T@\"NSString\",&,N,V_metricDescription"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_source"
- "T@\"NSString\",&,N,V_subsystem"
- "T@\"NSString\",&,N,V_symbol"
- "T@\"NSString\",&,N,V_value"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,V_build"
- "T@\"NSString\",R,V_category"
- "T@\"NSString\",R,V_name"
- "T@\"NSString\",R,V_source"
- "T@\"NSString\",R,V_subsystem"
- "T@\"NSUnit\",R,V_unit"
- "T@\"PPSCadence\",R,V_cadence"
- "T@\"PPSMetricType\",R,V_metricType"
- "T@\"PPSPBCadence\",&,N,V_cadence"
- "T@\"PPSPBEnumMapping\",&,N,V_enumMapping"
- "T@\"PPSPBGroupingDimensions\",&,N,V_groupBy"
- "T@\"PPSPBMetricType\",&,N,V_metricType"
- "T@\"PPSPBRounding\",&,N,V_rounding"
- "T@\"PPSPBSource\",&,N,V_source"
- "T@\"PPSPBUnit\",&,N,V_unit"
- "T@\"PPSRounding\",R,V_rounding"
- "T@\"PPSUnit\",R,V_unit"
- "TB,N"
- "TB,N,V_dmaCompliant"
- "TB,N,V_filterEntryLogging"
- "TB,R,N"
- "TB,R,V_DMACompliant"
- "TB,R,V_filterEntryLogging"
- "TI,N,V_fixedArraySize"
- "TI,N,V_timeToLive"
- "TI,R,V_fixedArraySize"
- "TI,R,V_timeToLive"
- "TQ,N,V_value"
- "TQ,R"
- "TQ,R,V_value"
- "Td,N,V_protoVersion"
- "Td,N,V_version"
- "Td,R,V_version"
- "Ti,N,V_appIdentifier"
- "Ti,N,V_auxiliaryType"
- "Ti,N,V_category"
- "Ti,N,V_datatype"
- "Ti,N,V_deviceCapability"
- "Ti,N,V_directionality"
- "Ti,N,V_enabledPopulation"
- "Ti,N,V_mode"
- "Ti,N,V_obfuscation"
- "Ti,N,V_privacyClassification"
- "Ti,N,V_storage"
- "Ti,N,V_type"
- "Ti,R,V_appIdentifier"
- "Ti,R,V_auxiliaryType"
- "Ti,R,V_category"
- "Ti,R,V_datatype"
- "Ti,R,V_deviceCapability"
- "Ti,R,V_directionality"
- "Ti,R,V_enabledPopulation"
- "Ti,R,V_mode"
- "Ti,R,V_obfuscation"
- "Ti,R,V_privacyClassification"
- "Ti,R,V_storage"
- "Ti,R,V_type"
- "TimeOfCaptureEventMetrics"
- "UIKitMetrics"
- "UTF8String"
- "VMSwapStatisticsMetrics"
- "Vv16@0:8"
- "[John] Cache is not empty and concatenatedPath is %@ and cachedHistoryResult is : %@"
- "^{_NSZone=}16@0:8"
- "^{sqlite3=}24@0:8@16"
- "_DMACompliant"
- "_appIdentifier"
- "_auxiliaryType"
- "_build"
- "_cadence"
- "_cadenceTuples"
- "_cadences"
- "_category"
- "_datatype"
- "_deviceCapability"
- "_directionality"
- "_dmaCompliant"
- "_enabledPopulation"
- "_enumMapping"
- "_enumMaps"
- "_exampleValue"
- "_filterEntryLogging"
- "_fixedArraySize"
- "_groupBy"
- "_groupBys"
- "_has"
- "_key"
- "_metadataHistoryCache"
- "_metricDescription"
- "_metricHistorys"
- "_metricType"
- "_metrics"
- "_metricsByID"
- "_mode"
- "_name"
- "_obfuscation"
- "_privacyClassification"
- "_protoVersion"
- "_rounding"
- "_setError"
- "_source"
- "_storage"
- "_subsystem"
- "_symbol"
- "_timeToLive"
- "_type"
- "_unit"
- "_value"
- "_version"
- "absoluteMeasure"
- "accumulatedNegativeMeasure"
- "accumulatedPositiveMeasure"
- "addAppIdentifier:"
- "addAuxiliaryType:"
- "addCadences:"
- "addCharactersInRange:"
- "addCharactersInString:"
- "addDMACompliant:"
- "addEnumMap:"
- "addEnumMapping:"
- "addFilterEntryLogging:"
- "addFixedArraySize:"
- "addGroupBy:"
- "addGroupingDimensions:"
- "addMetricHistory:"
- "addMetricType:"
- "addMetrics:"
- "addMetricsToCache:"
- "addObject:"
- "addObjectsFromArray:"
- "addOptionalFields:"
- "addRounding:"
- "addSource:"
- "aggregatedPushesMetrics"
- "albumAnimationMetrics"
- "albumMotionMetrics"
- "allDeclMetrics"
- "allDeclMetricsForSubsystem:"
- "allDeclSubsystem"
- "allKeys"
- "allValues"
- "allocWithZone:"
- "alphanumericCharacterSet"
- "amcStatsPerfCountersMetrics"
- "ans2Msp0Metrics"
- "aop2PerformanceMetrics"
- "aop2PowerMetrics"
- "aopExclavePowerMetrics"
- "appiconMetrics"
- "appleDiffusionMetrics"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "assetLoadMetrics"
- "audioAccessoryMetrics"
- "autoAssetDownloadMetrics"
- "autorelease"
- "awdlStateLoggingCadence"
- "awdlStateMetrics"
- "backupRestoreMetrics"
- "batteryConfigMetrics"
- "batteryLoggingCadence"
- "batteryMetrics"
- "batteryShutdownMetrics"
- "boolValue"
- "buddyDataMetrics"
- "buildDeviceMetadata"
- "bytes"
- "cacheFrameworkMetrics"
- "cacheFrameworkMetricsForSubsystem:"
- "cachePlistMetrics"
- "cachePlistMetricsForSubsystem:"
- "cadenceEventSBC"
- "cadenceEventSBC_EventScreenStateChange"
- "cadenceEventXPCWithFrequency:"
- "cadenceInit"
- "cadenceInit_EventSBC"
- "cadencePeriodic:"
- "cadenceTupleWithJSONObject:"
- "cadenceTuples"
- "cadenceWithJSONObject:"
- "cadenceWithProto:"
- "cadencesAtIndex:"
- "cadencesCount"
- "cadencesType"
- "cameraInPocketDecision"
- "canBeConvertedToEncoding:"
- "captureButtonAction"
- "captureButtonConfig"
- "celsius"
- "characterSetWithRange:"
- "checkInSessionMetrics"
- "class"
- "clearCadences"
- "clearEnumMaps"
- "clearGroupBys"
- "clearMetricHistorys"
- "clearMetrics"
- "compileMetrics"
- "configMetrics"
- "configurationMetrics"
- "conformsToProtocol:"
- "consoleModeEnabledMetrics"
- "constructDeviceTypeMetric"
- "containerPath"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "copyTo:"
- "copyWithZone:"
- "countByEnumeratingWithState:objects:count:"
- "cpuCoreConfigMetrics"
- "cpuViolationsMetrics"
- "d"
- "d16@0:8"
- "dataWithJSONObject:options:error:"
- "dcpScanoutStatsMetrics"
- "debugDescription"
- "defaultManager"
- "deltaMeasure"
- "description"
- "deviceCapabilityMetrics"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithPropertiesOfPPSMetric:"
- "dimensionless"
- "displayLoggingCadence"
- "displayMetricsWithStorage:timeToLive:category:"
- "doubleValue"
- "edrRequestMetrics"
- "enumMapAtIndex:"
- "enumMapType"
- "enumMappingToProto:"
- "enumMappingWithProto:"
- "enumMaps"
- "enumMapsCount"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "eventMetrics"
- "eyeTrackingMetrics"
- "fileExistsAtPath:isDirectory:"
- "fileResidentRatioMetrics"
- "fileURLWithPath:isDirectory:"
- "firstObject"
- "genericDimension"
- "geoFenceTriggerMetrics"
- "getAllFrameworkSubsystem"
- "getAllSubsystem"
- "getBytes:range:"
- "getCategoriesForFilepath:subsystem:"
- "getMetadataByCategoryForSubsystem:"
- "getMetadataByNameForSubsystem:category:"
- "getMetadataForConcatenatedString:"
- "getMetadataForSubsystem:"
- "getMetadataForSubsystem:category:"
- "getMetadataForSubsystem:category:name:"
- "getMetadataHistoryForFilepath:subsystem:category:"
- "getMetadataHistoryForFilepath:subsystem:category:name:"
- "getSubsystemsForFilepath:"
- "gpuStatsGpuPowerControllerStatesMetrics"
- "grams"
- "groupByAtIndex:"
- "groupByToProto:"
- "groupByType"
- "groupByWithProto:"
- "groupBys"
- "groupBysCount"
- "handwritingModelInferenceMetrics"
- "handwritingModelLoadMetrics"
- "hasAppIdentifier"
- "hasAuxiliaryType"
- "hasBuild"
- "hasCadence"
- "hasCategory"
- "hasDatatype"
- "hasDeviceCapability"
- "hasDirectionality"
- "hasDmaCompliant"
- "hasEnabledPopulation"
- "hasEnumMapping"
- "hasError"
- "hasExampleValue"
- "hasFilterEntryLogging"
- "hasFixedArraySize"
- "hasGroupBy"
- "hasKey"
- "hasMetricDescription"
- "hasMetricType"
- "hasMode"
- "hasName"
- "hasObfuscation"
- "hasPrivacyClassification"
- "hasProtoVersion"
- "hasRounding"
- "hasSource"
- "hasStorage"
- "hasSubsystem"
- "hasSymbol"
- "hasTimeToLive"
- "hasType"
- "hasUnit"
- "hasValue"
- "hasVersion"
- "hash"
- "histogramMetrics"
- "i16@0:8"
- "idleTimerStateMetrics"
- "ihaConsentMetrics"
- "inferenceMetrics"
- "init"
- "initWithArray:"
- "initWithBytes:length:"
- "initWithCadenceTuples:"
- "initWithCadenceType:value:"
- "initWithCapacity:"
- "initWithCategory:value:"
- "initWithContentsOfURL:"
- "initWithData:"
- "initWithDouble:"
- "initWithLongLong:"
- "initWithName:subsystem:category:version:datatype:unit:cadence:directionality:storage:timeToLive:mode:deviceCapability:population:obfuscation:privacyClassification:optionalPayload:"
- "initWithName:version:datatype:unit:baseMetric:optionalPayload:"
- "initWithName:version:datatype:unit:mode:baseMetric:optionalPayload:"
- "initWithSymbol:"
- "initWithType:value:"
- "initWithUTF8String:"
- "initWithUnit:"
- "intValue"
- "integerValue"
- "intelligencePlatformViewUpdateMetrics"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isValidAppIdentifier:"
- "isValidAuxiliaryType:"
- "isValidBuild:"
- "isValidCadenceJSON:"
- "isValidCadenceTupleJSON:"
- "isValidCategory:"
- "isValidDMACompliant:"
- "isValidDatatype:"
- "isValidDeviceCapability:"
- "isValidDirectionality:"
- "isValidEnumDeclaration:"
- "isValidEnumDeclarationJSON:"
- "isValidFilterEntryLogging:"
- "isValidFixedArraySize:"
- "isValidGroupingDimensions:"
- "isValidGroupingDimensionsJSON:"
- "isValidJSONObject:"
- "isValidMetricJSON:"
- "isValidMetricType:"
- "isValidMetricType:value:"
- "isValidMetricTypeJSON:"
- "isValidMode:"
- "isValidName:"
- "isValidObfuscation:"
- "isValidOptionalPayload:"
- "isValidPopulation:"
- "isValidPrivacyClassification:"
- "isValidRounding:"
- "isValidRounding:value:"
- "isValidRoundingJSON:"
- "isValidSource:"
- "isValidSourceJSON:"
- "isValidStorage:"
- "isValidSubsystem:"
- "isValidTTL:"
- "isValidUnitJSON:"
- "isValidVersion:"
- "ispIopStateMetrics"
- "ispIspEventsMetrics"
- "json"
- "jsonDataWithMetrics:"
- "kilobytes"
- "layerCountMetrics"
- "length"
- "linkAdvisoryMetrics"
- "loadMetricsForSubsystem:"
- "localeMetrics"
- "longValue"
- "lowercaseString"
- "mailCategorizationEnabledMetrics"
- "mailCategorizationMetrics"
- "mailIMAPMetrics"
- "mailSyncMetrics"
- "megabytes"
- "mergeFrom:"
- "messageMetricDump"
- "messageTranscriptForegroundMetrics"
- "messageTriggerDump"
- "metadataHistoryCache"
- "metricDeclMap"
- "metricHistoryAtIndex:"
- "metricHistoryType"
- "metricHistorys"
- "metricHistorysCount"
- "metricTypeWithJSONObject:"
- "metricTypeWithProto:"
- "metricWithJSONObject:"
- "metricWithProto:"
- "metricWithProto:withBuild:"
- "metricsAtIndex:"
- "metricsByID"
- "metricsCount"
- "metricsType"
- "metricsWithJSONData:"
- "metricsWithPlist:subsystem:"
- "microWattHours"
- "microseconds"
- "milliAmpereHours"
- "milliAmperes"
- "milliVolts"
- "milliWatts"
- "milliampereHours"
- "milliamperes"
- "milliseconds"
- "millivolts"
- "milliwatts"
- "minutes"
- "mmExecuteRequestMetrics"
- "modeChange"
- "modelLoadMetrics"
- "modelUnLoadMetrics"
- "motionCuesEnabledMetrics"
- "mutableCopy"
- "nanoseconds"
- "newInstanceModelLoadMetrics"
- "newInstanceModelUnLoadMetrics"
- "numberOfMatchesInString:options:range:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offscreenReasonMetrics"
- "ongoingRestoreMetrics"
- "openReadConnection:"
- "optInMetrics"
- "path"
- "performQuery:conn:"
- "performReadQuery:conn:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "photosGenerativeEditMetrics"
- "plistMetricsFromDir:"
- "plistMetricsFromDir:forSubsystem:"
- "pmpDcsCeilingMetrics"
- "pmpDcsFloorMetrics:"
- "pmpPmcAveFloorMetrics"
- "pmpPmcDcsFloorMetrics:"
- "pmpPmcDispFloorMetrics"
- "pmpPmcRmbsMetrics"
- "pmpPmcSocFloorMetrics:"
- "pmpSocFloorMetrics:"
- "position"
- "powerExceptionsDetectionMetrics"
- "predictedContextInferenceMetrics"
- "predictedContextTrainingMetrics"
- "proto"
- "protoData"
- "pubSubMetrics"
- "q40@0:8@16@24^{sqlite3=}32"
- "queryCategoriesForFilepath:subsystem:"
- "queryIDForSubsystem:category:conn:"
- "queryMetadataForFKID:conn:"
- "queryMetadataForFKID:name:conn:"
- "queryMetadataHistoryForFilepath:subsystem:category:"
- "queryMetadataHistoryForFilepath:subsystem:category:name:"
- "querySubsystemsForFilepath:"
- "railEnergyPMUMetrics"
- "rcsRegisterKeepAliveMetrics"
- "rcsSessionManagementMetrics"
- "readFrom:"
- "regularExpressionWithPattern:options:error:"
- "release"
- "relevanceContextUpdate"
- "remoteControlSessionMetrics"
- "removeAllObjects"
- "renderPassCountMetrics"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "roundDown"
- "roundNearest"
- "roundUp"
- "roundingWithJSONObject:"
- "roundingWithProto:"
- "seconds"
- "secureIndicatorActiveIntervalTypeMetrics"
- "secureIndicatorTypeMetrics"
- "self"
- "sensorUsageMetrics"
- "setAppIdentifier:"
- "setAuxiliaryType:"
- "setBuild:"
- "setCadence:"
- "setCadences:"
- "setCategory:"
- "setDatatype:"
- "setDeviceCapability:"
- "setDirectionality:"
- "setDmaCompliant:"
- "setEnabledPopulation:"
- "setEnumMapping:"
- "setEnumMaps:"
- "setExampleValue:"
- "setFilterEntryLogging:"
- "setFixedArraySize:"
- "setGroupBy:"
- "setGroupBys:"
- "setHasAppIdentifier:"
- "setHasAuxiliaryType:"
- "setHasCategory:"
- "setHasDatatype:"
- "setHasDeviceCapability:"
- "setHasDirectionality:"
- "setHasDmaCompliant:"
- "setHasEnabledPopulation:"
- "setHasFilterEntryLogging:"
- "setHasFixedArraySize:"
- "setHasMode:"
- "setHasObfuscation:"
- "setHasPrivacyClassification:"
- "setHasProtoVersion:"
- "setHasStorage:"
- "setHasTimeToLive:"
- "setHasType:"
- "setHasValue:"
- "setHasVersion:"
- "setKey:"
- "setMetadataDefaults:"
- "setMetadataForConcatenatedString:result:"
- "setMetadataHistoryCache:"
- "setMetricDescription:"
- "setMetricHistorys:"
- "setMetricType:"
- "setMetrics:"
- "setMetricsByID:"
- "setMode:"
- "setName:"
- "setObfuscation:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptionalFields:"
- "setPosition:"
- "setPrivacyClassification:"
- "setProtoVersion:"
- "setRounding:"
- "setSource:"
- "setStorage:"
- "setSubsystem:"
- "setSymbol:"
- "setTimeToLive:"
- "setType:"
- "setUnit:"
- "setValue:"
- "setValue:forKey:"
- "setVersion:"
- "sharedStore"
- "singMetrics"
- "smartReplySessionMetrics"
- "smcAccumulatedKeyValueMetrics"
- "smcAccumulatedLookUpMetrics"
- "smcInstantKeyValueMetrics"
- "smcInstantLookUpMetrics"
- "smcOLEDDisplayPowerMetrics"
- "smcPowerDeliveryCLVRMetrics"
- "socStatsDeviceStatesMetrics"
- "socStatsEventsMetrics"
- "socStatsIdsFuseMetrics"
- "socStatsOprtpMetrics"
- "socStatsPmgrCountersMetrics"
- "songTransitionMetrics"
- "sourceToProto:"
- "sourceWithProto:"
- "springfieldUsageMetrics"
- "stateDimension"
- "stringByAppendingString:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "summarizationMetrics"
- "superclass"
- "sysdiagnoseEventMetrics"
- "telephonyActivity"
- "telephonyRegistration"
- "tgiExecuteRequestMetrics"
- "timeOffsetCadence"
- "timeOffsetMetrics"
- "timezoneLoggingCadence"
- "timezoneMetrics"
- "triggerEventMetrics"
- "unitWithJSONObject:"
- "unitWithProto:"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v2AssetDownloadMetrics"
- "v32@0:8@16@24"
- "valueForKey:"
- "vkDataScannerMetrics"
- "volts"
- "watts"
- "writeTo:"
- "zone"
- "zoomEnabledMetrics"
- "{?=\"protoVersion\"b1}"
- "{?=\"value\"b1\"category\"b1}"
- "{?=\"value\"b1\"type\"b1}"
- "{?=\"version\"b1\"appIdentifier\"b1\"auxiliaryType\"b1\"datatype\"b1\"deviceCapability\"b1\"directionality\"b1\"enabledPopulation\"b1\"fixedArraySize\"b1\"mode\"b1\"obfuscation\"b1\"privacyClassification\"b1\"storage\"b1\"timeToLive\"b1\"dmaCompliant\"b1\"filterEntryLogging\"b1}"

```
