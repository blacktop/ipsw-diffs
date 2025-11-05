## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis`

```diff

-382.1.0.0.0
-  __TEXT.__text: 0xfce94
-  __TEXT.__auth_stubs: 0x1800
-  __TEXT.__objc_methlist: 0x5650
-  __TEXT.__const: 0x318
-  __TEXT.__cstring: 0x17298
-  __TEXT.__oslogstring: 0xbcda
-  __TEXT.__gcc_except_tab: 0xa3b8
+385.13.0.0.0
+  __TEXT.__text: 0x103948
+  __TEXT.__auth_stubs: 0x1830
+  __TEXT.__objc_methlist: 0x5ac4
+  __TEXT.__const: 0x378
   __TEXT.__dlopen_cstrs: 0x16a
-  __TEXT.__unwind_info: 0x2150
-  __TEXT.__objc_classname: 0xa8e
-  __TEXT.__objc_methname: 0xcede
-  __TEXT.__objc_methtype: 0x17bb
-  __TEXT.__objc_stubs: 0x7ce0
-  __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0xd20
-  __DATA_CONST.__objc_classlist: 0x3e0
+  __TEXT.__cstring: 0x17ae8
+  __TEXT.__oslogstring: 0xc928
+  __TEXT.__gcc_except_tab: 0xa5c8
+  __TEXT.__unwind_info: 0x2180
+  __TEXT.__objc_classname: 0xabb
+  __TEXT.__objc_methname: 0xd366
+  __TEXT.__objc_methtype: 0x1811
+  __TEXT.__objc_stubs: 0x7e00
+  __DATA_CONST.__got: 0x430
+  __DATA_CONST.__const: 0xd58
+  __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2838
+  __DATA_CONST.__objc_selrefs: 0x2908
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x170
-  __AUTH_CONST.__auth_got: 0xc18
-  __AUTH_CONST.__const: 0x3c40
-  __AUTH_CONST.__cfstring: 0xb520
-  __AUTH_CONST.__objc_const: 0xf6f0
+  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_arraydata: 0x1b8
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH_CONST.__const: 0x3de0
+  __AUTH_CONST.__cfstring: 0xbba0
+  __AUTH_CONST.__objc_const: 0xf948
   __AUTH_CONST.__objc_intobj: 0x168
-  __AUTH_CONST.__objc_arrayobj: 0x1b0
-  __AUTH.__objc_data: 0x26c0
+  __AUTH_CONST.__objc_arrayobj: 0x1f8
+  __AUTH.__objc_data: 0x2760
   __AUTH.__thread_vars: 0x60
-  __AUTH.__thread_bss: 0x19
-  __DATA.__objc_ivar: 0xc64
+  __AUTH.__thread_bss: 0x20
+  __DATA.__objc_ivar: 0xccc
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4f0
+  __DATA.__bss: 0x510
   __DATA.__common: 0x498
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: AE9A4ADC-D442-392B-A26F-3924C98A58A3
-  Functions: 2853
-  Symbols:   6755
-  CStrings:  7965
+  UUID: 988FFEB8-CA5B-3657-B092-3D6EA3BA3B79
+  Functions: 2880
+  Symbols:   6889
+  CStrings:  8181
 
Symbols:
+ +[SABinaryLoadInfo binaryLoadInfoForLiveProcessWithPid:dataGatheringOptions:additionalCSSymbolicatorFlags:mainBinaryOut:sharedCacheOut:]
+ +[SABootInfo(Serialization) classDictionaryKey]
+ +[SABootInfo(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ +[SANANDGarbageCollectionEvent parseKTrace:findingGarbageCollectionEvents:]
+ +[SANANDGarbageCollectionEvent(Serialization) classDictionaryKey]
+ +[SANANDGarbageCollectionEvent(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ +[SASharedCache sharedCacheWithUUID:slidBaseAddress:]
+ -[SABootInfo .cxx_destruct]
+ -[SABootInfo bootArgs]
+ -[SABootInfo debugDescription]
+ -[SABootInfo kernelVersion]
+ -[SABootInfo osBuildVersion]
+ -[SABootInfo osProductVersionExtra]
+ -[SABootInfo osProductVersion]
+ -[SABootInfo uuid]
+ -[SABootInfo wallTimeAtMachAbsZero]
+ -[SABootInfo(JSONSerialization) writeJSONDictionaryEntriesToStream:]
+ -[SABootInfo(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SABootInfo(Serialization) addSelfToSerializationDictionary:]
+ -[SABootInfo(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SABootInfo(Serialization) sizeInBytesForSerializedVersion]
+ -[SAExclave sharedCache]
+ -[SAMicrostackshotStatistics bytes_other_data]
+ -[SAMicrostackshotStatistics setBytes_other_data:]
+ -[SANANDGarbageCollectionEvent .cxx_destruct]
+ -[SANANDGarbageCollectionEvent debugDescription]
+ -[SANANDGarbageCollectionEvent endTimestamp]
+ -[SANANDGarbageCollectionEvent reasonCode]
+ -[SANANDGarbageCollectionEvent reason]
+ -[SANANDGarbageCollectionEvent startTimestamp]
+ -[SANANDGarbageCollectionEvent(JSONSerialization) writeJSONDictionaryEntriesToStream:]
+ -[SANANDGarbageCollectionEvent(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SANANDGarbageCollectionEvent(Serialization) addSelfToSerializationDictionary:]
+ -[SANANDGarbageCollectionEvent(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SANANDGarbageCollectionEvent(Serialization) sizeInBytesForSerializedVersion]
+ -[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]
+ -[SASamplePrinter kernelVersionAtWallTime:]
+ -[SASamplePrinter sortHeavyCallTree:]
+ -[SASampleStore bootCycles]
+ -[SASampleStore handleNonMicrostackshotData:bufSize:statistics:]
+ -[SASampleStore kperfSampleAtTimestamp:isPET:state:ignore:]
+ -[SASampleStore nandGarbageCollectionEvents]
+ -[SASampleStore sharedCacheResidentSizeInBytes]
+ -[SASampleStore sharedCacheVirtualSizeInBytes]
+ -[SATask addOutOfOrderState:]
+ -[SAThreadExclavesInfo reverseOrderOfCallstacks]
+ -[SATimeRange deltaMachWithTimeDomainPriorityList:timeDomainUsed:]
+ -[SATimeRange deltaSecondsWithTimeDomainPriorityList:timeDomainUsed:]
+ GCC_except_table119
+ GCC_except_table125
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table133
+ GCC_except_table151
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table176
+ GCC_except_table185
+ GCC_except_table193
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table212
+ GCC_except_table214
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table22
+ GCC_except_table222
+ GCC_except_table231
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table241
+ GCC_except_table246
+ GCC_except_table25
+ GCC_except_table250
+ GCC_except_table254
+ GCC_except_table283
+ GCC_except_table290
+ GCC_except_table291
+ GCC_except_table31
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table44
+ GCC_except_table52
+ GCC_except_table522
+ GCC_except_table525
+ GCC_except_table530
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table78
+ GCC_except_table96
+ OBJC_IVAR_$_SABootInfo._bootArgs
+ OBJC_IVAR_$_SABootInfo._kernelVersion
+ OBJC_IVAR_$_SABootInfo._osBuildVersion
+ OBJC_IVAR_$_SABootInfo._osProductVersion
+ OBJC_IVAR_$_SABootInfo._osProductVersionExtra
+ OBJC_IVAR_$_SABootInfo._uuid
+ OBJC_IVAR_$_SABootInfo._wallTimeAtMachAbsZero
+ OBJC_IVAR_$_SAExclave._sharedCache
+ OBJC_IVAR_$_SAKPerfState._petTimerMostRecentSampleWasDeadReckoned
+ OBJC_IVAR_$_SAKPerfState._petTimerNextExpectedSampleMachAbs
+ OBJC_IVAR_$_SAKPerfState._petTimerPeriodMachAbs
+ OBJC_IVAR_$_SAKPerfState._timestampAfterTimeAdjustments
+ OBJC_IVAR_$_SAKPerfState._timestampBeforeAnyTimeAdjustments
+ OBJC_IVAR_$_SAMicrostackshotStatistics._bytes_other_data
+ OBJC_IVAR_$_SANANDGarbageCollectionEvent._endTimestamp
+ OBJC_IVAR_$_SANANDGarbageCollectionEvent._reasonCode
+ OBJC_IVAR_$_SANANDGarbageCollectionEvent._startTimestamp
+ OBJC_IVAR_$_SASampleStore._bootCycles
+ OBJC_IVAR_$_SASampleStore._lastPMIMicrostackshotSampleCount
+ OBJC_IVAR_$_SASampleStore._lastPMIMicrostackshotWallTime
+ OBJC_IVAR_$_SASampleStore._msInFlightChunkGroupData
+ OBJC_IVAR_$_SASampleStore._msInFlightChunkGroupMagic
+ OBJC_IVAR_$_SASampleStore._nandGarbageCollectionEvents
+ OBJC_IVAR_$_SASampleStore._sharedCacheResidentSizeInBytes
+ OBJC_IVAR_$_SASampleStore._sharedCacheVirtualSizeInBytes
+ OBJC_IVAR_$_SASharedCache._isExclaveSharedCache
+ OBJC_IVAR_$_SAStack._isKernel
+ _OBJC_CLASS_$_SABootInfo
+ _OBJC_CLASS_$_SANANDGarbageCollectionEvent
+ _OBJC_METACLASS_$_SABootInfo
+ _OBJC_METACLASS_$_SANANDGarbageCollectionEvent
+ _SA_TSPMetadata_SharedCacheInfo
+ _SA_TSPMetadata_SharedCacheResidentSize
+ _SA_TSPMetadata_SharedCacheVirtualSize
+ _StringForMicrostackshotStateQoS
+ __100-[SASampleStore _addMicrostackshotFromData:ofTypes:inTimeRangeStart:end:onlyPid:onlyTid:statistics:]_block_invoke.507
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1447
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1454
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1457
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1462
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1466
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1470
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1463
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1467
+ __110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1856
+ __110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1860
+ __116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.314
+ __116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.318
+ __116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.319
+ __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1939
+ __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1942
+ __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2292
+ __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2308
+ __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2312
+ __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2254
+ __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2263
+ __264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.367
+ __264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.377
+ __264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.381
+ __28-[SASampleStore postprocess]_block_invoke.218
+ __28-[SASampleStore postprocess]_block_invoke.222
+ __28-[SASampleStore postprocess]_block_invoke.230
+ __28-[SASampleStore postprocess]_block_invoke_2.223
+ __28-[SASampleStore postprocess]_block_invoke_2.234
+ __28-[SASampleStore postprocess]_block_invoke_3.237
+ __28-[SASampleStore symbolicate]_block_invoke.563
+ __28-[SASampleStore symbolicate]_block_invoke.566
+ __28-[SASampleStore symbolicate]_block_invoke.569
+ __28-[SASampleStore symbolicate]_block_invoke.574
+ __28-[SASampleStore symbolicate]_block_invoke.579
+ __28-[SASampleStore symbolicate]_block_invoke.588
+ __28-[SASampleStore symbolicate]_block_invoke_2.580
+ __28-[SASampleStore symbolicate]_block_invoke_2.589
+ __29-[SASamplePrinter preprocess]_block_invoke.1348
+ __29-[SASamplePrinter preprocess]_block_invoke.1352
+ __29-[SASampleStore gatherTrials]_block_invoke.637
+ __29-[SASampleStore gatherTrials]_block_invoke_2.638
+ __30+[SASharedCache addDscSymDir:]_block_invoke.523
+ __30-[SASamplePrinter printHeader]_block_invoke.1037
+ __30-[SASamplePrinter printHeader]_block_invoke.1049
+ __30-[SASamplePrinter printHeader]_block_invoke.1191
+ __30-[SASamplePrinter printHeader]_block_invoke.1246
+ __30-[SASamplePrinter printHeader]_block_invoke.1278
+ __30-[SASamplePrinter printHeader]_block_invoke.1291
+ __30-[SASamplePrinter printHeader]_block_invoke_2.1161
+ __30-[SASamplePrinter printHeader]_block_invoke_2.1192
+ __30-[SASamplePrinter printHeader]_block_invoke_2.1247
+ __31+[SASharedCache addDSCSymData:]_block_invoke.576
+ __31+[SASharedCache addDSCSymData:]_block_invoke.579
+ __37-[SASamplePrinter checkForBadOptions]_block_invoke.357
+ __37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2653
+ __37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2658
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1365
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1370
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1375
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1394
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1366
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1371
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1376
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_3.1367
+ __44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1405
+ __461-[SASamplePrinter stateChangeStringForThreadState:serialDispatchQueue:swiftTaskStates:thread:threadStateIndexes:taskState:task:iteratorIndex:missingStateIsInAnotherStack:numSamplesOmittedSincePreviousDisplayedSample:sampleTimestamp:previousSampleTimestamp:previousDisplayedTimestamp:previousTaskState:previousThread:previousThreadState:dispatchQueueChanges:swiftTaskChanges:priorityChanges:nameChanges:threadChanges:isTimeJump:ioEventsSincePreviousThreadState:]_block_invoke.2234
+ __461-[SASamplePrinter stateChangeStringForThreadState:serialDispatchQueue:swiftTaskStates:thread:threadStateIndexes:taskState:task:iteratorIndex:missingStateIsInAnotherStack:numSamplesOmittedSincePreviousDisplayedSample:sampleTimestamp:previousSampleTimestamp:previousDisplayedTimestamp:previousTaskState:previousThread:previousThreadState:dispatchQueueChanges:swiftTaskChanges:priorityChanges:nameChanges:threadChanges:isTimeJump:ioEventsSincePreviousThreadState:]_block_invoke.2238
+ __48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.554
+ __48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.557
+ __48-[SASamplePrinter copyDescriptionForTimeRanges:]_block_invoke.2421
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1908
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1912
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1914
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1917
+ __49-[SASampleStore symbolicateViaBulkSymbolication:]_block_invoke.531
+ __49-[SASampleStore symbolicateViaBulkSymbolication:]_block_invoke.534
+ __49-[SASampleStore symbolicateViaBulkSymbolication:]_block_invoke.542
+ __50-[SASamplePrinter sortedLoadInfosForBinaryImages:]_block_invoke.1774
+ __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke.1820
+ __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke.1824
+ __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke_2.1828
+ __53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.381
+ __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.86
+ __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.92
+ __56-[SASamplePrinter stacksForThread:task:taskSampleCount:]_block_invoke.1927
+ __56-[SASampleStore(SASampleStoreNSCoding) encodeWithCoder:]_block_invoke.1415
+ __58-[SASamplePrinter printLaunchdThrottledProcessesToStream:]_block_invoke.425
+ __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke.2350
+ __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke_2.2351
+ __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1895
+ __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1902
+ __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke_2.1896
+ __65-[SASamplePrinter displayStringForOnBehalfOfForTasks:includePid:]_block_invoke.2604
+ __77-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]_block_invoke.403
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.232
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.235
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.240
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.248
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.276
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.289
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.297
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.310
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.327
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.335
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.344
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.347
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.351
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.314
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.328
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.338
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.329
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.341
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.150
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.158
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.161
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.167
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.170
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.176
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.182
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.187
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.192
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.196
+ __OBJC_$_CLASS_METHODS_SABootInfo(Serialization|JSONSerialization)
+ __OBJC_$_CLASS_METHODS_SANANDGarbageCollectionEvent(Serialization|JSONSerialization)
+ __OBJC_$_INSTANCE_METHODS_SABootInfo(Serialization|JSONSerialization)
+ __OBJC_$_INSTANCE_METHODS_SANANDGarbageCollectionEvent(Serialization|JSONSerialization)
+ __OBJC_$_INSTANCE_VARIABLES_SABootInfo
+ __OBJC_$_INSTANCE_VARIABLES_SANANDGarbageCollectionEvent
+ __OBJC_CLASS_PROTOCOLS_$_SABootInfo(Serialization|JSONSerialization)
+ __OBJC_CLASS_PROTOCOLS_$_SANANDGarbageCollectionEvent(Serialization|JSONSerialization)
+ __OBJC_CLASS_RO_$_SABootInfo
+ __OBJC_CLASS_RO_$_SANANDGarbageCollectionEvent
+ __OBJC_METACLASS_RO_$_SABootInfo
+ __OBJC_METACLASS_RO_$_SANANDGarbageCollectionEvent
+ __ReadAheadTaskLevelInfo_block_invoke.2022
+ __ReadAheadTaskLevelInfo_block_invoke.2027
+ __ReadAheadTaskLevelInfo_block_invoke.2030
+ __SAKCDataReadAheadJetsamCoalitionInfo_block_invoke.2015
+ __TimerTier
+ __ZN11flatbuffers8Verifier20VerifyVectorOfTablesIN17FlatbufferSymbols19TranslatedImageInfoEEEbPKNS_6VectorINS_6OffsetIT_EEEE
+ __ZNK17FlatbufferSymbols9TimeRange6VerifyERN11flatbuffers8VerifierE
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke
+ ___29-[SATask addOutOfOrderState:]_block_invoke
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke
+ ___39-[SASampleStore gatherSharedCacheStats]_block_invoke
+ ___54-[SASampleStore(SASampleStoreNSCoding) initWithCoder:]_block_invoke_2
+ ___54-[SASampleStore(SASampleStoreNSCoding) initWithCoder:]_block_invoke_3
+ ___56-[SASampleStore(KPerf) kperfRecord:state:frameIterator:]_block_invoke
+ ___75+[SANANDGarbageCollectionEvent parseKTrace:findingGarbageCollectionEvents:]_block_invoke
+ ____debugMicrostackshots_block_invoke
+ ___block_descriptor_198_e8_32s40s48s56s64r72r80r88r96r104r112r120r128r136r144r_e15_v28?08I16^B20l
+ ___block_descriptor_40_ea8_32s_e38_v16?0"SANANDGarbageCollectionEvent"8l
+ ___block_descriptor_48_e8_32bs40bs_e15_v28?08I16^B20l
+ ___block_descriptor_48_e8_32s40s_e35_v32?0"NSNumber"8"SAThread"16^B24l
+ ___block_descriptor_48_ea8_32s_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8l
+ ___block_descriptor_56_e8_32bs40r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8l
+ ___block_descriptor_56_e8_32r40r_e9_v16?0r*8l
+ ___copy_helper_block_e8_32b40b
+ ___copy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r112r120r128r136r144r
+ ___destroy_helper_block_e8_32s40s48s56s64r72r80r88r96r104r112r120r128r136r144r
+ ___snprintf_chk
+ __block_literal_global.1040
+ __block_literal_global.1249
+ __block_literal_global.1777
+ __block_literal_global.1827
+ __block_literal_global.1831
+ __block_literal_global.1904
+ __block_literal_global.198
+ __block_literal_global.2005
+ __block_literal_global.2010
+ __block_literal_global.204
+ __block_literal_global.2041
+ __block_literal_global.2060
+ __block_literal_global.2075
+ __block_literal_global.2077
+ __block_literal_global.219
+ __block_literal_global.2251
+ __block_literal_global.2266
+ __block_literal_global.233
+ __block_literal_global.2354
+ __block_literal_global.236
+ __block_literal_global.239
+ __block_literal_global.2612
+ __block_literal_global.2646
+ __block_literal_global.2655
+ __block_literal_global.266
+ __block_literal_global.268
+ __block_literal_global.289
+ __block_literal_global.337
+ __block_literal_global.340
+ __block_literal_global.353
+ __block_literal_global.362
+ __block_literal_global.369
+ __block_literal_global.476
+ __block_literal_global.503
+ __block_literal_global.509
+ __block_literal_global.520
+ __block_literal_global.539
+ __block_literal_global.556
+ __block_literal_global.591
+ __block_literal_global.593
+ __block_literal_global.601
+ __block_literal_global.603
+ __block_literal_global.610
+ __block_literal_global.629
+ __block_literal_global.669
+ __block_literal_global.681
+ __block_literal_global.861
+ _dyld_shared_cache_for_each_file
+ _mach_error_string
+ _mincore
+ _objc_msgSend$binaryLoadInfoForLiveProcessWithPid:dataGatheringOptions:additionalCSSymbolicatorFlags:mainBinaryOut:sharedCacheOut:
+ _objc_msgSend$bootCycles
+ _objc_msgSend$bytes_other_data
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$deltaMachTo:timeDomainPriorityList:timeDomainUsed:
+ _objc_msgSend$deltaSecondsWithTimeDomainPriorityList:timeDomainUsed:
+ _objc_msgSend$nandGarbageCollectionEvents
+ _objc_msgSend$setBytes_other_data:
+ _objc_msgSend$setMachineArchitecture:
+ _objc_msgSend$sharedCacheResidentSizeInBytes
+ _objc_msgSend$sharedCacheVirtualSizeInBytes
+ _objc_msgSend$wallTimeAtMachAbsZero
- -[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]
- -[SASamplePrinter indexForBinary:]
- GCC_except_table120
- GCC_except_table149
- GCC_except_table153
- GCC_except_table154
- GCC_except_table172
- GCC_except_table175
- GCC_except_table192
- GCC_except_table194
- GCC_except_table196
- GCC_except_table209
- GCC_except_table210
- GCC_except_table213
- GCC_except_table217
- GCC_except_table221
- GCC_except_table224
- GCC_except_table225
- GCC_except_table230
- GCC_except_table232
- GCC_except_table236
- GCC_except_table24
- GCC_except_table252
- GCC_except_table268
- GCC_except_table27
- GCC_except_table286
- GCC_except_table287
- GCC_except_table29
- GCC_except_table30
- GCC_except_table33
- GCC_except_table46
- GCC_except_table501
- GCC_except_table504
- GCC_except_table507
- GCC_except_table54
- GCC_except_table61
- GCC_except_table66
- GCC_except_table86
- GCC_except_table87
- GCC_except_table92
- OBJC_IVAR_$_SAKPerfState._mostRecentSampleIsPET
- _ReduceToSignificantDigits
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1414
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1421
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1424
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1429
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1433
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1437
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1430
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1434
- __110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1822
- __110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1826
- __116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.268
- __116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke.272
- __116-[SASampleStore _addKCDataStackshot:timestamp:sampleIndex:shouldSkipSampleOut:primaryDataIsKPerf:addStaticInfoOnly:]_block_invoke_2.273
- __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1905
- __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1908
- __125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2260
- __125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2268
- __125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2273
- __125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2289
- __125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke.2293
- __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2220
- __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2229
- __264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.321
- __264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.331
- __264-[SASampleStore _parseKCDataTaskContainer:timestampOfSample:sampleIndex:sharedCaches:frameIterator:primaryDataIsKPerf:addStaticInfoOnly:taskUniquePidsInThisSample:taskPidsInThisSample:importanceDonations:rPidForJetsamCoalitionId:port_label_info_array:exclaveInfo:]_block_invoke.335
- __28-[SASampleStore postprocess]_block_invoke.172
- __28-[SASampleStore postprocess]_block_invoke.176
- __28-[SASampleStore postprocess]_block_invoke.184
- __28-[SASampleStore postprocess]_block_invoke_2.177
- __28-[SASampleStore postprocess]_block_invoke_2.188
- __28-[SASampleStore postprocess]_block_invoke_3.191
- __28-[SASampleStore symbolicate]_block_invoke.443
- __28-[SASampleStore symbolicate]_block_invoke.446
- __28-[SASampleStore symbolicate]_block_invoke.449
- __28-[SASampleStore symbolicate]_block_invoke.454
- __28-[SASampleStore symbolicate]_block_invoke.459
- __28-[SASampleStore symbolicate]_block_invoke.468
- __28-[SASampleStore symbolicate]_block_invoke_2.460
- __28-[SASampleStore symbolicate]_block_invoke_2.469
- __29-[SASamplePrinter preprocess]_block_invoke.1315
- __29-[SASamplePrinter preprocess]_block_invoke.1319
- __29-[SASampleStore gatherTrials]_block_invoke.514
- __29-[SASampleStore gatherTrials]_block_invoke_2.515
- __30+[SASharedCache addDscSymDir:]_block_invoke.521
- __30-[SASamplePrinter printHeader]_block_invoke.1008
- __30-[SASamplePrinter printHeader]_block_invoke.1013
- __30-[SASamplePrinter printHeader]_block_invoke.1154
- __30-[SASamplePrinter printHeader]_block_invoke.1209
- __30-[SASamplePrinter printHeader]_block_invoke.1242
- __30-[SASamplePrinter printHeader]_block_invoke.1255
- __30-[SASamplePrinter printHeader]_block_invoke_2.1155
- __30-[SASamplePrinter printHeader]_block_invoke_2.1210
- __31+[SASharedCache addDSCSymData:]_block_invoke.574
- __31+[SASharedCache addDSCSymData:]_block_invoke.577
- __37-[SASamplePrinter checkForBadOptions]_block_invoke.356
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1332
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1337
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1342
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1361
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1333
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1338
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1343
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_3.1334
- __44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1372
- __461-[SASamplePrinter stateChangeStringForThreadState:serialDispatchQueue:swiftTaskStates:thread:threadStateIndexes:taskState:task:iteratorIndex:missingStateIsInAnotherStack:numSamplesOmittedSincePreviousDisplayedSample:sampleTimestamp:previousSampleTimestamp:previousDisplayedTimestamp:previousTaskState:previousThread:previousThreadState:dispatchQueueChanges:swiftTaskChanges:priorityChanges:nameChanges:threadChanges:isTimeJump:ioEventsSincePreviousThreadState:]_block_invoke.2200
- __461-[SASamplePrinter stateChangeStringForThreadState:serialDispatchQueue:swiftTaskStates:thread:threadStateIndexes:taskState:task:iteratorIndex:missingStateIsInAnotherStack:numSamplesOmittedSincePreviousDisplayedSample:sampleTimestamp:previousSampleTimestamp:previousDisplayedTimestamp:previousTaskState:previousThread:previousThreadState:dispatchQueueChanges:swiftTaskChanges:priorityChanges:nameChanges:threadChanges:isTimeJump:ioEventsSincePreviousThreadState:]_block_invoke.2204
- __48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.552
- __48+[SASharedCache sharedCacheWithDyldSharedCache:]_block_invoke.555
- __48-[SASamplePrinter copyDescriptionForTimeRanges:]_block_invoke.2402
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1874
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1878
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1880
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1883
- __49-[SASampleStore symbolicateViaBulkSymbolication:]_block_invoke.411
- __49-[SASampleStore symbolicateViaBulkSymbolication:]_block_invoke.414
- __49-[SASampleStore symbolicateViaBulkSymbolication:]_block_invoke.422
- __50-[SASamplePrinter sortedLoadInfosForBinaryImages:]_block_invoke.1741
- __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke.1787
- __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke.1790
- __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke_2.1794
- __53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.362
- __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.80
- __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.85
- __56-[SASamplePrinter stacksForThread:task:taskSampleCount:]_block_invoke.1893
- __56-[SASampleStore(SASampleStoreNSCoding) encodeWithCoder:]_block_invoke.1293
- __58-[SASamplePrinter printLaunchdThrottledProcessesToStream:]_block_invoke.424
- __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke.2331
- __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke_2.2332
- __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1758
- __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1765
- __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke_2.1759
- __65-[SASamplePrinter displayStringForOnBehalfOfForTasks:includePid:]_block_invoke.2585
- __77-[SASampleStore parseKCDataExclavesContainer:exclaveInfo:primaryDataIsKPerf:]_block_invoke.357
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.213
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.216
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.221
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.229
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.257
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.270
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.278
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.291
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.308
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.316
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.325
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.328
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.332
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.295
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.309
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.319
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.310
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.322
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.139
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.142
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.147
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.156
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.159
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.162
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.168
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.177
- __ReadAheadTaskLevelInfo_block_invoke.1797
- __ReadAheadTaskLevelInfo_block_invoke.1802
- __ReadAheadTaskLevelInfo_block_invoke.1805
- __SAKCDataReadAheadJetsamCoalitionInfo_block_invoke.1790
- ___125-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:]_block_invoke
- ___block_descriptor_214_e8_32s40s48s56s64bs72bs80r88r96r104r112r120r128r136r144r152r160r_e15_v28?08I16^B20l
- ___copy_helper_block_e8_32s40s48s56s64b72b80r88r96r104r112r120r128r136r144r152r160r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r136r144r152r160r
- __block_literal_global.1213
- __block_literal_global.158
- __block_literal_global.1744
- __block_literal_global.1767
- __block_literal_global.1780
- __block_literal_global.1785
- __block_literal_global.1793
- __block_literal_global.1797
- __block_literal_global.1832
- __block_literal_global.1847
- __block_literal_global.1849
- __block_literal_global.187
- __block_literal_global.193
- __block_literal_global.199
- __block_literal_global.220
- __block_literal_global.2217
- __block_literal_global.222
- __block_literal_global.2232
- __block_literal_global.2253
- __block_literal_global.2262
- __block_literal_global.2335
- __block_literal_global.243
- __block_literal_global.2593
- __block_literal_global.316
- __block_literal_global.318
- __block_literal_global.321
- __block_literal_global.323
- __block_literal_global.334
- __block_literal_global.386
- __block_literal_global.471
- __block_literal_global.474
- __block_literal_global.481
- __block_literal_global.483
- __block_literal_global.490
- __block_literal_global.506
- __block_literal_global.514
- __block_literal_global.537
- __block_literal_global.546
- __block_literal_global.554
- __block_literal_global.558
- __block_literal_global.857
- _fmod
- _objc_msgSend$deltaMachAbsTimeSeconds
- _objc_msgSend$deltaMachContTimeSeconds
- _objc_msgSend$deltaWallTime
CStrings:
+ " (Exclave)"
+ "%'llu %zu/%zu %s\n"
+ "%'llu Dead reckoned %d samples\n"
+ "%'llu Ignoring PET Sample at %s due to existing PET sample at %s (%lld before most recent event with period %llu)\n\n"
+ "%*s%s: layoutid %llu, flags 0x%llx, sharedcache_index %u%s\n"
+ "%-*s%.0f%% (%.2fs/%.2fs, %@)\n"
+ "%-*s%0.02f%% (%@ / %@)\n"
+ "%.0fs gap with no PMI microstackshots (but none missing) between %@ and %@"
+ "%.0fs gap with no PMI microstackshots between %@ and %@"
+ "%@ %@ %@ (%@) build %@, kernel %@, bootargs %@"
+ "%d load infos were null (%d non-null)"
+ "%llu missing PMI microstackshots between %@ and %@"
+ "%s: after serializing (with %u rootFrames, %u loadInfos), ended with length %ld, should be %lu"
+ "((void*)(additions + 1)) - ((void*)serializedExclave) <= (long) [self sizeInBytesForSerializedVersion]"
+ "(entire binary)"
+ "/"
+ "@48@0:8i16Q20I28^@32^@40"
+ "All %d load infos were null"
+ "B40@0:8^{?=CCQdQQQQQ}16Q24@32"
+ "Bad UUID for load info entry: %@"
+ "Captured %{iec-bytes}u of 0x%x (%{iec-bytes}lu total), waiting for needed following chunk"
+ "Exclave %@ has shared cache index %u, but only %lu load infos"
+ "Found invalid chunk 0x%x length %u"
+ "GC reason:%@(%llu) %@ - %@"
+ "Ignoring systemstats backwards compatibility chunk"
+ "Including 0x%x microstackshot for %s [%d] thread 0x%llx at %@"
+ "Invalid data following boot info header (%{iec-bytes}u)"
+ "Invalid data following dscsym header (%{iec-bytes}u)"
+ "Invalid data following dscsym header (%{iec-bytes}u), lost %{iec-bytes}lu of data in the preceding chunk!"
+ "Kernel callstacks for non-kernel tasks in microstackshots is unsupported"
+ "Load info for unexpected pid %d"
+ "Load info with no pid"
+ "Low mem"
+ "Low validity bands"
+ "MAX_CHUNK_SIZE 0x%x isn't a page multiple 0x%lx"
+ "Microstackshot statistics:\n%llu bytes parsed (%llu ms, %llu non-ms, %llu invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
+ "Missing case for systemstats micro chunk %u"
+ "Must move data"
+ "NAND Garbage Collection: "
+ "No UUID for load info entry"
+ "No load address for load info entry %@ segment %@"
+ "No threads for %@, not including in report"
+ "Not dead-reckoning samples"
+ "Not including duplicate microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
+ "Not including microstackshot for %s [%d] at %@ due to being too early (%fs)"
+ "Not including microstackshot for %s [%d] at %@ due to being too late (%fs)"
+ "Not including microstackshot for %s [%d] at %@ due to being wrong pid (requested %d)"
+ "Not including microstackshot for %s [%d] at %@ due to being wrong thread (0x%llx, requested 0x%llx)"
+ "Not including microstackshot for %s [%d] at %@ due to being wrong type (0x%x, requested 0x%x)"
+ "Not including microstackshot for %s [%d] at %@ due to no load info"
+ "Not including out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall, %fs for this thread)"
+ "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) first sample for this thread"
+ "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs"
+ "Out-of-order microstackshot for %s [%d] thread 0x%llx at %@ (by %fs overall) is still after latest microstackshot for that thread by %fs (out of order for task)"
+ "Parsed %{iec-bytes}lu dscysm data in microstackshots stream"
+ "Parsed %{iec-bytes}lu of non-MS data, %{iec-bytes}lu of invalid data"
+ "Parsed boot info in microstackshots stream for %@"
+ "Partial microstackshot (%lu), requesting more data"
+ "Partial microstackshot (%{iec-bytes}lu), requesting more data"
+ "Previous %{iec-bytes}lu chunk 0x%x missing needed followup chunk"
+ "Resume after power loss"
+ "Room for OSLC"
+ "SABootInfo"
+ "SANANDGarbageCollectionEvent"
+ "SA_DEAD_RECKONING"
+ "SA_LOG_MICROSTACKSHOTS"
+ "SLC idle"
+ "SLC low on space"
+ "Shared cache residency: "
+ "SharedCacheInfo"
+ "SharedCacheSizeResident"
+ "SharedCacheSizeVirtual"
+ "SystemStats boot info dict isn't a dictionary: %s"
+ "T@\"NSArray\",R,V_bootCycles"
+ "T@\"NSArray\",R,V_nandGarbageCollectionEvents"
+ "T@\"NSString\",R,V_bootArgs"
+ "T@\"NSString\",R,V_osBuildVersion"
+ "T@\"NSString\",R,V_osProductVersion"
+ "T@\"NSString\",R,V_osProductVersionExtra"
+ "T@\"SASharedCache\",R,V_sharedCache"
+ "TLC idle"
+ "TLC low on space"
+ "TQ,V_bytes_other_data"
+ "Task %@ exit at %@, but has later timestamp %@, pushing exit out"
+ "Td,R,V_wallTimeAtMachAbsZero"
+ "Unknown SABootInfo version"
+ "Unknown SANANDGarbageCollectionEvent version"
+ "Virtual card ingest"
+ "_bootCycles"
+ "_bytes_other_data"
+ "_isExclaveSharedCache"
+ "_isKernel"
+ "_lastPMIMicrostackshotSampleCount"
+ "_lastPMIMicrostackshotWallTime"
+ "_msInFlightChunkGroupData"
+ "_msInFlightChunkGroupMagic"
+ "_nandGarbageCollectionEvents"
+ "_petTimerMostRecentSampleWasDeadReckoned"
+ "_petTimerNextExpectedSampleMachAbs"
+ "_petTimerPeriodMachAbs"
+ "_reasonCode"
+ "_sharedCacheResidentSizeInBytes"
+ "_sharedCacheVirtualSizeInBytes"
+ "_timestampAfterTimeAdjustments"
+ "_timestampBeforeAnyTimeAdjustments"
+ "_wallTimeAtMachAbsZero"
+ "binaryLoadInfoForLiveProcessWithPid:dataGatheringOptions:additionalCSSymbolicatorFlags:mainBinaryOut:sharedCacheOut:"
+ "bootCycles"
+ "boot_args"
+ "bufferLength %lu < serialized SABootInfo struct %lu"
+ "bufferLength %lu < serialized SAExclave struct v2 with %u root frames, %u image infos"
+ "bufferLength %lu < serialized SANANDGarbageCollectionEvent struct %lu"
+ "bufferLength >= sizeof(*serializedBootInfo)"
+ "bufferLength >= sizeof(*serializedNANDGarbageCollectionEvent)"
+ "bufferLength >= sizeof(*serializedSharedCache) + (sizeof(SASerializedIndex) * serializedSharedCache->numBinaryLoadInfos) + sizeof(SASerializedSharedCache_v4_additions)"
+ "bytes_other_data"
+ "componentsSeparatedByString:"
+ "d32@0:8@16^Q24"
+ "deltaMachWithTimeDomainPriorityList:timeDomainUsed:"
+ "deltaSecondsWithTimeDomainPriorityList:timeDomainUsed:"
+ "failed to create dyld process:%d (%s)"
+ "failed to create snapshot of the process:%d (%s)"
+ "failed to fstat shared cache file %s: %{errno}d"
+ "failed to get shared cache"
+ "failed to open shared cache file %s: %{errno}d"
+ "hw_page_size"
+ "kernel_version"
+ "load_address"
+ "load_info_entries"
+ "load_infos"
+ "mach_timebase"
+ "machine_arch"
+ "main_binary_uuid"
+ "mincore of 0x%llx,0x%zx of shared cache file %s failed: %{errno}d"
+ "mmap of 0x%llx,0x%zx of shared cache file %s failed: %{errno}d"
+ "munmap of 0x%llx,0x%zx of shared cache file %s failed: %{errno}d"
+ "nandGarbageCollectionEvents"
+ "native shared cache has %llu/%llu pages resident"
+ "os_build_version"
+ "os_product_name"
+ "os_product_version"
+ "os_product_version_extra"
+ "q32@0:8@16^Q24"
+ "r^{exclave_textlayout_info=QQI}"
+ "reasonCode"
+ "round_page(MAX_CHUNK_SIZE) == MAX_CHUNK_SIZE"
+ "setBytes_other_data:"
+ "shared cache file %s has %llu/%llu pages resident"
+ "sharedCacheResidencyPercent"
+ "sharedCacheResidentSize"
+ "sharedCacheResidentSizeInBytes"
+ "sharedCacheVirtualSize"
+ "sharedCacheVirtualSizeInBytes"
+ "unknown(%llu)"
+ "v16@?0@\"SANANDGarbageCollectionEvent\"8"
+ "v16@?0r*8"
+ "vm_page_size"
+ "wallTimeAtMachAbsZero"
+ "walltime"
- "0"
- "Bad PASerializedSymbolDataStore magic"
- "Microstackshot buffer doesn't contain task_snapshot after micro_snapshot"
- "Microstackshot buffer doesn't contain thread_snapshot after task_snapshot"
- "Microstackshot buffer doesn't start with micro_snapshot"
- "Microstackshot statistics:\n%llu bytes parsed (%llu bytes invalid)\n%llu filtered out\n\ntotal     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ninterrupt count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\ntimer     count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nio        count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\npmi       count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nmacf      count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)\n\nunknown   count          %llu (%llu bytes)\n          num_load_infos %llu\n          num_frames     %llu\n          duplicate      %llu (%llu bytes)\n          out_of_order   %llu (%llu bytes)\n          no_load_info   %llu (%llu bytes)"
- "Not including microstackshot for %s [%d] at %s due being out of order (before previous by %fs)"
- "Remaining %lu bytes do not contain any microstackshots"
- "Skipping %lu bytes until next microstackshot in the buffer"
- "_mostRecentSampleIsPET"
- "r^{exclave_textlayout_info=QQ}"

```
