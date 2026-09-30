## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0x9f58
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0xb40
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__cstring: 0x1510
-  __TEXT.__oslogstring: 0x13f9
+2423.100.226.0.0
+  __TEXT.__text: 0x110e4
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_methlist: 0x120c
+  __TEXT.__const: 0x110
+  __TEXT.__gcc_except_tab: 0x2f0
+  __TEXT.__cstring: 0x17c1
+  __TEXT.__oslogstring: 0x2215
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x2c8
-  __TEXT.__objc_classname: 0x1fe
-  __TEXT.__objc_methname: 0x1e1a
-  __TEXT.__objc_methtype: 0x41f
-  __TEXT.__objc_stubs: 0x11c0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x1b0
+  __TEXT.__unwind_info: 0x448
+  __TEXT.__objc_classname: 0x225
+  __TEXT.__objc_methname: 0x2ec9
+  __TEXT.__objc_methtype: 0x6af
+  __TEXT.__objc_stubs: 0x18e0
+  __DATA_CONST.__got: 0x118
+  __DATA_CONST.__const: 0x380
   __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
-  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_selrefs: 0xa88
+  __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_arraydata: 0xf40
-  __AUTH_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__objc_arraydata: 0xff8
+  __AUTH_CONST.__auth_got: 0x2f0
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1a60
-  __AUTH_CONST.__objc_const: 0x1b58
-  __AUTH_CONST.__objc_intobj: 0x3ca8
-  __AUTH_CONST.__objc_dictobj: 0x488
-  __AUTH_CONST.__objc_doubleobj: 0xf10
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__cfstring: 0x1e00
+  __AUTH_CONST.__objc_const: 0x1e70
+  __AUTH_CONST.__objc_intobj: 0x3e40
+  __AUTH_CONST.__objc_dictobj: 0x528
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_doubleobj: 0xf20
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xd8
-  __DATA.__data: 0x2a0
+  __DATA.__objc_ivar: 0x14c
+  __DATA.__data: 0x300
+  __DATA.__common: 0x20
   __DATA.__bss: 0x4
   __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 337
-  Symbols:   500
-  CStrings:  748
+  Functions: 516
+  Symbols:   704
+  CStrings:  1035
 
