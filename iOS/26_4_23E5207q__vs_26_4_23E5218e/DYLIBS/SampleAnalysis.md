## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x11a3a4
-  __TEXT.__auth_stubs: 0x1750
-  __TEXT.__objc_methlist: 0x63a4
-  __TEXT.__const: 0x358
+427.0.0.0.0
+  __TEXT.__text: 0x11c290
+  __TEXT.__auth_stubs: 0x1770
+  __TEXT.__objc_methlist: 0x63ec
+  __TEXT.__const: 0x368
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x19445
-  __TEXT.__oslogstring: 0xc5e0
-  __TEXT.__gcc_except_tab: 0x23210
-  __TEXT.__unwind_info: 0x3f38
-  __TEXT.__objc_classname: 0xb53
-  __TEXT.__objc_methname: 0xe7ac
-  __TEXT.__objc_methtype: 0x19d2
-  __TEXT.__objc_stubs: 0x84a0
-  __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x3c80
+  __TEXT.__cstring: 0x19473
+  __TEXT.__oslogstring: 0xc707
+  __TEXT.__gcc_except_tab: 0x2369c
+  __TEXT.__unwind_info: 0x3fe0
+  __TEXT.__objc_classname: 0xb54
+  __TEXT.__objc_methname: 0xe8e0
+  __TEXT.__objc_methtype: 0x19e8
+  __TEXT.__objc_stubs: 0x8540
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x3cd0
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b88
+  __DATA_CONST.__objc_selrefs: 0x2bb8
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH_CONST.__const: 0xac0
-  __AUTH_CONST.__cfstring: 0xd7c0
-  __AUTH_CONST.__objc_const: 0x111a8
+  __AUTH_CONST.__auth_got: 0xbd0
+  __AUTH_CONST.__const: 0xae0
+  __AUTH_CONST.__cfstring: 0xd920
+  __AUTH_CONST.__objc_const: 0x11248
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xe68
+  __DATA.__objc_ivar: 0xe78
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x30

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: C0792FCC-1031-36D4-9C3A-65FE36BCE7DB
-  Functions: 2964
-  Symbols:   10936
-  CStrings:  8904
+  UUID: 21B5F3D0-8556-3A87-82AD-14A38AC2E946
+  Functions: 2981
+  Symbols:   10999
+  CStrings:  8942
 
