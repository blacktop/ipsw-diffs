## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-347.3.0.0.0
-  __TEXT.__text: 0xd3364
-  __TEXT.__auth_stubs: 0x15a0
-  __TEXT.__objc_methlist: 0x505c
+347.4.0.0.0
+  __TEXT.__text: 0xd46dc
+  __TEXT.__auth_stubs: 0x15d0
+  __TEXT.__objc_methlist: 0x50bc
   __TEXT.__const: 0x168
-  __TEXT.__cstring: 0x14e02
-  __TEXT.__oslogstring: 0xa658
-  __TEXT.__gcc_except_tab: 0x66bc
+  __TEXT.__cstring: 0x1501a
+  __TEXT.__oslogstring: 0xa7df
+  __TEXT.__gcc_except_tab: 0x6720
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x1e94
-  __TEXT.__objc_classname: 0x9c7
-  __TEXT.__objc_methname: 0xbf3e
+  __TEXT.__unwind_info: 0x1eb4
+  __TEXT.__objc_classname: 0x9e4
+  __TEXT.__objc_methname: 0xbf9e
   __TEXT.__objc_methtype: 0x164d
-  __TEXT.__objc_stubs: 0x70a0
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x31b8
-  __DATA_CONST.__objc_classlist: 0x398
+  __TEXT.__objc_stubs: 0x70e0
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x3230
+  __DATA_CONST.__objc_classlist: 0x3a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb4b8
-  __DATA_CONST.__objc_selrefs: 0x24a8
+  __DATA_CONST.__objc_const: 0xb5c0
+  __DATA_CONST.__objc_selrefs: 0x24c8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x490
-  __DATA_CONST.__objc_superrefs: 0x258
+  __DATA_CONST.__objc_classrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__cfstring: 0xa6e0
-  __AUTH_CONST.__objc_const: 0x480
+  __AUTH_CONST.__cfstring: 0xa6c0
+  __AUTH_CONST.__objc_const: 0x4c8
   __AUTH_CONST.__const: 0x680
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH.__objc_data: 0x4b0
-  __DATA.__objc_ivar: 0xb40
+  __AUTH_CONST.__auth_got: 0xb00
+  __AUTH.__objc_data: 0x500
+  __DATA.__objc_ivar: 0xb50
   __DATA.__data: 0x5c4
   __DATA.__thread_vars: 0x48
   __DATA.__crash_info: 0x40

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 79E1B31E-6FB2-321A-A488-E56383C1283C
-  Functions: 2549
-  Symbols:   8601
-  CStrings:  7298
+  UUID: 3F919932-D503-3C8C-9139-DE090509FC8C
+  Functions: 2562
+  Symbols:   8649
+  CStrings:  7318
 
