## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-385.14.0.0.0
-  __TEXT.__text: 0xe9034
-  __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_methlist: 0x5a94
-  __TEXT.__const: 0x338
+410.0.0.0.0
+  __TEXT.__text: 0xedf5c
+  __TEXT.__auth_stubs: 0x1760
+  __TEXT.__objc_methlist: 0x5d64
+  __TEXT.__const: 0x348
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x16f1b
-  __TEXT.__oslogstring: 0xbe0d
-  __TEXT.__gcc_except_tab: 0x9c54
-  __TEXT.__unwind_info: 0x2050
-  __TEXT.__objc_classname: 0xaae
-  __TEXT.__objc_methname: 0xceaf
-  __TEXT.__objc_methtype: 0x1792
-  __TEXT.__objc_stubs: 0x79a0
-  __DATA_CONST.__got: 0x3c8
-  __DATA_CONST.__const: 0x3508
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __TEXT.__cstring: 0x17e6a
+  __TEXT.__oslogstring: 0xc632
+  __TEXT.__gcc_except_tab: 0x9aec
+  __TEXT.__unwind_info: 0x2090
+  __TEXT.__objc_classname: 0xb12
+  __TEXT.__objc_methname: 0xd81f
+  __TEXT.__objc_methtype: 0x1a1c
+  __TEXT.__objc_stubs: 0x7d20
+  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__const: 0x3700
+  __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27d8
+  __DATA_CONST.__objc_selrefs: 0x2960
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x298
-  __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0xbb8
-  __AUTH_CONST.__const: 0xa60
-  __AUTH_CONST.__cfstring: 0xbb00
-  __AUTH_CONST.__objc_const: 0xf7b0
-  __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __DATA_CONST.__objc_superrefs: 0x2a0
+  __DATA_CONST.__objc_arraydata: 0x1d0
+  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0xb00
+  __AUTH_CONST.__cfstring: 0xc7e0
+  __AUTH_CONST.__objc_const: 0x101c8
+  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__objc_arrayobj: 0x210
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xc6c
+  __DATA.__objc_ivar: 0xd10
   __DATA.__data: 0x5c4
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x50
+  __DATA.__crash_info: 0x148
+  __DATA.__bss: 0x30
   __DATA.__common: 0x498
-  __DATA_DIRTY.__objc_ivar: 0x44
-  __DATA_DIRTY.__objc_data: 0x2710
-  __DATA_DIRTY.__bss: 0x438
+  __DATA_DIRTY.__objc_ivar: 0x48
+  __DATA_DIRTY.__objc_data: 0x2800
+  __DATA_DIRTY.__bss: 0x470
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 14124CEA-4AEF-30EF-853B-48B89AD5B2AE
-  Functions: 2726
-  Symbols:   9334
-  CStrings:  8009
+  UUID: CB42C2AB-65DC-3C65-A42C-0D81033890A8
+  Functions: 2798
+  Symbols:   9595
+  CStrings:  8396
 
