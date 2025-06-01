## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-1787.60.31.0.0
-  __TEXT.__text: 0x7ff0
+1787.80.12.0.0
+  __TEXT.__text: 0x8eb0
   __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_methlist: 0x890
-  __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x2d8
-  __TEXT.__cstring: 0xa11
+  __TEXT.__objc_methlist: 0x980
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x324
+  __TEXT.__cstring: 0xaf5
   __TEXT.__oslogstring: 0x59a
   __TEXT.__ustring: 0x5c6
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__objc_classname: 0x122
-  __TEXT.__objc_methname: 0x1b51
-  __TEXT.__objc_methtype: 0x43b
-  __TEXT.__objc_stubs: 0x1260
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__objc_classname: 0x124
+  __TEXT.__objc_methname: 0x1eb0
+  __TEXT.__objc_methtype: 0x45d
+  __TEXT.__objc_stubs: 0x1380
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x298
+  __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x11c0
-  __DATA_CONST.__objc_selrefs: 0x648
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__cfstring: 0x7c0
+  __DATA_CONST.__objc_const: 0x1380
+  __DATA_CONST.__objc_selrefs: 0x710
+  __DATA_CONST.__objc_arraydata: 0x110
+  __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_const: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x210
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x88
+  __DATA.__objc_classrefs: 0x98
   __DATA.__objc_superrefs: 0x38
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5FDC3F1-C707-32BC-96AF-8F6800BCF75F
-  Functions: 263
-  Symbols:   976
-  CStrings:  603
+  UUID: 42257A74-8533-3BB6-A3F9-D9409BD52C57
+  Functions: 294
+  Symbols:   1062
+  CStrings:  663
 
