## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/SampleAnalysis`

```diff

-411.0.0.0.0
-  __TEXT.__text: 0xedf5c
+412.0.0.0.0
+  __TEXT.__text: 0xee188
   __TEXT.__auth_stubs: 0x1760
   __TEXT.__objc_methlist: 0x5d64
   __TEXT.__const: 0x348
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__cstring: 0x17e6a
+  __TEXT.__cstring: 0x17f1c
   __TEXT.__oslogstring: 0xc632
-  __TEXT.__gcc_except_tab: 0x9aec
-  __TEXT.__unwind_info: 0x20c0
+  __TEXT.__gcc_except_tab: 0x9b58
+  __TEXT.__unwind_info: 0x20c8
   __TEXT.__objc_classname: 0xb12
-  __TEXT.__objc_methname: 0xd81f
+  __TEXT.__objc_methname: 0xd846
   __TEXT.__objc_methtype: 0x1a1c
   __TEXT.__objc_stubs: 0x7d20
   __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x3700
+  __DATA_CONST.__const: 0x3710
   __DATA_CONST.__objc_classlist: 0x408
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x1d0
   __AUTH_CONST.__auth_got: 0xbc8
   __AUTH_CONST.__const: 0xb00
-  __AUTH_CONST.__cfstring: 0xc7e0
-  __AUTH_CONST.__objc_const: 0x101c8
+  __AUTH_CONST.__cfstring: 0xc8c0
+  __AUTH_CONST.__objc_const: 0x101e8
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH.__objc_data: 0x50
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0xd10
+  __DATA.__objc_ivar: 0xd14
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x30
   __DATA.__common: 0x498
   __DATA_DIRTY.__objc_ivar: 0x48
-  __DATA_DIRTY.__objc_data: 0x2800
+  __DATA_DIRTY.__objc_data: 0x2850
   __DATA_DIRTY.__bss: 0x470
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: CBF77254-C360-346F-A987-908846FA3673
-  Functions: 2798
-  Symbols:   9595
-  CStrings:  8396
+  UUID: 72821A1F-45A2-34B1-8284-548E9514FCAC
+  Functions: 2799
+  Symbols:   9600
+  CStrings:  8412
 
Symbols:
+ -[SASampleStore isAnyPowerMitigationEnabledAtTailspinCapture]
+ GCC_except_table542
+ GCC_except_table547
+ _OBJC_IVAR_$_SASampleStore._powerMitigationLevelAtTailspinCapture
+ _SA_TSPMetadata_PowerManagementMitigationKey
+ _SA_TSPMetadata_PowerManagementMitigationLevelKey
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1528
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1531
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1525
+ ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1532
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1960
+ ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1962
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2433
+ ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2449
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2395
+ ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2404
+ ___30-[SASamplePrinter printHeader]_block_invoke.1339
+ ___30-[SASamplePrinter printHeader]_block_invoke.1366
+ ___30-[SASamplePrinter printHeader]_block_invoke.1373
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1340
+ ___30-[SASamplePrinter printHeader]_block_invoke_2.1386
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2753
+ ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2758
+ ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1467
+ ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1477
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2010
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2011
+ ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2012
+ ___ReadAheadTaskLevelInfo_block_invoke.2055
+ ___ReadAheadTaskLevelInfo_block_invoke.2060
+ ___ReadAheadTaskLevelInfo_block_invoke.2063
+ ___block_literal_global.1342
+ ___block_literal_global.1479
+ ___block_literal_global.1888
+ ___block_literal_global.1933
+ ___block_literal_global.1936
+ ___block_literal_global.1943
+ ___block_literal_global.2043
+ ___block_literal_global.2048
+ ___block_literal_global.2074
+ ___block_literal_global.2087
+ ___block_literal_global.2089
+ ___block_literal_global.2392
+ ___block_literal_global.2407
+ ___block_literal_global.2486
+ ___block_literal_global.2724
+ ___block_literal_global.2746
+ ___block_literal_global.2755
- GCC_except_table536
- GCC_except_table544
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1520
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke.1527
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1521
- ___103-[SASamplePrinter printTaskHeaderForTask:specialDispatchQueueId:specialThreadId:omitSpecial:omitOther:]_block_invoke_2.1528
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke.1956
- ___110-[SASamplePrinter printSingleStackForTasks:limitToDispatchQueueIds:limitToThreadIds:intersection:sampleCount:]_block_invoke_2.1958
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2429
- ___134-[SASamplePrinter addStack:toStream:sampleCount:binariesToDisplay:primaryState:primaryMicrostackshotState:onlyHeaviestStack:isKernel:]_block_invoke.2445
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2391
- ___245-[SASamplePrinter addStackForDispatchQueue:orSwiftTaskStates:orThread:andThreadStateIndexes:task:toRootObjects:nameChanges:dispatchQueueChanges:swiftTaskChanges:threadChanges:priorityChanges:microstackshotSummary:onlyHeaviestStack:includeState:]_block_invoke.2400
- ___30-[SASamplePrinter printHeader]_block_invoke.1335
- ___30-[SASamplePrinter printHeader]_block_invoke.1362
- ___30-[SASamplePrinter printHeader]_block_invoke.1369
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1336
- ___30-[SASamplePrinter printHeader]_block_invoke_2.1382
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2749
- ___37-[SASamplePrinter sortHeavyCallTree:]_block_invoke.2754
- ___41-[SASamplePrinter printTasksIndividually]_block_invoke.1463
- ___44-[SASamplePrinter printTasksWithAggregation]_block_invoke.1469
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke.2006
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_2.2007
- ___49-[SASamplePrinter stacksForTask:taskSampleCount:]_block_invoke_3.2008
- ___ReadAheadTaskLevelInfo_block_invoke.2039
- ___ReadAheadTaskLevelInfo_block_invoke.2044
- ___ReadAheadTaskLevelInfo_block_invoke.2047
- ___block_literal_global.1338
- ___block_literal_global.1475
- ___block_literal_global.1884
- ___block_literal_global.1927
- ___block_literal_global.1929
- ___block_literal_global.1932
- ___block_literal_global.2027
- ___block_literal_global.2032
- ___block_literal_global.2058
- ___block_literal_global.2071
- ___block_literal_global.2073
- ___block_literal_global.2388
- ___block_literal_global.2403
- ___block_literal_global.2482
- ___block_literal_global.2720
- ___block_literal_global.2742
- ___block_literal_global.2751
Functions:
~ -[SASamplePrinter printHeader] : 49004 -> 49232
~ -[SASampleStore .cxx_destruct] : 968 -> 980
+ -[SASampleStore isAnyPowerMitigationEnabledAtTailspinCapture]
~ -[SASampleStore(SASampleStoreNSCoding) encodeWithCoder:] : 7872 -> 7892
~ -[SASampleStore(SASampleStoreNSCoding) initWithCoder:] : 16992 -> 17044
~ ___94-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:afterMachAbsTime:warningsOut:errorOut:]_block_invoke_3 : 2560 -> 2664
CStrings:
+ "Extreme"
+ "High"
+ "Low"
+ "Medium"
+ "Power Management Mitigation Level (at tailspin capture): "
+ "PowerManagementMitigation"
+ "PowerManagementMitigationLevel"
+ "_powerMitigationLevelAtTailspinCapture"

```
