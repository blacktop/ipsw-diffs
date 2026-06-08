## UnblockService

> `/System/Library/PrivateFrameworks/UnblockService.framework/UnblockService`

```diff

-14.0.0.0.0
-  __TEXT.__text: 0xe2b4
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x404
+17.0.0.0.0
+  __TEXT.__text: 0xd9f4
+  __TEXT.__objc_methlist: 0x41c
   __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__cstring: 0x4b2
-  __TEXT.__oslogstring: 0x1e7a
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0xc7
-  __TEXT.__objc_methname: 0x16b3
-  __TEXT.__objc_methtype: 0x30a
-  __TEXT.__objc_stubs: 0x1800
-  __DATA_CONST.__got: 0x130
+  __TEXT.__gcc_except_tab: 0x178
+  __TEXT.__cstring: 0x4bf
+  __TEXT.__oslogstring: 0x1eae
+  __TEXT.__unwind_info: 0x200
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x180
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x670
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x130
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__cfstring: 0x380
   __AUTH_CONST.__objc_const: 0x940
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x80
   __DATA.__data: 0x60
   __DATA.__common: 0x4
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__common: 0x4
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
-  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
+  - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis
   - /System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C7935EF-D558-3304-AADA-279F53255458
-  Functions: 180
-  Symbols:   816
-  CStrings:  489
+  UUID: 51EE0460-34F8-3BF9-B43C-CF361EE53870
+  Functions: 182
+  Symbols:   821
+  CStrings:  181
 
Symbols:
+ -[UBSystemWatchdogStackshotReport initWithPid:procName:bundleID:exitSnapshot:reason:issueType:]
+ -[UBSystemWatchdogStackshotReport issueType]
+ -[UBSystemWatchdogStackshotReport reportNamePrefix]
+ -[UBUnblockReactiveRecovery selectTaskForServiceNode:serviceContext:]
+ -[UBUnblockReactiveRecovery useStackshotData:]
+ -[UBUnblockReactiveRecovery(Termination) doTermination:options:].cold.1
+ -[UBUnblockReactiveRecovery(Termination) doTerminations:options:]
+ GCC_except_table72
+ _OBJC_CLASS_$_CDSystemWatchdogStackshotReport
+ _OBJC_CLASS_$_UBSystemWatchdogStackshotReport
+ _OBJC_IVAR_$_UBSystemWatchdogStackshotReport._issueType
+ _OBJC_METACLASS_$_CDSystemWatchdogStackshotReport
+ _OBJC_METACLASS_$_UBSystemWatchdogStackshotReport
+ __OBJC_$_INSTANCE_METHODS_UBSystemWatchdogStackshotReport
+ __OBJC_$_INSTANCE_VARIABLES_UBSystemWatchdogStackshotReport
+ __OBJC_$_PROP_LIST_UBSystemWatchdogStackshotReport
+ __OBJC_CLASS_RO_$_UBSystemWatchdogStackshotReport
+ __OBJC_METACLASS_RO_$_UBSystemWatchdogStackshotReport
+ ___106-[UBUnblockReactiveRecovery(ThreadExhaustion) threadExhaustionsAboveLimit:threadIDToThreadExhaustionDict:]_block_invoke.153
+ ___164-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:]_block_invoke.206
+ ___block_literal_global.209
+ ___block_literal_global.292
+ ___block_literal_global.295
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$doTerminations:options:
+ _objc_msgSend$selectTaskForServiceNode:serviceContext:
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- -[UBCrackShotReport initWithPid:procName:bundleID:exitSnapshot:reason:issueType:]
- -[UBCrackShotReport issueType]
- -[UBCrackShotReport reportNamePrefix]
- -[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:].cold.4
- -[UBUnblockReactiveRecovery selectTaskForServiceNode:serviceResult:options:]
- GCC_except_table70
- _OBJC_CLASS_$_OSACrackShotReport
- _OBJC_CLASS_$_UBCrackShotReport
- _OBJC_IVAR_$_UBCrackShotReport._issueType
- _OBJC_METACLASS_$_OSACrackShotReport
- _OBJC_METACLASS_$_UBCrackShotReport
- __OBJC_$_INSTANCE_METHODS_UBCrackShotReport
- __OBJC_$_INSTANCE_VARIABLES_UBCrackShotReport
- __OBJC_$_PROP_LIST_UBCrackShotReport
- __OBJC_CLASS_RO_$_UBCrackShotReport
- __OBJC_METACLASS_RO_$_UBCrackShotReport
- ___106-[UBUnblockReactiveRecovery(ThreadExhaustion) threadExhaustionsAboveLimit:threadIDToThreadExhaustionDict:]_block_invoke.154
- ___164-[UBUnblockReactiveRecovery fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:]_block_invoke.205
- ___block_literal_global.208
- ___block_literal_global.291
- ___block_literal_global.294
- _objc_msgSend$selectTaskForServiceNode:serviceResult:options:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "No dependency node for thread 0x%llx"
+ "Service <%{public}@ [%d] tid[%llx]>: We selected %{public}@ [%d] for termination to recover, but it has already been terminated."
+ "Skipping the actual termination due to UBReactiveRecoveryOptionSkipTermination."
- "%{public}@ [%d] has already been terminated."
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDictionary\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_workloop>\""
- "@\"NSObject<OS_xpc_object>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"SADependencyGraphNode\""
- "@\"SASampleStore\""
- "@\"SATask\""
- "@\"UBStuckServiceRecoveryResult\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "@32@0:8Q16^@24"
- "@32@0:8d16^@24"
- "@36@0:8@16B24@28"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24o^@32"
- "@40@0:8@16d24@32"
- "@40@0:8@16d24Q32"
- "@48@0:8@16d24@32Q40"
- "@48@0:8@16d24@32o^@40"
- "@60@0:8i16@20@28^{exit_reason_snapshot=IQQ}36@44q52"
- "@72@0:8@16@24@32@40@48@56Q64"
- "B16@0:8"
- "B32@0:8@16Q24"
- "Deadlock"
- "NSCopying"
- "No dependency graph node for service!"
- "No dependency node for thread 0x%#llx"
- "Q16@0:8"
- "Skipping the actual termination due to kReactiveRecoverySkipTermination."
- "Stackshot"
- "T@\"NSDictionary\",R,V_threadIDToDeadlockDict"
- "T@\"NSDictionary\",R,V_threadIDToThreadExhaustionDict"
- "T@\"NSMutableDictionary\",R,V_taskIs3PAppDict"
- "T@\"NSMutableSet\",R,V_tasksBlocked"
- "T@\"NSSet\",R,V_deadlocks"
- "T@\"NSSet\",R,V_tasksInvolved"
- "T@\"NSSet\",R,V_threadExhaustions"
- "T@\"NSString\",R,V_clientName"
- "T@\"SADependencyGraphNode\",R,V_node"
- "T@\"SADependencyGraphNode\",R,V_serviceNode"
- "T@\"SATask\",R,V_task"
- "T@\"UBStuckServiceRecoveryResult\",R,V_serviceResult"
- "TQ,R,V_numThreadsInvolved"
- "TQ,R,V_options"
- "TQ,V_numThreadsBlocked"
- "TQ,V_numThreadsInvolved"
- "Td,R,V_timeSpentBlocked"
- "Td,R,V_timeSpentDeadlocked"
- "Termination"
- "ThreadExhaustion"
- "Tq,R,V_issueType"
- "UBCrackShotReport"
- "UBDeadlockInfo"
- "UBServiceContext"
- "UBThreadExhaustionInfo"
- "UBUnblockReactiveRecovery"
- "UBUnblockService"
- "UTF8String"
- "UUIDString"
- "XPCHandling"
- "_clientName"
- "_deadlocks"
- "_dependencyGraph"
- "_init"
- "_issueType"
- "_listenerConnection"
- "_lock"
- "_node"
- "_numThreadsBlocked"
- "_numThreadsInvolved"
- "_options"
- "_recover:error:"
- "_sampleStore"
- "_serviceNode"
- "_serviceResult"
- "_stackshotData"
- "_stuckServices"
- "_task"
- "_taskIs3PAppDict"
- "_tasksBlocked"
- "_tasksInvolved"
- "_threadExhaustions"
- "_threadIDToDeadlockDict"
- "_threadIDToThreadExhaustionDict"
- "_timeSpentBlocked"
- "_timeSpentDeadlocked"
- "_workloop"
- "addCharactersInString:"
- "addKCDataStackshot:"
- "addObject:"
- "addObjectsFromArray:"
- "allKeys"
- "allObjects"
- "allValues"
- "alphanumericCharacterSet"
- "anyObject"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "arrayWithObjects:count:"
- "avoidKillingTask:options:"
- "boolValue"
- "bytes"
- "clearCaches"
- "clientName"
- "code"
- "compare:options:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "containsObject:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countForObject:"
- "d"
- "d16@0:8"
- "dataWithBytes:length:"
- "deadlocks"
- "dealloc"
- "debugDescription"
- "deltaSecondsTo:timeDomainPriorityList:timeDomainUsed:"
- "dependency"
- "dependencyChainForNode:processInfos:options:"
- "dependencyGraphForThreadsInSampleStore:atTimestamp:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dispatchQueue"
- "dispatchQueueLabel"
- "doTermination:options:"
- "dqLabel"
- "effectiveJetsamPriority"
- "emitTelemetryForError:"
- "endTimestamp"
- "enumerateKeysAndObjectsUsingBlock:"
- "errorWithDomain:code:userInfo:"
- "fillInRecoveryInfo:deadlockNodeSelected:exhaustedTaskSelected:suspendedTaskSelected:threadExhaustions:processLevelDependencies:options:"
- "findDeadlocks"
- "formUnionWithCharacterSet:"
- "getDiagnosticsQueue"
- "handleIncomingMessage:"
- "handleReactiveRecoveryRequest:"
- "hasPrefix:"
- "headerDescription"
- "i24@0:8Q16"
- "identifier"
- "incidentUUID"
- "init"
- "initFileURLWithPath:isDirectory:"
- "initForFileParsing"
- "initForStuckServices:clientName:"
- "initWithArray:"
- "initWithArray:copyItems:"
- "initWithCapacity:"
- "initWithFormat:"
- "initWithNode:timeSpentDeadlocked:tasksInvolved:numThreadsInvolved:"
- "initWithObjects:"
- "initWithPid:name:is3P:"
- "initWithPid:procName:bundleID:exitSnapshot:reason:"
- "initWithPid:procName:bundleID:exitSnapshot:reason:issueType:"
- "initWithProcess:thread:"
- "initWithService:clientName:"
- "initWithServiceNode:serviceResult:deadlocks:threadIDToDeadlockDict:threadExhaustions:threadIDToThreadExhaustionDict:options:"
- "initWithTask:timeSpentBlocked:numThreadsInvolved:"
- "initWithTid:threadName:dqid:dqLabel:"
- "initWithUTF8String:"
- "intersectSet:"
- "invertedSet"
- "isAbsolutePath"
- "isBlockedByADeadlock"
- "isEqualToString:"
- "isPartOfADeadlock"
- "isSuspended"
- "isWaiting"
- "isWaitingUninterruptibly"
- "issueType"
- "lastObject"
- "length"
- "lt:"
- "mainBinaryPath"
- "mainThread"
- "minusSet:"
- "mutableCopy"
- "name"
- "node"
- "numThreadsBlocked"
- "numThreadsInvolved"
- "numberWithBool:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "openListenerConnection"
- "options"
- "pid"
- "postprocess"
- "prepareCrashMessage:"
- "prepareDependencyGraph"
- "process"
- "processThreadInfosForDeadlock:processInfos:options:"
- "processesAndThreadsInvolved"
- "q"
- "q16@0:8"
- "q32@0:8@16Q24"
- "reasonToAvoidKillingTask:options:"
- "recover:error:"
- "recoveryConfidence"
- "recoveryStatus"
- "removeAllObjects"
- "removeObjectsInRange:"
- "reportNamePrefix"
- "sampleTimestamps"
- "saveWithOptions:"
- "selectNodeInDeadlocks:longerThan:serviceContext:"
- "selectNodeInDeadlocksBlockingTask:preferredMinimumDuration:serviceContext:processLevelDependencies:"
- "selectTaskBlockingTask:serviceContext:"
- "selectTaskForServiceNode:serviceResult:options:"
- "selectTaskInTasks:serviceContext:"
- "selectTaskInThreadDependencyChainWithServiceContext:"
- "selectTaskInvolvedInAnyIssueWithServiceContext:ignoreMinTimeBlocked:"
- "selectThreadExhaustionBlockingTask:serviceContext:processLevelDependencies:"
- "selectThreadExhaustionInAllThreadExhaustionsWithServiceContext:"
- "selectThreadExhaustionInThreadExhaustions:allowSuspended:serviceContext:"
- "selectedProcess"
- "service"
- "serviceNode"
- "serviceProcessName"
- "serviceResult"
- "set"
- "setDataGatheringOptions:"
- "setIncidentID:"
- "setIssueType:"
- "setNumOtherIssues:"
- "setNumThreadsBlocked:"
- "setNumThreadsBlockedByOtherIssues:"
- "setNumThreadsBlockedByThisIssue:"
- "setNumThreadsInvolved:"
- "setObject:forKeyedSubscript:"
- "setProcessesAndThreadsInvolved:"
- "setProcessesBlockedByOtherIssuesOnly:"
- "setProcessesBlockedByThisAndOtherIssues:"
- "setProcessesBlockedByThisIssueOnly:"
- "setRecoveryConfidence:"
- "setRecoveryStatus:"
- "setSelectedProcess:"
- "setServiceDependencyChain:"
- "setServiceProcessIs3P:"
- "setServiceProcessName:"
- "setThreadID:"
- "setTimeSinceIssueBegan:"
- "setupAndActivate:"
- "sharedInstance"
- "sortedArrayUsingComparator:"
- "startTimestamp"
- "stringWithFormat:"
- "subarrayWithRange:"
- "suppressTelemetry"
- "takeLiveStackshot"
- "task"
- "taskDependency"
- "taskIs3PApp:options:"
- "taskIs3PAppDict"
- "taskStates"
- "tasksBlocked"
- "tasksByPid"
- "tasksInvolved"
- "thread"
- "threadExhaustions"
- "threadExhaustionsAboveLimit:threadIDToThreadExhaustionDict:"
- "threadID"
- "threadIDToDeadlockDict"
- "threadIDToThreadExhaustionDict"
- "threadId"
- "threadName"
- "threadState"
- "threadStates"
- "threads"
- "tid"
- "timeElapsed"
- "timeSpentBlocked"
- "timeSpentDeadlocked"
- "timestampLastRan"
- "timestampOfLastStackshot"
- "unarchivedArrayOfObjectsOfClass:fromData:error:"
- "unionSet:"
- "useStackshotBuffer:size:"
- "useStackshotBuffer:size:frontmostPids:atTime:machTime:sequence:isSnapshotDead:"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v32@0:8@16Q24"
- "v32@0:8r^v16Q24"
- "v40@0:8@16@24Q32"
- "v72@0:8@16@24@32@40@48@56Q64"
- "whitespaceAndNewlineCharacterSet"
- "workQueueHardThreadLimit"
- "workQueueSoftThreadLimit"
- "wqExceededConstrainedThreadLimit"
- "wqExceededTotalThreadLimit"
- "writeDiagnostics:terminatedProcBundleID:options:"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