Symbols:
+ _CSManagingServiceName
+ _CSRestrictionManagerErrorDomain
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_PLDefaults
+ _basename
+ _bzero
+ _dispatch_suspend
+ _dispatch_sync
+ _gOverrideCPUPercentage
+ _gOverrideCPUTimeWindow
+ _gOverrideLimitCPUPercentage
+ _gOverrideProcess
+ _kPowerExceptionEnableLimitCPUUsage
+ _kPowerExceptionGlobalCPUPercentage
+ _kPowerExceptionGlobalCPUTimeWindow
+ _kPowerExceptionGlobalLimitCPUPercentage
+ _kPowerExceptionMaxKills
+ _kPowerExceptionMaxNonFatal
+ _objc_retain_x27
+ _proc_pidpath
+ _proc_setcpu_percentage
+ _strerror
CStrings:
+ "\x04"
+ "\b"
+ "\f"
+ "\x19"
+ "!21"
+ "%s: CSProcess not found for PID: %d "
+ "(NON FATAL) "
+ "-[CSProcessManager incrementCPUViolationCounter:fatal:]"
+ "@\"CSDaemon\""
+ "@\"NSMutableDictionary\"16@0:8"
+ "@36@0:8@16@24B32"
+ "AffectedProcesses for contextIdentifier:%@ updated to %@"
+ "AffectedProcesses for contextIdentifier:%@ was already set to %@"
+ "Attempted applying thresholds on invalid PID for process:%@ (%d)"
+ "Attempted cleanup on Process:%@ with no currentPID"
+ "Attempted monitoring on invalid PID:%d for process %@"
+ "Attempted setting invalid PID for Process:%@"
+ "ByBand: Allocating for Band10"
+ "ByBand: Allocating for Band15"
+ "ByBand: Allocating for Band20"
+ "ByBand: Allocating for Band25"
+ "ByBand: Allocating for Band30"
+ "ByBand: Allocating for Band35"
+ "ByBand: Allocating for Band40"
+ "ByBand: Allocating for Band45"
+ "ByBand: Allocating for Band50"
+ "ByBand: Allocating for Band55"
+ "ByBand: Allocating for Band60"
+ "ByBand: Allocating for Band65"
+ "ByBand: Allocating for Band70"
+ "ByBand: Allocating for Band75"
+ "ByBand: Allocating for Band80"
+ "ByBand: Allocating for Band85"
+ "ByBand: Allocating for Band90"
+ "ByBand: Allocating for Band95"
+ "CPULimit"
+ "CSCPUTimeRestriction with cpuThreshold: %@, timeWindow: %@, fatal: %d"
+ "CSRestrictionManagerErrorDomain"
+ "Clearing current restrictions for process:%@"
+ "Configuring cpuMonitor with cpuThreshold: %@, timeWindow:%@, fatal:%s, limit_cpu_usage:%s for process:%@ (%d)"
+ "Could not locate CSProcess object for processName:%@ so ignoring this violation"
+ "Error enabling CPU monitoring: %d (%s)"
+ "ExcessiveCPUPercentage"
+ "ExcessiveCPUTimeWindow"
+ "Failed %d to apply thresholds on process:%@ (%d)"
+ "Failed to get CSProcessManager for logging violation???"
+ "Failed to release restriction:%@ for process:%@"
+ "Fatal"
+ "Fatal violation count (%llu >= %ld) so setting non fatal for process:%@ (%d)"
+ "FatalCount"
+ "FromPowerExceptions"
+ "Global CPU monitoring percentage has been changed to %ld"
+ "Global CPU monitoring time window has been changed to %ld"
+ "Global Max cpu usage limit percentage has been changed to %ld"
+ "Global overriding cpu threshold to be (%ld) for process:%@ (%d)"
+ "Global overriding cpu time window to be (%ld) for process:%@ (%d)"
+ "Global overriding cpu usage limit threshold to be (%ld) for process:%@ (%d)"
+ "Incrementing %s violation counters for process %@ (%d)"
+ "Inspecting restriction: %@ for process:%@"
+ "IssueType"
+ "IssueType:%lld MitigationType:%lld MitigationReason:%lld cpu_fatal_cnt:%llu cpu_non_fatal_cnt:%llu exits_cnt:%llu for process %@ (%llu)"
+ "LimitCPUTimeWindow"
+ "Max cpu usage limit has been enabled with %ld"
+ "Max number of fatal violations has been changed to %ld"
+ "Max number of non fatal violations has been changed to %ld"
+ "MitigationReason"
+ "MitigationType"
+ "Monitor for process %@ (%d) already exists"
+ "No"
+ "No available active scenario for process:%@."
+ "Non fatal violation count (%llu >= %ld) so setting max cpu limit for process:%@ (%d)"
+ "NonFatal"
+ "NonFatalCount"
+ "Not Set"
+ "Overriding cpu threshold to be (%ld) for process:%@ (%d)"
+ "Overriding cpu time window to be (%ld) for process:%@ (%d)"
+ "Overriding cpu usage limit threshold to be (%ld) for process:%@ (%d)"
+ "PIDPollingInterval"
+ "Picking scenario %@ for process:%@"
+ "PowerExceptionEnableLimitCPUUsage"
+ "PowerExceptionGlobalCPUPercentage"
+ "PowerExceptionGlobalCPUTimeWindow"
+ "PowerExceptionGlobalLimitCPUPercentage"
+ "PowerExceptionMaxKills"
+ "PowerExceptionMaxNonFatal"
+ "Process:%@ (%d) exited"
+ "Q"
+ "Received %sCPU violation: %@[%llu] (%@) used %.2f seconds of CPU over %.2f seconds (averaging %d%%), violating a CPU usage limit of %.2f seconds over %lld seconds."
+ "SafeguardsScheduledWorkReporting"
+ "Scenarios that remain changed after debounce: %@"
+ "ScheduledIntensive"
+ "ScheduledIntensiveActivities"
+ "Sending %s violation fromPowerExceptions (%s) for process %@ (%llu) to Power Log"
+ "Started monitoring process %@ (%d) for exit."
+ "T@\"CSDaemon\",&,V_safeguardsDaemon"
+ "T@\"NSDictionary\",&,N,V_restrictionsByProcess"
+ "T@\"NSMutableDictionary\",&,N,V_activeScenariosWithRestrictions"
+ "T@\"NSMutableDictionary\",&,N,V_currentAffectedRestrictionsForContext"
+ "T@\"NSMutableDictionary\",&,N,V_currentContextDate"
+ "T@\"NSMutableDictionary\",&,N,V_currentPIDList"
+ "T@\"NSMutableDictionary\",&,N,V_processNameIdentiferByName"
+ "T@\"NSMutableDictionary\",&,V_currentActiveScenariosWithRestrictions"
+ "T@\"NSMutableDictionary\",&,V_restrictionsByProcessForScenario"
+ "T@\"NSMutableDictionary\",&,V_restrictionsByProcessPerScenario"
+ "T@\"NSNumber\",&,N,V_cpuThreshold"
+ "T@\"NSNumber\",&,N,V_cpuTimeWindow"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_processExitMonitor"
+ "TB,N,V_cpuIsFatal"
+ "TB,N,V_cpuUsageLimitSet"
+ "TB,N,V_needClearRestrictions"
+ "TB,N,V_resetNonFatalCPUMonitor"
+ "TB,R,N,V_fatalMitigation"
+ "TQ,N,V_cpu_fatal_cnt"
+ "TQ,N,V_cpu_nonfatal_cnt"
+ "TQ,N,V_exits_cnt"
+ "TQ,N,V_issueType"
+ "TQ,N,V_mitigationReason"
+ "TQ,N,V_mitigationType"
+ "TargetProcess"
+ "Tf,N,V_PIDPollingInterval"
+ "TimeWindowSize"
+ "Tq,V_debounceTimeBeforeRestrictions"
+ "Tq,V_enableLimitCPUUsage"
+ "Tq,V_globalOverrideCPUPercentage"
+ "Tq,V_globalOverrideCPUTimeWindow"
+ "Tq,V_globalOverrideLimitCPUPercentage"
+ "Tq,V_maxNumberOfKills"
+ "Tq,V_maxNumberOfNonfatal"
+ "Violation not from us? savedFatal (%d) == isFatal (%d), savedTimeWindow (%lld) == limitWindow (%lld), savedThreshold (%llu) == limitValue (%lld) for processName:%@"
+ "Yes"
+ "_PIDPollingInterval"
+ "_activeScenariosWithRestrictions"
+ "_cpuIsFatal"
+ "_cpuTimeWindow"
+ "_cpuUsageLimitSet"
+ "_cpu_fatal_cnt"
+ "_cpu_nonfatal_cnt"
+ "_currentActiveScenariosWithRestrictions"
+ "_currentAffectedRestrictionsForContext"
+ "_currentContextDate"
+ "_currentPIDList"
+ "_debounceTimeBeforeRestrictions"
+ "_enableLimitCPUUsage"
+ "_exits_cnt"
+ "_fatalMitigation"
+ "_globalOverrideCPUPercentage"
+ "_globalOverrideCPUTimeWindow"
+ "_globalOverrideLimitCPUPercentage"
+ "_issueType"
+ "_maxNumberOfKills"
+ "_maxNumberOfNonfatal"
+ "_mitigationReason"
+ "_mitigationType"
+ "_needClearRestrictions"
+ "_processExitMonitor"
+ "_processNameIdentiferByName"
+ "_processesAffectedByScenarioMap[%@]: %@"
+ "_resetNonFatalCPUMonitor"
+ "_restrictionsByProcess"
+ "_safeguardsDaemon"
+ "activeScenariosWithRestrictions"
+ "allObjects"
+ "allValues"
+ "arrayWithObject:"
+ "clearRestrictionsForProcess:"
+ "com.apple.computesafeguards.managing"
+ "com.apple.matd"
+ "com.apple.migrationd"
+ "cpuIsFatal"
+ "cpuTimeWindow"
+ "cpuUsageLimitSet"
+ "cpu_fatal_cnt"
+ "cpu_nonfatal_cnt"
+ "currentActiveScenariosWithRestrictions"
+ "currentAffectedRestrictionsForContext"
+ "currentContextDate"
+ "currentPIDList"
+ "date"
+ "debounceTimeBeforeRestrictions"
+ "determineAndApplyRestrictionsForProcess:"
+ "dictionaryWithValuesForKeys:"
+ "doubleValue"
+ "enableLimitCPUUsage"
+ "exits_cnt"
+ "f"
+ "f16@0:8"
+ "fatal"
+ "fatalMitigation"
+ "forceMitigation: Attempted applying thresholds on invalid PID for process:%@ (%d)"
+ "forceMitigation: Could not locate CSProcess for process:%@"
+ "forceMitigation: Error enabling CPU monitoring: %d (%s) for process:%@"
+ "forceMitigation: Force mitigation %@ for process: %@"
+ "forceMitigation: Unknown mitigation: %@ for process:%@"
+ "forceMitigation:forProcess:withHandler:"
+ "fullProcessNameForPid:"
+ "getActiveScenariosWithHandler:"
+ "getCountsForProcess: Could not locate CSProcess for process:%@"
+ "getCountsForProcess:WithHandler:"
+ "getPollingInterval"
+ "getPollingIntervalWithHandler:"
+ "getProcessesAffectedByScenarioMapWithHandler:"
+ "getProperties"
+ "getRestrictionsForProcess: count=0 for process: %@, scenario: %@"
+ "getRestrictionsForProcess: nothing found for process: %@"
+ "getRestrictionsForProcess: nothing found for process: %@, scenario: %@"
+ "getRestrictionsForProcess: restrictionsDictionaries: %@"
+ "getRestrictionsForProcess:forScenario:withHandler:"
+ "getScenarioRefreshIntervalWithHandler:"
+ "getScenariosWithHandler:"
+ "getTargetProcessWithHandler:"
+ "globalOverrideCPUPercentage"
+ "globalOverrideCPUTimeWindow"
+ "globalOverrideLimitCPUPercentage"
+ "hasPrefix:"
+ "i36@0:8f16f20i24B28B32"
+ "identiferForName:"
+ "incrementCPUViolationCounter:"
+ "incrementCPUViolationCounter:fatal:"
+ "incrementExitCounter"
+ "initWithThreshold:andTimeWindow:andFatal:"
+ "intValue"
+ "isEqualToArray:"
+ "issueType"
+ "leniencyScore"
+ "longForKey:ifNotSet:"
+ "longLongValue"
+ "longValue"
+ "maxNumberOfKills"
+ "maxNumberOfNonfatal"
+ "mitigationReason"
+ "mitigationType"
+ "modifyPollingInterval:"
+ "modifyProcessCounts: Could not locate CSProcess for process:%@"
+ "modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:"
+ "modifyRestrictionsByProcessPerScenario:"
+ "modifyScenarioRefreshInterval:"
+ "modifyTargetProcess:withPercentage:withSeconds:withLimit:"
+ "needClearRestrictions"
+ "non fatal"
+ "not null"
+ "null"
+ "numberWithBool:"
+ "numberWithFloat:"
+ "numberWithLongLong:"
+ "pollPIDs: %@ was PID: %d before, is %d now. CSProcess exit handler should fire soon."
+ "pollPIDs: Allowing _overrideProcess of %@ (%d)"
+ "pollPIDs: Error grabbing RBSProcessHandle (pid%i) to perform isDaemon check %@"
+ "pollPIDs: Process:%@ (%d) got a non fatal violation, trying to re-arm the monitoring"
+ "pollPIDs: Process:%@ (%d) is not explicitly enrolled, it will get default restrictions."
+ "pollPIDs: Process:%@ (%d) seems to have relaunched since saved pid is PID_NOT_RUNNING"
+ "pollPIDs: Skipping pid: %d since fullProcessNameForPid failed"
+ "pollPIDs: Skipping pid: %d since it is not a daemon"
+ "pollPIDs: Tracking process:%@ (%d)"
+ "pollPIDs: called, currentPIDList: %s"
+ "pollPIDs: name: %@ identifier: %@"
+ "pollPIDs: totalPIDs: %d skippedPIDs: %d queryRBSPIDs: %d monitorPIDs: %d"
+ "process is nil?"
+ "processExitMonitor"
+ "processNameIdentiferByName"
+ "q16@0:8"
+ "removeObjectsForKeys:"
+ "reportScheduledIntensiveWorkByProcesses:"
+ "reportScheduledIntensiveWorkByProcesses: create DAS context for processes %@, state:%@"
+ "reportScheduledIntensiveWorkByProcesses: unrecognized process name: %@"
+ "resetNonFatalCPUMonitor"
+ "restrictionsByProcess"
+ "restrictionsForScenario:"
+ "safeguardsDaemon"
+ "scenario: %@, set restrictions:%@"
+ "setActiveScenariosWithRestrictions:"
+ "setCpuIsFatal:"
+ "setCpuThreshold:"
+ "setCpuTimeWindow:"
+ "setCpuUsageLimitSet:"
+ "setCpu_fatal_cnt:"
+ "setCpu_nonfatal_cnt:"
+ "setCurrentActiveScenariosWithRestrictions:"
+ "setCurrentAffectedRestrictionsForContext:"
+ "setCurrentContextDate:"
+ "setCurrentPIDList:"
+ "setDebounceTimeBeforeRestrictions:"
+ "setEnableLimitCPUUsage:"
+ "setExits_cnt:"
+ "setGlobalOverrideCPUPercentage:"
+ "setGlobalOverrideCPUTimeWindow:"
+ "setGlobalOverrideLimitCPUPercentage:"
+ "setIssueType:"
+ "setMaxNumberOfKills:"
+ "setMaxNumberOfNonfatal:"
+ "setMitigationReason:"
+ "setMitigationType:"
+ "setNeedClearRestrictions:"
+ "setPIDPollingInterval:"
+ "setProcessExitMonitor:"
+ "setProcessNameIdentiferByName:"
+ "setResetNonFatalCPUMonitor:"
+ "setRestrictionsByProcess:"
+ "setSafeguardsDaemon:"
+ "setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:"
+ "shouldBeFatalOnViolation"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringWithUTF8String:"
+ "updateContextForIdentifier:withState:withRestrictions:"
+ "updateRestrictionsDataForScenarios:"
+ "updateState:forIdentifier:withRestrictions:"
+ "v20@0:8f16"
+ "v24@0:8@\"NSDictionary\"16"
+ "v24@0:8@\"NSNumber\"16"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSDictionary\">16"
+ "v24@0:8@?<v@?@\"NSNumber\">16"
+ "v24@0:8@?<v@?@\"NSSet\">16"
+ "v24@0:8i16B20"
+ "v24@0:8q16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@16@?24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSArray\">32"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40"
+ "v48@0:8@16@24@32@40"
+ "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@?<v@?@\"NSError\">48"
+ "v56@0:8@16@24@32@40@?48"
- "\a"
- "\n"
- "\x17"
- "%@ was PID: %d before, is %d now. Exit handler should fire soon."
- "Attmpted applying thresholds on invalid PID: %d"
- "Attmpted cleanup on Process:%@ with no currentPID"
- "Attmpted monitoring on invalid PID:%d "
- "Attmpted setting invalid PID for Process:%@"
- "ByBand: Allocating for Band1"
- "ByBand: Allocating for Band2"
- "ByBand: Allocating for Band3"
- "CSCPUTimeRestriction with cpuThreshold: %@, timeWindow: %@"
- "Configuring cpuMonitor with cpuThreshold: %@ and timeWindow:%@ for pid:%d"
- "Error enabling CPU monitoring: %d"
- "Error grabbing RBSProcessHandle (pid%i) to perform isDaemon check %@"
- "Failed to apply thresholds on PID: %d"
- "Mitigation"
- "Monitor for pid:%d already exists"
- "Picking scenario for process:%@ at random from multiple options."
- "Process:%@[%d] is not explicitly enrolled, it will get default restrictions."
- "Received %sCPU violation: %@[%llu] (%@) used %.2fs of CPU over %.2f seconds (averaging %d%%), violating a CPU usage limit of %.2fs over %lld seconds."
- "Scenarios that remain changed after deounce: %@"
- "Skipping pid: %d since it is not a daemon"
- "Skipping pid: %d since we could not get daemonJobLabel, bundleIDidentifier or name"
- "Started monitoring pid:%d for exit."
- "T@\"NSDictionary\",&,V_restrictionsByProcessForScenario"
- "T@\"NSDictionary\",&,V_restrictionsByProcessPerScenario"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_processMonitor"
- "TimeWndowSize"
- "Tracking pid: %d for process:%@"
- "Using bundleID:%@ for pid: %d"
- "Using daemonJobLabel:%@ for pid: %d"
- "Using name:%@ for pid: %d"
- "_processMonitor"
- "_shouldBeFatalOnViolation"
- "bundle"
- "daemonJobLabel"
- "i32@0:8f16f20i24B28"
- "processMonitor"
- "setProcessMonitor:"
- "setThreshold:overTimeWindow:forPID:withFatalEffect:"

```
