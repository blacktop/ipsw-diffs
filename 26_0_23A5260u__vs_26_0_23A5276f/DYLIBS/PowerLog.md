## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-2954.0.0.502.3
-  __TEXT.__text: 0x25728
+2964.0.40.502.1
+  __TEXT.__text: 0x26978
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x1854
+  __TEXT.__objc_methlist: 0x1904
   __TEXT.__const: 0xcf8
-  __TEXT.__gcc_except_tab: 0xba0
-  __TEXT.__cstring: 0x22e7
-  __TEXT.__oslogstring: 0x3e91
-  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__gcc_except_tab: 0xc1c
+  __TEXT.__cstring: 0x2305
+  __TEXT.__oslogstring: 0x3fc8
+  __TEXT.__unwind_info: 0xa50
   __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x4b2f
-  __TEXT.__objc_methtype: 0xc27
-  __TEXT.__objc_stubs: 0x38c0
+  __TEXT.__objc_methname: 0x4d37
+  __TEXT.__objc_methtype: 0xc4c
+  __TEXT.__objc_stubs: 0x39a0
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__const: 0x878
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1228
+  __DATA_CONST.__objc_selrefs: 0x1298
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x540
   __AUTH_CONST.__cfstring: 0x27a0
-  __AUTH_CONST.__objc_const: 0x25c0
+  __AUTH_CONST.__objc_const: 0x25f8
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7B679AB5-A02F-3358-B2FA-83A8ED4D50A3
-  Functions: 944
-  Symbols:   3037
-  CStrings:  1970
+  UUID: CAE75840-1CC9-3464-BB56-7A2B9EACCA8D
+  Functions: 970
+  Symbols:   3104
+  CStrings:  1993
 
Symbols:
+ -[SafeguardsManagingClient clearMitigationRecordsWithError:]
+ -[SafeguardsManagingClient getMaxRelaunchPollingInterval:]
+ -[SafeguardsManagingClient getRelaunchPollingInterval:]
+ -[SafeguardsManagingClient getTargetProcessMitigationRecords:]
+ -[SafeguardsManagingClient setMaxRelaunchPollingInterval:error:]
+ -[SafeguardsManagingClient setRelaunchPollingInterval:error:]
+ -[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]
+ GCC_except_table100
+ GCC_except_table103
+ GCC_except_table106
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table60
+ GCC_except_table69
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table83
+ GCC_except_table85
+ GCC_except_table89
+ GCC_except_table92
+ GCC_except_table94
+ GCC_except_table97
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.78
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.78.cold.1
+ ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.68
+ ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke.74
+ ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke.75
+ ___40-[SafeguardsManagingClient getDefaults:]_block_invoke.65
+ ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke.67
+ ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke.66
+ ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke.62
+ ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke.60
+ ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.79
+ ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke.63
+ ___55-[SafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke
+ ___55-[SafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke.58
+ ___55-[SafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke.cold.1
+ ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.61
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.83
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.83.cold.1
+ ___58-[SafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke
+ ___58-[SafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke.59
+ ___58-[SafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke.cold.1
+ ___60-[SafeguardsManagingClient clearMitigationRecordsWithError:]_block_invoke
+ ___60-[SafeguardsManagingClient clearMitigationRecordsWithError:]_block_invoke.77
+ ___60-[SafeguardsManagingClient clearMitigationRecordsWithError:]_block_invoke.cold.1
+ ___61-[SafeguardsManagingClient setRelaunchPollingInterval:error:]_block_invoke
+ ___61-[SafeguardsManagingClient setRelaunchPollingInterval:error:]_block_invoke.cold.1
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.80
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.80.cold.1
+ ___62-[SafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke
+ ___62-[SafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke.71
+ ___62-[SafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke.cold.1
+ ___64-[SafeguardsManagingClient setMaxRelaunchPollingInterval:error:]_block_invoke
+ ___64-[SafeguardsManagingClient setMaxRelaunchPollingInterval:error:]_block_invoke.cold.1
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.81
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.81.cold.1
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.82
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.82.cold.1
+ ___70-[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]_block_invoke.73
+ ___72-[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]_block_invoke
+ ___72-[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]_block_invoke.76
+ ___72-[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
+ ___block_literal_global.183
+ _objc_msgSend$clearMitigationRecordsWithHandler:
+ _objc_msgSend$getMaxRelaunchPollingIntervalWithHandler:
+ _objc_msgSend$getRelaunchPollingIntervalWithHandler:
+ _objc_msgSend$getTargetProcessMitigationRecordsWithHandler:
+ _objc_msgSend$modifyMaxRelaunchPollingInterval:
+ _objc_msgSend$modifyRelaunchPollingInterval:
+ _objc_msgSend$modifyTargetProcessMitigationRecords:withHandler:
- GCC_except_table114
- GCC_except_table117
- GCC_except_table66
- GCC_except_table68
- GCC_except_table70
- GCC_except_table74
- GCC_except_table76
- GCC_except_table84
- GCC_except_table90
- GCC_except_table93
- GCC_except_table96
- GCC_except_table99
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.72
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.72.cold.1
- ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.66
- ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke.70
- ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke.71
- ___40-[SafeguardsManagingClient getDefaults:]_block_invoke.63
- ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke.65
- ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke.64
- ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke.60
- ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke.58
- ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.73
- ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke.61
- ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.59
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.77
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.77.cold.1
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.74
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.74.cold.1
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.75
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.75.cold.1
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.76
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.76.cold.1
- ___70-[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]_block_invoke.69
CStrings:
+ "Failed to clear mitigation records %@"
+ "Failed to copy max relaunch polling interval %@"
+ "Failed to copy relaunch polling interval %@"
+ "Failed to get mitigation information, %@"
+ "Failed to get mitigation records for target process %@"
+ "Failed to set mitigation records %@"
+ "Failed to set relaunch polling interval %@"
+ "Failed to set relaunch polling interval max %@"
+ "clearMitigationRecordsWithError:"
+ "clearMitigationRecordsWithHandler:"
+ "getMaxRelaunchPollingInterval:"
+ "getMaxRelaunchPollingIntervalWithHandler:"
+ "getRelaunchPollingInterval:"
+ "getRelaunchPollingIntervalWithHandler:"
+ "getTargetProcessMitigationRecords:"
+ "getTargetProcessMitigationRecordsWithHandler:"
+ "modifyMaxRelaunchPollingInterval:"
+ "modifyRelaunchPollingInterval:"
+ "modifyTargetProcessMitigationRecords:withHandler:"
+ "setMaxRelaunchPollingInterval:error:"
+ "setRelaunchPollingInterval:error:"
+ "setTargetProcessMitigationRecords:withError:"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
- "Failed to get mitigtaion information, %@"

```