Symbols:
+ -[SASamplePrintOptions callTreeAggregationResolved]
+ -[SASamplePrintOptions setTaskAggregation:]
+ -[SASamplePrintOptions taskAggregation]
+ -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:ioSize:numIOs:isReportHeader:]
+ -[SASamplePrinter displayStringForResourceCoalition:]
+ -[SASampleStore taskForMicrostackshotTask:taskName:loadInfos:numLoadInfos:sharedCache:loadInfosIsPartial:timestamp:architecture:needAOTInfo:isFromCurrentBoot:]
+ -[SATask resourceCoalitionName]
+ -[SATaskAggregationIdentifier .cxx_destruct]
+ -[SATaskAggregationIdentifier copyWithZone:]
+ -[SATaskAggregationIdentifier hash]
+ -[SATaskAggregationIdentifier initWithBinary:sharedCache:rcid:]
+ -[SATaskAggregationIdentifier isEqual:]
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table177
+ GCC_except_table188
+ GCC_except_table208
+ GCC_except_table453
+ GCC_except_table456
+ GCC_except_table459
+ _OBJC_CLASS_$_SATaskAggregationIdentifier
+ _OBJC_IVAR_$_SASamplePrintOptions._taskAggregation
+ _OBJC_IVAR_$_SATask._resourceCoalitionName
+ _OBJC_IVAR_$_SATaskAggregationIdentifier._binary
+ _OBJC_IVAR_$_SATaskAggregationIdentifier._rcid
+ _OBJC_IVAR_$_SATaskAggregationIdentifier._sharedCache
+ _OBJC_METACLASS_$_SATaskAggregationIdentifier
+ _XPC_COALITION_INFO_KEY_BUNDLE_IDENTIFIER
+ _XPC_COALITION_INFO_KEY_NAME
+ __OBJC_$_INSTANCE_METHODS_SATaskAggregationIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_SATaskAggregationIdentifier
+ __OBJC_CLASS_PROTOCOLS_$_SATaskAggregationIdentifier
+ __OBJC_CLASS_RO_$_SATaskAggregationIdentifier
+ __OBJC_METACLASS_RO_$_SATaskAggregationIdentifier
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1225
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1229
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1232
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1226
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1233
+ ___1077-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:ioSize:numIOs:isReportHeader:]_block_invoke
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1588
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1590
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2002
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2010
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2015
+ ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2031
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1962
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1971
+ ___30-[SASamplePrinter printHeader]_block_invoke.1071
+ ___30-[SASamplePrinter printHeader]_block_invoke.1102
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1072
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1115
+ ___37-[SASamplePrinter checkForBadOptions]_block_invoke.349
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1169
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_10
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_2
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_3
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_4
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_5
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_6
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_7
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_8
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke_9
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1176
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_2
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_3
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_4
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_5
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_6
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_7
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_8
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke_9
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1638
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1639
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1640
+ ___52-[SASampleStore gatherUnknownResourceCoalitionNames]_block_invoke
+ ___SAJSONWriteDictionary_block_invoke
+ ___block_descriptor_40_e8_32s_e31_q24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e15_v32?0816^B24lr40l8s32l8
+ ___block_descriptor_57_e8_32s40s48s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8
+ ___block_literal_global.1075
+ ___block_literal_global.1519
+ ___block_literal_global.1562
+ ___block_literal_global.1565
+ ___block_literal_global.1959
+ ___block_literal_global.1974
+ ___block_literal_global.1995
+ ___block_literal_global.2004
+ ___block_literal_global.2062
+ ___block_literal_global.223
+ ___block_literal_global.2296
+ ___block_literal_global.522
+ ___strlcpy_chk
+ __unnamed_array_storage.1654
+ __unnamed_array_storage.2090
+ __unnamed_array_storage.2096
+ __unnamed_array_storage.447
+ __unnamed_array_storage.453
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$resourceCoalitionName
+ _objc_msgSend$setTaskAggregation:
+ _objc_msgSend$taskAggregation
+ _xpc_coalition_copy_info
+ _xpc_dictionary_get_string
- -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionIDs:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:pidStartTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:isTranslocated:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:wqExceededConstrainedThreadLimit:wqExceededTotalThreadLimit:ioSize:numIOs:isReportHeader:]
- -[SASampleStore taskForMicrostackshotTask:loadInfos:numLoadInfos:sharedCache:loadInfosIsPartial:timestamp:architecture:needAOTInfo:isFromCurrentBoot:]
- GCC_except_table106
- GCC_except_table107
- GCC_except_table133
- GCC_except_table135
- GCC_except_table136
- GCC_except_table169
- GCC_except_table180
- GCC_except_table186
- GCC_except_table200
- GCC_except_table452
- GCC_except_table455
- GCC_except_table458
- GCC_except_table51
- _OBJC_IVAR_$_SASamplePrintOptions._aggregateProcessesByExecutable
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1210
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1214
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1217
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1211
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1218
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1572
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1574
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1990
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.1998
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2003
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2019
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1950
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.1959
- ___30-[SASamplePrinter printHeader]_block_invoke.1056
- ___30-[SASamplePrinter printHeader]_block_invoke.1087
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1057
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1100
- ___37-[SASamplePrinter checkForBadOptions]_block_invoke.337
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke.1154
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_10
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_2
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_3
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_4
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_5
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_6
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_7
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_8
- ___38-[SASamplePrinter printTasksByProcess]_block_invoke_9
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke.1161
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_2
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_3
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_4
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_5
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_6
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_7
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_8
- ___41-[SASamplePrinter printTasksByExecutable]_block_invoke_9
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1622
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.1623
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.1624
- ___block_literal_global.1060
- ___block_literal_global.1503
- ___block_literal_global.1546
- ___block_literal_global.1549
- ___block_literal_global.1947
- ___block_literal_global.1962
- ___block_literal_global.1983
- ___block_literal_global.1992
- ___block_literal_global.205
- ___block_literal_global.2050
- ___block_literal_global.2284
- ___block_literal_global.517
- __unnamed_array_storage.1638
- __unnamed_array_storage.2060
- __unnamed_array_storage.2078
- __unnamed_array_storage.435
- __unnamed_array_storage.441
- _objc_msgSend$aggregateProcessesByExecutable
- _objc_msgSend$setAggregateProcessesByExecutable:
CStrings:
+ "\aU\x11\x19\x15"
+ "%*s%s: flags:0x%llx waiter:0x%llx context:0x%llx priority:%d hops:%d portlabel_id:%d%s\n"
+ "%*s%s: flags:0x%llx waiter:0x%llx context:0x%llx priority:%d hops:%d%s\n"
+ "%*s%s: type:0x%x owner:0x%llx waiter:0x%llx context:0x%llx portlabel_id:%d flags:0x%x%s\n"
+ "%*s%s: type:0x%x owner:0x%llx waiter:0x%llx context:0x%llx%s\n"
+ "%llu sample%s %@"
+ "No info for rcid %llu (used by %@ [%d])"
+ "No port label info for id %d from turnstile"
+ "No port label info for id %d from waitinfo"
+ "RCID %llu has bundleid:%s"
+ "RCID %llu has name:%s"
+ "RCID %llu has no bundleid/name"
+ "Resource Coalition: "
+ "SATaskAggregationIdentifier"
+ "TQ,V_taskAggregation"
+ "_options.callTreeAggregationResolved != kSAAggregateCallTreesByProcess"
+ "_options.callTreeAggregationResolved == kSAAggregateCallTreesByDispatchQueue"
+ "_options.swiftAsyncCallTreeAggregationResolved != kSAAggregateSwiftAsyncTogetherWithOtherCallTrees && _options.callTreeAggregationResolved != kSAAggregateCallTreesByProcess"
+ "_rcid"
+ "_resourceCoalitionName"
+ "_taskAggregation"
+ "bufferLength %lu < serialized SATask struct v9 with %u root frames, %u image infos, %u task states, %u threads, %u dispatch queues, %u swift tasks"
+ "bufferLength >= sizeofV9"
+ "conflicting display options: aggregation of multiple task instances requires kSAAggregateCallTreesByProcess"
+ "dictionaryWithObjects:forKeys:count:"
+ "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\ntaskAggregation: %llu\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
+ "q24@?0@\"NSString\"8@\"NSString\"16"
+ "resourceCoalitionName"
+ "resourceCoalitionSampleCounts"
+ "setTaskAggregation:"
+ "swiftAsyncCallTreeAggregationResolved returned default: %s"
+ "taskAggregation"
+ "\x95\x12"
- "\aU)\x15"
- "%-*s%llu"
- ", %llu"
- "No port label info for id %d"
- "Resource Coalition ID: "
- "TB,V_aggregateProcessesByExecutable"
- "_aggregateProcessesByExecutable"
- "_options.callTreeAggregation != kSAAggregateCallTreesByProcess"
- "_options.callTreeAggregation == kSAAggregateCallTreesByDispatchQueue || _options.callTreeAggregation == kSAAggregateCallTreesDefaultBehavior"
- "_options.swiftAsyncCallTreeAggregation != kSAAggregateSwiftAsyncTogetherWithOtherCallTrees && _options.callTreeAggregation != kSAAggregateCallTreesByProcess"
- "conflicting display options: aggregateProcessesByExecutable requires kSAAggregateCallTreesByProcess"
- "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\naggregateProcessesByExecutable: %d\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
- "resourceCoalitionIDs"
- "\xa5\x12"

```
