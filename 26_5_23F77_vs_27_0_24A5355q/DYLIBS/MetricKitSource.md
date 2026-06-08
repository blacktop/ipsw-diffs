## MetricKitSource

> `/System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource`

```diff

-297.120.4.0.0
-  __TEXT.__text: 0x7028
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x6d4
-  __TEXT.__const: 0x18a
-  __TEXT.__cstring: 0x391
-  __TEXT.__oslogstring: 0x5a4
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__swift5_typeref: 0x4f
-  __TEXT.__swift5_reflstr: 0x9
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0x54
-  __TEXT.__swift5_fieldmd: 0x10
+353.0.0.0.0
+  __TEXT.__text: 0xcf90
+  __TEXT.__objc_methlist: 0x76c
+  __TEXT.__const: 0x696
+  __TEXT.__cstring: 0x5b2
+  __TEXT.__oslogstring: 0x70f
+  __TEXT.__gcc_except_tab: 0x1f0
+  __TEXT.__swift5_typeref: 0x16a
+  __TEXT.__constg_swiftt: 0x110
+  __TEXT.__swift5_fieldmd: 0xa8
+  __TEXT.__swift5_types: 0x1c
+  __TEXT.__swift5_reflstr: 0x4c
+  __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0xc
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x238
-  __TEXT.__objc_classname: 0x127
-  __TEXT.__objc_methname: 0x1914
-  __TEXT.__objc_methtype: 0x365
-  __TEXT.__objc_stubs: 0x10c0
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0x168
-  __DATA_CONST.__objc_classlist: 0x58
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__eh_frame: 0x220
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x198
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x668
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x290
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x480
-  __AUTH_CONST.__objc_const: 0xdb8
+  __DATA_CONST.__got: 0x308
+  __AUTH_CONST.__const: 0x439
+  __AUTH_CONST.__cfstring: 0x560
+  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH.__objc_data: 0xb0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__data: 0x1b8
-  __DATA.__bss: 0x200
-  __DATA.__common: 0x18
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__data: 0x268
+  __DATA.__bss: 0xb60
+  __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__data: 0x98
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9EA122A8-FFE3-3735-BF21-7CA83E5CFB1C
-  Functions: 221
-  Symbols:   794
-  CStrings:  435
+  UUID: 8C23885B-45E9-380D-8CDC-977720DA73ED
+  Functions: 362
+  Symbols:   995
+  CStrings:  145
 
Symbols:
+ +[MXSampleAnalysisParser eventTimestampFromSampleStore:]
+ +[MXSampleAnalysisParser eventTimestampFromSampleStore:].cold.1
+ +[MXSampleAnalysisParser eventTimestampFromSampleStore:].cold.2
+ +[MXSampleAnalysisParser eventTimestampFromSampleStore:].cold.3
+ +[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]
+ +[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:].cold.1
+ +[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:].cold.2
+ +[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:].cold.3
+ +[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:].cold.4
+ +[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:].cold.5
+ +[MXSourceUtilities stateAwareClientsWithDomains]
+ -[MXPowerlogData encodeWithCoder:].cold.1
+ -[MXPowerlogData encodeWithCoder:].cold.2
+ -[MXPowerlogData initWithCoder:].cold.1
+ -[MXPowerlogData initWithCoder:].cold.2
+ -[MXPowerlogData intervalMetrics]
+ -[MXPowerlogData metalFrameRateMetrics]
+ -[MXPowerlogData setIntervalMetrics:]
+ -[MXPowerlogData setMetalFrameRateMetrics:]
+ -[MXPowerlogData setStateMetrics:]
+ -[MXPowerlogData stateMetrics]
+ -[MXReportCrashData initWithDiagnosticContainer:]
+ -[MXReportCrashData memoryExceptionDiagnosticContainer]
+ -[MXReportCrashData setMemoryExceptionDiagnosticContainer:]
+ GCC_except_table16
+ GCC_except_table9
+ _NSStringFromClass
+ _OBJC_CLASS_$_MXAverage
+ _OBJC_CLASS_$_MXCallStackArray
+ _OBJC_CLASS_$_MXDiagnosticEnvironment
+ _OBJC_CLASS_$_MXFlatFrameData
+ _OBJC_CLASS_$_MXHistogram
+ _OBJC_CLASS_$_MXHistogramBucket
+ _OBJC_CLASS_$_MXIntervalMetricData
+ _OBJC_CLASS_$_MXMemoryExceptionDiagnosticContainer
+ _OBJC_CLASS_$_MXMetalFrameRateMetric
+ _OBJC_CLASS_$_MXReportedState
+ _OBJC_CLASS_$_MXStateMetricData
+ _OBJC_CLASS_$_MXThreadMetadata
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_NSUnit
+ _OBJC_CLASS_$_NSUnitFrequency
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_MXPowerlogData._intervalMetrics
+ _OBJC_IVAR_$_MXPowerlogData._metalFrameRateMetrics
+ _OBJC_IVAR_$_MXPowerlogData._stateMetrics
+ _OBJC_IVAR_$_MXReportCrashData._memoryExceptionDiagnosticContainer
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __DATA__TtC15MetricKitSource15SourceUtilities
+ __METACLASS_DATA__TtC15MetricKitSource15SourceUtilities
+ ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.35
+ ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.42
+ ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.42.cold.1
+ ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.42.cold.2
+ ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.43
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.48
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.49
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.49.cold.1
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.49.cold.2
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.50
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.52
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.52.cold.1
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.cold.1
+ ___89+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:]_block_invoke.cold.2
+ ___block_descriptor_48_e8_32s40r_e45_B24?0"SSReportedState"8"SSReportedState"16lr40l8s32l8
+ ___block_literal_global.78
+ ___swift_memcpy0_1
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_MetricKitSource
+ _associated conformance 15MetricKitSource0C14LoggerCategoryOSHAASQ
+ _associated conformance 15MetricKitSource0aB14LoggerCategoryOSHAASQ
+ _associated conformance 15MetricKitSource21MeasurementCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLOSHAASQ
+ _associated conformance 15MetricKitSource21MeasurementCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 15MetricKitSource21MeasurementCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 15MetricKitSource22DateIntervalCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLOSHAASQ
+ _associated conformance 15MetricKitSource22DateIntervalCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 15MetricKitSource22DateIntervalCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$baseUnit
+ _objc_msgSend$bits
+ _objc_msgSend$containsObject:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$dictionary
+ _objc_msgSend$domain
+ _objc_msgSend$durationSeconds
+ _objc_msgSend$eventTimestampFromSampleStore:
+ _objc_msgSend$exabits
+ _objc_msgSend$exabytes
+ _objc_msgSend$exbibits
+ _objc_msgSend$exbibytes
+ _objc_msgSend$getSignpostDataforPid:forClient:andEventTimestamp:reportedStateData:
+ _objc_msgSend$gibibits
+ _objc_msgSend$gibibytes
+ _objc_msgSend$gigabits
+ _objc_msgSend$gigabytes
+ _objc_msgSend$gigahertz
+ _objc_msgSend$hash
+ _objc_msgSend$hertz
+ _objc_msgSend$hours
+ _objc_msgSend$initWithDiagnosticContainer:
+ _objc_msgSend$initWithDomain:label:stableContext:durationSeconds:
+ _objc_msgSend$initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:callStack:hangDuration:hangType:
+ _objc_msgSend$initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:callStack:launchDuration:
+ _objc_msgSend$initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:callStack:totalCpuTime:totalSampledTime:
+ _objc_msgSend$initWithMetaData:applicationVersion:signpostData:reportedStateData:pid:totalWritesCaused:stackTrace:
+ _objc_msgSend$initWithSymbol:
+ _objc_msgSend$isMetricKitClient:
+ _objc_msgSend$kibibits
+ _objc_msgSend$kibibytes
+ _objc_msgSend$kilobits
+ _objc_msgSend$kilobytes
+ _objc_msgSend$kilohertz
+ _objc_msgSend$label
+ _objc_msgSend$mebibits
+ _objc_msgSend$mebibytes
+ _objc_msgSend$megabits
+ _objc_msgSend$megahertz
+ _objc_msgSend$microhertz
+ _objc_msgSend$microseconds
+ _objc_msgSend$millihertz
+ _objc_msgSend$minutes
+ _objc_msgSend$nanohertz
+ _objc_msgSend$nanoseconds
+ _objc_msgSend$nibbles
+ _objc_msgSend$pebibits
+ _objc_msgSend$pebibytes
+ _objc_msgSend$petabits
+ _objc_msgSend$petabytes
+ _objc_msgSend$picoseconds
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$setFilterPredicate:
+ _objc_msgSend$setMonitorStateHeartbeats:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setStateTransitionBlock:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$stableContext
+ _objc_msgSend$stableState
+ _objc_msgSend$stateAwareClientsWithDomains
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$symbol
+ _objc_msgSend$tebibits
+ _objc_msgSend$tebibytes
+ _objc_msgSend$terabits
+ _objc_msgSend$terabytes
+ _objc_msgSend$terahertz
+ _objc_msgSend$yobibits
+ _objc_msgSend$yobibytes
+ _objc_msgSend$yottabits
+ _objc_msgSend$yottabytes
+ _objc_msgSend$zebibits
+ _objc_msgSend$zebibytes
+ _objc_msgSend$zettabits
+ _objc_msgSend$zettabytes
+ _objc_opt_isKindOfClass
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x3
+ _objc_retain_x8
+ _objc_setProperty_atomic_copy
+ _swift_allocError
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_dynamicCastUnknownClass
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_initStackObject
+ _swift_lookUpClassMethod
+ _swift_release_x19
+ _swift_release_x20
+ _swift_retain_x20
+ _swift_willThrow
+ _symbolic SS
+ _symbolic SS_So17MXReportCrashDataCt
+ _symbolic _____ 15MetricKitSource0C14LoggerCategoryO
+ _symbolic _____ 15MetricKitSource0C9UtilitiesC
+ _symbolic _____ 15MetricKitSource0aB14LoggerCategoryO
+ _symbolic _____ 15MetricKitSource21MeasurementCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLO
+ _symbolic _____ 15MetricKitSource22DateIntervalCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLO
+ _symbolic _____ySSSo17MXReportCrashDataCG s18_DictionaryStorageC
+ _symbolic _____ySS_So17MXReportCrashDataCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySo6NSUnitCG 10Foundation11MeasurementV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15MetricKitSource21MeasurementCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 15MetricKitSource22DateIntervalCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15MetricKitSource21MeasurementCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 15MetricKitSource22DateIntervalCodingKeys33_340AD078E7FD7726BFEB88E55470ED03LLO
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
- +[MXSampleAnalysisParser constructPayloadWithReport:withType:].cold.10
- +[MXSampleAnalysisParser constructPayloadWithReport:withType:].cold.11
- +[MXSampleAnalysisParser constructPayloadWithReport:withType:].cold.12
- GCC_except_table7
- _OBJC_CLASS_$_SignpostSupportPIDAllowlist
- _OBJC_CLASS_$_SignpostSupportSubsystemCategoryAllowlist
- ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.29
- ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.37
- ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.37.cold.1
- ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.37.cold.2
- ___71+[MXSourceUtilities getSignpostDataforPid:forClient:andEventTimestamp:]_block_invoke.38
- ___block_literal_global.55
- _objc_msgSend$addPIDNumber:
- _objc_msgSend$addSubsystem:category:
- _objc_msgSend$date
- _objc_msgSend$initWithMetaData:applicationVersion:signpostData:pid:callStack:hangDuration:hangType:
- _objc_msgSend$initWithMetaData:applicationVersion:signpostData:pid:callStack:launchDuration:
- _objc_msgSend$initWithMetaData:applicationVersion:signpostData:pid:callStack:totalCpuTime:totalSampledTime:
- _objc_msgSend$initWithMetaData:applicationVersion:signpostData:pid:totalWritesCaused:stackTrace:
- _objc_msgSend$setPidFilter:
- _objc_msgSend$setSubsystemCategoryFilter:
- _objc_retain_x25
CStrings:
+ "%@__%@__%lx"
+ "' for dimension "
+ ") must be >= 'begin' ("
+ "B24@?0@\"SSReportedState\"8@\"SSReportedState\"16"
+ "DateInterval 'end' ("
+ "MXPowerlogData %p decoded intervalMetrics: FAILED - returned nil"
+ "MXPowerlogData %p decoded intervalMetrics: count=%lu, class=%{public}@"
+ "MXPowerlogData encoding intervalMetrics: count=%lu, class=%{public}@"
+ "MXPowerlogData encoding intervalMetrics: nil"
+ "MXStateAwareClients"
+ "MetricManager"
+ "PID passed for reading MXSignpost was nil"
+ "SourceManager"
+ "State record limit reached (%d), dropping additional state transitions"
+ "Unknown unit symbol '"
+ "begin"
+ "com.apple.MetricKitSource"
+ "com.apple.metrickit.metricmanager"
+ "com.apple.metrickit.source"
+ "decode"
+ "encode"
+ "end"
+ "intervalMetrics"
+ "memoryExceptionDiagnosticContainer"
+ "metalFrameRateMetrics"
+ "stateMetrics"
+ "subsystem == %@ AND processIdentifier == %@"
+ "transport"
+ "unit"
+ "utilities"
+ "value"
- ".cxx_destruct"
- "@\"MXAnimationMetric\""
- "@\"MXAppExitMetric\""
- "@\"MXAppLaunchDiagnostic\""
- "@\"MXAppLaunchMetric\""
- "@\"MXAppResponsivenessMetric\""
- "@\"MXAppRunTimeMetric\""
- "@\"MXCPUExceptionDiagnostic\""
- "@\"MXCPUMetric\""
- "@\"MXCellularConditionMetric\""
- "@\"MXCrashDiagnostic\""
- "@\"MXDiskIOMetric\""
- "@\"MXDiskSpaceUsageMetric\""
- "@\"MXDiskWriteExceptionDiagnostic\""
- "@\"MXDisplayMetric\""
- "@\"MXGPUMetric\""
- "@\"MXHangDiagnostic\""
- "@\"MXLocationActivityMetric\""
- "@\"MXMemoryMetric\""
- "@\"MXNetworkTransferMetric\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSObject<OS_os_log>\""
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8@16Q24"
- "@32@0:8@16q24"
- "@36@0:8i16@20@28"
- "@40@0:8q16@24@32"
- "@44@0:8B16@20@28@36"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B28@0:8@16I24"
- "MXHangTracerData"
- "MXPowerlogData"
- "MXReportCrashData"
- "MXSampleAnalysisParser"
- "MXSourceData"
- "MXSourceManager"
- "MXSourceUtilities"
- "MXSourceXPCClient"
- "MXSourceXPCPayload"
- "MXSourceXPCServer"
- "MXSpaceAttributionData"
- "MXSpinTracerData"
- "NSCoding"
- "NSSecureCoding"
- "T@\"MXAnimationMetric\",&,V_animationMetrics"
- "T@\"MXAppExitMetric\",&,V_applicationExitMetrics"
- "T@\"MXAppLaunchDiagnostic\",&,V_appLaunchDiagnostic"
- "T@\"MXAppLaunchMetric\",&,V_applicationLaunchMetrics"
- "T@\"MXAppResponsivenessMetric\",&,V_applicationResponsivenessMetrics"
- "T@\"MXAppRunTimeMetric\",&,V_applicationTimeMetrics"
- "T@\"MXCPUExceptionDiagnostic\",&,V_cpuExceptionDiagnostic"
- "T@\"MXCPUMetric\",&,V_cpuMetrics"
- "T@\"MXCellularConditionMetric\",&,V_cellularConditionMetrics"
- "T@\"MXCrashDiagnostic\",&,V_crashDiagnostic"
- "T@\"MXDiskIOMetric\",&,V_diskIOMetrics"
- "T@\"MXDiskSpaceUsageMetric\",&,V_diskSpaceUsageMetrics"
- "T@\"MXDiskWriteExceptionDiagnostic\",&,V_diskWriteExceptionDiagnostic"
- "T@\"MXDisplayMetric\",&,V_displayMetrics"
- "T@\"MXGPUMetric\",&,V_gpuMetrics"
- "T@\"MXHangDiagnostic\",&,V_hangDiagnostic"
- "T@\"MXLocationActivityMetric\",&,V_locationActivityMetrics"
- "T@\"MXMemoryMetric\",&,V_memoryMetrics"
- "T@\"MXNetworkTransferMetric\",&,V_networkTransferMetrics"
- "T@\"NSArray\",&,V_signpostMetrics"
- "T@\"NSDate\",&,V_beginDate"
- "T@\"NSDate\",&,V_datestamp"
- "T@\"NSDate\",&,V_endDate"
- "T@\"NSDictionary\",&,V_metrics"
- "T@\"NSObject<OS_os_log>\",&,N,V_sourceManagerLogHandle"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,R"
- "TB,V_includesMultipleApplicationVersions"
- "Td,N,R"
- "Tq,V_sourceID"
- "_TtC15MetricKitSource15MXDateFormatter"
- "_animationMetrics"
- "_appLaunchDiagnostic"
- "_applicationExitMetrics"
- "_applicationLaunchMetrics"
- "_applicationResponsivenessMetrics"
- "_applicationTimeMetrics"
- "_beginDate"
- "_cellularConditionMetrics"
- "_connection"
- "_cpuExceptionDiagnostic"
- "_cpuMetrics"
- "_crashDiagnostic"
- "_createXPCConnection"
- "_datestamp"
- "_diskIOMetrics"
- "_diskSpaceUsageMetrics"
- "_diskWriteExceptionDiagnostic"
- "_displayMetrics"
- "_endDate"
- "_gpuMetrics"
- "_hangDiagnostic"
- "_includesMultipleApplicationVersions"
- "_locationActivityMetrics"
- "_memoryMetrics"
- "_metrics"
- "_networkTransferMetrics"
- "_signpostMetrics"
- "_sourceID"
- "_sourceManagerLogHandle"
- "addObject:"
- "addPIDNumber:"
- "addSubsystem:category:"
- "address"
- "aggregateStacksByProcess"
- "anyClientsAvailable"
- "array"
- "binary"
- "boolValue"
- "bundleIdentifier"
- "bundleWithPath:"
- "bytes"
- "bytesWritten"
- "callTreeForTask:"
- "callTreeForThread:inTask:"
- "callTreesForThreadsInTask:"
- "category"
- "childFrames"
- "connection"
- "constructPayloadWithReport:withType:"
- "containingBundleRecord"
- "count"
- "cpuDuration"
- "cpuExceptionDiagnostic"
- "cpuUsed"
- "currentLocale"
- "d16@0:8"
- "date"
- "dateByAddingTimeInterval:"
- "dateFromString:"
- "dateFromString:format:"
- "dateTruncatedToMinute:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "datestamp"
- "dealloc"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "deliverSamplePayloadForClient:"
- "deltaMachAbsTimeSeconds"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "diskWriteExceptionDiagnostic"
- "durationMs"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endEvent"
- "enumerateObjectsUsingBlock:"
- "eventTimeRange"
- "frame"
- "getCallStackForReport:withType:"
- "getSignpostDataforPid:forClient:andEventTimestamp:"
- "guessMissingTimesBasedOnTimestamp:"
- "hangDuration"
- "includesMultipleApplicationVersions"
- "indexOfFirstSampleOnOrAfterTimestamp:"
- "init"
- "initPayloadDataWithDiagnostics:"
- "initPayloadDataWithMutipleAppVersions:withTimeStampBegin:withTimeStampEnd:withMetrics:"
- "initWithBinaryName:binaryUUID:address:binaryOffset:sampleCount:withDepth:subFrameArray:"
- "initWithBundleIdentifier:error:"
- "initWithCoder:"
- "initWithDoubleValue:unit:"
- "initWithMachServiceName:options:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:hangDuration:hangType:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:launchDuration:"
- "initWithMetaData:applicationVersion:signpostData:pid:callStack:totalCpuTime:totalSampledTime:"
- "initWithMetaData:applicationVersion:signpostData:pid:totalWritesCaused:stackTrace:"
- "initWithRegionFormat:osVersion:deviceType:appBuildVersion:platformArchitecture:bundleID:"
- "initWithSourceID:withDateStamp:andMetrics:"
- "initWithSubSystem:category:name:beginTimeStamp:endTimeStamp:duration:isInterval:"
- "initWithThreadArray:aggregatedByProcess:"
- "initWithTopCallStackFrames:isAttributedThread:"
- "instruction"
- "interfaceWithProtocol:"
- "isAppAnalyticsEnabled"
- "isEqualToString:"
- "isMetricKitClient:"
- "isMetricKitClient:forUser:"
- "launchDuration"
- "mainThread"
- "measurementByConvertingToUnit:"
- "megabytes"
- "milliseconds"
- "name"
- "now"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offsetIntoTextSegment"
- "oneDay"
- "options"
- "parseCallTree:isAttributedThread:"
- "parseCallTreeFrame:withDepth:"
- "pid"
- "printTargetThreadOnly"
- "processImagePath"
- "processLogArchiveWithPath:startDate:endDate:errorOut:"
- "q"
- "q16@0:8"
- "regionFormat"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "resume"
- "rootFrames"
- "sampleCount"
- "sampleStore"
- "sampleTimestamps"
- "seconds"
- "sendDiagnostic:forDate:andSourceID:"
- "sendDiagnosticReport:forType:forSourceID:"
- "sendDiagnosticReport:forType:forSourceID:options:"
- "sendMetrics:forDate:andSourceID:"
- "setAnimationMetrics:"
- "setAppLaunchDiagnostic:"
- "setApplicationExitMetrics:"
- "setApplicationLaunchMetrics:"
- "setApplicationResponsivenessMetrics:"
- "setApplicationTimeMetrics:"
- "setBeginDate:"
- "setCellularConditionMetrics:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnection:"
- "setCpuExceptionDiagnostic:"
- "setCpuMetrics:"
- "setCrashDiagnostic:"
- "setDateFormat:"
- "setDatestamp:"
- "setDiskIOMetrics:"
- "setDiskSpaceUsageMetrics:"
- "setDiskWriteExceptionDiagnostic:"
- "setDisplayMetrics:"
- "setEmitEventProcessingBlock:"
- "setEndDate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setGpuMetrics:"
- "setHangDiagnostic:"
- "setIncludesMultipleApplicationVersions:"
- "setIntervalCompletionProcessingBlock:"
- "setLocale:"
- "setLocationActivityMetrics:"
- "setMemoryMetrics:"
- "setMetrics:"
- "setNetworkTransferMetrics:"
- "setObject:forKey:"
- "setPidFilter:"
- "setRemoteObjectInterface:"
- "setSignpostMetrics:"
- "setSourceID:"
- "setSourceManagerLogHandle:"
- "setSubsystemCategoryFilter:"
- "setTimeZone:"
- "setWithObjects:"
- "sharedManager"
- "simulatePayloadDeliveryForClient:"
- "sourceManagerLogHandle"
- "startTime"
- "stringByDeletingLastPathComponent"
- "stringFromDate:"
- "stringFromDate:format:"
- "subsystem"
- "supportsSecureCoding"
- "targetProcess"
- "targetProcessBundleShortVersion"
- "targetProcessBundleVersion"
- "targetProcessId"
- "targetThreadId"
- "thread"
- "threadCallTrees"
- "threadId"
- "threads"
- "totalCPUTime"
- "totalWritesCaused"
- "uid"
- "uuid"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"MXSourceXPCPayload\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8q16"
- "v40@0:8@16@24q32"
- "v40@0:8@16q24q32"
- "v48@0:8@16q24q32@40"
- "wallTime"
- "writeDiagnosticDataWithPayload:"
- "writeMetricDataWithPayload:"

```
