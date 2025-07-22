## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-2964.0.64.0.0
-  __TEXT.__text: 0x184d0
-  __TEXT.__auth_stubs: 0x5c0
-  __TEXT.__objc_methlist: 0x1474
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x984
-  __TEXT.__cstring: 0x18f8
-  __TEXT.__oslogstring: 0x15fa
+2964.0.107.502.1
+  __TEXT.__text: 0x18364
+  __TEXT.__auth_stubs: 0x600
+  __TEXT.__objc_methlist: 0x14b4
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x9a0
+  __TEXT.__cstring: 0xf2c
+  __TEXT.__oslogstring: 0x1b9a
   __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methname: 0x3b9c
+  __TEXT.__objc_methname: 0x3c60
   __TEXT.__objc_methtype: 0x660
-  __TEXT.__objc_stubs: 0x30c0
+  __TEXT.__objc_stubs: 0x3140
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__const: 0x678
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe10
+  __DATA_CONST.__objc_selrefs: 0xe40
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x240
-  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x20c8
+  __AUTH_CONST.__cfstring: 0x1340
+  __AUTH_CONST.__objc_const: 0x2128
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x300
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F494120E-42F8-3FD3-9FEE-FBA4126EBD52
-  Functions: 585
-  Symbols:   2052
-  CStrings:  1275
+  UUID: 7F81BA7F-7994-3493-9903-01DB57737048
+  Functions: 587
+  Symbols:   2073
+  CStrings:  1269
 
