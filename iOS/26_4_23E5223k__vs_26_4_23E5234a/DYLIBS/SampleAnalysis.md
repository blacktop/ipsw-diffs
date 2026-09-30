## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

 427.0.0.0.0
-  __TEXT.__text: 0x11c290
+  __TEXT.__text: 0x11c4e8
   __TEXT.__auth_stubs: 0x1770
-  __TEXT.__objc_methlist: 0x63ec
+  __TEXT.__objc_methlist: 0x641c
   __TEXT.__const: 0x368
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x19473
+  __TEXT.__cstring: 0x194a1
   __TEXT.__oslogstring: 0xc707
   __TEXT.__gcc_except_tab: 0x2369c
-  __TEXT.__unwind_info: 0x3fe0
+  __TEXT.__unwind_info: 0x3ff0
   __TEXT.__objc_classname: 0xb54
-  __TEXT.__objc_methname: 0xe8e0
+  __TEXT.__objc_methname: 0xe966
   __TEXT.__objc_methtype: 0x19e8
-  __TEXT.__objc_stubs: 0x8540
+  __TEXT.__objc_stubs: 0x85a0
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x3cd0
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bb8
+  __DATA_CONST.__objc_selrefs: 0x2bd8
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xbd0
   __AUTH_CONST.__const: 0xae0
-  __AUTH_CONST.__cfstring: 0xd920
-  __AUTH_CONST.__objc_const: 0x11248
+  __AUTH_CONST.__cfstring: 0xd960
+  __AUTH_CONST.__objc_const: 0x112a8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x228
   __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xe78
+  __DATA.__objc_ivar: 0xe80
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x30

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EDB8D304-2DCC-33C9-90C1-5A4D55071B54
-  Functions: 2981
-  Symbols:   10999
-  CStrings:  8942
+  UUID: 4801C6DA-F37C-38F5-BF5A-CE98944D0396
+  Functions: 2985
+  Symbols:   11012
+  CStrings:  8954
 
