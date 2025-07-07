## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0xc7390
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x49ec
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x14203
-  __TEXT.__oslogstring: 0xa23a
-  __TEXT.__gcc_except_tab: 0x65e0
+347.0.1.0.0
+  __TEXT.__text: 0xcb34c
+  __TEXT.__auth_stubs: 0x1570
+  __TEXT.__objc_methlist: 0x4d54
+  __TEXT.__const: 0x178
+  __TEXT.__cstring: 0x143f3
+  __TEXT.__oslogstring: 0xa20d
+  __TEXT.__gcc_except_tab: 0x655c
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x1d5c
-  __TEXT.__objc_classname: 0x8c2
-  __TEXT.__objc_methname: 0xae5e
-  __TEXT.__objc_methtype: 0x14d7
-  __TEXT.__objc_stubs: 0x6ac0
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x3038
-  __DATA_CONST.__objc_classlist: 0x330
+  __TEXT.__unwind_info: 0x1dc0
+  __TEXT.__objc_classname: 0x910
+  __TEXT.__objc_methname: 0xbbe6
+  __TEXT.__objc_methtype: 0x1515
+  __TEXT.__objc_stubs: 0x6f40
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x30f8
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xa3c0
-  __DATA_CONST.__objc_selrefs: 0x2220
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0x9980
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__objc_intobj: 0x138
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__auth_got: 0xac0
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x420
-  __DATA.__objc_superrefs: 0x1e8
-  __DATA.__objc_ivar: 0xa24
+  __DATA_CONST.__objc_const: 0xacb8
+  __DATA_CONST.__objc_selrefs: 0x2428
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x448
+  __DATA_CONST.__objc_superrefs: 0x208
+  __DATA_CONST.__objc_arraydata: 0x78
+  __AUTH_CONST.__cfstring: 0xa3a0
+  __AUTH_CONST.__objc_const: 0x120
+  __AUTH_CONST.__const: 0x620
+  __AUTH_CONST.__objc_intobj: 0x150
+  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__auth_got: 0xad0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0xad4
   __DATA.__data: 0x5c4
   __DATA.__thread_vars: 0x48
   __DATA.__crash_info: 0x40
   __DATA.__thread_bss: 0x11
   __DATA.__common: 0x498
   __DATA.__bss: 0x38
-  __DATA_DIRTY.__const: 0x6c0
+  __DATA_DIRTY.__const: 0x3e0
   __DATA_DIRTY.__objc_const: 0x2be8
-  __DATA_DIRTY.__objc_ivar: 0x2c
+  __DATA_DIRTY.__objc_ivar: 0x34
   __DATA_DIRTY.__objc_data: 0x1fe0
-  __DATA_DIRTY.__bss: 0x408
+  __DATA_DIRTY.__bss: 0x410
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EDD82772-4B57-316E-90A5-693159537065
-  Functions: 2381
-  Symbols:   8056
-  CStrings:  6812
+  UUID: E1B312DE-A63D-360A-8CEA-00842FE09EC2
+  Functions: 2468
+  Symbols:   8335
+  CStrings:  7103
 
