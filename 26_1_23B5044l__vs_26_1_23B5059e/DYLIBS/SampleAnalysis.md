## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-412.0.0.0.0
-  __TEXT.__text: 0xee5c8
+413.0.0.0.0
+  __TEXT.__text: 0xf0330
   __TEXT.__auth_stubs: 0x1760
-  __TEXT.__objc_methlist: 0x5d64
+  __TEXT.__objc_methlist: 0x5e9c
   __TEXT.__const: 0x348
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x17fb5
-  __TEXT.__oslogstring: 0xc632
-  __TEXT.__gcc_except_tab: 0x9b58
-  __TEXT.__unwind_info: 0x20c8
-  __TEXT.__objc_classname: 0xb12
-  __TEXT.__objc_methname: 0xd8ae
-  __TEXT.__objc_methtype: 0x1a1c
-  __TEXT.__objc_stubs: 0x7d20
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x3710
-  __DATA_CONST.__objc_classlist: 0x408
+  __TEXT.__cstring: 0x1839e
+  __TEXT.__oslogstring: 0xc66a
+  __TEXT.__gcc_except_tab: 0x9d94
+  __TEXT.__unwind_info: 0x2118
+  __TEXT.__objc_classname: 0xb34
+  __TEXT.__objc_methname: 0xd955
+  __TEXT.__objc_methtype: 0x1a44
+  __TEXT.__objc_stubs: 0x7e00
+  __DATA_CONST.__got: 0x3e8
+  __DATA_CONST.__const: 0x3b80
+  __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2960
+  __DATA_CONST.__objc_selrefs: 0x29a0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2a0
-  __DATA_CONST.__objc_arraydata: 0x1d0
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __DATA_CONST.__objc_arraydata: 0x1e8
   __AUTH_CONST.__auth_got: 0xbc8
   __AUTH_CONST.__const: 0xb00
-  __AUTH_CONST.__cfstring: 0xc9c0
-  __AUTH_CONST.__objc_const: 0x10268
+  __AUTH_CONST.__cfstring: 0xd0a0
+  __AUTH_CONST.__objc_const: 0x104f0
   __AUTH_CONST.__objc_intobj: 0x2a0
-  __AUTH_CONST.__objc_arrayobj: 0x210
+  __AUTH_CONST.__objc_arrayobj: 0x228
+  __AUTH.__objc_data: 0xa0
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xd24
+  __DATA.__objc_ivar: 0xd34
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x30

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7E38280C-8A71-3578-B4BA-E0424B88326A
-  Functions: 2799
-  Symbols:   9604
-  CStrings:  8433
+  UUID: 1FE43654-1E8E-31E4-BD3E-27E8D9119885
+  Functions: 2829
+  Symbols:   9704
+  CStrings:  8568
 
