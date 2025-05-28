## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-1851.102.4.0.0
-  __TEXT.__text: 0x8ef0
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x9b0
+1851.120.59.0.0
+  __TEXT.__text: 0xbfdc
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0xad4
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x324
-  __TEXT.__cstring: 0xb0e
-  __TEXT.__oslogstring: 0x59a
+  __TEXT.__gcc_except_tab: 0x3ec
+  __TEXT.__cstring: 0xca7
+  __TEXT.__oslogstring: 0x872
   __TEXT.__ustring: 0x5c6
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methname: 0x1f64
-  __TEXT.__objc_methtype: 0x45d
-  __TEXT.__objc_stubs: 0x1380
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x2b0
+  __TEXT.__unwind_info: 0x364
+  __TEXT.__objc_classname: 0x126
+  __TEXT.__objc_methname: 0x2382
+  __TEXT.__objc_methtype: 0x596
+  __TEXT.__objc_stubs: 0x1b80
+  __DATA_CONST.__got: 0x38
+  __DATA_CONST.__const: 0x338
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x13e0
-  __DATA_CONST.__objc_selrefs: 0x730
+  __DATA_CONST.__objc_const: 0x1530
+  __DATA_CONST.__objc_selrefs: 0x820
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x98
+  __DATA_CONST.__objc_classrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_const: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__auth_got: 0x280
   __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x104
+  __DATA.__objc_ivar: 0x118
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0xa0

   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 298
-  Symbols:   1072
-  CStrings:  604
+  Functions: 344
+  Symbols:   1261
+  CStrings:  679
 
