## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-2973.80.185.0.0
-  __TEXT.__text: 0x27728
-  __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x1954
+3031.100.213.502.1
+  __TEXT.__text: 0x2042c
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_methlist: 0x1474
   __TEXT.__const: 0xe98
-  __TEXT.__gcc_except_tab: 0xc48
-  __TEXT.__cstring: 0x23f5
-  __TEXT.__oslogstring: 0x40e4
-  __TEXT.__unwind_info: 0xa98
-  __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x4e9f
-  __TEXT.__objc_methtype: 0xd24
-  __TEXT.__objc_stubs: 0x3a80
+  __TEXT.__gcc_except_tab: 0x8e8
+  __TEXT.__cstring: 0x22b1
+  __TEXT.__oslogstring: 0x39c7
+  __TEXT.__unwind_info: 0x7f0
+  __TEXT.__objc_classname: 0x22e
+  __TEXT.__objc_methname: 0x3f69
+  __TEXT.__objc_methtype: 0x69b
+  __TEXT.__objc_stubs: 0x34c0
   __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x7e8
-  __DATA_CONST.__objc_classlist: 0xb0
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__objc_classlist: 0xa0
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12d8
-  __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0x1010
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x198
-  __AUTH_CONST.__auth_got: 0x4d0
-  __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x2940
-  __AUTH_CONST.__objc_const: 0x2608
-  __AUTH_CONST.__objc_intobj: 0x498
+  __AUTH_CONST.__auth_got: 0x490
+  __AUTH_CONST.__const: 0x540
+  __AUTH_CONST.__cfstring: 0x2900
+  __AUTH_CONST.__objc_const: 0x21d8
+  __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x320
-  __DATA.__objc_ivar: 0x1c0
-  __DATA.__data: 0x2b0
-  __DATA.__bss: 0x180
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x1a0
+  __DATA.__data: 0x1f0
+  __DATA.__bss: 0x160
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x78

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 196FDFB4-1F13-3EB9-8284-C52FF07B030B
-  Functions: 986
-  Symbols:   3153
-  CStrings:  2042
+  UUID: E50E43FA-8CB3-3230-8BFF-1B13E807C285
+  Functions: 809
+  Symbols:   2658
+  CStrings:  1842
 
