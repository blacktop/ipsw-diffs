## PowerLog

> `/System/Library/PrivateFrameworks/PowerLog.framework/PowerLog`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0x231b4
+2954.0.0.502.3
+  __TEXT.__text: 0x25728
   __TEXT.__auth_stubs: 0x980
-  __TEXT.__objc_methlist: 0x16ec
-  __TEXT.__const: 0xcf0
-  __TEXT.__gcc_except_tab: 0xa9c
-  __TEXT.__cstring: 0x21d3
-  __TEXT.__oslogstring: 0x3b87
-  __TEXT.__unwind_info: 0x8b0
+  __TEXT.__objc_methlist: 0x1854
+  __TEXT.__const: 0xcf8
+  __TEXT.__gcc_except_tab: 0xba0
+  __TEXT.__cstring: 0x22e7
+  __TEXT.__oslogstring: 0x3e91
+  __TEXT.__unwind_info: 0x9d0
   __TEXT.__objc_classname: 0x298
-  __TEXT.__objc_methname: 0x4554
-  __TEXT.__objc_methtype: 0x9ac
-  __TEXT.__objc_stubs: 0x36e0
+  __TEXT.__objc_methname: 0x4b2f
+  __TEXT.__objc_methtype: 0xc27
+  __TEXT.__objc_stubs: 0x38c0
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x828
+  __DATA_CONST.__const: 0x850
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1130
+  __DATA_CONST.__objc_selrefs: 0x1228
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x180
+  __DATA_CONST.__objc_arraydata: 0x170
   __AUTH_CONST.__auth_got: 0x4d0
   __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x2580
-  __AUTH_CONST.__objc_const: 0x2548
-  __AUTH_CONST.__objc_intobj: 0x450
+  __AUTH_CONST.__cfstring: 0x27a0
+  __AUTH_CONST.__objc_const: 0x25c0
+  __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH.__objc_data: 0x320
   __DATA.__objc_ivar: 0x1c0
   __DATA.__data: 0x2b0
   __DATA.__bss: 0x160
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x5a0
+  __DATA_DIRTY.__objc_data: 0x3c0
   __DATA_DIRTY.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2BEB83C7-75C1-3F03-BA6A-C0281253CC43
-  Functions: 881
-  Symbols:   2874
-  CStrings:  1875
+  UUID: 7B679AB5-A02F-3358-B2FA-83A8ED4D50A3
+  Functions: 944
+  Symbols:   3037
+  CStrings:  1970
 
