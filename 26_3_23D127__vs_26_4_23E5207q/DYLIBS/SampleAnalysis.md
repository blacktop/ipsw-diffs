## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-415.0.1.0.0
-  __TEXT.__text: 0xf0180
-  __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0x5e9c
+424.0.0.0.0
+  __TEXT.__text: 0x11a3a4
+  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__objc_methlist: 0x63a4
   __TEXT.__const: 0x358
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x1833c
-  __TEXT.__oslogstring: 0xc5dd
-  __TEXT.__gcc_except_tab: 0x9d64
-  __TEXT.__unwind_info: 0x2118
-  __TEXT.__objc_classname: 0xb34
-  __TEXT.__objc_methname: 0xd955
-  __TEXT.__objc_methtype: 0x1a44
-  __TEXT.__objc_stubs: 0x7de0
-  __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x3b80
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__cstring: 0x19445
+  __TEXT.__oslogstring: 0xc5e0
+  __TEXT.__gcc_except_tab: 0x23210
+  __TEXT.__unwind_info: 0x3f38
+  __TEXT.__objc_classname: 0xb53
+  __TEXT.__objc_methname: 0xe7ac
+  __TEXT.__objc_methtype: 0x19d2
+  __TEXT.__objc_stubs: 0x84a0
+  __DATA_CONST.__got: 0x3f0
+  __DATA_CONST.__const: 0x3c80
+  __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29a0
-  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_selrefs: 0x2b88
+  __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH_CONST.__const: 0xb00
-  __AUTH_CONST.__cfstring: 0xd080
-  __AUTH_CONST.__objc_const: 0x104f0
-  __AUTH_CONST.__objc_intobj: 0x2a0
+  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__const: 0xac0
+  __AUTH_CONST.__cfstring: 0xd7c0
+  __AUTH_CONST.__objc_const: 0x111a8
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x228
-  __AUTH.__objc_data: 0xa0
+  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xd34
+  __DATA.__objc_ivar: 0xe68
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x30
   __DATA.__common: 0x498
-  __DATA_DIRTY.__objc_ivar: 0x48
-  __DATA_DIRTY.__objc_data: 0x2850
+  __DATA_DIRTY.__objc_ivar: 0x10
+  __DATA_DIRTY.__objc_data: 0x2940
   __DATA_DIRTY.__bss: 0x470
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B8177F4D-2B3D-3D15-9633-51352AF133BD
-  Functions: 2829
-  Symbols:   9702
-  CStrings:  8561
+  UUID: C0792FCC-1031-36D4-9C3A-65FE36BCE7DB
+  Functions: 2964
+  Symbols:   10936
+  CStrings:  8904
 