Symbols:
+ -[SACountedState mCore]
+ -[SASamplePrintOptions omitStacksWithMCore]
+ -[SASamplePrintOptions setOmitStacksWithMCore:]
+ -[SASampleStore isMCoreForCPUNum:]
+ GCC_except_table137
+ GCC_except_table147
+ GCC_except_table166
+ GCC_except_table197
+ GCC_except_table211
+ GCC_except_table218
+ GCC_except_table253
+ GCC_except_table261
+ GCC_except_table276
+ GCC_except_table282
+ GCC_except_table308
+ GCC_except_table349
+ GCC_except_table552
+ GCC_except_table556
+ GCC_except_table559
+ GCC_except_table564
+ GCC_except_table569
+ GCC_except_table572
+ GCC_except_table574
+ GCC_except_table578
+ GCC_except_table596
+ GCC_except_table600
+ _.str.163
+ _.str.164
+ _.str.165
+ _.str.166
+ _OBJC_IVAR_$_SACountedState._mCore
+ _OBJC_IVAR_$_SASamplePrintOptions._omitStacksWithMCore
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1719
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1722
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1723
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.2203
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2204
+ ___123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.2294
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2681
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2703
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke.1983
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_2.2021
+ ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_3.2029
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2641
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2650
+ ___29-[SASamplePrinter preprocess]_block_invoke.1626
+ ___29-[SASamplePrinter preprocess]_block_invoke_2.1627
+ ___29-[SASamplePrinter preprocess]_block_invoke_3.1628
+ ___30-[SASamplePrinter printHeader]_block_invoke.1047
+ ___30-[SASamplePrinter printHeader]_block_invoke.1513
+ ___30-[SASamplePrinter printHeader]_block_invoke.1547
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1061
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1514
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1560
+ ___30-[SASamplePrinter printHeader]_block_invoke_3.1063
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2999
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.3004
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1656
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1662
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1666
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2253
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2254
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2255
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke.1671
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_2.1672
+ ___ReadAheadTaskLevelInfo_block_invoke.2083
+ ___ReadAheadTaskLevelInfo_block_invoke.2088
+ ___ReadAheadTaskLevelInfo_block_invoke.2091
+ ___block_descriptor_280_ea8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e74_v80?0Q8Q16Q24"SATaskState"32"SAThread"40Q48"SAThreadState"56B64B68^B72ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
+ ___block_descriptor_312_ea8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8
+ ___block_literal_global.1325
+ ___block_literal_global.1516
+ ___block_literal_global.158
+ ___block_literal_global.1668
+ ___block_literal_global.1970
+ ___block_literal_global.2071
+ ___block_literal_global.2076
+ ___block_literal_global.2102
+ ___block_literal_global.2115
+ ___block_literal_global.2117
+ ___block_literal_global.2132
+ ___block_literal_global.2177
+ ___block_literal_global.2180
+ ___block_literal_global.2638
+ ___block_literal_global.2653
+ ___block_literal_global.2740
+ ___block_literal_global.2972
+ ___block_literal_global.3001
+ ___block_literal_global.347
+ ___block_literal_global.363
+ _objc_msgSend$mCore
+ _objc_msgSend$omitStacksWithMCore
+ _objc_msgSend$setOmitStacksWithMCore:
- GCC_except_table120
- GCC_except_table138
- GCC_except_table168
- GCC_except_table182
- GCC_except_table267
- GCC_except_table278
- GCC_except_table307
- GCC_except_table551
- GCC_except_table554
- GCC_except_table557
- GCC_except_table560
- GCC_except_table567
- GCC_except_table571
- GCC_except_table573
- GCC_except_table576
- GCC_except_table594
- GCC_except_table599
- GCC_except_table87
- _.str.155
- _.str.156
- _.str.157
- _.str.158
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1708
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1712
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1709
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.2196
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2197
- ___123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.2287
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2674
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2696
- ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke.1976
- ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_2.2014
- ___1579-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:energyNJ:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_3.2022
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2634
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2643
- ___29-[SASamplePrinter preprocess]_block_invoke.1619
- ___29-[SASamplePrinter preprocess]_block_invoke_2.1620
- ___29-[SASamplePrinter preprocess]_block_invoke_3.1621
- ___30-[SASamplePrinter printHeader]_block_invoke.1040
- ___30-[SASamplePrinter printHeader]_block_invoke.1506
- ___30-[SASamplePrinter printHeader]_block_invoke.1533
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1054
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1507
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1553
- ___30-[SASamplePrinter printHeader]_block_invoke_3.1056
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2992
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2997
- ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1649
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1655
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1659
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2246
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2247
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2248
- ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke.1664
- ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_2.1665
- ___ReadAheadTaskLevelInfo_block_invoke.2082
- ___ReadAheadTaskLevelInfo_block_invoke.2087
- ___ReadAheadTaskLevelInfo_block_invoke.2090
- ___block_descriptor_279_ea8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e74_v80?0Q8Q16Q24"SATaskState"32"SAThread"40Q48"SAThreadState"56B64B68^B72ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
- ___block_descriptor_311_ea8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8
- ___block_literal_global.1318
- ___block_literal_global.1509
- ___block_literal_global.154
- ___block_literal_global.1661
- ___block_literal_global.1969
- ___block_literal_global.2070
- ___block_literal_global.2075
- ___block_literal_global.2101
- ___block_literal_global.2114
- ___block_literal_global.2116
- ___block_literal_global.2125
- ___block_literal_global.2170
- ___block_literal_global.2173
- ___block_literal_global.2631
- ___block_literal_global.2646
- ___block_literal_global.2733
- ___block_literal_global.2965
- ___block_literal_global.2994
- ___block_literal_global.340
- ___block_literal_global.356
CStrings:
+ "TB,R,V_mCore"
+ "TB,V_omitStacksWithMCore"
+ "_mCore"
+ "_omitStacksWithMCore"
+ "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayCPUSpeedInCallTrees: %d\ndisplayPMICycleIntervalInCallTrees: %d\ndisplayVMFaultAddressAsLeafFrame: %d\ndisplayVMFaultIntervalInCallTrees: %d\ndisplayVMFaultTypeInCallTrees: %d\ndisplayPageGrabIntervalInCallTrees: %d\ndisplayPageGrabTypeInCallTrees: %d\ndisplayPageGrabVMTagInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ndisplayTrialInformation: %d\nrepeatPrimaryStateInCallTrees: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\ntaskAggregation: %llu\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithMCore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\nprintProblematicProcessesAndThreads: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
+ "isMCoreForCPUNum:"
+ "m-core"
+ "mCore"
+ "omitStacksWithMCore"
+ "setOmitStacksWithMCore:"
+ "suspended:%d runnable:%d running:%d ecore:%d mcore:%d pcore:%d cpunum:%d cpuSpeedMhz:%u pmiCycleInterval:%llu vmFaultIntervalPages:%llu vmFaultType:%u vmFaultFlags:%u pageGrabIntervalPages:%llu pageGrabVMTag:%u pageGrabFlags:%u"
- "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayCPUSpeedInCallTrees: %d\ndisplayPMICycleIntervalInCallTrees: %d\ndisplayVMFaultAddressAsLeafFrame: %d\ndisplayVMFaultIntervalInCallTrees: %d\ndisplayVMFaultTypeInCallTrees: %d\ndisplayPageGrabIntervalInCallTrees: %d\ndisplayPageGrabTypeInCallTrees: %d\ndisplayPageGrabVMTagInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ndisplayTrialInformation: %d\nrepeatPrimaryStateInCallTrees: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\ntaskAggregation: %llu\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\nprintProblematicProcessesAndThreads: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
- "suspended:%d runnable:%d running:%d ecore:%d pcore:%d cpunum:%d cpuSpeedMhz:%u pmiCycleInterval:%llu vmFaultIntervalPages:%llu vmFaultType:%u vmFaultFlags:%u pageGrabIntervalPages:%llu pageGrabVMTag:%u pageGrabFlags:%u"

```
