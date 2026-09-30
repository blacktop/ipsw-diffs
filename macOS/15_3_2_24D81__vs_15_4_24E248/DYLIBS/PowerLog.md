## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0x1de04
+2423.100.232.0.0
+  __TEXT.__text: 0x1e2ec
   __TEXT.__auth_stubs: 0x6c0
-  __TEXT.__objc_methlist: 0x12b4
+  __TEXT.__objc_methlist: 0x1404
   __TEXT.__const: 0x1d0
   __TEXT.__gcc_except_tab: 0x8d0
-  __TEXT.__cstring: 0x1e17
-  __TEXT.__oslogstring: 0x368b
-  __TEXT.__unwind_info: 0x6c0
-  __TEXT.__objc_classname: 0x1f2
-  __TEXT.__objc_methname: 0x3ac1
-  __TEXT.__objc_methtype: 0x563
+  __TEXT.__cstring: 0x1e84
+  __TEXT.__oslogstring: 0x36b5
+  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__objc_classname: 0x20b
+  __TEXT.__objc_methname: 0x3d0a
+  __TEXT.__objc_methtype: 0x5c9
   __TEXT.__objc_stubs: 0x2e40
   __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__const: 0x268
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf0
+  __DATA_CONST.__objc_selrefs: 0xe70
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x160
   __AUTH_CONST.__auth_got: 0x370
   __AUTH_CONST.__const: 0x850
-  __AUTH_CONST.__cfstring: 0x21c0
-  __AUTH_CONST.__objc_const: 0x20c0
+  __AUTH_CONST.__cfstring: 0x2200
+  __AUTH_CONST.__objc_const: 0x2230
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x1ac
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0x60
-  __DATA.__bss: 0xd0
+  __DATA.__bss: 0xc8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: E31AB967-56EB-3D34-AA37-D38A41DB481A
-  Functions: 764
-  Symbols:   1685
-  CStrings:  1615
+  UUID: 05D5A827-8954-328B-9A12-9B6D8FD7CB8F
+  Functions: 795
+  Symbols:   1725
+  CStrings:  1646
 
