## PerfPowerMetricMonitor

> `/System/Library/PrivateFrameworks/PerfPowerMetricMonitor.framework/PerfPowerMetricMonitor`

```diff

-2964.0.40.502.1
-  __TEXT.__text: 0x178fc
-  __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0x142c
+2964.0.64.0.0
+  __TEXT.__text: 0x184d0
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x1474
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x86c
-  __TEXT.__cstring: 0x189b
-  __TEXT.__oslogstring: 0x1594
+  __TEXT.__gcc_except_tab: 0x984
+  __TEXT.__cstring: 0x18f8
+  __TEXT.__oslogstring: 0x15fa
   __TEXT.__ustring: 0x6c0
-  __TEXT.__unwind_info: 0x4b0
+  __TEXT.__unwind_info: 0x4c8
   __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methname: 0x3ac0
+  __TEXT.__objc_methname: 0x3b9c
   __TEXT.__objc_methtype: 0x660
-  __TEXT.__objc_stubs: 0x3000
+  __TEXT.__objc_stubs: 0x30c0
   __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xde0
+  __DATA_CONST.__objc_selrefs: 0xe10
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x40
-  __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__auth_got: 0x2e8
-  __AUTH_CONST.__const: 0x160
-  __AUTH_CONST.__cfstring: 0x12c0
-  __AUTH_CONST.__objc_const: 0x2038
-  __AUTH_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_arraydata: 0x240
+  __AUTH_CONST.__auth_got: 0x2f0
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__cfstring: 0x1320
+  __AUTH_CONST.__objc_const: 0x20c8
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x1f0
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x300
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF7DA862-EE01-3701-B90D-ED1929583860
-  Functions: 567
-  Symbols:   1994
-  CStrings:  1255
+  UUID: F494120E-42F8-3FD3-9FEE-FBA4126EBD52
+  Functions: 585
+  Symbols:   2052
+  CStrings:  1275
 
Symbols:
+ -[PPSMetricMonitor endWithError:].cold.1
+ -[PPSMetricMonitor isAnalyticsSent]
+ -[PPSMetricMonitor monitoredStartTime]
+ -[PPSMetricMonitor setIsAnalyticsSent:]
+ -[PPSMetricMonitor setMonitoredStartTime:]
+ -[PPSMetricMonitor startMonitoringProcessWithName:error:].cold.3
+ -[PPSMetricMonitor startMonitoringProcessWithPID:error:].cold.3
+ -[PPSMetricMonitor startMonitoringProcessesWithName:error:].cold.3
+ -[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:].cold.3
+ -[PPSMetricMonitor startMonitoringProcessesWithPID:error:].cold.3
+ -[PPSMetricMonitorService monitoredStartTime]
+ -[PPSMetricMonitorService setMonitoredStartTime:]
+ GCC_except_table106
+ GCC_except_table15
+ GCC_except_table181
+ GCC_except_table23
+ GCC_except_table27
+ GCC_except_table30
+ GCC_except_table42
+ GCC_except_table46
+ GCC_except_table51
+ GCC_except_table60
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table73
+ GCC_except_table84
+ _AnalyticsSendEventLazy
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_PPSMetricMonitor._isAnalyticsSent
+ _OBJC_IVAR_$_PPSMetricMonitor._monitoredStartTime
+ _OBJC_IVAR_$_PPSMetricMonitorService._monitoredStartTime
+ ___33-[PPSMetricMonitor endWithError:]_block_invoke
+ ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.91
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.80
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.80.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.81
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.81.cold.1
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.82
+ ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.86
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.243
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.245
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.246
+ ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.247
+ ___55-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke.109
+ ___55-[PPSMetricMonitorService stopMonitoringHeadlessClient]_block_invoke.cold.2
+ ___56-[PPSMetricMonitor startMonitoringProcessWithPID:error:]_block_invoke_3
+ ___57-[PPSMetricMonitor startMonitoringProcessWithName:error:]_block_invoke_3
+ ___58-[PPSMetricMonitor startMonitoringProcessesWithPID:error:]_block_invoke_3
+ ___59-[PPSMetricMonitor startMonitoringProcessesWithName:error:]_block_invoke_3
+ ___65-[PPSMetricMonitor startMonitoringProcessesWithNames:PIDs:error:]_block_invoke_3
+ ___block_descriptor_32_e19_"NSDictionary"8?0l
+ ___block_descriptor_36_e19_"NSDictionary"8?0l
+ ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.242
+ ___block_literal_global.27
+ ___block_literal_global.283
+ ___block_literal_global.287
+ ___block_literal_global.79
+ _objc_msgSend$isAnalyticsSent
+ _objc_msgSend$monitoredStartTime
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$setIsAnalyticsSent:
+ _objc_msgSend$setMonitoredStartTime:
+ _objc_msgSend$timeIntervalSinceDate:
- GCC_except_table10
- GCC_except_table105
- GCC_except_table13
- GCC_except_table16
- GCC_except_table177
- GCC_except_table22
- GCC_except_table25
- GCC_except_table35
- GCC_except_table40
- GCC_except_table45
- GCC_except_table59
- GCC_except_table64
- GCC_except_table68
- GCC_except_table72
- GCC_except_table83
- ___42-[PPSMetricMonitor _handleXPCInterruption]_block_invoke.69
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.58
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.58.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.59
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.59.cold.1
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.60
- ___50-[PPSMetricMonitor _setUpXPCConnectionWithConfig:]_block_invoke.64
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.233
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.235
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.236
- ___54-[PPSMetricMonitorService _shouldAcceptNewConnection:]_block_invoke.237
- ___block_literal_global.232
- ___block_literal_global.274
- ___block_literal_global.278
CStrings:
+ "!I"
+ "@\"NSDictionary\"8@?0"
+ "T@\"NSDate\",&,V_monitoredStartTime"
+ "TB,V_isAnalyticsSent"
+ "Timer stopped. Monitored for %.2f seconds"
+ "_isAnalyticsSent"
+ "_monitoredStartTime"
+ "com.apple.perfpowermetricmonitor.usage"
+ "isAnalyticsSent"
+ "monitoredStartTime"
+ "monitoringDuration"
+ "numberWithUnsignedInteger:"
+ "processes monitored count: %lu"
+ "processes monitored count: 1"
+ "setIsAnalyticsSent:"
+ "setMonitoredStartTime:"
+ "targetAppCount"
+ "timeIntervalSinceDate:"
- "!H"

```