Symbols:
+ -[PPSClient metricCollection]
+ -[PPSClient requestedProcessNames]
+ -[PPSClient setMetricCollection:]
+ -[PPSClient setRequestedProcessNames:]
+ -[PPSMetricCollection combineWithMetricCollection:]
+ -[PPSMetricCollection sampleTime]
+ -[PPSMetricCollection setSampleTime:]
+ -[PPSMetricCollection updateMetrics:forPid:]
+ -[PPSMetricMonitor collectMetricsOnDemand]
+ -[PPSMetricMonitor collectMetricsOnSnapshot:]
+ -[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:]
+ -[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:].cold.1
+ -[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:].cold.2
+ -[PPSMetricMonitorService _cancelProcessPollingTimer]
+ -[PPSMetricMonitorService _pollForProcessNames:]
+ -[PPSMetricMonitorService _pollForProcessNames:].cold.1
+ -[PPSMetricMonitorService _pollForProcessNames:].cold.2
+ -[PPSMetricMonitorService _startProcessPollingTimer:]
+ -[PPSMetricMonitorService _startProcessPollingTimer:].cold.1
+ -[PPSMetricMonitorService _updateMetricCollection:metricCollection:]
+ -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.1
+ -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.2
+ -[PPSMetricMonitorService _updateMetricCollection:metricCollection:].cold.3
+ -[PPSMetricMonitorService collectMetricsOnDemand:]
+ -[PPSMetricMonitorService collectMetricsOnDemand:].cold.1
+ -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:]
+ -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:].cold.1
+ -[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:].cold.2
+ -[PPSMetricMonitorService fullProcessNameForPid:]
+ -[PPSMetricMonitorService processPollingRepeatingTimer]
+ -[PPSMetricMonitorService setProcessPollingRepeatingTimer:]
+ -[PPSMetricMonitorService startMonitoringProcessesWithNames:withPIDs:completion:]
+ -[PPSMetricMonitorService startMonitoringProcessesWithNames:withPIDs:completion:].cold.1
+ -[PPSProcessMetricCollection combineWithProcessMetricCollection:]
+ -[PPSProcessMetricCollection sampleTime]
+ -[PPSProcessMetricCollection setSampleTime:]
+ GCC_except_table19
+ GCC_except_table24
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table38
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table46
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_PPSClient._metricCollection
+ _OBJC_IVAR_$_PPSClient._requestedProcessNames
+ _OBJC_IVAR_$_PPSMetricCollection._sampleTime
+ _OBJC_IVAR_$_PPSMetricMonitorService._processPollingRepeatingTimer
+ _OBJC_IVAR_$_PPSProcessMetricCollection._sampleTime
+ ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.64
+ ___42-[PPSMetricMonitor collectMetricsOnDemand]_block_invoke
+ ___42-[PPSMetricMonitor collectMetricsOnDemand]_block_invoke_2
+ ___45-[PPSMetricMonitor collectMetricsOnSnapshot:]_block_invoke
+ ___45-[PPSMetricMonitor collectMetricsOnSnapshot:]_block_invoke_2
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.53
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.53.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.54
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.54.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.55
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.59
+ ___53-[PPSMetricMonitorService _startProcessPollingTimer:]_block_invoke
+ ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.87
+ ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.88
+ ___65-[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:]_block_invoke
+ ___65-[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e41_v24?0"PPSMetricCollection"8"NSError"16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_literal_global.84
+ __dispatch_main_q
+ __dispatch_source_type_timer
+ _basename
+ _bzero
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_time
+ _free
+ _kPPSProcessSampleTimeKey
+ _kPPSSampleTimeKey
+ _malloc_type_malloc
+ _memset
+ _objc_msgSend$_cancelProcessPollingTimer
+ _objc_msgSend$_pollForProcessNames:
+ _objc_msgSend$_startProcessPollingTimer:
+ _objc_msgSend$_updateMetricCollection:metricCollection:
+ _objc_msgSend$addMonitoredProcessesWithPIDs:error:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$bytesRead
+ _objc_msgSend$bytesWritten
+ _objc_msgSend$collectMetricsOnDemand
+ _objc_msgSend$collectMetricsOnDemand:
+ _objc_msgSend$collectMetricsOnSnapshotWithError:
+ _objc_msgSend$collectMetricsOnSnapshotWithError:completion:
+ _objc_msgSend$combineWithMetricCollection:
+ _objc_msgSend$combineWithProcessMetricCollection:
+ _objc_msgSend$cpuInstructions
+ _objc_msgSend$cpuPInstructions
+ _objc_msgSend$fullProcessNameForPid:
+ _objc_msgSend$metricCollection
+ _objc_msgSend$minusSet:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$processPollingRepeatingTimer
+ _objc_msgSend$removeObject:
+ _objc_msgSend$requestedProcessNames
+ _objc_msgSend$sampleTime
+ _objc_msgSend$sampleWithValue:timestamp:
+ _objc_msgSend$set
+ _objc_msgSend$setBatteryPower:
+ _objc_msgSend$setBatteryTemperature:
+ _objc_msgSend$setBytesRead:
+ _objc_msgSend$setBytesWritten:
+ _objc_msgSend$setCellIn:
+ _objc_msgSend$setCellOut:
+ _objc_msgSend$setCellularPower:
+ _objc_msgSend$setChargingRate:
+ _objc_msgSend$setCpuInstructions:
+ _objc_msgSend$setCpuPInstructions:
+ _objc_msgSend$setCpuPower:
+ _objc_msgSend$setDcInputPower:
+ _objc_msgSend$setDisplayAPL:
+ _objc_msgSend$setDisplayCost:
+ _objc_msgSend$setDisplayFPS:
+ _objc_msgSend$setDisplayPower:
+ _objc_msgSend$setDramPower:
+ _objc_msgSend$setGpuPower:
+ _objc_msgSend$setInducedThermalPressure:
+ _objc_msgSend$setIsSystemPowerAvailableWhileCharging:
+ _objc_msgSend$setMetricCollection:
+ _objc_msgSend$setOtherSocPower:
+ _objc_msgSend$setProcessPollingRepeatingTimer:
+ _objc_msgSend$setRequestedProcessNames:
+ _objc_msgSend$setSampleTime:
+ _objc_msgSend$setSkinTemperature:
+ _objc_msgSend$setSystemLoadPower:
+ _objc_msgSend$setThermalPressure:
+ _objc_msgSend$setWifiAWDLRange:
+ _objc_msgSend$setWifiAWDLStatus:
+ _objc_msgSend$setWifiIn:
+ _objc_msgSend$setWifiOut:
+ _objc_msgSend$setWifiPower:
+ _objc_msgSend$startMonitoringProcessesWithNames:withPIDs:completion:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$updateMetrics:forPid:
+ _objc_msgSend$wifiAWDLRange
+ _objc_msgSend$wifiAWDLStatus
+ _objc_opt_new
+ _proc_listpids
+ _proc_pidpath
- GCC_except_table14
- GCC_except_table21
- GCC_except_table23
- GCC_except_table31
- GCC_except_table37
- ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.55
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.44
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.44.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.45
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.45.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.46
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.50
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.68
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.69
- ___block_literal_global.65
CStrings:
+ "\x06"
+ "\x12"
+ "\x1f\x01$"
+ "\x1f\x06"
+ "%s %@ %@"
+ "%s called by client (monitored pids): %@"
+ "%s called by client: %d process names: %@, PIDs: %@ "
+ "-[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:]"
+ "-[PPSMetricMonitorService _updateMetricCollection:metricCollection:]"
+ "-[PPSMetricMonitorService collectMetricsOnDemand:]"
+ "-[PPSMetricMonitorService collectMetricsOnSnapshotWithError:completion:]"
+ "-[PPSMetricMonitorService startMonitoringProcessesWithNames:withPIDs:completion:]"
+ "@\"NSMutableSet\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "@\"PPSMetricCollection\""
+ "@20@0:8i16"
+ "@24@0:8^@16"
+ "B40@0:8@16@24^@32"
+ "Combining client metric collection"
+ "Combining process metrics for monitored PID (%d)"
+ "Copying client metric collection"
+ "Copying process metrics for monitored PID (%d)"
+ "Failed to find matching PID for process name(s): %@"
+ "Found PID (%d) for %@. Adding to monitor."
+ "Found procs :%@, pending:%@"
+ "No process metrics found for PID (%d)."
+ "Polling for matches to requested process names."
+ "Rejecting client %d with mode updateOnSnapshot; already running"
+ "Repeating timer for polling process launch armed."
+ "Stopping polling because we found all requested process names."
+ "T@\"NSMutableSet\",&,V_monitoredPIDs"
+ "T@\"NSMutableSet\",&,V_requestedProcessNames"
+ "T@\"NSNumber\",&,N,V_sampleTime"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_processPollingRepeatingTimer"
+ "T@\"PPSMetricCollection\",&,V_metricCollection"
+ "__sampleTime__"
+ "_cancelProcessPollingTimer"
+ "_metricCollection"
+ "_pollForProcessNames:"
+ "_processPollingRepeatingTimer"
+ "_requestedProcessNames"
+ "_sampleTime"
+ "_startProcessPollingTimer:"
+ "_updateMetricCollection:metricCollection:"
+ "addMonitoredProcessesWithPIDs:error:"
+ "addObjectsFromArray:"
+ "collectMetricsOnDemand"
+ "collectMetricsOnDemand:"
+ "collectMetricsOnSnapshot:"
+ "collectMetricsOnSnapshotWithError:"
+ "collectMetricsOnSnapshotWithError:completion:"
+ "combineWithMetricCollection:"
+ "combineWithProcessMetricCollection:"
+ "fullProcessNameForPid:"
+ "metricCollection"
+ "minusSet:"
+ "objectForKey:"
+ "processPollingRepeatingTimer"
+ "removeObject:"
+ "requestedProcessNames"
+ "sampleTime"
+ "set"
+ "setMetricCollection:"
+ "setProcessPollingRepeatingTimer:"
+ "setRequestedProcessNames:"
+ "setSampleTime:"
+ "startMonitoringProcessesWithNames:PIDs:error:"
+ "startMonitoringProcessesWithNames:withPIDs called while already monitoring"
+ "startMonitoringProcessesWithNames:withPIDs:completion:"
+ "stringWithUTF8String:"
+ "updateMetrics:forPid:"
+ "v24@0:8@?<v@?@\"PPSMetricCollection\"@\"NSError\">16"
+ "v24@?0@\"PPSMetricCollection\"8@\"NSError\"16"
+ "v32@0:8@16@24"
+ "v32@0:8^@16@?24"
+ "v32@0:8^@16@?<v@?@\"PPSMetricCollection\"@\"NSError\">24"
+ "v40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@?32"
- "\x04"
- "\x1f\x01#"
- "\x1f\x05"
- "T@\"NSArray\",&,V_monitoredPIDs"

```
