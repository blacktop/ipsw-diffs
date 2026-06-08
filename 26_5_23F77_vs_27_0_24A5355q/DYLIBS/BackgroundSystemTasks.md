## BackgroundSystemTasks

> `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`

```diff

-2109.120.16.0.0
-  __TEXT.__text: 0x1444c
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x12d4
-  __TEXT.__const: 0x110
-  __TEXT.__cstring: 0xabc
-  __TEXT.__oslogstring: 0x20b3
-  __TEXT.__gcc_except_tab: 0x6dc
-  __TEXT.__unwind_info: 0x5d0
-  __TEXT.__objc_classname: 0x266
-  __TEXT.__objc_methname: 0x3f46
-  __TEXT.__objc_methtype: 0x53d
-  __TEXT.__objc_stubs: 0x2700
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x698
+2463.0.0.502.1
+  __TEXT.__text: 0x13508
+  __TEXT.__objc_methlist: 0x13bc
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0xb8f
+  __TEXT.__oslogstring: 0x2209
+  __TEXT.__gcc_except_tab: 0x414
+  __TEXT.__unwind_info: 0x538
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x690
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc90
+  __DATA_CONST.__objc_selrefs: 0xd28
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0xf20
-  __AUTH_CONST.__objc_const: 0x28c0
-  __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x208
-  __DATA.__objc_ivar: 0x1f4
+  __DATA_CONST.__got: 0x160
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x1120
+  __AUTH_CONST.__objc_const: 0x29e0
+  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x20c
   __DATA.__data: 0x1e0
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x3e8
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E5D0F34-FD24-3776-9D65-20E788C8D77B
-  Functions: 531
-  Symbols:   1931
-  CStrings:  1149
+  UUID: 01FD1166-1758-3D76-AB62-E6E457D5266E
+  Functions: 551
+  Symbols:   1984
+  CStrings:  435
 
Symbols:
+ +[BGSystemTaskRequest primaryDomainFromString:identifier:]
+ +[BGSystemTaskRequest primaryDomainFromString:identifier:].cold.1
+ +[BGSystemTaskRequest primaryDomainFromString:identifier:].cold.2
+ +[BGSystemTaskRequest purposeFromString:identifier:]
+ +[BGSystemTaskRequest purposeFromString:identifier:].cold.1
+ +[BGSystemTaskRequest secondaryDomainsFromXPCArray:identifier:]
+ +[BGSystemTaskRequest stringArrayFromSecondaryDomains:]
+ +[BGSystemTaskRequest stringFromDomain:]
+ +[BGSystemTaskRequest stringFromPurpose:]
+ +[BGSystemTaskRequest taskRequestWithDescriptor:withIdentifier:].cold.14
+ -[BGNonRepeatingSystemTaskRequest .cxx_destruct]
+ -[BGNonRepeatingSystemTaskRequest primaryDomain]
+ -[BGNonRepeatingSystemTaskRequest purpose]
+ -[BGNonRepeatingSystemTaskRequest secondaryDomains]
+ -[BGNonRepeatingSystemTaskRequest setPrimaryDomain:]
+ -[BGNonRepeatingSystemTaskRequest setPurpose:]
+ -[BGNonRepeatingSystemTaskRequest setSecondaryDomains:]
+ -[BGSystemTask expirationHandlerWithReasonMask]
+ -[BGSystemTask expirationReasonMask]
+ -[BGSystemTask handleExpirationWithReasonMask:]
+ -[BGSystemTask invokeExpirationHandlerWithReasonMask:]
+ -[BGSystemTask invokeExpirationHandlerWithReasonMask:].cold.1
+ -[BGSystemTask setExpirationHandlerWithReasonMask:]
+ -[BGSystemTask setExpirationReasonMask:]
+ -[BGSystemTaskThroughputMetrics endCPUTime]
+ -[BGSystemTaskThroughputMetrics setEndCPUTime:]
+ -[BGSystemTaskThroughputMetrics setStartCPUTime:]
+ -[BGSystemTaskThroughputMetrics startCPUTime]
+ _OBJC_IVAR_$_BGNonRepeatingSystemTaskRequest._primaryDomain
+ _OBJC_IVAR_$_BGNonRepeatingSystemTaskRequest._purpose
+ _OBJC_IVAR_$_BGNonRepeatingSystemTaskRequest._secondaryDomains
+ _OBJC_IVAR_$_BGSystemTask._expirationHandlerWithReasonMask
+ _OBJC_IVAR_$_BGSystemTask._expirationReasonMask
+ _OBJC_IVAR_$_BGSystemTaskThroughputMetrics._endCPUTime
+ _OBJC_IVAR_$_BGSystemTaskThroughputMetrics._startCPUTime
+ ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.93
+ ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.93.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.101
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.101.cold.1
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.107
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99
+ ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.99.cold.1
+ ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.89
+ ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.89.cold.1
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.91
+ ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.91.cold.1
+ ___50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.85
+ ___51-[BGSystemTask setExpirationHandlerWithReasonMask:]_block_invoke
+ ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.124
+ ___58+[BGSystemTaskRequest primaryDomainFromString:identifier:]_block_invoke
+ ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.143
+ ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.141
+ ___63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.92
+ ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.144
+ _clock_gettime_nsec_np
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$endCPUTime
+ _objc_msgSend$expirationReasonMask
+ _objc_msgSend$handleExpirationWithReasonMask:
+ _objc_msgSend$invokeExpirationHandlerWithReasonMask:
+ _objc_msgSend$primaryDomain
+ _objc_msgSend$primaryDomainFromString:identifier:
+ _objc_msgSend$purpose
+ _objc_msgSend$purposeFromString:identifier:
+ _objc_msgSend$reportThroughputMetricsForIdentifier:taskName:itemCount:uptimeDuration:wallClockDuration:qos:workloadCategory:expectedValue:error:
+ _objc_msgSend$secondaryDomains
+ _objc_msgSend$secondaryDomainsFromXPCArray:identifier:
+ _objc_msgSend$setEndCPUTime:
+ _objc_msgSend$setPrimaryDomain:
+ _objc_msgSend$setPurpose:
+ _objc_msgSend$setSecondaryDomains:
+ _objc_msgSend$setStartCPUTime:
+ _objc_msgSend$startCPUTime
+ _objc_msgSend$stringArrayFromSecondaryDomains:
+ _objc_msgSend$stringFromDomain:
+ _objc_msgSend$stringFromPurpose:
+ _objc_msgSend$unregisterSystemTaskWithIdentifier:cancellationReason:completionHandler:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _primaryDomainFromString:identifier:.domainLookupTable
+ _primaryDomainFromString:identifier:.onceToken
- -[BGSystemTask expirationReason]
- -[BGSystemTask handleExpirationWithReason:]
- -[BGSystemTask invokeExpirationHandlerWithReason:]
- -[BGSystemTask invokeExpirationHandlerWithReason:].cold.1
- -[BGSystemTask setExpirationReason:]
- GCC_except_table1
- GCC_except_table161
- GCC_except_table162
- GCC_except_table163
- GCC_except_table164
- GCC_except_table165
- GCC_except_table167
- GCC_except_table168
- GCC_except_table169
- GCC_except_table44
- _OBJC_IVAR_$_BGSystemTask._expirationReason
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.94
- ___48-[BGSystemTaskScheduler resumeScheduling:error:]_block_invoke.94.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.100
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.100.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.103
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.103.cold.1
- ___49-[BGSystemTaskScheduler runTaskWithRegistration:]_block_invoke.109
- ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.90
- ___49-[BGSystemTaskScheduler submitTaskRequest:error:]_block_invoke.90.cold.1
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.92
- ___49-[BGSystemTaskScheduler updateTaskRequest:error:]_block_invoke.92.cold.1
- ___50-[BGSystemTaskScheduler installEventStreamHandler]_block_invoke.86
- ___54-[BGSystemTaskScheduler deregisterTaskWithIdentifier:]_block_invoke.125
- ___58-[BGSystemTaskScheduler systemTask:consumedResults:error:]_block_invoke.144
- ___58-[BGSystemTaskScheduler systemTask:producedResults:error:]_block_invoke.142
- ___63-[BGSystemTaskScheduler cancelTaskRequestWithIdentifier:error:]_block_invoke.93
- ___68-[BGSystemTaskScheduler systemTask:resetResultsForIdentifier:error:]_block_invoke.145
- _objc_msgSend$expirationReason
- _objc_msgSend$handleExpirationWithReason:
- _objc_msgSend$invokeExpirationHandlerWithReason:
- _objc_msgSend$reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:
- _objc_msgSend$requestsApplicationLaunch
- _objc_msgSend$setRequestsApplicationLaunch:
- _objc_msgSend$unregisterSystemTaskWithIdentifier:completionHandler:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%{public}@: BGSystemTaskApplicationRelationshipTypeRequestsApplicationLaunch is deprecated and no longer supported as of Rizz (27.0)"
+ "%{public}@: Invalid domain value '%s', defaulting to Default"
+ "%{public}@: Invalid purpose value '%s', defaulting to Default"
+ "%{public}@: Secondary domains array contains non-NSString element: %{public}@"
+ "%{public}@: requestsApplicationLaunch is deprecated and no longer supported as of Rizz (27.0)"
+ "AIML"
+ "CatchUp"
+ "Default"
+ "Enablement"
+ "Health"
+ "Mail"
+ "Media"
+ "Messages"
+ "Photos"
+ "Preview"
+ "PrimaryDomain"
+ "Proactive"
+ "Purpose"
+ "Received request to expire %@ with reason mask: 0x%llx"
+ "Search"
+ "SecondaryDomains"
+ "SensingConnectivity"
+ "Services"
+ "Siri"
+ "StorageTech"
+ "\xe1"
- "#16@0:8"
- "%{public}@: relatedApplications cannot be empty when requestsApplicationLaunch is set to true"
- ".cxx_destruct"
- "@\"<BGSystemTaskDelegate>\""
- "@\"BGSystemTaskRequest\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_nw_endpoint>\""
- "@\"NSObject<OS_nw_parameters>\""
- "@\"NSObject<OS_os_transaction>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"_DASScheduler\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24@?32"
- "@48@0:8@16@24Q32@40"
- "@56@0:8@16@24@32Q40@48"
- "@64@0:8@16@24Q32@40@48@56"
- "@72@0:8@16@24@32Q40@48@56@64"
- "@?"
- "@?16@0:8"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B24@0:8^@16"
- "B32@0:8@\"BGSystemTask\"16@\"NSString\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8^@16^@24"
- "B32@0:8d16^@24"
- "B40@0:8@\"BGSystemTask\"16@\"NSSet\"24^@32"
- "B40@0:8@\"BGSystemTask\"16@\"NSString\"24^@32"
- "B40@0:8@16@24@?32"
- "B40@0:8@16@24^@32"
- "B40@0:8Q16@24^@32"
- "B40@0:8Q16Q24^@32"
- "B48@0:8Q16Q24@32^@40"
- "B48@0:8Q16Q24Q32@40"
- "B56@0:8Q16Q24Q32@40^@48"
- "B72@0:8@16Q24Q32@40Q48@56^@64"
- "BGFastPassSystemTask"
- "BGFastPassSystemTaskRequest"
- "BGNonRepeatingSystemTask"
- "BGNonRepeatingSystemTaskRequest"
- "BGRepeatingSystemTask"
- "BGRepeatingSystemTaskRequest"
- "BGSystemTask"
- "BGSystemTaskCheckpoints"
- "BGSystemTaskCompletionDependency"
- "BGSystemTaskDelegate"
- "BGSystemTaskDependency"
- "BGSystemTaskPerformanceMetadata"
- "BGSystemTaskProgressMetrics"
- "BGSystemTaskRequest"
- "BGSystemTaskResult"
- "BGSystemTaskResultDependency"
- "BGSystemTaskScheduler"
- "BGSystemTaskSchedulerRegistration"
- "BGSystemTaskSerializableDependency"
- "BGSystemTaskStatus"
- "BGSystemTaskThroughputMetrics"
- "BGSystemTaskWorkload"
- "NSCopying"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Received request to expire %@ with reason: %lu"
- "T#,R"
- "T@\"<BGSystemTaskDelegate>\",W,V_delegate"
- "T@\"BGSystemTaskRequest\",&,N,V_taskRequest"
- "T@\"BGSystemTaskRequest\",R,C,V_taskRequest"
- "T@\"BGSystemTaskScheduler\",R"
- "T@\"NSArray\",&,N,V_featureCodes"
- "T@\"NSArray\",C,N,V_featureCodes"
- "T@\"NSArray\",C,N,V_involvedProcesses"
- "T@\"NSArray\",C,N,V_processingTaskIdentifiers"
- "T@\"NSArray\",C,N,V_relatedApplications"
- "T@\"NSDate\",&,N,V_endTimestamp"
- "T@\"NSDate\",&,N,V_startTimestamp"
- "T@\"NSDictionary\",C,N,V_context"
- "T@\"NSDictionary\",C,N,V_networkEndpoint"
- "T@\"NSDictionary\",C,N,V_networkParameters"
- "T@\"NSMutableDictionary\",&,N,V_pendingTaskRegistrationsMap"
- "T@\"NSMutableDictionary\",&,N,V_preRunningTasksMap"
- "T@\"NSMutableDictionary\",&,N,V_registrations"
- "T@\"NSMutableDictionary\",&,N,V_runningConsumedResults"
- "T@\"NSMutableDictionary\",&,N,V_runningTasksMap"
- "T@\"NSMutableDictionary\",&,N,V_taskProgressInfo"
- "T@\"NSMutableDictionary\",&,N,V_taskToProgressMap"
- "T@\"NSMutableDictionary\",&,N,V_throughputMetricsMap"
- "T@\"NSNumber\",&,N,V_expectedMetricValue"
- "T@\"NSNumber\",&,N,V_itemsCompleted"
- "T@\"NSNumber\",&,N,V_qos"
- "T@\"NSNumber\",&,N,V_totalItemCount"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_generatedLaunchQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_internalQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_performanceMetricQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_registeredLaunchQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_resultQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
- "T@\"NSObject<OS_nw_endpoint>\",&,N,V_networkEndpointPrimitive"
- "T@\"NSObject<OS_nw_parameters>\",&,N,V_networkParametersPrimitive"
- "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
- "T@\"NSObject<OS_xpc_object>\",&,N,V_descriptor"
- "T@\"NSSet\",C,N,V_dependencies"
- "T@\"NSSet\",C,N,V_producedResultIdentifiers"
- "T@\"NSSet\",R,C,N,V_blockingReasons"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_taskName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_dataBudgetName"
- "T@\"NSString\",C,N,V_diskVolume"
- "T@\"NSString\",C,N,V_groupName"
- "T@\"NSString\",C,N,V_processingTaskIdentifier"
- "T@\"NSString\",C,N,V_rateLimitConfigurationName"
- "T@\"NSString\",C,N,V_remoteDevice"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_identifier"
- "T@\"NSString\",R,C,V_identifier"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_identifier"
- "T@\"NSString\",R,N,V_performanceMetricIdentifier"
- "T@\"NSUUID\",R,N,V_reportingUUID"
- "T@\"NSUUID\",R,N,V_uuid"
- "T@\"_DASScheduler\",&,N,V_scheduler"
- "T@?,C,N,V_clientLedExpirationHandler"
- "T@?,C,N,V_completionHandler"
- "T@?,C,N,V_expirationAckHandler"
- "T@?,C,N,V_expirationHandler"
- "T@?,C,N,V_expirationHandlerWithReason"
- "T@?,C,N,V_launchHandler"
- "TB,N,V_appRefresh"
- "TB,N,V_backlogged"
- "TB,N,V_beforeApplicationLaunch"
- "TB,N,V_blockRebootActivitiesForSU"
- "TB,N,V_bypassBatteryAging"
- "TB,N,V_bypassPeakPower"
- "TB,N,V_clampToBGQoS"
- "TB,N,V_communicatesWithPairedDevice"
- "TB,N,V_dataBudgeted"
- "TB,N,V_hasPropagatedExpiration"
- "TB,N,V_isInternalVariant"
- "TB,N,V_magneticInterferenceSensitivity"
- "TB,N,V_mailFetch"
- "TB,N,V_mayRebootDevice"
- "TB,N,V_overrideRateLimiting"
- "TB,N,V_postInstall"
- "TB,N,V_powerBudgeted"
- "TB,N,V_powerNap"
- "TB,N,V_preventsDeviceSleep"
- "TB,N,V_reRun"
- "TB,N,V_requestsApplicationLaunch"
- "TB,N,V_requestsImmediateRuntime"
- "TB,N,V_requiresBuddyComplete"
- "TB,N,V_requiresExternalPower"
- "TB,N,V_requiresExternalPowerIsSetByUser"
- "TB,N,V_requiresInexpensiveNetworkConnectivity"
- "TB,N,V_requiresNetworkConnectivity"
- "TB,N,V_requiresRemoteDeviceWake"
- "TB,N,V_requiresSignificantUserInactivity"
- "TB,N,V_requiresUnconstrainedNetworkConnectivity"
- "TB,N,V_requiresUserInactivity"
- "TB,N,V_requiresUserInactivityIsSetByUser"
- "TB,N,V_resourceIntensive"
- "TB,N,V_runOnAppForeground"
- "TB,N,V_shouldWakeDevice"
- "TB,N,V_useStatisticalModelForTriggersRestart"
- "TB,N,V_userRequestedBackupTask"
- "TB,R,N"
- "TQ,N,V_expirationReason"
- "TQ,N,V_groupConcurrencyLimit"
- "TQ,N,V_itemCount"
- "TQ,N,V_requiresMinimumBatteryLevel"
- "TQ,N,V_requiresMinimumDataBudgetPercentage"
- "TQ,R"
- "TQ,R,N,V_batchSize"
- "TQ,R,N,V_category"
- "TQ,R,N,V_count"
- "Td,N,V_expectedDuration"
- "Td,N,V_interval"
- "Td,N,V_minDurationBetweenInstances"
- "Td,N,V_randomInitialDelay"
- "Td,N,V_scheduleAfter"
- "Td,N,V_trySchedulingBefore"
- "Tq,N,V_applicationRelationship"
- "Tq,N,V_networkDownloadSize"
- "Tq,N,V_networkUploadSize"
- "Tq,N,V_priority"
- "Tq,N,V_requiresProtectionClass"
- "Tq,N,V_resources"
- "Tq,N,V_runOnMotionState"
- "Tq,N,V_semanticVersion"
- "Tq,N,V_targetDevice"
- "Tq,R,N,V_status"
- "Tq,V_state"
- "T{os_unfair_lock_s=I},N,V_lock"
- "UTF8String"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_appRefresh"
- "_applicationRelationship"
- "_backlogged"
- "_batchSize"
- "_beforeApplicationLaunch"
- "_blockRebootActivitiesForSU"
- "_blockingReasons"
- "_bypassBatteryAging"
- "_bypassPeakPower"
- "_category"
- "_clampToBGQoS"
- "_clientLedExpirationHandler"
- "_communicatesWithPairedDevice"
- "_completionHandler"
- "_context"
- "_count"
- "_dataBudgetName"
- "_dataBudgeted"
- "_delegate"
- "_dependencies"
- "_descriptor"
- "_diskVolume"
- "_endTimestamp"
- "_expectedDuration"
- "_expectedMetricValue"
- "_expirationAckHandler"
- "_expirationHandler"
- "_expirationHandlerWithReason"
- "_expirationReason"
- "_featureCodes"
- "_generatedLaunchQueue"
- "_groupConcurrencyLimit"
- "_groupName"
- "_hasPropagatedExpiration"
- "_identifier"
- "_internalQueue"
- "_interval"
- "_involvedProcesses"
- "_isInternalVariant"
- "_itemCount"
- "_itemsCompleted"
- "_launchHandler"
- "_lock"
- "_magneticInterferenceSensitivity"
- "_mailFetch"
- "_mayRebootDevice"
- "_minDurationBetweenInstances"
- "_networkDownloadSize"
- "_networkEndpoint"
- "_networkEndpointPrimitive"
- "_networkParameters"
- "_networkParametersPrimitive"
- "_networkUploadSize"
- "_overrideRateLimiting"
- "_pendingTaskRegistrationsMap"
- "_performanceMetricIdentifier"
- "_performanceMetricQueue"
- "_postInstall"
- "_powerBudgeted"
- "_powerNap"
- "_preRunningTasksMap"
- "_preventsDeviceSleep"
- "_priority"
- "_processingTaskIdentifier"
- "_processingTaskIdentifiers"
- "_producedResultIdentifiers"
- "_qos"
- "_queue"
- "_randomInitialDelay"
- "_rateLimitConfigurationName"
- "_reRun"
- "_registeredLaunchQueue"
- "_registrations"
- "_relatedApplications"
- "_remoteDevice"
- "_reportingUUID"
- "_requestsApplicationLaunch"
- "_requestsImmediateRuntime"
- "_requiresBuddyComplete"
- "_requiresExternalPower"
- "_requiresExternalPowerIsSetByUser"
- "_requiresInexpensiveNetworkConnectivity"
- "_requiresMinimumBatteryLevel"
- "_requiresMinimumDataBudgetPercentage"
- "_requiresNetworkConnectivity"
- "_requiresProtectionClass"
- "_requiresRemoteDeviceWake"
- "_requiresSignificantUserInactivity"
- "_requiresUnconstrainedNetworkConnectivity"
- "_requiresUserInactivity"
- "_requiresUserInactivityIsSetByUser"
- "_resourceIntensive"
- "_resources"
- "_resultQueue"
- "_runOnAppForeground"
- "_runOnMotionState"
- "_runningConsumedResults"
- "_runningTasksMap"
- "_scheduleAfter"
- "_scheduler"
- "_semanticVersion"
- "_shouldWakeDevice"
- "_startTimestamp"
- "_state"
- "_status"
- "_targetDevice"
- "_taskName"
- "_taskProgressInfo"
- "_taskRequest"
- "_taskToProgressMap"
- "_throughputMetricsMap"
- "_totalItemCount"
- "_transaction"
- "_trySchedulingBefore"
- "_useStatisticalModelForTriggersRestart"
- "_userRequestedBackupTask"
- "_uuid"
- "acknowledgeSystemTaskLaunchWithIdentifier:error:"
- "acknowledgeSystemTaskSuspensionWithIdentifier:retryAfter:"
- "activityStartedWithParameters:"
- "activityStoppedWithParameters:"
- "addItemCount:"
- "addObject:"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "appRefresh"
- "applicationRelationship"
- "array"
- "arrayWithObjects:count:"
- "asDASActivityResult"
- "asDictionary"
- "autorelease"
- "backlogged"
- "batchSize"
- "beforeApplicationLaunch"
- "blockRebootActivitiesForSU"
- "blockingReasons"
- "boolValue"
- "bypassBatteryAging"
- "bypassPeakPower"
- "cStringUsingEncoding:"
- "canTaskRegistration:produceResultOfIdentifier:"
- "cancelTaskRequestWithIdentifier:error:"
- "category"
- "clampToBGQoS"
- "class"
- "clearLocked"
- "clientLedExpirationHandler"
- "communicatesWithPairedDevice"
- "compare:"
- "completeSystemTaskWithIdentifier:"
- "completionHandler"
- "conformsToProtocol:"
- "consumedResults:error:"
- "containsObject:"
- "context"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "das_dedup"
- "dataBudgetName"
- "dataBudgeted"
- "debugDescription"
- "defaultManager"
- "delegate"
- "delegate:"
- "dependencies"
- "deregisterTaskWithIdentifier:"
- "deregisterThroughputTrackingFor:withEndTime:error:"
- "description"
- "descriptionInStringsFileFormat"
- "descriptor"
- "descriptorWithTaskRequest:"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "diskVolume"
- "duration"
- "eligibleToRun"
- "endTimestamp"
- "errorWithDomain:code:userInfo:"
- "exemptTask:"
- "expectedDuration"
- "expectedMetricValue"
- "expirationAckHandler"
- "expirationHandler"
- "expirationHandlerWithReason"
- "expireTaskWithRegistration:withReason:"
- "expiring"
- "featureCodes"
- "fileExistsAtPath:isDirectory:"
- "generatedLaunchQueue"
- "getSubmittedSystemTaskRequests:error:"
- "getSubmittedSystemTaskRequestsWithCompletionHandler:"
- "getTaskStatusForIdentifier:completionHandler:"
- "groupConcurrencyLimit"
- "groupName"
- "handleClientFailedtoExpireTaskWithIdentifier:completionHandler:"
- "handleClientLedSystemTaskExpirationWithIdentifier:retryAfter:completionHandler:"
- "handleDeniedTaskLaunch:"
- "handleExpirationWithReason:"
- "hasPropagatedExpiration"
- "hasValidExpirationHandler"
- "hash"
- "init"
- "initWithIdentifier:"
- "initWithIdentifier:batchSize:"
- "initWithIdentifier:consumptionCount:"
- "initWithIdentifier:count:"
- "initWithIdentifier:cumulativeProductionCount:"
- "initWithIdentifier:launchQueue:launchHandler:"
- "initWithIdentifier:qos:workloadCategory:expectedMetricValue:"
- "initWithIdentifier:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
- "initWithIdentifier:queue:"
- "initWithIdentifier:queue:taskRequest:"
- "initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:"
- "initWithIdentifier:taskName:qos:workloadCategory:expectedMetricValue:itemsCompleted:totalItemCount:"
- "initWithStartDate:endDate:"
- "initialize"
- "installEventStreamHandler"
- "installResubmissionHandler"
- "intValue"
- "integerValue"
- "internalQueue"
- "interval"
- "invalid"
- "invokeExpirationHandlerWithReason:"
- "involvedProcesses"
- "isEqual:"
- "isEqualToString:"
- "isInternalVariant"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSubsetOfSet:"
- "itemCount"
- "itemsCompleted"
- "launchHandler"
- "length"
- "lock"
- "logger"
- "magneticInterferenceSensitivity"
- "mailFetch"
- "mayRebootDevice"
- "minDurationBetweenInstances"
- "networkDownloadSize"
- "networkEndpoint"
- "networkEndpointPrimitive"
- "networkParameters"
- "networkParametersPrimitive"
- "networkUploadSize"
- "now"
- "numberWithBool:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operatingSystemVersion"
- "orderedSetWithArray:"
- "overrideRateLimiting"
- "pendingTaskRegistrationsMap"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performanceMetricIdentifier"
- "performanceMetricQueue"
- "postInstall"
- "powerBudgeted"
- "powerNap"
- "preRunningTasksMap"
- "prepareForRunning"
- "preventsDeviceSleep"
- "priority"
- "processEvent:forRegistration:"
- "processInfo"
- "processingTaskIdentifier"
- "processingTaskIdentifiers"
- "producedCumulativeResults:error:"
- "producedResultIdentifiers"
- "q16@0:8"
- "qos"
- "queue"
- "queue_reportBufferedTaskWorkloadProgress"
- "queue_reportThroughputForPerformanceMetric:error:"
- "randomInitialDelay"
- "rateLimitConfigurationName"
- "reRun"
- "registerForTaskWithIdentifier:usingQueue:launchHandler:"
- "registerThroughputTrackingFor:withStartTime:error:"
- "registeredLaunchQueue"
- "registrations"
- "relatedApplications"
- "release"
- "remoteDevice"
- "removeObjectForKey:"
- "reportCumulativeResultConsumptionWithError:"
- "reportCustomCheckpoint:forTask:error:"
- "reportFeatureCheckpoint:forFeature:atDate:error:"
- "reportFeatureCheckpoint:forFeature:error:"
- "reportPendingThroughputMetrics"
- "reportProgressForTaskWithName:withGlobalTarget:completed:atDate:category:subCategory:error:"
- "reportProgressMetrics:error:"
- "reportProgressMetricsForIdentifier:taskName:itemsCompleted:totalItemCount:qos:workloadCategory:expectedValue:error:"
- "reportSystemTaskWithIdentifier:consumedResults:completionHandler:"
- "reportSystemTaskWithIdentifier:producedResults:completionHandler:"
- "reportSystemWorkload:ofCategory:error:"
- "reportTaskWorkloadProgress:completed:category:subCategory:error:"
- "reportTaskWorkloadProgress:target:completed:category:subCategory:completionHandler:"
- "reportThroughputMetricsForIdentifier:taskName:itemCount:totalDuration:qos:workloadCategory:expectedValue:error:"
- "reportingUUID"
- "requestsApplicationLaunch"
- "requestsImmediateRuntime"
- "requiresBuddyComplete"
- "requiresExternalPower"
- "requiresExternalPowerIsSetByUser"
- "requiresInexpensiveNetworkConnectivity"
- "requiresMinimumBatteryLevel"
- "requiresMinimumDataBudgetPercentage"
- "requiresNetworkConnectivity"
- "requiresProtectionClass"
- "requiresRemoteDeviceWake"
- "requiresSignificantUserInactivity"
- "requiresUnconstrainedNetworkConnectivity"
- "requiresUserInactivity"
- "requiresUserInactivityIsSetByUser"
- "resetResultsForIdentifier:byTaskWithIdentifier:completionHandler:"
- "resetResultsForIdentifier:error:"
- "resourceIntensive"
- "resources"
- "respondsToSelector:"
- "resubmitRunningTasks:"
- "resultQueue"
- "resultQueue_aggregateConsumedResult:"
- "resultQueue_containsPendingConsumedResults"
- "resumeScheduling:error:"
- "resumeTaskSchedulingWithIdentifier:completionHandler:"
- "retain"
- "retainCount"
- "runOnAppForeground"
- "runOnMotionState"
- "runTaskWithRegistration:"
- "runningConsumedResults"
- "runningTasksMap"
- "scheduleAfter"
- "scheduler"
- "schedulerWithClientName:"
- "self"
- "semanticVersion"
- "sendTaskWorkloadProgressToPPS:completed:category:subCategory:"
- "set"
- "setAppRefresh:"
- "setApplicationRelationship:"
- "setBacklogged:"
- "setBeforeApplicationLaunch:"
- "setBlockRebootActivitiesForSU:"
- "setBypassBatteryAging:"
- "setBypassPeakPower:"
- "setClampToBGQoS:"
- "setClientLedExpirationHandler:"
- "setCommunicatesWithPairedDevice:"
- "setCompletionHandler:"
- "setContext:"
- "setDataBudgetName:"
- "setDataBudgeted:"
- "setDelegate:"
- "setDependencies:"
- "setDescriptor:"
- "setDiskVolume:"
- "setEndTimestamp:"
- "setExpectedDuration:"
- "setExpectedMetricValue:"
- "setExpirationAckHandler:"
- "setExpirationHandler:"
- "setExpirationHandlerWithReason:"
- "setExpirationReason:"
- "setFeatureCodes:"
- "setGeneratedLaunchQueue:"
- "setGroupConcurrencyLimit:"
- "setGroupName:"
- "setHasPropagatedExpiration:"
- "setIdentifier:"
- "setInternalQueue:"
- "setInterval:"
- "setInvolvedProcesses:"
- "setIsInternalVariant:"
- "setItemCount:"
- "setItemsCompleted:"
- "setLaunchHandler:"
- "setLock:"
- "setMagneticInterferenceSensitivity:"
- "setMailFetch:"
- "setMayRebootDevice:"
- "setMinDurationBetweenInstances:"
- "setNetworkDownloadSize:"
- "setNetworkEndpoint:"
- "setNetworkEndpointPrimitive:"
- "setNetworkParameters:"
- "setNetworkParametersPrimitive:"
- "setNetworkUploadSize:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOverrideRateLimiting:"
- "setPendingTaskRegistrationsMap:"
- "setPerformanceMetricQueue:"
- "setPostInstall:"
- "setPowerBudgeted:"
- "setPowerNap:"
- "setPreRunningTasksMap:"
- "setPreventsDeviceSleep:"
- "setPriority:"
- "setProcessingTaskIdentifier:"
- "setProcessingTaskIdentifiers:"
- "setProducedResultIdentifiers:"
- "setQos:"
- "setQueue:"
- "setRandomInitialDelay:"
- "setRateLimitConfigurationName:"
- "setReRun:"
- "setRegisteredLaunchQueue:"
- "setRegistrations:"
- "setRelatedApplications:"
- "setRemoteDevice:"
- "setRequestsApplicationLaunch:"
- "setRequestsImmediateRuntime:"
- "setRequiresBuddyComplete:"
- "setRequiresExternalPower:"
- "setRequiresExternalPowerIsSetByUser:"
- "setRequiresInexpensiveNetworkConnectivity:"
- "setRequiresMinimumBatteryLevel:"
- "setRequiresMinimumDataBudgetPercentage:"
- "setRequiresNetworkConnectivity:"
- "setRequiresProtectionClass:"
- "setRequiresRemoteDeviceWake:"
- "setRequiresSignificantUserInactivity:"
- "setRequiresUnconstrainedNetworkConnectivity:"
- "setRequiresUserInactivity:"
- "setRequiresUserInactivityIsSetByUser:"
- "setResourceIntensive:"
- "setResources:"
- "setResultQueue:"
- "setRunOnAppForeground:"
- "setRunOnMotionState:"
- "setRunningConsumedResults:"
- "setRunningTasksMap:"
- "setScheduleAfter:"
- "setScheduler:"
- "setSemanticVersion:"
- "setShouldWakeDevice:"
- "setStartTimestamp:"
- "setState:"
- "setTargetDevice:"
- "setTaskCompleted"
- "setTaskExpiredWithRetryAfter:error:"
- "setTaskName:"
- "setTaskProgressInfo:"
- "setTaskRequest:"
- "setTaskToProgressMap:"
- "setThroughputMetricsMap:"
- "setTotalItemCount:"
- "setTransaction:"
- "setTrySchedulingBefore:"
- "setUseStatisticalModelForTriggersRestart:"
- "setUserRequestedBackupTask:"
- "setWithArray:"
- "setWithObjects:"
- "sharedInstance"
- "sharedScheduler"
- "shouldBeDataBudgeted"
- "shouldReportTaskWorkloadProgress:"
- "shouldWakeDevice"
- "startTimestamp"
- "state"
- "status"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "submitTaskRequest:error:"
- "submitTaskRequestWithIdentifier:descriptor:completionHandler:"
- "superclass"
- "suspensionExemptionsForActivity:"
- "suspensionThreshold"
- "suspensionThresholdForTask:"
- "systemTask:canConsumeResultOfIdentifier:"
- "systemTask:consumedResults:error:"
- "systemTask:producedResults:error:"
- "systemTask:resetResultsForIdentifier:error:"
- "targetDevice"
- "taskName"
- "taskProgressInfo"
- "taskRequest"
- "taskRequestForIdentifier:"
- "taskRequestWithDescriptor:withIdentifier:"
- "taskStartedWithParameters:error:"
- "taskStoppedWithParameters:error:"
- "taskToProgressMap"
- "throughputMetricsMap"
- "timeIntervalSinceDate:"
- "totalItemCount"
- "transaction"
- "trySchedulingBefore"
- "unregisterSystemTaskWithIdentifier:completionHandler:"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "updateSystemConstraintsWithParameters:"
- "updateTaskRequest:error:"
- "updateTaskRequestWithIdentifier:descriptor:completionHandler:"
- "useStatisticalModelForTriggersRestart"
- "userRequestedBackupTask"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8{os_unfair_lock_s=I}16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "validateFeatureCheckpoint:"
- "zone"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "{os_unfair_lock_s=I}16@0:8"
- "\xd1"

```
