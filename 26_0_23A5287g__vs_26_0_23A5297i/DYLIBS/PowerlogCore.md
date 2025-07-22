## PowerlogCore

> `/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`

```diff

-2964.0.64.0.0
-  __TEXT.__text: 0xd9b10
-  __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_methlist: 0x8860
-  __TEXT.__const: 0x1830
-  __TEXT.__cstring: 0x3a824
-  __TEXT.__oslogstring: 0x76b1
-  __TEXT.__gcc_except_tab: 0x28b0
-  __TEXT.__unwind_info: 0x2d60
-  __TEXT.__objc_classname: 0x8a7
-  __TEXT.__objc_methname: 0x12df7
-  __TEXT.__objc_methtype: 0x1890
-  __TEXT.__objc_stubs: 0xf800
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x2470
-  __DATA_CONST.__objc_classlist: 0x338
+2964.0.107.502.1
+  __TEXT.__text: 0xdd088
+  __TEXT.__auth_stubs: 0x1ad0
+  __TEXT.__objc_methlist: 0x8a58
+  __TEXT.__const: 0x1888
+  __TEXT.__cstring: 0x3af0f
+  __TEXT.__oslogstring: 0x7d8e
+  __TEXT.__gcc_except_tab: 0x29e4
+  __TEXT.__unwind_info: 0x2e18
+  __TEXT.__objc_classname: 0x90f
+  __TEXT.__objc_methname: 0x13070
+  __TEXT.__objc_methtype: 0x1909
+  __TEXT.__objc_stubs: 0xfb00
+  __DATA_CONST.__got: 0x798
+  __DATA_CONST.__const: 0x2580
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_nlclslist: 0x80
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x50c8
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x3ccc0
-  __AUTH_CONST.__auth_got: 0xd78
-  __AUTH_CONST.__const: 0x22e0
-  __AUTH_CONST.__cfstring: 0x5e6c0
-  __AUTH_CONST.__objc_const: 0x9070
+  __DATA_CONST.__objc_selrefs: 0x5170
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x3d138
+  __AUTH_CONST.__auth_got: 0xd80
+  __AUTH_CONST.__const: 0x23a0
+  __AUTH_CONST.__cfstring: 0x5f1c0
+  __AUTH_CONST.__objc_const: 0x9440
   __AUTH_CONST.__objc_intobj: 0x4800
-  __AUTH_CONST.__objc_doubleobj: 0x10c0
+  __AUTH_CONST.__objc_doubleobj: 0x10d0
   __AUTH_CONST.__objc_arrayobj: 0x1158
-  __AUTH_CONST.__objc_dictobj: 0xec90
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0x630
-  __DATA.__data: 0x440
-  __DATA.__bss: 0x1719
+  __AUTH_CONST.__objc_dictobj: 0xed58
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x654
+  __DATA.__data: 0x4a0
+  __DATA.__bss: 0x1739
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__data: 0x24

   - /System/Library/PrivateFrameworks/AppleBasebandManager.framework/AppleBasebandManager
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/DiagnosticExtensions
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsystemstats.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 083BA9F8-0DF3-35E9-AD23-426DF5EE0FCE
-  Functions: 4512
-  Symbols:   15793
-  CStrings:  29117
+  UUID: 34A54EF4-F419-314F-874E-16BF20BE6D07
+  Functions: 4589
+  Symbols:   16039
+  CStrings:  29375
 
Symbols:
+ +[PLUtilities getDefaultL0bThresholdForDeviceType]
+ +[PLUtilities getDefaultL0bThresholdForDeviceType].cold.1
+ +[PLUtilities getDefaultL0bThresholdForDeviceType].cold.2
+ +[PLUtilities getDefaultL0bThresholdForDeviceType].cold.3
+ +[PLUtilities getDefaultL0bThresholdForDeviceType].cold.4
+ +[PLUtilities getDefaultL0bThresholdForDeviceType].cold.5
+ +[PLUtilities getOverridableMonotonicNow]
+ +[PPSSignpostController _workQueue]
+ +[PPSSignpostController registerDataCollectionActivity]
+ +[PPSSignpostController registerDataCollectionActivity].cold.1
+ +[PPSSignpostController unregisterDataCollectionActivity]
+ +[PPSSignpostServiceRequest supportsSecureCoding]
+ -[PLSubmissionConfig conditionCheckForAppIntents]
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.2
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.3
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.4
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.5
+ -[PLSubmissionFileSP copyAndPrepareLog].cold.6
+ -[PLXPCRelay handlePeer:forEvent:].cold.16
+ -[PLXPCRelay handlePeer:forEvent:].cold.17
+ -[PLXPCRelay handlePeer:forEvent:].cold.18
+ -[PLXPCRelay handlePeer:forEvent:].cold.19
+ -[PLXPCRelay setXpcConnection:]
+ -[PLXPCRelay startRelay].cold.1
+ -[PLXPCRelay stopRelay].cold.1
+ -[PLXPCRelay xpcConnection]
+ -[PPSSafeguardController handleTask:].cold.1
+ -[PPSSignpostController .cxx_destruct]
+ -[PPSSignpostController _clearState]
+ -[PPSSignpostController _handleTask:]
+ -[PPSSignpostController _handleTask:].cold.1
+ -[PPSSignpostController _lastCollectionDate]
+ -[PPSSignpostController _performWithStartDate:endDate:]
+ -[PPSSignpostController _performWithStartDate:endDate:].cold.1
+ -[PPSSignpostController connection]
+ -[PPSSignpostController generateForTimeRange:]
+ -[PPSSignpostController init]
+ -[PPSSignpostController setConnection:]
+ -[PPSSignpostServiceConnection .cxx_destruct]
+ -[PPSSignpostServiceConnection connectionToServer]
+ -[PPSSignpostServiceConnection init]
+ -[PPSSignpostServiceConnection invalidate]
+ -[PPSSignpostServiceConnection service]
+ -[PPSSignpostServiceConnection setConnectionToServer:]
+ -[PPSSignpostServiceRequest .cxx_destruct]
+ -[PPSSignpostServiceRequest description]
+ -[PPSSignpostServiceRequest encodeWithCoder:]
+ -[PPSSignpostServiceRequest endDate]
+ -[PPSSignpostServiceRequest initWithCoder:]
+ -[PPSSignpostServiceRequest init]
+ -[PPSSignpostServiceRequest setEndDate:]
+ -[PPSSignpostServiceRequest setSourceURL:]
+ -[PPSSignpostServiceRequest setStartDate:]
+ -[PPSSignpostServiceRequest setType:]
+ -[PPSSignpostServiceRequest setUuid:]
+ -[PPSSignpostServiceRequest sourceURL]
+ -[PPSSignpostServiceRequest startDate]
+ -[PPSSignpostServiceRequest type]
+ -[PPSSignpostServiceRequest uuid]
+ GCC_except_table168
+ GCC_except_table40
+ _OBJC_CLASS_$_BrightnessSystemClient
+ _OBJC_CLASS_$_PPSSignpostController
+ _OBJC_CLASS_$_PPSSignpostServiceConnection
+ _OBJC_CLASS_$_PPSSignpostServiceRequest
+ _OBJC_IVAR_$_PLXPCRelay._xpcConnection
+ _OBJC_IVAR_$_PPSSignpostController._connection
+ _OBJC_IVAR_$_PPSSignpostServiceConnection._connectionToServer
+ _OBJC_IVAR_$_PPSSignpostServiceConnection._service
+ _OBJC_IVAR_$_PPSSignpostServiceRequest._endDate
+ _OBJC_IVAR_$_PPSSignpostServiceRequest._sourceURL
+ _OBJC_IVAR_$_PPSSignpostServiceRequest._startDate
+ _OBJC_IVAR_$_PPSSignpostServiceRequest._type
+ _OBJC_IVAR_$_PPSSignpostServiceRequest._uuid
+ _OBJC_METACLASS_$_PPSSignpostController
+ _OBJC_METACLASS_$_PPSSignpostServiceConnection
+ _OBJC_METACLASS_$_PPSSignpostServiceRequest
+ _PPSLogAPFS
+ _PPSLogAPFS._logHandle
+ _PPSLogAPFS.cold.1
+ _PPSLogAPFS.onceToken
+ _PPSLogSignpostController
+ _PPSLogSignpostController._logHandle
+ _PPSLogSignpostController.cold.1
+ _PPSLogSignpostController.onceToken
+ __OBJC_$_CLASS_METHODS_PPSSignpostController
+ __OBJC_$_CLASS_METHODS_PPSSignpostServiceRequest
+ __OBJC_$_CLASS_PROP_LIST_PPSSignpostServiceRequest
+ __OBJC_$_INSTANCE_METHODS_PPSSignpostController
+ __OBJC_$_INSTANCE_METHODS_PPSSignpostServiceConnection
+ __OBJC_$_INSTANCE_METHODS_PPSSignpostServiceRequest
+ __OBJC_$_INSTANCE_VARIABLES_PPSSignpostController
+ __OBJC_$_INSTANCE_VARIABLES_PPSSignpostServiceConnection
+ __OBJC_$_INSTANCE_VARIABLES_PPSSignpostServiceRequest
+ __OBJC_$_PROP_LIST_PPSSignpostController
+ __OBJC_$_PROP_LIST_PPSSignpostServiceConnection
+ __OBJC_$_PROP_LIST_PPSSignpostServiceRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PPSSignpostServiceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PPSSignpostServiceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PPSSignpostServiceRequest
+ __OBJC_CLASS_RO_$_PPSSignpostController
+ __OBJC_CLASS_RO_$_PPSSignpostServiceConnection
+ __OBJC_CLASS_RO_$_PPSSignpostServiceRequest
+ __OBJC_LABEL_PROTOCOL_$_PPSSignpostServiceDelegate
+ __OBJC_METACLASS_RO_$_PPSSignpostController
+ __OBJC_METACLASS_RO_$_PPSSignpostServiceConnection
+ __OBJC_METACLASS_RO_$_PPSSignpostServiceRequest
+ __OBJC_PROTOCOL_$_PPSSignpostServiceDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_PPSSignpostServiceDelegate
+ ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.853
+ ___18-[PLXPCRelay init]_block_invoke.20
+ ___23-[PLXPCRelay stopRelay]_block_invoke
+ ___24-[PLXPCRelay startRelay]_block_invoke
+ ___24-[PLXPCRelay startRelay]_block_invoke.30
+ ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.1
+ ___24-[PLXPCRelay startRelay]_block_invoke.30.cold.2
+ ___24-[PLXPCRelay startRelay]_block_invoke.36
+ ___24-[PLXPCRelay startRelay]_block_invoke.41
+ ___24-[PLXPCRelay startRelay]_block_invoke.41.cold.1
+ ___24-[PLXPCRelay startRelay]_block_invoke_2
+ ___24-[PLXPCRelay startRelay]_block_invoke_2.42
+ ___27-[PLArchiveManager migrate]_block_invoke.536
+ ___29-[PLXPCRelay relayConnection]_block_invoke.133
+ ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.1
+ ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.2
+ ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.3
+ ___29-[PLXPCRelay relayConnection]_block_invoke.133.cold.4
+ ___29-[PLXPCRelay relayConnection]_block_invoke.136
+ ___29-[PLXPCRelay relayConnection]_block_invoke.143
+ ___29-[PLXPCRelay relayConnection]_block_invoke.149
+ ___29-[PLXPCRelay relayConnection]_block_invoke.155
+ ___29-[PLXPCRelay relayConnection]_block_invoke.161
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.102
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.108
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.117
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.123
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.57
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.63
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.69
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.75
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.87
+ ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.96
+ ___35-[PLArchiveManager migrateArchive:]_block_invoke.520
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.424
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.424.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.430
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.435
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke.435.cold.1
+ ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.436
+ ___36-[PPSSignpostServiceConnection init]_block_invoke
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.14
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.14.cold.1
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.17
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.17.cold.1
+ ___36-[PPSSignpostServiceConnection init]_block_invoke.cold.1
+ ___37+[PLUtilities exitWithReason:action:]_block_invoke.188
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.756
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.762
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.769
+ ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.775
+ ___37-[PPSSignpostController _handleTask:]_block_invoke
+ ___37-[PPSSignpostController _handleTask:]_block_invoke.107
+ ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.496
+ ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.669
+ ___39-[PLSubmissionFileSP copyAndPrepareLog]_block_invoke.157
+ ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.327
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.416
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.422
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.432
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.443
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.449
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.458
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.480
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.486
+ ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.499
+ ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.497
+ ___46-[PPSSignpostController generateForTimeRange:]_block_invoke
+ ___46-[PPSSignpostController generateForTimeRange:]_block_invoke.56
+ ___46-[PPSSignpostController generateForTimeRange:]_block_invoke_2
+ ___46-[PPSSignpostController generateForTimeRange:]_block_invoke_3
+ ___46-[PPSSignpostController generateForTimeRange:]_block_invoke_3.cold.1
+ ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.498
+ ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.737
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.703
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.707
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.707.cold.1
+ ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.713
+ ___55+[PPSSignpostController registerDataCollectionActivity]_block_invoke
+ ___55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.694
+ ___55-[PPSSignpostController _performWithStartDate:endDate:]_block_invoke
+ ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.899
+ ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.798
+ ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.146
+ ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.561
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.746
+ ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.752
+ ___Block_byref_object_copy_.732
+ ___Block_byref_object_dispose_.733
+ ___PPSLogAPFS_block_invoke
+ ___PPSLogSignpostController_block_invoke
+ ___block_descriptor_32_e22_v16?0"BGSystemTask"8l
+ ___block_descriptor_40_e8_32s_e22_v32?0"NSURL"8Q16^B24ls32l8
+ ___block_descriptor_41_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e19_v20?0B8"NSDate"12ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e22_v32?0"NSURL"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56r_e19_"NSDictionary"8?0lr56l8s32l8s40l8s48l8
+ ___block_literal_global.167
+ ___block_literal_global.174
+ ___block_literal_global.184
+ ___block_literal_global.189
+ ___block_literal_global.190
+ ___block_literal_global.208
+ ___block_literal_global.226
+ ___block_literal_global.244
+ ___block_literal_global.262
+ ___block_literal_global.295
+ ___block_literal_global.316
+ ___block_literal_global.334
+ ___block_literal_global.338
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.362
+ ___block_literal_global.371
+ ___block_literal_global.396
+ ___block_literal_global.408
+ ___block_literal_global.432
+ ___block_literal_global.438
+ ___block_literal_global.440
+ ___block_literal_global.445
+ ___block_literal_global.448
+ ___block_literal_global.450
+ ___block_literal_global.455
+ ___block_literal_global.462
+ ___block_literal_global.469
+ ___block_literal_global.472
+ ___block_literal_global.475
+ ___block_literal_global.480
+ ___block_literal_global.491
+ ___block_literal_global.499
+ ___block_literal_global.5
+ ___block_literal_global.501
+ ___block_literal_global.508
+ ___block_literal_global.51
+ ___block_literal_global.510
+ ___block_literal_global.572
+ ___block_literal_global.684
+ ___block_literal_global.749
+ ___block_literal_global.751
+ ___block_literal_global.754
+ ___block_literal_global.758
+ ___block_literal_global.761
+ ___block_literal_global.764
+ ___block_literal_global.767
+ ___block_literal_global.833
+ ___block_literal_global.856
+ ___block_literal_global.876
+ ___block_literal_global.966
+ _blockingFlushCachesWithReason:timeout:.classDebugEnabled.693
+ _blockingFlushCachesWithReason:timeout:.defaultOnce.692
+ _blockingFlushQueues:withTimeout:.classDebugEnabled.702
+ _blockingFlushQueues:withTimeout:.classDebugEnabled.712
+ _blockingFlushQueues:withTimeout:.defaultOnce.701
+ _blockingFlushQueues:withTimeout:.defaultOnce.711
+ _flushCachesWithReason:.defaultOnce.668
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.145
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.144
+ _handlePeer:forEvent:.classDebugEnabled.101
+ _handlePeer:forEvent:.classDebugEnabled.107
+ _handlePeer:forEvent:.classDebugEnabled.116
+ _handlePeer:forEvent:.classDebugEnabled.122
+ _handlePeer:forEvent:.classDebugEnabled.56
+ _handlePeer:forEvent:.classDebugEnabled.62
+ _handlePeer:forEvent:.classDebugEnabled.68
+ _handlePeer:forEvent:.classDebugEnabled.74
+ _handlePeer:forEvent:.classDebugEnabled.86
+ _handlePeer:forEvent:.classDebugEnabled.95
+ _handlePeer:forEvent:.defaultOnce.100
+ _handlePeer:forEvent:.defaultOnce.106
+ _handlePeer:forEvent:.defaultOnce.115
+ _handlePeer:forEvent:.defaultOnce.121
+ _handlePeer:forEvent:.defaultOnce.55
+ _handlePeer:forEvent:.defaultOnce.61
+ _handlePeer:forEvent:.defaultOnce.67
+ _handlePeer:forEvent:.defaultOnce.73
+ _handlePeer:forEvent:.defaultOnce.85
+ _handlePeer:forEvent:.defaultOnce.94
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.560
+ _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.559
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.761
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.768
+ _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.774
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.760
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.767
+ _kPLTaskingEndNotification_block_invoke_6.defaultOnce.773
+ _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.898
+ _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.897
+ _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.948
+ _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.949
+ _migrateArchive:.classDebugEnabled.519
+ _migrateArchive:.defaultOnce.518
+ _objc_msgSend$_clearState
+ _objc_msgSend$_handleTask:
+ _objc_msgSend$_lastCollectionDate
+ _objc_msgSend$_performWithStartDate:endDate:
+ _objc_msgSend$_workQueue
+ _objc_msgSend$conditionCheckForAppIntents
+ _objc_msgSend$copyPropertyForKey:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$decodeIntegerForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$duration
+ _objc_msgSend$encodeInteger:forKey:
+ _objc_msgSend$generateForTimeRange:
+ _objc_msgSend$handlePeer:forEvent:
+ _objc_msgSend$inBUIDemoMode
+ _objc_msgSend$notifyExpired
+ _objc_msgSend$process:withReply:
+ _objc_msgSend$setConnection:
+ _objc_msgSend$setRequiresSignificantUserInactivity:
+ _objc_msgSend$setResourceIntensive:
+ _objc_msgSend$setResources:
+ _objc_msgSend$setSourceURL:
+ _objc_msgSend$setType:
+ _objc_msgSend$setXpcConnection:
+ _objc_msgSend$sourceURL
+ _objc_msgSend$type
+ _objc_msgSend$xpcConnection
+ _registerDailyTasks.classDebugEnabled.429
+ _registerDailyTasks.defaultOnce.428
+ _relayConnection.classDebugEnabled.154
+ _relayConnection.classDebugEnabled.160
+ _relayConnection.defaultOnce.153
+ _relayConnection.defaultOnce.159
+ _relayConnectionSync_block_invoke.classDebugEnabled.35
+ _relayConnectionSync_block_invoke.defaultOnce.34
+ _relayConnectionSync_block_invoke_2.classDebugEnabled
+ _relayConnectionSync_block_invoke_2.defaultOnce
+ _relayConnectionSync_block_invoke_3.classDebugEnabled
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.135
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.142
+ _relayConnectionSync_block_invoke_3.classDebugEnabled.148
+ _relayConnectionSync_block_invoke_3.defaultOnce
+ _relayConnectionSync_block_invoke_3.defaultOnce.134
+ _relayConnectionSync_block_invoke_3.defaultOnce.141
+ _relayConnectionSync_block_invoke_3.defaultOnce.147
+ _shouldStartTaskingToday.classDebugEnabled.415
+ _shouldStartTaskingToday.classDebugEnabled.421
+ _shouldStartTaskingToday.classDebugEnabled.442
+ _shouldStartTaskingToday.classDebugEnabled.448
+ _shouldStartTaskingToday.classDebugEnabled.457
+ _shouldStartTaskingToday.classDebugEnabled.479
+ _shouldStartTaskingToday.classDebugEnabled.485
+ _shouldStartTaskingToday.classDebugEnabled.491
+ _shouldStartTaskingToday.defaultOnce.414
+ _shouldStartTaskingToday.defaultOnce.420
+ _shouldStartTaskingToday.defaultOnce.441
+ _shouldStartTaskingToday.defaultOnce.447
+ _shouldStartTaskingToday.defaultOnce.456
+ _shouldStartTaskingToday.defaultOnce.478
+ _shouldStartTaskingToday.defaultOnce.484
+ _shouldStartTaskingToday.defaultOnce.490
+ _startRelay.classDebugEnabled
+ _startRelay.defaultOnce
+ _stopRelay.classDebugEnabled
+ _stopRelay.defaultOnce
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.745
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.751
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.744
+ _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.750
+ _xpc_connection_get_context
- +[PLModelingUtilities alsCurveHigherThanDefault]
- +[PLModelingUtilities getDefaultL0bThresholdForDeviceType]
- -[PLCoreOperator startServicesForRelay]
- -[PLCoreService startRelayServices]
- -[PLCoreStorage entriesForKey:withComparisons:].cold.4
- -[PLCoreStorage entriesForKey:withComparisons:].cold.5
- -[PowerlogCore setupForRelay]
- -[PowerlogCore setupForRelay].cold.1
- -[PowerlogCore setupForRelay].cold.2
- GCC_except_table166
- _PLLogRelay
- _PLLogRelay.__logObj
- _PLLogRelay.cold.1
- _PLLogRelay.onceToken
- ___104-[PLCoreStorage entriesForKey:inTimeRange:withCountOfEntriesBefore:withCountOfEntriesAfter:withFilters:]_block_invoke.851
- ___18-[PLXPCRelay init]_block_invoke.24
- ___27-[PLArchiveManager migrate]_block_invoke.530
- ___29-[PLXPCRelay relayConnection]_block_invoke.135
- ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.1
- ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.2
- ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.3
- ___29-[PLXPCRelay relayConnection]_block_invoke.135.cold.4
- ___29-[PLXPCRelay relayConnection]_block_invoke.141
- ___29-[PLXPCRelay relayConnection]_block_invoke.148
- ___29-[PLXPCRelay relayConnection]_block_invoke.154
- ___29-[PLXPCRelay relayConnection]_block_invoke.160
- ___29-[PLXPCRelay relayConnection]_block_invoke.166
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.103
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.109
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.118
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.124
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.34
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.40
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.46
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.52
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.64
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.70
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.79
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.85
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.91
- ___34-[PLXPCRelay handlePeer:forEvent:]_block_invoke.97
- ___35-[PLArchiveManager migrateArchive:]_block_invoke.514
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.422
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.422.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.428
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.433
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke.433.cold.1
- ___35-[PLCoreStorage registerDailyTasks]_block_invoke_2.434
- ___37+[PLUtilities exitWithReason:action:]_block_invoke.179
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.754
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.760
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.767
- ___37-[PLCoreStorage writeAggregateEntry:]_block_invoke.773
- ___38-[PLArchiveManager trimCleanEnergyLog]_block_invoke.490
- ___39-[PLCoreStorage flushCachesWithReason:]_block_invoke.665
- ___41-[PLCoreStorage initOperatorDependancies]_block_invoke.325
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.409
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.415
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.425
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.436
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.442
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.451
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.473
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.479
- ___45-[PLSubmissionConfig shouldStartTaskingToday]_block_invoke.485
- ___46-[PLArchiveManager trimExtendedPersistenceLog]_block_invoke.491
- ___47-[PLArchiveManager trimBackgroundProcessingLog]_block_invoke.492
- ___48-[PLCoreStorage writeEntry:withCompletionBlock:]_block_invoke.735
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.701
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.705
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.705.cold.1
- ___49-[PLCoreStorage blockingFlushQueues:withTimeout:]_block_invoke.711
- ___55-[PLCoreStorage blockingFlushCachesWithReason:timeout:]_block_invoke.692
- ___61-[PLCoreStorage lastEntryForKey:withComparisons:isSingleton:]_block_invoke.897
- ___63-[PLCoreStorage processEntriesForKey:withProperties:withBlock:]_block_invoke.796
- ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.137
- ___74-[PLCoreStorage handleSchemaMismatchForTable:expectedVersion:schemaMatch:]_block_invoke.559
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.744
- ___76-[PLCoreStorage writeProportionateAggregateEntry:withStartDate:withEndDate:]_block_invoke.750
- ___Block_byref_object_copy_.730
- ___Block_byref_object_dispose_.731
- ___PLLogRelay_block_invoke
- ___block_literal_global.142
- ___block_literal_global.157
- ___block_literal_global.181
- ___block_literal_global.198
- ___block_literal_global.199
- ___block_literal_global.205
- ___block_literal_global.215
- ___block_literal_global.217
- ___block_literal_global.220
- ___block_literal_global.235
- ___block_literal_global.271
- ___block_literal_global.289
- ___block_literal_global.293
- ___block_literal_global.307
- ___block_literal_global.325
- ___block_literal_global.327
- ___block_literal_global.336
- ___block_literal_global.343
- ___block_literal_global.348
- ___block_literal_global.360
- ___block_literal_global.369
- ___block_literal_global.387
- ___block_literal_global.399
- ___block_literal_global.423
- ___block_literal_global.429
- ___block_literal_global.431
- ___block_literal_global.436
- ___block_literal_global.441
- ___block_literal_global.442
- ___block_literal_global.446
- ___block_literal_global.451
- ___block_literal_global.453
- ___block_literal_global.457
- ___block_literal_global.463
- ___block_literal_global.471
- ___block_literal_global.476
- ___block_literal_global.488
- ___block_literal_global.493
- ___block_literal_global.502
- ___block_literal_global.503
- ___block_literal_global.542
- ___block_literal_global.553
- ___block_literal_global.556
- ___block_literal_global.665
- ___block_literal_global.730
- ___block_literal_global.732
- ___block_literal_global.735
- ___block_literal_global.739
- ___block_literal_global.742
- ___block_literal_global.745
- ___block_literal_global.748
- ___block_literal_global.831
- ___block_literal_global.854
- ___block_literal_global.874
- ___block_literal_global.945
- _blockingFlushCachesWithReason:timeout:.classDebugEnabled.691
- _blockingFlushCachesWithReason:timeout:.defaultOnce.690
- _blockingFlushQueues:withTimeout:.classDebugEnabled.700
- _blockingFlushQueues:withTimeout:.classDebugEnabled.710
- _blockingFlushQueues:withTimeout:.defaultOnce.699
- _blockingFlushQueues:withTimeout:.defaultOnce.709
- _flushCachesWithReason:.defaultOnce.666
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.136
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.135
- _handlePeer:forEvent:.classDebugEnabled.102
- _handlePeer:forEvent:.classDebugEnabled.108
- _handlePeer:forEvent:.classDebugEnabled.117
- _handlePeer:forEvent:.classDebugEnabled.123
- _handlePeer:forEvent:.classDebugEnabled.33
- _handlePeer:forEvent:.classDebugEnabled.39
- _handlePeer:forEvent:.classDebugEnabled.45
- _handlePeer:forEvent:.classDebugEnabled.51
- _handlePeer:forEvent:.classDebugEnabled.63
- _handlePeer:forEvent:.classDebugEnabled.69
- _handlePeer:forEvent:.classDebugEnabled.78
- _handlePeer:forEvent:.classDebugEnabled.84
- _handlePeer:forEvent:.classDebugEnabled.90
- _handlePeer:forEvent:.classDebugEnabled.96
- _handlePeer:forEvent:.defaultOnce.101
- _handlePeer:forEvent:.defaultOnce.107
- _handlePeer:forEvent:.defaultOnce.116
- _handlePeer:forEvent:.defaultOnce.122
- _handlePeer:forEvent:.defaultOnce.32
- _handlePeer:forEvent:.defaultOnce.38
- _handlePeer:forEvent:.defaultOnce.44
- _handlePeer:forEvent:.defaultOnce.50
- _handlePeer:forEvent:.defaultOnce.62
- _handlePeer:forEvent:.defaultOnce.68
- _handlePeer:forEvent:.defaultOnce.77
- _handlePeer:forEvent:.defaultOnce.83
- _handlePeer:forEvent:.defaultOnce.89
- _handlePeer:forEvent:.defaultOnce.95
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.classDebugEnabled.558
- _handleSchemaMismatchForTable:expectedVersion:schemaMatch:.defaultOnce.557
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.759
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.766
- _kPLTaskingEndNotification_block_invoke_6.classDebugEnabled.772
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.758
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.765
- _kPLTaskingEndNotification_block_invoke_6.defaultOnce.771
- _lastEntryForKey:withComparisons:isSingleton:.classDebugEnabled.896
- _lastEntryForKey:withComparisons:isSingleton:.defaultOnce.895
- _logMessage:fromFile:fromFunction:fromLineNumber:.defaultOnce.946
- _logMessage:fromFile:fromFunction:fromLineNumber:.objectForKey.947
- _migrateArchive:.classDebugEnabled.513
- _migrateArchive:.defaultOnce.512
- _objc_msgSend$alsCurveHigherThanDefault
- _objc_msgSend$setupForRelay
- _objc_msgSend$startRelayServices
- _registerDailyTasks.classDebugEnabled.427
- _registerDailyTasks.defaultOnce.426
- _relayConnection.classDebugEnabled.159
- _relayConnection.classDebugEnabled.165
- _relayConnection.defaultOnce.158
- _relayConnection.defaultOnce.164
- _relayConnectionSync_block_invoke.classDebugEnabled.140
- _relayConnectionSync_block_invoke.classDebugEnabled.147
- _relayConnectionSync_block_invoke.classDebugEnabled.153
- _relayConnectionSync_block_invoke.defaultOnce.139
- _relayConnectionSync_block_invoke.defaultOnce.146
- _relayConnectionSync_block_invoke.defaultOnce.152
- _shouldStartTaskingToday.classDebugEnabled.408
- _shouldStartTaskingToday.classDebugEnabled.414
- _shouldStartTaskingToday.classDebugEnabled.435
- _shouldStartTaskingToday.classDebugEnabled.441
- _shouldStartTaskingToday.classDebugEnabled.450
- _shouldStartTaskingToday.classDebugEnabled.472
- _shouldStartTaskingToday.classDebugEnabled.478
- _shouldStartTaskingToday.classDebugEnabled.484
- _shouldStartTaskingToday.defaultOnce.407
- _shouldStartTaskingToday.defaultOnce.413
- _shouldStartTaskingToday.defaultOnce.434
- _shouldStartTaskingToday.defaultOnce.440
- _shouldStartTaskingToday.defaultOnce.449
- _shouldStartTaskingToday.defaultOnce.471
- _shouldStartTaskingToday.defaultOnce.477
- _shouldStartTaskingToday.defaultOnce.483
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.743
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.classDebugEnabled.749
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.742
- _writeProportionateAggregateEntry:withStartDate:withEndDate:.defaultOnce.748
CStrings:
+ "%@ last signpost collection date: %@"
+ "%@%@/"
+ "'%@' task expired!"
+ "-[PLXPCRelay startRelay]"
+ "-[PLXPCRelay startRelay]_block_invoke"
+ "-[PLXPCRelay startRelay]_block_invoke_2"
+ "-[PLXPCRelay stopRelay]"
+ "/Library/Signposts/"
+ "@\"<PPSSignpostServiceDelegate>\""
+ "@\"PPSSignpostServiceConnection\""
+ "AABConstraints"
+ "App intents found, proceeding with submission"
+ "AppIntents"
+ "AppIntentsServices_Activity_1_2"
+ "BUI_DEMO_QUERY_TIME"
+ "BUI_DEMO_QUERY_TIME_OFFSET"
+ "BackdropCopy"
+ "Blending_and_Transition"
+ "CallTranslation"
+ "Capability23"
+ "Checking for app intents..."
+ "Clearing"
+ "Connection error occurred: %@"
+ "Connection interrupted while service is active."
+ "Connection invalidated while service is active."
+ "Deferring '%@' task..."
+ "DestinationCopy"
+ "DidComplete"
+ "DidDefer"
+ "DoneWithWork"
+ "EligibleFileCount"
+ "ExtPhyRXDuration2G"
+ "ExtPhyRXDuration5G"
+ "ExtPhyRXDurationSC"
+ "Failed to establish connection to signpost service"
+ "Failed to expire '%@' task with error: %@"
+ "Failed to generate signpost tag file at '%@'"
+ "Failed to generate signpost tarball"
+ "Failed to get creation date for signpost file '%@'"
+ "Failed to move signpost tarball from '%@' to '%@'"
+ "Filter"
+ "Finished '%@' task..."
+ "Finished on-demand signpost collection..."
+ "Finished signpost collection: '%@'"
+ "Generated %lu signpost files for data range '%@'"
+ "Group"
+ "Initializing signpost controller..."
+ "IsANEIntensive"
+ "IsDiskIntensive"
+ "IsGPUIntensive"
+ "IsOffloadEvent"
+ "LightSourceSupport"
+ "Mask"
+ "No app intents found, skipping submission"
+ "OffscreenReasons"
+ "OrionActiveRDOIndex"
+ "OrionChargeCapable"
+ "OrionEvtBuffer"
+ "OrionExternalConnected"
+ "OrionPresenceStatus"
+ "OrionVoltageConstraint"
+ "Other"
+ "PLBatteryAgent_EventBackward_Iconography"
+ "PLBatteryAgent_EventForward_OrionBuffer"
+ "PLBatteryAgent_EventForward_OrionInfo"
+ "PLCLPCAgent_EventInterval_TGAccumulators"
+ "PLCLPCAgent_EventInterval_TGCPUClusterAccumulators"
+ "PLCLPCAgent_EventInterval_TGInfo"
+ "PPSSignpostController"
+ "PPSSignpostControllerLastCollectionDate"
+ "PPSSignpostServiceConnection"
+ "PPSSignpostServiceDelegate"
+ "PPSSignpostServiceRequest"
+ "Patten_and_TiledImage"
+ "Plugin_and_Cache"
+ "Property %@ is not of the expected NSDictionary class to get default L0b Threshold for Device Type"
+ "Property L0b in %@ is not of the expected NSDictionary class to get default L0b Threshold for Device Type"
+ "Recovering last signpost collection date: %@"
+ "Registering signpost collection activity ('%@')..."
+ "Relay: Relay running in aggd with service %s to %s"
+ "Relay: XPC error! %@"
+ "Relay: closing relay in aggd with service %s to %s"
+ "Relay: could not create relayMessage object"
+ "Relay: could not create relayMessage object for listener key"
+ "Relay: could not create replyMessage object"
+ "Relay: could not create replyXpcDict object"
+ "Relay: peer(%d) connected"
+ "Remaining signpost collection range: ['%@', '%@']"
+ "RemainingDurationToCollect"
+ "RequestedTimeRangeDuration"
+ "Saving"
+ "Shadow"
+ "Signpost collection activity ('%@') is disabled!"
+ "Signpost collection requested on-demand for range: %@"
+ "Signpost file '%@' is outside of requested range"
+ "Signpost tarball generated at '%@'"
+ "SignpostCollection"
+ "Signpost_%@"
+ "SlowChargerReason"
+ "Starting signpost collection: '%@'"
+ "T@\"<PPSSignpostServiceDelegate>\",R,V_service"
+ "T@\"NSObject<OS_xpc_object>\",&,V_xpcConnection"
+ "T@\"NSURL\",&,V_sourceURL"
+ "T@\"NSUUID\",&,V_uuid"
+ "T@\"PPSSignpostServiceConnection\",&,V_connection"
+ "TGID"
+ "TGName"
+ "TGType"
+ "TaskDuration"
+ "Ti,V_type"
+ "TimeToEmptyDbgData"
+ "TimestampEvent"
+ "Transform_and_Scaling"
+ "Ts00"
+ "Ts04"
+ "Ts08"
+ "Ts0C"
+ "Ts0G"
+ "Ts0K"
+ "Unable to get %@ property to obtain default L0b Threshold for Device Type"
+ "Unable to initialize BrightnessSystemClient to get default L0b Threshold for Device Type"
+ "Watchdog"
+ "XPCRelay_Connection"
+ "_clearState"
+ "_handleTask:"
+ "_lastCollectionDate"
+ "_performWithStartDate:endDate:"
+ "_sourceURL"
+ "_type"
+ "_xpcConnection"
+ "apfs"
+ "chargeStatus"
+ "com.apple.PerfPowerServicesSignpostService"
+ "com.apple.perfpowerservices.signpost"
+ "com.apple.perfpowerservices.signpost.controller.midnight"
+ "com.apple.perfpowerservices.signpost.controller.task"
+ "com.apple.powerlog.plxpclogger.xpc"
+ "conditionCheckForAppIntents"
+ "controller"
+ "copyPropertyForKey:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "decodeIntegerForKey:"
+ "decodeObjectForKey:"
+ "defaultL0bThreshold value is %@. Returned value with 15 percent padding added is O %f"
+ "downlinkTranslationEnabled"
+ "downlinkTranslationMode"
+ "encodeInteger:forKey:"
+ "farEndLanguage"
+ "generateForTimeRange:"
+ "getOverridableMonotonicNow"
+ "nearEndLanguage"
+ "notifyExpired"
+ "process:withReply:"
+ "requestType=%d, sourceURL=%@, startDate=%@, endDate=%@, uuid=%@"
+ "sd08"
+ "sd0O"
+ "sd0U"
+ "sd0g"
+ "sd0u"
+ "sd0y"
+ "sd16"
+ "sd1c"
+ "sd1o"
+ "sd1s"
+ "sd2D"
+ "sd3V"
+ "sd3d"
+ "sd3h"
+ "sd3p"
+ "setRequiresSignificantUserInactivity:"
+ "setResourceIntensive:"
+ "setResources:"
+ "setSourceURL:"
+ "setType:"
+ "setXpcConnection:"
+ "showing_hint"
+ "sourceURL"
+ "translationActive"
+ "uplinkTranslationEnabled"
+ "uplinkTranslationMode"
+ "v20@?0B8@\"NSDate\"12"
+ "v32@0:8@\"PPSSignpostServiceRequest\"16@?<v@?B@\"NSDate\">24"
+ "xpcConnection"
- "All entries found in cache and database: %@"
- "Done starting services for lite mode relay"
- "Entries found in database: %@"
- "PhotoSharingEnabled"
- "Start Powerlog Services for relay"
- "Starting services for lite mode relay"
- "alsCurveHigherThanDefault"
- "footprintSum"
- "isANEIntensive"
- "isCPUIntensive"
- "isDiskIntensive"
- "isGPUIntensive"
- "isMemoryIntensive"
- "relay"
- "setupForRelay"
- "startRelayServices"
- "startServicesForRelay"

```