Symbols:
+ -[PPSClient monitoredPIDs]
+ -[PPSClient setMonitoredPIDs:]
+ -[PPSMetricCollection setWifiAWDLRange:]
+ -[PPSMetricCollection setWifiAWDLStatus:]
+ -[PPSMetricCollection wifiAWDLRange]
+ -[PPSMetricCollection wifiAWDLStatus]
+ -[PPSMetricMonitor currentProcessNames]
+ -[PPSMetricMonitor currentProcessPIDs]
+ -[PPSMetricMonitor setCurrentProcessNames:]
+ -[PPSMetricMonitor setCurrentProcessPIDs:]
+ -[PPSMetricMonitor startMonitoringProcessesWithName:error:]
+ -[PPSMetricMonitor startMonitoringProcessesWithName:error:].cold.1
+ -[PPSMetricMonitor startMonitoringProcessesWithName:error:].cold.2
+ -[PPSMetricMonitor startMonitoringProcessesWithPID:error:]
+ -[PPSMetricMonitor startMonitoringProcessesWithPID:error:].cold.1
+ -[PPSMetricMonitor startMonitoringProcessesWithPID:error:].cold.2
+ -[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]
+ -[PPSMetricMonitorService startMonitoringProcessesWithName:completion:].cold.1
+ -[PPSMetricMonitorService startMonitoringProcessesWithName:completion:].cold.2
+ -[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:]
+ -[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:].cold.1
+ -[PPSProcessMetricCollection bundleID]
+ -[PPSProcessMetricCollection bytesRead]
+ -[PPSProcessMetricCollection bytesWritten]
+ -[PPSProcessMetricCollection cpuInstructions]
+ -[PPSProcessMetricCollection pid]
+ -[PPSProcessMetricCollection processName]
+ -[PPSProcessMetricCollection setBundleID:]
+ -[PPSProcessMetricCollection setBytesRead:]
+ -[PPSProcessMetricCollection setBytesWritten:]
+ -[PPSProcessMetricCollection setCpuInstructions:]
+ -[PPSProcessMetricCollection setPid:]
+ -[PPSProcessMetricCollection setProcessName:]
+ GCC_except_table13
+ GCC_except_table25
+ GCC_except_table32
+ GCC_except_table37
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_IVAR_$_PPSClient._monitoredPIDs
+ _OBJC_IVAR_$_PPSMetricCollection._wifiAWDLRange
+ _OBJC_IVAR_$_PPSMetricCollection._wifiAWDLStatus
+ _OBJC_IVAR_$_PPSMetricMonitor._currentProcessNames
+ _OBJC_IVAR_$_PPSMetricMonitor._currentProcessPIDs
+ _OBJC_IVAR_$_PPSProcessMetricCollection._bundleID
+ _OBJC_IVAR_$_PPSProcessMetricCollection._bytesRead
+ _OBJC_IVAR_$_PPSProcessMetricCollection._bytesWritten
+ _OBJC_IVAR_$_PPSProcessMetricCollection._cpuInstructions
+ _OBJC_IVAR_$_PPSProcessMetricCollection._pid
+ _OBJC_IVAR_$_PPSProcessMetricCollection._processName
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_9
+ ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.55
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.44
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.44.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.45
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.45.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.50
+ ___58-[PPSMetricMonitor startMonitoringProcessesWithPID:error:]_block_invoke
+ ___58-[PPSMetricMonitor startMonitoringProcessesWithPID:error:]_block_invoke_2
+ ___59-[PPSMetricMonitor startMonitoringProcessesWithName:error:]_block_invoke
+ ___59-[PPSMetricMonitor startMonitoringProcessesWithName:error:]_block_invoke_2
+ ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.68
+ ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.69
+ ___block_descriptor_48_e8_32s40s_e36_v32?0"NSNumber"8"PPSClient"16^B24ls32l8s40l8
+ ___block_literal_global.65
+ _kPPSBundleIDKey
+ _kPPSPidKey
+ _kPPSProcessNameKey
+ _objc_msgSend$addObject:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$bundleID
+ _objc_msgSend$containsObject:
+ _objc_msgSend$currentProcessNames
+ _objc_msgSend$currentProcessPIDs
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$monitoredPIDs
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$pid
+ _objc_msgSend$processName
+ _objc_msgSend$setCurrentProcessNames:
+ _objc_msgSend$setCurrentProcessPIDs:
+ _objc_msgSend$setMonitoredPIDs:
+ _objc_msgSend$startMonitoringProcessesWithName:completion:
+ _objc_msgSend$startMonitoringProcessesWithName:error:
+ _objc_msgSend$startMonitoringProcessesWithPID:completion:
+ _objc_msgSend$startMonitoringProcessesWithPID:error:
- -[PPSClient monitoredPID]
- -[PPSClient setMonitoredPID:]
- -[PPSMetricMonitor currentProcessName]
- -[PPSMetricMonitor currentProcessPID]
- -[PPSMetricMonitor setCurrentProcessName:]
- -[PPSMetricMonitor setCurrentProcessPID:]
- -[PPSMetricMonitorService startMonitoringProcessWithName:completion:].cold.1
- -[PPSMetricMonitorService startMonitoringProcessWithName:completion:].cold.2
- -[PPSMetricMonitorService startMonitoringProcessWithPID:completion:].cold.1
- GCC_except_table15
- GCC_except_table24
- GCC_except_table26
- _OBJC_IVAR_$_PPSClient._monitoredPID
- _OBJC_IVAR_$_PPSMetricMonitor._currentProcessName
- _OBJC_IVAR_$_PPSMetricMonitor._currentProcessPID
- ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.51
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.40
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.40.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.41
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.41.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.42
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.65
- ___62-[PPSMetricMonitorService listener:shouldAcceptNewConnection:]_block_invoke.66
- ___block_descriptor_48_e8_32s40r_e36_v32?0"NSNumber"8"PPSClient"16^B24ls32l8r40l8
- ___block_literal_global.62
- _objc_msgSend$currentProcessName
- _objc_msgSend$currentProcessPID
- _objc_msgSend$monitoredPID
- _objc_msgSend$setCurrentProcessName:
- _objc_msgSend$setCurrentProcessPID:
- _objc_msgSend$setMonitoredPID:
- _objc_msgSend$startMonitoringProcessWithName:error:
- _objc_msgSend$startMonitoringProcessWithPID:completion:
- _objc_msgSend$startMonitoringProcessWithPID:error:
CStrings:
+ "\x1f\x01#"
+ "\x1f\x03"
+ "#\x14"
+ "-[PPSMetricMonitor startMonitoringProcessesWithName:error:]"
+ "-[PPSMetricMonitor startMonitoringProcessesWithPID:error:]"
+ "-[PPSMetricMonitorService startMonitoringProcessesWithName:completion:]"
+ "-[PPSMetricMonitorService startMonitoringProcessesWithPID:completion:]"
+ "@\"NSArray\""
+ "Failed to resume monitoring PID %@: %@"
+ "T@\"NSArray\",&,V_currentProcessNames"
+ "T@\"NSArray\",&,V_currentProcessPIDs"
+ "T@\"NSArray\",&,V_monitoredPIDs"
+ "T@\"NSMutableDictionary\",&,N,V_processMetrics"
+ "T@\"NSString\",&,N,V_bundleID"
+ "T@\"NSString\",&,N,V_processName"
+ "T@\"PPSMetricSample\",&,N,V_bytesRead"
+ "T@\"PPSMetricSample\",&,N,V_bytesWritten"
+ "T@\"PPSMetricSample\",&,N,V_cpuInstructions"
+ "T@\"PPSMetricSample\",&,N,V_wifiAWDLRange"
+ "T@\"PPSMetricSample\",&,N,V_wifiAWDLStatus"
+ "Ti,N,V_pid"
+ "__bundleID__"
+ "__pid__"
+ "__processName__"
+ "_bundleID"
+ "_bytesRead"
+ "_bytesWritten"
+ "_cpuInstructions"
+ "_currentProcessNames"
+ "_currentProcessPIDs"
+ "_monitoredPIDs"
+ "_pid"
+ "_processName"
+ "_wifiAWDLRange"
+ "_wifiAWDLStatus"
+ "addObject:"
+ "arrayWithObjects:count:"
+ "bundleID"
+ "bytesRead"
+ "bytesWritten"
+ "containsObject:"
+ "cpuInstructions"
+ "currentProcessNames"
+ "currentProcessPIDs"
+ "initWithArray:"
+ "monitoredPIDs"
+ "mutableCopy"
+ "pid"
+ "processName"
+ "setBundleID:"
+ "setBytesRead:"
+ "setBytesWritten:"
+ "setCpuInstructions:"
+ "setCurrentProcessNames:"
+ "setCurrentProcessPIDs:"
+ "setMonitoredPIDs:"
+ "setPid:"
+ "setProcessName:"
+ "setWifiAWDLRange:"
+ "setWifiAWDLStatus:"
+ "startMonitoringProcessesWithName:completion:"
+ "startMonitoringProcessesWithName:error:"
+ "startMonitoringProcessesWithPID:completion:"
+ "startMonitoringProcessesWithPID:error:"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "wifiAWDLRange"
+ "wifiAWDLStatus"
- "\r"
- "\x1e#"
- "#\x13"
- "-[PPSMetricMonitorService startMonitoringProcessWithName:completion:]"
- "-[PPSMetricMonitorService startMonitoringProcessWithPID:completion:]"
- "@\"NSDictionary\""
- "Failed to resume monitoring PID %d: %@"
- "T@\"NSDictionary\",&,N,V_processMetrics"
- "T@\"NSNumber\",&,V_monitoredPID"
- "T@\"NSString\",&,V_currentProcessName"
- "Ti,V_currentProcessPID"
- "_currentProcessName"
- "_currentProcessPID"
- "_monitoredPID"
- "currentProcessName"
- "currentProcessPID"
- "monitoredPID"
- "setCurrentProcessName:"
- "setCurrentProcessPID:"
- "setMonitoredPID:"

```