Symbols:
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ ___22-[PLClientLogger init]_block_invoke.141
+ ___22-[PLClientLogger init]_block_invoke.145
+ ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.192
+ ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.192.cold.1
+ ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.192.cold.2
+ ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.228
+ ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.229
+ ___block_literal_global.133
+ ___block_literal_global.143
+ ___block_literal_global.147
+ ___block_literal_global.172
+ ___block_literal_global.181
+ _objc_retainAutoreleasedReturnValue
- -[SafeguardsClient .cxx_destruct]
- -[SafeguardsClient connection]
- -[SafeguardsClient featureEnabled]
- -[SafeguardsClient init]
- -[SafeguardsClient init].cold.1
- -[SafeguardsClient init].cold.2
- -[SafeguardsClient interrupted]
- -[SafeguardsClient logger]
- -[SafeguardsClient reportExcessiveCPUUseBy:pid:path:timestamp:observed_cpu_nsecs:observation_nsecs:cpu_nsecs_allowed:limit_window_nsecs:flags:]
- -[SafeguardsClient setConnection:]
- -[SafeguardsClient setFeatureEnabled:]
- -[SafeguardsClient setInterrupted:]
- -[SafeguardsClient setLogger:]
- -[SafeguardsManagingClient .cxx_destruct]
- -[SafeguardsManagingClient clearMitigationRecordsWithError:]
- -[SafeguardsManagingClient clearTargetProcessWithError:]
- -[SafeguardsManagingClient connection]
- -[SafeguardsManagingClient featureEnabled]
- -[SafeguardsManagingClient forceCPUViolationForProcess:error:]
- -[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]
- -[SafeguardsManagingClient forceDetectorViolationForProcess:error:]
- -[SafeguardsManagingClient forceMidnightRoutine:]
- -[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]
- -[SafeguardsManagingClient getActiveScenarios:]
- -[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]
- -[SafeguardsManagingClient getDefaults:]
- -[SafeguardsManagingClient getInfoForProcess:error:]
- -[SafeguardsManagingClient getMaxRelaunchPollingInterval:]
- -[SafeguardsManagingClient getMitigationPolicy:]
- -[SafeguardsManagingClient getMonitoredList:]
- -[SafeguardsManagingClient getPenaltyList:]
- -[SafeguardsManagingClient getPollingInterval:]
- -[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]
- -[SafeguardsManagingClient getRelaunchPollingInterval:]
- -[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]
- -[SafeguardsManagingClient getScenarioRefreshInterval:]
- -[SafeguardsManagingClient getScenarios:]
- -[SafeguardsManagingClient getTargetProcess:]
- -[SafeguardsManagingClient getTargetProcessMitigationRecords:]
- -[SafeguardsManagingClient getTriggerInterval:]
- -[SafeguardsManagingClient init]
- -[SafeguardsManagingClient init].cold.1
- -[SafeguardsManagingClient init].cold.2
- -[SafeguardsManagingClient interrupted]
- -[SafeguardsManagingClient logger]
- -[SafeguardsManagingClient reportScheduledIntensiveWorkByProcesses:]
- -[SafeguardsManagingClient resetRuleParameters:error:]
- -[SafeguardsManagingClient sendCoalitionEntries:error:]
- -[SafeguardsManagingClient setConnection:]
- -[SafeguardsManagingClient setContextForIdentifier:withState:error:]
- -[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]
- -[SafeguardsManagingClient setFeatureEnabled:]
- -[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]
- -[SafeguardsManagingClient setInterrupted:]
- -[SafeguardsManagingClient setLogger:]
- -[SafeguardsManagingClient setMaxRelaunchPollingInterval:error:]
- -[SafeguardsManagingClient setPollingInterval:error:]
- -[SafeguardsManagingClient setRelaunchPollingInterval:error:]
- -[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]
- -[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]
- -[SafeguardsManagingClient setScenarioRefreshInterval:error:]
- -[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]
- -[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:]
- -[SafeguardsManagingClient setTriggerInterval:error:]
- GCC_except_table100
- GCC_except_table103
- GCC_except_table106
- GCC_except_table109
- GCC_except_table112
- GCC_except_table115
- GCC_except_table118
- GCC_except_table121
- GCC_except_table124
- GCC_except_table139
- GCC_except_table142
- GCC_except_table19
- GCC_except_table24
- GCC_except_table27
- GCC_except_table30
- GCC_except_table33
- GCC_except_table36
- GCC_except_table39
- GCC_except_table45
- GCC_except_table51
- GCC_except_table54
- GCC_except_table60
- GCC_except_table63
- GCC_except_table69
- GCC_except_table72
- GCC_except_table75
- GCC_except_table77
- GCC_except_table79
- GCC_except_table81
- GCC_except_table83
- GCC_except_table85
- GCC_except_table87
- GCC_except_table89
- GCC_except_table92
- GCC_except_table94
- GCC_except_table97
- _OBJC_CLASS_$_SafeguardsClient
- _OBJC_CLASS_$_SafeguardsManagingClient
- _OBJC_IVAR_$_SafeguardsClient._connection
- _OBJC_IVAR_$_SafeguardsClient._featureEnabled
- _OBJC_IVAR_$_SafeguardsClient._interrupted
- _OBJC_IVAR_$_SafeguardsClient._logger
- _OBJC_IVAR_$_SafeguardsManagingClient._connection
- _OBJC_IVAR_$_SafeguardsManagingClient._featureEnabled
- _OBJC_IVAR_$_SafeguardsManagingClient._interrupted
- _OBJC_IVAR_$_SafeguardsManagingClient._logger
- _OBJC_METACLASS_$_SafeguardsClient
- _OBJC_METACLASS_$_SafeguardsManagingClient
- __OBJC_$_INSTANCE_METHODS_SafeguardsClient
- __OBJC_$_INSTANCE_METHODS_SafeguardsManagingClient
- __OBJC_$_INSTANCE_VARIABLES_SafeguardsClient
- __OBJC_$_INSTANCE_VARIABLES_SafeguardsManagingClient
- __OBJC_$_PROP_LIST_SafeguardsClient
- __OBJC_$_PROP_LIST_SafeguardsManagingClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SafeguardsScheduledWorkReporting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SafeguardsViolationReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES_SafeguardsScheduledWorkReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES_SafeguardsViolationReporting
- __OBJC_$_PROTOCOL_REFS_SafeguardsScheduledWorkReporting
- __OBJC_$_PROTOCOL_REFS_SafeguardsViolationReporting
- __OBJC_CLASS_RO_$_SafeguardsClient
- __OBJC_CLASS_RO_$_SafeguardsManagingClient
- __OBJC_LABEL_PROTOCOL_$_SafeguardsScheduledWorkReporting
- __OBJC_LABEL_PROTOCOL_$_SafeguardsViolationReporting
- __OBJC_METACLASS_RO_$_SafeguardsClient
- __OBJC_METACLASS_RO_$_SafeguardsManagingClient
- __OBJC_PROTOCOL_$_SafeguardsScheduledWorkReporting
- __OBJC_PROTOCOL_$_SafeguardsViolationReporting
- __OBJC_PROTOCOL_REFERENCE_$_SafeguardsScheduledWorkReporting
- __OBJC_PROTOCOL_REFERENCE_$_SafeguardsViolationReporting
- ___103-[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke
- ___103-[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.cold.1
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.80
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.80.cold.1
- ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.cold.1
- ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke
- ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke.78
- ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke.78.cold.1
- ___111-[SafeguardsManagingClient setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:]_block_invoke.cold.1
- ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke
- ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.68
- ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.cold.1
- ___131-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]_block_invoke
- ___131-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]_block_invoke.74
- ___131-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:]_block_invoke.cold.1
- ___143-[SafeguardsClient reportExcessiveCPUUseBy:pid:path:timestamp:observed_cpu_nsecs:observation_nsecs:cpu_nsecs_allowed:limit_window_nsecs:flags:]_block_invoke
- ___143-[SafeguardsClient reportExcessiveCPUUseBy:pid:path:timestamp:observed_cpu_nsecs:observation_nsecs:cpu_nsecs_allowed:limit_window_nsecs:flags:]_block_invoke.cold.1
- ___22-[PLClientLogger init]_block_invoke.139
- ___22-[PLClientLogger init]_block_invoke.143
- ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke
- ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke.75
- ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke.cold.1
- ___24-[SafeguardsClient init]_block_invoke
- ___24-[SafeguardsClient init]_block_invoke.9
- ___32-[SafeguardsManagingClient init]_block_invoke
- ___32-[SafeguardsManagingClient init]_block_invoke.47
- ___40-[SafeguardsManagingClient getDefaults:]_block_invoke
- ___40-[SafeguardsManagingClient getDefaults:]_block_invoke.65
- ___40-[SafeguardsManagingClient getDefaults:]_block_invoke.cold.1
- ___41-[SafeguardsManagingClient getScenarios:]_block_invoke
- ___41-[SafeguardsManagingClient getScenarios:]_block_invoke.50
- ___41-[SafeguardsManagingClient getScenarios:]_block_invoke.cold.1
- ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke
- ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke.67
- ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke.cold.1
- ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke
- ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke.66
- ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke.cold.1
- ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke
- ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke.62
- ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke.cold.1
- ___47-[SafeguardsManagingClient getActiveScenarios:]_block_invoke
- ___47-[SafeguardsManagingClient getActiveScenarios:]_block_invoke.48
- ___47-[SafeguardsManagingClient getActiveScenarios:]_block_invoke.cold.1
- ___47-[SafeguardsManagingClient getPollingInterval:]_block_invoke
- ___47-[SafeguardsManagingClient getPollingInterval:]_block_invoke.57
- ___47-[SafeguardsManagingClient getPollingInterval:]_block_invoke.cold.1
- ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke
- ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke.60
- ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke.cold.1
- ___48-[SafeguardsManagingClient getMitigationPolicy:]_block_invoke
- ___48-[SafeguardsManagingClient getMitigationPolicy:]_block_invoke.51
- ___48-[SafeguardsManagingClient getMitigationPolicy:]_block_invoke.cold.1
- ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke
- ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.81
- ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.cold.1
- ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke
- ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke.63
- ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke.cold.1
- ___53-[SafeguardsManagingClient setPollingInterval:error:]_block_invoke
- ___53-[SafeguardsManagingClient setPollingInterval:error:]_block_invoke.cold.1
- ___53-[SafeguardsManagingClient setTriggerInterval:error:]_block_invoke
- ___53-[SafeguardsManagingClient setTriggerInterval:error:]_block_invoke.cold.1
- ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke
- ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke.79
- ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke.79.cold.1
- ___54-[SafeguardsManagingClient resetRuleParameters:error:]_block_invoke.cold.1
- ___55-[SafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke
- ___55-[SafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke.58
- ___55-[SafeguardsManagingClient getRelaunchPollingInterval:]_block_invoke.cold.1
- ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke
- ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.61
- ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.cold.1
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.85
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.85.cold.1
- ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.cold.1
- ___56-[SafeguardsManagingClient clearTargetProcessWithError:]_block_invoke
- ___56-[SafeguardsManagingClient clearTargetProcessWithError:]_block_invoke.cold.1
- ___58-[SafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke
- ___58-[SafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke.59
- ___58-[SafeguardsManagingClient getMaxRelaunchPollingInterval:]_block_invoke.cold.1
- ___60-[SafeguardsManagingClient clearMitigationRecordsWithError:]_block_invoke
- ___60-[SafeguardsManagingClient clearMitigationRecordsWithError:]_block_invoke.77
- ___60-[SafeguardsManagingClient clearMitigationRecordsWithError:]_block_invoke.cold.1
- ___61-[SafeguardsManagingClient setRelaunchPollingInterval:error:]_block_invoke
- ___61-[SafeguardsManagingClient setRelaunchPollingInterval:error:]_block_invoke.cold.1
- ___61-[SafeguardsManagingClient setScenarioRefreshInterval:error:]_block_invoke
- ___61-[SafeguardsManagingClient setScenarioRefreshInterval:error:]_block_invoke.cold.1
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.82
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.82.cold.1
- ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.cold.1
- ___62-[SafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke
- ___62-[SafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke.71
- ___62-[SafeguardsManagingClient getTargetProcessMitigationRecords:]_block_invoke.cold.1
- ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.190
- ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.190.cold.1
- ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.190.cold.2
- ___64-[SafeguardsManagingClient setMaxRelaunchPollingInterval:error:]_block_invoke
- ___64-[SafeguardsManagingClient setMaxRelaunchPollingInterval:error:]_block_invoke.cold.1
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.83
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.83.cold.1
- ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.cold.1
- ___68-[SafeguardsManagingClient reportScheduledIntensiveWorkByProcesses:]_block_invoke
- ___68-[SafeguardsManagingClient reportScheduledIntensiveWorkByProcesses:]_block_invoke.cold.1
- ___68-[SafeguardsManagingClient setContextForIdentifier:withState:error:]_block_invoke
- ___68-[SafeguardsManagingClient setContextForIdentifier:withState:error:]_block_invoke.cold.1
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.84
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.84.cold.1
- ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.cold.1
- ___70-[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]_block_invoke
- ___70-[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]_block_invoke.73
- ___70-[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]_block_invoke.cold.1
- ___71-[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke
- ___71-[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke.53
- ___71-[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke.cold.1
- ___72-[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]_block_invoke
- ___72-[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]_block_invoke.76
- ___72-[SafeguardsManagingClient setTargetProcessMitigationRecords:withError:]_block_invoke.cold.1
- ___76-[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke
- ___76-[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke.55
- ___76-[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke.cold.1
- ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.226
- ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.227
- ___block_descriptor_40_e8_32r_e15_v16?0"NSSet"8lr32l8
- ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_40_e8_32r_e18_v16?0"NSNumber"8lr32l8
- ___block_descriptor_40_e8_32r_e22_v16?0"NSDictionary"8lr32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
- ___block_descriptor_48_e8_32r40r_e29_v24?0"NSArray"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e34_v24?0"NSDictionary"8"NSError"16lr32l8r40l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_56_e23_v28?0B8d12"NSError"20l
- ___block_literal_global.131
- ___block_literal_global.141
- ___block_literal_global.145
- ___block_literal_global.170
- ___block_literal_global.179
- ___block_literal_global.188
- ___clientInterface_block_invoke
- ___managingClientInterface_block_invoke
- _clientInterface.interface
- _clientInterface.onceToken
- _managingClientInterface.interface
- _managingClientInterface.onceToken
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_xpcConnection
- _objc_msgSend$clearMitigationRecordsWithHandler:
- _objc_msgSend$clearTargetProcess
- _objc_msgSend$forceCPUViolationForProcess:withHandler:
- _objc_msgSend$forceDetectionWithStartTime:endTime:withHandler:
- _objc_msgSend$forceDetectorViolationForProcess:withHandler:
- _objc_msgSend$forceMidnightRoutineWithHandler:
- _objc_msgSend$forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:
- _objc_msgSend$getActiveScenariosWithHandler:
- _objc_msgSend$getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:
- _objc_msgSend$getDefaultsWithHandler:
- _objc_msgSend$getInfoForProcess:withHandler:
- _objc_msgSend$getMaxRelaunchPollingIntervalWithHandler:
- _objc_msgSend$getMitigationPolicyWithHandler:
- _objc_msgSend$getMonitoredListWithHandler:
- _objc_msgSend$getPenaltyListWithHandler:
- _objc_msgSend$getPollingIntervalWithHandler:
- _objc_msgSend$getProcessesAffectedByScenarioMapWithHandler:
- _objc_msgSend$getRelaunchPollingIntervalWithHandler:
- _objc_msgSend$getRestrictionsForProcess:forScenario:withHandler:
- _objc_msgSend$getScenarioRefreshIntervalWithHandler:
- _objc_msgSend$getScenariosWithHandler:
- _objc_msgSend$getTargetProcessMitigationRecordsWithHandler:
- _objc_msgSend$getTargetProcessWithHandler:
- _objc_msgSend$getTriggerIntervalWithHandler:
- _objc_msgSend$initWithMachServiceName:options:
- _objc_msgSend$logger
- _objc_msgSend$modifyContextForIdentifier:withState:
- _objc_msgSend$modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:
- _objc_msgSend$modifyMaxRelaunchPollingInterval:
- _objc_msgSend$modifyPollingInterval:
- _objc_msgSend$modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:
- _objc_msgSend$modifyRelaunchPollingInterval:
- _objc_msgSend$modifyRestrictionsByProcessPerScenario:withHandler:
- _objc_msgSend$modifyScenarioRefreshInterval:
- _objc_msgSend$modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:
- _objc_msgSend$modifyTargetProcessMitigationRecords:withHandler:
- _objc_msgSend$modifyTriggerInterval:
- _objc_msgSend$remoteObjectProxyWithErrorHandler:
- _objc_msgSend$reportExcessiveCPUUseBy:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:
- _objc_msgSend$reportScheduledIntensiveWorkByProcesses:
- _objc_msgSend$resetRuleParameters:withHandler:
- _objc_msgSend$setInterrupted:
- _objc_msgSend$setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:
- _objc_msgSend$stringWithCString:
- _objc_msgSend$updateCoalitionEntries:withHandler:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _xpc_connection_set_target_user_session_uid
- _xpc_strerror
- _xpc_user_sessions_enabled
- _xpc_user_sessions_get_foreground_uid
CStrings:
- "(FATAL) "
- "@24@0:8^@16"
- "@32@0:8@16^@24"
- "@40@0:8@16@24^@32"
- "B32@0:8@16^@24"
- "B40@0:8@16@24^@32"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8@16@24^B32^d40^@48"
- "B64@0:8@16@24@32@40@48^@56"
- "B72@0:8@16@24@32@40@48@56^@64"
- "B96@0:8@16@24@32@40@48@56@64@72@80^@88"
- "Connection to service interrupted"
- "Connection to service invalidated"
- "Failed to clear mitigation records %@"
- "Failed to clear target process %@"
- "Failed to copy active scenarios %@"
- "Failed to copy max relaunch polling interval %@"
- "Failed to copy polling interval %@"
- "Failed to copy relaunch polling interval %@"
- "Failed to copy restrictions %@"
- "Failed to copy scenario map %@"
- "Failed to copy scenario refresh interval %@"
- "Failed to copy scenarios %@"
- "Failed to copy trigger interval %@"
- "Failed to force CPU violation %@"
- "Failed to force detection with startTime and endTime %@"
- "Failed to force detector violation %@"
- "Failed to force midnight routine %@"
- "Failed to force mitigation %@"
- "Failed to get cpu percentage trigger %@"
- "Failed to get defaults %@"
- "Failed to get mitigation information, %@"
- "Failed to get mitigation records for target process %@"
- "Failed to get monitored list %@"
- "Failed to get penalty list %@"
- "Failed to get process info %@"
- "Failed to get target process %@"
- "Failed to report scheduled intensive work %@"
- "Failed to report violation %@"
- "Failed to reset rule parameters %@"
- "Failed to send coalition entries %@"
- "Failed to set context %@"
- "Failed to set defaults %@"
- "Failed to set mitigation records %@"
- "Failed to set polling interval %@"
- "Failed to set process info %@"
- "Failed to set relaunch polling interval %@"
- "Failed to set relaunch polling interval max %@"
- "Failed to set restrictions %@"
- "Failed to set rule parameters %@"
- "Failed to set scenario refresh interval %@"
- "Failed to set trigger interval %@"
- "Initialized connection"
- "Not setting up connection as feature is not enabled."
- "Received %sCPU usage trigger: \n  %s[%d] (%s) used %.2fs of CPU over %.2f seconds (averaging %d%%), violating a CPU usage limit of %.2fs over %lld seconds."
- "Reporting %@ as now running intensive workloads"
- "SafeguardsClient"
- "SafeguardsManagingClient"
- "SafeguardsScheduledWorkReporting"
- "SafeguardsViolationReporting"
- "T@\"NSObject<OS_os_log>\",&,V_logger"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "TB,V_featureEnabled"
- "TB,V_interrupted"
- "_featureEnabled"
- "_interrupted"
- "_logger"
- "clearMitigationRecordsWithError:"
- "clearMitigationRecordsWithHandler:"
- "clearTargetProcess"
- "clearTargetProcessWithError:"
- "com.apple.computesafeguards"
- "com.apple.computesafeguards.managing"
- "com.apple.computesafeguards.violationhandler"
- "featureEnabled"
- "forceCPUViolationForProcess:error:"
- "forceCPUViolationForProcess:withHandler:"
- "forceDetectionWithStartTime:endTime:error:"
- "forceDetectionWithStartTime:endTime:withHandler:"
- "forceDetectorViolationForProcess:error:"
- "forceDetectorViolationForProcess:withHandler:"
- "forceMidnightRoutine:"
- "forceMidnightRoutineWithHandler:"
- "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:"
- "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:"
- "getActiveScenarios:"
- "getActiveScenariosWithHandler:"
- "getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:"
- "getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:"
- "getDefaults:"
- "getDefaultsWithHandler:"
- "getInfoForProcess:error:"
- "getInfoForProcess:withHandler:"
- "getMaxRelaunchPollingInterval:"
- "getMaxRelaunchPollingIntervalWithHandler:"
- "getMitigationPolicy:"
- "getMitigationPolicyWithHandler:"
- "getMonitoredList:"
- "getMonitoredListWithHandler:"
- "getPenaltyList:"
- "getPenaltyListWithHandler:"
- "getPollingInterval:"
- "getPollingIntervalWithHandler:"
- "getProcessesAffectedByScenarioMapWithError:"
- "getProcessesAffectedByScenarioMapWithHandler:"
- "getRelaunchPollingInterval:"
- "getRelaunchPollingIntervalWithHandler:"
- "getRestrictionsForProcess:forScenario:withError:"
- "getRestrictionsForProcess:forScenario:withHandler:"
- "getScenarioRefreshInterval:"
- "getScenarioRefreshIntervalWithHandler:"
- "getScenarios:"
- "getScenariosWithHandler:"
- "getTargetProcess:"
- "getTargetProcessMitigationRecords:"
- "getTargetProcessMitigationRecordsWithHandler:"
- "getTargetProcessWithHandler:"
- "getTriggerInterval:"
- "getTriggerIntervalWithHandler:"
- "initWithMachServiceName:options:"
- "interrupted"
- "logger"
- "modifyContextForIdentifier:withState:"
- "modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:"
- "modifyMaxRelaunchPollingInterval:"
- "modifyPollingInterval:"
- "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:withHandler:"
- "modifyRelaunchPollingInterval:"
- "modifyRestrictionsByProcessPerScenario:withHandler:"
- "modifyScenarioRefreshInterval:"
- "modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:"
- "modifyTargetProcessMitigationRecords:withHandler:"
- "modifyTriggerInterval:"
- "remoteObjectProxyWithErrorHandler:"
- "reportExcessiveCPUUseBy:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:"
- "reportExcessiveCPUUseBy:pid:path:timestamp:observed_cpu_nsecs:observation_nsecs:cpu_nsecs_allowed:limit_window_nsecs:flags:"
- "reportScheduledIntensiveWorkByProcesses:"
- "resetRuleParameters:error:"
- "resetRuleParameters:withHandler:"
- "safeguards_detection"
- "safeguardsclient"
- "safeguardsmanagingclient"
- "sendCoalitionEntries:error:"
- "setContextForIdentifier:withState:error:"
- "setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:"
- "setFeatureEnabled:"
- "setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withPolicyMask:error:"
- "setInterrupted:"
- "setLogger:"
- "setMaxRelaunchPollingInterval:error:"
- "setPollingInterval:error:"
- "setRelaunchPollingInterval:error:"
- "setRestrictionsByProcessPerScenario:error:"
- "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:error:"
- "setRuleParameters:withWindowSize:withStepSize:withMaxLookback:withDaemonOnly:withHandler:"
- "setScenarioRefreshInterval:error:"
- "setTargetProcessMitigationRecords:withError:"
- "setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:"
- "setTriggerInterval:error:"
- "stringWithCString:"
- "updateCoalitionEntries:withHandler:"
- "v16@?0@\"NSArray\"8"
- "v16@?0@\"NSNumber\"8"
- "v16@?0@\"NSSet\"8"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@\"NSSet\"16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSNumber\">16"
- "v24@0:8@?<v@?@\"NSSet\">16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v28@?0B8d12@\"NSError\"20"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSNumber\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@\"NSNumber\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?Bd@\"NSError\">32"
- "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
- "v48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40"
- "v48@0:8@16@24@32@40"
- "v64@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v72@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@?<v@?@\"NSError\">64"
- "v72@0:8@16@24@32@40@48@56@?64"
- "v84@0:8@\"NSString\"16Q24@\"NSString\"32{mach_timespec=Ii}40q48q56q64q72B80"
- "v84@0:8@16Q24@32{mach_timespec=Ii}40q48q56q64q72B80"
- "v84@0:8[33c]16i24[1024c]28{mach_timespec=Ii}36q44q52q60q68Q76"
- "v96@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80@?<v@?@\"NSError\">88"
- "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
- "xpc_user_sessions_get_foreground_uid() failed with error %d - %s"

```
