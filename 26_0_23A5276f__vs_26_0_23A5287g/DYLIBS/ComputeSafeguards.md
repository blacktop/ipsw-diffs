## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2964.0.40.502.1
-  __TEXT.__text: 0x2f104
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x271c
-  __TEXT.__const: 0x240
+2964.0.64.0.0
+  __TEXT.__text: 0x2f628
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x2754
+  __TEXT.__const: 0x260
   __TEXT.__gcc_except_tab: 0x500
-  __TEXT.__cstring: 0x334c
-  __TEXT.__oslogstring: 0x6952
-  __TEXT.__unwind_info: 0x850
+  __TEXT.__cstring: 0x345c
+  __TEXT.__oslogstring: 0x6a71
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0x2d9
-  __TEXT.__objc_methname: 0x6da6
-  __TEXT.__objc_methtype: 0xdd6
-  __TEXT.__objc_stubs: 0x3da0
+  __TEXT.__objc_methname: 0x700c
+  __TEXT.__objc_methtype: 0xe4a
+  __TEXT.__objc_stubs: 0x3e80
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x628
+  __DATA_CONST.__const: 0x688
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1728
+  __DATA_CONST.__objc_selrefs: 0x1768
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0xab8
-  __AUTH_CONST.__auth_got: 0x3a8
+  __DATA_CONST.__objc_arraydata: 0xac8
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x32a0
-  __AUTH_CONST.__objc_const: 0x3b00
+  __AUTH_CONST.__cfstring: 0x3360
+  __AUTH_CONST.__objc_const: 0x3b30
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x318
+  __DATA.__objc_ivar: 0x31c
   __DATA.__data: 0x318
   __DATA.__common: 0x48
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: 4C10795F-079A-3616-943E-3E25EAC5D940
-  Functions: 1137
-  Symbols:   3530
-  CStrings:  2596
+  UUID: FB72F3B4-298D-35AA-AFEF-3026B8D3552E
+  Functions: 1152
+  Symbols:   3569
+  CStrings:  2627
 
