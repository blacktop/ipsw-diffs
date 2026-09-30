## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0xe02c
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0xf0c
-  __TEXT.__const: 0xb8
-  __TEXT.__gcc_except_tab: 0x6a4
-  __TEXT.__cstring: 0xe63
-  __TEXT.__oslogstring: 0x92f
+2954.0.0.502.3
+  __TEXT.__text: 0x17190
+  __TEXT.__auth_stubs: 0x570
+  __TEXT.__objc_methlist: 0x13dc
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x844
+  __TEXT.__cstring: 0x17cb
+  __TEXT.__oslogstring: 0x147d
   __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x3b8
-  __TEXT.__objc_classname: 0x127
-  __TEXT.__objc_methname: 0x2900
-  __TEXT.__objc_methtype: 0x596
-  __TEXT.__objc_stubs: 0x2000
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x38
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__objc_classname: 0x185
+  __TEXT.__objc_methname: 0x3998
+  __TEXT.__objc_methtype: 0x660
+  __TEXT.__objc_stubs: 0x2f00
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f0
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x1b0
-  __AUTH_CONST.__auth_got: 0x280
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xbe0
-  __AUTH_CONST.__objc_const: 0x18b0
+  __DATA_CONST.__objc_selrefs: 0xda0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x40
+  __DATA_CONST.__objc_arraydata: 0x208
+  __AUTH_CONST.__auth_got: 0x2c8
+  __AUTH_CONST.__const: 0x160
+  __AUTH_CONST.__cfstring: 0x1220
+  __AUTH_CONST.__objc_const: 0x1fa8
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_ivar: 0x16c
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x230
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1e4
+  __DATA.__data: 0x300
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__bss: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5F03DCAB-FABE-37D0-82BA-3439C4C2B102
-  Functions: 395
-  Symbols:   1436
-  CStrings:  869
+  UUID: 1AE5B681-90CF-30BF-8B1A-57BBD87463EA
+  Functions: 558
+  Symbols:   1959
+  CStrings:  1229
 