Symbols:
+ +[SABlockingInfo displaysSameContent:other:pid:tid:displayOptions:]
+ +[SACallTreeState treeCountedStateWithBlockingInfos:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:]
+ +[SAKPerfState kperfStateWithSession:petTimerID:]
+ +[SATaskState stateWithStackshotTaskV1:machTimebase:hwPageSize:pagesGrabbedTotal:pagesGrabbedIOPLUPL:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
+ +[SAThreadState stateWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:]
+ +[SAThreadState stateWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:threadPolicyVersion:]
+ +[SAThreadState stateWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:]
+ +[SAThreadState stateWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:threadPolicyVersion:threadInstructionCycles:]
+ +[SAThreadStateMicrostackshot stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:vmFaultAddress:vmFaultIntervalPages:vmFaultType:vmFaultFlags:pageGrabUPLSampleCount:pageGrabIOPLSampleCount:pageGrabIntervalPages:pageGrabVMTag:pageGrabFlags:]
+ +[SAVMRangeLock vmRangeLockWithKCDataVMRL:]
+ +[SAVMRangeLock(Serialization) classDictionaryKey]
+ +[SAVMRangeLock(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ -[SABlockingInfo compare:]
+ -[SABlockingInfo descriptionForPid:tid:threadPriority:options:nameCallback:]
+ -[SABlockingInfo displaysSameContentAs:forPid:tid:displayOptions:]
+ -[SABlockingInfo displaysSomethingForPid:tid:displayOptions:]
+ -[SACallTreeState initWithBlockingInfos:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:]
+ -[SACountedState compare:]
+ -[SACountedState copyWithZone:]
+ -[SACountedState cpuNum]
+ -[SACountedState cpuSpeedMhz]
+ -[SACountedState debugDescription]
+ -[SACountedState eCore]
+ -[SACountedState hasCPUNum]
+ -[SACountedState hash]
+ -[SACountedState initWithThreadState:sampleStore:printOptions:haveAnyOnlyPMIMicrostackshots:pmiCycleIntervalChanges:haveAnyOnlyVMFaultMicrostackshots:vmFaultIntervalChanges:haveAnyOnlyPageGrabMicrostackshots:pageGrabIntervalChanges:]
+ -[SACountedState isEmpty]
+ -[SACountedState isEqual:]
+ -[SACountedState pCore]
+ -[SACountedState pageGrabFlags]
+ -[SACountedState pageGrabIntervalPages]
+ -[SACountedState pageGrabVMTag]
+ -[SACountedState pmiCycleInterval]
+ -[SACountedState runnable]
+ -[SACountedState running]
+ -[SACountedState setCpuNum:]
+ -[SACountedState setPageGrabIntervalPages:]
+ -[SACountedState setVmFaultIntervalPages:]
+ -[SACountedState suspended]
+ -[SACountedState vmFaultFlags]
+ -[SACountedState vmFaultIntervalPages]
+ -[SACountedState vmFaultType]
+ -[SAMicrostackshotStatistics page_grab]
+ -[SAMicrostackshotStatistics vm_fault]
+ -[SASamplePrintOptions displayPageGrabIntervalInCallTrees]
+ -[SASamplePrintOptions displayPageGrabTypeInCallTrees]
+ -[SASamplePrintOptions displayPageGrabVMTagInCallTrees]
+ -[SASamplePrintOptions displayVMFaultAddressAsLeafFrame]
+ -[SASamplePrintOptions displayVMFaultIntervalInCallTrees]
+ -[SASamplePrintOptions displayVMFaultTypeInCallTrees]
+ -[SASamplePrintOptions repeatPrimaryStateInCallTrees]
+ -[SASamplePrintOptions setDisplayPageGrabIntervalInCallTrees:]
+ -[SASamplePrintOptions setDisplayPageGrabTypeInCallTrees:]
+ -[SASamplePrintOptions setDisplayPageGrabVMTagInCallTrees:]
+ -[SASamplePrintOptions setDisplayVMFaultAddressAsLeafFrame:]
+ -[SASamplePrintOptions setDisplayVMFaultIntervalInCallTrees:]
+ -[SASamplePrintOptions setDisplayVMFaultTypeInCallTrees:]
+ -[SASamplePrintOptions setRepeatPrimaryStateInCallTrees:]
+ -[SASamplePrinter addStackHeaderToStream:threadIds:dispatchQueues:swiftTasks:isIdleWorkQueue:threadName:threadNameChanges:count:firstSampleIndex:lastSampleIndex:timeWhenFirstAttemptedToSample:minPriority:maxPriority:minBasePriority:maxBasePriority:cpuTimeNs:cpuInstructions:cpuCycles:isProcessorIdleThread:isGlobalForcedIdleThread:ioSize:numIOs:timeSinceThreadRan:timeSinceThreadWasMadeRunnable:]
+ -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]
+ -[SASamplePrinter compareFrame1:frame2:]
+ -[SASamplePrinter extraSampleCountForThreadState:]
+ -[SASamplePrinter preprocess]
+ -[SASampleStore _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]
+ -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]
+ -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]
+ -[SASampleStore addKCDataThreadV4:threadV2:deltaThreadV3:deltaThreadV2:timestamp:sampleIndex:stack:threadExclavesInfo:threadName:dispatchQueueLabel:waitInfo:waitInfoPortLabelInfo:turnstileInfo:turnstileInfoPortLabelInfo:vmrlsForThread:instructionCycles:task:kernelTask:taskIsSuspended:]
+ -[SASampleStore disconnectMappingsInterval]
+ -[SASampleStore initWithPAStyleCoder:]
+ -[SASampleStore setDisconnectMappingsInterval:]
+ -[SATaskState pagesGrabbedIOPLUPL]
+ -[SATaskState pagesGrabbedTotal]
+ -[SAThreadState blockingInfos]
+ -[SAThreadState initWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:]
+ -[SAThreadState initWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:threadPolicyVersion:]
+ -[SAThreadState initWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:]
+ -[SAThreadState initWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:threadPolicyVersion:threadInstructionCycles:]
+ -[SAThreadState isPageGrabRecord]
+ -[SAThreadState isVMFaultRecord]
+ -[SAThreadState numMicrostackshotTypes]
+ -[SAThreadState pageGrabFlags]
+ -[SAThreadState pageGrabIOPLSampleCount]
+ -[SAThreadState pageGrabIntervalPages]
+ -[SAThreadState pageGrabUPLSampleCount]
+ -[SAThreadState pageGrabVMTag]
+ -[SAThreadState pmiCycleExtraSampleCount]
+ -[SAThreadState setPageGrabIntervalPages:]
+ -[SAThreadState setVmFaultIntervalPages:]
+ -[SAThreadState vmFaultAddress]
+ -[SAThreadState vmFaultExtraSampleCount]
+ -[SAThreadState vmFaultFlags]
+ -[SAThreadState vmFaultIntervalPages]
+ -[SAThreadState vmFaultType]
+ -[SAThreadStateMicrostackshot isPageGrabRecord]
+ -[SAThreadStateMicrostackshot isVMFaultRecord]
+ -[SAThreadStateMicrostackshot numMicrostackshotTypes]
+ -[SAThreadStateMicrostackshot pageGrabFlags]
+ -[SAThreadStateMicrostackshot pageGrabIOPLSampleCount]
+ -[SAThreadStateMicrostackshot pageGrabIntervalPages]
+ -[SAThreadStateMicrostackshot pageGrabUPLSampleCount]
+ -[SAThreadStateMicrostackshot pageGrabVMTag]
+ -[SAThreadStateMicrostackshot pmiCycleExtraSampleCount]
+ -[SAThreadStateMicrostackshot setPageGrabIntervalPages:]
+ -[SAThreadStateMicrostackshot setVmFaultIntervalPages:]
+ -[SAThreadStateMicrostackshot vmFaultAddress]
+ -[SAThreadStateMicrostackshot vmFaultExtraSampleCount]
+ -[SAThreadStateMicrostackshot vmFaultFlags]
+ -[SAThreadStateMicrostackshot vmFaultIntervalPages]
+ -[SAThreadStateMicrostackshot vmFaultType]
+ -[SATurnstileInfo displaysSomethingForPid:tid:displayOptions:]
+ -[SAVMRangeLock blockerAtomic]
+ -[SAVMRangeLock blockerExclusive]
+ -[SAVMRangeLock blockerShared]
+ -[SAVMRangeLock blockerStreaming]
+ -[SAVMRangeLock blockingPid]
+ -[SAVMRangeLock blockingTid]
+ -[SAVMRangeLock debugDescription]
+ -[SAVMRangeLock descriptionForPid:tid:threadPriority:options:nameCallback:]
+ -[SAVMRangeLock displaysSomethingForPid:tid:displayOptions:]
+ -[SAVMRangeLock flags]
+ -[SAVMRangeLock init]
+ -[SAVMRangeLock isEqual:]
+ -[SAVMRangeLock waiterAtomic]
+ -[SAVMRangeLock waiterExclusive]
+ -[SAVMRangeLock waiterShared]
+ -[SAVMRangeLock waiterStreaming]
+ -[SAVMRangeLock(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SAVMRangeLock(Serialization) addSelfToSerializationDictionary:]
+ -[SAVMRangeLock(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SAVMRangeLock(Serialization) sizeInBytesForSerializedVersion]
+ -[SAWaitInfo descriptionForPid:tid:threadPriority:options:nameCallback:]
+ -[SAWaitInfo displaysSomethingForPid:tid:displayOptions:]
+ GCC_except_table1
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table120
+ GCC_except_table121
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table125
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table136
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table145
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table154
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table162
+ GCC_except_table163
+ GCC_except_table164
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table177
+ GCC_except_table179
+ GCC_except_table180
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table185
+ GCC_except_table186
+ GCC_except_table187
+ GCC_except_table188
+ GCC_except_table189
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table2
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table207
+ GCC_except_table208
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table23
+ GCC_except_table230
+ GCC_except_table231
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table239
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table271
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table276
+ GCC_except_table277
+ GCC_except_table278
+ GCC_except_table281
+ GCC_except_table282
+ GCC_except_table283
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table286
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table289
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table292
+ GCC_except_table293
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table297
+ GCC_except_table298
+ GCC_except_table299
+ GCC_except_table30
+ GCC_except_table300
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table305
+ GCC_except_table306
+ GCC_except_table307
+ GCC_except_table308
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table311
+ GCC_except_table312
+ GCC_except_table313
+ GCC_except_table314
+ GCC_except_table315
+ GCC_except_table316
+ GCC_except_table318
+ GCC_except_table319
+ GCC_except_table321
+ GCC_except_table322
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table326
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table337
+ GCC_except_table339
+ GCC_except_table34
+ GCC_except_table340
+ GCC_except_table342
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table356
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table36
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table369
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table379
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table387
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table39
+ GCC_except_table390
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table400
+ GCC_except_table401
+ GCC_except_table50
+ GCC_except_table51
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table548
+ GCC_except_table551
+ GCC_except_table552
+ GCC_except_table554
+ GCC_except_table555
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table565
+ GCC_except_table568
+ GCC_except_table57
+ GCC_except_table570
+ GCC_except_table573
+ GCC_except_table574
+ GCC_except_table59
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table60
+ GCC_except_table8
+ GCC_except_table83
+ GCC_except_table86
+ GCC_except_table97
+ _.str.155
+ _.str.156
+ _.str.157
+ _.str.158
+ _.str.159
+ _.str.160
+ _.str.162
+ _.str.48
+ _.str.52
+ _.str.77
+ _.str.78
+ _.str.79
+ _.str.80
+ _.str.891
+ _.str.96
+ _OBJC_CLASS_$_SACountedState
+ _OBJC_CLASS_$_SAVMRangeLock
+ _OBJC_IVAR_$_SACallTreeState._blockingInfos
+ _OBJC_IVAR_$_SACallTreeState._pageGrabIOPLSampleCount
+ _OBJC_IVAR_$_SACallTreeState._pageGrabUPLSampleCount
+ _OBJC_IVAR_$_SACallTreeStateChildren._originPid
+ _OBJC_IVAR_$_SACallTreeStateChildren._proximatePid
+ _OBJC_IVAR_$_SACountedState._cpuNumOffByOne
+ _OBJC_IVAR_$_SACountedState._cpuSpeedMhz
+ _OBJC_IVAR_$_SACountedState._eCore
+ _OBJC_IVAR_$_SACountedState._pCore
+ _OBJC_IVAR_$_SACountedState._pageGrabFlags
+ _OBJC_IVAR_$_SACountedState._pageGrabIntervalPages
+ _OBJC_IVAR_$_SACountedState._pageGrabVMTag
+ _OBJC_IVAR_$_SACountedState._pmiCycleInterval
+ _OBJC_IVAR_$_SACountedState._runnable
+ _OBJC_IVAR_$_SACountedState._running
+ _OBJC_IVAR_$_SACountedState._suspended
+ _OBJC_IVAR_$_SACountedState._vmFaultFlags
+ _OBJC_IVAR_$_SACountedState._vmFaultIntervalPages
+ _OBJC_IVAR_$_SACountedState._vmFaultType
+ _OBJC_IVAR_$_SAMicrostackshotStatistics._page_grab
+ _OBJC_IVAR_$_SAMicrostackshotStatistics._vm_fault
+ _OBJC_IVAR_$_SASamplePrintOptions._displayPageGrabIntervalInCallTrees
+ _OBJC_IVAR_$_SASamplePrintOptions._displayPageGrabTypeInCallTrees
+ _OBJC_IVAR_$_SASamplePrintOptions._displayPageGrabVMTagInCallTrees
+ _OBJC_IVAR_$_SASamplePrintOptions._displayVMFaultAddressAsLeafFrame
+ _OBJC_IVAR_$_SASamplePrintOptions._displayVMFaultIntervalInCallTrees
+ _OBJC_IVAR_$_SASamplePrintOptions._displayVMFaultTypeInCallTrees
+ _OBJC_IVAR_$_SASamplePrintOptions._repeatPrimaryStateInCallTrees
+ _OBJC_IVAR_$_SASamplePrinter._countedStateCache
+ _OBJC_IVAR_$_SASamplePrinter._extraSampleCount
+ _OBJC_IVAR_$_SASamplePrinter._extraSampleCountForTask
+ _OBJC_IVAR_$_SASamplePrinter._haveAnyOnlyPMIMicrostackshots
+ _OBJC_IVAR_$_SASamplePrinter._haveAnyOnlyPageGrabMicrostackshots
+ _OBJC_IVAR_$_SASamplePrinter._haveAnyOnlyVMFaultMicrostackshots
+ _OBJC_IVAR_$_SASamplePrinter._numSamplesWhenLastPreprocessed
+ _OBJC_IVAR_$_SASamplePrinter._pageGrabIntervalPagesMax
+ _OBJC_IVAR_$_SASamplePrinter._pageGrabIntervalPagesMin
+ _OBJC_IVAR_$_SASamplePrinter._pageGrabTypeCounts
+ _OBJC_IVAR_$_SASamplePrinter._pageGrabTypeCountsByTask
+ _OBJC_IVAR_$_SASamplePrinter._pageGrabVMTagCounts
+ _OBJC_IVAR_$_SASamplePrinter._pageGrabVMTagCountsByTask
+ _OBJC_IVAR_$_SASamplePrinter._pmiCycleIntervalMax
+ _OBJC_IVAR_$_SASamplePrinter._pmiCycleIntervalMin
+ _OBJC_IVAR_$_SASamplePrinter._vmFaultIntervalPagesMax
+ _OBJC_IVAR_$_SASamplePrinter._vmFaultIntervalPagesMin
+ _OBJC_IVAR_$_SASamplePrinter._vmFaultTypeCounts
+ _OBJC_IVAR_$_SASamplePrinter._vmFaultTypeCountsByTask
+ _OBJC_IVAR_$_SASampleStore._disconnectMappingsInterval
+ _OBJC_IVAR_$_SASampleStore._lastMicrostackshotSampleCount
+ _OBJC_IVAR_$_SASampleStore._lastMicrostackshotWallTime
+ _OBJC_IVAR_$_SASampleStore._numMicrostackshotsLost
+ _OBJC_IVAR_$_SASampleStore._pageGrabIntervalPagesMostRecent
+ _OBJC_IVAR_$_SASampleStore._vmFaultIntervalPagesMostRecent
+ _OBJC_IVAR_$_SAStack._sampleCount
+ _OBJC_IVAR_$_SATaskState._pagesGrabbedIOPLUPL
+ _OBJC_IVAR_$_SATaskState._pagesGrabbedTotal
+ _OBJC_IVAR_$_SAThreadCallTree._dispatchQueue
+ _OBJC_IVAR_$_SAThreadCallTree._swiftTask
+ _OBJC_IVAR_$_SAThreadCallTree._thread
+ _OBJC_IVAR_$_SAThreadState._blockingInfos
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._cpuSpeed100Mhz
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._microstackshotFlags
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._pageGrabFlags
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._pageGrabIOPLSampleCount
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._pageGrabIntervalPages
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._pageGrabUPLSampleCount
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._pageGrabVMTag
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._pmiCycleInterval
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._vmFaultAddress
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._vmFaultFlags
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._vmFaultIntervalPages
+ _OBJC_IVAR_$_SAThreadStateMicrostackshot._vmFaultType
+ _OBJC_IVAR_$_SATurnstileInfoWithPortLabel._portDomain
+ _OBJC_IVAR_$_SATurnstileInfoWithPortLabel._portFlags
+ _OBJC_IVAR_$_SATurnstileInfoWithPortLabel._portName
+ _OBJC_IVAR_$_SAVMRangeLock._blockerAtomic
+ _OBJC_IVAR_$_SAVMRangeLock._blockerExclusive
+ _OBJC_IVAR_$_SAVMRangeLock._blockerShared
+ _OBJC_IVAR_$_SAVMRangeLock._blockerStreaming
+ _OBJC_IVAR_$_SAVMRangeLock._blockingTid
+ _OBJC_IVAR_$_SAVMRangeLock._flags
+ _OBJC_IVAR_$_SAVMRangeLock._waiterAtomic
+ _OBJC_IVAR_$_SAVMRangeLock._waiterExclusive
+ _OBJC_IVAR_$_SAVMRangeLock._waiterShared
+ _OBJC_IVAR_$_SAVMRangeLock._waiterStreaming
+ _OBJC_IVAR_$_SAWaitInfoWithPortLabel._portDomain
+ _OBJC_IVAR_$_SAWaitInfoWithPortLabel._portFlags
+ _OBJC_IVAR_$_SAWaitInfoWithPortLabel._portName
+ _OBJC_METACLASS_$_SACountedState
+ _OBJC_METACLASS_$_SAVMRangeLock
+ _SACopyStringForPageGrabType
+ _SACopyStringForVMFaultType
+ _SAFormattedBytesDoubleEx
+ __OBJC_$_CLASS_METHODS_SAVMRangeLock(Serialization)
+ __OBJC_$_INSTANCE_METHODS_SACountedState
+ __OBJC_$_INSTANCE_METHODS_SAVMRangeLock(Serialization)
+ __OBJC_$_INSTANCE_VARIABLES_SACountedState
+ __OBJC_$_INSTANCE_VARIABLES_SAVMRangeLock
+ __OBJC_$_PROP_LIST_SACountedState
+ __OBJC_CLASS_PROTOCOLS_$_SACountedState
+ __OBJC_CLASS_PROTOCOLS_$_SAVMRangeLock(Serialization)
+ __OBJC_CLASS_RO_$_SACountedState
+ __OBJC_CLASS_RO_$_SAVMRangeLock
+ __OBJC_METACLASS_RO_$_SACountedState
+ __OBJC_METACLASS_RO_$_SAVMRangeLock
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1705
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1709
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1712
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1706
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1713
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_6
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_7
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_8
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_9
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.2184
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2185
+ ___116-[SASampleStore(KPerf) addLoadInfoFromKTrace:lastKTraceEventTimestamp:checkForNewLoadInfosEvenWithExistingLoadInfo:]_block_invoke.192
+ ___123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.2275
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke.162
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke.167
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_10
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_11
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_12
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_13
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_14
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_15
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_16
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_2
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_2.163
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_2.168
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_3
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_3.171
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_4
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_4.172
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_5
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_6
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_7
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_8
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:kperfState:ktraceDataUnavailable:]_block_invoke_9
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2662
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2684
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke.318
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke.320
+ ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_2.321
+ ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke
+ ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke.1970
+ ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_2
+ ___1570-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numFaults:numPageins:numPagesGrabbedTotal:numPagesGrabbedIOPLUPL:vmFaultTypeCounts:pageGrabTypeCounts:pageGrabVMTagCounts:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke_3
+ ___23+[SABinary clearCaches]_block_invoke.97
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2622
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2631
+ ___28-[SASampleStore postprocess]_block_invoke.222
+ ___28-[SASampleStore postprocess]_block_invoke_2.223
+ ___28-[SASampleStore postprocess]_block_invoke_3.226
+ ___28-[SASampleStore symbolicate]_block_invoke.527
+ ___29-[SASamplePrinter preprocess]_block_invoke.1616
+ ___29-[SASamplePrinter preprocess]_block_invoke_2.1617
+ ___29-[SASamplePrinter preprocess]_block_invoke_3.1618
+ ___29-[SASamplePrinter preprocess]_block_invoke_4
+ ___29-[SASampleStore gatherTrials]_block_invoke.571
+ ___29-[SASampleStore gatherTrials]_block_invoke_2.572
+ ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
+ ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke.367
+ ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke.377
+ ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke.381
+ ___292-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_2
+ ___30-[SASamplePrinter printHeader]_block_invoke.1037
+ ___30-[SASamplePrinter printHeader]_block_invoke.1503
+ ___30-[SASamplePrinter printHeader]_block_invoke.1530
+ ___30-[SASamplePrinter printHeader]_block_invoke.1537
+ ___30-[SASamplePrinter printHeader]_block_invoke_10
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1051
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1504
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1550
+ ___30-[SASamplePrinter printHeader]_block_invoke_3.1056
+ ___30-[SASamplePrinter printHeader]_block_invoke_8
+ ___30-[SASamplePrinter printHeader]_block_invoke_9
+ ___31+[SASharedCache addDSCSymData:]_block_invoke.498
+ ___32-[SASegment addTailspinSymbols:]_block_invoke.29
+ ___34-[SASegment addInfoFromCSSegment:]_block_invoke.38
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_2
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_3
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_4
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_5
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_6
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_7
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_8
+ ___356-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:vmrls:exclaveInfo:]_block_invoke_9
+ ___37-[SASamplePrinter checkForBadOptions]_block_invoke_2
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2980
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2985
+ ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.653
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1646
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1652
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1656
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2234
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2235
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2236
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke.1661
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_2.1662
+ ___51-[SASamplePrinter printTaskHeaderForMultipleTasks:]_block_invoke_3
+ ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.358
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke.502
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke.506
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke_2
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke_3
+ ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke_4
+ ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.491
+ ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.138
+ ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.354
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.221
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.233
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.259
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.278
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.292
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.311
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.322
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.270
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.285
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.296
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.314
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.328
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.309
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.317
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_4.318
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_5.321
+ ___99-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:ktraceDataUnavailable:]_block_invoke.403
+ ___ReadAheadTaskLevelInfo_block_invoke.2076
+ ___ReadAheadTaskLevelInfo_block_invoke.2081
+ ___ReadAheadTaskLevelInfo_block_invoke.2084
+ ___SAKCDataReadAheadVMRL_block_invoke
+ ___block_descriptor_101_ea8_32s40r48r_e23_v16?0^{dyld_image_s=}8lr40l8r48l8s32l8
+ ___block_descriptor_105_ea8_32s40s48s56s64r72r80r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr64l8s32l8s40l8r72l8r80l8s48l8s56l8
+ ___block_descriptor_129_ea8_32s40s48s56s64s72s80r88r96r104r112r120r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8r80l8r88l8r96l8r104l8r112l8r120l8s64l8s72l8
+ ___block_descriptor_149_ea8_32s40s48s56s64s72s80s_e51_v20?0I8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}12ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_184_ea8_32s40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r_e28_v32?0"SATaskState"8Q16^B24ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8
+ ___block_descriptor_198_ea8_32s40s48s56s64s72r80r88r96r104r112r120r128r136r144r152r_e15_v28?08I16^B20lr72l8r80l8r88l8r96l8s32l8r104l8r112l8s40l8r120l8r128l8r136l8r144l8r152l8s48l8s56l8s64l8
+ ___block_descriptor_278_ea8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
+ ___block_descriptor_311_ea8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8
+ ___block_descriptor_40_ea8_32bs_e15_v28?08I16^B20ls32l8
+ ___block_descriptor_40_ea8_32bs_e20_v24?0"SATask"8^B16ls32l8
+ ___block_descriptor_40_ea8_32bs_e22_v24?0{_CSTypeRef=QQ}8ls32l8
+ ___block_descriptor_40_ea8_32bs_e24_v32?0"SAFrame"8Q16^B24ls32l8
+ ___block_descriptor_40_ea8_32bs_e34_v24?0"SADispatchQueueState"8^B16ls32l8
+ ___block_descriptor_40_ea8_32bs_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8
+ ___block_descriptor_40_ea8_32bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8
+ ___block_descriptor_40_ea8_32bs_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
+ ___block_descriptor_40_ea8_32bs_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8
+ ___block_descriptor_40_ea8_32bs_e59_v48?0{_CSRange=QQ}8^{_CSTypeRef=QQ}24^{_CSTypeRef=QQ}32Q40ls32l8
+ ___block_descriptor_40_ea8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_ea8_32r_e20_v24?0"SATask"8^B16lr32l8
+ ___block_descriptor_40_ea8_32r_e24_v16?0"NSMutableArray"8lr32l8
+ ___block_descriptor_40_ea8_32r_e24_v32?0"SAFrame"8Q16^B24lr32l8
+ ___block_descriptor_40_ea8_32r_e28_v32?0"SATaskState"8Q16^B24lr32l8
+ ___block_descriptor_40_ea8_32r_e29_v16?0"NSMutableDictionary"8lr32l8
+ ___block_descriptor_40_ea8_32r_e30_v32?0"SAThreadState"8Q16^B24lr32l8
+ ___block_descriptor_40_ea8_32r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8
+ ___block_descriptor_40_ea8_32r_e39_v32?0"NSUUID"8"NSMutableArray"16^B24lr32l8
+ ___block_descriptor_40_ea8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_ea8_32s_e13_v20?0I8r^Q12ls32l8
+ ___block_descriptor_40_ea8_32s_e21_q16?0"SATaskState"8ls32l8
+ ___block_descriptor_40_ea8_32s_e21_v16?0"SATimestamp"8ls32l8
+ ___block_descriptor_40_ea8_32s_e23_q16?0"SARecipeState"8ls32l8
+ ___block_descriptor_40_ea8_32s_e23_q16?0"SAThreadState"8ls32l8
+ ___block_descriptor_40_ea8_32s_e24_v16?0"NSMutableArray"8ls32l8
+ ___block_descriptor_40_ea8_32s_e26_v16?0"SABinaryLoadInfo"8ls32l8
+ ___block_descriptor_40_ea8_32s_e29_q24?0"SAStack"8"SAStack"16ls32l8
+ ___block_descriptor_40_ea8_32s_e29_v32?08"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e30_v32?0"NSUUID"8"NSURL"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e30_v32?0"SAThreadState"8Q16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e31_q24?0"NSString"8"NSString"16ls32l8
+ ___block_descriptor_40_ea8_32s_e34_v24?0"SADispatchQueueState"8^B16ls32l8
+ ___block_descriptor_40_ea8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e38_v32?0"NSNumber"8"SASwiftTask"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8
+ ___block_descriptor_40_ea8_32s_e39_v32?0"NSNumber"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e40_v24?0"TRIRolloutAllocationStatus"8^B16ls32l8
+ ___block_descriptor_40_ea8_32s_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e42_v32?0"NSNumber"8"SADispatchQueue"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e43_q24?0"SACallTreeNode"8"SACallTreeNode"16ls32l8
+ ___block_descriptor_40_ea8_32s_e43_v24?0"TRIExperimentAllocationStatus"8^B16ls32l8
+ ___block_descriptor_40_ea8_32s_e44_v20?0I8r^{jetsam_coalition_snapshot=QQQQ}12ls32l8
+ ___block_descriptor_40_ea8_32s_e44_v32?0"NSUUID"8"SAUUIDToSymbolicate"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
+ ___block_descriptor_40_ea8_32s_e47_v20?0I8r^{exclave_textlayout_segment=[16C]Q}12ls32l8
+ ___block_descriptor_40_ea8_32s_e48_v32?0"NSNumber"8"SADependencyGraphNode"16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e55_v20?0I8r^{stackshot_vmrl_blocking_relationship=QQQI}12ls32l8
+ ___block_descriptor_40_ea8_32s_e57_v40?0"NSString"8"NSString"16"NSString"24"NSString"32ls32l8
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_41_ea8_32bs_e28_v32?0"SATaskState"8Q16^B24ls32l8
+ ___block_descriptor_41_ea8_32bs_e30_v32?0"SAThreadState"8Q16^B24ls32l8
+ ___block_descriptor_41_ea8_32r_e30_v32?0"SAThreadState"8Q16^B24lr32l8
+ ___block_descriptor_41_ea8_32r_e35_v32?0"NSString"8"NSString"16^B24lr32l8
+ ___block_descriptor_45_ea8_32bs_e24_v32?0"SAFrame"8Q16^B24ls32l8
+ ___block_descriptor_48_ea8_32bs40bs_e15_v28?08I16^B20ls32l8s40l8
+ ___block_descriptor_48_ea8_32bs_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
+ ___block_descriptor_48_ea8_32r40r_e27_v24?0"SAInstruction"8^B16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e29_v24?0"SAMountSnapshot"8^B16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e34_v24?0"SADispatchQueueState"8^B16lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e35_v32?0"NSNumber"8"NSNumber"16^B24lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8r40l8
+ ___block_descriptor_48_ea8_32r40r_e41_v32?0"SACountedState"8"NSNumber"16^B24lr32l8r40l8
+ ___block_descriptor_48_ea8_32r_e20_v24?0"SATask"8^B16lr32l8
+ ___block_descriptor_48_ea8_32s40bs_e20_v24?0"SATask"8^B16ls40l8s32l8
+ ___block_descriptor_48_ea8_32s40bs_e30_v32?0"SAThreadState"8Q16^B24ls40l8s32l8
+ ___block_descriptor_48_ea8_32s40bs_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40bs_e8_B16?0Q8ls40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e15_v32?0r*8Q16Q24ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e17_v16?0"SAFrame"8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e20_v24?0"SATask"8^B16ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e22_v24?0{_CSTypeRef=QQ}8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e23_i48?0r*8r*16r*24Q32Q40lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e24_v16?0"NSMutableArray"8ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e25_v32?0"NSString"816^B24lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e28_v32?0"SATaskState"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e28_v32?0"SATimestamp"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e29_v16?0"NSMutableDictionary"8lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e35_v32?0"NSNumber"8"SAThread"16^B24lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e8_v12?0i8ls32l8r40l8
+ ___block_descriptor_48_ea8_32s40s_e16_v16?0"SATask"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e20_v24?0"SATask"8^B16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e21_"NSString"20?0i8Q12ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e27_q24?0"SATask"8"SATask"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e27_v28?0"SABinary"8i16B20B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e29_q24?0"NSArray"8"NSArray"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e34_v32?0"SABinary"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e35_v24?0"SASymbol"8"SASourceInfo"16ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e38_v32?0"NSNumber"8"SASwiftTask"16^B24ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e5_q8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e8_q12?0B8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40s_e8_q16?0Q8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s_e15_v16?0"NSSet"8ls32l8
+ ___block_descriptor_48_ea8_32s_e18_q16?0"SASymbol"8ls32l8
+ ___block_descriptor_48_ea8_32s_e26_i48?0[16C]8r*16r*24Q32Q40ls32l8
+ ___block_descriptor_48_ea8_32s_e29_v16?0"NSMutableDictionary"8ls32l8
+ ___block_descriptor_48_ea8_32s_e30_v32?0"SARecipeState"8Q16^B24ls32l8
+ ___block_descriptor_48_ea8_32s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8
+ ___block_descriptor_48_ea8_32s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8
+ ___block_descriptor_48_ea8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
+ ___block_descriptor_48_ea8_32s_e50_v32?0"SAOnBehalfOfSingle"8"NSMutableData"16^B24ls32l8
+ ___block_descriptor_49_ea8_32s40bs_e20_v16?0"SAHIDEvent"8ls32l8s40l8
+ ___block_descriptor_49_ea8_32s40bs_e20_v24?0"SATask"8^B16ls32l8s40l8
+ ___block_descriptor_49_ea8_32s40bs_e24_v32?0"SAFrame"8Q16^B24ls40l8s32l8
+ ___block_descriptor_49_ea8_32s40r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8
+ ___block_descriptor_49_ea8_32s40r_e47_v40?0"NSString"8"NSString"16"NSArray"24^B32ls32l8r40l8
+ ___block_descriptor_49_ea8_32s40s_e15_v32?0r*8Q16Q24ls32l8s40l8
+ ___block_descriptor_50_ea8_32s40s_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8s40l8
+ ___block_descriptor_50_ea8_32s_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
+ ___block_descriptor_52_ea8_32bs40r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr40l8s32l8
+ ___block_descriptor_52_ea8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_52_ea8_32r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr32l8
+ ___block_descriptor_52_ea8_32s40r_e23_v16?0^{dyld_image_s=}8ls32l8r40l8
+ ___block_descriptor_56_ea8_32bs40r_e18_v36?0r*8Q16Q24i32lr40l8s32l8
+ ___block_descriptor_56_ea8_32bs40r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8r40l8
+ ___block_descriptor_56_ea8_32bs_e22_v24?0{_CSTypeRef=QQ}8ls32l8
+ ___block_descriptor_56_ea8_32r40r48r_e57_v40?0"NSString"8"NSString"16"NSString"24"NSString"32lr32l8r40l8r48l8
+ ___block_descriptor_56_ea8_32r40r_e16_v32?0r^v8Q16Q24lr32l8r40l8
+ ___block_descriptor_56_ea8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_56_ea8_32r40r_e9_v16?0r*8lr32l8r40l8
+ ___block_descriptor_56_ea8_32r_e15_v32?0816^B24lu40l8u48l8r32l8
+ ___block_descriptor_56_ea8_32r_e15_v32?0r*8Q16Q24lr32l8
+ ___block_descriptor_56_ea8_32r_e22_v24?0{_CSTypeRef=QQ}8lr32l8
+ ___block_descriptor_56_ea8_32s40bs_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40r48r_e20_v24?0"SATask"8^B16ls32l8r40l8r48l8
+ ___block_descriptor_56_ea8_32s40r48r_e22_v24?0{_CSTypeRef=QQ}8lr40l8r48l8s32l8
+ ___block_descriptor_56_ea8_32s40r48r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8r48l8
+ ___block_descriptor_56_ea8_32s40r_e20_v24?0"SATask"8^B16ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40r_e25_v20?0"NSDictionary"8B16ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
+ ___block_descriptor_56_ea8_32s40r_e38_v32?0"SASymbol"8"SASourceInfo"16Q24lr40l8s32l8
+ ___block_descriptor_56_ea8_32s40r_e5_v8?0lu48l8r40l8s32l8
+ ___block_descriptor_56_ea8_32s40s48bs_e30_v32?0"SAThreadState"8Q16^B24ls32l8s48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48r_e16_v16?0"SATask"8ls32l8r48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48r_e19_v20?0"SATask"8B16ls32l8s40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48r_e20_v24?0"SATask"8^B16ls32l8r48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48r_e20_v24?0"SATask"8^B16ls32l8s40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48r_e23_v16?0^{dyld_image_s=}8lr48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48r_e35_v32?0"NSNumber"8"SAThread"16^B24lr48l8s32l8s40l8
+ ___block_descriptor_56_ea8_32s40s48r_e54_v40?0"NSSet"8"NSSet"16"NSString"24"SATimestamp"32ls32l8s40l8r48l8
+ ___block_descriptor_56_ea8_32s40s48r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8r48l8s40l8
+ ___block_descriptor_56_ea8_32s40s48s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e28_v32?0"SATaskState"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e30_v24?0"SASwiftTaskState"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e5_q8?0ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e8_q12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s48s_e8_q16?0Q8ls32l8s40l8s48l8
+ ___block_descriptor_56_ea8_32s40s_e19_v20?0"SATask"8B16ls32l8s40l8
+ ___block_descriptor_56_ea8_32s40s_e21_v16?0"SATimestamp"8ls32l8s40l8
+ ___block_descriptor_56_ea8_32s_e25_Q32?0{_CSTypeRef=QQ}8Q24ls32l8
+ ___block_descriptor_56_ea8_32s_e29_v16?0"NSMutableDictionary"8ls32l8
+ ___block_descriptor_57_ea8_32s40s48bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls48l8s32l8s40l8
+ ___block_descriptor_58_ea8_32s_e22_v24?0{_CSTypeRef=QQ}8ls32l8
+ ___block_descriptor_60_ea8_32s40s48s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32bs40r48r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr40l8r48l8s32l8
+ ___block_descriptor_64_ea8_32r40r48r56r_e20_v24?0"SATask"8^B16lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32r40r48r56r_e22_v24?0{_CSTypeRef=QQ}8lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32r40r48r56r_e25_i16?0^{__CFDictionary=}8lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32r40r48r56r_e35_v24?0"SASymbol"8"SASourceInfo"16lr32l8r40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32r40r_e22_v24?0{_CSTypeRef=QQ}8lr32l8r40l8
+ ___block_descriptor_64_ea8_32r40r_e23_i48?0r*8r*16r*24Q32Q40lr32l8r40l8
+ ___block_descriptor_64_ea8_32r40r_e30_v16?0^{dyld_shared_cache_s=}8lr32l8r40l8
+ ___block_descriptor_64_ea8_32s40bs48r_e29_v24?0"SAMountSnapshot"8^B16ls40l8s32l8r48l8
+ ___block_descriptor_64_ea8_32s40r48r56r_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8r40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e16_v28?0Q8r^Q16I24lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_ea8_32s40s48r_e29_v16?0"NSMutableDictionary"8ls32l8s40l8r48l8
+ ___block_descriptor_64_ea8_32s40s48r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8r48l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56r_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e23_v16?0"SAThreadState"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e24_v24?0r^{?=QQQQQQII}8Q16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e48_v32?0"NSNumber"8"SADependencyGraphNode"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_ea8_32s40s48s_e13_v20?0I8r^Q12ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s40s48s_e42_v32?0"NSNumber"8"SADispatchQueue"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32s_e22_v24?0{_CSTypeRef=QQ}8ls32l8
+ ___block_descriptor_65_ea8_32s40s48r56r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r48l8r56l8s40l8
+ ___block_descriptor_65_ea8_32s40s48s56bs_e21_v16?0"SATimeRange"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_ea8_32s40s48s56s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_ea8_32s40s48s_e21_v16?0"SATimestamp"8ls32l8s40l8s48l8
+ ___block_descriptor_66_ea8_32s40s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8
+ ___block_descriptor_69_ea8_32r40r48r56r_e8_v12?0i8lr32l8r40l8r48l8r56l8
+ ___block_descriptor_72_ea8_32r40r48r56r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8r40l8r48l8r56l8
+ ___block_descriptor_72_ea8_32s40r48r56r64r_e15_v32?0r*8Q16Q24ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_72_ea8_32s40s48r56r64r_e20_v24?0"SATask"8^B16ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_72_ea8_32s40s48r_e29_v16?0"NSMutableDictionary"8ls32l8r48l8s40l8
+ ___block_descriptor_72_ea8_32s40s48s56s64r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48s56s64r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_72_ea8_32s40s48s56s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s_e25_v32?0"SAThread"8Q16^B24ls32l8s40l8
+ ___block_descriptor_72_ea8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
+ ___block_descriptor_72_ea8_32s40s_e40_v32?0"NSNumber"8"SAInstruction"16^B24ls32l8s40l8
+ ___block_descriptor_73_ea8_32s40s48s56r64r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_80_ea8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
+ ___block_descriptor_80_ea8_32s40s48s56s64s72s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_ea8_32s40r48r56r64r72r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_81_ea8_32s40s48s56s64r72r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_81_ea8_32s40s48s56s64s72s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_ea8_32s40s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8
+ ___block_descriptor_88_ea8_32s40s48s56s64s72s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_ea8_32s40s48s56s64s_e13_v20?0I8r^Q12ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_96_ea8_32s40r48r56r64r72r80r_e39_v40?0{_CSTypeRef=QQ}8{_CSTypeRef=QQ}24lr40l8s32l8r48l8r56l8r64l8r72l8r80l8
+ ___block_literal_global.100
+ ___block_literal_global.101
+ ___block_literal_global.109
+ ___block_literal_global.125
+ ___block_literal_global.130
+ ___block_literal_global.1315
+ ___block_literal_global.149
+ ___block_literal_global.1506
+ ___block_literal_global.154
+ ___block_literal_global.1658
+ ___block_literal_global.188
+ ___block_literal_global.194
+ ___block_literal_global.1963
+ ___block_literal_global.2064
+ ___block_literal_global.2069
+ ___block_literal_global.207
+ ___block_literal_global.2095
+ ___block_literal_global.210
+ ___block_literal_global.2108
+ ___block_literal_global.2110
+ ___block_literal_global.2113
+ ___block_literal_global.2158
+ ___block_literal_global.2161
+ ___block_literal_global.231
+ ___block_literal_global.233
+ ___block_literal_global.235
+ ___block_literal_global.260
+ ___block_literal_global.2619
+ ___block_literal_global.262
+ ___block_literal_global.2634
+ ___block_literal_global.2721
+ ___block_literal_global.292
+ ___block_literal_global.2953
+ ___block_literal_global.2982
+ ___block_literal_global.313
+ ___block_literal_global.316
+ ___block_literal_global.330
+ ___block_literal_global.337
+ ___block_literal_global.353
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.369
+ ___block_literal_global.420
+ ___block_literal_global.423
+ ___block_literal_global.463
+ ___block_literal_global.465
+ ___block_literal_global.467
+ ___block_literal_global.478
+ ___block_literal_global.490
+ ___block_literal_global.500
+ ___block_literal_global.508
+ ___block_literal_global.529
+ ___block_literal_global.534
+ ___block_literal_global.536
+ ___block_literal_global.544
+ ___block_literal_global.565
+ ___block_literal_global.570
+ ___block_literal_global.596
+ ___block_literal_global.600
+ ___block_literal_global.650
+ ___block_literal_global.767
+ __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:vmrls:exclaveInfo:.next_fake_unique_pid
+ _inflate
+ _inflateEnd
+ _inflateInit_
+ _kcdata_iter_array_elem_size
+ _objc_msgSend$arrayByAddingObject:
+ _objc_msgSend$blockingInfos
+ _objc_msgSend$dataWithBytesNoCopy:length:
+ _objc_msgSend$disconnectMappingsInterval
+ _objc_msgSend$displayPageGrabIntervalInCallTrees
+ _objc_msgSend$displayPageGrabTypeInCallTrees
+ _objc_msgSend$displayPageGrabVMTagInCallTrees
+ _objc_msgSend$displayVMFaultAddressAsLeafFrame
+ _objc_msgSend$displayVMFaultIntervalInCallTrees
+ _objc_msgSend$displayVMFaultTypeInCallTrees
+ _objc_msgSend$displaysSomethingForPid:tid:displayOptions:
+ _objc_msgSend$eCore
+ _objc_msgSend$hasCPUNum
+ _objc_msgSend$initWithBlockingInfos:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:
+ _objc_msgSend$initWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:
+ _objc_msgSend$initWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:threadPolicyVersion:
+ _objc_msgSend$initWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:
+ _objc_msgSend$initWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:threadPolicyVersion:threadInstructionCycles:
+ _objc_msgSend$initWithThreadState:sampleStore:printOptions:haveAnyOnlyPMIMicrostackshots:pmiCycleIntervalChanges:haveAnyOnlyVMFaultMicrostackshots:vmFaultIntervalChanges:haveAnyOnlyPageGrabMicrostackshots:pageGrabIntervalChanges:
+ _objc_msgSend$isPMICycleRecord
+ _objc_msgSend$isPageGrabRecord
+ _objc_msgSend$isVMFaultRecord
+ _objc_msgSend$numMicrostackshotTypes
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$pCore
+ _objc_msgSend$pageGrabFlags
+ _objc_msgSend$pageGrabIOPLSampleCount
+ _objc_msgSend$pageGrabIntervalPages
+ _objc_msgSend$pageGrabUPLSampleCount
+ _objc_msgSend$pageGrabVMTag
+ _objc_msgSend$pagesGrabbedIOPLUPL
+ _objc_msgSend$pagesGrabbedTotal
+ _objc_msgSend$pmiCycleExtraSampleCount
+ _objc_msgSend$pointerValue
+ _objc_msgSend$repeatPrimaryStateInCallTrees
+ _objc_msgSend$runnable
+ _objc_msgSend$running
+ _objc_msgSend$setCpuNum:
+ _objc_msgSend$setDisplayCPUSpeedInCallTrees:
+ _objc_msgSend$setDisplayPMICycleIntervalInCallTrees:
+ _objc_msgSend$setDisplayPageGrabIntervalInCallTrees:
+ _objc_msgSend$setDisplayPageGrabTypeInCallTrees:
+ _objc_msgSend$setDisplayPageGrabVMTagInCallTrees:
+ _objc_msgSend$setDisplayVMFaultAddressAsLeafFrame:
+ _objc_msgSend$setDisplayVMFaultIntervalInCallTrees:
+ _objc_msgSend$setDisplayVMFaultTypeInCallTrees:
+ _objc_msgSend$setOmitFramesAfterLineCount:
+ _objc_msgSend$setPageGrabIntervalPages:
+ _objc_msgSend$setProcessNamesToPrint:
+ _objc_msgSend$setRepeatPrimaryStateInCallTrees:
+ _objc_msgSend$setSwiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways:
+ _objc_msgSend$setVmFaultIntervalPages:
+ _objc_msgSend$stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:vmFaultAddress:vmFaultIntervalPages:vmFaultType:vmFaultFlags:pageGrabUPLSampleCount:pageGrabIOPLSampleCount:pageGrabIntervalPages:pageGrabVMTag:pageGrabFlags:
+ _objc_msgSend$suspended
+ _objc_msgSend$unsignedCharValue
+ _objc_msgSend$unsignedShortValue
+ _objc_msgSend$vmFaultAddress
+ _objc_msgSend$vmFaultExtraSampleCount
+ _objc_msgSend$vmFaultFlags
+ _objc_msgSend$vmFaultIntervalPages
+ _objc_msgSend$vmFaultType
+ _objc_terminate
+ _saos_printf_memory_demand_interval
+ _saos_printf_seconds_sigfig
- +[SACallTreeState treeCountedStateWithWaitInfo:turnstileInfo:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:]
- +[SATaskState stateWithStackshotTaskV1:machTimebase:hwPageSize:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:]
- +[SAThreadState stateWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:]
- +[SAThreadState stateWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:threadPolicyVersion:]
- +[SAThreadState stateWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:]
- +[SAThreadState stateWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:threadPolicyVersion:threadInstructionCycles:]
- +[SAThreadStateMicrostackshot stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:]
- -[SACSSymbolOwnerWrapper symbolOwner]
- -[SACallTreeState initWithWaitInfo:turnstileInfo:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:]
- -[SASamplePrintOptions callTreeAggregationResolved]
- -[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]
- -[SASamplePrinter checkForBadOptions]
- -[SASamplePrinter printLaunchdThrottledProcessesToStream:]
- -[SASamplePrinter printStack:stream:]
- -[SASampleStore _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]
- -[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]
- -[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]
- -[SASampleStore addKCDataThreadV4:threadV2:deltaThreadV3:deltaThreadV2:timestamp:sampleIndex:stack:threadExclavesInfo:threadName:dispatchQueueLabel:waitInfo:waitInfoPortLabelInfo:turnstileInfo:turnstileInfoPortLabelInfo:instructionCycles:task:kernelTask:taskIsSuspended:]
- -[SAThreadState initWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:]
- -[SAThreadState initWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:threadPolicyVersion:]
- -[SAThreadState initWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:]
- -[SAThreadState initWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:threadPolicyVersion:threadInstructionCycles:]
- -[SATurnstileInfo compare:]
- -[SATurnstileInfo displaysSameContentAs:forPid:tid:displayOptions:]
- -[SAWaitInfo compare:]
- -[SAWaitInfo displaysSameContentAs:forPid:tid:displayOptions:]
- GCC_except_table132
- GCC_except_table274
- GCC_except_table541
- GCC_except_table544
- GCC_except_table549
- _.str.64
- _.str.65
- _.str.66
- _.str.67
- _.str.68
- _.str.69
- _.str.70
- _.str.71
- _.str.72
- _.str.734
- _.str.89
- _.str.90
- _.str.91
- _.str.92
- _.str.98
- _OBJC_IVAR_$_SACSSymbolOwnerWrapper._isDiskLayout
- _OBJC_IVAR_$_SACallTreeState._turnstileInfo
- _OBJC_IVAR_$_SACallTreeState._waitInfo
- _OBJC_IVAR_$_SASampleStore._lastPMIMicrostackshotSampleCount
- _OBJC_IVAR_$_SASampleStore._lastPMIMicrostackshotWallTime
- _OBJC_IVAR_$_SASampleStore._numPMIMicrostackshotsLost
- _OBJC_IVAR_$_SASampleStore._pmiCycleIntervalMax
- _OBJC_IVAR_$_SASampleStore._pmiCycleIntervalMin
- _OBJC_IVAR_$_SAStack._count
- _OBJC_IVAR_$_SAThreadState._turnstileInfo
- _OBJC_IVAR_$_SAThreadState._waitInfo
- _SACountedStateCompare
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1537
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1541
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1544
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1538
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1545
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1998
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2000
- ___116-[SASampleStore(KPerf) addLoadInfoFromKTrace:lastKTraceEventTimestamp:checkForNewLoadInfosEvenWithExistingLoadInfo:]_block_invoke.190
- ___123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke_3
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.162
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.167
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_10
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_11
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_12
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_13
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_14
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_15
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_16
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.163
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.168
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_3
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_3.171
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_4
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_4.172
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_5
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_6
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_7
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_8
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_9
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2471
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2487
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke_2
- ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke.297
- ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke.299
- ___138-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:]_block_invoke_2.300
- ___1459-[SASamplePrinter addTaskHeaderToStream:displayName:pid:mainBinary:mainBinaryPath:sharedCaches:uid:bundleIdentifier:bundleVersion:bundleShortVersion:bundleBuildVersion:bundleProjectName:bundleSourceVersion:bundleProductBuildVersion:adamID:installerVersionID:developerType:appType:isBeta:cohortID:vendorID:distributorID:codesigningID:teamID:resourceCoalitionSampleCounts:onBehalfOfProcesses:architectureString:kernelVersion:parentName:responsibleName:taskExecedFromName:taskExecedToName:forkTimestamp:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:numSamples:totalNumSamples:numSamplesSuspended:numSamplesTerminated:startingTaskSize:endingTaskSize:maxTaskSize:startSampleIndexOfMaxTaskSize:endSampleIndexOfMaxTaskSize:numPageins:cpuTimeNs:cpuInstructions:cpuCycles:nonThreadCpuTimeNs:nonThreadCpuInstructions:nonThreadCpuCycles:usesSuddenTermination:allowsIdleExit:memoryLimitStr:jetsamPriorityStr:isTranslocated:hardenedHeap:mteCheckedAllocationsEnabled:mteUserDataAllocationsTagged:mteSoftModeEnabled:mteInheritanceTurnedOn:isRunningBoardManaged:isUnresponsive:timeOfLastResponse:numThreads:numIdleWorkQueueThreads:numOtherHiddenThreads:hieSwallowedException:numSamplesWQExceededConstrainedThreadLimit:numSamplesWQExceededTotalThreadLimit:numSamplesWQExceededCooperativeThreadLimit:numSamplesWQExceededActiveConstrainedThreadLimit:numSamplesTALEngaged:isRunawayMitigated:threadsDeadlocked:threadsBlockedByADeadlock:ioSize:numIOs:isReportHeader:]_block_invoke
- ___23+[SABinary clearCaches]_block_invoke.99
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2433
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2442
- ___28-[SASampleStore postprocess]_block_invoke.214
- ___28-[SASampleStore postprocess]_block_invoke_2.215
- ___28-[SASampleStore postprocess]_block_invoke_3.218
- ___28-[SASampleStore symbolicate]_block_invoke.505
- ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke
- ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.346
- ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.356
- ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.360
- ___286-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke_2
- ___29-[SASampleStore gatherTrials]_block_invoke.549
- ___29-[SASampleStore gatherTrials]_block_invoke_2.550
- ___30-[SASamplePrinter printHeader]_block_invoke.1352
- ___30-[SASamplePrinter printHeader]_block_invoke.1379
- ___30-[SASamplePrinter printHeader]_block_invoke.1386
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1353
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1399
- ___31+[SASharedCache addDSCSymData:]_block_invoke.499
- ___32-[SASegment addTailspinSymbols:]_block_invoke.31
- ___34-[SASegment addInfoFromCSSegment:]_block_invoke.40
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_2
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_3
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_4
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_5
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_6
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_7
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_8
- ___350-[SASampleStore _parseKCDataThreadContainer:timestampOfSample:sampleIndex:task:kernelTask:frameIterator:mainThreadID:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:threadIDsInThisTaskThisSample:dispatchQueueIDsInThisTaskThisSample:taskIsSuspended:waitInfos:numWaitInfos:turnstileInfos:numTurnstileInfos:port_label_info_array:exclaveInfo:]_block_invoke_9
- ___37-[SASamplePrinter checkForBadOptions]_block_invoke.382
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2791
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2796
- ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.631
- ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1480
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1486
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1490
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2048
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2049
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2050
- ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.356
- ___54-[SACallTreeState writeJSONDictionaryEntriesToStream:]_block_invoke_2
- ___67-[SASampleStore _addMicrostackshotFromData:statistics:filterBlock:]_block_invoke.484
- ___69+[SASharedCache sharedCacheWithDyldSharedCache:dataGatheringOptions:]_block_invoke.492
- ___89-[SABinary symbolOwnerWrapperWithOptions:pid:checkExclave:additionalCSSymbolicatorFlags:]_block_invoke.142
- ___92+[SABinaryLoadInfo addBinaryLoadInfoForDyldImage:toLoadInfos:isKernel:dataGatheringOptions:]_block_invoke.355
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.219
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.231
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.257
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.276
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.290
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.309
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.320
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.268
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.283
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.294
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.312
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.326
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.307
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.315
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_4.316
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_5.319
- ___99-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:ktraceDataUnavailable:]_block_invoke.382
- ___ReadAheadTaskLevelInfo_block_invoke.2054
- ___ReadAheadTaskLevelInfo_block_invoke.2059
- ___ReadAheadTaskLevelInfo_block_invoke.2062
- ___block_descriptor_101_e8_32s40r48r_e23_v16?0^{dyld_image_s=}8lr40l8r48l8s32l8
- ___block_descriptor_129_e8_32s40s48s56s64s72s80r88r96r104r112r120r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8r80l8r88l8r96l8r104l8r112l8r120l8s64l8s72l8
- ___block_descriptor_141_e8_32s40s48s56s64s72s_e51_v20?0I8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}12ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_184_e8_32s40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r_e28_v32?0"SATaskState"8Q16^B24ls32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8
- ___block_descriptor_198_e8_32s40s48s56s64r72r80r88r96r104r112r120r128r136r144r_e15_v28?08I16^B20lr64l8r72l8r80l8r88l8s32l8r96l8r104l8s40l8r112l8r120l8r128l8r136l8r144l8s48l8s56l8
- ___block_descriptor_277_e8_32s40s48s56s64s72s80s88s96s104r112r120r128r136r144r152r160r168r176r184r192r200r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8s88l8r200l8s96l8
- ___block_descriptor_311_e8_32s40s48s56s64s72s80s88s96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r_e39_v32?0"SAThread"8"SAThreadState"16Q24ls32l8s40l8s48l8r96l8s56l8r104l8r112l8s64l8s72l8s80l8s88l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8
- ___block_descriptor_32_e43_q24?0"SACallTreeNode"8"SACallTreeNode"16l
- ___block_descriptor_40_e8_32bs_e15_v28?08I16^B20ls32l8
- ___block_descriptor_40_e8_32bs_e20_v24?0"SATask"8^B16ls32l8
- ___block_descriptor_40_e8_32bs_e22_v24?0{_CSTypeRef=QQ}8ls32l8
- ___block_descriptor_40_e8_32bs_e24_v32?0"SAFrame"8Q16^B24ls32l8
- ___block_descriptor_40_e8_32bs_e34_v24?0"SADispatchQueueState"8^B16ls32l8
- ___block_descriptor_40_e8_32bs_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8
- ___block_descriptor_40_e8_32bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8
- ___block_descriptor_40_e8_32bs_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
- ___block_descriptor_40_e8_32bs_e59_v48?0{_CSRange=QQ}8^{_CSTypeRef=QQ}24^{_CSTypeRef=QQ}32Q40ls32l8
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32r_e20_v24?0"SATask"8^B16lr32l8
- ___block_descriptor_40_e8_32r_e24_v16?0"NSMutableArray"8lr32l8
- ___block_descriptor_40_e8_32r_e24_v32?0"SAFrame"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32r_e28_v32?0"SATaskState"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32r_e29_v16?0"NSMutableDictionary"8lr32l8
- ___block_descriptor_40_e8_32r_e30_v32?0"SAThreadState"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8
- ___block_descriptor_40_e8_32r_e39_v32?0"NSUUID"8"NSMutableArray"16^B24lr32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32s_e13_v20?0I8r^Q12ls32l8
- ___block_descriptor_40_e8_32s_e20_v24?0"SATask"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e21_q16?0"SATaskState"8ls32l8
- ___block_descriptor_40_e8_32s_e21_v16?0"SATimestamp"8ls32l8
- ___block_descriptor_40_e8_32s_e23_q16?0"SARecipeState"8ls32l8
- ___block_descriptor_40_e8_32s_e23_q16?0"SAThreadState"8ls32l8
- ___block_descriptor_40_e8_32s_e24_v16?0"NSMutableArray"8ls32l8
- ___block_descriptor_40_e8_32s_e26_v16?0"SABinaryLoadInfo"8ls32l8
- ___block_descriptor_40_e8_32s_e29_q24?0"SAStack"8"SAStack"16ls32l8
- ___block_descriptor_40_e8_32s_e29_v32?08"NSDictionary"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e30_v32?0"NSUUID"8"NSURL"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e31_q24?0"NSString"8"NSString"16ls32l8
- ___block_descriptor_40_e8_32s_e34_v24?0"SADispatchQueueState"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e38_v32?0"NSNumber"8"SASwiftTask"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8
- ___block_descriptor_40_e8_32s_e39_v32?0"NSNumber"8"NSDictionary"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e40_v24?0"TRIRolloutAllocationStatus"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e42_v32?0"NSNumber"8"SADispatchQueue"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e43_v24?0"TRIExperimentAllocationStatus"8^B16ls32l8
- ___block_descriptor_40_e8_32s_e44_v20?0I8r^{jetsam_coalition_snapshot=QQQQ}12ls32l8
- ___block_descriptor_40_e8_32s_e44_v32?0"NSUUID"8"SAUUIDToSymbolicate"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
- ___block_descriptor_40_e8_32s_e47_v20?0I8r^{exclave_textlayout_segment=[16C]Q}12ls32l8
- ___block_descriptor_40_e8_32s_e48_v32?0"NSNumber"8"SADependencyGraphNode"16^B24ls32l8
- ___block_descriptor_40_e8_32s_e57_v40?0"NSString"8"NSString"16"NSString"24"NSString"32ls32l8
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_41_e8_32bs_e28_v32?0"SATaskState"8Q16^B24ls32l8
- ___block_descriptor_41_e8_32bs_e30_v32?0"SAThreadState"8Q16^B24ls32l8
- ___block_descriptor_41_e8_32r_e30_v32?0"SAThreadState"8Q16^B24lr32l8
- ___block_descriptor_41_e8_32r_e35_v32?0"NSString"8"NSString"16^B24lr32l8
- ___block_descriptor_45_e8_32bs_e24_v32?0"SAFrame"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32bs40bs_e15_v28?08I16^B20ls32l8s40l8
- ___block_descriptor_48_e8_32bs_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
- ___block_descriptor_48_e8_32r40r_e27_v24?0"SAInstruction"8^B16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e29_v24?0"SAMountSnapshot"8^B16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e34_v24?0"SADispatchQueueState"8^B16lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e35_v32?0"NSNumber"8"NSNumber"16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32r40r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32r_e20_v24?0"SATask"8^B16lr32l8
- ___block_descriptor_48_e8_32s40bs_e20_v24?0"SATask"8^B16ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e30_v32?0"SAThreadState"8Q16^B24ls40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e8_B16?0Q8ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e15_v32?0r*8Q16Q24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"SAFrame"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e20_v24?0"SATask"8^B16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e22_v24?0{_CSTypeRef=QQ}8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e23_i48?0r*8r*16r*24Q32Q40lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e24_v16?0"NSMutableArray"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"816^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e28_v32?0"SATaskState"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e28_v32?0"SATimestamp"8Q16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e29_v16?0"NSMutableDictionary"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e35_v32?0"NSNumber"8"SAThread"16^B24lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0i8ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e16_v16?0"SATask"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e20_v24?0"SATask"8^B16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e21_"NSString"20?0i8Q12ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e27_q24?0"SATask"8"SATask"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e27_v28?0"SABinary"8i16B20B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e29_q24?0"NSArray"8"NSArray"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e34_v32?0"SABinary"8"NSArray"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e35_v24?0"SASymbol"8"SASourceInfo"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e38_v32?0"NSNumber"8"SASwiftTask"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e5_q8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_q12?0B8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_q16?0Q8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e15_v16?0"NSSet"8ls32l8
- ___block_descriptor_48_e8_32s_e18_q16?0"SASymbol"8ls32l8
- ___block_descriptor_48_e8_32s_e26_i48?0[16C]8r*16r*24Q32Q40ls32l8
- ___block_descriptor_48_e8_32s_e29_v16?0"NSMutableDictionary"8ls32l8
- ___block_descriptor_48_e8_32s_e30_v32?0"SARecipeState"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8
- ___block_descriptor_48_e8_32s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8
- ___block_descriptor_48_e8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8
- ___block_descriptor_48_e8_32s_e50_v32?0"SAOnBehalfOfSingle"8"NSMutableData"16^B24ls32l8
- ___block_descriptor_49_e8_32s40bs_e20_v16?0"SAHIDEvent"8ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e20_v24?0"SATask"8^B16ls32l8s40l8
- ___block_descriptor_49_e8_32s40bs_e24_v32?0"SAFrame"8Q16^B24ls40l8s32l8
- ___block_descriptor_49_e8_32s40bs_e35_v32?0"NSNumber"8"SAThread"16^B24ls40l8s32l8
- ___block_descriptor_49_e8_32s40r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8
- ___block_descriptor_49_e8_32s40r_e47_v40?0"NSString"8"NSString"16"NSArray"24^B32ls32l8r40l8
- ___block_descriptor_49_e8_32s40s_e15_v32?0r*8Q16Q24ls32l8s40l8
- ___block_descriptor_50_e8_32s40s_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8s40l8
- ___block_descriptor_50_e8_32s_e40_v32?0"NSNumber"8"SAMountStatus"16^B24ls32l8
- ___block_descriptor_52_e8_32bs40r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr40l8s32l8
- ___block_descriptor_52_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_52_e8_32r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr32l8
- ___block_descriptor_52_e8_32s40r_e23_v16?0^{dyld_image_s=}8ls32l8r40l8
- ___block_descriptor_56_e8_32bs40r_e18_v36?0r*8Q16Q24i32lr40l8s32l8
- ___block_descriptor_56_e8_32bs40r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8r40l8
- ___block_descriptor_56_e8_32bs_e22_v24?0{_CSTypeRef=QQ}8ls32l8
- ___block_descriptor_56_e8_32r40r48r_e57_v40?0"NSString"8"NSString"16"NSString"24"NSString"32lr32l8r40l8r48l8
- ___block_descriptor_56_e8_32r40r_e16_v32?0r^v8Q16Q24lr32l8r40l8
- ___block_descriptor_56_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_56_e8_32r40r_e9_v16?0r*8lr32l8r40l8
- ___block_descriptor_56_e8_32r_e15_v32?0816^B24lu40l8u48l8r32l8
- ___block_descriptor_56_e8_32r_e15_v32?0r*8Q16Q24lr32l8
- ___block_descriptor_56_e8_32r_e22_v24?0{_CSTypeRef=QQ}8lr32l8
- ___block_descriptor_56_e8_32s40bs_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e20_v24?0"SATask"8^B16ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e22_v24?0{_CSTypeRef=QQ}8lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r_e20_v24?0"SATask"8^B16ls32l8r40l8
- ___block_descriptor_56_e8_32s40r_e25_v20?0"NSDictionary"8B16ls32l8r40l8
- ___block_descriptor_56_e8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
- ___block_descriptor_56_e8_32s40r_e38_v32?0"SASymbol"8"SASourceInfo"16Q24lr40l8s32l8
- ___block_descriptor_56_e8_32s40r_e5_v8?0lu48l8r40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e30_v32?0"SAThreadState"8Q16^B24ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e16_v16?0"SATask"8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e19_v20?0"SATask"8B16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e20_v24?0"SATask"8^B16ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e20_v24?0"SATask"8^B16ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e23_v16?0^{dyld_image_s=}8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e35_v32?0"NSNumber"8"SAThread"16^B24lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e54_v40?0"NSSet"8"NSSet"16"NSString"24"SATimestamp"32ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e71_v72?0Q8Q16"SATaskState"24"SAThread"32Q40"SAThreadState"48B56B60^B64ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e28_v32?0"SATaskState"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e30_v24?0"SASwiftTaskState"8^B16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSNumber"8"NSNumber"16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e5_q8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e8_q12?0B8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e8_q16?0Q8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e19_v20?0"SATask"8B16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e21_v16?0"SATimestamp"8ls32l8s40l8
- ___block_descriptor_56_e8_32s_e25_Q32?0{_CSTypeRef=QQ}8Q24ls32l8
- ___block_descriptor_56_e8_32s_e29_v16?0"NSMutableDictionary"8ls32l8
- ___block_descriptor_58_e8_32s_e22_v24?0{_CSTypeRef=QQ}8ls32l8
- ___block_descriptor_60_e8_32s40s48s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32bs40r48r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32r40r48r56r_e20_v24?0"SATask"8^B16lr32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32r40r48r56r_e22_v24?0{_CSTypeRef=QQ}8lr32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32r40r48r56r_e25_i16?0^{__CFDictionary=}8lr32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32r40r48r56r_e35_v24?0"SASymbol"8"SASourceInfo"16lr32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32r40r_e22_v24?0{_CSTypeRef=QQ}8lr32l8r40l8
- ___block_descriptor_64_e8_32r40r_e23_i48?0r*8r*16r*24Q32Q40lr32l8r40l8
- ___block_descriptor_64_e8_32r40r_e30_v16?0^{dyld_shared_cache_s=}8lr32l8r40l8
- ___block_descriptor_64_e8_32s40bs48r_e29_v24?0"SAMountSnapshot"8^B16ls40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40r48r56r_e43_v40?0"SAThread"8"SAThreadState"16Q24^B32ls32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_64_e8_32s40s48r56r_e16_v28?0Q8r^Q16I24lr48l8s32l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e34_v32?0"NSNumber"8"NSArray"16^B24ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_descriptor_64_e8_32s40s48r_e29_v16?0"NSMutableDictionary"8ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e24_v32?0"SAFrame"8Q16^B24ls32l8s40l8r56l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e24_v24?0r^{?=QQQQQQII}8Q16ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e48_v32?0"NSNumber"8"SADependencyGraphNode"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s_e13_v20?0I8r^Q12ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e42_v32?0"NSNumber"8"SADispatchQueue"16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s_e22_v24?0{_CSTypeRef=QQ}8ls32l8
- ___block_descriptor_65_e8_32s40s48r56r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r48l8r56l8s40l8
- ___block_descriptor_65_e8_32s40s48s56bs_e21_v16?0"SATimeRange"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s56s_e20_v24?0"SATask"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_65_e8_32s40s48s_e21_v16?0"SATimestamp"8ls32l8s40l8s48l8
- ___block_descriptor_66_e8_32s40s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8
- ___block_descriptor_69_e8_32r40r48r56r_e8_v12?0i8lr32l8r40l8r48l8r56l8
- ___block_descriptor_72_e8_32r40r48r56r_e35_v32?0"NSNumber"8"SAThread"16^B24lr32l8r40l8r48l8r56l8
- ___block_descriptor_72_e8_32s40r48r56r64r_e15_v32?0r*8Q16Q24ls32l8r40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e20_v24?0"SATask"8^B16ls32l8s40l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48r_e29_v16?0"NSMutableDictionary"8ls32l8r48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e30_v32?0"SAThreadState"8Q16^B24ls32l8r64l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s_e41_v32?0"NSNumber"8"NSMutableArray"16^B24ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s_e25_v32?0"SAThread"8Q16^B24ls32l8s40l8
- ___block_descriptor_72_e8_32s40s_e29_v16?0"NSMutableDictionary"8ls32l8s40l8
- ___block_descriptor_72_e8_32s40s_e40_v32?0"NSNumber"8"SAInstruction"16^B24ls32l8s40l8
- ___block_descriptor_73_e8_32s40s48s56r64r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_80_e8_32s40r_e29_v16?0"NSMutableDictionary"8ls32l8r40l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_81_e8_32s40r48r56r64r72r_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8r40l8r48l8r56l8r64l8r72l8
- ___block_descriptor_81_e8_32s40s48s56s64r72r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8s48l8s56l8r64l8r72l8
- ___block_descriptor_81_e8_32s40s48s56s64s72s_e35_v32?0"NSNumber"8"SAThread"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_81_e8_32s40s_e22_v24?0{_CSTypeRef=QQ}8ls32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s_e38_v32?0"SASymbol"8"SASourceInfo"16Q24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s_e13_v20?0I8r^Q12ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_96_e8_32s40r48r56r64r72r80r_e39_v40?0{_CSTypeRef=QQ}8{_CSTypeRef=QQ}24lr40l8s32l8r48l8r56l8r64l8r72l8r80l8
- ___block_descriptor_97_ea8_32s40s48s56r64r72r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr56l8s32l8r64l8r72l8s40l8s48l8
- ___block_literal_global.104
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.1164
- ___block_literal_global.127
- ___block_literal_global.1355
- ___block_literal_global.143
- ___block_literal_global.144
- ___block_literal_global.1492
- ___block_literal_global.151
- ___block_literal_global.186
- ___block_literal_global.192
- ___block_literal_global.1926
- ___block_literal_global.1942
- ___block_literal_global.1971
- ___block_literal_global.1974
- ___block_literal_global.202
- ___block_literal_global.2042
- ___block_literal_global.2047
- ___block_literal_global.205
- ___block_literal_global.2073
- ___block_literal_global.2086
- ___block_literal_global.2088
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.226
- ___block_literal_global.227
- ___block_literal_global.242
- ___block_literal_global.2430
- ___block_literal_global.2445
- ___block_literal_global.252
- ___block_literal_global.2524
- ___block_literal_global.254
- ___block_literal_global.275
- ___block_literal_global.2762
- ___block_literal_global.2784
- ___block_literal_global.2793
- ___block_literal_global.311
- ___block_literal_global.314
- ___block_literal_global.328
- ___block_literal_global.341
- ___block_literal_global.348
- ___block_literal_global.358
- ___block_literal_global.421
- ___block_literal_global.424
- ___block_literal_global.464
- ___block_literal_global.466
- ___block_literal_global.468
- ___block_literal_global.479
- ___block_literal_global.486
- ___block_literal_global.491
- ___block_literal_global.507
- ___block_literal_global.512
- ___block_literal_global.514
- ___block_literal_global.522
- ___block_literal_global.543
- ___block_literal_global.562
- ___block_literal_global.574
- ___block_literal_global.578
- ___block_literal_global.628
- ___block_literal_global.64
- ___block_literal_global.768
- __parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:ktraceDataUnavailable:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:.next_fake_unique_pid
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$descriptionForPid:tid:options:nameCallback:
- _objc_msgSend$initWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:
- _objc_msgSend$initWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:threadPolicyVersion:
- _objc_msgSend$initWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:
- _objc_msgSend$initWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:threadPolicyVersion:threadInstructionCycles:
- _objc_msgSend$initWithWaitInfo:turnstileInfo:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:
- _objc_msgSend$stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:
- _objc_msgSend$waitInfo
- _objc_release_x10
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
CStrings:
+ " (%.0f%% (%llu) IOPL/UPL)\n"
+ " (%.1f%s cycles, %.1f%s instructions, %.2fc/i, %.2fGHz avg)"
+ " (%llu cycles, %llu instructions, %fc/i, %.2fGHz avg)"
+ " (flags none)"
+ " (flags unknown(0x%x))"
+ " disconnect mappings interval"
+ " page grab interval"
+ " page grab memory demand/step"
+ " vm_fault interval"
+ " vm_fault memory demand/step"
+ " waiting on "
+ "!previousTurnstileInfo"
+ "!previousWaitInfo"
+ "%'llu No sampling point before jetsam priority change\n"
+ "%'llu No sampling point before runaway mitigation\n"
+ "%*s%s: %llu-%llu duration:%llu count:%llu%s\n"
+ "%*s%s: cluster_type:%d size:%llu used:%llu overhead:%llu%s\n"
+ "%*s%s: cpu_number:%d cluster_type:%d init_latency_mt:%llu workqueue_latency_mt:%llu total_latency_mt:%llu total_cycles:%llu total_instrs:%llu tasks_processed:%llu threads_processed:%llu faulting_time_mt:%llu total_buf:%llu intercluster_buf_used:%llu%s\n"
+ "%*s%s: flags:0x%x passcode_status:%d lock_state:%d%s\n"
+ "%*s%s: id:%llu name:%s%s\n"
+ "%*s%s: inner:%llu outer:%llu prior:%llu%s\n"
+ "%*s%s: inner:%llu outer:%llu%s\n"
+ "%*s%s: mat:%llu %s [%d] thread 0x%llx%s\n"
+ "%*s%s: pages:%u time:%llu maxtime:%llu hitlimit:%d%s\n"
+ "%*s%s: waiter:0x%llx blocker:0x%llx hash:0x%llx flags:0x%x%s\n"
+ "%-*s%llu pages"
+ "%.*f"
+ "%.0f%s%sB"
+ "%.0f%sK%sB"
+ "%.0fs gap with no microstackshots (but none missing) between %@ and %@"
+ "%.0fs gap with no microstackshots between %@ and %@"
+ "%.2f%s%sB"
+ "%.2f%sK%sB"
+ "%@ vm_fault"
+ "%@: cssegment name doesn't match: %s"
+ "%@: cssegment name is NULL"
+ "%@sec"
+ "%llu %@"
+ "%llu missing microstackshot between %@ and %@"
+ "%llu missing microstackshots between %@ and %@"
+ "%llu tag %u"
+ "%llupages"
+ "%s\n"
+ "%s %s vs last sample index %lu timestamp %s"
+ "%s: too many (%lu) vmRangeLocks"
+ "/atomic"
+ "/streaming"
+ "1.2.12"
+ "@\"SACountedState\""
+ "@104@0:8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}16@24@32Q40Q48@56@64@72@80@88@96"
+ "@104@0:8r^{thread_snapshot_v2=QQQQQQQQQQQIIssCCCC}16@24@32Q40Q48@56@64@72@80{mach_timebase_info=II}88@96"
+ "@108@0:8r^{thread_delta_snapshot_v3=QQQQIIssCCCCQQ}16@24@32Q40Q48@56@64@72@80@88@96I104"
+ "@116@0:8r^{thread_snapshot_v4=QQQQQQQQQQQIIssCCCCQQQ}16@24@32Q40Q48@56@64@72@80{mach_timebase_info=II}88@96I104r^{instrs_cycles_snapshot=QQ}108"
+ "@152@0:8r^{micro_snapshot=IIQQCS}16r^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24@32@40Q48Q56@64@72@80{mach_timebase_info=II}88Q96Q104Q112S120S124S128S132Q136S144C148"
+ "@64@0:8@16@24@32B40B44B48B52B56B60"
+ "@92@0:8@16B24B28@32I40i44Q48C56@60i68i72Q76Q84"
+ "B36@0:8i16Q20Q28"
+ "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQiiQQQQQQSSSSQSSSS}16Q24@32"
+ "Base of compressed stackshot is before the returned stackshot buffer"
+ "Begin compressed buffer"
+ "Decompressed kcdata buffer from %u to %{bytes}lu"
+ "Error generating call tree: %@"
+ "Failed to allocate %zu bytes for decompressed kcdata buffer: %{errno}d"
+ "Failed to allocate NSData for compressed-none kcdata buffer"
+ "Footer does not fit in the buffer (footer size %zu, available space %lu)"
+ "Including 0x%x microstackshot %llu for %s [%d] thread 0x%llx leaf frame 0x%llx at %@"
+ "KCData compressed buffer failed to get payload from compressed stackshot"
+ "KCData compressed buffer has invalid compressed size: %llu"
+ "KCData compressed buffer has invalid uncompressed size: %llu"
+ "KCData compressed buffer has no compression type"
+ "KCData compressed buffer has unsupported kcdata compression type %llu"
+ "Microstackshot statistics:\n%llu bytes parsed (%llu ms, %llu non-ms, %llu invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nvm_fault  count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npage grab count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
+ "Multiple binaries with UUID %@ exist, using %@"
+ "Multiple turnstile infos: %s and %s"
+ "Multiple wait infos: %s and %s"
+ "No samples for specified time interval"
+ "Not including 0x%x microstackshot %llu for %s [%d] at %@ due to filter"
+ "Not including 0x%x microstackshot %llu for %s [%d] at %@ due to no load info"
+ "Not including duplicate 0x%x microstackshot %llu for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
+ "Not including out-of-order 0x%x microstackshot %llu for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
+ "Out-of-order 0x%x microstackshot %llu for %s [%d] thread 0x%llx at %@ (by %fs overall) first sample for this thread"
+ "Out-of-order 0x%x microstackshot %llu for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs"
+ "Out-of-order 0x%x microstackshot %llu for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs (out of order for task)"
+ "Page Grab Types: "
+ "Page Grab VMTags: "
+ "Pages Grabbed: "
+ "SABlockingInfo subclass %s doesn't implement descriptionForPid"
+ "SABlockingInfo subclass %s doesn't implement displaysSomethingForPid"
+ "SACountedState"
+ "SAVMRangeLock"
+ "T@\"NSArray\",R,V_blockingInfos"
+ "T@\"SAMSTypeStats\",R,V_page_grab"
+ "T@\"SAMSTypeStats\",R,V_vm_fault"
+ "TB,R,V_blockerAtomic"
+ "TB,R,V_blockerExclusive"
+ "TB,R,V_blockerShared"
+ "TB,R,V_blockerStreaming"
+ "TB,R,V_eCore"
+ "TB,R,V_pCore"
+ "TB,R,V_runnable"
+ "TB,R,V_running"
+ "TB,R,V_suspended"
+ "TB,R,V_waiterAtomic"
+ "TB,R,V_waiterExclusive"
+ "TB,R,V_waiterShared"
+ "TB,R,V_waiterStreaming"
+ "TB,V_displayPageGrabIntervalInCallTrees"
+ "TB,V_displayPageGrabTypeInCallTrees"
+ "TB,V_displayPageGrabVMTagInCallTrees"
+ "TB,V_displayVMFaultAddressAsLeafFrame"
+ "TB,V_displayVMFaultIntervalInCallTrees"
+ "TB,V_displayVMFaultTypeInCallTrees"
+ "TB,V_repeatPrimaryStateInCallTrees"
+ "TC,R,V_pageGrabFlags"
+ "TQ,R,V_pagesGrabbedIOPLUPL"
+ "TQ,R,V_pagesGrabbedTotal"
+ "TQ,R,V_pmiCycleInterval"
+ "TQ,V_pageGrabIntervalPages"
+ "TQ,V_vmFaultIntervalPages"
+ "TS,R"
+ "TS,R,V_cpuSpeedMhz"
+ "TS,R,V_pageGrabVMTag"
+ "TS,R,V_vmFaultFlags"
+ "TS,R,V_vmFaultType"
+ "Td,V_disconnectMappingsInterval"
+ "Uncompressing KCData compressed buffer type 0x%llx: %u -> %u"
+ "Unknown SAVMRangeLock version"
+ "Unsupported blockinginfo class %s"
+ "Unsupported blockinginfo class %s (vs %s)"
+ "VM Fault Types: "
+ "VM Faults: "
+ "VM range lock owned by "
+ "VM tag %u"
+ "VM tag none"
+ "WARNING: Decompressed size %lu does not match expected size %u"
+ "Ws"
+ "[blockingInfo isKindOfClass:SAVMRangeLock.class]"
+ "[previousBlockingInfo isKindOfClass:SAVMRangeLock.class]"
+ "[self isKindOfClass:SAVMRangeLock.class]"
+ "[self isKindOfClass:SAWaitInfo.class]"
+ "_blockerAtomic"
+ "_blockerExclusive"
+ "_blockerShared"
+ "_blockerStreaming"
+ "_blockingInfos"
+ "_blockingTid"
+ "_countedStateCache"
+ "_cpuNumOffByOne"
+ "_cpuSpeedMhz"
+ "_disconnectMappingsInterval"
+ "_displayPageGrabIntervalInCallTrees"
+ "_displayPageGrabTypeInCallTrees"
+ "_displayPageGrabVMTagInCallTrees"
+ "_displayVMFaultAddressAsLeafFrame"
+ "_displayVMFaultIntervalInCallTrees"
+ "_displayVMFaultTypeInCallTrees"
+ "_eCore"
+ "_extraSampleCount"
+ "_extraSampleCountForTask"
+ "_haveAnyOnlyPMIMicrostackshots"
+ "_haveAnyOnlyPageGrabMicrostackshots"
+ "_haveAnyOnlyVMFaultMicrostackshots"
+ "_lastMicrostackshotSampleCount"
+ "_lastMicrostackshotWallTime"
+ "_numMicrostackshotsLost"
+ "_numSamplesWhenLastPreprocessed"
+ "_pCore"
+ "_pageGrabFlags"
+ "_pageGrabIOPLSampleCount"
+ "_pageGrabIntervalPages"
+ "_pageGrabIntervalPagesMax"
+ "_pageGrabIntervalPagesMin"
+ "_pageGrabIntervalPagesMostRecent"
+ "_pageGrabTypeCounts"
+ "_pageGrabTypeCountsByTask"
+ "_pageGrabUPLSampleCount"
+ "_pageGrabVMTag"
+ "_pageGrabVMTagCounts"
+ "_pageGrabVMTagCountsByTask"
+ "_page_grab"
+ "_pagesGrabbedIOPLUPL"
+ "_pagesGrabbedTotal"
+ "_repeatPrimaryStateInCallTrees"
+ "_runnable"
+ "_running"
+ "_suspended"
+ "_vmFaultAddress"
+ "_vmFaultFlags"
+ "_vmFaultIntervalPages"
+ "_vmFaultIntervalPagesMax"
+ "_vmFaultIntervalPagesMin"
+ "_vmFaultIntervalPagesMostRecent"
+ "_vmFaultType"
+ "_vmFaultTypeCounts"
+ "_vmFaultTypeCountsByTask"
+ "_vm_fault"
+ "_waiterAtomic"
+ "_waiterExclusive"
+ "_waiterShared"
+ "_waiterStreaming"
+ "anonymous"
+ "arrayByAddingObject:"
+ "blockerAtomic"
+ "blockerExclusive"
+ "blockerShared"
+ "blockerStreaming"
+ "blockingInfos"
+ "bufferLength %lu < serialized SAThreadState struct plus %u vm range locks %llu"
+ "bufferLength %lu < serialized SAThreadState v11 struct %lu"
+ "bufferLength %lu < serialized SAVMRangeLock struct %lu"
+ "bufferLength >= sizeof(*serializedThreadState_v11)"
+ "bufferLength >= sizeof(*serializedThreadState_v13)"
+ "bufferLength >= sizeof(*serializedVMRangeLock)"
+ "bufferLength >= sizeofV13"
+ "cache-hit"
+ "copy-on-read"
+ "copy-on-write"
+ "crashinfo cs auxiliary info"
+ "dataWithBytesNoCopy:length:"
+ "decompression"
+ "disconnectMappingsInterval"
+ "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayCPUSpeedInCallTrees: %d\ndisplayPMICycleIntervalInCallTrees: %d\ndisplayVMFaultAddressAsLeafFrame: %d\ndisplayVMFaultIntervalInCallTrees: %d\ndisplayVMFaultTypeInCallTrees: %d\ndisplayPageGrabIntervalInCallTrees: %d\ndisplayPageGrabTypeInCallTrees: %d\ndisplayPageGrabVMTagInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ndisplayTrialInformation: %d\nrepeatPrimaryStateInCallTrees: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\ntaskAggregation: %llu\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\nprintProblematicProcessesAndThreads: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
+ "displayPageGrabIntervalInCallTrees"
+ "displayPageGrabTypeInCallTrees"
+ "displayPageGrabVMTagInCallTrees"
+ "displayVMFaultAddressAsLeafFrame"
+ "displayVMFaultIntervalInCallTrees"
+ "displayVMFaultTypeInCallTrees"
+ "displaysSomethingForPid:tid:displayOptions:"
+ "exclusive"
+ "file"
+ "guard"
+ "hasCPUNum"
+ "inflate failed with result %d"
+ "inflateInit failed"
+ "initWithBlockingInfos:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:"
+ "initWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:"
+ "initWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:blockingInfos:threadPolicyVersion:"
+ "initWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:"
+ "initWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:blockingInfos:threadPolicyVersion:threadInstructionCycles:"
+ "initWithThreadState:sampleStore:printOptions:haveAnyOnlyPMIMicrostackshots:pmiCycleIntervalChanges:haveAnyOnlyVMFaultMicrostackshots:vmFaultIntervalChanges:haveAnyOnlyPageGrabMicrostackshots:pageGrabIntervalChanges:"
+ "iopl"
+ "iopl page grab%s"
+ "isPageGrabRecord"
+ "isVMFaultRecord"
+ "kcd_c_totalin"
+ "kcd_c_totalout"
+ "kcd_c_type"
+ "kcdata compression none, but totalin %u != totalout %u"
+ "lastSampleIndex - firstSampleIndex + 1 >= sampleCount"
+ "latency info buffer"
+ "latency info cpu"
+ "lock state"
+ "nil report start time %s, or report end time %s"
+ "no-zero-fill"
+ "not a vm_fault"
+ "numFaults"
+ "numMicrostackshotTypes"
+ "numMicrostackshotsLost"
+ "numPagesGrabbedIOPLUPL"
+ "numPagesGrabbedTotal"
+ "numVMRangeLocks < UINT16_MAX"
+ "numberWithUnsignedChar:"
+ "numberWithUnsignedShort:"
+ "page list request in progress"
+ "pageGrabFlags"
+ "pageGrabIOPLSampleCount"
+ "pageGrabIntervalPages"
+ "pageGrabIntervalPagesMax"
+ "pageGrabIntervalPagesMin"
+ "pageGrabTypeCounts"
+ "pageGrabUPLSampleCount"
+ "pageGrabVMTag"
+ "pageGrabVMTagCounts"
+ "page_grab"
+ "pagein"
+ "pagesGrabbedIOPLUPL"
+ "pagesGrabbedTotal"
+ "pagesec"
+ "pmiCycleExtraSampleCount"
+ "pointerValue"
+ "ran off end of adornment (%ld): '%s'"
+ "repeatPrimaryStateInCallTrees"
+ "reportStartTime && reportEndTime"
+ "setCpuNum:"
+ "setDisconnectMappingsInterval:"
+ "setDisplayPageGrabIntervalInCallTrees:"
+ "setDisplayPageGrabTypeInCallTrees:"
+ "setDisplayPageGrabVMTagInCallTrees:"
+ "setDisplayVMFaultAddressAsLeafFrame:"
+ "setDisplayVMFaultIntervalInCallTrees:"
+ "setDisplayVMFaultTypeInCallTrees:"
+ "setPageGrabIntervalPages:"
+ "setRepeatPrimaryStateInCallTrees:"
+ "setVmFaultIntervalPages:"
+ "stack.sampleCount == 0 || stack.rootObjects != nil"
+ "stackshot fault stats"
+ "stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:vmFaultAddress:vmFaultIntervalPages:vmFaultType:vmFaultFlags:pageGrabUPLSampleCount:pageGrabIOPLSampleCount:pageGrabIntervalPages:pageGrabVMTag:pageGrabFlags:"
+ "suspended:%d runnable:%d running:%d ecore:%d pcore:%d cpunum:%d cpuSpeedMhz:%u pmiCycleInterval:%llu vmFaultIntervalPages:%llu vmFaultType:%u vmFaultFlags:%u pageGrabIntervalPages:%llu pageGrabVMTag:%u pageGrabFlags:%u"
+ "suspension info"
+ "suspension source"
+ "swapin"
+ "task exec meta"
+ "this thread"
+ "thread group"
+ "thread group snapshot"
+ "tree state %lu-%lu (%lu) [%d] thread 0x%llx priority:%d state:(%@) microState:0x%x blockingInfo:<%@> deadlocked:%d indirectly_deadlocked:%d io:%@ timeRanges:%@ originPid:%d proximatePid:%d uplSamples:%u ioplSamples:%u"
+ "unknown core"
+ "unknown(%d)"
+ "unknown(0x%x)"
+ "unsignedCharValue"
+ "unsignedShortValue"
+ "upl"
+ "upl page grab%s"
+ "v16@?0@\"SAThreadState\"8"
+ "v20@?0I8r^{stackshot_vmrl_blocking_relationship=QQQI}12"
+ "v32@?0@\"SACountedState\"8@\"NSNumber\"16^B24"
+ "vm range lock blocking relationship"
+ "vmFaultAddress"
+ "vmFaultExtraSampleCount"
+ "vmFaultFlags"
+ "vmFaultIntervalPages"
+ "vmFaultIntervalPagesMax"
+ "vmFaultIntervalPagesMin"
+ "vmFaultType"
+ "vmFaultTypeCounts"
+ "vmRangeLockIndex %lu >= numVMRangeLocks %lu"
+ "vmRangeLockIndex < numVMRangeLocks"
+ "vm_fault"
+ "vmrl tid:0x%llx flags:0x%llx"
+ "waiterAtomic"
+ "waiterExclusive"
+ "waiterShared"
+ "waiterStreaming"
+ "zero-fill"
+ "\xc2"
- " (%.1f%s cycles, %.1f%s instructions, %.2fc/i)"
- " (%llu cycles, %llu instructions, %fc/i)"
- "%.0f  %sB"
- "%.0f G%sB"
- "%.0f K%sB"
- "%.0f M%sB"
- "%.0fs gap with no PMI microstackshots (but none missing) between %@ and %@"
- "%.0fs gap with no PMI microstackshots between %@ and %@"
- "%.2f  %sB"
- "%.2f G%sB"
- "%.2f K%sB"
- "%.2f M%sB"
- "%@: Got dyld shared cache %@ though have existing %@"
- "%llu missing PMI microstackshots between %@ and %@"
- "@\"SATurnstileInfo\""
- "@100@0:8@16@24B32B36{_SACountedState=(?=Q{?=ISCb1b1b1b1b1})}40I48i52Q56C64@68i76i80Q84Q92"
- "@104@0:8r^{micro_snapshot=IIQQCS}16r^{thread_snapshot=IIIQQQQQiiiiccccc[3c]QQQQ[4Q][4Q]QQQQQQQQQQ[64c]}24@32@40Q48Q56@64@72@80{mach_timebase_info=II}88Q96"
- "@112@0:8r^{thread_delta_snapshot_v2=QQQQIIssCCCC}16@24@32Q40Q48@56@64@72@80@88@96@104"
- "@112@0:8r^{thread_snapshot_v2=QQQQQQQQQQQIIssCCCC}16@24@32Q40Q48@56@64@72@80{mach_timebase_info=II}88@96@104"
- "@116@0:8r^{thread_delta_snapshot_v3=QQQQIIssCCCCQQ}16@24@32Q40Q48@56@64@72@80@88@96@104I112"
- "@124@0:8r^{thread_snapshot_v4=QQQQQQQQQQQIIssCCCCQQQ}16@24@32Q40Q48@56@64@72@80{mach_timebase_info=II}88@96@104I112r^{instrs_cycles_snapshot=QQ}116"
- "B40@0:8^{?=CCQQQQQQQQQQQQQQiiIQCCCCCCCIC(?=S{?=b1b1b1b1b1b1})QIICCCQQiiQQQ}16Q24@32"
- "Including 0x%x microstackshot for %s [%d] thread 0x%llx at %@"
- "Microstackshot statistics:\n%llu bytes parsed (%llu ms, %llu non-ms, %llu invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
- "No samples\n"
- "No samples for specified time interval\n"
- "Not including duplicate microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
- "Not including microstackshot for %s [%d] at %@ due to no load info"
- "Not including out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
- "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) first sample for this thread"
- "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs"
- "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs (out of order for task)"
- "Thread %s state %s vs last sample index %lu timestamp %s"
- "WARNING: Multiple binaries with UUID %@ exist, using %@"
- "Xs"
- "_isDiskLayout"
- "_lastPMIMicrostackshotSampleCount"
- "_lastPMIMicrostackshotWallTime"
- "_turnstileInfo"
- "displayHeader: %d\ndisplayBody: %d\ndisplayFooter: %d\ntabDelineateBinaryImageSections: %d\nbinaryImagesBeforeStacks: %d\nprintSpinSignatureStack: %d\nprintTargetThreadOnly: %d\nprintHeavyStacks: %d\nprintJson: %d\nforceOneBasedTimeIndexes: %d\nshowThreadStateAsLeafFrame: %d\npatchTruncatedStacks: %d\nomitTasksBelowPercentOfTotalSamples: %d\nomitStacksBelowPercentOfTaskSamples: %d\nomitFramesBelowPercentOfStackSamples: %d\nomitTasksBelowSampleCount: %lld\nomitStacksBelowSampleCount: %lld\nomitFramesBelowSampleCount: %lld\nprocessSortAttributes: %@\ncallTreeSortAttributes: %@\ndisplayKernelFrames: %d\ndisplayExclaveFrames: %d\ndisplayUserFrames: %d\ndisplayFrameAddresses: %d\ndisplayDetailedCpuTime: %d\ndisplayDetailedWallTime: %d\ndisplayOffsetsFromUnnamedSymbols: %d\ndisplayFullSourcePaths: %d\ndisplaySymbolInformation: %d\ndisplayBinaryImageAddresses: %d\ndisplayBinaryImagesLackingNameOrPath: %d\ndisplayRunningThreads: %d\ndisplayRunnableThreads: %d\ndisplayBlockedThreads: %d\ndisplayCPUNumForRunningThreads: %d\ndisplayCPUClusterInfoForRunningThreads: %d\ndisplayCPUNumForNonRunningThreads: %d\ndisplayThreadRunningState: %d\ndisplayIdleWorkQueueThreads: %d\ndisplayAllBinaries: %d\ndisplayBlockedReasons: %d\ndisplayBlockedReasonsLackingProcessOwners: %d\ndisplayAddressesInBlockedReasons: %d\ndisplayMultipleMatchingBlockedReasons: %d\ndisplayEmptyBootArgs: %d\nhidEventDisplayOptions: 0x%llx\ndisplayTasksWithZeroCount: %d\ndisplayAllTaskSizeChanges: %d\ndisplayCodesigningIDsMatchingBundleIDs: %d\ndisplayDefaultPowerModes: %d\ndisplayIOInCallTrees: %d\ndisplayEachIndividualIOInCallTrees: %d\ndisplayOnBehalfOfInCallTrees: %d\ndisplayQoSTransitionsBetweenUnspecifiedAndUnavailable: %d\ndisplayTrialInformation: %d\ncallTreeTimestampsTimeDomain: 0x%llx\ncallTreeAggregation: %llu\nswiftAsyncCallTreeAggregation: %llu\nswiftAsyncDisplayCRootCallstacks: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfSwiftAsyncCallstacksAlways: %d\nswiftAsyncPrintLeafyCCallstackOnTopOfCRootCallstacksAlways: %d\ntaskAggregation: %llu\naggregateFramesByOffsetIntoBinary: %d\nmicrostackshotsFormat: %d\nsystemstatsFormat: %d\nincludeUserIdleAndBatteryStateInStacks: %d\nomitStacksOnBattery: %d\nomitStacksOnAC: %d\nomitStacksWithUserIdle: %d\nomitStacksWithUserActive: %d\nomitStacksWithECore: %d\nomitStacksWithPCore: %d\nomitStacksBelowBasePriority: %d\nomitStacksAboveBasePriority: %d\nomitAbsoluteWallTimes: %d\nprintProblematicProcessesAndThreads: %d\ntidsToPrint: %@\npidsToPrint: %@\nuniquePidsToPrint: %@\nprocessUUIDsToPrint: %@\n"
- "initWithKCDataDeltaThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:"
- "initWithKCDataDeltaThreadV3:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:oldThreadState:waitInfo:turnstileInfo:threadPolicyVersion:"
- "initWithKCDataThreadV2:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:"
- "initWithKCDataThreadV4:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:name:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:waitInfo:turnstileInfo:threadPolicyVersion:threadInstructionCycles:"
- "initWithWaitInfo:turnstileInfo:isPartOfADeadlock:isBlockedByADeadlock:state:microstackshotState:pid:threadId:threadPriority:timeRange:originPid:proximatePid:startSampleIndex:sampleCount:"
- "lastSampleIndex - firstSampleIndex + 1 >= count"
- "not e-core"
- "not p-core"
- "numPMIMicrostackshotsLost"
- "pager initialization"
- "stack.count == 0 || stack.rootObjects != nil"
- "stateWithMicrostackshot:thread:startTimestamp:endTimestamp:startSampleIndex:endSampleIndex:leafUserFrame:leafOfCRootFramesReplacedBySwiftAsync:leafKernelFrame:machTimebase:pmiCycleInterval:"
- "tree state %lu-%lu (%lu) [%d] thread 0x%llx priority:%d state:0x%llx microState:0x%x waitInfo:%@ turnstileInfo:%@ deadlocked:%d indirectly_deadlocked:%d io:%@ timeRanges:%@ originPid:%d proximatePid:%d"
- "{_SACountedState=\"\"(?=\"bits\"Q\"\"{?=\"pmiCycleIntervalMillions\"I\"cpuSpeed100Mhz\"S\"_cpuNumOffbyOne\"C\"pCore\"b1\"eCore\"b1\"running\"b1\"runnable\"b1\"suspended\"b1})}"
- "\xd2"

```
