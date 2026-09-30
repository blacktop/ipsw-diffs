## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/Versions/A/ComputeSafeguards`

```diff

-2308.80.23.0.0
-  __TEXT.__text: 0xa5a0
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0xb40
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x14c6
-  __TEXT.__oslogstring: 0x1390
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__unwind_info: 0x290
-  __TEXT.__objc_classname: 0x1fd
-  __TEXT.__objc_methname: 0x1e1a
-  __TEXT.__objc_methtype: 0x41f
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0x38
+2423.100.232.0.0
+  __TEXT.__text: 0x12294
+  __TEXT.__auth_stubs: 0x400
+  __TEXT.__objc_methlist: 0x120c
+  __TEXT.__const: 0x110
+  __TEXT.__cstring: 0x1777
+  __TEXT.__oslogstring: 0x2155
+  __TEXT.__gcc_except_tab: 0x2cc
+  __TEXT.__unwind_info: 0x410
+  __TEXT.__objc_classname: 0x224
+  __TEXT.__objc_methname: 0x2ec9
+  __TEXT.__objc_methtype: 0x6af
+  __TEXT.__objc_stubs: 0x17e0
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__const: 0x78
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
-  __AUTH_CONST.__auth_got: 0x1c8
-  __AUTH_CONST.__const: 0x2b0
-  __AUTH_CONST.__cfstring: 0x1a20
-  __AUTH_CONST.__objc_const: 0x1b58
-  __AUTH_CONST.__objc_intobj: 0x3ab0
-  __AUTH_CONST.__objc_dictobj: 0x488
-  __AUTH_CONST.__objc_doubleobj: 0xde0
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_arraydata: 0xff8
+  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__cfstring: 0x1dc0
+  __AUTH_CONST.__objc_const: 0x1e70
+  __AUTH_CONST.__objc_intobj: 0x3e40
+  __AUTH_CONST.__objc_dictobj: 0x528
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_doubleobj: 0xf20
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0xd8
-  __DATA.__data: 0x2a0
+  __DATA.__objc_ivar: 0x14c
+  __DATA.__data: 0x300
   __DATA.__bss: 0xd8
+  __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/PrivateFrameworks/PowerlogCore.framework/Versions/A/PowerlogCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 90088D98-EBE8-39E3-A6E7-933D495A81B7
-  Functions: 341
-  Symbols:   839
-  CStrings:  940
+  UUID: 04BE8D97-A42C-3DFE-9E64-2A95B7AAE383
+  Functions: 532
+  Symbols:   1168
+  CStrings:  1254
 
Symbols:
+ +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:]
+ +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:].cold.1
+ +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:].cold.2
+ +[CSContextStore sharedInstance].cold.1
+ +[CSDaemon _sharedInstance].cold.1
+ +[CSDaemon run].cold.1
+ +[CSExcessiveCPUViolationHandler sharedInstance].cold.1
+ +[CSLogger initialize].cold.1
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.10
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.11
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.12
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.13
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.14
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.15
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.16
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.17
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.18
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.19
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.5
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.6
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.7
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.8
+ +[CSRestrictionFactory _cpuTimeRestrictionWithBand:errors:].cold.9
+ +[CSScenarioManager sharedInstance].cold.1
+ +[CSViolationHandlerService _sharedInstance].cold.1
+ +[CSViolationHandlerService run].cold.1
+ -[CSCPUTimeRestriction applyToProcess:].cold.4
+ -[CSCPUTimeRestriction applyToProcess:].cold.5
+ -[CSCPUTimeRestriction enableLimitCPUUsage]
+ -[CSCPUTimeRestriction fatalMitigation]
+ -[CSCPUTimeRestriction getProperties]
+ -[CSCPUTimeRestriction globalOverrideCPUPercentage]
+ -[CSCPUTimeRestriction globalOverrideCPUTimeWindow]
+ -[CSCPUTimeRestriction globalOverrideLimitCPUPercentage]
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.1
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.2
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.3
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.4
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.5
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:].cold.6
+ -[CSCPUTimeRestriction initWithThreshold:andTimeWindow:andFatal:]
+ -[CSCPUTimeRestriction leniencyScore]
+ -[CSCPUTimeRestriction maxNumberOfKills]
+ -[CSCPUTimeRestriction maxNumberOfNonfatal]
+ -[CSCPUTimeRestriction setEnableLimitCPUUsage:]
+ -[CSCPUTimeRestriction setGlobalOverrideCPUPercentage:]
+ -[CSCPUTimeRestriction setGlobalOverrideCPUTimeWindow:]
+ -[CSCPUTimeRestriction setGlobalOverrideLimitCPUPercentage:]
+ -[CSCPUTimeRestriction setMaxNumberOfKills:]
+ -[CSCPUTimeRestriction setMaxNumberOfNonfatal:]
+ -[CSCPUTimeRestriction shouldBeFatalOnViolation]
+ -[CSContextStore currentAffectedRestrictionsForContext]
+ -[CSContextStore currentContextDate]
+ -[CSContextStore setCurrentAffectedRestrictionsForContext:]
+ -[CSContextStore setCurrentContextDate:]
+ -[CSContextStore updateState:forIdentifier:withRestrictions:]
+ -[CSContextStore updateState:forIdentifier:withRestrictions:].cold.1
+ -[CSContextStore updateState:forIdentifier:withRestrictions:].cold.2
+ -[CSDaemon updateContextForIdentifier:withState:withRestrictions:]
+ -[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.4
+ -[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.5
+ -[CSProcess cpuIsFatal]
+ -[CSProcess cpuThreshold]
+ -[CSProcess cpuTimeWindow]
+ -[CSProcess cpuUsageLimitSet]
+ -[CSProcess cpu_fatal_cnt]
+ -[CSProcess cpu_nonfatal_cnt]
+ -[CSProcess exits_cnt]
+ -[CSProcess incrementCPUViolationCounter:]
+ -[CSProcess incrementExitCounter]
+ -[CSProcess issueType]
+ -[CSProcess mitigationReason]
+ -[CSProcess mitigationType]
+ -[CSProcess needClearRestrictions]
+ -[CSProcess processExitMonitor]
+ -[CSProcess resetNonFatalCPUMonitor]
+ -[CSProcess setCpuIsFatal:]
+ -[CSProcess setCpuThreshold:]
+ -[CSProcess setCpuTimeWindow:]
+ -[CSProcess setCpuUsageLimitSet:]
+ -[CSProcess setCpu_fatal_cnt:]
+ -[CSProcess setCpu_nonfatal_cnt:]
+ -[CSProcess setExits_cnt:]
+ -[CSProcess setIssueType:]
+ -[CSProcess setMitigationReason:]
+ -[CSProcess setMitigationType:]
+ -[CSProcess setNeedClearRestrictions:]
+ -[CSProcess setProcessExitMonitor:]
+ -[CSProcess setResetNonFatalCPUMonitor:]
+ -[CSProcessManager PIDPollingInterval]
+ -[CSProcessManager currentPIDList]
+ -[CSProcessManager fullProcessNameForPid:]
+ -[CSProcessManager getPollingInterval]
+ -[CSProcessManager identiferForName:]
+ -[CSProcessManager incrementCPUViolationCounter:fatal:]
+ -[CSProcessManager incrementCPUViolationCounter:fatal:].cold.1
+ -[CSProcessManager modifyPollingInterval:]
+ -[CSProcessManager pollPIDs].cold.1
+ -[CSProcessManager processNameIdentiferByName]
+ -[CSProcessManager recordTerminationForPID:].cold.1
+ -[CSProcessManager setCurrentPIDList:]
+ -[CSProcessManager setPIDPollingInterval:]
+ -[CSProcessManager setProcessNameIdentiferByName:]
+ -[CSRestrictionManager clearRestrictionsForProcess:]
+ -[CSRestrictionManager clearRestrictionsForProcess:].cold.1
+ -[CSRestrictionManager currentActiveScenariosWithRestrictions]
+ -[CSRestrictionManager debounceTimeBeforeRestrictions]
+ -[CSRestrictionManager determineAndApplyRestrictionsForProcess:]
+ -[CSRestrictionManager determineScenarioForProcess:].cold.3
+ -[CSRestrictionManager forceMitigation:forProcess:withHandler:]
+ -[CSRestrictionManager forceMitigation:forProcess:withHandler:].cold.1
+ -[CSRestrictionManager forceMitigation:forProcess:withHandler:].cold.2
+ -[CSRestrictionManager forceMitigation:forProcess:withHandler:].cold.3
+ -[CSRestrictionManager getActiveScenariosWithHandler:]
+ -[CSRestrictionManager getCountsForProcess:WithHandler:]
+ -[CSRestrictionManager getCountsForProcess:WithHandler:].cold.1
+ -[CSRestrictionManager getPollingIntervalWithHandler:]
+ -[CSRestrictionManager getProcessesAffectedByScenarioMapWithHandler:]
+ -[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]
+ -[CSRestrictionManager getScenarioRefreshIntervalWithHandler:]
+ -[CSRestrictionManager getScenariosWithHandler:]
+ -[CSRestrictionManager getTargetProcessWithHandler:]
+ -[CSRestrictionManager listener:shouldAcceptNewConnection:]
+ -[CSRestrictionManager modifyPollingInterval:]
+ -[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:]
+ -[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:].cold.1
+ -[CSRestrictionManager modifyRestrictionsByProcessPerScenario:]
+ -[CSRestrictionManager modifyScenarioRefreshInterval:]
+ -[CSRestrictionManager modifyTargetProcess:withPercentage:withSeconds:withLimit:]
+ -[CSRestrictionManager reportScheduledIntensiveWorkByProcesses:]
+ -[CSRestrictionManager safeguardsDaemon]
+ -[CSRestrictionManager setCurrentActiveScenariosWithRestrictions:]
+ -[CSRestrictionManager setDebounceTimeBeforeRestrictions:]
+ -[CSRestrictionManager setSafeguardsDaemon:]
+ -[CSRestrictionManager updateRestrictionsDataForScenarios:]
+ -[CSScenario restrictionsByProcess]
+ -[CSScenario setRestrictionsByProcess:]
+ -[CSScenarioManager activeScenariosWithRestrictions]
+ -[CSScenarioManager restrictionsForScenario:]
+ -[CSScenarioManager setActiveScenariosWithRestrictions:]
+ -[CSScenarioRestrictionsAttributesTemplate isEqual:]
+ GCC_except_table13
+ GCC_except_table14
+ GCC_except_table22
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table37
+ GCC_except_table39
+ GCC_except_table43
+ GCC_except_table61
+ GCC_except_table66
+ OBJC_IVAR_$_CSCPUTimeRestriction._enableLimitCPUUsage
+ OBJC_IVAR_$_CSCPUTimeRestriction._fatalMitigation
+ OBJC_IVAR_$_CSCPUTimeRestriction._globalOverrideCPUPercentage
+ OBJC_IVAR_$_CSCPUTimeRestriction._globalOverrideCPUTimeWindow
+ OBJC_IVAR_$_CSCPUTimeRestriction._globalOverrideLimitCPUPercentage
+ OBJC_IVAR_$_CSCPUTimeRestriction._maxNumberOfKills
+ OBJC_IVAR_$_CSCPUTimeRestriction._maxNumberOfNonfatal
+ OBJC_IVAR_$_CSContextStore._currentAffectedRestrictionsForContext
+ OBJC_IVAR_$_CSContextStore._currentContextDate
+ OBJC_IVAR_$_CSProcess._cpuIsFatal
+ OBJC_IVAR_$_CSProcess._cpuThreshold
+ OBJC_IVAR_$_CSProcess._cpuTimeWindow
+ OBJC_IVAR_$_CSProcess._cpuUsageLimitSet
+ OBJC_IVAR_$_CSProcess._cpu_fatal_cnt
+ OBJC_IVAR_$_CSProcess._cpu_nonfatal_cnt
+ OBJC_IVAR_$_CSProcess._exits_cnt
+ OBJC_IVAR_$_CSProcess._issueType
+ OBJC_IVAR_$_CSProcess._mitigationReason
+ OBJC_IVAR_$_CSProcess._mitigationType
+ OBJC_IVAR_$_CSProcess._needClearRestrictions
+ OBJC_IVAR_$_CSProcess._processExitMonitor
+ OBJC_IVAR_$_CSProcess._resetNonFatalCPUMonitor
+ OBJC_IVAR_$_CSProcessManager._PIDPollingInterval
+ OBJC_IVAR_$_CSProcessManager._currentPIDList
+ OBJC_IVAR_$_CSProcessManager._processNameIdentiferByName
+ OBJC_IVAR_$_CSRestrictionManager._currentActiveScenariosWithRestrictions
+ OBJC_IVAR_$_CSRestrictionManager._debounceTimeBeforeRestrictions
+ OBJC_IVAR_$_CSRestrictionManager._safeguardsDaemon
+ OBJC_IVAR_$_CSScenario._restrictionsByProcess
+ OBJC_IVAR_$_CSScenarioManager._activeScenariosWithRestrictions
+ _CSManagingServiceName
+ _CSRestrictionManagerErrorDomain
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_PLDefaults
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __103-[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:]_block_invoke.146
+ __56-[CSRestrictionManager getCountsForProcess:WithHandler:]_block_invoke.135
+ __63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke.149
+ __63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke.150
+ __63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke.160
+ __74-[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]_block_invoke.cold.1
+ __74-[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]_block_invoke.cold.2
+ __74-[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]_block_invoke.cold.3
+ __74-[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]_block_invoke.cold.4
+ __Block_object_assign
+ __Block_object_dispose
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SafeguardsScheduledWorkReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SafeguardsScheduledWorkReporting
+ __OBJC_$_PROTOCOL_REFS_SafeguardsScheduledWorkReporting
+ __OBJC_LABEL_PROTOCOL_$_SafeguardsScheduledWorkReporting
+ __OBJC_PROTOCOL_$_SafeguardsScheduledWorkReporting
+ __OBJC_PROTOCOL_REFERENCE_$_SafeguardsScheduledWorkReporting
+ ___103-[CSRestrictionManager modifyProcessCounts:withFatalCount:withNonFatalCount:withExitCount:withHandler:]_block_invoke
+ ___37-[CSProcessManager identiferForName:]_block_invoke
+ ___38-[CSProcessManager getPollingInterval]_block_invoke
+ ___42-[CSProcessManager modifyPollingInterval:]_block_invoke
+ ___48-[CSRestrictionManager getScenariosWithHandler:]_block_invoke
+ ___52-[CSRestrictionManager getTargetProcessWithHandler:]_block_invoke
+ ___54-[CSRestrictionManager getActiveScenariosWithHandler:]_block_invoke
+ ___54-[CSRestrictionManager modifyScenarioRefreshInterval:]_block_invoke
+ ___56-[CSRestrictionManager getCountsForProcess:WithHandler:]_block_invoke
+ ___62-[CSRestrictionManager getScenarioRefreshIntervalWithHandler:]_block_invoke
+ ___63-[CSRestrictionManager forceMitigation:forProcess:withHandler:]_block_invoke
+ ___63-[CSRestrictionManager modifyRestrictionsByProcessPerScenario:]_block_invoke
+ ___66-[CSDaemon updateContextForIdentifier:withState:withRestrictions:]_block_invoke
+ ___69-[CSRestrictionManager getProcessesAffectedByScenarioMapWithHandler:]_block_invoke
+ ___74-[CSRestrictionManager getRestrictionsForProcess:forScenario:withHandler:]_block_invoke
+ ___81-[CSRestrictionManager modifyTargetProcess:withPercentage:withSeconds:withLimit:]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___block_descriptor_48_e8_32r40r_e5_v8?0l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_58_e8_32s40s48r_e5_v8?0l
+ ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0l
+ ___copy_helper_block_e8_32r
+ ___copy_helper_block_e8_32r40r
+ ___copy_helper_block_e8_32r40r48r56r
+ ___copy_helper_block_e8_32s40r
+ ___copy_helper_block_e8_32s40s48r
+ ___copy_helper_block_e8_32s40s48s56r
+ ___copy_helper_block_e8_32s40s48s56r64r
+ ___copy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32r40r
+ ___destroy_helper_block_e8_32r40r48r56r
+ ___destroy_helper_block_e8_32s40r
+ ___destroy_helper_block_e8_32s40s48r
+ ___destroy_helper_block_e8_32s40s48s56r
+ ___destroy_helper_block_e8_32s40s48s56r64r
+ ___destroy_helper_block_e8_32s40s48s56s
+ __block_literal_global.52
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
+ _objc_msgSend$allObjects
+ _objc_msgSend$allValues
+ _objc_msgSend$arrayWithObject:
+ _objc_msgSend$clearRestrictionsForProcess:
+ _objc_msgSend$cpuIsFatal
+ _objc_msgSend$cpuTimeWindow
+ _objc_msgSend$cpu_fatal_cnt
+ _objc_msgSend$cpu_nonfatal_cnt
+ _objc_msgSend$date
+ _objc_msgSend$determineAndApplyRestrictionsForProcess:
+ _objc_msgSend$dictionaryWithValuesForKeys:
+ _objc_msgSend$doubleValue
+ _objc_msgSend$exits_cnt
+ _objc_msgSend$fullProcessNameForPid:
+ _objc_msgSend$getPollingInterval
+ _objc_msgSend$getProperties
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$identiferForName:
+ _objc_msgSend$incrementCPUViolationCounter:
+ _objc_msgSend$incrementCPUViolationCounter:fatal:
+ _objc_msgSend$incrementExitCounter
+ _objc_msgSend$initWithThreshold:andTimeWindow:andFatal:
+ _objc_msgSend$intValue
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$issueType
+ _objc_msgSend$leniencyScore
+ _objc_msgSend$longForKey:ifNotSet:
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$mitigationReason
+ _objc_msgSend$mitigationType
+ _objc_msgSend$modifyPollingInterval:
+ _objc_msgSend$needClearRestrictions
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithFloat:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$removeObjectsForKeys:
+ _objc_msgSend$resetNonFatalCPUMonitor
+ _objc_msgSend$restrictionsByProcess
+ _objc_msgSend$restrictionsForScenario:
+ _objc_msgSend$scenarioForIdentifier:
+ _objc_msgSend$setCpuIsFatal:
+ _objc_msgSend$setCpuThreshold:
+ _objc_msgSend$setCpuTimeWindow:
+ _objc_msgSend$setCpuUsageLimitSet:
+ _objc_msgSend$setCpu_fatal_cnt:
+ _objc_msgSend$setCpu_nonfatal_cnt:
+ _objc_msgSend$setExits_cnt:
+ _objc_msgSend$setIssueType:
+ _objc_msgSend$setMitigationReason:
+ _objc_msgSend$setMitigationType:
+ _objc_msgSend$setNeedClearRestrictions:
+ _objc_msgSend$setResetNonFatalCPUMonitor:
+ _objc_msgSend$setRestrictionsByProcess:
+ _objc_msgSend$setThreshold:overTimeWindow:forPID:withFatalEffect:withCPULimit:
+ _objc_msgSend$shouldBeFatalOnViolation
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$updateRestrictionsDataForScenarios:
+ _objc_msgSend$updateState:forIdentifier:withRestrictions:
+ _proc_pidpath
+ _proc_setcpu_percentage
+ _strerror
+ getMainQueue.cold.1
+ isInternalBuild.cold.1
+ processLogger.cold.1
- +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:]
- +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:].cold.1
- +[CSCPUMonitorHelper setThreshold:overTimeWindow:forPID:withFatalEffect:].cold.2
- -[CSCPUTimeRestriction _shouldBeFatalOnViolation]
- -[CSProcess processMonitor]
- -[CSProcess setProcessMonitor:]
- GCC_except_table10
- OBJC_IVAR_$_CSProcess._processMonitor
- __block_literal_global.50
- _objc_msgSend$_shouldBeFatalOnViolation
- _objc_msgSend$bundle
- _objc_msgSend$daemonJobLabel
- _objc_msgSend$setThreshold:overTimeWindow:forPID:withFatalEffect:
CStrings:
+ ""
+ "\f"
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
- "\n"
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