Symbols:
+ +[SATaskState stateWithStackshotTaskV1:machTimebase:hwPageSize:pagesGrabbedTotal:pagesGrabbedIOPLUPL:energyNJ:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
+ -[SABinary setSymbolOwner:fromDisk:]
+ -[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:dsymOnly:]
+ -[SABinary(Serialization) numSegmentsForSerializedBufferLength:]
+ -[SAInstruction(Serialization) numInlineFramesForSerializedBufferLength:]
+ -[SASamplePrintOptions setShowTaskEnergyAsLeafFrame:]
+ -[SASamplePrintOptions showTaskEnergyAsLeafFrame]
+ -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]
+ -[SASharedCache(Serialization) numLoadInfosForSerializedBufferLength:]
+ -[SATaskState energyNJ]
+ GCC_except_table119
+ GCC_except_table132
+ GCC_except_table168
+ GCC_except_table220
+ GCC_except_table260
+ GCC_except_table274
+ GCC_except_table279
+ GCC_except_table302
+ GCC_except_table317
+ GCC_except_table320
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table338
+ GCC_except_table341
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table561
+ GCC_except_table562
+ GCC_except_table563
+ GCC_except_table567
+ GCC_except_table571
+ GCC_except_table576
+ GCC_except_table577
+ GCC_except_table594
+ GCC_except_table595
+ GCC_except_table599
+ _.str.100
+ _.str.101
+ _.str.73
+ _.str.98
+ _.str.99
+ _CSSymbolicatorForeachSharedCacheSymbolicatorWithFlagsAndNotification
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_SABinary._onlyCheckedForDsymWhenLastSymbolicated
+ _OBJC_IVAR_$_SACallTreeState._energyNJ
+ _OBJC_IVAR_$_SASamplePrintOptions._showTaskEnergyAsLeafFrame
+ _OBJC_IVAR_$_SATaskState._energyNJ
+ _SAFormattedDouble
+ __SASerializableFillSerializedIndicesWithCollectionOfSerializableInstances
+ __SASerializableIndexForPointerFromSerializationDictionary
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1708
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1715
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1709
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1716
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.2196
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2197
+ ___123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.2287
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2674
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2696
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke.1976
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_2
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_2.2014
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_3
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_3.2022
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_4
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2634
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2643
+ ___28-[SASampleStore symbolicate]_block_invoke_7
+ ___28-[SASampleStore symbolicate]_block_invoke_8
+ ___28-[SASampleStore symbolicate]_block_invoke_9
+ ___29-[SASamplePrinter preprocess]_block_invoke.1619
+ ___29-[SASamplePrinter preprocess]_block_invoke_2.1620
+ ___29-[SASamplePrinter preprocess]_block_invoke_3.1621
+ ___29-[SASampleStore gatherTrials]_block_invoke.574
+ ___29-[SASampleStore gatherTrials]_block_invoke_2.575
+ ___30-[SASamplePrinter printHeader]_block_invoke.1040
+ ___30-[SASamplePrinter printHeader]_block_invoke.1506
+ ___30-[SASamplePrinter printHeader]_block_invoke.1533
+ ___30-[SASamplePrinter printHeader]_block_invoke.1540
+ ___30-[SASamplePrinter printHeader]_block_invoke_11
+ ___30-[SASamplePrinter printHeader]_block_invoke_12
+ ___30-[SASamplePrinter printHeader]_block_invoke_13
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1054
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1507
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1553
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.499
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2992
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2997
+ ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.656
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1649
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1655
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1659
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2246
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2247
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2248
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke.1664
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_2.1665
+ ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.492
+ ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.355
+ ___98-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:dsymOnly:]_block_invoke
+ ___98-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:dsymOnly:]_block_invoke.138
+ ___98-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:dsymOnly:]_block_invoke.140
+ ___98-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:dsymOnly:]_block_invoke_2
+ ___ReadAheadTaskLevelInfo_block_invoke.2082
+ ___ReadAheadTaskLevelInfo_block_invoke.2087
+ ___ReadAheadTaskLevelInfo_block_invoke.2090
+ ___block_descriptor_279_ea8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e74_v80?0Q8Q16Q24"SATaskState"32"SAThread"40Q48"SAThreadState"56B64B68^B72ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
+ ___block_descriptor_40_ea8_32s_e31_q24?0"NSNumber"8"NSNumber"16ls32l8
+ ___block_descriptor_48_ea8_32s40s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8
+ ___block_descriptor_49_ea8_32s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8
+ ___block_descriptor_56_ea8_32s40s48r_e74_v80?0Q8Q16Q24"SATaskState"32"SAThread"40Q48"SAThreadState"56B64B68^B72ls32l8r48l8s40l8
+ ___block_literal_global.122
+ ___block_literal_global.1318
+ ___block_literal_global.1509
+ ___block_literal_global.151
+ ___block_literal_global.1661
+ ___block_literal_global.1969
+ ___block_literal_global.2070
+ ___block_literal_global.2075
+ ___block_literal_global.2101
+ ___block_literal_global.2114
+ ___block_literal_global.2116
+ ___block_literal_global.2125
+ ___block_literal_global.2170
+ ___block_literal_global.2173
+ ___block_literal_global.2631
+ ___block_literal_global.2646
+ ___block_literal_global.2733
+ ___block_literal_global.2965
+ ___block_literal_global.2994
+ ___block_literal_global.340
+ ___block_literal_global.356
+ ___block_literal_global.358
+ ___block_literal_global.421
+ ___block_literal_global.424
+ ___block_literal_global.464
+ ___block_literal_global.466
+ ___block_literal_global.468
+ ___block_literal_global.479
+ ___block_literal_global.491
+ ___block_literal_global.532
+ ___block_literal_global.537
+ ___block_literal_global.539
+ ___block_literal_global.547
+ ___block_literal_global.568
+ ___block_literal_global.574
+ ___block_literal_global.599
+ ___block_literal_global.603
+ ___block_literal_global.653
+ ___block_literal_global.772
+ ___block_literal_global.99
+ _memset
+ _objc_msgSend$energyNJ
+ _objc_msgSend$numInlineFramesForSerializedBufferLength:
+ _objc_msgSend$numLoadInfosForSerializedBufferLength:
+ _objc_msgSend$numSegmentsForSerializedBufferLength:
+ _objc_msgSend$showTaskEnergyAsLeafFrame
- +[SATaskState stateWithStackshotTaskV1:machTimebase:hwPageSize:pagesGrabbedTotal:pagesGrabbedIOPLUPL:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
- -[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]
- -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]
- GCC_except_table147
- GCC_except_table166
- GCC_except_table167
- GCC_except_table197
- GCC_except_table211
- GCC_except_table218
- GCC_except_table253
- GCC_except_table261
- GCC_except_table276
- GCC_except_table282
- GCC_except_table308
- GCC_except_table321
- GCC_except_table322
- GCC_except_table329
- GCC_except_table330
- GCC_except_table335
- GCC_except_table336
- GCC_except_table342
- GCC_except_table345
- GCC_except_table548
- GCC_except_table552
- GCC_except_table559
- GCC_except_table564
- GCC_except_table565
- GCC_except_table570
- GCC_except_table574
- GCC_except_table591
- GCC_except_table592
- GCC_except_table596
- _.str.52
- _.str.77
- _.str.78
- _.str.79
- _.str.80
- _SASerializableFillSerializedIndicesWithCollectionOfSerializableInstances
- _SASerializableIndexForPointerFromSerializationDictionary
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1705
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1709
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1706
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1713
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.2184
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2185
- ___123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.2275
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2662
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2684
- ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke
- ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke.1970
- ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_2
- ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_3
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2622
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2631
- ___29-[SASamplePrinter preprocess]_block_invoke.1616
- ___29-[SASamplePrinter preprocess]_block_invoke_2.1617
- ___29-[SASamplePrinter preprocess]_block_invoke_3.1618
- ___29-[SASampleStore gatherTrials]_block_invoke.571
- ___29-[SASampleStore gatherTrials]_block_invoke_2.572
- ___30-[SASamplePrinter printHeader]_block_invoke.1037
- ___30-[SASamplePrinter printHeader]_block_invoke.1503
- ___30-[SASamplePrinter printHeader]_block_invoke.1530
- ___30-[SASamplePrinter printHeader]_block_invoke.1537
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1051
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1504
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1550
- ___31+[SASharedCache addDSCSymData:]_block_invoke.498
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2980
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2985
- ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.653
- ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1646
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1652
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1656
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2234
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2235
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2236
- ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke.1661
- ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_2.1662
- ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.491
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.138
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.140
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke_2
- ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.354
- ___ReadAheadTaskLevelInfo_block_invoke.2076
- ___ReadAheadTaskLevelInfo_block_invoke.2081
- ___ReadAheadTaskLevelInfo_block_invoke.2084
- ___block_descriptor_278_ea8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
- ___block_descriptor_48_ea8_32s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8
- ___block_descriptor_56_ea8_32s40s48r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8r48l8s40l8
- ___block_literal_global.101
- ___block_literal_global.108
- ___block_literal_global.130
- ___block_literal_global.1315
- ___block_literal_global.1506
- ___block_literal_global.1658
- ___block_literal_global.1963
- ___block_literal_global.2064
- ___block_literal_global.2069
- ___block_literal_global.2095
- ___block_literal_global.2108
- ___block_literal_global.2110
- ___block_literal_global.2113
- ___block_literal_global.2158
- ___block_literal_global.2161
- ___block_literal_global.2619
- ___block_literal_global.2634
- ___block_literal_global.2721
- ___block_literal_global.2953
- ___block_literal_global.2982
- ___block_literal_global.337
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.420
- ___block_literal_global.423
- ___block_literal_global.463
- ___block_literal_global.465
- ___block_literal_global.467
- ___block_literal_global.478
- ___block_literal_global.490
- ___block_literal_global.534
- ___block_literal_global.536
- ___block_literal_global.544
- ___block_literal_global.565
- ___block_literal_global.570
- ___block_literal_global.596
- ___block_literal_global.600
- ___block_literal_global.650
- ___block_literal_global.767
CStrings:
+ "%-*s%@Wh\n"
+ "%.0f%s%s"
+ "%.0f%sG%s"
+ "%.0f%sK%s"
+ "%.0f%sM%s"
+ "%.0f%sm%s"
+ "%.0f%sn%s"
+ "%.0f%su%s"
+ "%.2f%s%s"
+ "%.2f%sG%s"
+ "%.2f%sK%s"
+ "%.2f%sM%s"
+ "%.2f%sm%s"
+ "%.2f%sn%s"
+ "%.2f%su%s"
+ "%@B"
+ "%@Wh"
+ "%lld%s%s"
+ "%lld%sK%s"
+ "%s: base size %lu > buffer length %lu"
+ "%s: size %lu implies too many inline frames (%lu)"
+ "%s: size %lu implies too many load infos (%lu)"
+ "%s: size %lu implies too many segments (%lu)"
+ "((void*)(additions + 1)) - ((void*)serializedBinary) <= (long) bufferLength"
+ "C24@0:8Q16"
+ "Energy: "
+ "S24@0:8Q16"
+ "Symbolication during serialization for %@: Got only %u inline frames out of %lu"
+ "Symbolication during serialization for %@: Got only %u loadInfos out of %lu"
+ "Symbolication during serialization for %@: Got only %u segments out of %lu"
+ "Symbolication during serialization for %@: No binary info, not serializing anything"
+ "Symbolication during serialization for %@: No segment info, not serializing anything"
+ "TB,V_showTaskEnergyAsLeafFrame"
+ "TQ,R,V_energyNJ"
+ "_energyNJ"
+ "_onlyCheckedForDsymWhenLastSymbolicated"
+ "_showTaskEnergyAsLeafFrame"
+ "baseSize <= bufferLength"
+ "bufferLength %lu < serialized SATaskState struct v4 with %u donating unique pids"
+ "energyNJ"
+ "energy_nWh"
+ "i < maxNumIndices"
+ "numInlineFrames < UINT8_MAX"
+ "numInlineFramesForSerializedBufferLength:"
+ "numLoadInfos < UINT16_MAX"
+ "numLoadInfosForSerializedBufferLength:"
+ "numSegments < UINT16_MAX"
+ "numSegmentsForSerializedBufferLength:"
+ "setShowTaskEnergyAsLeafFrame:"
+ "showTaskEnergyAsLeafFrame"
+ "v80@?0Q8Q16Q24@\"SATaskState\"32@\"SAThread\"40Q48@\"SAThreadState\"56B64B68^B72"
- "%.0f%s%sB"
- "%.0f%sG%sB"
- "%.0f%sK%sB"
- "%.0f%sM%sB"
- "%.2f%s%sB"
- "%.2f%sG%sB"
- "%.2f%sK%sB"
- "%.2f%sM%sB"
- "%lld%s%sB"
- "%lld%sK%sB"
- "%s: more than %d binaries"
- "%s: more than %d segments"
- "%s: size %lu (%lu segments) > buffer length %lu"
- "((void*)(additions + 1)) - ((void*)serializedBinary) == (long) [self sizeInBytesForSerializedVersion]"
- "WARNING: SAKernelCache %@ got its %lu binaries after starting serialization!"
- "WARNING: SASharedCache %@ got its %lu binaries after starting serialization!"
- "_binaryLoadInfos.count < UINT16_MAX"
- "_segments.count < UINT16_MAX"
- "bufferLength %lu != serialized SAKernelCache struct %lu"
- "bufferLength %lu != serialized SASharedCache struct %lu"
- "bufferLength == sizeof(*serializedKernelCache)"
- "bufferLength >= sizeof(SASerializedSharedCache) + sizeof(SASerializedSharedCache_additions)"
- "i < numIndices"
- "v72@?0Q8Q16@\"SATaskState\"24@\"SAThread\"32Q40@\"SAThreadState\"48B56B60^B64"

```
