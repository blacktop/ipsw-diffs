## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2954.0.0.502.3
-  __TEXT.__text: 0x2c8b0
+2964.0.40.502.1
+  __TEXT.__text: 0x2f104
   __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_methlist: 0x24bc
+  __TEXT.__objc_methlist: 0x271c
   __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0x498
-  __TEXT.__cstring: 0x331f
-  __TEXT.__oslogstring: 0x6468
-  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__gcc_except_tab: 0x500
+  __TEXT.__cstring: 0x334c
+  __TEXT.__oslogstring: 0x6952
+  __TEXT.__unwind_info: 0x850
   __TEXT.__objc_classname: 0x2d9
-  __TEXT.__objc_methname: 0x665c
-  __TEXT.__objc_methtype: 0xdae
-  __TEXT.__objc_stubs: 0x3ac0
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__objc_methname: 0x6da6
+  __TEXT.__objc_methtype: 0xdd6
+  __TEXT.__objc_stubs: 0x3da0
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x628
   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15d8
+  __DATA_CONST.__objc_selrefs: 0x1728
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x898
+  __DATA_CONST.__objc_arraydata: 0xab8
   __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x3280
-  __AUTH_CONST.__objc_const: 0x38b8
-  __AUTH_CONST.__objc_intobj: 0x3ed0
-  __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__objc_doubleobj: 0xf70
+  __AUTH_CONST.__cfstring: 0x32a0
+  __AUTH_CONST.__objc_const: 0x3b00
+  __AUTH_CONST.__objc_intobj: 0x378
+  __AUTH_CONST.__objc_dictobj: 0x410
+  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x2ec
+  __DATA.__objc_ivar: 0x318
   __DATA.__data: 0x318
   __DATA.__common: 0x48
   __DATA.__bss: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: C5F006CA-05EF-32E5-93EB-EC9640219A2C
-  Functions: 1077
-  Symbols:   3377
-  CStrings:  2513
+  UUID: 4C10795F-079A-3616-943E-3E25EAC5D940
+  Functions: 1137
+  Symbols:   3530
+  CStrings:  2596
 