Symbols:
+ +[SALostPerfEvent parseKTrace:findingLostPerfEvents:]
+ +[SALostPerfEvent(Serialization) classDictionaryKey]
+ +[SALostPerfEvent(Serialization) newInstanceWithoutReferencesFromSerializedBuffer:bufferLength:]
+ -[SALostPerfEvent .cxx_destruct]
+ -[SALostPerfEvent debugDescription]
+ -[SALostPerfEvent domain]
+ -[SALostPerfEvent endTime]
+ -[SALostPerfEvent initWithStartTime:]
+ -[SALostPerfEvent lostPerf]
+ -[SALostPerfEvent mode]
+ -[SALostPerfEvent source]
+ -[SALostPerfEvent startTime]
+ -[SALostPerfEvent type]
+ -[SALostPerfEvent(SAJSONSerialization) writeJSONDictionaryEntriesToStream:]
+ -[SALostPerfEvent(Serialization) addSelfToBuffer:bufferLength:withCompletedSerializationDictionary:]
+ -[SALostPerfEvent(Serialization) addSelfToSerializationDictionary:]
+ -[SALostPerfEvent(Serialization) populateReferencesUsingBuffer:bufferLength:andDeserializationDictionary:andDataBufferDictionary:]
+ -[SALostPerfEvent(Serialization) sizeInBytesForSerializedVersion]
+ -[SALostPerfEventV7 domain]
+ -[SALostPerfEventV7 initWithStartTime:reason:]
+ -[SALostPerfEventV7 lostPerf]
+ -[SALostPerfEventV7 mode]
+ -[SALostPerfEventV7 source]
+ -[SALostPerfEventV7 type]
+ -[SASampleStore deadReckonSamplesBeforeTimestamp:timestampIsSampleEvent:kperfState:]
+ -[SASampleStore lostPerfEvents]
+ -[SASampleStore setEndTime:]
+ -[SASampleStore setStartTime:]
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table114
+ GCC_except_table132
+ GCC_except_table181
+ GCC_except_table214
+ GCC_except_table236
+ GCC_except_table265
+ GCC_except_table280
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table541
+ GCC_except_table544
+ GCC_except_table549
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table77
+ GCC_except_table95
+ _.str.161
+ _OBJC_CLASS_$_SALostPerfEvent
+ _OBJC_CLASS_$_SALostPerfEventV7
+ _OBJC_IVAR_$_SALostPerfEvent._endTime
+ _OBJC_IVAR_$_SALostPerfEvent._startTime
+ _OBJC_IVAR_$_SALostPerfEventV7._reason
+ _OBJC_IVAR_$_SASampleStore._lostPerfEvents
+ _OBJC_METACLASS_$_SALostPerfEvent
+ _OBJC_METACLASS_$_SALostPerfEventV7
+ __OBJC_$_CLASS_METHODS_SALostPerfEvent(SAJSONSerialization|Serialization)
+ __OBJC_$_INSTANCE_METHODS_SALostPerfEvent(SAJSONSerialization|Serialization)
+ __OBJC_$_INSTANCE_METHODS_SALostPerfEventV7
+ __OBJC_$_INSTANCE_VARIABLES_SALostPerfEvent
+ __OBJC_$_INSTANCE_VARIABLES_SALostPerfEventV7
+ __OBJC_CLASS_PROTOCOLS_$_SALostPerfEvent(SAJSONSerialization|Serialization)
+ __OBJC_CLASS_RO_$_SALostPerfEvent
+ __OBJC_CLASS_RO_$_SALostPerfEventV7
+ __OBJC_METACLASS_RO_$_SALostPerfEvent
+ __OBJC_METACLASS_RO_$_SALostPerfEventV7
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1537
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1541
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1544
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1538
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1545
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1998
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.2000
+ ___116-[SASampleStore(KPerf) addLoadInfoFromKTrace:lastKTraceEventTimestamp:checkForNewLoadInfosEvenWithExistingLoadInfo:]_block_invoke.190
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.162
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.167
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_16
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.163
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.168
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_3.171
+ ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_4.172
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2471
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2487
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2433
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2442
+ ___29-[SASampleStore gatherTrials]_block_invoke.549
+ ___29-[SASampleStore gatherTrials]_block_invoke_2.550
+ ___30-[SASamplePrinter printHeader]_block_invoke.1352
+ ___30-[SASamplePrinter printHeader]_block_invoke.1379
+ ___30-[SASamplePrinter printHeader]_block_invoke.1386
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1353
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1399
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2791
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2796
+ ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.631
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1480
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1486
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1490
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2048
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2049
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2050
+ ___53+[SALostPerfEvent parseKTrace:findingLostPerfEvents:]_block_invoke
+ ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.356
+ ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.105
+ ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.99
+ ___91-[SASampleStore(KPerf) deadReckonSamplesBeforeTimestamp:timestampIsSampleEvent:kperfState:]_block_invoke
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.219
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.231
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.257
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.276
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.290
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.309
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.320
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.268
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.283
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.294
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.312
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.326
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.307
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.315
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_4.316
+ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_5.319
+ ___ReadAheadTaskLevelInfo_block_invoke.2054
+ ___ReadAheadTaskLevelInfo_block_invoke.2059
+ ___ReadAheadTaskLevelInfo_block_invoke.2062
+ ___block_descriptor_121_ea8_32s40s48s56s64s72r80r88r96r104r_e5_v8?0ls32l8s40l8s48l8r72l8r80l8r88l8s56l8s64l8r96l8r104l8
+ ___block_descriptor_270_ea8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r144r152r160r168r176r184r192r200r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8r136l8s48l8r144l8r152l8s56l8s64l8r160l8s72l8s80l8s88l8s96l8r168l8s104l8s112l8r176l8r184l8r192l8s120l8r200l8s128l8
+ ___block_descriptor_40_ea8_32s_e25_v16?0"SALostPerfEvent"8ls32l8
+ ___block_descriptor_64_e8_32bs40r48r_e45_v16?0^{trace_point=QQQQQQII{timeval=qi}**i}8lr40l8r48l8s32l8
+ ___block_literal_global.1164
+ ___block_literal_global.1355
+ ___block_literal_global.1492
+ ___block_literal_global.186
+ ___block_literal_global.192
+ ___block_literal_global.1926
+ ___block_literal_global.1942
+ ___block_literal_global.1971
+ ___block_literal_global.1974
+ ___block_literal_global.2042
+ ___block_literal_global.2047
+ ___block_literal_global.205
+ ___block_literal_global.2073
+ ___block_literal_global.2086
+ ___block_literal_global.2088
+ ___block_literal_global.2430
+ ___block_literal_global.2445
+ ___block_literal_global.2524
+ ___block_literal_global.2762
+ ___block_literal_global.2784
+ ___block_literal_global.2793
+ ___block_literal_global.311
+ ___block_literal_global.314
+ ___block_literal_global.328
+ ___block_literal_global.574
+ ___block_literal_global.578
+ ___block_literal_global.628
+ _domains
+ _lostPerfs
+ _modes
+ _objc_msgSend$domain
+ _objc_msgSend$initWithStartTime:reason:
+ _objc_msgSend$keysSortedByValueUsingSelector:
+ _objc_msgSend$lostPerf
+ _objc_msgSend$lostPerfEvents
+ _objc_msgSend$mode
+ _objc_msgSend$source
+ _sources
+ _types
- -[SASampleStore deadReckonSamplesBeforeTimestamp:kperfState:]
- GCC_except_table112
- GCC_except_table128
- GCC_except_table180
- GCC_except_table213
- GCC_except_table235
- GCC_except_table264
- GCC_except_table279
- GCC_except_table34
- GCC_except_table36
- GCC_except_table39
- GCC_except_table53
- GCC_except_table539
- GCC_except_table54
- GCC_except_table542
- GCC_except_table547
- GCC_except_table59
- GCC_except_table60
- GCC_except_table83
- GCC_except_table86
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1524
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1528
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1531
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1525
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1532
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1985
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1987
- ___116-[SASampleStore(KPerf) addLoadInfoFromKTrace:lastKTraceEventTimestamp:checkForNewLoadInfosEvenWithExistingLoadInfo:]_block_invoke.185
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.160
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke.165
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.161
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_2.166
- ___123-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:afterMachAbsTime:beforeMachAbsTime:petTimerID:ktraceDataUnavailable:]_block_invoke_3.169
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2458
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2474
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2420
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2429
- ___29-[SASampleStore gatherTrials]_block_invoke.558
- ___29-[SASampleStore gatherTrials]_block_invoke_2.559
- ___30-[SASamplePrinter printHeader]_block_invoke.1339
- ___30-[SASamplePrinter printHeader]_block_invoke.1366
- ___30-[SASamplePrinter printHeader]_block_invoke.1373
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1340
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1386
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2778
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2783
- ___40-[SASampleStore gatherRootInstalledInfo]_block_invoke.640
- ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1467
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1473
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1477
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2035
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2036
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2037
- ___53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.347
- ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.103
- ___55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.97
- ___68-[SASampleStore(KPerf) deadReckonSamplesBeforeTimestamp:kperfState:]_block_invoke
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.214
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.226
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.252
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.271
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.285
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.304
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke.313
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.263
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.278
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.289
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.307
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_2.317
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.302
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3.310
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_4.311
- ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_5.312
- ___ReadAheadTaskLevelInfo_block_invoke.2055
- ___ReadAheadTaskLevelInfo_block_invoke.2060
- ___ReadAheadTaskLevelInfo_block_invoke.2063
- ___block_descriptor_113_ea8_32s40s48s56s64r72r80r88r96r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8r80l8s56l8r88l8r96l8
- ___block_descriptor_262_ea8_32s40s48s56s64s72s80s88s96s104s112s120s128r136r144r152r160r168r176r184r192r_e30_v32?0"SAThreadState"8Q16^B24ls32l8s40l8r128l8s48l8r136l8r144l8s56l8s64l8r152l8s72l8s80l8r160l8s88l8s96l8r168l8r176l8r184l8s104l8r192l8s112l8s120l8
- ___block_literal_global.1151
- ___block_literal_global.1342
- ___block_literal_global.1479
- ___block_literal_global.181
- ___block_literal_global.187
- ___block_literal_global.1913
- ___block_literal_global.1943
- ___block_literal_global.1958
- ___block_literal_global.1961
- ___block_literal_global.200
- ___block_literal_global.2043
- ___block_literal_global.2048
- ___block_literal_global.2074
- ___block_literal_global.2087
- ___block_literal_global.2089
- ___block_literal_global.2417
- ___block_literal_global.2432
- ___block_literal_global.2511
- ___block_literal_global.2749
- ___block_literal_global.2771
- ___block_literal_global.2780
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.319
- ___block_literal_global.583
- ___block_literal_global.587
- ___block_literal_global.637
CStrings:
+ "%'llu Clearing on-core state for thread 0x%llx \n"
+ "%'llu Created %s-core threadState (index %lu) for thread 0x%llx (sample index %ld-%ld, machabs %llu-%llu) with kernel leaf frame 0x%llx exclaves:%d\n"
+ "%'llu Done parsing ending stackshot %lu (past end of ktrace data)\n"
+ "%'llu Done parsing stackshot %lu\n"
+ "%'llu Not dead-reckoning sample at %llu due to real sample at %llu\n"
+ "%'llu Parsing stackshot %lu\n"
+ "%'llu Parsing stackshot %lu (past end of ktrace data)\n"
+ "%@ %@ (%.0f%%)"
+ "@28@0:8@16I24"
+ "ADAPTDIS"
+ "AGX"
+ "ARCHILIM"
+ "ARCHTEMP"
+ "ARCHTRTL"
+ "B40@0:8^{?=CCQQI}16Q24@32"
+ "CLKILIM"
+ "CLKTEMP"
+ "CLKTRTL"
+ "CLPC"
+ "CPUZONE"
+ "Control Effort"
+ "Current"
+ "DRAMTEMP"
+ "EMPTYBAT"
+ "FANNOISE"
+ "FASTCHRG"
+ "FASTTEMP"
+ "FDIE_LTS"
+ "HEATPIPE"
+ "HIP"
+ "HighPower"
+ "INTELBAT"
+ "KPerf timer %d has no action, ignoring"
+ "LONGCHRG"
+ "LOWPOWER"
+ "LTSVCAP"
+ "Lost Perf: "
+ "Lost perf %@ %@ - %@"
+ "LowPower"
+ "NOTSET"
+ "No lost perf"
+ "Noise"
+ "OTHER"
+ "PKGZONE"
+ "PMU"
+ "PMUEM"
+ "PMUTEMP"
+ "PPM"
+ "PREPCKUP"
+ "PSUTEMP"
+ "SALostPerfEvent"
+ "SALostPerfEventV7"
+ "SDIETEMP"
+ "SKINTEMP"
+ "SLOWTEMP"
+ "SMC FAST"
+ "SMC SLOW"
+ "SUSTAIN"
+ "SYSZONE"
+ "SilentRunning"
+ "State"
+ "State Of Charge"
+ "T@\"NSArray\",R,V_lostPerfEvents"
+ "UPO-AV"
+ "Unknown"
+ "Unknown SALostPerfEvent version"
+ "_lostPerfEvents"
+ "bufferLength %lu < serialized SALostPerfEvent struct %lu"
+ "bufferLength >= sizeof(*serializedLostPerfEvent)"
+ "domain"
+ "initWithStartTime:"
+ "initWithStartTime:reason:"
+ "keysSortedByValueUsingSelector:"
+ "lostPerf"
+ "lostPerfEvents"
+ "mode"
+ "source"
+ "v16@?0@\"SALostPerfEvent\"8"
- "%'llu Created %s-core threadState (index %lu) for thread 0x%llx (sample index %ld-%ld, machabs %llu-%llu) with kernel leaf frame 0x%llx) exclaves:%d\n"
- "IconServices"
- "KPerf timer %d  has no action, ignoring"
- "Solarium"
- "SwiftUI"

```