Symbols:
+ +[SASampleStore filterBlockForMicrostackshotTypes:startTime:endTime:pid:tid:]
+ +[SASharedCache currentSharedCacheWithDataGatheringOptions:]
+ +[SASharedCache sharedCacheWithCSSymbolicator:dataGatheringOptions:]
+ +[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]
+ +[SASharedCache sharedCacheWithUUID:slide:slidBaseAddress:dataGatheringOptions:]
+ +[SATask taskWithPid:uniquePid:name:mainBinaryPath:forkTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:]
+ +[SATaskState stateWithKCDataDeltaTask:terminatedThreadsInstructionCycles:memoryStatus:machTimebase:donatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
+ +[SATaskState stateWithKCDataTask:terminatedThreadsInstructionCycles:memoryStatus:machTimebase:donatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
+ +[SATaskState stateWithKCDataTransitioningTask:terminatedThreadsInstructionCycles:memoryStatus:machTimebase:donatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
+ +[SAThreadStateMicrostackshot stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:]
+ -[SABinary applyLength:]
+ -[SABinary checkForSegmentWithCleanName:]
+ -[SABinary segmentWithCleanName:length:offsetIntoBinary:]
+ -[SABinary segmentWithName:length:offsetIntoBinary:]
+ -[SABootInfo initWithUUID:wallTime:bootArgs:kernelVersion:osProductVersion:osProductVersionExtra:osBuildVersion:]
+ -[SADependencyGraphNode debugDescription]
+ -[SADependencyGraphNode taskDependency]
+ -[SADependencyGraphTaskNode .cxx_destruct]
+ -[SADependencyGraphTaskNode initWithTask:taskState:]
+ -[SADependencyGraphTaskNode taskState]
+ -[SADependencyGraphTaskNode task]
+ -[SAExclave fillInName:textLayout:dataGatheringOptions:]
+ -[SAExclave initWithKCData:name:textLayout:dataGatheringOptions:]
+ -[SAMicrostackshotInfo .cxx_destruct]
+ -[SAMicrostackshotInfo bootInfo]
+ -[SAMicrostackshotInfo clear]
+ -[SAMicrostackshotInfo microSnapshotFlags]
+ -[SAMicrostackshotInfo processID]
+ -[SAMicrostackshotInfo processMainBinaryUUID]
+ -[SAMicrostackshotInfo processName]
+ -[SAMicrostackshotInfo processResourceCoalitionID]
+ -[SAMicrostackshotInfo setBootinfo:microSnapshotFlags:wallTime:processID:processName:processMainBinaryUUID:processResourceCoalitionID:threadID:threadOnBehalfOfProximatePid:threadOnBehalfOfOriginPid:]
+ -[SAMicrostackshotInfo threadID]
+ -[SAMicrostackshotInfo threadOnBehalfOfOriginPid]
+ -[SAMicrostackshotInfo threadOnBehalfOfProximatePid]
+ -[SAMicrostackshotInfo wallTime]
+ -[SAMountStatusData dealloc]
+ -[SAMountStatusData initWithMount:status:]
+ -[SAMountStatusData mount]
+ -[SAMountStatusData status]
+ -[SAOnBehalfOfMultiple displayStringWithPids:]
+ -[SASamplePrintOptions displayCPUSpeedInCallTrees]
+ -[SASamplePrintOptions displayPMICycleIntervalInCallTrees]
+ -[SASamplePrintOptions setDisplayCPUSpeedInCallTrees:]
+ -[SASamplePrintOptions setDisplayPMICycleIntervalInCallTrees:]
+ -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]
+ -[SASamplePrinter hasTargetProcess]
+ -[SASamplePrinter printLaunchdThrottledProcessesToStream:]
+ -[SASamplePrinter printMultipleTasks:]
+ -[SASamplePrinter rawNameForTask:]
+ -[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]
+ -[SASampleStore _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]
+ -[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]
+ -[SASampleStore _backfillForkTimestamp:toPreviousTasksEnumerator:execTimestampOfNextTask:]
+ -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]
+ -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]
+ -[SASampleStore _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]
+ -[SASampleStore _taskForPid:uniquePid:name:forkTime:loadInfos:numLoadInfos:loadInfosIsPartial:textExecLoadInfos:numTextExecLoadInfos:textExecLoadInfosIsPartial:architecture:timestamp:sharedCache:needAOTInfo:usesSuddenTermination:allowsIdleExit:isRunningBoardManaged:]
+ -[SASampleStore addBootCycle:]
+ -[SASampleStore addMicrostackshotsFromData:statistics:filterBlock:]
+ -[SASampleStore addMicrostackshotsFromFile:statistics:filterBlock:]
+ -[SASampleStore backfillTask:lastSampleIndex:timestamp:haveSnap:terminatedThreadsUserTimeInNs:terminatedThreadsSystemTimeInNs:terminatedThreadsCycles:terminatedThreadsInstructions:suspendCount:pageins:isDarwinBG:isForeground:isBoosted:isDirty:isRunningBoardActive:hasRunningBoardAssertion:haveWQFlags:wqExceededTotalThreadLimit:wqExceededConstrainedThreadLimit:haveCoopAndActiveConstrWQFlags:wqExceededCooperativeThreadLimit:wqExceededActiveConstrainedThreadLimit:haveMem:taskSizeInBytes:haveLatencyQos:latencyQos:haveRunawayMitigated:isRunawayMitigated:effectiveJetsamPriority:]
+ -[SASampleStore deadReckonSamplesBeforeTimestamp:kperfState:]
+ -[SASampleStore detector]
+ -[SASampleStore findTargetProcessesInTimeRange:]
+ -[SASampleStore issueType]
+ -[SASampleStore mitigationReason]
+ -[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:ktraceDataUnavailable:]
+ -[SASampleStore setDetector:]
+ -[SASampleStore setIssueType:]
+ -[SASampleStore setMitigationReason:]
+ -[SASampleStore setTargetMainBinaryUUID:]
+ -[SASampleStore setTargetProcesses:]
+ -[SASampleStore targetMainBinaryUUID]
+ -[SASampleStore targetProcesses]
+ -[SASampleStore(KPerfPrivate) parseKTraceFile:afterMachAbsTime:warningsOut:errorOut:]
+ -[SASampleStore(KPerfPrivate) parseStackshotsFromKTraceFile:afterMachAbsTime:warningsOut:errorOut:]
+ -[SASegment applyLength:]
+ -[SASegment enumerateAllSymbols:]
+ -[SATask forkTimestamp]
+ -[SATask hardenedHeap]
+ -[SATask initWithPid:uniquePid:name:mainBinaryPath:forkTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:]
+ -[SATask isRunningBoardManaged]
+ -[SATaskAggregationIdentifier initWithBinary:sharedCache:rcid:isTarget:]
+ -[SATaskState assertionJetsamPriority]
+ -[SATaskState correspondsToKCDataDeltaTask:terminatedThreadsInstructionCycles:memoryStatus:machTimebase:donatingUniquePids:]
+ -[SATaskState correspondsToKCDataTask:terminatedThreadsInstructionCycles:memoryStatus:machTimebase:donatingUniquePids:]
+ -[SATaskState correspondsToKCDataTransitioningTask:terminatedThreadsInstructionCycles:memoryStatus:machTimebase:donatingUniquePids:]
+ -[SATaskState effectiveJetsamPriority]
+ -[SATaskState hasRunningBoardAssertion]
+ -[SATaskState isRunawayMitigated]
+ -[SATaskState isRunningBoardActive]
+ -[SATaskState isTALEngaged]
+ -[SATaskState memoryLimitMB]
+ -[SATaskState requestedJetsamPriority]
+ -[SATaskState wqExceededActiveConstrainedThreadLimit]
+ -[SATaskState wqExceededCooperativeThreadLimit]
+ -[SATaskStateInTransition initWithKCDataTransitioningTask:andTerminatedThreadsInstructionCycles:memoryStatus:machTimebase:andDonatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
+ -[SAThreadState isPMICycleRecord]
+ -[SAThreadState pmiCycleInterval]
+ -[SAThreadState timestampLastRan]
+ -[SAThreadStateMicrostackshot isPMICycleRecord]
+ -[SAThreadStateMicrostackshot pmiCycleInterval]
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table180
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table212
+ GCC_except_table213
+ GCC_except_table216
+ GCC_except_table224
+ GCC_except_table235
+ GCC_except_table238
+ GCC_except_table264
+ GCC_except_table27
+ GCC_except_table275
+ GCC_except_table279
+ GCC_except_table44
+ GCC_except_table49
+ GCC_except_table536
+ GCC_except_table539
+ GCC_except_table544
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table69
+ GCC_except_table7
+ GCC_except_table80
+ GCC_except_table88
+ GCC_except_table90
+ _.str.72
+ _.str.734
+ _.str.82
+ _CSSymbolicatorGetSharedCacheBaseAddress
+ _CopyBootArgs
+ _CopyKernelVersion
+ _GetOSVersions
+ _MobileGestalt_copy_productTypeDescForPowerPerf_obj
+ _MobileGestalt_get_current_device
+ _OBJC_CLASS_$_SADependencyGraphTaskNode
+ _OBJC_CLASS_$_SAKTraceDataUnavailable
+ _OBJC_CLASS_$_SAMicrostackshotInfo
+ _OBJC_CLASS_$_SAMountStatusData
+ _OBJC_IVAR_$_SADependencyGraphNode._taskDependency
+ _OBJC_IVAR_$_SADependencyGraphTaskNode._task
+ _OBJC_IVAR_$_SADependencyGraphTaskNode._taskState
+ _OBJC_IVAR_$_SAKPerfState._taskEffectiveJetsamPriority
+ _OBJC_IVAR_$_SAKPerfState._taskRunawayMitigatedStateChanges
+ _OBJC_IVAR_$_SAKTraceDataUnavailable._effectiveJetsamPriority
+ _OBJC_IVAR_$_SAKTraceDataUnavailable._runawayMitigation
+ _OBJC_IVAR_$_SAMicrostackshotInfo._bootInfo
+ _OBJC_IVAR_$_SAMicrostackshotInfo._microSnapshotFlags
+ _OBJC_IVAR_$_SAMicrostackshotInfo._processID
+ _OBJC_IVAR_$_SAMicrostackshotInfo._processMainBinaryUUID
+ _OBJC_IVAR_$_SAMicrostackshotInfo._processName
+ _OBJC_IVAR_$_SAMicrostackshotInfo._processResourceCoalitionID
+ _OBJC_IVAR_$_SAMicrostackshotInfo._threadID
+ _OBJC_IVAR_$_SAMicrostackshotInfo._threadOnBehalfOfOriginPid
+ _OBJC_IVAR_$_SAMicrostackshotInfo._threadOnBehalfOfProximatePid
+ _OBJC_IVAR_$_SAMicrostackshotInfo._wallTime
+ _OBJC_IVAR_$_SAMountStatusData._mount
+ _OBJC_IVAR_$_SAMountStatusData._status
+ _OBJC_IVAR_$_SASamplePrintOptions._displayCPUSpeedInCallTrees
+ _OBJC_IVAR_$_SASamplePrintOptions._displayPMICycleIntervalInCallTrees
+ _OBJC_IVAR_$_SASamplePrinter._hasTimeIndexes
+ _OBJC_IVAR_$_SASampleStore._detector
+ _OBJC_IVAR_$_SASampleStore._issueType
+ _OBJC_IVAR_$_SASampleStore._microstackshotInfo
+ _OBJC_IVAR_$_SASampleStore._mitigationReason
+ _OBJC_IVAR_$_SASampleStore._numPMIMicrostackshotsLost
+ _OBJC_IVAR_$_SASampleStore._pmiCycleIntervalMax
+ _OBJC_IVAR_$_SASampleStore._pmiCycleIntervalMin
+ _OBJC_IVAR_$_SASampleStore._targetMainBinaryUUID
+ _OBJC_IVAR_$_SASampleStore._targetProcesses
+ _OBJC_IVAR_$_SAStack._timeSinceThreadRan
+ _OBJC_IVAR_$_SATask._forkTimestamp
+ _OBJC_IVAR_$_SATask._hardenedHeap
+ _OBJC_IVAR_$_SATask._isRunningBoardManaged
+ _OBJC_IVAR_$_SATaskAggregationIdentifier._isTarget
+ _OBJC_IVAR_$_SATaskState._assertionJetsamPriority
+ _OBJC_IVAR_$_SATaskState._effectiveJetsamPriority
+ _OBJC_IVAR_$_SATaskState._memoryLimitMB
+ _OBJC_IVAR_$_SATaskState._requestedJetsamPriority
+ _OBJC_IVAR_$_SATaskStateKPerf._filledRunawayMitigated
+ _OBJC_IVAR_$_SAThreadState._timestampLastRan
+ _OBJC_METACLASS_$_SADependencyGraphTaskNode
+ _OBJC_METACLASS_$_SAKTraceDataUnavailable
+ _OBJC_METACLASS_$_SAMicrostackshotInfo
+ _OBJC_METACLASS_$_SAMountStatusData
+ _OSKextCopyLoadedKextInfo
+ _SACopySanitizedStringWhitespaceOnlyNullable
+ _SACountedStateCompare
+ __OBJC_$_INSTANCE_METHODS_SADependencyGraphTaskNode
+ __OBJC_$_INSTANCE_METHODS_SAMicrostackshotInfo
+ __OBJC_$_INSTANCE_METHODS_SAMountStatusData
+ __OBJC_$_INSTANCE_VARIABLES_SADependencyGraphTaskNode
+ __OBJC_$_INSTANCE_VARIABLES_SAKTraceDataUnavailable
+ __OBJC_$_INSTANCE_VARIABLES_SAMicrostackshotInfo
+ __OBJC_$_INSTANCE_VARIABLES_SAMountStatusData
+ __OBJC_$_PROP_LIST_SADependencyGraphTaskNode
+ __OBJC_$_PROP_LIST_SAMicrostackshotInfo
+ __OBJC_$_PROP_LIST_SAMountStatusData
+ __OBJC_CLASS_RO_$_SADependencyGraphTaskNode
+ __OBJC_CLASS_RO_$_SAKTraceDataUnavailable
+ __OBJC_CLASS_RO_$_SAMicrostackshotInfo
+ __OBJC_CLASS_RO_$_SAMountStatusData
+ __OBJC_METACLASS_RO_$_SADependencyGraphTaskNode
+ __OBJC_METACLASS_RO_$_SAKTraceDataUnavailable
+ __OBJC_METACLASS_RO_$_SAMicrostackshotInfo
+ __OBJC_METACLASS_RO_$_SAMountStatusData
+ __ZZ94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]E9onceToken
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1520
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1524
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1527
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1521
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1528
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1956
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1958
+ ___116-[SASampleStore(KPerf) addLoadInfoFromKTrace:lastKTraceEventTimestamp:checkForNewLoadInfosEvenWithExistingLoadInfo:]_block_invoke.185
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.160
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.165
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_10
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_11
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_12
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_13
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_14
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_15
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.161
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.166
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_3
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_3.169
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_4
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_5
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_6
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_7
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_8
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_9
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2429
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2445
+ ___1359-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke.297
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke.299
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_2
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_2.300
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_3
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2391
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2400
+ ___28-[SASampleStore symbolicate]_block_invoke.505
+ ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke
+ ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.346
+ ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.356
+ ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.360
+ ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke_2
+ ___29-[SASampleStore gatherTrials]_block_invoke.558
+ ___29-[SASampleStore gatherTrials]_block_invoke_2.559
+ ___30-[SASamplePrinter printHeader]_block_invoke.1335
+ ___30-[SASamplePrinter printHeader]_block_invoke.1362
+ ___30-[SASamplePrinter printHeader]_block_invoke.1369
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1336
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1382
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.502
+ ___32-[SABootInfo initForCurrentBoot]_block_invoke
+ ___32-[SASegment addTailspinSymbols:]_block_invoke.34
+ ___33-[SASampleStore gatherOsVersions]_block_invoke
+ ___34-[SASamplePrinter printDeadlocks:]_block_invoke
+ ___34-[SASegment addInfoFromCSSegment:]_block_invoke.43
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_2
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_3
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_4
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_5
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_6
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_7
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_8
+ ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_9
+ ___37-[SASamplePrinter checkForBadOptions]_block_invoke.382
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2749
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2754
+ ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.640
+ ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke_2
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1463
+ ___44-[SAProximateProcess displayStringWithPids:]_block_invoke
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1469
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1473
+ ___46-[SAOnBehalfOfMultiple displayStringWithPids:]_block_invoke
+ ___48-[SASampleStore findTargetProcessesInTimeRange:]_block_invoke
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2006
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2007
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2008
+ ___50-[SASamplePrinter printRunawayMitigatedProcesses:]_block_invoke
+ ___50-[SASamplePrinter printRunawayMitigatedProcesses:]_block_invoke_2
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_2
+ ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.347
+ ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.103
+ ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.97
+ ___56-[SASamplePrinter shouldPrintTask:thread:dispatchQueue:]_block_invoke
+ ___57-[SABinary segmentWithCleanName:length:offsetIntoBinary:]_block_invoke
+ ___593-[SASampleStore(KPerfPrivate) backfillTask:lastSampleIndex:timestamp:haveSnap:terminatedThreadsUserTimeInNs:terminatedThreadsSystemTimeInNs:terminatedThreadsCycles:terminatedThreadsInstructions:suspendCount:pageins:isDarwinBG:isForeground:isBoosted:isDirty:isRunningBoardActive:hasRunningBoardAssertion:haveWQFlags:wqExceededTotalThreadLimit:wqExceededConstrainedThreadLimit:haveCoopAndActiveConstrWQFlags:wqExceededCooperativeThreadLimit:wqExceededActiveConstrainedThreadLimit:haveMem:taskSizeInBytes:haveLatencyQos:latencyQos:haveRunawayMitigated:isRunawayMitigated:effectiveJetsamPriority:]_block_invoke
+ ___60+[SASharedCache currentSharedCacheWithDataGatheringOptions:]_block_invoke
+ ___60-[SASamplePrinter printProcessesWithHIESwallowedExceptions:]_block_invoke_2
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke.484
+ ___68+[SASharedCache sharedCacheWithCSSymbolicator:dataGatheringOptions:]_block_invoke
+ ___68+[SASharedCache sharedCacheWithCSSymbolicator:dataGatheringOptions:]_block_invoke_2
+ ___68-[SASampleStore(KPerf) deadReckonSamplesBeforeTimestamp:kperfState:]_block_invoke
+ ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke
+ ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.495
+ ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke_2
+ ___76+[SADependencyGraphNode dependencyGraphForThreadsInSampleStore:atTimestamp:]_block_invoke.21
+ ___77+[SASampleStore filterBlockForMicrostackshotTypes:startTime:endTime:pid:tid:]_block_invoke
+ ___80+[SASharedCache sharedCacheWithUUID:slide:slidBaseAddress:dataGatheringOptions:]_block_invoke
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.214
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.226
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.252
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.271
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.285
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.304
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.313
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.263
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.278
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.289
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.307
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.317
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.302
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.310
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_4
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_4.311
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_5
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_5.312
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_6
+ ___99-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:ktraceDataUnavailable:]_block_invoke
+ ___99-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:ktraceDataUnavailable:]_block_invoke.382
+ ___CopyMountStatusData_block_invoke.73
+ ___ReadAheadTaskLevelInfo_block_invoke.2039
+ ___ReadAheadTaskLevelInfo_block_invoke.2044
+ ___ReadAheadTaskLevelInfo_block_invoke.2047
+ ___SASortStringArray_block_invoke
+ ___SASortedStringArray_block_invoke
+ ___block_descriptor_113_ea8_32s40s48s56s64r72r80r88r96r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8r80l8s56l8r88l8r96l8
+ ___block_descriptor_173_ea8_32s40s48s56r64r72r80r88r96r_e28_v32?0"SATaskState"8Q16^B24ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8s48l8
+ ___block_descriptor_184_e8_32s40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r_e28_v32?0"SATaskState"8Q16^B24ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8
+ ___block_descriptor_311_e8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8
+ ___block_descriptor_32_e14_"NSArray"8?0l
+ ___block_descriptor_32_e29_q24?0"NSArray"8"NSArray"16l
+ ___block_descriptor_32_e31_q24?0"NSString"8"NSString"16l
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e57_v40?0"NSString"8"NSString"16"NSString"24"NSString"32ls32l8
+ ___block_descriptor_48_e8_32s40s_e16_v16?0"SATask"8ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r48r_e57_v40?0"NSString"8"NSString"16"NSString"24"NSString"32lr32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lu48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e20_v24?0"SATask"8^B16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e28_v32?0"SATaskState"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr32l8
+ ___block_descriptor_56_ea8_32s40s48r_e23_v16?0^{ktrace_chunk=}8lr48l8s32l8s40l8
+ ___block_descriptor_64_e30_Q16?0"SAMicrostackshotInfo"8l
+ ___block_descriptor_64_e8_32s40s48s56s_e48_v32?0"NSNumber"8"SADependencyGraphNode"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56r_e23_v16?0^{ktrace_chunk=}8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_ea8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
+ ___block_descriptor_65_e8_32s40s48s56s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_72_ea8_32s40s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8
+ ___block_descriptor_80_e8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
+ ___block_descriptor_80_ea8_32s40s48s_e390_v16?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}Q{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v{?=QQQ^{kpdecode_exclave_callstack}}I}8ls32l8s40l8s48l8
+ ___block_descriptor_80_ea8_32s40s48s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8s48l8
+ ___block_descriptor_88_ea8_32s40s48r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr48l8s32l8s40l8
+ ___block_descriptor_88_ea8_32s40s48s56s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_97_ea8_32s40s48s56r64r72r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr56l8s32l8r64l8r72l8s40l8s48l8
+ ___block_literal_global.1151
+ ___block_literal_global.1338
+ ___block_literal_global.142
+ ___block_literal_global.143
+ ___block_literal_global.1475
+ ___block_literal_global.181
+ ___block_literal_global.187
+ ___block_literal_global.1884
+ ___block_literal_global.1927
+ ___block_literal_global.1929
+ ___block_literal_global.1932
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.2027
+ ___block_literal_global.2032
+ ___block_literal_global.2058
+ ___block_literal_global.2071
+ ___block_literal_global.2073
+ ___block_literal_global.2388
+ ___block_literal_global.2403
+ ___block_literal_global.242
+ ___block_literal_global.2482
+ ___block_literal_global.254
+ ___block_literal_global.2720
+ ___block_literal_global.2742
+ ___block_literal_global.275
+ ___block_literal_global.2751
+ ___block_literal_global.306
+ ___block_literal_global.309
+ ___block_literal_global.319
+ ___block_literal_global.341
+ ___block_literal_global.348
+ ___block_literal_global.479
+ ___block_literal_global.482
+ ___block_literal_global.486
+ ___block_literal_global.494
+ ___block_literal_global.512
+ ___block_literal_global.514
+ ___block_literal_global.522
+ ___block_literal_global.543
+ ___block_literal_global.558
+ ___block_literal_global.583
+ ___block_literal_global.587
+ ___block_literal_global.637
+ ___block_literal_global.64
+ ___block_literal_global.71
+ ___block_literal_global.771
+ __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:.next_fake_unique_pid
+ _kCFBundleIdentifierKey
+ _ktrace_config_kdebug_get_typefilter
+ _ktrace_machine_product
+ _objc_msgSend$_doSharedCachesWork:
+ _objc_msgSend$addMicrostackshotsFromData:statistics:filterBlock:
+ _objc_msgSend$addMicrostackshotsFromFile:statistics:filterBlock:
+ _objc_msgSend$assertionJetsamPriority
+ _objc_msgSend$detector
+ _objc_msgSend$displayCPUSpeedInCallTrees
+ _objc_msgSend$displayPMICycleIntervalInCallTrees
+ _objc_msgSend$effectiveJetsamPriority
+ _objc_msgSend$forkTimestamp
+ _objc_msgSend$hardenedHeap
+ _objc_msgSend$hasRunningBoardAssertion
+ _objc_msgSend$initWithKCDataTransitioningTask:andTerminatedThreadsInstructionCycles:memoryStatus:machTimebase:andDonatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:
+ _objc_msgSend$initWithMount:status:
+ _objc_msgSend$initWithPid:uniquePid:name:mainBinaryPath:forkTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isRunawayMitigated
+ _objc_msgSend$isRunningBoardActive
+ _objc_msgSend$isRunningBoardManaged
+ _objc_msgSend$isTALEngaged
+ _objc_msgSend$issueType
+ _objc_msgSend$memoryLimitMB
+ _objc_msgSend$microSnapshotFlags
+ _objc_msgSend$mitigationReason
+ _objc_msgSend$mount
+ _objc_msgSend$pmiCycleInterval
+ _objc_msgSend$processID
+ _objc_msgSend$processName
+ _objc_msgSend$requestedJetsamPriority
+ _objc_msgSend$stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:
+ _objc_msgSend$status
+ _objc_msgSend$targetMainBinaryUUID
+ _objc_msgSend$targetProcesses
+ _objc_msgSend$timestampLastRan
+ _objc_msgSend$wqExceededActiveConstrainedThreadLimit
+ _objc_msgSend$wqExceededCooperativeThreadLimit
+ _objc_release_x10
- +[SABinaryLoadInfo sortBinaryLoadInfos:]
- +[SASegment segmentWithBinary:name:length:]
- +[SASharedCache sharedCacheWithCSSymbolicator:]
- +[SASharedCache sharedCacheWithDyldSharedCache:]
- +[SASharedCache sharedCacheWithUUID:slidBaseAddress:]
- +[SASharedCache sharedCacheWithUUID:slide:slidBaseAddress:findMappingsIfUnknown:]
- +[SATask taskWithPid:uniquePid:name:mainBinaryPath:pidStartTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:]
- +[SATaskState stateWithKCDataDeltaTask:terminatedThreadsInstructionCycles:machTimebase:donatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
- +[SATaskState stateWithKCDataTask:terminatedThreadsInstructionCycles:machTimebase:donatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
- +[SATaskState stateWithKCDataTransitioningTask:terminatedThreadsInstructionCycles:machTimebase:donatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
- +[SAThreadStateMicrostackshot stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:]
- -[SAAuxiliaryData dealloc]
- -[SABinary addSegment:]
- -[SABinary segmentWithCleanName:]
- -[SABinary setLength:]
- -[SAExclave fillInName:textLayout:]
- -[SAExclave initWithKCData:name:textLayout:]
- -[SAOnBehalfOfMultiple displayString]
- -[SARecipe insertState:hasConcurrentExecution:]
- -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]
- -[SASamplePrinter aggregateByDispatchQueue:]
- -[SASamplePrinter complainAboutSamplingGapBetweenStartTimestamp:endTimestamp:]
- -[SASamplePrinter displayTimeIndexForSampleIndex:]
- -[SASamplePrinter hasTimeIndexes]
- -[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]
- -[SASampleStore _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]
- -[SASampleStore _addMicrostackshotFromData:ofTypes:inTimeRangeStart:end:onlyPid:onlyTid:statistics:]
- -[SASampleStore _backfillPidStartTimestamp:toPreviousTasksEnumerator:execTimestampOfNextTask:]
- -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]
- -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]
- -[SASampleStore _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]
- -[SASampleStore _taskForPid:uniquePid:name:pidStartTime:loadInfos:numLoadInfos:loadInfosIsPartial:textExecLoadInfos:numTextExecLoadInfos:textExecLoadInfosIsPartial:architecture:timestamp:sharedCache:needAOTInfo:]
- -[SASampleStore addSharedCache:]
- -[SASampleStore backfillTask:lastSampleIndex:timestamp:haveSnap:terminatedThreadsUserTimeInNs:terminatedThreadsSystemTimeInNs:terminatedThreadsCycles:terminatedThreadsInstructions:suspendCount:pageins:isDarwinBG:isForeground:isBoosted:isDirty:haveWQFlags:wqExceededTotalThreadLimit:wqExceededConstrainedThreadLimit:haveMem:taskSizeInBytes:haveLatencyQos:latencyQos:]
- -[SASampleStore gatherBootArgs]
- -[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]
- -[SASampleStore setEndTime:]
- -[SASampleStore setStartTime:]
- -[SASegment grabInstructionsFromOtherSegment:]
- -[SASegment setLength:]
- -[SATask initWithPid:uniquePid:name:mainBinaryPath:pidStartTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:]
- -[SATaskAggregationIdentifier initWithBinary:sharedCache:rcid:]
- -[SATaskState correspondsToKCDataDeltaTask:terminatedThreadsInstructionCycles:machTimebase:donatingUniquePids:]
- -[SATaskState correspondsToKCDataTask:terminatedThreadsInstructionCycles:machTimebase:donatingUniquePids:]
- -[SATaskState correspondsToKCDataTransitioningTask:terminatedThreadsInstructionCycles:machTimebase:donatingUniquePids:]
- -[SATaskStateInTransition initWithKCDataTransitioningTask:andTerminatedThreadsInstructionCycles:machTimebase:andDonatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
- GCC_except_table105
- GCC_except_table106
- GCC_except_table107
- GCC_except_table122
- GCC_except_table123
- GCC_except_table124
- GCC_except_table132
- GCC_except_table149
- GCC_except_table151
- GCC_except_table152
- GCC_except_table184
- GCC_except_table186
- GCC_except_table2
- GCC_except_table203
- GCC_except_table214
- GCC_except_table215
- GCC_except_table217
- GCC_except_table231
- GCC_except_table237
- GCC_except_table259
- GCC_except_table273
- GCC_except_table30
- GCC_except_table38
- GCC_except_table498
- GCC_except_table50
- GCC_except_table501
- GCC_except_table506
- GCC_except_table57
- GCC_except_table63
- GCC_except_table64
- GCC_except_table77
- _.str.476
- _.str.61
- _.str.727
- _FreeMountStatusData
- _OBJC_IVAR_$_SATask._pidStartTimestamp
- __ZZ77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]E9onceToken
- ___100-[SASampleStore _addMicrostackshotFromData:ofTypes:inTimeRangeStart:end:onlyPid:onlyTid:statistics:]_block_invoke
- ___100-[SASampleStore _addMicrostackshotFromData:ofTypes:inTimeRangeStart:end:onlyPid:onlyTid:statistics:]_block_invoke.479
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1402
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1406
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1409
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1403
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1410
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1780
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1782
- ___1143-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.296
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.298
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.299
- ___116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_3
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2189
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2205
- ___23-[SABinary addSegment:]_block_invoke
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2151
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2160
- ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke
- ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.345
- ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.355
- ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.359
- ___264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke_2
- ___28-[SASampleStore symbolicate]_block_invoke.500
- ___29-[SASampleStore gatherTrials]_block_invoke.545
- ___29-[SASampleStore gatherTrials]_block_invoke_2.546
- ___30-[SASamplePrinter printHeader]_block_invoke.1234
- ___30-[SASamplePrinter printHeader]_block_invoke.1264
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1235
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1277
- ___31+[SASharedCache addDSCSymData:]_block_invoke.505
- ___32-[SASegment addTailspinSymbols:]_block_invoke.38
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_2
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_3
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_4
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_5
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_6
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_7
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_8
- ___328-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_9
- ___34-[SASegment addInfoFromCSSegment:]_block_invoke.46
- ___35+[SASharedCache currentSharedCache]_block_invoke
- ___35-[SAProximateProcess displayString]_block_invoke
- ___37-[SAOnBehalfOfMultiple displayString]_block_invoke
- ___37-[SASamplePrinter checkForBadOptions]_block_invoke.353
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2514
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2519
- ___380-[SASampleStore(KPerfPrivate) backfillTask:lastSampleIndex:timestamp:haveSnap:terminatedThreadsUserTimeInNs:terminatedThreadsSystemTimeInNs:terminatedThreadsCycles:terminatedThreadsInstructions:suspendCount:pageins:isDarwinBG:isForeground:isBoosted:isDirty:haveWQFlags:wqExceededTotalThreadLimit:wqExceededConstrainedThreadLimit:haveMem:taskSizeInBytes:haveLatencyQos:latencyQos:]_block_invoke
- ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1349
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1356
- ___47+[SASharedCache sharedCacheWithCSSymbolicator:]_block_invoke
- ___47+[SASharedCache sharedCacheWithCSSymbolicator:]_block_invoke_2
- ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke
- ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.496
- ___48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke_2
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1830
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1831
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1832
- ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.331
- ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.84
- ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.90
- ___56-[SASampleStore(KPerf) kperfRecord:state:frameIterator:]_block_invoke
- ___76+[SADependencyGraphNode dependencyGraphForThreadsInSampleStore:atTimestamp:]_block_invoke_4
- ___77-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]_block_invoke
- ___77-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]_block_invoke.381
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.198
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.210
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.236
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.255
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.269
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.288
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.297
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.247
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.262
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.273
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.291
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.301
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.286
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.294
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_4
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_4.295
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_5
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_5.296
- ___77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_6
- ___81+[SASharedCache sharedCacheWithUUID:slide:slidBaseAddress:findMappingsIfUnknown:]_block_invoke
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.150
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.155
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_10
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_11
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_12
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_2
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_2.151
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_2.156
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_3
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_3.159
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_4
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_5
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_6
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_7
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_8
- ___84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke_9
- ___CopyMountStatusData_block_invoke.53
- ___ReadAheadTaskLevelInfo_block_invoke.1912
- ___ReadAheadTaskLevelInfo_block_invoke.1917
- ___ReadAheadTaskLevelInfo_block_invoke.1920
- ___block_descriptor_105_ea8_32s40s48s56r64r72r80r88r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8r72l8r80l8r88l8
- ___block_descriptor_120_e8_32s40r48r56r64r72r80r88r96r104r112r_e28_v32?0"SATaskState"8Q16^B24ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8
- ___block_descriptor_147_ea8_32s40s48s56r64r72r80r_e28_v32?0"SATaskState"8Q16^B24ls32l8s40l8r56l8r64l8r72l8r80l8s48l8
- ___block_descriptor_303_e8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8
- ___block_descriptor_48_ea8_32r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr32l8
- ___block_descriptor_48_ea8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0lu48l8s32l8s40l8
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_ea8_32s40s48r_e23_v16?0^{ktrace_chunk=}8ls32l8s40l8r48l8
- ___block_descriptor_57_e8_32s40s48s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e48_v32?0"NSNumber"8"SADependencyGraphNode"16^B24ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_ea8_32s40s48s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8
- ___block_descriptor_72_ea8_32s40s48s_e390_v16?0^{kpdecode_record=QQQi(?={?=[20c]}{?=[20c]}){?=I[4Q]}{?=iiQ}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}{kpdecode_callstack=II[256Q]}Q{kpdecode_pmc=i[32Q]}{?=IIII}{?=IQQQQ}{?=QQIssb3b3b3b3}{?=QiiQQ}{?=QQsC}{?=Q}{?=II}{?=Qi}{?=i^Q}{?=Q}{?=Ii}{?=[256c]QQI}{?=QQQQ}{?=QQ}{?=b3b3b3}{?=[64c]Q}{?=[64c]Q}{?={?=ISi}QQ}{?=QQQQQQQ}{?=III}^v{?=QQQ^{kpdecode_exclave_callstack}}I}8ls32l8s40l8s48l8
- ___block_descriptor_72_ea8_32s40s48s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
- ___block_descriptor_80_ea8_32s40s48r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr48l8s32l8s40l8
- ___block_descriptor_80_ea8_32s40s48s56s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8s48l8s56l8
- ___block_descriptor_81_ea8_32s40s48r56r64r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr48l8s32l8r56l8r64l8s40l8
- ___block_literal_global.1034
- ___block_literal_global.1237
- ___block_literal_global.139
- ___block_literal_global.152
- ___block_literal_global.169
- ___block_literal_global.1710
- ___block_literal_global.1754
- ___block_literal_global.1757
- ___block_literal_global.1799
- ___block_literal_global.185
- ___block_literal_global.1900
- ___block_literal_global.1905
- ___block_literal_global.1931
- ___block_literal_global.1943
- ___block_literal_global.1945
- ___block_literal_global.203
- ___block_literal_global.2148
- ___block_literal_global.2163
- ___block_literal_global.2242
- ___block_literal_global.2485
- ___block_literal_global.250
- ___block_literal_global.2507
- ___block_literal_global.2516
- ___block_literal_global.273
- ___block_literal_global.290
- ___block_literal_global.293
- ___block_literal_global.303
- ___block_literal_global.340
- ___block_literal_global.347
- ___block_literal_global.475
- ___block_literal_global.481
- ___block_literal_global.483
- ___block_literal_global.495
- ___block_literal_global.502
- ___block_literal_global.509
- ___block_literal_global.51
- ___block_literal_global.517
- ___block_literal_global.527
- ___block_literal_global.539
- ___block_literal_global.570
- ___block_literal_global.574
- ___block_literal_global.775
- __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:.next_fake_unique_pid
- __saos_printf_frame_base
- __saos_printf_frame_base_noindent
- __saos_printf_frame_timerange
- __saos_printf_indent_and_count
- __saos_printf_indent_and_count_noindent
- _objc_msgSend$currentSharedCache
- _objc_msgSend$initWithKCDataTransitioningTask:andTerminatedThreadsInstructionCycles:machTimebase:andDonatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:
- _objc_msgSend$initWithPid:uniquePid:name:mainBinaryPath:pidStartTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:
- _objc_msgSend$segmentWithName:
- _objc_msgSend$sharedCacheWithUUID:slide:
- _objc_msgSend$sharedCacheWithUUID:slide:slidBaseAddress:
- _objc_msgSend$stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:
- _objc_release_x4
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _saos_printf_frame
- _saos_printf_frame_noindent
- _saos_printf_microstackshot_state_as_frame
- _saos_printf_seconds_sigfig
CStrings:
+ " (requested "
+ " -> "
+ " ago"
+ "!\""
+ "!self.options.printJson"
+ "%'llu %s changed jetsam priority %d -> %d\n"
+ "%'llu %s changed runaway mitigation %d -> %d\n"
+ "%'llu task [%d] effective jetsam priority %d backfilled to %d task states (indexes %lu-%lu)\n"
+ "%'llu task [%d] effective jetsam priority %d backfilled to all (%d) task states (indexes %lu-%lu)\n"
+ "%'llu task [%d] runaway mitigated %d backfilled to %d task states (indexes %lu-%lu)\n"
+ "%'llu task [%d] runaway mitigated %d backfilled to all (%d) task states (indexes %lu-%lu)\n"
+ "%'llu task [%d] state (terminated cpu %llu, terminated instruction %llu, terminated cycles %llu, suspend count %d, pageins %u, darwinBG %d, foreground %d, boosted %d, dirty %d, isRunningBoardActive %d, hasRunningBoardAssertion %d, wq total %d, wq constrained %d wq cooperative %d wq active constrained %d) backfilled to %d task states (indexes %lu-%lu)\n"
+ "%'llu task [%d] state (terminated cpu %llu, terminated instruction %llu, terminated cycles %llu, suspend count %d, pageins %u, darwinBG %d, foreground %d, boosted %d, dirty %d, isRunningBoardActive %d, hasRunningBoardAssertion %d, wq total %d, wq constrained %d wq cooperative %d wq active constrained %d) backfilled to all (%d) task states (indexes %lu-%lu)\n"
+ "%*s%s: memlimit:%u effectivepri:%u requestedpri:%u assertionpri:%u%s\n"
+ "%-*s%lu (%@)\n"
+ "%-*sHas hardened heap\n"
+ "%-*sProcess clamped to Utility QoS for %lu sample%s\n"
+ "%-*sProcess is runaway mitigated\n"
+ "%-*sWorkqueue exceeded active constrained thread limit for %lu sample%s (more dispatch items runnable than allowed to run concurrently)\n"
+ "%-*sWorkqueue exceeded constrained thread limit (%u) for %lu sample%s (too many dispatch threads blocked in synchronous operations)\n"
+ "%-*sWorkqueue exceeded cooperative thread limit for %lu sample%s (more swift tasks runnable than allowed to run concurrently)\n"
+ "%-*sWorkqueue exceeded total thread limit (%u) for %lu sample%s (too many dispatch threads blocked in synchronous operations)\n"
+ "%@ - %@"
+ "%@ -> %@"
+ "%@ blocked by %@ which isn't alive at this time"
+ "%@ blocked by non-existent task [%d]"
+ "%@ has length above max: 0x%llx"
+ "%@ setting length above max for text segment: 0x%llx"
+ "%@ thread 0x%llx (%@)"
+ "%@ thread 0x%llx (%@) blocked by %@"
+ "%@ thread 0x%llx (%@) blocked by %@ thread 0x%llx (%@)"
+ "%@ updating length to 0x%llx"
+ "%d"
+ "%d - %d"
+ "%llu cycles/step"
+ "%llu gigacycles/step"
+ "%llu pmi cycle interval"
+ "%llu samples lost"
+ "%llu-"
+ "%lu from %@ due to missing load infos"
+ "%s: setting length to 0x%llx when we have a symbol at offset 0x%llx: %s"
+ "%u sample%s %@ (%@)"
+ "%u sample%s originated by %@"
+ "%uMhz"
+ "(badstring)"
+ ", assertion "
+ "0-length product type"
+ "0-length product type from MG"
+ "0@`"
+ "0OA"
+ "7OF"
+ "@\"NSArray\"8@?0"
+ "@\"SABootInfo\""
+ "@\"SADependencyGraphTaskNode\""
+ "@\"SAMicrostackshotInfo\""
+ "@100@0:8@16@24B32B36{_SACountedState=(?=Q{?=ISCb1b1b1b1b1})}40I48i52Q56C64@68i76i80Q84Q92"
+ "@104@0:8r^{micro_snapshot=IIQQCS}16r^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24@32@40Q48Q56@64@72@80{mach_timebase_info=II}88Q96"
+ "@32@0:8^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}16^{netfs_status=I[512c]II[0Q]}24"
+ "@88@0:8r^{transitioning_task_snapshot=QQQi[32c]}16r^{instrs_cycles_snapshot=QQ}24r^{task_memorystatus_snapshot=iiii}32{mach_timebase_info=II}40@48@56@64Q72Q80"
+ "AppDefined"
+ "AppKitDefined"
+ "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQiiQQQ}16Q24@32"
+ "B40@0:8^{?=CCiiiIQQQQQdIIIIIQQQ{_CSArchitecture=ii}(?=S{?=b1b1b1b1b1b1b1b1b1b1b1b1})}16Q24@32"
+ "B48@0:8r*16Q24@32^@40"
+ "Backfilled effectiveJetsamPriority %d, but most recent task state has not been filled"
+ "Backfilled runaway mitigated state change %d, but most recent task state has not been filled"
+ "Boot UUID in boot info invalid (%@)"
+ "Booted from a live filesystem, may check for roots installed multiple times"
+ "Booted from a snapshot, checking for roots installed once"
+ "Cannot target a single task and multiple tasks at the same time"
+ "Detector: "
+ "Got hw model %@ from MG"
+ "Heaviest stack for the target processes:\n"
+ "IconServices"
+ "Ignoring kext %@"
+ "Invalid build number class %s"
+ "Invalid entry in UUIDToBinaryLocations: %s -> %s"
+ "Issue type: "
+ "Jetsam Priority: "
+ "LeftMouseDragged"
+ "MULTIPLE PATHS"
+ "Memory Limit: "
+ "Missing tracecodes to track effective jetsam priority"
+ "Missing tracecodes to track runaway mitigation"
+ "Mitigation reason: "
+ "MouseEntered"
+ "MouseExited"
+ "MouseMoved"
+ "No UUID for kext %@, not including in load info"
+ "No boot UUID in boot info"
+ "No cpu type(%d)/subtype(%d) 0x%x/0x%x for main kernel binary"
+ "No heaviest callstack for target tasks"
+ "No kernel load infos for boot %{public}@"
+ "No load address for kext %@, not including in load info"
+ "No process with UUID %@"
+ "No wall time in boot info"
+ "Not including microstackshot for %@ [%d] at %@ due to being too early (%fs)"
+ "Not including microstackshot for %@ [%d] at %@ due to being too late (%fs)"
+ "Not including microstackshot for %@ [%d] at %@ due to being wrong pid (requested %d)"
+ "Not including microstackshot for %@ [%d] at %@ due to being wrong thread (0x%llx, requested 0x%llx)"
+ "Not including microstackshot for %@ [%d] at %@ due to being wrong type (0x%llx, requested 0x%x)"
+ "Number of Instances: "
+ "OSBundleCPUSubtype"
+ "OSBundleCPUType"
+ "OSBundleExecLoadAddress"
+ "OSBundleExecLoadSize"
+ "OSBundleExecutablePath"
+ "OSBundleLoadAddress"
+ "OSBundleLoadSize"
+ "OSBundleUUID"
+ "OSKext provided no load infos"
+ "OtherMouseDown"
+ "OtherMouseDragged"
+ "OtherMouseUp"
+ "Processes runaway mitigated: "
+ "Q16@?0@\"SAMicrostackshotInfo\"8"
+ "RightMouseDragged"
+ "Rq"
+ "RunningBoard Mgd: "
+ "SADependencyGraphTaskNode"
+ "SAKTraceDataUnavailable"
+ "SAMicrostackshotInfo"
+ "SAMountStatusData"
+ "SA_VERIFY_FLATBUFFERS"
+ "ScrollWheel"
+ "Segment %@ mismatched offsetIntoBinary 0x%llx (with length 0x%llx) - possibly due to two segments with the same name which is unsupported. Symbols may be incorrect"
+ "Setting target processes including %s which isn't in this SASampleStore"
+ "Solarium"
+ "Steps Missing: "
+ "SwiftUI"
+ "SystemDefined"
+ "T@\"NSArray\",C"
+ "T@\"NSString\",C,V_detector"
+ "T@\"NSString\",C,V_issueType"
+ "T@\"NSString\",C,V_mitigationReason"
+ "T@\"NSString\",R,V_processName"
+ "T@\"NSUUID\",C"
+ "T@\"NSUUID\",R,V_processMainBinaryUUID"
+ "T@\"SABootInfo\",R,V_bootInfo"
+ "T@\"SADependencyGraphTaskNode\",R"
+ "TB,V_displayCPUSpeedInCallTrees"
+ "TB,V_displayPMICycleIntervalInCallTrees"
+ "TQ,R,V_microSnapshotFlags"
+ "TQ,R,V_processResourceCoalitionID"
+ "T^{netfs_status=I[512c]II[0Q]},R,V_status"
+ "T^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]},R,V_mount"
+ "TabletPointer"
+ "TabletProximity"
+ "Target tasks do not share the same displayed load info, cannot merge stacks"
+ "Task %@ monotonically increasing data decreased at index %lu of %lu between %@ and %@:\nterminated threads cpu time %llu (%llu + %llu) -> %llu (%llu + %llu)\nterminated threads instructions %llu -> %llu\nterminated threads cycles %llu -> %llu\nfaults %u -> %u\npageins %u -> %u\ncow faults %u -> %u\n"
+ "Td,R,V_wallTime"
+ "Ti,R,V_processID"
+ "Ti,R,V_threadOnBehalfOfOriginPid"
+ "Ti,R,V_threadOnBehalfOfProximatePid"
+ "UUID too short for kext %@ (%lu), not including in load info"
+ "Unable to check for live filesystem, assuming not %{errno}d"
+ "Unable to create SASegment for CSSegment %s (from %@)"
+ "Unable to get boot time: %d"
+ "Unable to get bootsessionuuid: %d %s"
+ "Unable to get current device from MG: %d"
+ "Unable to get hw model from MG: %d"
+ "Unable to parse bootsessionuuid %s"
+ "Version dict provided invalid build number (class %s)"
+ "Xs"
+ "[_tasksByPid[@(task.pid)] indexOfObjectIdenticalTo:task] != NSNotFound"
+ "^{netfs_status=I[512c]II[0Q]}"
+ "^{netfs_status=I[512c]II[0Q]}16@0:8"
+ "^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}"
+ "^{statfs=IiQQQQQ{fsid=[2i]}IIII[16c][1024c][1024c]I[7I]}16@0:8"
+ "__kernel__"
+ "_assertionJetsamPriority"
+ "_bootInfo"
+ "_detector"
+ "_displayCPUSpeedInCallTrees"
+ "_displayPMICycleIntervalInCallTrees"
+ "_doSharedCachesWork:"
+ "_effectiveJetsamPriority"
+ "_filledRunawayMitigated"
+ "_forkTimestamp"
+ "_hardenedHeap"
+ "_hasTimeIndexes"
+ "_isRunningBoardManaged"
+ "_isTarget"
+ "_issueType"
+ "_memoryLimitMB"
+ "_microSnapshotFlags"
+ "_microstackshotInfo"
+ "_mitigationReason"
+ "_mount"
+ "_numPMIMicrostackshotsLost"
+ "_pmiCycleInterval"
+ "_pmiCycleIntervalMax"
+ "_pmiCycleIntervalMin"
+ "_processID"
+ "_processMainBinaryUUID"
+ "_processName"
+ "_processResourceCoalitionID"
+ "_requestedJetsamPriority"
+ "_runawayMitigation"
+ "_status"
+ "_swiftAsyncStitchIndex %u, _numUserFrames %u, maxDepth %u: %s"
+ "_targetMainBinaryUUID"
+ "_targetProcesses"
+ "_taskDependency"
+ "_taskEffectiveJetsamPriority"
+ "_taskRunawayMitigatedStateChanges"
+ "_threadOnBehalfOfOriginPid"
+ "_threadOnBehalfOfProximatePid"
+ "_timeSinceThreadRan"
+ "_timestampLastRan"
+ "addMicrostackshotsFromData:statistics:filterBlock:"
+ "addMicrostackshotsFromFile:statistics:filterBlock:"
+ "assertionJetsamPriority"
+ "blockedByDeadlock"
+ "bootInfo"
+ "bufferLength %lu < serialized SATaskState struct v3 with %u donating unique pids"
+ "bufferLength %lu < serialized SAThreadState v10 struct %lu"
+ "bufferLength %lu < serialized SAThreadState v9 struct %lu"
+ "bufferLength >= sizeof(*serializedThreadState_v10)"
+ "bufferLength >= sizeof(*serializedThreadState_v9)"
+ "com.apple.kpi."
+ "deadlocks"
+ "detector"
+ "displayCPUSpeedInCallTrees"
+ "displayPMICycleIntervalInCallTrees"
+ "effectiveJetsamPriority"
+ "enumerateAllSymbols:"
+ "forkTimestamp"
+ "hardenedHeap"
+ "hasRunningBoardAssertion"
+ "i40@0:8@16@24@?32"
+ "initWithKCDataTransitioningTask:andTerminatedThreadsInstructionCycles:memoryStatus:machTimebase:andDonatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:"
+ "initWithMount:status:"
+ "initWithPid:uniquePid:name:mainBinaryPath:forkTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:"
+ "isEqualToArray:"
+ "isPMICycleRecord"
+ "isRunawayMitigated"
+ "isRunningBoardActive"
+ "isRunningBoardManaged"
+ "isTALEngaged"
+ "issueType"
+ "jetsam priority %d"
+ "jetsam priority unknown"
+ "jetsamPriorityStr"
+ "kern.bootsessionuuid"
+ "last ran "
+ "launchdThrottledProcesses"
+ "memory status"
+ "memoryLimitMB"
+ "memoryLimitStr"
+ "microSnapshotFlags"
+ "mitigationReason"
+ "mount"
+ "no uuid"
+ "numPMIMicrostackshotsLost"
+ "numSamplesTALEngaged"
+ "numSamplesWQExceededActiveConstrainedThreadLimit"
+ "numSamplesWQExceededConstrainedThreadLimit"
+ "numSamplesWQExceededCooperativeThreadLimit"
+ "numSamplesWQExceededTotalThreadLimit"
+ "numStepsMissing"
+ "parseKTraceFile:afterMachAbsTime:warningsOut:errorOut:"
+ "parseStackshotsFromKTraceFile:afterMachAbsTime:warningsOut:errorOut:"
+ "pmiCycleInterval"
+ "pmiCycleIntervalMax"
+ "pmiCycleIntervalMin"
+ "printHIDEvent doesn't support json output"
+ "printJson not supported with systemstatsFormat"
+ "printProcessesHittingWQThreadLimits doesn't support json output"
+ "printProcessesWithHIESwallowedExceptions doesn't support json output"
+ "printRunawayMitigatedProcesses doesn't support json output"
+ "printSystemStatsStyleBinaryImages doesn't support json output"
+ "process clamped to Utility QoS"
+ "process has a runningboard assertion"
+ "process has no runningboard assertion"
+ "process memory limit %@"
+ "process not runaway mitigated"
+ "process runaway mitigated"
+ "process runningboard active"
+ "process runningboard inactive"
+ "process unclamped from Utility QoS"
+ "processID"
+ "processMainBinaryUUID"
+ "processName"
+ "processResourceCoalitionID"
+ "q40@0:8@16@24@?32"
+ "requestedJetsamPriority"
+ "setDetector:"
+ "setDisplayCPUSpeedInCallTrees:"
+ "setDisplayPMICycleIntervalInCallTrees:"
+ "setIssueType:"
+ "setMitigationReason:"
+ "setTargetMainBinaryUUID:"
+ "setTargetProcesses:"
+ "startTime %p or endTime %p nil"
+ "startTime && endTime"
+ "stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:"
+ "status"
+ "stepsMissingDetails"
+ "targetMainBinaryUUID"
+ "targetProcesses"
+ "targetTasks"
+ "targeting a HID event while targeting multiple processes"
+ "targeting main binary %@, but no target tasks"
+ "taskDependency"
+ "threadOnBehalfOfOriginPid"
+ "threadOnBehalfOfProximatePid"
+ "timestampLastRan"
+ "v40@?0@\"NSString\"8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
+ "wqExceededActiveConstrainedThreadLimit"
+ "wqExceededCooperativeThreadLimit"
+ "{_SACountedState=\"\"(?=\"bits\"Q\"\"{?=\"pmiCycleIntervalMillions\"I\"cpuSpeed100Mhz\"S\"_cpuNumOffbyOne\"C\"pCore\"b1\"eCore\"b1\"running\"b1\"runnable\"b1\"suspended\"b1})}"
- " -> %@"
- " -> %@\n"
- "%'llu task [%d] state (terminated cpu %llu, terminated instruction %llu, terminated cycles %llu, suspend count %d, pageins %u, darwinBG %d, foreground %d, boosted %d, dirty %d, wq total %d, wq constrained %d) backfilled to %d task states (indexes %lu-%lu)\n"
- "%'llu task [%d] state (terminated cpu %llu, terminated instruction %llu, terminated cycles %llu, suspend count %d, pageins %u, darwinBG %d, foreground %d, boosted %d, dirty %d, wq total %d, wq constrained %d) backfilled to all (%d) task states (indexes %lu-%lu)\n"
- "%@: No segment for %{public}s"
- "%s has length above max: 0x%llx"
- "%s: setting length 0"
- "%s: setting length to %llu when it was already %llu"
- "%s: setting length to %llu when we have a symbol at offset %llu: %s"
- "1`"
- "2q"
- "7OE"
- "@100@0:8@16@24B32B36Q40I48i52Q56C64@68i76i80Q84Q92"
- "@80@0:8r^{transitioning_task_snapshot=QQQi[32c]}16r^{instrs_cycles_snapshot=QQ}24{mach_timebase_info=II}32@40@48@56Q64Q72"
- "@96@0:8r^{micro_snapshot=IIQQCS}16r^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24@32@40Q48Q56@64@72@80{mach_timebase_info=II}88"
- "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQiiQ}16Q24@32"
- "B40@0:8^{?=CCiiiIQQQQQdIIIIIQQQ{_CSArchitecture=ii}(?=S{?=b1b1b1b1b1b1})}16Q24@32"
- "Binary %s segments not added after deserializing segments: %s vs\n%s"
- "No build number"
- "No nsstring for %s"
- "Not including microstackshot for %s [%d] at %@ due to being too early (%fs)"
- "Not including microstackshot for %s [%d] at %@ due to being too late (%fs)"
- "Not including microstackshot for %s [%d] at %@ due to being wrong pid (requested %d)"
- "Not including microstackshot for %s [%d] at %@ due to being wrong thread (0x%llx, requested 0x%llx)"
- "Not including microstackshot for %s [%d] at %@ due to being wrong type (0x%x, requested 0x%x)"
- "Overlap:%f eventEndToDataStart:%f eventStartToDataEnd:%f %@ vs %@-%@"
- "SAKTSYM Unable to get string for symbol owner path %s"
- "SAKTSYM new segment %@"
- "SAKTSYM segment %@ added length 0x%llx"
- "SAKTSYM segment %@ added offsetIntoBinary 0x%llx"
- "SAKTSYM segment %@ length mismatch 0x%llx"
- "TB,R,V_allowsIdleExit"
- "TB,R,V_usesSuddenTermination"
- "Task %@ monotonically increasing data decreased at index %lu of %lu between %@ and %@:\nterminated threads cpu time %llu (%llu + %llu) -> %llu (%llu + %llu)\nterminated threads instructions %llu -> %llu\nterminated threads cycles %llu -> %llufaults %u -> %upageins %u -> %ucow faults %u -> %u"
- "Unable to create NSString for signing identifier %s"
- "Xr"
- "^^{?}"
- "_cpuNum < UINT8_MAX"
- "_length == 0"
- "_pidStartTimestamp"
- "_segments.count >= segments.count"
- "_swiftAsyncStitchIndex %u, _numUserFrames %u: %s"
- "_swiftAsyncStitchIndex <= _numUserFrames"
- "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_ADDRESSSPACE"
- "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_IPCSTACKENTRY"
- "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_SCRESULT"
- "containerType == STACKSHOT_KCCONTAINER_EXCLAVE_TEXTLAYOUT"
- "initWithKCDataTransitioningTask:andTerminatedThreadsInstructionCycles:machTimebase:andDonatingUniquePids:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:"
- "initWithPid:uniquePid:name:mainBinaryPath:pidStartTime:loadInfos:numLoadInfos:textExecLoadInfos:numTextExecLoadInfos:architecture:sharedCache:"
- "segmentName"
- "stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:"

```
