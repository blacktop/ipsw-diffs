## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis`

```diff

-385.13.0.0.0
-  __TEXT.__text: 0x103948
-  __TEXT.__auth_stubs: 0x1830
-  __TEXT.__objc_methlist: 0x5ac4
+385.14.0.0.0
+  __TEXT.__text: 0x103ecc
+  __TEXT.__auth_stubs: 0x1840
+  __TEXT.__objc_methlist: 0x5adc
   __TEXT.__const: 0x378
   __TEXT.__dlopen_cstrs: 0x16a
-  __TEXT.__cstring: 0x17ae8
-  __TEXT.__oslogstring: 0xc928
-  __TEXT.__gcc_except_tab: 0xa5c8
-  __TEXT.__unwind_info: 0x2180
+  __TEXT.__cstring: 0x17b60
+  __TEXT.__oslogstring: 0xc95f
+  __TEXT.__gcc_except_tab: 0xa618
+  __TEXT.__unwind_info: 0x2190
   __TEXT.__objc_classname: 0xabb
-  __TEXT.__objc_methname: 0xd366
+  __TEXT.__objc_methname: 0xd390
   __TEXT.__objc_methtype: 0x1811
-  __TEXT.__objc_stubs: 0x7e00
+  __TEXT.__objc_stubs: 0x7e40
   __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2908
+  __DATA_CONST.__objc_selrefs: 0x2918
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH_CONST.__auth_got: 0xc38
   __AUTH_CONST.__auth_ptr: 0x38
-  __AUTH_CONST.__const: 0x3de0
-  __AUTH_CONST.__cfstring: 0xbba0
-  __AUTH_CONST.__objc_const: 0xf948
+  __AUTH_CONST.__const: 0x3e10
+  __AUTH_CONST.__cfstring: 0xbbc0
+  __AUTH_CONST.__objc_const: 0xf978
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH.__objc_data: 0x2760
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xccc
+  __DATA.__objc_ivar: 0xcd0
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x40
   __DATA.__bss: 0x510

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2880
-  Symbols:   6889
-  CStrings:  6705
+  Functions: 2884
+  Symbols:   6899
+  CStrings:  6717
 
Symbols:
+ -[SASampleStore memSize]
+ -[SASampleStore setMemSize:]
+ GCC_except_table524
+ GCC_except_table527
+ GCC_except_table532
+ OBJC_IVAR_$_SASampleStore._memSize
+ _SAJSONWriteString
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1451
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1458
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1461
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1474
+ __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1471
+ __110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1864
+ __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1943
+ __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1946
+ __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2296
+ __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2316
+ __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2258
+ __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2267
+ __29-[SASamplePrinter preprocess]_block_invoke.1356
+ __29-[SASampleStore gatherTrials]_block_invoke.638
+ __29-[SASampleStore gatherTrials]_block_invoke_2.639
+ __30-[SASamplePrinter printHeader]_block_invoke.1041
+ __30-[SASamplePrinter printHeader]_block_invoke.1053
+ __30-[SASamplePrinter printHeader]_block_invoke.1195
+ __30-[SASamplePrinter printHeader]_block_invoke.1250
+ __30-[SASamplePrinter printHeader]_block_invoke.1282
+ __30-[SASamplePrinter printHeader]_block_invoke.1295
+ __30-[SASamplePrinter printHeader]_block_invoke_2.1165
+ __30-[SASamplePrinter printHeader]_block_invoke_2.1196
+ __30-[SASamplePrinter printHeader]_block_invoke_2.1251
+ __37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2657
+ __37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2662
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1369
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1374
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1379
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke.1398
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1370
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1375
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1380
+ __41-[SASamplePrinter printTasksIndividually]_block_invoke_3.1371
+ __44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1409
+ __461-[SASamplePrinter stateChangeStringForThreadState:serialDispatchQueue:swiftTaskStates:thread:threadStateIndexes:taskState:task:iteratorIndex:missingStateIsInAnotherStack:numSamplesOmittedSincePreviousDisplayedSample:sampleTimestamp:previousSampleTimestamp:previousDisplayedTimestamp:previousTaskState:previousThread:previousThreadState:dispatchQueueChanges:swiftTaskChanges:priorityChanges:nameChanges:threadChanges:isTimeJump:ioEventsSincePreviousThreadState:]_block_invoke.2242
+ __48-[SASamplePrinter copyDescriptionForTimeRanges:]_block_invoke.2425
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1916
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1918
+ __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1921
+ __50-[SASamplePrinter sortedLoadInfosForBinaryImages:]_block_invoke.1778
+ __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke.1828
+ __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke_2.1832
+ __56-[SASamplePrinter stacksForThread:task:taskSampleCount:]_block_invoke.1931
+ __56-[SASampleStore(SASampleStoreNSCoding) encodeWithCoder:]_block_invoke.1421
+ __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke.2354
+ __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke_2.2355
+ __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1904
+ __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1911
+ __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke_2.1905
+ __65-[SASamplePrinter displayStringForOnBehalfOfForTasks:includePid:]_block_invoke.2608
+ __ReadAheadTaskLevelInfo_block_invoke.2031
+ __ReadAheadTaskLevelInfo_block_invoke.2036
+ __ReadAheadTaskLevelInfo_block_invoke.2039
+ __SAKCDataReadAheadJetsamCoalitionInfo_block_invoke.2024
+ ___SAJSONWriteDictionary_block_invoke
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"816^B24l
+ __block_literal_global.1044
+ __block_literal_global.1253
+ __block_literal_global.1781
+ __block_literal_global.1835
+ __block_literal_global.1913
+ __block_literal_global.2014
+ __block_literal_global.2019
+ __block_literal_global.2050
+ __block_literal_global.2069
+ __block_literal_global.2084
+ __block_literal_global.2086
+ __block_literal_global.2255
+ __block_literal_global.2270
+ __block_literal_global.2358
+ __block_literal_global.2616
+ __block_literal_global.2650
+ __block_literal_global.2659
+ __block_literal_global.630
+ __block_literal_global.670
+ __block_literal_global.682
+ _ktrace_machine_memory_size
+ _objc_msgSend$memSize
+ _objc_msgSend$setMemSize:
- GCC_except_table522
- GCC_except_table525
- GCC_except_table530
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1447
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1454
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1457
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1462
- __103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1463
- __110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1856
- __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1939
- __123-[SASamplePrinter addHeaderForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:toStack:task:taskSampleCount:]_block_invoke.1942
- __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2292
- __134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2308
- __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2254
- __245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2263
- __29-[SASamplePrinter preprocess]_block_invoke.1348
- __29-[SASampleStore gatherTrials]_block_invoke.637
- __29-[SASampleStore gatherTrials]_block_invoke_2.638
- __30-[SASamplePrinter printHeader]_block_invoke.1037
- __30-[SASamplePrinter printHeader]_block_invoke.1049
- __30-[SASamplePrinter printHeader]_block_invoke.1191
- __30-[SASamplePrinter printHeader]_block_invoke.1246
- __30-[SASamplePrinter printHeader]_block_invoke.1278
- __30-[SASamplePrinter printHeader]_block_invoke.1291
- __30-[SASamplePrinter printHeader]_block_invoke_2.1161
- __30-[SASamplePrinter printHeader]_block_invoke_2.1192
- __30-[SASamplePrinter printHeader]_block_invoke_2.1247
- __37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2653
- __37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2658
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1365
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1370
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1375
- __41-[SASamplePrinter printTasksIndividually]_block_invoke.1394
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1366
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1371
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_2.1376
- __41-[SASamplePrinter printTasksIndividually]_block_invoke_3.1367
- __44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1405
- __461-[SASamplePrinter stateChangeStringForThreadState:serialDispatchQueue:swiftTaskStates:thread:threadStateIndexes:taskState:task:iteratorIndex:missingStateIsInAnotherStack:numSamplesOmittedSincePreviousDisplayedSample:sampleTimestamp:previousSampleTimestamp:previousDisplayedTimestamp:previousTaskState:previousThread:previousThreadState:dispatchQueueChanges:swiftTaskChanges:priorityChanges:nameChanges:threadChanges:isTimeJump:ioEventsSincePreviousThreadState:]_block_invoke.2234
- __48-[SASamplePrinter copyDescriptionForTimeRanges:]_block_invoke.2421
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1908
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1914
- __49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.1917
- __50-[SASamplePrinter sortedLoadInfosForBinaryImages:]_block_invoke.1774
- __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke.1820
- __52-[SASamplePrinter printSystemStatsStyleBinaryImages]_block_invoke_2.1828
- __56-[SASamplePrinter stacksForThread:task:taskSampleCount:]_block_invoke.1927
- __56-[SASampleStore(SASampleStoreNSCoding) encodeWithCoder:]_block_invoke.1415
- __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke.2350
- __61-[SASamplePrinter stacksForSwiftAsyncInTask:taskSampleCount:]_block_invoke_2.2351
- __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1895
- __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke.1902
- __61-[SASampleStore(SASampleStoreNSCoding) initWithPAStyleCoder:]_block_invoke_2.1896
- __65-[SASamplePrinter displayStringForOnBehalfOfForTasks:includePid:]_block_invoke.2604
- __ReadAheadTaskLevelInfo_block_invoke.2022
- __ReadAheadTaskLevelInfo_block_invoke.2027
- __ReadAheadTaskLevelInfo_block_invoke.2030
- __SAKCDataReadAheadJetsamCoalitionInfo_block_invoke.2015
- __block_literal_global.1040
- __block_literal_global.1249
- __block_literal_global.1777
- __block_literal_global.1827
- __block_literal_global.1904
- __block_literal_global.2005
- __block_literal_global.2010
- __block_literal_global.2041
- __block_literal_global.2060
- __block_literal_global.2075
- __block_literal_global.2077
- __block_literal_global.2251
- __block_literal_global.2266
- __block_literal_global.2354
- __block_literal_global.2612
- __block_literal_global.2646
- __block_literal_global.2655
- __block_literal_global.629
- __block_literal_global.669
- __block_literal_global.681
CStrings:
+ "\x03\x1f\x01\x11\x81\"!1\xa2\x12\x1b5\x151\xc5\x12\x13V\x82B\x11"
+ "Memory size: "
+ "Non-string (%s) key %s"
+ "TQ,V_memSize"
+ "Unable to get hw.memsize: %d %s"
+ "[key isKindOfClass:NSString.class]"
+ "_memSize"
+ "hw.memsize"
+ "memSize"
+ "setMemSize:"
+ "v32@?0@\"NSString\"8@16^B24"
- "\x03\x1f\x01\x11\x81\"!1\xa2\x12\x1b%\x151\xc5\x12\x13V\x82B\x11"
- "\"%@\":"

```