Symbols:
+ +[PLClientLogAggregator sharedInstance].cold.1
+ +[PLClientLogger sharedInstance].cold.1
+ +[PLModelingUtilities internalBuild].cold.1
+ +[PLModelingUtilities isHeySiriAlwaysOn].cold.1
+ -[SafeguardsClient logger]
+ -[SafeguardsClient setLogger:]
+ -[SafeguardsManagingClient .cxx_destruct]
+ -[SafeguardsManagingClient connection]
+ -[SafeguardsManagingClient featureEnabled]
+ -[SafeguardsManagingClient forceMitigation:forProcess:error:]
+ -[SafeguardsManagingClient getActiveScenarios:]
+ -[SafeguardsManagingClient getCountsForProcess:error:]
+ -[SafeguardsManagingClient getPollingInterval:]
+ -[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]
+ -[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]
+ -[SafeguardsManagingClient getScenarioRefreshInterval:]
+ -[SafeguardsManagingClient getScenarios:]
+ -[SafeguardsManagingClient getTargetProcess:]
+ -[SafeguardsManagingClient init]
+ -[SafeguardsManagingClient interrupted]
+ -[SafeguardsManagingClient logger]
+ -[SafeguardsManagingClient reportScheduledIntensiveWorkByProcesses:]
+ -[SafeguardsManagingClient setConnection:]
+ -[SafeguardsManagingClient setFeatureEnabled:]
+ -[SafeguardsManagingClient setInterrupted:]
+ -[SafeguardsManagingClient setLogger:]
+ -[SafeguardsManagingClient setPollingInterval:error:]
+ -[SafeguardsManagingClient setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:]
+ -[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]
+ -[SafeguardsManagingClient setScenarioRefreshInterval:error:]
+ -[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withLimit:error:]
+ GCC_except_table163
+ GCC_except_table311
+ GCC_except_table313
+ GCC_except_table319
+ OBJC_IVAR_$_SafeguardsClient._logger
+ OBJC_IVAR_$_SafeguardsManagingClient._connection
+ OBJC_IVAR_$_SafeguardsManagingClient._featureEnabled
+ OBJC_IVAR_$_SafeguardsManagingClient._interrupted
+ OBJC_IVAR_$_SafeguardsManagingClient._logger
+ PLADPushTimeIntervalForDistributionKeySinceStartTime.cold.1
+ PLLogClientLogging.cold.1
+ PLLogDiscretionaryEnergyMonitor.cold.1
+ _OBJC_CLASS_$_SafeguardsManagingClient
+ _OBJC_METACLASS_$_SafeguardsManagingClient
+ _PLSysdiagnoseCopyBackgroundProcessingLog
+ __22-[PLClientLogger init]_block_invoke.116
+ __22-[PLClientLogger init]_block_invoke.120
+ __64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.167
+ __64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.167.cold.1
+ __64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.167.cold.2
+ __78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.207
+ __78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.208
+ __OBJC_$_INSTANCE_METHODS_SafeguardsManagingClient
+ __OBJC_$_INSTANCE_VARIABLES_SafeguardsManagingClient
+ __OBJC_$_PROP_LIST_SafeguardsManagingClient
+ __OBJC_CLASS_RO_$_SafeguardsManagingClient
+ __OBJC_METACLASS_RO_$_SafeguardsManagingClient
+ __block_literal_global.108
+ __block_literal_global.118
+ __block_literal_global.122
+ __block_literal_global.147
+ __block_literal_global.156
+ _kPPSUrsaErrorDomain
+ discretionaryEnergyMonitorQueue.cold.1
+ logHandle.cold.1
+ logHandleBatteryUIExternalData.cold.1
- +[SafeguardsClient initialize]
- GCC_except_table161
- GCC_except_table308
- GCC_except_table314
- GCC_except_table316
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_13
- _OUTLINED_FUNCTION_14
- __22-[PLClientLogger init]_block_invoke.122
- __22-[PLClientLogger init]_block_invoke.126
- __64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.173
- __64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.173.cold.1
- __64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.173.cold.2
- __78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.213
- __78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.214
- __OBJC_$_CLASS_METHODS_SafeguardsClient
- __block_literal_global.114
- __block_literal_global.124
- __block_literal_global.128
- __block_literal_global.153
- __block_literal_global.162
- _logger
CStrings:
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@40@0:8@16@24^@32"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "B56@0:8@16@24@32@40^@48"
+ "BGSQL"
+ "BGSQL DROP Success: %d Execution Time: %f"
+ "BackgroundProcessing_DASActivityLifecycle_24_5"
+ "BackgroundProcessing_DASPoliciesBlockingCriteria_24_5"
+ "SafeguardsManagingClient"
+ "T@\"NSObject<OS_os_log>\",&,V_logger"
+ "_logger"
+ "com.apple.PerfPowerServices.Ursa"
+ "forceMitigation:forProcess:error:"
+ "getActiveScenarios:"
+ "getCountsForProcess:error:"
+ "getPollingInterval:"
+ "getProcessesAffectedByScenarioMapWithError:"
+ "getRestrictionsForProcess:forScenario:withError:"
+ "getScenarioRefreshInterval:"
+ "getScenarios:"
+ "getTargetProcess:"
+ "logger"
+ "reportScheduledIntensiveWorkByProcesses:"
+ "safeguardsmanagingclient"
+ "setLogger:"
+ "setPollingInterval:error:"
+ "setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:"
+ "setRestrictionsByProcessPerScenario:error:"
+ "setScenarioRefreshInterval:error:"
+ "setTargetProcessTo:withPercentage:withSeconds:withLimit:error:"
- "Button::CaptureButtonAction"
- "Button::CaptureButtonConfig"
- "initialize"

```