Symbols:
+ +[PPSMetricMonitorConfiguration tracingConfiguration:]
+ +[PPSMetricMonitorHeadlessClient _initConnection]
+ +[PPSMetricMonitorHeadlessClient isMonitoring]
+ +[PPSMetricMonitorHeadlessClient monitoredProcesses]
+ +[PPSMetricMonitorHeadlessClient startMonitoringProcessesWithNames:config:error:]
+ +[PPSMetricMonitorHeadlessClient startMonitoringProcessesWithPID:config:error:]
+ +[PPSMetricMonitorHeadlessClient startMonitoringSystemMetricsWithConfig:error:]
+ +[PPSMetricMonitorHeadlessClient stopMonitoring]
+ -[PPSClient clientMetrics]
+ -[PPSClient monitoredProcessNames]
+ -[PPSClient setClientMetrics:]
+ -[PPSClient setMonitoredProcessNames:]
+ -[PPSMetricCollection accumSystemLoad]
+ -[PPSMetricCollection clearMetrics:]
+ -[PPSMetricCollection clearMetrics:].cold.1
+ -[PPSMetricCollection combineWithMetricCollection:trackedPids:]
+ -[PPSMetricCollection combineWithMetricCollection:trackedPids:].cold.1
+ -[PPSMetricCollection displayEnergy]
+ -[PPSMetricCollection packageEnergy]
+ -[PPSMetricCollection setAccumSystemLoad:]
+ -[PPSMetricCollection setDisplayEnergy:]
+ -[PPSMetricCollection setPackageEnergy:]
+ -[PPSMetricMonitor _cancelUpdateTimer]
+ -[PPSMetricMonitor _cancelUpdateTimer].cold.1
+ -[PPSMetricMonitor _startUpdateTimer:]
+ -[PPSMetricMonitor setUpdateTimer:]
+ -[PPSMetricMonitor updateTimer]
+ -[PPSMetricMonitorConfiguration emitTracingSignposts]
+ -[PPSMetricMonitorConfiguration initWithMode:updateInterval:updateDelegate:emitSignposts:]
+ -[PPSMetricMonitorConfiguration initWithMode:updateInterval:updateDelegate:emitSignposts:includeBackBoardUsage:emitTracingSignposts:isHeadless:]
+ -[PPSMetricMonitorConfiguration initWithMode:updateInterval:updateDelegate:includeBackBoardUsage:emitTracingSignposts:isHeadless:]
+ -[PPSMetricMonitorConfiguration isHeadless]
+ -[PPSMetricMonitorConfiguration setEmitTracingSignposts:]
+ -[PPSMetricMonitorConfiguration setIsHeadless:]
+ -[PPSMetricMonitorService _addProcessesNeededForAccounting:]
+ -[PPSMetricMonitorService _canStartMonitoringForClient:withError:]
+ -[PPSMetricMonitorService _canStartMonitoringForClient:withError:].cold.1
+ -[PPSMetricMonitorService _canStartMonitoringForClient:withError:].cold.2
+ -[PPSMetricMonitorService _canStartMonitoringForClient:withError:].cold.3
+ -[PPSMetricMonitorService _cancelHeadlessTimeoutTimer]
+ -[PPSMetricMonitorService _cancelProcessPollingTimer].cold.1
+ -[PPSMetricMonitorService _cancelQueryTimer]
+ -[PPSMetricMonitorService _cancelQueryTimer].cold.1
+ -[PPSMetricMonitorService _checkIfProcessesAreAlive:]
+ -[PPSMetricMonitorService _checkIfProcessesAreAlive:].cold.1
+ -[PPSMetricMonitorService _collectMetricsAndUpdateHeadlessClient]
+ -[PPSMetricMonitorService _collectMetricsAndUpdateHeadlessClient].cold.1
+ -[PPSMetricMonitorService _collectMetricsAndUpdateHeadlessClient].cold.2
+ -[PPSMetricMonitorService _collectMetricsAndUpdateHeadlessClient].cold.3
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:]
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:].cold.1
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:].cold.2
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:andUpdateClient:]
+ -[PPSMetricMonitorService _collectMetricsWithTimeout:andUpdateClient:].cold.1
+ -[PPSMetricMonitorService _emitPowerSignpostWithMetric:value:]
+ -[PPSMetricMonitorService _emitPowerSignpostWithMetric:value:pid:]
+ -[PPSMetricMonitorService _findProcesses:]
+ -[PPSMetricMonitorService _findProcesses:].cold.1
+ -[PPSMetricMonitorService _handleConnectionEndedWithClient:].cold.1
+ -[PPSMetricMonitorService _isProcessAlive:]
+ -[PPSMetricMonitorService _postAccountingProcessesForSubsystem:processes:metrics:]
+ -[PPSMetricMonitorService _quantizePowerMetric:]
+ -[PPSMetricMonitorService _sendMetricMonitorTimeoutNotification]
+ -[PPSMetricMonitorService _sendMetricMonitorTimeoutNotification].cold.1
+ -[PPSMetricMonitorService _shouldAcceptNewConnection:]
+ -[PPSMetricMonitorService _shouldAcceptheadlessClientConnection:]
+ -[PPSMetricMonitorService _shouldAcceptheadlessClientConnection:].cold.1
+ -[PPSMetricMonitorService _startHeadlessTimeoutTimer]
+ -[PPSMetricMonitorService _startProcessPollingTimer:].cold.2
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:]
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:].cold.1
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:].cold.2
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:].cold.3
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:].cold.4
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:].cold.5
+ -[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:].cold.6
+ -[PPSMetricMonitorService emitPowerMetrics:ofClient:]
+ -[PPSMetricMonitorService emitPowerMetrics:ofClient:].cold.1
+ -[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:]
+ -[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:].cold.1
+ -[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:].cold.2
+ -[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:].cold.3
+ -[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:].cold.4
+ -[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:].cold.5
+ -[PPSMetricMonitorService hasHeadlessClient]
+ -[PPSMetricMonitorService headlessClientMonitoredProcesses:]
+ -[PPSMetricMonitorService headlessClientTrackedProcesses]
+ -[PPSMetricMonitorService headlessTimeoutTimer]
+ -[PPSMetricMonitorService headlessUpdateTimer]
+ -[PPSMetricMonitorService isMonitoringForHeadlessWithCompletion:]
+ -[PPSMetricMonitorService isMonitoringForHeadlessWithCompletion:].cold.1
+ -[PPSMetricMonitorService lastQueryDate]
+ -[PPSMetricMonitorService metricQueryQueue]
+ -[PPSMetricMonitorService networkingTrackPreviousMct]
+ -[PPSMetricMonitorService postAccountingProcessesScreenState]
+ -[PPSMetricMonitorService previousGPUMct]
+ -[PPSMetricMonitorService previousMct]
+ -[PPSMetricMonitorService setHasHeadlessClient:]
+ -[PPSMetricMonitorService setHeadlessClientTrackedProcesses:]
+ -[PPSMetricMonitorService setHeadlessQueryTimer:]
+ -[PPSMetricMonitorService setHeadlessQueryTimer:].cold.1
+ -[PPSMetricMonitorService setHeadlessTimeoutTimer:]
+ -[PPSMetricMonitorService setHeadlessUpdateTimer:]
+ -[PPSMetricMonitorService setLastQueryDate:]
+ -[PPSMetricMonitorService setMetricQueryQueue:]
+ -[PPSMetricMonitorService setNetworkingTrackPreviousMct:]
+ -[PPSMetricMonitorService setPostAccountingProcessesScreenState:]
+ -[PPSMetricMonitorService setPreviousGPUMct:]
+ -[PPSMetricMonitorService setPreviousMct:]
+ -[PPSMetricMonitorService setSleepWakeHistory:]
+ -[PPSMetricMonitorService setUpdateInterval:]
+ -[PPSMetricMonitorService sleepWakeHistory]
+ -[PPSMetricMonitorService startHeadlessUpdateTimer:]
+ -[PPSMetricMonitorService startMonitoringPids:forClient:withError:]
+ -[PPSMetricMonitorService stopMonitoringHeadlessClient]
+ -[PPSMetricMonitorService updateInterval]
+ -[PPSProcessMetricCollection clearMetrics]
+ -[PPSProcessMetricCollection clearMetrics].cold.1
+ -[PPSProcessMetricCollection combineWithProcessMetricCollection:].cold.1
+ -[PPSProcessMetricCollection displayPower]
+ -[PPSProcessMetricCollection locationDesiredAccuracy]
+ -[PPSProcessMetricCollection networkingPower]
+ -[PPSProcessMetricCollection qosBackground]
+ -[PPSProcessMetricCollection qosUserInitiated]
+ -[PPSProcessMetricCollection qosUserInteractive]
+ -[PPSProcessMetricCollection qosUtility]
+ -[PPSProcessMetricCollection setDisplayPower:]
+ -[PPSProcessMetricCollection setLocationDesiredAccuracy:]
+ -[PPSProcessMetricCollection setNetworkingPower:]
+ -[PPSProcessMetricCollection setQosBackground:]
+ -[PPSProcessMetricCollection setQosUserInitiated:]
+ -[PPSProcessMetricCollection setQosUserInteractive:]
+ -[PPSProcessMetricCollection setQosUtility:]
+ -[PPSProcessMetricCollection setWeightOnScreen:]
+ -[PPSProcessMetricCollection weightOnScreen]
+ -[PPSSleepWakeInterval copyWithZone:]
+ -[PPSSleepWakeInterval description]
+ -[PPSSleepWakeInterval duration]
+ -[PPSSleepWakeInterval initWithSleepTime:wakeTime:]
+ -[PPSSleepWakeInterval isEmitted]
+ -[PPSSleepWakeInterval setIsEmitted:]
+ -[PPSSleepWakeInterval setSleepTime:]
+ -[PPSSleepWakeInterval setWakeTime:]
+ -[PPSSleepWakeInterval sleepTime]
+ -[PPSSleepWakeInterval wakeTime]
+ GCC_except_table11
+ GCC_except_table175
+ GCC_except_table3
+ GCC_except_table45
+ GCC_except_table59
+ GCC_except_table64
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table8
+ GCC_except_table83
+ _NSSelectorFromString
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_PPSMetricMonitorHeadlessClient
+ _OBJC_CLASS_$_PPSSleepWakeInterval
+ _OBJC_IVAR_$_PPSClient._clientMetrics
+ _OBJC_IVAR_$_PPSClient._monitoredProcessNames
+ _OBJC_IVAR_$_PPSMetricCollection._accumSystemLoad
+ _OBJC_IVAR_$_PPSMetricCollection._displayEnergy
+ _OBJC_IVAR_$_PPSMetricCollection._packageEnergy
+ _OBJC_IVAR_$_PPSMetricMonitor._updateTimer
+ _OBJC_IVAR_$_PPSMetricMonitorConfiguration._emitTracingSignposts
+ _OBJC_IVAR_$_PPSMetricMonitorConfiguration._isHeadless
+ _OBJC_IVAR_$_PPSMetricMonitorService._hasHeadlessClient
+ _OBJC_IVAR_$_PPSMetricMonitorService._headlessClientTrackedProcesses
+ _OBJC_IVAR_$_PPSMetricMonitorService._headlessTimeoutTimer
+ _OBJC_IVAR_$_PPSMetricMonitorService._headlessUpdateTimer
+ _OBJC_IVAR_$_PPSMetricMonitorService._lastQueryDate
+ _OBJC_IVAR_$_PPSMetricMonitorService._metricQueryQueue
+ _OBJC_IVAR_$_PPSMetricMonitorService._networkingTrackPreviousMct
+ _OBJC_IVAR_$_PPSMetricMonitorService._postAccountingProcessesScreenState
+ _OBJC_IVAR_$_PPSMetricMonitorService._previousGPUMct
+ _OBJC_IVAR_$_PPSMetricMonitorService._previousMct
+ _OBJC_IVAR_$_PPSMetricMonitorService._sleepWakeHistory
+ _OBJC_IVAR_$_PPSMetricMonitorService._updateInterval
+ _OBJC_IVAR_$_PPSProcessMetricCollection._displayPower
+ _OBJC_IVAR_$_PPSProcessMetricCollection._locationDesiredAccuracy
+ _OBJC_IVAR_$_PPSProcessMetricCollection._networkingPower
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosBackground
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosUserInitiated
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosUserInteractive
+ _OBJC_IVAR_$_PPSProcessMetricCollection._qosUtility
+ _OBJC_IVAR_$_PPSProcessMetricCollection._weightOnScreen
+ _OBJC_IVAR_$_PPSSleepWakeInterval._isEmitted
+ _OBJC_IVAR_$_PPSSleepWakeInterval._sleepTime
+ _OBJC_IVAR_$_PPSSleepWakeInterval._wakeTime
+ _OBJC_METACLASS_$_PPSMetricMonitorHeadlessClient
+ _OBJC_METACLASS_$_PPSSleepWakeInterval
+ _PLEmitPowerSignpost
+ _PLEmitSystemPowerSignpost
+ _PLEmitSystemPowerSignpost.cold.1
+ _PLLogPower
+ _PLLogPower.__logObj
+ _PLLogPower.cold.1
+ _PLLogPower.onceToken
+ _PLLogPowerSignpost
+ _PLLogPowerSignpost.cold.1
+ _PLLogPowerSignpost.log
+ _PLLogPowerSignpost.onceToken
+ __OBJC_$_CLASS_METHODS_PPSMetricMonitorHeadlessClient
+ __OBJC_$_INSTANCE_METHODS_PPSSleepWakeInterval
+ __OBJC_$_INSTANCE_VARIABLES_PPSSleepWakeInterval
+ __OBJC_$_PROP_LIST_PPSSleepWakeInterval
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PPSMetricMonitorServiceHeadlessInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PPSMetricMonitorServiceHeadlessInterface
+ __OBJC_CLASS_PROTOCOLS_$_PPSSleepWakeInterval
+ __OBJC_CLASS_RO_$_PPSMetricMonitorHeadlessClient
+ __OBJC_CLASS_RO_$_PPSSleepWakeInterval
+ __OBJC_LABEL_PROTOCOL_$_PPSMetricMonitorServiceHeadlessInterface
+ __OBJC_METACLASS_RO_$_PPSMetricMonitorHeadlessClient
+ __OBJC_METACLASS_RO_$_PPSSleepWakeInterval
+ __OBJC_PROTOCOL_$_PPSMetricMonitorServiceHeadlessInterface
+ __OBJC_PROTOCOL_REFERENCE_$_PPSMetricMonitorServiceHeadlessInterface
+ ___36-[PPSMetricCollection clearMetrics:]_block_invoke
+ ___38-[PPSMetricMonitor _startUpdateTimer:]_block_invoke
+ ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.69
+ ___46+[PPSMetricMonitorHeadlessClient isMonitoring]_block_invoke
+ ___46+[PPSMetricMonitorHeadlessClient isMonitoring]_block_invoke_2
+ ___48+[PPSMetricMonitorHeadlessClient stopMonitoring]_block_invoke
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.58
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.58.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.64
+ ___50-[PPSMetricMonitorService collectMetricsOnDemand:]_block_invoke
+ ___50-[PPSMetricMonitorService collectMetricsOnDemand:]_block_invoke.cold.1
+ ___50-[PPSMetricMonitorService collectMetricsOnDemand:]_block_invoke.cold.2
+ ___50-[PPSMetricMonitorService collectMetricsOnDemand:]_block_invoke.cold.3
+ ___52+[PPSMetricMonitorHeadlessClient monitoredProcesses]_block_invoke
+ ___52+[PPSMetricMonitorHeadlessClient monitoredProcesses]_block_invoke_2
+ ___52-[PPSMetricMonitorService startHeadlessUpdateTimer:]_block_invoke
+ ___53-[PPSMetricMonitorService _startHeadlessTimeoutTimer]_block_invoke
+ ___54-[PPSMetricMonitorService _collectMetricsWithTimeout:]_block_invoke
+ ___54-[PPSMetricMonitorService _collectMetricsWithTimeout:]_block_invoke.cold.1
+ ___54-[PPSMetricMonitorService _collectMetricsWithTimeout:]_block_invoke.cold.2
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.233
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.235
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.236
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.237
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.cold.1
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke_2
+ ___55-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke
+ ___55-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke.cold.1
+ ___57-[PPSMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke
+ ___57-[PPSMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.cold.1
+ ___60-[PPSMetricMonitorService headlessClientMonitoredProcesses:]_block_invoke
+ ___61-[PPSMetricMonitorService setUpWithConfiguration:completion:]_block_invoke
+ ___63-[PPSMetricCollection combineWithMetricCollection:trackedPids:]_block_invoke
+ ___63-[PPSMetricCollection combineWithMetricCollection:trackedPids:]_block_invoke.cold.1
+ ___63-[PPSMetricCollection combineWithMetricCollection:trackedPids:]_block_invoke.cold.2
+ ___68-[PPSMetricMonitorService _updateAndTrimSleepWakeHistoryRelativeTo:]_block_invoke
+ ___70-[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:]_block_invoke
+ ___70-[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:]_block_invoke.cold.1
+ ___70-[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:]_block_invoke.cold.2
+ ___70-[PPSMetricMonitorService startMonitoringSystemMetricsWithCompletion:]_block_invoke
+ ___71-[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]_block_invoke
+ ___71-[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]_block_invoke_2
+ ___71-[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]_block_invoke_2.cold.1
+ ___71-[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]_block_invoke_2.cold.2
+ ___81-[PPSMetricMonitorService startMonitoringProcessesWithNames:withPIDs:completion:]_block_invoke
+ ___81-[PPSMetricMonitorService startMonitoringProcessesWithNames:withPIDs:completion:]_block_invoke_2
+ ___PLLogPowerSignpost_block_invoke
+ ___PLLogPower_block_invoke
+ ___block_descriptor_40_e47_B24?0"PPSSleepWakeInterval"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32r_e15_v16?0"NSSet"8lr32l8
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_40_e8_32s_e12_v24?08^B16ls32l8
+ ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e12_v24?08^B16ls32l8s40l8
+ ___block_descriptor_52_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_52_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_60_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
+ ___block_descriptor_68_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs56r64r_e5_v8?0lr56l8s32l8r64l8s48l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8r72l8s40l8s48l8s64l8s56l8
+ ___block_literal_global.103
+ ___block_literal_global.232
+ ___block_literal_global.271
+ ___block_literal_global.275
+ ___powerMetricsTotalsLogHandle_block_invoke
+ __os_signpost_emit_unreliably_with_name_impl
+ _class_copyPropertyList
+ _dispatch_assert_queue$V2
+ _headlessClientId
+ _kPPSMMConfigEmitSignposts
+ _kPPSMMConfigEmitTracingSignpost
+ _kPPSMMConfigIsHeadless
+ _kPPSMetricMonitorHeadlessServiceName
+ _mach_continuous_time
+ _notify_post
+ _objc_msgSend$_addProcessesNeededForAccounting:
+ _objc_msgSend$_canStartMonitoringForClient:withError:
+ _objc_msgSend$_cancelHeadlessTimeoutTimer
+ _objc_msgSend$_cancelQueryTimer
+ _objc_msgSend$_cancelUpdateTimer
+ _objc_msgSend$_checkIfProcessesAreAlive:
+ _objc_msgSend$_collectMetricsAndUpdateHeadlessClient
+ _objc_msgSend$_collectMetricsWithTimeout:
+ _objc_msgSend$_collectMetricsWithTimeout:andUpdateClient:
+ _objc_msgSend$_emitPowerSignpostWithMetric:value:
+ _objc_msgSend$_emitPowerSignpostWithMetric:value:pid:
+ _objc_msgSend$_findProcesses:
+ _objc_msgSend$_initConnection
+ _objc_msgSend$_isProcessAlive:
+ _objc_msgSend$_postAccountingProcessesForSubsystem:processes:metrics:
+ _objc_msgSend$_quantizePowerMetric:
+ _objc_msgSend$_sendMetricMonitorTimeoutNotification
+ _objc_msgSend$_shouldAcceptNewConnection:
+ _objc_msgSend$_shouldAcceptheadlessClientConnection:
+ _objc_msgSend$_startHeadlessTimeoutTimer
+ _objc_msgSend$_startUpdateTimer:
+ _objc_msgSend$_updateAndTrimSleepWakeHistoryRelativeTo:
+ _objc_msgSend$accumSystemLoad
+ _objc_msgSend$allKeys
+ _objc_msgSend$array
+ _objc_msgSend$batteryCapacity
+ _objc_msgSend$brightnessPercent
+ _objc_msgSend$clearMetrics
+ _objc_msgSend$clearMetrics:
+ _objc_msgSend$clientMetrics
+ _objc_msgSend$collectMetricsWithTimeout:
+ _objc_msgSend$combineWithMetricCollection:trackedPids:
+ _objc_msgSend$containsString:
+ _objc_msgSend$copy
+ _objc_msgSend$date
+ _objc_msgSend$disableAccounting
+ _objc_msgSend$displayEnergy
+ _objc_msgSend$distantPast
+ _objc_msgSend$emitPowerMetrics:ofClient:
+ _objc_msgSend$emitSignposts
+ _objc_msgSend$emitTracingSignposts
+ _objc_msgSend$emitTracingToolPowerMetrics:ofClient:
+ _objc_msgSend$enableAccounting
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$getMachTimeFromSeconds:
+ _objc_msgSend$getSecondsFromMachTime:
+ _objc_msgSend$gpuTime
+ _objc_msgSend$hasHeadlessClient
+ _objc_msgSend$headlessClientMonitoredProcesses:
+ _objc_msgSend$headlessClientTrackedProcesses
+ _objc_msgSend$headlessTimeoutTimer
+ _objc_msgSend$headlessUpdateTimer
+ _objc_msgSend$initWithConfiguration:delegate:error:
+ _objc_msgSend$initWithMode:updateInterval:updateDelegate:emitSignposts:
+ _objc_msgSend$initWithMode:updateInterval:updateDelegate:emitSignposts:includeBackBoardUsage:emitTracingSignposts:isHeadless:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$initWithSleepTime:wakeTime:
+ _objc_msgSend$isEmitted
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isHeadless
+ _objc_msgSend$isMonitoringForHeadlessWithCompletion:
+ _objc_msgSend$lastObject
+ _objc_msgSend$lastQueryDate
+ _objc_msgSend$locationDesiredAccuracy
+ _objc_msgSend$metricNormalizer
+ _objc_msgSend$metricQueryQueue
+ _objc_msgSend$monitoredProcessNames
+ _objc_msgSend$networkingPower
+ _objc_msgSend$networkingTrackPreviousMct
+ _objc_msgSend$now
+ _objc_msgSend$objCType
+ _objc_msgSend$packageEnergy
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$previousGPUMct
+ _objc_msgSend$previousMct
+ _objc_msgSend$qosBackground
+ _objc_msgSend$qosUserInitiated
+ _objc_msgSend$qosUserInteractive
+ _objc_msgSend$qosUtility
+ _objc_msgSend$queryLastSleepTimeMCT
+ _objc_msgSend$queryLastWakeTimeMCT
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$serviceName
+ _objc_msgSend$setAccumSystemLoad:
+ _objc_msgSend$setApplicationState:
+ _objc_msgSend$setBundleID:
+ _objc_msgSend$setClientMetrics:
+ _objc_msgSend$setCoalitionID:
+ _objc_msgSend$setCpuCost:
+ _objc_msgSend$setCpuSeconds:
+ _objc_msgSend$setDisplayEnergy:
+ _objc_msgSend$setEnergyCost:
+ _objc_msgSend$setEnergyOverhead:
+ _objc_msgSend$setGpuCost:
+ _objc_msgSend$setGpuTime:
+ _objc_msgSend$setHasHeadlessClient:
+ _objc_msgSend$setHeadlessTimeoutTimer:
+ _objc_msgSend$setHeadlessUpdateTimer:
+ _objc_msgSend$setIsEmitted:
+ _objc_msgSend$setLastQueryDate:
+ _objc_msgSend$setLocationCost:
+ _objc_msgSend$setLocationDesiredAccuracy:
+ _objc_msgSend$setMonitoredProcessNames:
+ _objc_msgSend$setNetworkCost:
+ _objc_msgSend$setNetworkingPower:
+ _objc_msgSend$setNetworkingTrackPreviousMct:
+ _objc_msgSend$setOngoingLocation:
+ _objc_msgSend$setPackageEnergy:
+ _objc_msgSend$setPid:
+ _objc_msgSend$setPreviousGPUMct:
+ _objc_msgSend$setPreviousMct:
+ _objc_msgSend$setProcessMetrics:
+ _objc_msgSend$setProcessName:
+ _objc_msgSend$setQosBackground:
+ _objc_msgSend$setQosUserInitiated:
+ _objc_msgSend$setQosUserInteractive:
+ _objc_msgSend$setQosUtility:
+ _objc_msgSend$setSleepTime:
+ _objc_msgSend$setSleepWakeHistory:
+ _objc_msgSend$setUpdateTimer:
+ _objc_msgSend$setWakeTime:
+ _objc_msgSend$setWeightOnScreen:
+ _objc_msgSend$sleepTime
+ _objc_msgSend$sleepWakeHistory
+ _objc_msgSend$startHeadlessUpdateTimer:
+ _objc_msgSend$startMonitoring
+ _objc_msgSend$startMonitoringPids:forClient:withError:
+ _objc_msgSend$stopMonitoringHeadlessClient
+ _objc_msgSend$timeIntervalSinceNow
+ _objc_msgSend$unionSet:
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$updateTimer
+ _objc_msgSend$wakeTime
+ _objc_msgSend$weightOnScreen
+ _objc_opt_isKindOfClass
+ _objc_retain_x4
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _powerMetricsTotalsLogHandle
+ _powerMetricsTotalsLogHandle.__logObj
+ _powerMetricsTotalsLogHandle.cold.1
+ _powerMetricsTotalsLogHandle.onceToken
+ _property_getAttributes
+ _property_getName
- -[PPSClient metricCollection]
- -[PPSClient setMetricCollection:]
- -[PPSMetricCollection combineWithMetricCollection:]
- -[PPSMetricCollection updateMetrics:forPid:]
- -[PPSMetricMonitor initWithConfiguration:delegate:error:].cold.3
- -[PPSMetricMonitorService _canStartMonitoringForClient:]
- -[PPSMetricMonitorService _canStartMonitoringForClient:].cold.1
- -[PPSMetricMonitorService _pollForProcessNames:].cold.2
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:]
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.1
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.2
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.3
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.4
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.5
- -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.6
- -[PPSMetricMonitorService collectMetricsOnDemand:].cold.2
- -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:]
- -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:].cold.1
- -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:].cold.2
- -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:].cold.3
- -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:].cold.4
- -[PPSMetricMonitorService endWithError:]
- -[PPSMetricMonitorService endWithError:].cold.1
- -[PPSMetricMonitorService setUpdateInterval:completion:]
- -[PPSMetricMonitorService setUpdateInterval:completion:].cold.1
- -[PPSMetricMonitorService startMonitoringProcessesWithName:completion:].cold.1
- -[PPSMetricMonitorService startMonitoringProcessesWithName:completion:].cold.2
- -[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:].cold.1
- -[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:].cold.2
- -[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:].cold.3
- -[PPSMetricMonitorService startMonitoringSystemMetricsWithCompletion:].cold.1
- -[PPSMetricMonitorService updateWithMetricCollection:]
- -[PPSMetricMonitorService updateWithMetricCollection:].cold.1
- GCC_except_table18
- GCC_except_table20
- GCC_except_table24
- GCC_except_table26
- GCC_except_table27
- GCC_except_table29
- GCC_except_table30
- GCC_except_table32
- GCC_except_table34
- GCC_except_table36
- GCC_except_table38
- GCC_except_table46
- GCC_except_table65
- GCC_except_table71
- _OBJC_IVAR_$_PPSClient._metricCollection
- _OUTLINED_FUNCTION_9
- ___40-[PPSMetricMonitorService endWithError:]_block_invoke
- ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.70
- ___44-[PPSMetricMonitor setUpdateInterval:error:]_block_invoke
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.60.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.61
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.65
- ___54-[PPSMetricMonitorService updateWithMetricCollection:]_block_invoke
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.87
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.88
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.cold.1
- ___block_descriptor_48_e8_32s40s_e36_v32?0"NSNumber"8"PPSClient"16^B24ls32l8s40l8
- ___block_literal_global.84
- __dispatch_main_q
- _objc_msgSend$_canStartMonitoringForClient:
- _objc_msgSend$_updateMetricCollection:metricCollection:
- _objc_msgSend$addMonitoredProcessWithPID:error:
- _objc_msgSend$changeUpdateInterval:
- _objc_msgSend$collectMetricsOnSnapshotWithError:
- _objc_msgSend$collectMetricsOnSnapshotWithError:completion:
- _objc_msgSend$combineWithMetricCollection:
- _objc_msgSend$currentUpdateInterval
- _objc_msgSend$currentUpdateMode
- _objc_msgSend$initWithMode:updateInterval:updateDelegate:
- _objc_msgSend$metricCollection
- _objc_msgSend$setMetricCollection:
- _objc_msgSend$setUpdateInterval:completion:
- _objc_msgSend$startMonitoringWithConfigurationMode:updateInterval:
- _objc_msgSend$updateMetrics:forPid:
- _objc_sync_enter
- _objc_sync_exit
CStrings:
+ "!H"
+ "%.6e"
+ "%s : no headless client is monitoring"
+ "%s called by client: %d pids: %@ "
+ "%s config : %@"
+ "%s for client: %d"
+ "%s interval: %f"
+ "%s with client: %d"
+ "%s: %d"
+ "%s: Cancelling headless timeout timer"
+ "%s: Starting headless timeout timer"
+ "%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\n"
+ "%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\nProcess name: %{public}s\nSignpost ID is PID\nGPU Power Impact = %{public, name=GPU_Power_Impact}.2f\n"
+ "%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\nProcess name: %{public}s\nSignpost ID is PID\nWifi In = %{public, name=Wifi_In, units=B}d B\nWifi Out = %{public, name=Wifi_Out, units=B}d B\nCellular In = %{public, name=Cellular_In, units=B}d B\nCellular Out = %{public, name=Cellular_Out, units=B}d B\nNetworking Power Impact = %{public, name=Networking_Power_Impact}.2f\n"
+ "%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\nSystem Power Usage (sampled power) = %{public, name=System_Power_Usage, units=%/hr}.2f %%/hr\nThermal State = %{public, name=Thermal_State}ld \nCharging Status = %{public, name=Charging_State}d \nDisplay APL = %{public, name=Display_APL}.2f \nFrame Rate = %{public, name=Frame_Rate, units =fps}.2f FPS \nDisplay Brightness Percentage = %{public, name=Display_Brightness_Percentage, units=%}.2f %%\n"
+ "-[PPSMetricCollection clearMetrics:]"
+ "-[PPSMetricCollection combineWithMetricCollection:trackedPids:]"
+ "-[PPSMetricMonitor _cancelUpdateTimer]"
+ "-[PPSMetricMonitor _startUpdateTimer:]"
+ "-[PPSMetricMonitor setUpdateInterval:error:]"
+ "-[PPSMetricMonitorService _canStartMonitoringForClient:withError:]"
+ "-[PPSMetricMonitorService _cancelHeadlessTimeoutTimer]"
+ "-[PPSMetricMonitorService _cancelProcessPollingTimer]"
+ "-[PPSMetricMonitorService _cancelQueryTimer]"
+ "-[PPSMetricMonitorService _checkIfProcessesAreAlive:]"
+ "-[PPSMetricMonitorService _collectMetricsAndUpdateHeadlessClient]"
+ "-[PPSMetricMonitorService _collectMetricsWithTimeout:]"
+ "-[PPSMetricMonitorService _collectMetricsWithTimeout:andUpdateClient:]"
+ "-[PPSMetricMonitorService _handleConnectionEndedWithClient:]"
+ "-[PPSMetricMonitorService _shouldAcceptheadlessClientConnection:]"
+ "-[PPSMetricMonitorService _startHeadlessTimeoutTimer]"
+ "-[PPSMetricMonitorService _startProcessPollingTimer:]"
+ "-[PPSMetricMonitorService emitPowerMetrics:ofClient:]"
+ "-[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:]"
+ "-[PPSMetricMonitorService isMonitoringForHeadlessWithCompletion:]"
+ "-[PPSMetricMonitorService setHeadlessQueryTimer:]"
+ "-[PPSMetricMonitorService startHeadlessUpdateTimer:]"
+ "-[PPSMetricMonitorService startMonitoringPids:forClient:withError:]"
+ "-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke"
+ "-[PPSProcessMetricCollection clearMetrics]"
+ "-[PPSProcessMetricCollection combineWithProcessMetricCollection:]"
+ "<SleepWake: Sleep=%llu, Wake=%llu>"
+ "@\"NSMutableArray\""
+ "@\"NSSet\""
+ "@24@0:8d16"
+ "@32@0:8Q16Q24"
+ "@40@0:8q16d24B32B36"
+ "@48@0:8q16d24B32B36B40B44"
+ "@52@0:8q16d24B32B36B40B44B48"
+ "Adding new sleep interval to history: Sleep=%llu, Wake=%llu"
+ "Append metrics collected to client %@ cache"
+ "Application_State"
+ "B20@0:8i16"
+ "B24@?0@\"PPSSleepWakeInterval\"8@\"NSDictionary\"16"
+ "Battery_Power_W"
+ "Battery_Temp_C"
+ "CPU_Inst"
+ "CPU_PInst"
+ "CPU_Power_W"
+ "Cell_In"
+ "Cell_Out"
+ "Cellular Power Impact = %.2f"
+ "Cellular_Power_W"
+ "Charging_Rate_mA"
+ "Clear metrics for client %d"
+ "Clear metrics for headless client"
+ "Client config is nil"
+ "Create metrics for client %@"
+ "Current Sleep/Wake History: %@"
+ "DC_Input_Power_W"
+ "DRAM_Power_W"
+ "Delegate does not respond to sleep/wake query methods."
+ "DidSleep"
+ "Disk_Read"
+ "Disk_Write"
+ "Display Power Impact = %.2f"
+ "Display_APL"
+ "Display_Power_W"
+ "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nDisplay Power      %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nLocation Desired Accuracy %8.3f %@\nQOS Utility %8.3f s   %@\nQOS Background %8.3f s   %@\nQOS User Initiated %8.3f s   %@\nQOS User Interactive %8.3f s   %@\nApplication State               %@\n%29s"
+ "Energy_Cost"
+ "Energy_Overhead"
+ "Failed to post metricmonitor timeout notification(attempt %d). Status: %d Retrying"
+ "Failed to post notification after %d attempts. Giving up."
+ "GPU_Cost"
+ "GPU_Power_W"
+ "GPU_Time"
+ "Induced_Thermal_State"
+ "Location_Cost"
+ "New client connection from PID %d. Current clients: %@"
+ "Ongoing_Location"
+ "Only one headless client is allowed"
+ "Other_SoC_Power_W"
+ "PPSMetricMonitorConfig(mode: %ld updateInterval: %f updateDelegate: %d includeBackBoardUsage: %d isHeadless: %d emitTracingSignposts: %d emitSignposts: %d))"
+ "PPSMetricMonitorHeadlessClient"
+ "PPSMetricMonitorServiceHeadlessInterface"
+ "PPSSleepWakeInterval"
+ "Per-app GPU power impact"
+ "Per-app networking power"
+ "Per-app subsystem power"
+ "Power"
+ "PowerMetrics"
+ "Process %@ has exited"
+ "Process name: %{public}s\nSignpost ID is PID\nCPU Power Impact = %{public, name=CPU_Power_Impact}.2f\nGPU Power Impact = %{public, name=GPU_Power_Impact}.2f\nQOS Utility = %{public, name=QOS_Utility, units=s}.2f s\nQOS Background = %{public, name=QOS_Background, units=s}.2f s\nQOS User Initiated = %{public, name=QOS_User_Initiated, units=s}.2f s\nQOS User Interactive = %{public, name=QOS_User_Interactive, units=s}.2f s\nCPU Instructions = %{public, name=CPU_Instructions}lld \nANE Time = %{public, name=ANE_Time, units=s}.2f s \nLocation Desired Accuracy = %{public, name=Location_Desired_Accuracy}.2f \nApplication State = %{public, name=Application_State}d \nDisplay Power Impact = %{public, name=Display_Power_Impact}.2f\n%{public, signpost.description:begin_time}llu\n%{public, signpost.description:end_time}llu\n"
+ "Q"
+ "Queried sleep time (%llu) is older than last known sleep time (%llu). Ignoring."
+ "Skin_Temp_C"
+ "Successfully posted metricmonitor timeout notification."
+ "SystemMetrics"
+ "System_Load_Power_W"
+ "T@\"NSDate\",&,V_lastQueryDate"
+ "T@\"NSMutableArray\",&,N,V_sleepWakeHistory"
+ "T@\"NSMutableDictionary\",&,V_headlessClientTrackedProcesses"
+ "T@\"NSMutableSet\",&,V_monitoredProcessNames"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_metricQueryQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_headlessTimeoutTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_headlessUpdateTimer"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_updateTimer"
+ "T@\"NSSet\",&,V_postAccountingProcessesScreenState"
+ "T@\"PPSMetricCollection\",&,V_clientMetrics"
+ "T@\"PPSMetricSample\",&,N,V_accumSystemLoad"
+ "T@\"PPSMetricSample\",&,N,V_displayEnergy"
+ "T@\"PPSMetricSample\",&,N,V_locationDesiredAccuracy"
+ "T@\"PPSMetricSample\",&,N,V_networkingPower"
+ "T@\"PPSMetricSample\",&,N,V_packageEnergy"
+ "T@\"PPSMetricSample\",&,N,V_qosBackground"
+ "T@\"PPSMetricSample\",&,N,V_qosUserInitiated"
+ "T@\"PPSMetricSample\",&,N,V_qosUserInteractive"
+ "T@\"PPSMetricSample\",&,N,V_qosUtility"
+ "T@\"PPSMetricSample\",&,N,V_weightOnScreen"
+ "TB,N,V_emitTracingSignposts"
+ "TB,N,V_isHeadless"
+ "TB,V_hasHeadlessClient"
+ "TB,V_isEmitted"
+ "TQ,N,V_sleepTime"
+ "TQ,N,V_wakeTime"
+ "TQ,V_networkingTrackPreviousMct"
+ "TQ,V_previousGPUMct"
+ "TQ,V_previousMct"
+ "Td,V_updateInterval"
+ "The timeout was reached, stopping timer"
+ "Thermal_State"
+ "Trimed %lu old sleep/wake intervals."
+ "Update interval smaller than 0.2 s is not supported; defaulting to 0.2 s"
+ "Updating wake time for last sleep interval: Sleep=%llu, NewWake=%llu"
+ "WiFi Power Impact = %.2f"
+ "WiFi_In"
+ "WiFi_Out"
+ "WiFi_Power_W"
+ "Zero duration interval [%llu -> %llu], skipping emission."
+ "_accumSystemLoad"
+ "_addProcessesNeededForAccounting:"
+ "_canStartMonitoringForClient:withError:"
+ "_cancelHeadlessTimeoutTimer"
+ "_cancelQueryTimer"
+ "_cancelUpdateTimer"
+ "_checkIfProcessesAreAlive:"
+ "_clientMetrics"
+ "_collectMetricsAndUpdateHeadlessClient"
+ "_collectMetricsWithTimeout:"
+ "_collectMetricsWithTimeout:andUpdateClient:"
+ "_displayEnergy"
+ "_emitPowerSignpostWithMetric:value:"
+ "_emitPowerSignpostWithMetric:value:pid:"
+ "_emitTracingSignposts"
+ "_findProcesses:"
+ "_hasHeadlessClient"
+ "_headlessClientTrackedProcesses"
+ "_headlessTimeoutTimer"
+ "_headlessUpdateTimer"
+ "_initConnection"
+ "_isEmitted"
+ "_isHeadless"
+ "_isProcessAlive:"
+ "_lastQueryDate"
+ "_locationDesiredAccuracy"
+ "_metricQueryQueue"
+ "_monitoredProcessNames"
+ "_networkingPower"
+ "_networkingTrackPreviousMct"
+ "_packageEnergy"
+ "_postAccountingProcessesForSubsystem:processes:metrics:"
+ "_postAccountingProcessesScreenState"
+ "_previousGPUMct"
+ "_previousMct"
+ "_qosBackground"
+ "_qosUserInitiated"
+ "_qosUserInteractive"
+ "_qosUtility"
+ "_quantizePowerMetric:"
+ "_sendMetricMonitorTimeoutNotification"
+ "_shouldAcceptNewConnection:"
+ "_shouldAcceptheadlessClientConnection:"
+ "_sleepTime"
+ "_sleepWakeHistory"
+ "_startHeadlessTimeoutTimer"
+ "_startUpdateTimer:"
+ "_updateAndTrimSleepWakeHistoryRelativeTo:"
+ "_updateTimer"
+ "_wakeTime"
+ "_weightOnScreen"
+ "accumSystemLoad"
+ "allKeys"
+ "array"
+ "batteryCapacity"
+ "brightnessPercent"
+ "clearMetrics"
+ "clearMetrics:"
+ "clientMetrics"
+ "collectMetricsWithTimeout:"
+ "com.apple.PerfPowerMetricMonitor.monitorQueue"
+ "com.apple.PerfPowerMetricMonitorHeadless.xpc"
+ "com.apple.perfpowermetricmonitor.monitoring_timed_out"
+ "com.apple.powerlog"
+ "combineWithMetricCollection:trackedPids:"
+ "containsString:"
+ "copy"
+ "d24@0:8d16"
+ "d40@0:8q16@24@32"
+ "date"
+ "disableAccounting"
+ "displayEnergy"
+ "distantPast"
+ "duration"
+ "emitPowerMetrics:ofClient:"
+ "emitTracingSignpost"
+ "emitTracingSignposts"
+ "emitTracingToolPowerMetrics:ofClient:"
+ "enableAccounting"
+ "enumerateObjectsUsingBlock:"
+ "filteredArrayUsingPredicate:"
+ "getMachTimeFromSeconds:"
+ "getSecondsFromMachTime:"
+ "hasHeadlessClient"
+ "headlessClientMonitoredProcesses:"
+ "headlessClientTrackedProcesses"
+ "headlessTimeoutTimer"
+ "headlessUpdateTimer"
+ "initWithMode:updateInterval:updateDelegate:emitSignposts:"
+ "initWithMode:updateInterval:updateDelegate:emitSignposts:includeBackBoardUsage:emitTracingSignposts:isHeadless:"
+ "initWithMode:updateInterval:updateDelegate:includeBackBoardUsage:emitTracingSignposts:isHeadless:"
+ "initWithObjects:"
+ "initWithSleepTime:wakeTime:"
+ "isEmitted"
+ "isEqualToString:"
+ "isHeadless"
+ "isMonitoring"
+ "isMonitoringForHeadlessWithCompletion:"
+ "lastObject"
+ "lastQueryDate"
+ "locationDesiredAccuracy"
+ "metric Monitor is ready"
+ "metricNormalizer"
+ "metricQueryQueue"
+ "metrics collected %@"
+ "monitoredProcessNames"
+ "monitoredProcesses"
+ "networkingPower"
+ "networkingTrackPreviousMct"
+ "now"
+ "objCType"
+ "packageEnergy"
+ "postAccountingProcessesScreenState"
+ "predicateWithBlock:"
+ "previousGPUMct"
+ "previousMct"
+ "qosBackground"
+ "qosUserInitiated"
+ "qosUserInteractive"
+ "qosUtility"
+ "queryLastSleepTimeMCT"
+ "queryLastWakeTimeMCT"
+ "removeAllObjects"
+ "serviceName"
+ "setAccumSystemLoad:"
+ "setClientMetrics:"
+ "setDisplayEnergy:"
+ "setEmitTracingSignposts:"
+ "setHasHeadlessClient:"
+ "setHeadlessClientTrackedProcesses:"
+ "setHeadlessQueryTimer:"
+ "setHeadlessTimeoutTimer:"
+ "setHeadlessUpdateTimer:"
+ "setIsEmitted:"
+ "setIsHeadless:"
+ "setLastQueryDate:"
+ "setLocationDesiredAccuracy:"
+ "setMetricQueryQueue:"
+ "setMonitoredProcessNames:"
+ "setNetworkingPower:"
+ "setNetworkingTrackPreviousMct:"
+ "setPackageEnergy:"
+ "setPostAccountingProcessesScreenState:"
+ "setPreviousGPUMct:"
+ "setPreviousMct:"
+ "setQosBackground:"
+ "setQosUserInitiated:"
+ "setQosUserInteractive:"
+ "setQosUtility:"
+ "setSleepTime:"
+ "setSleepWakeHistory:"
+ "setUpdateTimer:"
+ "setWakeTime:"
+ "setWeightOnScreen:"
+ "sleepTime"
+ "sleepWakeHistory"
+ "startHeadlessUpdateTimer:"
+ "startMonitoring"
+ "startMonitoringPids:forClient:withError:"
+ "startMonitoringProcessesWithNames:config:error:"
+ "startMonitoringProcessesWithPID:config:error:"
+ "startMonitoringSystemMetricsWithConfig:error:"
+ "stopMonitoringHeadlessClient"
+ "timeIntervalSinceNow"
+ "tracingConfiguration:"
+ "unionSet:"
+ "unsignedLongLongValue"
+ "unsupported config"
+ "updateTimer"
+ "v12@?0B8"
+ "v16@?0@\"NSSet\"8"
+ "v24@0:8@?<v@?@\"NSSet\">16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8Q16"
+ "v24@?0@8^B16"
+ "v28@0:8i16@20"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24^@32"
+ "videocodecd"
+ "wakeTime"
+ "weightOnScreen"
+ "{\"metric\":\"%{public}@\",\"value\":%{public}@,\"pid\":%{public}@}"
+ "{\"metric\":\"%{public}@\",\"value\":%{public}@}"
- "%s called by client (monitored pids): %@"
- "%s called by client: %d interval: %@"
- "-[PPSMetricMonitorService _updateMetricCollection:metricCollection:]"
- "-[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:]"
- "-[PPSMetricMonitorService endWithError:]"
- "-[PPSMetricMonitorService setUpdateInterval:completion:]"
- "-[PPSMetricMonitorService updateWithMetricCollection:]"
- "All clients disconnected"
- "Combining client metric collection"
- "Copying client metric collection"
- "Copying process metrics for monitored PID (%d)"
- "Energy Cost        %8.3f     %@\nEnergy Overhead    %8.3f     %@\nCPU Cost           %8.3f     %@\nCPU Seconds        %8.3f s   %@\nCPU Energy         %8.3f nJ  %@\nGPU Cost           %8.3f     %@\nNetwork Cost       %8d     %@\nWiFi In            %8d B   %@\nWiFi Out           %8d B   %@\nCell In            %8d B   %@\nCell Out           %8d B   %@\nLocation Cost      %8.3f     %@\nOngoing Location   %8s     %@\nApplication State               %@\n%29s"
- "Found client for pid %d -> %@"
- "PPSMetricMonitorConfig(mode: %ld updateInterval: %f updateDelegate: %d includeBackBoardUsage: %d))"
- "Rejecting client %d due to incompatible mode (current: %ld; requested: %ld)"
- "Rejecting client %d due to incompatible update interval (current: %f; requested: %f)"
- "Rejecting client %d with mode updateOnSnapshot; already running"
- "Rejecting client %d with mode updateOnStop; already running"
- "Service is busy"
- "T@\"PPSMetricCollection\",&,V_metricCollection"
- "Unable to change update interval while multiple clients are connected"
- "_canStartMonitoringForClient:"
- "_metricCollection"
- "_updateMetricCollection:metricCollection:"
- "addMonitoredProcessWithPID:error:"
- "changeUpdateInterval:"
- "collectMetricsOnSnapshotWithError:"
- "collectMetricsOnSnapshotWithError:completion:"
- "combineWithMetricCollection:"
- "currentUpdateInterval"
- "currentUpdateMode"
- "metricCollection"
- "setMetricCollection:"
- "setUpdateInterval:completion:"
- "startMonitoringWithConfigurationMode:updateInterval:"
- "updateMetrics:forPid:"
- "v32@0:8^@16@?24"
- "v32@0:8^@16@?<v@?@\"PPSMetricCollection\"@\"NSError\">24"

```