Symbols:
+ -[PPSMetricMonitorService _getHeadlessClientStatus]
+ -[PPSMetricMonitorService postAccountingAudio]
+ -[PPSMetricMonitorService setPostAccountingAudio:]
+ -[PPSProcessMetricCollection audioActive]
+ -[PPSProcessMetricCollection setAudioActive:]
+ GCC_except_table108
+ GCC_except_table185
+ GCC_except_table38
+ GCC_except_table44
+ GCC_except_table62
+ GCC_except_table67
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table86
+ _OBJC_IVAR_$_PPSMetricMonitorService._postAccountingAudio
+ _OBJC_IVAR_$_PPSProcessMetricCollection._audioActive
+ ___51-[PPSMetricMonitorService _getHeadlessClientStatus]_block_invoke
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.248
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.249
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.250
+ ___55-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke.112
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_60_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.106
+ ___block_literal_global.245
+ ___block_literal_global.286
+ ___block_literal_global.290
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_msgSend$_getHeadlessClientStatus
+ _objc_msgSend$audioActive
+ _objc_msgSend$isPluggedIn
+ _objc_msgSend$setAudioActive:
+ _objc_retain_x25
- GCC_except_table106
- GCC_except_table181
- GCC_except_table42
- GCC_except_table60
- GCC_except_table65
- GCC_except_table69
- GCC_except_table73
- GCC_except_table84
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.243
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.245
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.247
- ___55-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke.109
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_52_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_literal_global.103
- ___block_literal_global.242
- ___block_literal_global.283
- ___block_literal_global.287
CStrings:
+ "!J"
+ "Appending metric collection snapshot to cache"
+ "Appending process metric collection snapshot to cache"
+ "Can start monitoring was called by client: %d"
+ "Cancelling headless timeout timer"
+ "Cancelling process polling timer"
+ "Cancelling query timer"
+ "Cancelling update timer"
+ "Check if processes are alive: %d"
+ "Checking for headless monitoring"
+ "Checking if headless client connection should be accepted"
+ "Clearing metrics"
+ "Collect metrics on demand was called by client: %d"
+ "Collect metrics with timeout was called by client: %d"
+ "Collecting metrics and updating headless client"
+ "Collecting metrics on demand"
+ "Collecting metrics with timeout %d"
+ "Connecting to perfpowermetricd"
+ "Connection ended with client: %d"
+ "Emitting power metrics"
+ "Emitting tracing tool power metrics"
+ "Finish monitoring and send metrics was called by client: %d"
+ "Initializing with config : %@"
+ "No headless client is monitoring"
+ "Resumed XPC connection to perfpowermetricd"
+ "Setting up XPC connection with config: %@"
+ "Setting update interval to %f s"
+ "Setup was called by client: %d config: %@"
+ "Start monitoring pids was called by client: %d pids: %@ "
+ "Start monitoring process with pid %d"
+ "Start monitoring process with the name: %@"
+ "Start monitoring processes with names and pids was called by client: %d process names: %@, PIDs: %@ "
+ "Start monitoring processes with names and pids: %@ %@"
+ "Start monitoring processes with names was called by client: %d processName: %@ "
+ "Start monitoring processes with pids %@"
+ "Start monitoring processes with pids was called by client: %d PID: %@"
+ "Start monitoring processes with the names: %@"
+ "Start monitoring system metrics was called by client: %d"
+ "Start monitoring system metrics with error"
+ "Starting XPC listener"
+ "Starting headless query timer with interval: %f"
+ "Starting headless timeout timer"
+ "Starting headless update timer with interval: %f"
+ "Starting process polling timer for client: %d"
+ "Starting update timer with interval: %f"
+ "Stop monitoring headless client"
+ "Stopping monitoring"
+ "T@\"NSSet\",&,V_postAccountingAudio"
+ "TB,N,V_audioActive"
+ "XPC connection to perfpowermetricd interrupted"
+ "XPC connection to perfpowermetricd invalidated"
+ "_audioActive"
+ "_getHeadlessClientStatus"
+ "_postAccountingAudio"
+ "audioActive"
+ "audiomxd"
+ "isPluggedIn"
+ "postAccountingAudio"
+ "setAudioActive:"
+ "setPostAccountingAudio:"
- "!I"
- "%s"
- "%s %@"
- "%s %@ %@"
- "%s %d"
- "%s : no headless client is monitoring"
- "%s called by client: %d"
- "%s called by client: %d PID: %@"
- "%s called by client: %d config: %@"
- "%s called by client: %d pids: %@ "
- "%s called by client: %d process names: %@, PIDs: %@ "
- "%s called by client: %d processName: %@ "
- "%s config : %@"
- "%s for client: %d"
- "%s interval: %f"
- "%s with client: %d"
- "%s: %d"
- "%s: Cancelling headless timeout timer"
- "%s: Starting headless timeout timer"
- "-[PPSMetricCollection clearMetrics:]"
- "-[PPSMetricCollection combineWithMetricCollection:trackedPids:]"
- "-[PPSMetricMonitor _cancelUpdateTimer]"
- "-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]"
- "-[PPSMetricMonitor _startUpdateTimer:]"
- "-[PPSMetricMonitor collectMetricsOnDemand]"
- "-[PPSMetricMonitor initWithConfiguration:delegate:error:]"
- "-[PPSMetricMonitor setUpdateInterval:error:]"
- "-[PPSMetricMonitor startMonitoringProcessWithName:error:]"
- "-[PPSMetricMonitor startMonitoringProcessWithPID:error:]"
- "-[PPSMetricMonitor startMonitoringProcessesWithName:error:]"
- "-[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:]"
- "-[PPSMetricMonitor startMonitoringProcessesWithPID:error:]"
- "-[PPSMetricMonitor startMonitoringSystemMetricsWithError:]"
- "-[PPSMetricMonitor stopMonitoring]"
- "-[PPSMetricMonitorService _canStartMonitoringForClient:withError:]"
- "-[PPSMetricMonitorService _cancelHeadlessTimeoutTimer]"
- "-[PPSMetricMonitorService _cancelProcessPollingTimer]"
- "-[PPSMetricMonitorService _cancelQueryTimer]"
- "-[PPSMetricMonitorService _checkIfProcessesAreAlive:]"
- "-[PPSMetricMonitorService _collectMetricsAndUpdateHeadlessClient]"
- "-[PPSMetricMonitorService _collectMetricsWithTimeout:]"
- "-[PPSMetricMonitorService _collectMetricsWithTimeout:andUpdateClient:]"
- "-[PPSMetricMonitorService _handleConnectionEndedWithClient:]"
- "-[PPSMetricMonitorService _shouldAcceptheadlessClientConnection:]"
- "-[PPSMetricMonitorService _startHeadlessTimeoutTimer]"
- "-[PPSMetricMonitorService _startProcessPollingTimer:]"
- "-[PPSMetricMonitorService collectMetricsOnDemand:]"
- "-[PPSMetricMonitorService emitPowerMetrics:ofClient:]"
- "-[PPSMetricMonitorService emitTracingToolPowerMetrics:ofClient:]"
- "-[PPSMetricMonitorService finishMonitoringAndSendMetrics]"
- "-[PPSMetricMonitorService isMonitoringForHeadlessWithCompletion:]"
- "-[PPSMetricMonitorService setHeadlessQueryTimer:]"
- "-[PPSMetricMonitorService setUpWithConfiguration:completion:]"
- "-[PPSMetricMonitorService startHeadlessUpdateTimer:]"
- "-[PPSMetricMonitorService startMonitoringPids:forClient:withError:]"
- "-[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]"
- "-[PPSMetricMonitorService startMonitoringProcessesWithNames:withPIDs:completion:]"
- "-[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:]"
- "-[PPSMetricMonitorService startMonitoringSystemMetricsWithCompletion:]"
- "-[PPSMetricMonitorService startXPCListener]"
- "-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke"
- "-[PPSProcessMetricCollection clearMetrics]"
- "-[PPSProcessMetricCollection combineWithProcessMetricCollection:]"
- "Connecting to powerlogHelperd"
- "Resumed XPC connection to powerlogHelperd"
- "XPC connection to powerlogHelperd interrupted"
- "XPC connection to powerlogHelperd invalidated"

```