Symbols:
+ +[PLModelingUtilities criticalBatteryLevel]
+ -[SafeguardsManagingClient clearTargetProcessWithError:]
+ -[SafeguardsManagingClient forceCPUViolationForProcess:error:]
+ -[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]
+ -[SafeguardsManagingClient forceDetectorViolationForProcess:error:]
+ -[SafeguardsManagingClient forceMidnightRoutine:]
+ -[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]
+ -[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]
+ -[SafeguardsManagingClient getDefaults:]
+ -[SafeguardsManagingClient getInfoForProcess:error:]
+ -[SafeguardsManagingClient getMitigationPolicy:]
+ -[SafeguardsManagingClient getMonitoredList:]
+ -[SafeguardsManagingClient getPenaltyList:]
+ -[SafeguardsManagingClient getTriggerInterval:]
+ -[SafeguardsManagingClient sendCoalitionEntries:error:]
+ -[SafeguardsManagingClient setContextForIdentifier:withState:error:]
+ -[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]
+ -[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]
+ -[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:]
+ -[SafeguardsManagingClient setTriggerInterval:error:]
+ GCC_except_table114
+ GCC_except_table117
+ GCC_except_table54
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table99
+ _PLBatteryUsageUIDynamicEndConfiguration
+ _PLConfigureBUIQueryInsightsAndSuggestionsSummary
+ _PLCopyBackgroundProcessingLog.cold.1
+ _PLCopyBackgroundProcessingLog.cold.2
+ _PLCopyBackgroundProcessingLog.cold.3
+ ___103-[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke
+ ___103-[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.cold.1
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.72
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.72.cold.1
+ ___111-[SafeguardsManagingClient forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:]_block_invoke.cold.1
+ ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke
+ ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.66
+ ___113-[SafeguardsManagingClient getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:]_block_invoke.cold.1
+ ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke
+ ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke.70
+ ___116-[SafeguardsManagingClient setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:]_block_invoke.cold.1
+ ___22-[PLClientLogger init]_block_invoke.139
+ ___22-[PLClientLogger init]_block_invoke.143
+ ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke
+ ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke.71
+ ___221-[SafeguardsManagingClient setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:]_block_invoke.cold.1
+ ___40-[SafeguardsManagingClient getDefaults:]_block_invoke
+ ___40-[SafeguardsManagingClient getDefaults:]_block_invoke.63
+ ___40-[SafeguardsManagingClient getDefaults:]_block_invoke.cold.1
+ ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke
+ ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke.65
+ ___43-[SafeguardsManagingClient getPenaltyList:]_block_invoke.cold.1
+ ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke
+ ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke.64
+ ___45-[SafeguardsManagingClient getMonitoredList:]_block_invoke.cold.1
+ ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke.60
+ ___47-[SafeguardsManagingClient getPollingInterval:]_block_invoke.57
+ ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke
+ ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke.58
+ ___47-[SafeguardsManagingClient getTriggerInterval:]_block_invoke.cold.1
+ ___48-[SafeguardsManagingClient getMitigationPolicy:]_block_invoke
+ ___48-[SafeguardsManagingClient getMitigationPolicy:]_block_invoke.51
+ ___48-[SafeguardsManagingClient getMitigationPolicy:]_block_invoke.cold.1
+ ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke
+ ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.73
+ ___49-[SafeguardsManagingClient forceMidnightRoutine:]_block_invoke.cold.1
+ ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke
+ ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke.61
+ ___52-[SafeguardsManagingClient getInfoForProcess:error:]_block_invoke.cold.1
+ ___53-[SafeguardsManagingClient setTriggerInterval:error:]_block_invoke
+ ___53-[SafeguardsManagingClient setTriggerInterval:error:]_block_invoke.cold.1
+ ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.59
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.77
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.77.cold.1
+ ___55-[SafeguardsManagingClient sendCoalitionEntries:error:]_block_invoke.cold.1
+ ___56-[SafeguardsManagingClient clearTargetProcessWithError:]_block_invoke
+ ___56-[SafeguardsManagingClient clearTargetProcessWithError:]_block_invoke.cold.1
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.74
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.74.cold.1
+ ___62-[SafeguardsManagingClient forceCPUViolationForProcess:error:]_block_invoke.cold.1
+ ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.190
+ ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.190.cold.1
+ ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.190.cold.2
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.75
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.75.cold.1
+ ___67-[SafeguardsManagingClient forceDetectorViolationForProcess:error:]_block_invoke.cold.1
+ ___68-[SafeguardsManagingClient setContextForIdentifier:withState:error:]_block_invoke
+ ___68-[SafeguardsManagingClient setContextForIdentifier:withState:error:]_block_invoke.cold.1
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.76
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.76.cold.1
+ ___70-[SafeguardsManagingClient forceDetectionWithStartTime:endTime:error:]_block_invoke.cold.1
+ ___70-[SafeguardsManagingClient setRestrictionsByProcessPerScenario:error:]_block_invoke.69
+ ___71-[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke.53
+ ___76-[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke.55
+ ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.226
+ ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.227
+ ___PLConfigureBUIQueryInsightsAndSuggestionsSummary_block_invoke
+ ___block_descriptor_48_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_56_e23_v28?0B8d12"NSError"20l
+ ___block_literal_global.131
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.170
+ ___block_literal_global.179
+ ___handleXPCEvent_block_invoke.161
+ _batteryUIInsightSummary
+ _batteryUIInsightSummary.cold.1
+ _batteryUISuggestionSummary
+ _batteryUISuggestionSummary.cold.1
+ _objc_msgSend$clearTargetProcess
+ _objc_msgSend$forceCPUViolationForProcess:withHandler:
+ _objc_msgSend$forceDetectionWithStartTime:endTime:withHandler:
+ _objc_msgSend$forceDetectorViolationForProcess:withHandler:
+ _objc_msgSend$forceMidnightRoutineWithHandler:
+ _objc_msgSend$forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:
+ _objc_msgSend$getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:
+ _objc_msgSend$getDefaultsWithHandler:
+ _objc_msgSend$getInfoForProcess:withHandler:
+ _objc_msgSend$getMitigationPolicyWithHandler:
+ _objc_msgSend$getMonitoredListWithHandler:
+ _objc_msgSend$getPenaltyListWithHandler:
+ _objc_msgSend$getTriggerIntervalWithHandler:
+ _objc_msgSend$modifyContextForIdentifier:withState:
+ _objc_msgSend$modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:
+ _objc_msgSend$modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:
+ _objc_msgSend$modifyRestrictionsByProcessPerScenario:withHandler:
+ _objc_msgSend$modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:
+ _objc_msgSend$modifyTriggerInterval:
+ _objc_msgSend$updateCoalitionEntries:withHandler:
- -[SafeguardsManagingClient forceMitigation:forProcess:error:]
- -[SafeguardsManagingClient getCountsForProcess:error:]
- -[SafeguardsManagingClient setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:]
- -[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withLimit:error:]
- GCC_except_table49
- GCC_except_table53
- GCC_except_table56
- GCC_except_table71
- _PLBatteryGaugePauseTracing
- _PLBatteryGaugeResumeTracing
- _PLBatteryGaugeStartTracing
- _PLBatteryGaugeStopTracing
- ___101-[SafeguardsManagingClient setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:]_block_invoke
- ___101-[SafeguardsManagingClient setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:]_block_invoke.61
- ___101-[SafeguardsManagingClient setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:]_block_invoke.cold.1
- ___22-[PLClientLogger init]_block_invoke.127
- ___22-[PLClientLogger init]_block_invoke.131
- ___45-[SafeguardsManagingClient getTargetProcess:]_block_invoke.58
- ___47-[SafeguardsManagingClient getPollingInterval:]_block_invoke.55
- ___54-[SafeguardsManagingClient getCountsForProcess:error:]_block_invoke
- ___54-[SafeguardsManagingClient getCountsForProcess:error:]_block_invoke.59
- ___54-[SafeguardsManagingClient getCountsForProcess:error:]_block_invoke.cold.1
- ___55-[SafeguardsManagingClient getScenarioRefreshInterval:]_block_invoke.57
- ___61-[SafeguardsManagingClient forceMitigation:forProcess:error:]_block_invoke
- ___61-[SafeguardsManagingClient forceMitigation:forProcess:error:]_block_invoke.62
- ___61-[SafeguardsManagingClient forceMitigation:forProcess:error:]_block_invoke.62.cold.1
- ___61-[SafeguardsManagingClient forceMitigation:forProcess:error:]_block_invoke.cold.1
- ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.178
- ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.178.cold.1
- ___64-[PLClientLogger xpcConnectionWithClientID:withKey:withPayload:]_block_invoke.178.cold.2
- ___71-[SafeguardsManagingClient getProcessesAffectedByScenarioMapWithError:]_block_invoke.51
- ___76-[SafeguardsManagingClient getRestrictionsForProcess:forScenario:withError:]_block_invoke.53
- ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.214
- ___78-[PLClientLogger xpcSendMessageWithRateLimitingforClient:withKey:withPayload:]_block_invoke.215
- ___90-[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withLimit:error:]_block_invoke
- ___90-[SafeguardsManagingClient setTargetProcessTo:withPercentage:withSeconds:withLimit:error:]_block_invoke.cold.1
- ___block_literal_global.119
- ___block_literal_global.129
- ___block_literal_global.133
- ___block_literal_global.136
- ___block_literal_global.140
- ___block_literal_global.158
- ___handleXPCEvent_block_invoke.134
- _objc_msgSend$forceMitigation:forProcess:withHandler:
- _objc_msgSend$getCountsForProcess:WithHandler:
- _objc_msgSend$modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:
- _objc_msgSend$modifyRestrictionsByProcessPerScenario:
- _objc_msgSend$modifyTargetProcess:withPercentage:withSeconds:withLimit:
- _queryPowerlog
CStrings:
+ "%@_%@_%@"
+ "%@_%@_%@_%@"
+ "15d"
+ "5"
+ "8d"
+ "B56@0:8@16@24^B32^d40^@48"
+ "B64@0:8@16@24@32@40@48^@56"
+ "B96@0:8@16@24@32@40@48@56@64@72@80^@88"
+ "BackgroundProcessing"
+ "BackgroundProcessing::TaskInstanceData"
+ "BackgroundProcessing::TaskInstanceStore"
+ "BackgroundProcessing::TaskMetadata"
+ "BackgroundProcessing::TaskRuntimeAllocation"
+ "DrainSummary"
+ "Failed to clear target process %@"
+ "Failed to copy trigger interval %@"
+ "Failed to force CPU violation %@"
+ "Failed to force detection with startTime and endTime %@"
+ "Failed to force detector violation %@"
+ "Failed to force midnight routine %@"
+ "Failed to get cpu percentage trigger %@"
+ "Failed to get defaults %@"
+ "Failed to get mitigtaion information, %@"
+ "Failed to get monitored list %@"
+ "Failed to get penalty list %@"
+ "Failed to get process info %@"
+ "Failed to send coalition entries %@"
+ "Failed to set context %@"
+ "Failed to set defaults %@"
+ "Failed to set process info %@"
+ "Failed to set trigger interval %@"
+ "For BGSQL copy log, the insert Query is %@"
+ "For BGSQL copy, the table of interest is %@, the original Path is %@ and the copy dest is %@"
+ "INSERT INTO %@ (TaskEndTime, Reason) VALUES ('%@', '%@')"
+ "Reason"
+ "TaskEndTime"
+ "The BGSQL copy log insertion query failed"
+ "The BGSQL copy open database failed"
+ "The epoch time for BGSQL copy log is %f"
+ "The payload for BGSQL copy log is %@"
+ "TimeOfCaptureEvent"
+ "_dynamic"
+ "clearTargetProcess"
+ "clearTargetProcessWithError:"
+ "criticalBatteryLevel"
+ "dynamic"
+ "forceCPUViolationForProcess:error:"
+ "forceCPUViolationForProcess:withHandler:"
+ "forceDetectionWithStartTime:endTime:error:"
+ "forceDetectionWithStartTime:endTime:withHandler:"
+ "forceDetectorViolationForProcess:error:"
+ "forceDetectorViolationForProcess:withHandler:"
+ "forceMidnightRoutine:"
+ "forceMidnightRoutineWithHandler:"
+ "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:error:"
+ "forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:"
+ "getCpuPercentageTriggerForWindowEndDate:windowStartDate:crossedThreshold:score:error:"
+ "getCpuPercentageTriggerForWindowEndDate:windowStartDate:handler:"
+ "getDefaults:"
+ "getDefaultsWithHandler:"
+ "getInfoForProcess:error:"
+ "getInfoForProcess:withHandler:"
+ "getMitigationPolicy:"
+ "getMitigationPolicyWithHandler:"
+ "getMonitoredList:"
+ "getMonitoredListWithHandler:"
+ "getPenaltyList:"
+ "getPenaltyListWithHandler:"
+ "getTriggerInterval:"
+ "getTriggerIntervalWithHandler:"
+ "insightSummary"
+ "insightsAndSuggestionsSummaryKey"
+ "isDynamicEnd"
+ "modifyContextForIdentifier:withState:"
+ "modifyDefaults:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:withHandler:"
+ "modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:"
+ "modifyRestrictionsByProcessPerScenario:withHandler:"
+ "modifyTargetProcess:withPercentage:withSeconds:withPenaltyBoxDuration:"
+ "modifyTriggerInterval:"
+ "sendCoalitionEntries:error:"
+ "setContextForIdentifier:withState:error:"
+ "setDefaultsWithMaxFatalCount:withMaxNonFatal:withEnableMitigations:withEnablePenaltyBox:withPercentage:withSeconds:withPenaltyBoxDuration:withMitigationsPluggedIn:withMitigateXPCServices:error:"
+ "setInfoForProcess:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:error:"
+ "setTargetProcessTo:withPercentage:withSeconds:withPenaltyBoxDuration:error:"
+ "setTriggerInterval:error:"
+ "suggestionSummary"
+ "updateCoalitionEntries:withHandler:"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v28@?0B8d12@\"NSError\"20"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@\"NSNumber\"24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"NSDate\"16@\"NSDate\"24@?<v@?Bd@\"NSError\">32"
+ "v40@0:8@\"NSNumber\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
+ "v64@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"NSError\">56"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v96@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"NSNumber\"56@\"NSNumber\"64@\"NSNumber\"72@\"NSNumber\"80@?<v@?@\"NSError\">88"
+ "v96@0:8@16@24@32@40@48@56@64@72@80@?88"
- "BackgroundAppUsageInsight"
- "Failed to get process counts %@"
- "Failed to set process counts %@"
- "OngoingRestoreInsight"
- "OngoingUpgradeInsight"
- "PLBatteryGaugeQuery"
- "bui_background_app_usage_insight"
- "bui_device_setup"
- "forceMitigation:forProcess:error:"
- "forceMitigation:forProcess:withHandler:"
- "gauges_v2"
- "getCountsForProcess:WithHandler:"
- "getCountsForProcess:error:"
- "metric monitor feature enabled"
- "modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:"
- "modifyRestrictionsByProcessPerScenario:"
- "modifyTargetProcess:withPercentage:withSeconds:withLimit:"
- "return_value"
- "setProcessCountsFor:withFatalCount:withNonFatalCount:withExitCount:error:"
- "setTargetProcessTo:withPercentage:withSeconds:withLimit:error:"
- "v24@0:8@\"NSDictionary\"16"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"

```