Symbols:
+ -[CSDetectionRule initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:]
+ -[CSDetectionRule initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:]
+ -[CSDetectionRule maxSlidingLookback]
+ -[CSDetectionRule processesAllowRegex]
+ -[CSDetectionRule processesDenyRegex]
+ -[CSDetectionRule setMaxSlidingLookback:]
+ -[CSDetectionRule setProcessesAllowRegex:]
+ -[CSDetectionRule setProcessesDenyRegex:]
+ -[CSIssueDetector _init].cold.1
+ -[CSIssueDetector genericCPUDetectorProcessDenyRegex]
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.4
+ -[CSIssueDetector getValueOfMetric:startDate:endDate:].cold.5
+ -[CSIssueDetector processCPUIntervalsForCondition:startDate:endDate:rule:normalizer:issueCandidates:]
+ -[CSIssueDetector processCPUIntervalsForCondition:startDate:endDate:rule:normalizer:issueCandidates:].cold.1
+ -[CSIssueDetector setGenericCPUDetectorProcessDenyRegex:]
+ -[CSPowerlogDBReader getCPUBasedIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:andMetricType:]
+ -[CSPowerlogDBReader getCPUBasedIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:andMetricType:].cold.1
+ -[CSPowerlogDBReader getCPUEnergyIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:]
+ -[CSProcess monitorForExitWithPID:].cold.3
+ _OBJC_IVAR_$_CSDetectionRule._maxSlidingLookback
+ _OBJC_IVAR_$_CSDetectionRule._processesAllowRegex
+ _OBJC_IVAR_$_CSDetectionRule._processesDenyRegex
+ _OBJC_IVAR_$_CSIssueDetector._genericCPUDetectorProcessDenyRegex
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.172
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.185
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.186
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.187
+ ___35-[CSProcess monitorForExitWithPID:]_block_invoke
+ ___35-[CSProcess monitorForExitWithPID:]_block_invoke_2
+ ___block_literal_global.155
+ ___block_literal_global.163
+ ___block_literal_global.179
+ ___block_literal_global.98
+ _dispatch_get_context
+ _dispatch_source_set_cancel_handler
+ _objc_msgSend$addTimeInterval:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$getCPUBasedIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:andMetricType:
+ _objc_msgSend$getCPUEnergyIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:
+ _objc_msgSend$initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:
+ _objc_msgSend$initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:
+ _objc_msgSend$maxSlidingLookback
+ _objc_msgSend$processCPUIntervalsForCondition:startDate:endDate:rule:normalizer:issueCandidates:
+ _objc_msgSend$processesAllowRegex
+ _objc_msgSend$processesDenyRegex
- -[CSDetectionRule initWithWindowSize:conditions:processesAllowList:processesDenyList:processesRegexAllowList:processesRegexDenyList:daemonOnly:mainThresholdValue:ruleID:]
- -[CSDetectionRule processesRegexAllowList]
- -[CSDetectionRule processesRegexDenyList]
- -[CSDetectionRule setProcessesRegexAllowList:]
- -[CSDetectionRule setProcessesRegexDenyList:]
- -[CSIssueDetector genericCPUDetectorProcessRegexDenyList]
- -[CSIssueDetector setGenericCPUDetectorProcessRegexDenyList:]
- -[CSIssueDetector string:matchesAnyRegexInArray:]
- _OBJC_IVAR_$_CSDetectionRule._processesRegexAllowList
- _OBJC_IVAR_$_CSDetectionRule._processesRegexDenyList
- _OBJC_IVAR_$_CSIssueDetector._genericCPUDetectorProcessRegexDenyList
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.175
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.188
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.189
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.190
- ___block_literal_global.141
- ___block_literal_global.166
- ___block_literal_global.170
- ___block_literal_global.85
- _dispatch_source_set_event_handler_f
- _objc_msgSend$initWithWindowSize:conditions:processesAllowList:processesDenyList:processesRegexAllowList:processesRegexDenyList:daemonOnly:mainThresholdValue:ruleID:
- _objc_msgSend$processesRegexAllowList
- _objc_msgSend$processesRegexDenyList
- _objc_msgSend$string:matchesAnyRegexInArray:
- _processExitHandler
CStrings:
+ "        SELECT LaunchdName AS %@, LaunchdCoalitionID AS %@, BundleId AS %@,         CASE WHEN timestamp > %f THEN timestamp ELSE %f END AS %@,         CASE WHEN timestampEnd < %f THEN timestampEnd ELSE %f END AS %@,         %@ AS %@         FROM PLCoalitionAgent_EventInterval_CoalitionInterval WHERE timestampEnd >= %f AND timestamp <= %f"
+ "@\"NSRegularExpression\""
+ "@56@0:8@16@24@32@40B48i52"
+ "@80@0:8f16f20f24@28@36@44@52@60B68f72i76"
+ "CPU %s %s threshold matches process with launchd name %@"
+ "CPUEnergyNormalized"
+ "CPUTimeNormalized"
+ "Metric Type CPUEnergy (%d) doesn't output a single value"
+ "Metric Type CPUEnergyUnplugged (%d) doesn't output a single value"
+ "T@\"NSRegularExpression\",&,V_genericCPUDetectorProcessDenyRegex"
+ "T@\"NSRegularExpression\",&,V_processesAllowRegex"
+ "T@\"NSRegularExpression\",&,V_processesDenyRegex"
+ "Tf,V_maxSlidingLookback"
+ "Unrecognized metric type passed to getCPUBasedIntervalListMapWithStartDate: %u"
+ "Unrecognized scalar metric type passed to processCPUIntervalsForCondition: %u"
+ "_genericCPUDetectorProcessDenyRegex"
+ "_maxSlidingLookback"
+ "_processesAllowRegex"
+ "_processesDenyRegex"
+ "addTimeInterval:"
+ "arrayByAddingObjectsFromArray:"
+ "com.apple.DiagnosticExtensions.FileArchiverService"
+ "com.apple.ReportCrash"
+ "com.apple.sysdiagnose"
+ "coreautomation\\.coreautomationd|^com\\.openssh\\.sshd\\."
+ "cpu_time / (timestampEnd - timestamp)"
+ "dictionaryWithDictionary:"
+ "energy"
+ "energy / 1000000.0 / (timestampEnd - timestamp)"
+ "genericCPUDetectorProcessDenyRegex"
+ "getCPUBasedIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:andMetricType:"
+ "getCPUEnergyIntervalListMapWithStartDate:andEndDate:andAllowListCoalitions:andDenyListCoalitions:andDaemonOnly:"
+ "initWithWindowSize:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:"
+ "initWithWindowSize:slidingWindowStepSize:maxSlidingLookback:conditions:processesAllowList:processesDenyList:processesAllowRegex:processesDenyRegex:daemonOnly:mainThresholdValue:ruleID:"
+ "maxSlidingLookback"
+ "monitorForExitWithPID: Failed to start monitoring process %@ (%d) for exit."
+ "monitorForExitWithPID: Monitor for process %@ (%d) already exists"
+ "monitorForExitWithPID: Started monitoring process %@ (%d) for exit."
+ "processCPUIntervalsForCondition:startDate:endDate:rule:normalizer:issueCandidates:"
+ "processesAllowRegex"
+ "processesDenyRegex"
+ "putIntoPenaltyBoxForProcess: Process:%@ and coalitionID %lld already in penalty box"
+ "putIntoPenaltyBoxForProcess: Put process:%@ and coalitionID %lld into penalty box. Reason: %s"
+ "seconds"
+ "select distinct Identifier as bundleId from PLApplicationAgent_EventForward_Application"
+ "setGenericCPUDetectorProcessDenyRegex:"
+ "setMaxSlidingLookback:"
+ "setProcessesAllowRegex:"
+ "setProcessesDenyRegex:"
+ "unplugged"
+ "v64@0:8@16@24@32@40@48@56"
- "++CPU threshold matches process %@"
- "++CPU unplugged threshold matches process %@"
- ".*coreautomation.coreautomationd.*"
- "Monitor for process %@ (%d) already exists"
- "SELECT LaunchdName AS %@, LaunchdCoalitionID AS %@, BundleId AS %@, CASE WHEN timestamp > %f THEN timestamp ELSE %f END AS %@, CASE WHEN timestampEnd < %f THEN timestampEnd ELSE %f END AS %@, cpu_time / (timestampEnd - timestamp) AS %@ FROM PLCoalitionAgent_EventInterval_CoalitionInterval WHERE timestampEnd >= %f AND timestamp <= %f"
- "Skip evaluting rule since duration from %@ to %@ is not enough for %f"
- "Skip evaluting rule since startDate %@ is later than endDate %@"
- "Started monitoring process %@ (%d) for exit."
- "T@\"NSArray\",&,V_genericCPUDetectorProcessRegexDenyList"
- "T@\"NSArray\",&,V_processesRegexAllowList"
- "T@\"NSArray\",&,V_processesRegexDenyList"
- "_genericCPUDetectorProcessRegexDenyList"
- "_processesRegexAllowList"
- "_processesRegexDenyList"
- "com\\.openssh\\.sshd\\..*"
- "genericCPUDetectorProcessRegexDenyList"
- "initWithWindowSize:conditions:processesAllowList:processesDenyList:processesRegexAllowList:processesRegexDenyList:daemonOnly:mainThresholdValue:ruleID:"
- "processesRegexAllowList"
- "processesRegexDenyList"
- "putIntoPenaltyBoxForProcess: Process:%@ already in penalty box"
- "putIntoPenaltyBoxForProcess: Put process:%@ into penalty box. Reason: %s"
- "select distinct AppBundleId as bundleId from PLApplicationAgent_EventNone_AllApps"
- "setGenericCPUDetectorProcessRegexDenyList:"
- "setProcessesRegexAllowList:"
- "setProcessesRegexDenyList:"
- "string:matchesAnyRegexInArray:"

```