Symbols:
+ -[CSMitigationManager handleCPUDetectionViolation:coalitionID:pid:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:].cold.3
+ -[CSMitigationManager killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:]
+ -[CSMitigationManager killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
+ -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:]
+ -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:].cold.1
+ -[CSMitigationManager penaltyBoxDurationMinsForProcess:]
+ -[CSMitigationManager penaltyBoxDurationMinsForProcess:].cold.1
+ -[CSMitigationManager powerlogDBReader]
+ -[CSMitigationManager setPowerlogDBReader:]
+ -[CSPowerlogDBReader getPowerExceptionsRecordsWithStartDate:andEndDate:]
+ -[CSProcess exemptBitMask]
+ -[CSProcess setExemptBitMask:]
+ -[CSProcessManager applyRecordsForProcess:]
+ -[CSProcessManager clearMitigationRecords]
+ -[CSProcessManager exemptProcessesDict]
+ -[CSProcessManager fillPIDDictionary:]
+ -[CSProcessManager fillPIDDictionary:].cold.1
+ -[CSProcessManager fillPIDDictionary:].cold.2
+ -[CSProcessManager fillPIDDictionary:].cold.3
+ -[CSProcessManager getMaxRelaunchPollingInterval]
+ -[CSProcessManager getPollPIDsCount]
+ -[CSProcessManager getRelaunchPollingInterval]
+ -[CSProcessManager getTargetProcessMitigationRecords]
+ -[CSProcessManager importMitigationRecords]
+ -[CSProcessManager initRelaunchPollingTimer]
+ -[CSProcessManager isXPCServiceExempt:withIssueType:]
+ -[CSProcessManager isXPCServiceExempt:withIssueType:].cold.1
+ -[CSProcessManager modifyMaxRelaunchPollingInterval:]
+ -[CSProcessManager modifyRelaunchPollingInterval:]
+ -[CSProcessManager modifyTargetProcessMitigationRecords:]
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.1
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.2
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.3
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.4
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.5
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.6
+ -[CSProcessManager modifyTargetProcessMitigationRecords:].cold.7
+ -[CSProcessManager pollPIDsCount]
+ -[CSProcessManager pollPenaltyBoxProcessRelaunch]
+ -[CSProcessManager pollPenaltyBoxProcessRelaunch].cold.1
+ -[CSProcessManager powerlogRecordsUUIDs]
+ -[CSProcessManager powerlogRecords]
+ -[CSProcessManager registerForPenaltyBoxRelaunchPolling:]
+ -[CSProcessManager registerForPenaltyBoxRelaunchPolling:].cold.1
+ -[CSProcessManager relaunchPollingIntervalMaxS]
+ -[CSProcessManager relaunchPollingIntervalS]
+ -[CSProcessManager relaunchPollingIntervalStartS]
+ -[CSProcessManager relaunchPollingTimerActive]
+ -[CSProcessManager relaunchPollingTimer]
+ -[CSProcessManager relaunchPollingUUIDs]
+ -[CSProcessManager savedRelaunchPollingIntervalStartS]
+ -[CSProcessManager setExemptProcessesDict:]
+ -[CSProcessManager setPollPIDsCount:]
+ -[CSProcessManager setPowerlogRecords:]
+ -[CSProcessManager setPowerlogRecordsUUIDs:]
+ -[CSProcessManager setRelaunchPollingIntervalMaxS:]
+ -[CSProcessManager setRelaunchPollingIntervalS:]
+ -[CSProcessManager setRelaunchPollingIntervalStartS:]
+ -[CSProcessManager setRelaunchPollingTimer:]
+ -[CSProcessManager setRelaunchPollingTimerActive:]
+ -[CSProcessManager setRelaunchPollingUUIDs:]
+ -[CSProcessManager setSavedRelaunchPollingIntervalStartS:]
+ -[CSProcessManager setTargetProcessRecords:]
+ -[CSProcessManager targetProcessRecords]
+ -[CSProcessManager unregisterAllForPenaltyBoxRelaunchPolling]
+ -[CSProcessManager unregisterForPenaltyBoxRelaunchPolling:]
+ -[CSRestrictionDataProvider _exemptProcessesDictWithErrors:]
+ -[CSRestrictionDataProvider _exemptProcessesDictWithErrors:].cold.1
+ -[CSRestrictionDataProvider _exemptProcessesDictWithErrors:].cold.2
+ -[CSRestrictionDataProvider exemptProcessesDict]
+ -[CSRestrictionManager clearMitigationRecordsWithHandler:]
+ -[CSRestrictionManager getMaxRelaunchPollingIntervalWithHandler:]
+ -[CSRestrictionManager getRelaunchPollingIntervalWithHandler:]
+ -[CSRestrictionManager getTargetProcessMitigationRecordsWithHandler:]
+ -[CSRestrictionManager modifyMaxRelaunchPollingInterval:]
+ -[CSRestrictionManager modifyRelaunchPollingInterval:]
+ -[CSRestrictionManager modifyTargetProcessMitigationRecords:withHandler:]
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table56
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table77
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_IVAR_$_CSMitigationManager._powerlogDBReader
+ _OBJC_IVAR_$_CSProcess._exemptBitMask
+ _OBJC_IVAR_$_CSProcessManager._exemptProcessesDict
+ _OBJC_IVAR_$_CSProcessManager._pollPIDsCount
+ _OBJC_IVAR_$_CSProcessManager._powerlogRecords
+ _OBJC_IVAR_$_CSProcessManager._powerlogRecordsUUIDs
+ _OBJC_IVAR_$_CSProcessManager._relaunchPollingIntervalMaxS
+ _OBJC_IVAR_$_CSProcessManager._relaunchPollingIntervalS
+ _OBJC_IVAR_$_CSProcessManager._relaunchPollingIntervalStartS
+ _OBJC_IVAR_$_CSProcessManager._relaunchPollingTimer
+ _OBJC_IVAR_$_CSProcessManager._relaunchPollingTimerActive
+ _OBJC_IVAR_$_CSProcessManager._relaunchPollingUUIDs
+ _OBJC_IVAR_$_CSProcessManager._savedRelaunchPollingIntervalStartS
+ _OBJC_IVAR_$_CSProcessManager._targetProcessRecords
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.175
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.188
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.189
+ ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.190
+ ___121-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]_block_invoke.318
+ ___44-[CSProcessManager initRelaunchPollingTimer]_block_invoke
+ ___46-[CSProcessManager getRelaunchPollingInterval]_block_invoke
+ ___49-[CSProcessManager getMaxRelaunchPollingInterval]_block_invoke
+ ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.316
+ ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.288
+ ___54-[CSRestrictionManager modifyRelaunchPollingInterval:]_block_invoke
+ ___57-[CSRestrictionManager modifyMaxRelaunchPollingInterval:]_block_invoke
+ ___58-[CSRestrictionManager clearMitigationRecordsWithHandler:]_block_invoke
+ ___69-[CSRestrictionManager getTargetProcessMitigationRecordsWithHandler:]_block_invoke
+ ___73-[CSRestrictionManager modifyTargetProcessMitigationRecords:withHandler:]_block_invoke
+ ___block_descriptor_57_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.166
+ ___block_literal_global.170
+ _objc_msgSend$_exemptProcessesDictWithErrors:
+ _objc_msgSend$applyRecordsForProcess:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$clearMitigationRecords
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$exemptBitMask
+ _objc_msgSend$exemptProcessesDict
+ _objc_msgSend$fillPIDDictionary:
+ _objc_msgSend$getMaxRelaunchPollingInterval
+ _objc_msgSend$getPollPIDsCount
+ _objc_msgSend$getPowerExceptionsRecordsWithStartDate:andEndDate:
+ _objc_msgSend$getRelaunchPollingInterval
+ _objc_msgSend$getTargetProcessMitigationRecords
+ _objc_msgSend$importMitigationRecords
+ _objc_msgSend$initRelaunchPollingTimer
+ _objc_msgSend$isXPCServiceExempt:withIssueType:
+ _objc_msgSend$killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:
+ _objc_msgSend$logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:
+ _objc_msgSend$modifyMaxRelaunchPollingInterval:
+ _objc_msgSend$modifyRelaunchPollingInterval:
+ _objc_msgSend$modifyTargetProcessMitigationRecords:
+ _objc_msgSend$penaltyBoxDurationMinsForProcess:
+ _objc_msgSend$pollPenaltyBoxProcessRelaunch
+ _objc_msgSend$registerForPenaltyBoxRelaunchPolling:
+ _objc_msgSend$setExemptBitMask:
+ _objc_msgSend$startOfDayForDate:
+ _objc_msgSend$unregisterAllForPenaltyBoxRelaunchPolling
+ _objc_msgSend$unregisterForPenaltyBoxRelaunchPolling:
- -[CSMitigationManager handleProcessStart:withMitigationReason:].cold.3
- -[CSMitigationManager killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:]
- -[CSMitigationManager killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:].cold.1
- -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:]
- -[CSMitigationManager logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:].cold.1
- -[CSProcessManager enrolledProcessesSet]
- -[CSProcessManager exemptProcessesSet]
- -[CSProcessManager identiferForPID:]
- -[CSProcessManager incrementCPUViolationCounter:fatal:]
- -[CSProcessManager incrementCPUViolationCounter:fatal:].cold.1
- -[CSProcessManager isXPCServiceExempt:]
- -[CSProcessManager pausePIDPolling]
- -[CSProcessManager pausePIDPolling].cold.1
- -[CSProcessManager processNameIdentiferByPID]
- -[CSProcessManager resumePIDPolling]
- -[CSProcessManager resumePIDPolling].cold.1
- -[CSProcessManager setEnrolledProcessesSet:]
- -[CSProcessManager setExemptProcessesSet:]
- -[CSProcessManager setProcessNameIdentiferByPID:]
- -[CSRestrictionDataProvider _exemptProcessesSetWithErrors:]
- -[CSRestrictionDataProvider _exemptProcessesSetWithErrors:].cold.1
- -[CSRestrictionDataProvider _exemptProcessesSetWithErrors:].cold.2
- -[CSRestrictionDataProvider _exemptProcessesSetWithErrors:].cold.3
- -[CSRestrictionDataProvider exemptProcessesSet]
- GCC_except_table23
- GCC_except_table35
- GCC_except_table36
- GCC_except_table40
- GCC_except_table43
- GCC_except_table50
- GCC_except_table63
- GCC_except_table67
- _OBJC_IVAR_$_CSProcessManager._enrolledProcessesSet
- _OBJC_IVAR_$_CSProcessManager._exemptProcessesSet
- _OBJC_IVAR_$_CSProcessManager._processNameIdentiferByPID
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.166
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.179
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.180
- ___112-[CSMitigationManager forceMitigation:forProcess:withPercentage:withSeconds:withPenaltyBoxDuration:withHandler:]_block_invoke.181
- ___121-[CSRestrictionManager modifyProcessInfoFor:withFatalCount:withNonFatalCount:withExitCount:withPenaltyCount:withHandler:]_block_invoke.307
- ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.7
- ___137-[CSExcessiveCPUViolationHandler handleViolationByProcess:pid:path:endTime:observedValue:observationWindow:limitValue:limitWindow:fatal:]_block_invoke.cold.8
- ___52-[CSRestrictionManager getMonitoredListWithHandler:]_block_invoke.305
- ___54-[CSRestrictionManager getInfoForProcess:withHandler:]_block_invoke.277
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_literal_global.142
- ___block_literal_global.157
- ___kCFBooleanFalse
- ___kCFBooleanTrue
- _objc_msgSend$_exemptProcessesSetWithErrors:
- _objc_msgSend$exemptProcessesSet
- _objc_msgSend$isXPCServiceExempt:
- _objc_msgSend$killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:
- _objc_msgSend$logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:
CStrings:
+ "                             SELECT *                             FROM XPCMetrics_CPUViolations_1_2 where timestamp >= %f AND timestamp <= %f"
+ " getPowerExceptionsRecordsWithStartDate Query %@"
+ "Exempt Processes dictionary missing"
+ "FatalCount is unexpectedly missing or of the wrong class"
+ "MitigationReason is unexpectedly missing or of the wrong class"
+ "MitigationType is unexpectedly missing or of the wrong class"
+ "N"
+ "NonFatalCount is unexpectedly missing or of the wrong class"
+ "SELECT timestamp, Event FROM PLSleepWakeAgent_EventForward_PowerState WHERE timestamp <= %f AND timestamp >= %f ORDER by ID"
+ "T@\"NSArray\",&,V_targetProcessRecords"
+ "T@\"NSDictionary\",&,V_exemptProcesses"
+ "T@\"NSDictionary\",&,V_exemptProcessesDict"
+ "T@\"NSMutableArray\",&,V_powerlogRecords"
+ "T@\"NSMutableArray\",&,V_powerlogRecordsUUIDs"
+ "T@\"NSMutableSet\",&,V_relaunchPollingUUIDs"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_relaunchPollingTimer"
+ "TB,V_relaunchPollingTimerActive"
+ "TC,V_pollPIDsCount"
+ "TI,V_exemptBitMask"
+ "Tf,V_relaunchPollingIntervalMaxS"
+ "Tf,V_relaunchPollingIntervalS"
+ "Tf,V_relaunchPollingIntervalStartS"
+ "Tf,V_savedRelaunchPollingIntervalStartS"
+ "TimeWindowSize is unexpectedly missing or of the wrong class"
+ "_exemptBitMask"
+ "_exemptProcessesDict"
+ "_exemptProcessesDictWithErrors:"
+ "_pollPIDsCount"
+ "_powerlogRecords"
+ "_powerlogRecordsUUIDs"
+ "_relaunchPollingIntervalMaxS"
+ "_relaunchPollingIntervalS"
+ "_relaunchPollingIntervalStartS"
+ "_relaunchPollingTimer"
+ "_relaunchPollingTimerActive"
+ "_relaunchPollingUUIDs"
+ "_savedRelaunchPollingIntervalStartS"
+ "_targetProcessRecords"
+ "applyRecordsForProcess:"
+ "applyRecordsForProcess: for target process %@, use _targetProcessRecords: %@"
+ "applyRecordsForProcess: process: %@ record: %@"
+ "applyRecordsForProcess: skipping unknown mitigationType value: %d"
+ "applyRecordsForProcess: unexpected PEMitigationDefault value"
+ "applyToProcess: Attempted applying thresholds on process:%@ with no current tracked pids"
+ "applyToProcess: Configuring cpuMonitor with cpuThreshold: %@, timeWindow:%@ for process:%@ (%d)"
+ "applyToProcess: Failed %d to apply thresholds on process:%@ (%d)"
+ "applyToProcess: process is nil?"
+ "arrayWithArray:"
+ "clearMitigationRecords"
+ "clearMitigationRecordsWithHandler:"
+ "com.apple.symptomsd.helper"
+ "com.apple.syncdefaultsd"
+ "currentCalendar"
+ "decideMitigation: Unknown issueType %d for exemptBitMask for Process:%@, assuming exempt "
+ "exemptBitMask"
+ "exemptProcesses: %@"
+ "exemptProcessesDict"
+ "exempt_processes dictionary missing"
+ "fillPIDDictionary:"
+ "fillPIDDictionary: Not enough memory"
+ "fillPIDDictionary: getProcessUUID() failed %d, so skipping pid: %d"
+ "fillPIDDictionary: proc_listpids return negative"
+ "fillPIDDictionary: unexpected null value for pidList"
+ "getMaxRelaunchPollingInterval"
+ "getMaxRelaunchPollingIntervalWithHandler:"
+ "getPollPIDsCount"
+ "getPowerExceptionsRecordsWithStartDate:andEndDate:"
+ "getRelaunchPollingInterval"
+ "getRelaunchPollingIntervalWithHandler:"
+ "getTargetProcessMitigationRecords"
+ "getTargetProcessMitigationRecordsWithHandler:"
+ "handleCPUDetectionViolation: fake cpu violation for process %@ (%llu), so ignoring"
+ "handleDetectedIssues: Skip CSMitigationManager to handleDetectorViolation for this issue with reason: %d"
+ "i68@0:8@16Q24Q32C40^C44^C52^@60"
+ "importMitigationRecords"
+ "importMitigationRecords: Updated startDate (was %@) to deviceBootTime %@"
+ "importMitigationRecords: found records"
+ "initRelaunchPollingTimer"
+ "isXPCServiceExempt: Unknown issueType %d for exemptBitMask for coalitionName:%@, assuming exempt "
+ "isXPCServiceExempt:withIssueType:"
+ "killProcess:pid:coalitionID:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:"
+ "logCPUViolationToPowerLog: Sending %s violation fromPowerExceptions (%s) for process %@ (%llu) (%@) to Power Log"
+ "logMitigationToPowerLogForProcess:withPid:withCoalitionID:withIssueType:withMitigationType:withReason:"
+ "modifyMaxRelaunchPollingInterval:"
+ "modifyRelaunchPollingInterval:"
+ "modifyTargetProcessMitigationRecords:"
+ "modifyTargetProcessMitigationRecords:withHandler:"
+ "penaltyBoxDurationMinsForProcess:"
+ "pollPIDsCount"
+ "pollPenaltyBoxProcessRelaunch"
+ "pollPenaltyBoxProcessRelaunch: Start (interval: %f)"
+ "pollPenaltyBoxProcessRelaunch: fillPIDDictionary failed"
+ "pollPenaltyBoxProcessRelaunch: found %@"
+ "pollPids: fillPIDDictionary failed"
+ "pollPids: pid dictionary is larger than INT_MAX"
+ "powerlogRecords"
+ "powerlogRecordsUUIDs"
+ "q24@0:8@16"
+ "record is unexpectedly of the wrong class"
+ "recordTerminationForPID: request polling for relaunch of process:%@"
+ "registerForPenaltyBoxRelaunchPolling:"
+ "registerForPenaltyBoxRelaunchPolling: skip adding uuid (already in the set)"
+ "registerForPenaltyBoxRelaunchPolling: timer now active"
+ "relaunchPollingIntervalMaxS"
+ "relaunchPollingIntervalS"
+ "relaunchPollingIntervalStartS"
+ "relaunchPollingTimer"
+ "relaunchPollingTimerActive"
+ "relaunchPollingUUIDs"
+ "savedRelaunchPollingIntervalStartS"
+ "setExemptBitMask:"
+ "setExemptProcessesDict:"
+ "setPollPIDsCount:"
+ "setPowerlogRecords:"
+ "setPowerlogRecordsUUIDs:"
+ "setRelaunchPollingIntervalMaxS:"
+ "setRelaunchPollingIntervalS:"
+ "setRelaunchPollingIntervalStartS:"
+ "setRelaunchPollingTimer:"
+ "setRelaunchPollingTimerActive:"
+ "setRelaunchPollingUUIDs:"
+ "setSavedRelaunchPollingIntervalStartS:"
+ "setTargetProcessRecords:"
+ "startOfDayForDate:"
+ "targetProcessRecords"
+ "timestampEnd is unexpectedly missing or of the wrong class"
+ "unregisterAllForPenaltyBoxRelaunchPolling"
+ "unregisterAllForPenaltyBoxRelaunchPolling: timer now inactive"
+ "unregisterForPenaltyBoxRelaunchPolling:"
+ "unregisterForPenaltyBoxRelaunchPolling: timer now inactive"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v48@0:8@16i24Q28C36C40C44"
- "%s: CSProcess not found for PID: %d "
- "+"
- "-[CSProcessManager incrementCPUViolationCounter:fatal:]"
- "Attempted applying thresholds on process:%@ with no current tracked pids"
- "Configuring cpuMonitor with cpuThreshold: %@, timeWindow:%@ for process:%@ (%d)"
- "Could not create exempt_processes set from plist"
- "Exempt Processes array missing"
- "Failed %d to apply thresholds on process:%@ (%d)"
- "Incrementing %s violation counters for process %@ (%d)"
- "No"
- "Repeating timer for PID polling disarmed."
- "SELECT timestamp, Event FROM PLSleepWakeAgent_EventForward_PowerState WHERE timestamp <= %f AND timestamp >= %f ORDER by timestamp"
- "Sending %s violation fromPowerExceptions (%s) for process %@ (%llu) to Power Log"
- "T@\"NSMutableDictionary\",&,V_processNameIdentiferByPID"
- "T@\"NSSet\",&,V_enrolledProcessesSet"
- "T@\"NSSet\",&,V_exemptProcesses"
- "T@\"NSSet\",&,V_exemptProcessesSet"
- "_enrolledProcessesSet"
- "_exemptProcessesSet"
- "_exemptProcessesSetWithErrors:"
- "_processNameIdentiferByPID"
- "com.apple.symptomsd-helper"
- "com.apple.syncdefaultsd<"
- "enrolledProcessesSet"
- "exemptProcessesSet"
- "exemptProcessesSet: %@"
- "handleDetectedIssues: Skip CSMitigationManager to handleDetectorViolation for this issue with reasion: %d"
- "handleViolationByProcess: ignore violation for exempt scheduled activity for process %@ (%llu)."
- "handleViolationByProcess: ignore violation in plugged-in state for process %@ (%llu)."
- "i60@0:8@16Q24C32^C36^C44^@52"
- "identiferForPID:"
- "identiferForPID: Skipping processNameIdentifier: %@ because its CSProcess is NULL?"
- "incrementCPUViolationCounter:fatal:"
- "isXPCServiceExempt:"
- "killProcess:pid:issueType:withMitigationDecisionType:withMitigationDecisionReason:withError:"
- "logCPUViolationToPowerLog: Sending %s violation fromPowerExceptions (%s) for process %@ (%llu) to Power Log"
- "logMitigationToPowerLogForProcess:withPid:withIssueType:withMitigationType:withReason:"
- "pausePIDPolling"
- "pollPIDs: Not enough memory"
- "pollPIDs: getProcessUUID() failed %d, so skipping pid: %d"
- "pollPIDs: proc_listpids return negative"
- "process is nil?"
- "processNameIdentiferByPID"
- "resumePIDPolling"
- "setEnrolledProcessesSet:"
- "setExemptProcessesSet:"
- "setProcessNameIdentiferByPID:"
- "v24@0:8i16B20"
- "v40@0:8@16i24C28C32C36"

```