Symbols:
+ +[SACallTreeState treeCountedStateWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:]
+ +[SACallTreeState writeJSONDictionaryEntriesToStream:state:primaryState:]
+ -[SACallTreeState initWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:]
+ -[SAMountStatusTracker iterateAllTimestamps:]
+ -[SAOnBehalfOfMultiple .cxx_destruct]
+ -[SAOnBehalfOfMultiple addProximateName:proximatePid:originName:originPid:count:]
+ -[SAOnBehalfOfMultiple displayString]
+ -[SAOnBehalfOfMultiple init]
+ -[SAOnBehalfOfSingle .cxx_destruct]
+ -[SAOnBehalfOfSingle copyWithZone:]
+ -[SAOnBehalfOfSingle hash]
+ -[SAOnBehalfOfSingle isEqual:]
+ -[SAOriginProcess .cxx_destruct]
+ -[SAProximateProcess .cxx_destruct]
+ -[SASamplePrintOptions displayCPUClusterInfoForRunningThreads]
+ -[SASamplePrintOptions omitStacksWithECore]
+ -[SASamplePrintOptions omitStacksWithPCore]
+ -[SASamplePrintOptions setDisplayCPUClusterInfoForRunningThreads:]
+ -[SASamplePrintOptions setOmitStacksWithECore:]
+ -[SASamplePrintOptions setOmitStacksWithPCore:]
+ -[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]
+ -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionIDs:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:ioSize:numIOs:isReportHeader:]
+ -[SASamplePrinter displayNameForDispatchQueue:]
+ -[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]
+ -[SASamplePrinter printTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]
+ -[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]
+ -[SASamplePrinter shouldPrintTask:thread:dispatchQueue:]
+ -[SASamplePrinter stackForThread:threadStateIndexes:task:taskSampleCount:isTarget:]
+ -[SASampleStore _getLastWakeTime]
+ -[SASampleStore _parseKCDataSharedCacheContainer:sharedCaches:]
+ -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]
+ -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]
+ -[SASampleStore _populateFromKtraceMachineInfo:is64bit:]
+ -[SASampleStore clusterFlagsForCPUNum:]
+ -[SASampleStore haveCPUClusterInfo]
+ -[SASampleStore isECoreForCPUNum:]
+ -[SASampleStore isPCoreForCPUNum:]
+ -[SASampleStore iterateAllTimestamps:]
+ -[SASampleStore setTargetDispatchQueueId:]
+ -[SASampleStore setTargetProcess:]
+ -[SASampleStore setWrDiagnosticName:]
+ -[SASampleStore setWrError:]
+ -[SASampleStore setWrSignpostCategory:]
+ -[SASampleStore setWrSignpostCount:]
+ -[SASampleStore setWrSignpostCountThreshold:]
+ -[SASampleStore setWrSignpostDurationSingle:]
+ -[SASampleStore setWrSignpostDurationSingleThreshold:]
+ -[SASampleStore setWrSignpostDurationSum:]
+ -[SASampleStore setWrSignpostDurationSumThreshold:]
+ -[SASampleStore setWrSignpostDurationUnion:]
+ -[SASampleStore setWrSignpostDurationUnionThreshold:]
+ -[SASampleStore setWrSignpostName:]
+ -[SASampleStore setWrSignpostSubsystem:]
+ -[SASampleStore setWrTriggeringSignpostCategory:]
+ -[SASampleStore setWrTriggeringSignpostName:]
+ -[SASampleStore setWrTriggeringSignpostSubsystem:]
+ -[SASampleStore setWrWorkflowDuration:]
+ -[SASampleStore setWrWorkflowDurationOmittingNetworkBoundIntervals:]
+ -[SASampleStore setWrWorkflowDurationOmittingNetworkBoundIntervalsThreshold:]
+ -[SASampleStore setWrWorkflowDurationThreshold:]
+ -[SASampleStore setWrWorkflowName:]
+ -[SASampleStore setWrWorkflowTimeoutDuration:]
+ -[SASampleStore targetDispatchQueueId]
+ -[SASampleStore wrDiagnosticName]
+ -[SASampleStore wrError]
+ -[SASampleStore wrSignpostCategory]
+ -[SASampleStore wrSignpostCountThreshold]
+ -[SASampleStore wrSignpostCount]
+ -[SASampleStore wrSignpostDurationSingleThreshold]
+ -[SASampleStore wrSignpostDurationSingle]
+ -[SASampleStore wrSignpostDurationSumThreshold]
+ -[SASampleStore wrSignpostDurationSum]
+ -[SASampleStore wrSignpostDurationUnionThreshold]
+ -[SASampleStore wrSignpostDurationUnion]
+ -[SASampleStore wrSignpostName]
+ -[SASampleStore wrSignpostSubsystem]
+ -[SASampleStore wrTriggeringSignpostCategory]
+ -[SASampleStore wrTriggeringSignpostName]
+ -[SASampleStore wrTriggeringSignpostSubsystem]
+ -[SASampleStore wrWorkflowDurationOmittingNetworkBoundIntervalsThreshold]
+ -[SASampleStore wrWorkflowDurationOmittingNetworkBoundIntervals]
+ -[SASampleStore wrWorkflowDurationThreshold]
+ -[SASampleStore wrWorkflowDuration]
+ -[SASampleStore wrWorkflowName]
+ -[SASampleStore wrWorkflowTimeoutDuration]
+ -[SATask distributorID]
+ -[SATask enumerateThreadStatesForThread:dispatchQueue:betweenStartTime:startSampleIndex:endTime:endSampleIndex:reverseOrder:block:]
+ -[SAThread cpuTimeForThreadStateIndex:inTimestampRangeStart:end:]
+ -[SAThreadState originPid]
+ -[SAThreadState proximatePid]
+ -[SATimestamp deltaMachTo:timeDomainPriorityList:timeDomainUsed:]
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table125
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table170
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table199
+ GCC_except_table211
+ GCC_except_table448
+ GCC_except_table451
+ GCC_except_table454
+ GCC_except_table46
+ GCC_except_table63
+ GCC_except_table80
+ GCC_except_table88
+ GCC_except_table90
+ _.str.446
+ _.str.58
+ _.str.67
+ _.str.676
+ _.str.68
+ _.str.84
+ _CSArchitectureIs64Bit
+ _KCLogItem
+ _KCLogIter
+ _NSDebugDescriptionErrorKey
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_SAOnBehalfOfMultiple
+ _OBJC_CLASS_$_SAOnBehalfOfSingle
+ _OBJC_CLASS_$_SAOriginProcess
+ _OBJC_CLASS_$_SAProximateProcess
+ _OBJC_IVAR_$_SACallTreeState._originPid
+ _OBJC_IVAR_$_SACallTreeState._proximatePid
+ _OBJC_IVAR_$_SAHIDStepSample._threadId
+ _OBJC_IVAR_$_SAMicrostackshotSummary._stateCounts
+ _OBJC_IVAR_$_SAOnBehalfOfMultiple._count
+ _OBJC_IVAR_$_SAOnBehalfOfMultiple._proximateProcesses
+ _OBJC_IVAR_$_SAOnBehalfOfSingle._originName
+ _OBJC_IVAR_$_SAOnBehalfOfSingle._originPid
+ _OBJC_IVAR_$_SAOnBehalfOfSingle._proximateName
+ _OBJC_IVAR_$_SAOnBehalfOfSingle._proximatePid
+ _OBJC_IVAR_$_SAOriginProcess._count
+ _OBJC_IVAR_$_SAOriginProcess._name
+ _OBJC_IVAR_$_SAOriginProcess._pids
+ _OBJC_IVAR_$_SAProximateProcess._count
+ _OBJC_IVAR_$_SAProximateProcess._name
+ _OBJC_IVAR_$_SAProximateProcess._originProcesses
+ _OBJC_IVAR_$_SAProximateProcess._pids
+ _OBJC_IVAR_$_SASamplePrintOptions._displayCPUClusterInfoForRunningThreads
+ _OBJC_IVAR_$_SASamplePrintOptions._omitStacksWithECore
+ _OBJC_IVAR_$_SASamplePrintOptions._omitStacksWithPCore
+ _OBJC_IVAR_$_SASampleStore._clusterFlagsForCPUNumMapping
+ _OBJC_IVAR_$_SASampleStore._targetDispatchQueueId
+ _OBJC_IVAR_$_SASampleStore._wrDiagnosticName
+ _OBJC_IVAR_$_SASampleStore._wrError
+ _OBJC_IVAR_$_SASampleStore._wrSignpostCategory
+ _OBJC_IVAR_$_SASampleStore._wrSignpostCount
+ _OBJC_IVAR_$_SASampleStore._wrSignpostCountThreshold
+ _OBJC_IVAR_$_SASampleStore._wrSignpostDurationSingle
+ _OBJC_IVAR_$_SASampleStore._wrSignpostDurationSingleThreshold
+ _OBJC_IVAR_$_SASampleStore._wrSignpostDurationSum
+ _OBJC_IVAR_$_SASampleStore._wrSignpostDurationSumThreshold
+ _OBJC_IVAR_$_SASampleStore._wrSignpostDurationUnion
+ _OBJC_IVAR_$_SASampleStore._wrSignpostDurationUnionThreshold
+ _OBJC_IVAR_$_SASampleStore._wrSignpostName
+ _OBJC_IVAR_$_SASampleStore._wrSignpostSubsystem
+ _OBJC_IVAR_$_SASampleStore._wrTriggeringSignpostCategory
+ _OBJC_IVAR_$_SASampleStore._wrTriggeringSignpostName
+ _OBJC_IVAR_$_SASampleStore._wrTriggeringSignpostSubsystem
+ _OBJC_IVAR_$_SASampleStore._wrWorkflowDuration
+ _OBJC_IVAR_$_SASampleStore._wrWorkflowDurationOmittingNetworkBoundIntervals
+ _OBJC_IVAR_$_SASampleStore._wrWorkflowDurationOmittingNetworkBoundIntervalsThreshold
+ _OBJC_IVAR_$_SASampleStore._wrWorkflowDurationThreshold
+ _OBJC_IVAR_$_SASampleStore._wrWorkflowName
+ _OBJC_IVAR_$_SASampleStore._wrWorkflowTimeoutDuration
+ _OBJC_IVAR_$_SAStack._isTargetCallTree
+ _OBJC_IVAR_$_SAStack._timeSinceThreadWasMadeRunnable
+ _OBJC_IVAR_$_SATask._distributorID
+ _OBJC_IVAR_$_SAThreadState._originPid
+ _OBJC_IVAR_$_SAThreadState._proximatePid
+ _OBJC_METACLASS_$_SAOnBehalfOfMultiple
+ _OBJC_METACLASS_$_SAOnBehalfOfSingle
+ _OBJC_METACLASS_$_SAOriginProcess
+ _OBJC_METACLASS_$_SAProximateProcess
+ _SkipToContainerEnd
+ __OBJC_$_INSTANCE_METHODS_SAOnBehalfOfMultiple
+ __OBJC_$_INSTANCE_METHODS_SAOnBehalfOfSingle
+ __OBJC_$_INSTANCE_METHODS_SAOriginProcess
+ __OBJC_$_INSTANCE_METHODS_SAProximateProcess
+ __OBJC_$_INSTANCE_VARIABLES_SAOnBehalfOfMultiple
+ __OBJC_$_INSTANCE_VARIABLES_SAOnBehalfOfSingle
+ __OBJC_$_INSTANCE_VARIABLES_SAOriginProcess
+ __OBJC_$_INSTANCE_VARIABLES_SAProximateProcess
+ __OBJC_CLASS_PROTOCOLS_$_SAOnBehalfOfSingle
+ __OBJC_CLASS_RO_$_SAOnBehalfOfMultiple
+ __OBJC_CLASS_RO_$_SAOnBehalfOfSingle
+ __OBJC_CLASS_RO_$_SAOriginProcess
+ __OBJC_CLASS_RO_$_SAProximateProcess
+ __OBJC_METACLASS_RO_$_SAOnBehalfOfMultiple
+ __OBJC_METACLASS_RO_$_SAOnBehalfOfSingle
+ __OBJC_METACLASS_RO_$_SAOriginProcess
+ __OBJC_METACLASS_RO_$_SAProximateProcess
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1199
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1203
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1206
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1200
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1207
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_3
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_4
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_5
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1558
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1560
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.248
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.250
+ ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.251
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1978
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1986
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1991
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2007
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke_2
+ ___131-[SATask enumerateThreadStatesForThread:dispatchQueue:betweenStartTime:startSampleIndex:endTime:endSampleIndex:reverseOrder:block:]_block_invoke
+ ___131-[SATask enumerateThreadStatesForThread:dispatchQueue:betweenStartTime:startSampleIndex:endTime:endSampleIndex:reverseOrder:block:]_block_invoke_2
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1938
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1947
+ ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke
+ ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke.297
+ ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke.307
+ ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke.311
+ ___252-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:]_block_invoke_2
+ ___28-[SASampleStore postprocess]_block_invoke.163
+ ___28-[SASampleStore postprocess]_block_invoke_3.167
+ ___28-[SASampleStore postprocess]_block_invoke_6
+ ___30-[SASamplePrinter printHeader]_block_invoke.1045
+ ___30-[SASamplePrinter printHeader]_block_invoke.1076
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1046
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1089
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.475
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_2
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_3
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_4
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_5
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_6
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_7
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_8
+ ___316-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:]_block_invoke_9
+ ___35-[SAProximateProcess displayString]_block_invoke
+ ___37-[SAOnBehalfOfMultiple displayString]_block_invoke
+ ___37-[SASamplePrinter checkForBadOptions]_block_invoke
+ ___37-[SASamplePrinter checkForBadOptions]_block_invoke.326
+ ___38-[SASamplePrinter printTasksByProcess]_block_invoke.1143
+ ___38-[SASampleStore iterateAllTimestamps:]_block_invoke
+ ___38-[SASampleStore iterateAllTimestamps:]_block_invoke_2
+ ___41-[SASamplePrinter printTasksByExecutable]_block_invoke.1150
+ ___42-[SASampleStore gatherUnknownProcessNames]_block_invoke_3
+ ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.466
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1608
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1609
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1610
+ ___49-[SATimestamp guessMissingTimesBasedOnTimestamp:]_block_invoke.3
+ ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.281
+ ___60-[SAMountStatusTracker(Serialization) iterateAllTimestamps:]_block_invoke
+ ___61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke_6
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.170
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.182
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.203
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.217
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.237
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.247
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.193
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.210
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.221
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.240
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.251
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.234
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.243
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_4.244
+ ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_5.246
+ ___78-[SASampleStore(KPerf) loadInfosForKTSymbolOwners:isKernelSpace:excludeRange:]_block_invoke
+ ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.125
+ ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.129
+ ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_2.130
+ ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_3.133
+ ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.336
+ ___KCLogIter_block_invoke
+ ___ReadAheadTaskLevelInfo_block_invoke.1574
+ ___ReadAheadTaskLevelInfo_block_invoke.1579
+ ___ReadAheadTaskLevelInfo_block_invoke.1582
+ ____LogKCData_block_invoke
+ ___block_descriptor_141_e8_32s40s48s56s64s72s_e51_v20?0I8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}12ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_214_e8_32s40s48s56s64bs72bs80r88r96r104r112r120r128r136r144r152r160r_e15_v28?08I16^B20lr80l8r88l8r96l8r104l8s32l8r112l8s64l8r120l8s40l8r128l8r136l8r144l8r152l8r160l8s48l8s56l8s72l8
+ ___block_descriptor_276_e8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
+ ___block_descriptor_303_e8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8
+ ___block_descriptor_32_e45_q24?0"SAOriginProcess"8"SAOriginProcess"16l
+ ___block_descriptor_32_e51_q24?0"SAProximateProcess"8"SAProximateProcess"16l
+ ___block_descriptor_34_e20_v24?0"SATask"8^B16l
+ ___block_descriptor_34_e35_v32?0"NSNumber"8"SAThread"16^B24l
+ ___block_descriptor_40_e13_v20?0I8r^I12l
+ ___block_descriptor_40_e13_v20?0I8r^Q12l
+ ___block_descriptor_40_e39_v20?0I8r^{stack_snapshot_frame32=II}12l
+ ___block_descriptor_40_e39_v20?0I8r^{stack_snapshot_frame64=QQ}12l
+ ___block_descriptor_40_e8_32bs_e20_v24?0"SATask"8^B16ls32l8
+ ___block_descriptor_40_e8_32bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e21_v16?0"SATimestamp"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_v24?0"SADispatchQueueState"8^B16ls32l8
+ ___block_descriptor_41_e13_v20?0I8r^v12l
+ ___block_descriptor_48_e8_32r40r_e34_v24?0"SADispatchQueueState"8^B16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0i8ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e21_v16?0"SATimestamp"8ls32l8
+ ___block_descriptor_48_e8_32s_e50_v32?0"SAOnBehalfOfSingle"8"NSMutableData"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e30_v32?0"SAThreadState"8Q16^B24ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32r40r48r56r_e20_v24?0"SATask"8^B16lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40r48r56r_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s_e13_v20?0I8r^Q12ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32r40r48r56r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48s_e353_v16?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}Q{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v}8ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_e8_32s40s48s56s64r72r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s_e13_v20?0I8r^Q12ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.1049
+ ___block_literal_global.149
+ ___block_literal_global.1493
+ ___block_literal_global.1532
+ ___block_literal_global.1535
+ ___block_literal_global.1552
+ ___block_literal_global.156
+ ___block_literal_global.1568
+ ___block_literal_global.1600
+ ___block_literal_global.1602
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.191
+ ___block_literal_global.1935
+ ___block_literal_global.1950
+ ___block_literal_global.1971
+ ___block_literal_global.1980
+ ___block_literal_global.199
+ ___block_literal_global.201
+ ___block_literal_global.2038
+ ___block_literal_global.2245
+ ___block_literal_global.225
+ ___block_literal_global.242
+ ___block_literal_global.253
+ ___block_literal_global.292
+ ___block_literal_global.299
+ ___block_literal_global.334
+ ___block_literal_global.339
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.372
+ ___block_literal_global.390
+ ___block_literal_global.394
+ ___block_literal_global.397
+ ___block_literal_global.405
+ ___block_literal_global.409
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.453
+ ___block_literal_global.465
+ ___block_literal_global.517
+ ___block_literal_global.63
+ ___block_literal_global.739
+ ___block_literal_global.87
+ ___block_literal_global.97
+ __block_invoke.knownMachTimebases
+ __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:.next_fake_unique_pid
+ __saos_printf_state_appended_noparens
+ __unnamed_array_storage.1624
+ __unnamed_array_storage.2048
+ __unnamed_array_storage.2054
+ __unnamed_array_storage.2060
+ __unnamed_array_storage.424
+ __unnamed_array_storage.430
+ _ktrace_machine_cluster_flags
+ _ktrace_machine_cpu_cluster
+ _ktrace_machine_create_current
+ _ktrace_machine_destroy
+ _objc_msgSend$deltaSecondsTo:timeDomainPriorityList:timeDomainUsed:
+ _objc_msgSend$displayCPUClusterInfoForRunningThreads
+ _objc_msgSend$distributorID
+ _objc_msgSend$distributorInfo
+ _objc_msgSend$initWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:
+ _objc_msgSend$isComparable:
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$omitStacksWithECore
+ _objc_msgSend$omitStacksWithPCore
+ _objc_msgSend$originPid
+ _objc_msgSend$proximatePid
+ _objc_msgSend$setDisplayCPUClusterInfoForRunningThreads:
+ _objc_msgSend$setOmitStacksWithECore:
+ _objc_msgSend$setOmitStacksWithPCore:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$targetDispatchQueueId
+ _objc_msgSend$userInfo
+ _objc_msgSend$wrDiagnosticName
+ _objc_msgSend$wrError
+ _objc_msgSend$wrSignpostCategory
+ _objc_msgSend$wrSignpostCount
+ _objc_msgSend$wrSignpostCountThreshold
+ _objc_msgSend$wrSignpostDurationSingle
+ _objc_msgSend$wrSignpostDurationSingleThreshold
+ _objc_msgSend$wrSignpostDurationSum
+ _objc_msgSend$wrSignpostDurationSumThreshold
+ _objc_msgSend$wrSignpostDurationUnion
+ _objc_msgSend$wrSignpostDurationUnionThreshold
+ _objc_msgSend$wrSignpostName
+ _objc_msgSend$wrSignpostSubsystem
+ _objc_msgSend$wrTriggeringSignpostCategory
+ _objc_msgSend$wrTriggeringSignpostName
+ _objc_msgSend$wrTriggeringSignpostSubsystem
+ _objc_msgSend$wrWorkflowDuration
+ _objc_msgSend$wrWorkflowDurationOmittingNetworkBoundIntervals
+ _objc_msgSend$wrWorkflowDurationOmittingNetworkBoundIntervalsThreshold
+ _objc_msgSend$wrWorkflowDurationThreshold
+ _objc_msgSend$wrWorkflowName
+ _objc_msgSend$wrWorkflowTimeoutDuration
- +[SACallTreeState treeCountedStateWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:onBehalfOfPid:startSampleIndex:sampleCount:]
- -[SACallTreeState initWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:onBehalfOfPid:startSampleIndex:sampleCount:]
- -[SAMountStatusTracker applyMachTimebase:]
- -[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]
- -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:codesigningID:teamID:resourceCoalitionIDs:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numIdleWorkQueueThreads:numOtherHiddenThreads:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:ioSize:numIOs:isReportHeader:]
- -[SASamplePrinter displayStringForMultipleOnBehalfOf:]
- -[SASamplePrinter printSingleStackForTasks:limitToThreadIds:sampleCount:]
- -[SASamplePrinter printTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]
- -[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]
- -[SASamplePrinter shouldPrintTask:thread:]
- -[SASamplePrinter stackForThread:threadStateIndexes:task:taskSampleCount:]
- -[SASampleStore initWithPAStyleCoder:]
- -[SATimeRange applyMachTimebase:]
- GCC_except_table105
- GCC_except_table111
- GCC_except_table142
- GCC_except_table153
- GCC_except_table159
- GCC_except_table173
- GCC_except_table198
- GCC_except_table210
- GCC_except_table400
- GCC_except_table403
- GCC_except_table404
- GCC_except_table407
- GCC_except_table54
- GCC_except_table65
- GCC_except_table69
- GCC_except_table81
- _.str.445
- _.str.59
- _.str.60
- _.str.670
- _.str.80
- _CSSymbolOwnerCacheGetFlags
- _CSSymbolOwnerCacheSetFlags
- _CSSymbolOwnerCacheSetMemoryLimit
- _OBJC_IVAR_$_SACallTreeState._onBehalfOfPid
- _OBJC_IVAR_$_SACallTreeStateChildren._onBehalfOfPid
- _OBJC_IVAR_$_SAHIDStepSample._thread
- _OBJC_IVAR_$_SAStack._isTargetThread
- _OBJC_IVAR_$_SAThreadState._onBehalfOfPid
- _ReadAheadTaskLevelInfo
- ___112-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke
- ___112-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1748
- ___112-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1756
- ___112-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1761
- ___112-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1777
- ___112-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke_2
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.278
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.286
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.324
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.328
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.332
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.336
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.337
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.341
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.346
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.356
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.361
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.365
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.371
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.375
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.379
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.382
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.383
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.384
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.385
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.386
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.387
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.420
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.326
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.351
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.367
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.399
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.421
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1708
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1717
- ___28-[SASampleStore postprocess]_block_invoke.161
- ___28-[SASampleStore postprocess]_block_invoke_3.168
- ___30-[SASamplePrinter printHeader]_block_invoke.841
- ___30-[SASamplePrinter printHeader]_block_invoke.879
- ___30-[SASamplePrinter printHeader]_block_invoke_2.842
- ___31+[SASharedCache addDSCSymData:]_block_invoke.474
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke.933
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke.940
- ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.465
- ___48-[SATask forwardFillMonotonicallyIncreasingData]_block_invoke_2
- ___48-[SATask forwardFillMonotonicallyIncreasingData]_block_invoke_3
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1374
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1375
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1376
- ___49-[SATimestamp guessMissingTimesBasedOnTimestamp:]_block_invoke_3
- ___50-[SAThread forwardFillMonotonicallyIncreasingData]_block_invoke
- ___50-[SAThread forwardFillMonotonicallyIncreasingData]_block_invoke_2
- ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.278
- ___54-[SASampleStore(SASampleStoreNSCoding) initWithCoder:]_block_invoke_2
- ___57-[SAMountStatusTracker(Serialization) applyMachTimebase:]_block_invoke
- ___73-[SASamplePrinter printSingleStackForTasks:limitToThreadIds:sampleCount:]_block_invoke
- ___73-[SASamplePrinter printSingleStackForTasks:limitToThreadIds:sampleCount:]_block_invoke.1328
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.167
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.179
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.200
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.214
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.234
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.244
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.190
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.207
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.218
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.237
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.248
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.231
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.240
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_4.241
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_5.243
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.127
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.131
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_2.132
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_3.135
- ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.335
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke.973
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke.977
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke.980
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke_2
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke_2.974
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke_2.981
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke_3
- ___95-[SASamplePrinter printTaskHeaderForTask:specialThreadId:omitSpecialThreadId:omitOtherThreads:]_block_invoke_4
- ___ReadAheadTaskLevelInfo_block_invoke.1538
- ___ReadAheadTaskLevelInfo_block_invoke.1542
- ___ReadAheadTaskLevelInfo_block_invoke.1545
- ___block_descriptor_100_e8_32s40s48s56s64s_e13_v20?0I8r^Q12ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_153_e8_32s40s48s56s64s72s_e51_v20?0I8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}12ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_206_e8_32s40s48s56s64bs72bs80r88r96r104r112r120r128r136r144r152r160r_e15_v28?08I16^B20lr80l8r88l8r96l8r104l8s32l8r112l8s64l8r120l8s40l8r128l8r136l8r144l8r152l8r160l8s48l8s56l8s72l8
- ___block_descriptor_275_e8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
- ___block_descriptor_293_e8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8r96l8s48l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8
- ___block_descriptor_40_e40_v32?0"NSNumber"8"SAMountStatus"16^B24l
- ___block_descriptor_44_e13_v20?0I8r^i12l
- ___block_descriptor_44_e38_v20?0I8r^{dyld_uuid_info_32=I[16C]}12l
- ___block_descriptor_44_e38_v20?0I8r^{dyld_uuid_info_64=Q[16C]}12l
- ___block_descriptor_44_e43_v20?0I8r^{user64_dyld_aot_info=QQQ[32C]}12l
- ___block_descriptor_44_e44_v20?0I8r^{jetsam_coalition_snapshot=QQQQ}12l
- ___block_descriptor_48_e49_v20?0I8r^{stackshot_thread_waitinfo_v2=QQQCsI}12l
- ___block_descriptor_48_e51_v20?0I8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}12l
- ___block_descriptor_48_e54_v20?0I8r^{stackshot_thread_turnstileinfo_v2=QQCCQs}12l
- ___block_descriptor_48_e8_32r40r_e20_v24?0"SATask"8^B16lr32l8r40l8
- ___block_descriptor_48_e8_32r_e40_v32?0"NSString"8"NSMutableData"16^B24lr32l8
- ___block_descriptor_48_e8_32s40r_e30_v32?0"SAThreadState"8Q16^B24lr40l8s32l8
- ___block_descriptor_52_e13_v20?0I8r^I12l
- ___block_descriptor_52_e13_v20?0I8r^Q12l
- ___block_descriptor_52_e39_v20?0I8r^{stack_snapshot_frame32=II}12l
- ___block_descriptor_52_e39_v20?0I8r^{stack_snapshot_frame64=QQ}12l
- ___block_descriptor_56_e8_32r40r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8r40l8
- ___block_descriptor_56_e8_32s40r48r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32r40r48r56r_e30_v32?0"SAThreadState"8Q16^B24lr32l8r40l8r48l8r56l8
- ___block_descriptor_65_e8_32s40r48r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r40l8r48l8
- ___block_descriptor_65_e8_32s40r48r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8r48l8
- ___block_descriptor_66_e8_32r40r48r56r_e30_v32?0"SAThreadState"8Q16^B24lr32l8r40l8r48l8r56l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_ea8_32s40s48s_e323_v16?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v}8ls32l8s40l8s48l8
- ___block_descriptor_84_e8_32s40s48s56s_e13_v20?0I8r^Q12ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32r40r48r56r64r72r80r_e28_v32?0"SATaskState"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8
- ___block_descriptor_93_e8_32r40r48r56r64r72r80r_e28_v32?0"SATaskState"8Q16^B24lr32l8r40l8r48l8r56l8r64l8r72l8r80l8
- ___block_literal_global.1265
- ___block_literal_global.1304
- ___block_literal_global.1307
- ___block_literal_global.147
- ___block_literal_global.1525
- ___block_literal_global.1551
- ___block_literal_global.1561
- ___block_literal_global.163
- ___block_literal_global.166
- ___block_literal_global.1705
- ___block_literal_global.171
- ___block_literal_global.1720
- ___block_literal_global.173
- ___block_literal_global.1741
- ___block_literal_global.175
- ___block_literal_global.1750
- ___block_literal_global.1808
- ___block_literal_global.198
- ___block_literal_global.200
- ___block_literal_global.2012
- ___block_literal_global.224
- ___block_literal_global.233
- ___block_literal_global.236
- ___block_literal_global.250
- ___block_literal_global.281
- ___block_literal_global.288
- ___block_literal_global.338
- ___block_literal_global.393
- ___block_literal_global.396
- ___block_literal_global.434
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.452
- ___block_literal_global.457
- ___block_literal_global.459
- ___block_literal_global.462
- ___block_literal_global.464
- ___block_literal_global.472
- ___block_literal_global.490
- ___block_literal_global.505
- ___block_literal_global.508
- ___block_literal_global.59
- ___block_literal_global.738
- ___block_literal_global.83
- ___block_literal_global.93
- __addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:.next_fake_unique_pid
- __unnamed_array_storage.1818
- __unnamed_array_storage.1824
- __unnamed_array_storage.1830
- __unnamed_array_storage.325
- __unnamed_array_storage.331
- _kcdata_iter_array_elem_size
- _kcdata_iter_array_valid
- _objc_msgSend$initWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:onBehalfOfPid:startSampleIndex:sampleCount:
- _objc_msgSend$keysSortedByValueUsingSelector:
- _objc_msgSend$onBehalfOfPid
CStrings:
+ "\x03\x1d\x11\x92A\x81\x11\x1e\x15\x11\xc5\x12\x13V\x82C"
+ "\aU)\x15"
+ "\x13"
+ " (unknown: 0x%x)"
+ " -- skipping"
+ " [%@:%@]"
+ " address 0x%llx"
+ " flags 0x%llx"
+ " name 0x%llx"
+ " to port address 0x%llx"
+ " with unknown flags 0x%llx"
+ " workloop address 0x%llx"
+ "!omitOther || !omitSpecial"
+ "!omitSpecial || !omitOther"
+ "%'llu %s creating thread 0x%llx\n"
+ "%'llu 0x%llx Skipping kperf content: %s\n"
+ "%'llu Created %s-core threadState (index %lu) for thread 0x%llx (sample index %ld-%ld, machabs %llu-%llu) with kernel stack (leaf frame 0x%llx)\n"
+ "%'llu Created off-core threadState (index %lu) for thread 0x%llx (sample index %ld-%ld, machabs %llu-%llu) with kernel stack (leaf frame 0x%llx) due to on-core thread state applying to multiple sample indexes\n"
+ "%'llu Not creating threadState for thread 0x%llx at machabs %llu due to already having a thread state for sample index %lu\n"
+ "%'llu Not creating threadState for thread 0x%llx at machabs %llu due to the thread being created after sample index %lu at machabs %llu\n"
+ "%'llu Parsing kperf for tid 0x%llx with content 0x%llx: %s\n"
+ "%'llu Parsing on-core %d kperf for tid 0x%llx with content 0x%llx: %s\n"
+ "%'llu Task [%d] creating thread 0x%llx in other process %s\n"
+ "%'llu Thread 0x%llx exited, but we don't have a task with that thread!\n"
+ "%'llu WARNING: Continuation for dyld info is empty string on thread 0x%llx: %s\n"
+ "%'llu WARNING: Ignoring record without a stack for thread 0x%llx\n"
+ "%'llu WARNING: Ignoring record without thread info for thread 0x%llx\n"
+ "%'llu WARNING: KPerf had an error getting user stack for task %s thread 0x%llx\n"
+ "%'llu WARNING: Missing first dyld tracepoint on thread 0x%llx\n"
+ "%'llu WARNING: Start for dyld info is empty string on thread 0x%llx: %s\n"
+ "%'llu WARNING: Unable to determine old pid for TRACE_DATA_NEWTHREAD on thread 0x%llx: %d\n"
+ "%'llu WARNING: Unable to determine pid for dyld on thread 0x%llx: %d\n"
+ "%'llu WARNING: Unable to determine pid for dyld string on thread 0x%llx: %d\n"
+ "%'llu WARNING: Unable to determine pid for exec on thread 0x%llx: %d\n"
+ "%'llu WARNING: Unable to determine pid for thread 0x%llx: %d\n"
+ "%'llu WARNING: null UUID in dyld tracepoint on thread 0x%llx\n"
+ "%'llu [%d] creating thread 0x%llx in new process [%d]\n"
+ "%'llu kernel creating thread 0x%llx in process [%d]\n"
+ "%'llu thread 0x%llx dispatch queue %lld backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx dispatch queue %lld backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx ran into non-kperf state at index %lu, stopping\n"
+ "%'llu thread 0x%llx sched info (cpu time %lld (%lld + %lld), state 0x%x, priority %d (%d), qos %d, rqos %d, qqoso %d, qosp %d) backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx sched info (cpu time %lld (%lld + %lld), state 0x%x, priority %d (%d), qos %d, rqos %d, qqoso %d, qosp %d) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s) backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx swift task %lld backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx swift task %lld backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx thread instructions (%llu) cycles (%llu) backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx thread instructions (%llu) cycles (%llu) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx thread name %s backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx thread name %s backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx user stack (leaf frame 0x%llx, swift async leaf 0x%llx) backfilled to %d thread states (indexes %lu-%lu)\n"
+ "%'llu thread 0x%llx user stack (leaf frame 0x%llx, swift async leaf 0x%llx) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
+ "%*s%s: %#18llx %s%s\n"
+ "%*s%s: %#18llx - %#18llx -> %#18llx %s-%s%s\n"
+ "%*s%s: %#18x %s%s\n"
+ "%*s%s: %d%s\n"
+ "%*s%s: %d/%d%s\n"
+ "%*s%s: %lld%s\n"
+ "%*s%s: %llu instructions, %llu cycles%s\n"
+ "%*s%s: %llu%s\n"
+ "%*s%s: %s\n"
+ "%*s%s: %s (0x%x, 0x%x)%s\n"
+ "%*s%s: %s [%d] (transitioning 0x%llx)%s\n"
+ "%*s%s: %s [%d]%s\n"
+ "%*s%s: %s slid base address 0x%llx, slide 0x%llx%s\n"
+ "%*s%s: %s slide 0x%llx%s\n"
+ "%*s%s: %s%s\n"
+ "%*s%s: %s.%03llu%s\n"
+ "%*s%s: %u%s\n"
+ "%*s%s: (invalid array)%s\n"
+ "%*s%s: (invalid container)%s\n"
+ "%*s%s: (invalid string)%s\n"
+ "%*s%s: 0x%llx %s -> 0x%llx %s%s\n"
+ "%*s%s: 0x%llx %s%s\n"
+ "%*s%s: 0x%llx%s\n"
+ "%*s%s: 0x%x%s\n"
+ "%*s%s: [%llu]%s\n"
+ "%*s%s: flags 0x%llx, trust level %u%s\n"
+ "%*s%s: id %d: %s slid base address 0x%llx, slide 0x%llx, flags 0x%x%s\n"
+ "%*s%s: id %llu%s\n"
+ "%*s%s: id %llu, flags 0x%llx, thread_group %llu, leader uniquepid %llu%s\n"
+ "%*s%s: id %llu, type %s%s\n"
+ "%*s%s: id:%d flags:0x%x domain:%d%s\n"
+ "%*s%s: of type %s, count %u size %u%s\n"
+ "%*s%s: thread_delta_v%d 0x%llx%s\n"
+ "%*s%s: thread_v%d 0x%llx dispatch queue %lld%s\n"
+ "%-*s0x%llx\n"
+ "%-*s0x%llx %@\n"
+ "%-*sSignpost count %llu, above threshold %llu\n"
+ "%-*sSignpost interval duration (single) "
+ "%-*sSignpost interval duration (sum) "
+ "%-*sSignpost interval duration (union) "
+ "%-*sWorkflow event duration "
+ "%-*sWorkflow event duration (omitting network bound intervals) "
+ "%-*sWorkflow event timed out after"
+ "%@ %#10x (%@) [%d] thread 0x%llx"
+ "%@ (0x%llx-0x%llx, %lu source infos)"
+ "%@ 0x%llx"
+ "%@ 0x%llx, %@ %@"
+ "%@ <%@> %@ (offset 0x%llx length 0x%llx, %lu symbols)"
+ "%@ <%@> length 0x%llx %@ %@ %@ %@ %@ %@: %lu segments (%s fake segment), (%@ symbol owner)"
+ "%@ DYLD info %@@0x%llx id:0x%llx %@%@ (dyld complete:%d, path complete:%d)"
+ "%@ [%d] (originated by %@ [%d])"
+ "%@ [%d] thread 0x%llx"
+ "%@ [0x%llx]"
+ "%@ [0x%llx] (swift:%d kernel:%d offByOne:%d trunc:%d anotherCallTree:%d"
+ "%@ slid base address 0x%llx"
+ "%@ slid base address 0x%llx, slide 0x%llx"
+ "%@ slide 0x%llx"
+ "%@ thread 0x%llx"
+ "%@ thread 0x%llx starting cpu time %llu < taskCpuTimeNs %llu\nlastThreadState.cpuTimeNs: %llu\nfirstTaskState.terminatedThreadsCpuTimeNs: %llu\nlastTaskState.terminatedThreadsCpuTimeNs: %llu\nfirstThreadState: %@\nlastThreadState: %@\nthread.exitTimestamp: %@\nlastTaskState: %@\ntaskHasTimeInTerminatedThreads: %d\naddEndCPU: %d\nstartTimestamp: %@\nendTimestamp: %@"
+ "%@0x%llx: %@"
+ "%@: adjusted load address of %@ <%@> from 0x%llx to 0x%llx to avoid overlapping with %@ <%@> 0x%llx - 0x%llx"
+ "%@: libktrace translation 0x%llx -> 0x%llx mismatch with existing translation -> 0x%llx"
+ "%@:%d,%d (0x%llx-0x%llx)"
+ "%s has text-exec %u load infos (first is 0x%llx %s)"
+ "%s: already know architecture %s, but guessing from machine architecture %s (data source 0x%llx)"
+ "%s: inlining into %s: %s (0x%llx-0x%llx) with length 0"
+ "%s: numSamples %lu >= specialNumSamples %lu"
+ "%s: specialDispatchQueue %llu doesn't exist"
+ "%s: specialThreadId 0x%llx doesn't exist"
+ "%u sample%s %@ [%@] (%@)"
+ "%u sample%s originated by %@ [%@]"
+ "(!dispatchQueueIds && !threadIds) || tasks.count == 1"
+ "(other dispatch queues/threads)"
+ ", 0x%llx"
+ ", above threshold "
+ ",\"primaryCountedState\":{"
+ "0x%llx"
+ "0x%llx (slide 0x%llx slidBaseAddress 0x%llx) Shared cache <%@> (%lu binaries)"
+ "0x%llx Kernel cache <%@> (%lu binaries)"
+ "7OE"
+ "@\"NSError\""
+ "@92@0:8@16@24Q32I40i44Q48C56@60i68i72Q76Q84"
+ "Already saw thread 0x%llx in this stackshot, ignoring second instance"
+ "B\x12"
+ "B20@0:8I16"
+ "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQii}16Q24@32"
+ "Changing %s slidBaseAddress to 0x%llx"
+ "Changing %s slide to 0x%llx"
+ "Container end with wrong ID (%llu != %llu)"
+ "Didn't find endof skipped container %llu"
+ "Dispatch Queue: "
+ "Error parsing kcdata buffer: array is invalid"
+ "Error parsing kcdata buffer: subcontainer of container type %u is invalid"
+ "Existing mount 0x%llx %s unresponsive for %d seconds, blocking %d threads"
+ "Heaviest stack for dispatch queue %@ thread 0x%llx:\n"
+ "Heaviest stack for dispatch queue %@:\n"
+ "Heaviest stack for thread 0x%llx:\n"
+ "Hit 65324447!\noptions: %{public}@\ntargetTask %d: %{public}@\ntargetThread 0x%llx: %{public}@"
+ "IO Event [thread:0x%llx, type:%@, size 0x%llx tier:%d]\nstart:%@\n  end:%@"
+ "Invalid kcdata: end container at indent 0"
+ "Invalid time domain 0x%llx"
+ "Ktrace load info for 64-bit arm kernel binary segment has no name, assuming TEXT_EXEC segment...\n"
+ "Limiting to specific dispatch queues/threads, but with multiple tasks"
+ "Logging kperf parsing to %s"
+ "Mismatch shared cache %s info: requested slide 0x%llx, slidBaseAddress 0x%llx (base address 0x%llx) vs existing shared cache with slide 0x%llx, slidBaseAddress 0x%llx (base address 0x%llx)"
+ "Mismatch shared cache info: existing slide 0x%llx, slidBaseAddress 0x%llx (base address 0x%llx) vs applied base address 0x%llx for %s"
+ "Mismatch shared cache info: existing slide 0x%llx, slidBaseAddress 0x%llx vs requested slide 0x%llx, slidBaseAddress 0x%llx for %s"
+ "Mismatching shared cache %{uuid_t}.16P slide 0x%llx slideBaseAddress 0x%llx, but task already has %@"
+ "New mount 0x%llx %s unresponsive for %d seconds, blocking %d threads"
+ "No heaviest callstack for %@, dispatch queue %@, thread 0x%llx"
+ "No matching shared cache for defunct 0x%llx 0x%llx %s"
+ "No task with thread 0x%llx at exit for name %@"
+ "No task with thread 0x%llx in event time range, clearing target thread"
+ "No task with thread 0x%llx, clearing target thread"
+ "No thread nor dispatch queue"
+ "No valid originPid:%d or proximatePid:%d, clearing it all out"
+ "Num threads: "
+ "Omitting special and other"
+ "SAKTSYM %@ [%d] Ignoring second shared cache %s slide 0x%llx slideBaseAddress 0x%llx (existing %@)"
+ "SAKTSYM %@ [%d] Shared cache %s with slide 0x%llx has no unslid base address"
+ "SAKTSYM %d segments and %d binaries excluded due to range 0x%llx-0x%llx"
+ "SAKTSYM No UUID for symbol owner at 0x%llx"
+ "SAKTSYM No macho for symbol owner at 0x%llx"
+ "SAKTSYM No name for segment at offset 0x%llx into %@"
+ "SAKTSYM No name for segment at offset 0x%llx into %@, assuming TEXT_EXEC"
+ "SAKTSYM kt says shared cache %@ has unslid base address 0x%llx"
+ "SAKTSYM segment %@ added length 0x%llx"
+ "SAKTSYM segment %@ added offsetIntoBinary 0x%llx"
+ "SAKTSYM segment %@ length mismatch 0x%llx"
+ "SAOnBehalfOfMultiple"
+ "SAOnBehalfOfSingle"
+ "SAOriginProcess"
+ "SAProximateProcess"
+ "SAStackIterator doesn't support backtrace style 0x%llx"
+ "Segment %s load address is 0 (length 0x%llx) for %@"
+ "Setting target process %s which isn't in this SASampleStore"
+ "Shared cache info id %d: %{uuid_t}.16P slid base address 0x%llx, slide 0x%llx, flags 0x%x doesn't match existing %{public}@"
+ "Signpost: "
+ "SymbolOwner %s base address 0x%llx != start address 0x%llx for segment %s"
+ "T@\"NSError\",C,V_wrError"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,V_wrDiagnosticName"
+ "T@\"NSString\",C,V_wrSignpostCategory"
+ "T@\"NSString\",C,V_wrSignpostName"
+ "T@\"NSString\",C,V_wrSignpostSubsystem"
+ "T@\"NSString\",C,V_wrTriggeringSignpostCategory"
+ "T@\"NSString\",C,V_wrTriggeringSignpostName"
+ "T@\"NSString\",C,V_wrTriggeringSignpostSubsystem"
+ "T@\"NSString\",C,V_wrWorkflowName"
+ "T@\"SATask\",&"
+ "TB,V_displayCPUClusterInfoForRunningThreads"
+ "TB,V_omitStacksWithECore"
+ "TB,V_omitStacksWithPCore"
+ "TQ,V_wrSignpostCount"
+ "TQ,V_wrSignpostCountThreshold"
+ "Target dispatch queue %llu never runs on target thread 0x%llx"
+ "Task %@ monotonically increasing data decreased at index %lu of %lu between %@ and %@:\nterminated threads cpu time %llu (%llu + %llu) -> %llu (%llu + %llu)\nterminated threads instructions %llu -> %llu\nterminated threads cycles %llu -> %llufaults %u -> %upageins %u -> %ucow faults %u -> %u"
+ "Td,V_wrSignpostDurationSingle"
+ "Td,V_wrSignpostDurationSingleThreshold"
+ "Td,V_wrSignpostDurationSum"
+ "Td,V_wrSignpostDurationSumThreshold"
+ "Td,V_wrSignpostDurationUnion"
+ "Td,V_wrSignpostDurationUnionThreshold"
+ "Td,V_wrWorkflowDuration"
+ "Td,V_wrWorkflowDurationOmittingNetworkBoundIntervals"
+ "Td,V_wrWorkflowDurationOmittingNetworkBoundIntervalsThreshold"
+ "Td,V_wrWorkflowDurationThreshold"
+ "Td,V_wrWorkflowTimeoutDuration"
+ "Thread 0x%llx"
+ "Thread 0x%llx monotonically increasing data decreased at index %lu of %lu between %@ and %@:\ncpu time %llu (%llu + %llu) -> %llu (%llu + %llu)\ninstructions %llu -> %llu\ncycles %llu -> %llu"
+ "Time domain other than walltime not handled for systemstats format: 0x%llx"
+ "Timed out resampling %s [%d] thread 0x%llx"
+ "Trigger: "
+ "Triggering Diagnostic: "
+ "Triggering Signpost: "
+ "UNKNOWN TASK thread 0x%llx"
+ "UNKNOWN TYPE (0x%x)"
+ "UNKNOWN(0x%x)"
+ "Unable to determine cluster for cpu %u: %{errno}d"
+ "Unable to determine flags for cluster %u: %{errno}d"
+ "Unable to get ktrace machine - cannot determine P vs E cores"
+ "Unexpected end container %llu (expected %llu)"
+ "Unknown dyld tracepoint 0x%x"
+ "Unknown turnstile flags 0x%llx"
+ "Using unknown mach timebase %f"
+ "WARNING: Target dispatch queue %llu not found"
+ "WARNING: Target thread 0x%llx not found"
+ "WARNING: Unable to calculate appropriate load addresses for shared cache %@ when applying %lu load infos with slide #%llx and slidbaseAddress 0x%llx"
+ "Workflow Error: "
+ "Workflow Name: "
+ "Xq"
+ "[ wait_type:0x%x, context:0x%llx, owner:0x%llx ]"
+ "[ wait_type:0x%x, context:0x%llx, owner:0x%llx, port name:%@, flags:0x%llx, domain:%llu]"
+ "[%d] -> [%d] 0x%llx @ %@"
+ "[%d] 0x%llx"
+ "[_tasksByPid[@(targetProcess.pid)] indexOfObjectIdenticalTo:targetProcess] != NSNotFound"
+ "_clusterFlagsForCPUNumMapping"
+ "_cpuNum < UINT8_MAX"
+ "_displayCPUClusterInfoForRunningThreads"
+ "_distributorID"
+ "_isTargetCallTree"
+ "_omitStacksWithECore"
+ "_omitStacksWithPCore"
+ "_originName"
+ "_originPid"
+ "_originProcesses"
+ "_pids"
+ "_proximateName"
+ "_proximatePid"
+ "_proximateProcesses"
+ "_stateCounts"
+ "_targetDispatchQueueId"
+ "_timeSinceThreadWasMadeRunnable"
+ "_wrDiagnosticName"
+ "_wrError"
+ "_wrSignpostCategory"
+ "_wrSignpostCount"
+ "_wrSignpostCountThreshold"
+ "_wrSignpostDurationSingle"
+ "_wrSignpostDurationSingleThreshold"
+ "_wrSignpostDurationSum"
+ "_wrSignpostDurationSumThreshold"
+ "_wrSignpostDurationUnion"
+ "_wrSignpostDurationUnionThreshold"
+ "_wrSignpostName"
+ "_wrSignpostSubsystem"
+ "_wrTriggeringSignpostCategory"
+ "_wrTriggeringSignpostName"
+ "_wrTriggeringSignpostSubsystem"
+ "_wrWorkflowDuration"
+ "_wrWorkflowDurationOmittingNetworkBoundIntervals"
+ "_wrWorkflowDurationOmittingNetworkBoundIntervalsThreshold"
+ "_wrWorkflowDurationThreshold"
+ "_wrWorkflowName"
+ "_wrWorkflowTimeoutDuration"
+ "aot shared cache load info"
+ "async_stack"
+ "backtrace style specified both swift async only and prefer/only C root frames: 0x%llx"
+ "bad container type %u"
+ "bad cpu num %u"
+ "bad tid 0x%llx"
+ "bitNum %d unset, but contents 0x%llx"
+ "bufferLength %lu < serialized SATask struct v8 with %u root frames, %u image infos, %u task states, %u threads, %u dispatch queues, %u swift tasks"
+ "bufferLength %lu < serialized SAThreadState v7 struct %lu"
+ "bufferLength >= sizeof(*serializedThreadState_v7)"
+ "bufferLength >= sizeofV8"
+ "cannot display timeline format with concurrent target dispatch queue %@ in %@"
+ "codesigning info"
+ "containerType == STACKSHOT_KCCONTAINER_SHAREDCACHE"
+ "containerType == STACKSHOT_KCCONTAINER_TASK || containerType == STACKSHOT_KCCONTAINER_TRANSITIONING_TASK"
+ "containerType == STACKSHOT_KCCONTAINER_THREAD"
+ "d40@0:8@16@24^Q32"
+ "data source 0x%llx"
+ "deltaMachTo:timeDomainPriorityList:timeDomainUsed:"
+ "deltaSecondsTo:timeDomainPriorityList:timeDomainUsed:"
+ "displayCPUClusterInfoForRunningThreads"
+ "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\naggregateProcessesByExecutable: %d\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
+ "distributorID"
+ "distributorInfo"
+ "e-core"
+ "eCore"
+ "endingDepth %u, numUserFrames %u, backtraceStyle 0x%llx, stitchIndex %u"
+ "existing source info %@ overlaps new %@:%d,%d (0x%llx-0x%llx)"
+ "haveCPUClusterInfo"
+ "hid step sample %@ thread 0x%llx, %lu-%lu, %@-%@"
+ "initWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:"
+ "invalid skipped container"
+ "invalid sort option 0x%llx"
+ "isComparable:"
+ "isECoreForCPUNum:"
+ "isPCoreForCPUNum:"
+ "isset(&unknownContents, bitNum)"
+ "kcdata_iter_container_valid(*kcdataiter)"
+ "keysSortedByValueUsingComparator:"
+ "load info %s length 0x%llx has a hit at 0x%llx"
+ "mach timebase"
+ "new source info %@:%d,%d (0x%llx-0x%llx) overlaps existing %@"
+ "no target dispatch queue nor thread id, target task %s, but no main thread"
+ "not e-core"
+ "not p-core"
+ "not runnable"
+ "not running"
+ "numSamples >= specialNumSamples"
+ "numThreads"
+ "omitStacksWithECore"
+ "omitStacksWithPCore"
+ "on cpu %u"
+ "on cpu UNKNOWN"
+ "originPid"
+ "p-core"
+ "pCore"
+ "port label flags 0x%llx is too large"
+ "proximatePid"
+ "q24@?0@\"SAOriginProcess\"8@\"SAOriginProcess\"16"
+ "q24@?0@\"SAProximateProcess\"8@\"SAProximateProcess\"16"
+ "q40@0:8@16@24^Q32"
+ "runnable before first sample for "
+ "setDisplayCPUClusterInfoForRunningThreads:"
+ "setOmitStacksWithECore:"
+ "setOmitStacksWithPCore:"
+ "setTargetDispatchQueueId:"
+ "setTargetProcess:"
+ "setWrDiagnosticName:"
+ "setWrError:"
+ "setWrSignpostCategory:"
+ "setWrSignpostCount:"
+ "setWrSignpostCountThreshold:"
+ "setWrSignpostDurationSingle:"
+ "setWrSignpostDurationSingleThreshold:"
+ "setWrSignpostDurationSum:"
+ "setWrSignpostDurationSumThreshold:"
+ "setWrSignpostDurationUnion:"
+ "setWrSignpostDurationUnionThreshold:"
+ "setWrSignpostName:"
+ "setWrSignpostSubsystem:"
+ "setWrTriggeringSignpostCategory:"
+ "setWrTriggeringSignpostName:"
+ "setWrTriggeringSignpostSubsystem:"
+ "setWrWorkflowDuration:"
+ "setWrWorkflowDurationOmittingNetworkBoundIntervals:"
+ "setWrWorkflowDurationOmittingNetworkBoundIntervalsThreshold:"
+ "setWrWorkflowDurationThreshold:"
+ "setWrWorkflowName:"
+ "setWrWorkflowTimeoutDuration:"
+ "sortUsingSelector:"
+ "specialDispatchQueue"
+ "specific_thread_name"
+ "stack with %d kernel frames (leaf 0x%llx), %d user (leaf 0x%llx), %d swift async (leaf 0x%llx), backtracer %llu"
+ "state 0x%x"
+ "system_memory"
+ "system_memory_status"
+ "target dispatch queue %llu, thread id 0x%llx, target task %s: no target dispatch queue nor thread"
+ "targetDispatchQueue || targetThread"
+ "targetDispatchQueueId"
+ "targetDispatchQueueLabel"
+ "targeting dispatch queue %llu in %@ but no such dispatch queue found"
+ "targeting dispatch queue %llu, but no target task"
+ "targeting thread 0x%llx in %@ but no such thread found"
+ "targeting thread 0x%llx, but no target task"
+ "thread_dispatch_label"
+ "thread_inscyc"
+ "tinfo_sched_v2"
+ "tree state %lu-%lu (%lu) [%d] thread 0x%llx priority:%d state:0x%llx microState:0x%x waitInfo:%@ turnstileInfo:%@ io:%@ timeRanges:%@ originPid:%d proximatePid:%d"
+ "turnstile blocked on 0x%llx at priority %d, %d hops, 0x%llx flags"
+ "turnstile blocked on 0x%llx at priority %d, %d hops, 0x%llx flags, port name:%@, flags:0x%llx, domain:%llu"
+ "unknown (0x%x)"
+ "unsuspended"
+ "userInfo"
+ "v16@?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}Q{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v}8"
+ "v20@?0I8r^v12"
+ "v32@?0@\"SAOnBehalfOfSingle\"8@\"NSMutableData\"16^B24"
+ "v40@?0@\"SAThread\"8@\"SAThreadState\"16Q24^B32"
+ "wrDiagnosticName"
+ "wrError"
+ "wrSignpostCategory"
+ "wrSignpostCount"
+ "wrSignpostCountThreshold"
+ "wrSignpostDurationSingle"
+ "wrSignpostDurationSingleThreshold"
+ "wrSignpostDurationSum"
+ "wrSignpostDurationSumThreshold"
+ "wrSignpostDurationUnion"
+ "wrSignpostDurationUnionThreshold"
+ "wrSignpostName"
+ "wrSignpostSubsystem"
+ "wrTriggeringSignpostCategory"
+ "wrTriggeringSignpostName"
+ "wrTriggeringSignpostSubsystem"
+ "wrWorkflowDuration"
+ "wrWorkflowDurationOmittingNetworkBoundIntervals"
+ "wrWorkflowDurationOmittingNetworkBoundIntervalsThreshold"
+ "wrWorkflowDurationThreshold"
+ "wrWorkflowName"
+ "wrWorkflowTimeoutDuration"
+ "\xd2"
- "\x03\x1d\x92A\x81\x11\x1e\x15\x12\xc5\x12\x12B"
- "\x04"
- "\aU(\x15"
- " (unknown: %#x)"
- " address %#llx"
- " flags %#llx"
- " name %#llx"
- " to port address %#llx"
- " with unknown flags %#llx"
- " workloop address %#llx"
- "!!_heaviestTask == !!_heaviestThread"
- "!omitSpecialThreadId || !omitOtherThreads"
- "%#llx"
- "%#llx (slide %#llx slidBaseAddress %#llx) Shared cache <%@> (%lu binaries)"
- "%#llx Kernel cache <%@> (%lu binaries)"
- "%'llu %lld Skipping kperf content: %s\n"
- "%'llu %s creating thread %#llx\n"
- "%'llu Created %s-core threadState (index %lu) for thread %#llx (sample index %ld-%ld, machabs %llu-%llu) with kernel stack (leaf frame %#llx)\n"
- "%'llu Created off-core threadState (index %lu) for thread %#llx (sample index %ld-%ld, machabs %llu-%llu) with kernel stack (leaf frame %#llx) due to on-core thread state applying to multiple sample indexes\n"
- "%'llu Not creating threadState for thread %#llx at machabs %llu due to already having a thread state for sample index %lu\n"
- "%'llu Not creating threadState for thread %#llx at machabs %llu due to the thread being created after sample index %lu at machabs %llu\n"
- "%'llu Parsing kperf for tid %#llx with content %#llx: %s\n"
- "%'llu Parsing on-core %d kperf for tid %#llx with content %#llx: %s\n"
- "%'llu Task [%d] creating thread %#llx in other process %s\n"
- "%'llu Thread %#llx exited, but we don't have a task with that thread!\n"
- "%'llu WARNING: Continuation for dyld info is empty string on thread %#llx: %s\n"
- "%'llu WARNING: Ignoring record without a stack for thread %#llx\n"
- "%'llu WARNING: Ignoring record without thread info for thread %#llx\n"
- "%'llu WARNING: KPerf had an error getting user stack for task %s thread %#llx\n"
- "%'llu WARNING: Missing first dyld tracepoint on thread %#llx\n"
- "%'llu WARNING: Start for dyld info is empty string on thread %#llx: %s\n"
- "%'llu WARNING: Unable to determine old pid for TRACE_DATA_NEWTHREAD on thread %#llx: %d\n"
- "%'llu WARNING: Unable to determine pid for dyld on thread %#llx: %d\n"
- "%'llu WARNING: Unable to determine pid for dyld string on thread %#llx: %d\n"
- "%'llu WARNING: Unable to determine pid for exec on thread %#llx: %d\n"
- "%'llu WARNING: Unable to determine pid for thread %#llx: %d\n"
- "%'llu WARNING: null UUID in dyld tracepoint on thread %#llx\n"
- "%'llu [%d] creating thread %#llx in new process [%d]\n"
- "%'llu kernel creating thread %#llx in process [%d]\n"
- "%'llu thread %#llx dispatch queue %lld backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx dispatch queue %lld backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx ran into non-kperf state at index %lu, stopping\n"
- "%'llu thread %#llx sched info (cpu time %lld (%lld + %lld), state %#x, priority %d (%d), qos %d, rqos %d, qqoso %d, qosp %d) backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx sched info (cpu time %lld (%lld + %lld), state %#x, priority %d (%d), qos %d, rqos %d, qqoso %d, qosp %d) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s) backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx snapshot info (io tier %d, passive %d, suspended %d, darwinbg %d, idlewq %d, gfi %d, runnable %s) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx swift task %lld backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx swift task %lld backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx thread instructions (%llu) cycles (%llu) backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx thread instructions (%llu) cycles (%llu) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx thread name %s backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx thread name %s backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx user stack (leaf frame %#llx, swift async leaf %#llx) backfilled to %d thread states (indexes %lu-%lu)\n"
- "%'llu thread %#llx user stack (leaf frame %#llx, swift async leaf %#llx) backfilled to all (%d) thread states (indexes %lu-%lu)\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): \n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx):  -- skipping\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#18llx %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#18llx - %#18llx -> %#18llx %s-%s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#18x %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#llx\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#llx %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#llx %s -> %#llx %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %#x\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %d\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %lld\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %llu\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %llu instructions, %llu cycles\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %s (%#x, %#x)\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %s [%d]\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %s [%d] (transitioning %#llx)\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %s slid base address %#llx, slide %#llx\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %s.%03llu\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): %u\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): Timebase %d/%d\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): UNSTRUCTURED DATA %d\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): UNSTRUCTURED DATA %lld\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): UNSTRUCTURED DATA %llu\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): UNSTRUCTURED DATA %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): UNSTRUCTURED DATA %u\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): UNSTRUCTURED DATA binary data\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): [%llu]\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): data: %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): id %d: %s slid base address %#llx, slide %#llx, flags %#x\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): id %llu\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): id %llu - done with unknown container\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): id %llu, flags %#llx, thread_group %llu, leader uniquepid %llu\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): id %llu, type %s\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): id:%d flags:%#x domain:%d\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): of type %s, count %u size %u\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): thread_delta_v2 %#llx\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): thread_delta_v3 %#llx\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): thread_v2 %#llx dispatch queue %lld\n"
- "%*s%s (%d bytes (%zu including kcdata structure), flags %#llx): thread_v4 %#llx dispatch queue %lld\n"
- "%*s%s (%zu bytes): %#18llx\n"
- "%*s%s (%zu bytes): %#18llx %#18llx\n"
- "%*s%s (%zu bytes): %#18llx %s\n"
- "%*s%s (%zu bytes): %#18llx - %#18llx -> %#18llx %s-%s\n"
- "%*s%s (%zu bytes): %#18x\n"
- "%*s%s (%zu bytes): %#18x %#18x\n"
- "%*s%s (%zu bytes): %#18x %s\n"
- "%*s%s (%zu bytes): %#llx\n"
- "%*s%s (%zu bytes): [%d]\n"
- "%*s%s (%zu bytes): [%llu]\n"
- "%*s%s (%zu bytes): id %llu, flags %#llx, thread_group %llu, leader uniquepid %llu\n"
- "%*s%s (%zu bytes): thread_delta_v2 %#llx\n"
- "%*s%s (%zu bytes): thread_delta_v3 %#llx\n"
- "%*s%s (%zu bytes): turnstile info thread %#llx, context %#llx, priority %d, numHops %d, flags %#llx\n"
- "%*s%s (%zu bytes): turnstile info thread %#llx, context %#llx, priority %d, numHops %d, flags %#llx, port label id %d\n"
- "%*s%s (%zu bytes): wait info thread %#llx, owner %#llx, context %#llx, wait_type %#x\n"
- "%*s%s (%zu bytes): wait info thread %#llx, owner %#llx, context %#llx, wait_type %#x, port label id %d, flags %#x\n"
- "%-*s%#llx\n"
- "%-*s%#llx %@\n"
- "%016llx "
- "%02x "
- "%@ \"%@\"(%llu)"
- "%@ %#10x (%@) [%d] thread %#llx"
- "%@ %#llx"
- "%@ (%#llx-%#llx, %lu source infos)"
- "%@ <%@> %@ (offset %#llx length %#llx, %lu symbols)"
- "%@ <%@> length %#llx %@ %@ %@ %@ %@ %@: %lu segments (%s fake segment), (%@ symbol owner)"
- "%@ DYLD info %@@%#llx id:%#llx %@%@ (dyld complete:%d, path complete:%d)"
- "%@ [%#llx]"
- "%@ [%#llx] (swift:%d kernel:%d offByOne:%d trunc:%d anotherCallTree:%d"
- "%@ [%d] thread %#llx"
- "%@ slid base address %#llx"
- "%@ slid base address %#llx, slide %#llx"
- "%@ slide %#llx"
- "%@ thread %#llx"
- "%@ thread %#llx starting cpu time %llu < taskCpuTimeNs %llu\nlastThreadState.cpuTimeNs: %llu\nfirstTaskState.terminatedThreadsCpuTimeNs: %llu\nlastTaskState.terminatedThreadsCpuTimeNs: %llu\nfirstThreadState: %@\nlastThreadState: %@\nthread.exitTimestamp: %@\nlastTaskState: %@\ntaskHasTimeInTerminatedThreads: %d\naddEndCPU: %d\nstartTimestamp: %@\nendTimestamp: %@"
- "%@%#llx: %@"
- "%@: adjusted load address of %@ <%@> from %#llx to %#llx to avoid overlapping with %@ <%@> %#llx - %#llx"
- "%@: libktrace translation %#llx -> %#llx mismatch with existing translation -> %#llx"
- "%@:%d,%d (%#llx-%#llx)"
- "%llu sample%s %@"
- "%s has text-exec %u load infos (first is %#llx %s)"
- "%s: already know architecture %s, but guessing from machine architecture %s (data source %#llx)"
- "%s: inlining into %s: %s (%#llx-%#llx) with length 0"
- "%s: numSamples %lu >= specialThreadNumSamples %lu"
- "%s: specialThreadId %#llx doesn't exist"
- "(dyldInfo.path || dyldInfo.stringID == 0 || dyldInfo.stringID == UINT64_MAX) && dyldInfo.uuid && dyldInfo.loadAddress"
- ", %#llx"
- "-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]"
- "2\x12"
- "7OD"
- "@88@0:8@16@24Q32I40i44Q48C56@60i68Q72Q80"
- "Already have a shared cache for %u: %@"
- "Already saw thread %#llx in this stackshot, ignoring second instance"
- "Aot info array not within a task"
- "Aot info not in an array: %#18llx - %#18llx -> %#18llx %s-%s"
- "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQi}16Q24@32"
- "Changing %s slidBaseAddress to %#llx"
- "Changing %s slide to %#llx"
- "Dispatch Queue label %s not in thread container"
- "Donating pids not within a task"
- "Existing mount %#llx %s unresponsive for %d seconds, blocking %d threads"
- "Heaviest stack for thread %#llx:\n"
- "Heaviest task %s, heaviest thread %s"
- "Hit 65324447!\noptions: %{public}@\ntargetTask %d: %{public}@\ntargetThread %#llx: %{public}@"
- "Hq"
- "IO Event [thread:%#llx, type:%@, size %#llx tier:%d]\nstart:%@\n  end:%@"
- "Invalid time domain %#llx"
- "Jetsam coalition snapshot %llu not within an array"
- "Kernel stack LR 32-bit not within a thread"
- "Kernel stack LR 64-bit not within a thread"
- "Kernel stack frame 32-bit not within a thread"
- "Kernel stack frame 64-bit not within a thread"
- "Load info 32-bit array not within a task"
- "Load info 32-bit not in an array: %#18x %s "
- "Load info 64-bit array not within a task"
- "Load info 64-bit not in an array: %#18llx %s "
- "Machine hasn't slept"
- "Mismatch shared cache %s info: requested slide %#llx, slidBaseAddress %#llx (base address %#llx) vs existing shared cache with slide %#llx, slidBaseAddress %#llx (base address %#llx)"
- "Mismatch shared cache info: existing slide %#llx, slidBaseAddress %#llx (base address %#llx) vs applied base address %#llx for %s"
- "Mismatch shared cache info: existing slide %#llx, slidBaseAddress %#llx vs requested slide %#llx, slidBaseAddress %#llx for %s"
- "Mismatching shared cache %{uuid_t}.16P slide %#llx slideBaseAddress %#llx, but task already has %@"
- "New mount %#llx %s unresponsive for %d seconds, blocking %d threads"
- "No matching shared cache for defunct %#llx %#llx %s"
- "No task container end"
- "No task with thread %#llx at exit for name %@"
- "No task with thread %#llx in event time range, clearing target thread"
- "No task with thread %#llx, clearing target thread"
- "No valid onBehalfOfPid data, clearing it all out"
- "Nonrunnable thread %#llx not within an array"
- "Nonrunnable threads not within a task"
- "Port label container %llu inside port label container %llu, treating as an unknown container"
- "SAKTSYM %@ [%d] Ignoring second shared cache %s slide %#llx slideBaseAddress %#llx (existing %@)"
- "SAKTSYM %@ [%d] Shared cache %s with slide %#llx has no unslid base address"
- "SAKTSYM %d segments and %d binaries excluded due to range %#llx-%#llx"
- "SAKTSYM No UUID for symbol owner at %#llx"
- "SAKTSYM No macho for symbol owner at %#llx"
- "SAKTSYM No name for segment at offset %#llx into %@"
- "SAKTSYM kt says shared cache %@ has unslid base address %#llx"
- "SAKTSYM segment %@ added length %#llx"
- "SAKTSYM segment %@ added offsetIntoBinary %#llx"
- "SAKTSYM segment %@ length mismatch %#llx"
- "SASampleStore.m"
- "SAStackIterator doesn't support backtrace style %#llx"
- "Segment %s load address is 0 (length %#llx) for %@"
- "Shared cache container %llu inside task container %llu, treating as an unknown container"
- "SymbolOwner %s base address %#llx != start address %#llx for segment %s"
- "T@\"SATask\",R,V_targetProcess"
- "Task container %llu inside task container %llu, treating as an unknown container"
- "Text exec load info array not within a task"
- "Text exec load info not in an array: %#18llx %s "
- "Thread %#llx"
- "Thread container %llu inside thread container %llu, treating as an unknown container"
- "Thread container %llu outside a task container, treating as an unknown container"
- "Thread delta array not within a task"
- "Thread name %s not in thread container"
- "Time domain other than walltime not handled for systemstats format: %#llx"
- "Timed out resampling %s [%d] thread %#llx"
- "UNKNOWN TASK thread %#llx"
- "UNKNOWN TYPE (%#x)"
- "UNKNOWN(%#x)"
- "Unknown container id %lld"
- "Unknown container type %#x, ignoring everything in this container"
- "Unknown dyld tracepoint %#x"
- "Unknown turnstile flags %#llx"
- "User async stack LR 64-bit not within a thread"
- "User async stack start index not within a thread"
- "User stack LR 32-bit not within a thread"
- "User stack LR 64-bit not within a thread"
- "User stack frame 32-bit not within a thread"
- "User stack frame 64-bit not within a thread"
- "WARNING: Donating pid not in an array"
- "WARNING: Target thread %#llx not found"
- "WARNING: Unable to calculate appropriate load addresses for shared cache %@ when applying %lu load infos with slide #%llx and slidbaseAddress %#llx"
- "Wait info for task's threads not within task"
- "[ wait_type:%#x, context:%#llx, owner:%#llx ]"
- "[ wait_type:%#x, context:%#llx, owner:%#llx, port name:%@, flags:%#llx, domain:%llu]"
- "[%d] %#llx"
- "[%d] -> [%d] %#llx @ %@"
- "_isTargetThread"
- "_onBehalfOfPid"
- "backtrace style specified both swift async only and prefer/only C root frames: %#llx"
- "bad tid %#llx"
- "bufend < buf + mallocsize"
- "data source %#llx"
- "didn't clean up turnstileInfos"
- "didn't clean up waitInfos"
- "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: %#llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ncallTreeTimestampsTimeDomain: %#llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\naggregateProcessesByExecutable: %d\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
- "endingDepth %u, numUserFrames %u, backtraceStyle %#llx, stitchIndex %u"
- "existing source info %@ overlaps new %@:%d,%d (%#llx-%#llx)"
- "guessing missing timestamps:\n%{public}@ ->\n%{public}@ based on\n%{public}@"
- "hid step sample %@ %@, %lu-%lu, %@-%@"
- "initWithWaitInfo:turnstileInfo:state:microstackshotState:pid:threadId:threadPriority:timeRange:onBehalfOfPid:startSampleIndex:sampleCount:"
- "invalid sort option %#llx"
- "kern stack frame %#llx not in an array"
- "kern stack frame %#x not in an array"
- "kern stack lr %#llx not in an array"
- "kern stack lr %#x not in an array"
- "keysSortedByValueUsingSelector:"
- "load info %s length %#llx has a hit at %#llx"
- "new source info %@:%d,%d (%#llx-%#llx) overlaps existing %@"
- "numSamples >= specialThreadNumSamples"
- "on cpu %d"
- "port label flags %#llx is too large"
- "printTargetThreadOnly, but target thread ID %llu doesn't exist"
- "stack with %d kernel frames (leaf %#llx), %d user (leaf %#llx), %d swift async (leaf %#llx), backtracer %llu"
- "state %#x"
- "target thread id %#llx, target task %s: no main thread"
- "target thread id %#llx, target task %s: no target thread"
- "targetThread"
- "timebase"
- "tree state %lu-%lu (%lu) [%d] thread %#llx priority:%d state:%#llx microState:%#x waitInfo:%@ turnstileInfo:%@ io:%@ timeRanges:%@ onBehalfOfPid:%d"
- "turnstile blocked on %#llx at priority %d, %d hops, %#llx flags"
- "turnstile blocked on %#llx at priority %d, %d hops, %#llx flags, port name:%@, flags:%#llx, domain:%llu"
- "turnstile info for task's threads not within task"
- "turnstileInfos == NULL"
- "unknown (%#x)"
- "user stack frame %#llx not in an array"
- "user stack frame %#x not in an array"
- "user stack lr %#llx not in an array"
- "user stack lr %#x not in an array"
- "v16@?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v}8"
- "v32@?0@\"NSString\"8@\"NSMutableData\"16^B24"
- "waitInfos == NULL"
- "\xc2"

```
