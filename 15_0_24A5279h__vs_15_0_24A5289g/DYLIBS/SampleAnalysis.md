## SampleAnalysis

> `/System/Library/PrivateFrameworks/SampleAnalysis.framework/Versions/A/SampleAnalysis`

```diff

-377.0.0.0.0
-  __TEXT.__text: 0xfb9a8
+378.0.0.0.0
+  __TEXT.__text: 0xfb808
   __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0x5620
+  __TEXT.__objc_methlist: 0x5618
   __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x16e61
-  __TEXT.__oslogstring: 0xbc20
-  __TEXT.__gcc_except_tab: 0xa294
+  __TEXT.__cstring: 0x16ecd
+  __TEXT.__oslogstring: 0xbc15
+  __TEXT.__gcc_except_tab: 0xa2c0
   __TEXT.__dlopen_cstrs: 0x16a
-  __TEXT.__unwind_info: 0x2138
-  __TEXT.__objc_classname: 0xa8b
-  __TEXT.__objc_methname: 0xccde
-  __TEXT.__objc_methtype: 0x17bd
+  __TEXT.__unwind_info: 0x2130
+  __TEXT.__objc_classname: 0xa8e
+  __TEXT.__objc_methname: 0xccd3
+  __TEXT.__objc_methtype: 0x17bb
   __TEXT.__objc_stubs: 0x7b40
   __DATA_CONST.__got: 0x430
   __DATA_CONST.__const: 0xd20

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x3c10
   __AUTH_CONST.__cfstring: 0xb2e0
-  __AUTH_CONST.__objc_const: 0xf690
+  __AUTH_CONST.__objc_const: 0xf670
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x1b0
   __AUTH.__objc_data: 0x26c0
   __AUTH.__thread_vars: 0x60
   __AUTH.__thread_bss: 0x19
-  __DATA.__objc_ivar: 0xc5c
+  __DATA.__objc_ivar: 0xc58
   __DATA.__data: 0x5c4
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4f8
+  __DATA.__bss: 0x4f0
   __DATA.__common: 0x498
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/libdscsym.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2847
-  Symbols:   6733
-  CStrings:  2850
+  Functions: 2844
+  Symbols:   6728
+  CStrings:  2849
 
Symbols:
+ -[SAKPerfState nextSampleForThread:isOnCore:]
+ GCC_except_table111
+ GCC_except_table29
+ GCC_except_table46
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table80
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table99
+ OBJC_IVAR_$_SAKPerfState._onCoreThreads
+ __53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.362
+ __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.80
+ __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.85
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.213
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.216
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.221
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.229
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.257
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.270
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.278
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.291
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.308
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.316
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.325
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.328
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.295
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.309
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.319
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.310
+ __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.322
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.139
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.142
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.153
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.156
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.159
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.162
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.168
+ __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.177
+ __block_literal_global.199
+ __block_literal_global.318
+ __block_literal_global.334
- -[SAKPerfState _checkCpuArraySize:]
- -[SAKPerfState dealloc]
- -[SAKPerfState nextSampleForCpu:isOnCore:]
- GCC_except_table108
- GCC_except_table117
- GCC_except_table12
- GCC_except_table22
- GCC_except_table23
- GCC_except_table38
- GCC_except_table39
- GCC_except_table44
- GCC_except_table52
- GCC_except_table57
- GCC_except_table62
- GCC_except_table64
- GCC_except_table78
- GCC_except_table8
- GCC_except_table88
- OBJC_IVAR_$_SAKPerfState._numCores
- OBJC_IVAR_$_SAKPerfState._onCoreBitArray
- __53-[SASampleStore(KPerf) forwardFillFromLastStackshot:]_block_invoke.366
- __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.86
- __55-[SASampleStore(KPerf) backfillExclaveFromKPerf:state:]_block_invoke.91
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.217
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.220
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.225
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.233
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.261
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.274
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.282
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.295
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.312
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.320
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.329
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke.336
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.299
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.313
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_2.323
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.314
- __77-[SASampleStore(KPerf) _parseKTraceFile:stackshotsOnly:warningsOut:errorOut:]_block_invoke_3.326
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.144
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.152
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.158
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.161
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.164
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.167
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.178
- __84-[SASampleStore(KPerf) _addKPerfDataFromKTraceSession:beforeMachAbsTime:petTimerID:]_block_invoke.182
- __ZZ35-[SAKPerfState _checkCpuArraySize:]E9onceToken
- ___35-[SAKPerfState _checkCpuArraySize:]_block_invoke
- __block_literal_global.203
- __block_literal_global.322
- __block_literal_global.325
- __block_literal_global.338
CStrings:
+ "%!'(MISSING)llu Created %!s(MISSING)-core threadState (index %!l(MISSING)u) for thread 0x%!l(MISSING)lx (sample index %!l(MISSING)d-%!l(MISSING)d, machabs %!l(MISSING)lu-%!l(MISSING)lu) with kernel leaf frame 0x%!l(MISSING)lx) exclaves:%!d(MISSING)\n"
+ "%!'(MISSING)llu Not creating threadState for thread 0x%!l(MISSING)lx at machabs %!l(MISSING)lu due to already having a thread state for sample index %!l(MISSING)u (kernel leaf frame 0x%!l(MISSING)lx, user leaf frame 0x%!l(MISSING)lx)\n"
+ "%!'(MISSING)llu Not creating threadState for thread 0x%!l(MISSING)lx at machabs %!l(MISSING)lu due to the thread being created after sample index %!l(MISSING)u at machabs %!l(MISSING)lu (kernel leaf frame 0x%!l(MISSING)lx, user leaf frame 0x%!l(MISSING)lx)\n"
+ "%!'(MISSING)llu PERF_TMR_Handler on thread 0x%!l(MISSING)lx core %!d(MISSING)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx core %!d(MISSING) event 0x%!x(MISSING) skipping kperf content 0x%!l(MISSING)lx: %!s(MISSING)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx core %!d(MISSING) parsing %!s(MISSING)-core kperf with content 0x%!l(MISSING)lx: %!s(MISSING)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx dispatch queue %!l(MISSING)ld backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx dispatch queue %!l(MISSING)ld backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx exclave info (%!l(MISSING)u exclaves, leaf frame 0x%!l(MISSING)lx) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx exclave info (%!l(MISSING)u exclaves, leaf frame 0x%!l(MISSING)lx) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx ran into non-kperf state at index %!l(MISSING)u, stopping\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx sched info (cpu time %!l(MISSING)ld (%!l(MISSING)ld + %!l(MISSING)ld), state 0x%!x(MISSING), priority %!d(MISSING) (%!d(MISSING)), qos %!d(MISSING), rqos %!d(MISSING), qoso %!d(MISSING), qosp %!d(MISSING)) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx sched info (cpu time %!l(MISSING)ld (%!l(MISSING)ld + %!l(MISSING)ld), state 0x%!x(MISSING), priority %!d(MISSING) (%!d(MISSING)), qos %!d(MISSING), rqos %!d(MISSING), qoso %!d(MISSING), qosp %!d(MISSING)) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx snapshot info (io tier %!d(MISSING), passive %!d(MISSING), suspended %!d(MISSING), darwinbg %!d(MISSING), idlewq %!d(MISSING), gfi %!d(MISSING), runnable %!s(MISSING)) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx snapshot info (io tier %!d(MISSING), passive %!d(MISSING), suspended %!d(MISSING), darwinbg %!d(MISSING), idlewq %!d(MISSING), gfi %!d(MISSING), runnable %!s(MISSING)) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx swift task %!l(MISSING)ld backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx swift task %!l(MISSING)ld backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx thread instructions (%!l(MISSING)lu) cycles (%!l(MISSING)lu) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx thread instructions (%!l(MISSING)lu) cycles (%!l(MISSING)lu) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx thread name %!s(MISSING) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx thread name %!s(MISSING) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx user stack (leaf frame 0x%!l(MISSING)lx, swift async leaf 0x%!l(MISSING)lx) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu Thread 0x%!l(MISSING)lx user stack (leaf frame 0x%!l(MISSING)lx, swift async leaf 0x%!l(MISSING)lx) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
+ "%!'(MISSING)llu WARNING: Thread 0x%!l(MISSING)lx core %!d(MISSING) ignoring record without a stack\n"
+ "%!'(MISSING)llu WARNING: Thread 0x%!l(MISSING)lx core %!d(MISSING) ignoring record without thread info\n"
+ "%!'(MISSING)llu WARNING: Thread 0x%!l(MISSING)lx core %!d(MISSING) unable to determine pid for thread: %!d(MISSING)\n"
+ "Logging kperf parsing to %!s(MISSING)\n"
- "%!'(MISSING)llu 0x%!l(MISSING)lx Skipping kperf content: %!s(MISSING)\n"
- "%!'(MISSING)llu Created %!s(MISSING)-core threadState (index %!l(MISSING)u) for thread 0x%!l(MISSING)lx (sample index %!l(MISSING)d-%!l(MISSING)d, machabs %!l(MISSING)lu-%!l(MISSING)lu) with kernel stack (leaf frame 0x%!l(MISSING)lx) exclaves:%!d(MISSING)\n"
- "%!'(MISSING)llu Not creating threadState for thread 0x%!l(MISSING)lx at machabs %!l(MISSING)lu due to already having a thread state for sample index %!l(MISSING)u\n"
- "%!'(MISSING)llu Not creating threadState for thread 0x%!l(MISSING)lx at machabs %!l(MISSING)lu due to the thread being created after sample index %!l(MISSING)u at machabs %!l(MISSING)lu\n"
- "%!'(MISSING)llu PERF_TMR_Handler on core %!d(MISSING)\n"
- "%!'(MISSING)llu Parsing kperf for tid 0x%!l(MISSING)lx with content 0x%!l(MISSING)lx: %!s(MISSING)\n"
- "%!'(MISSING)llu Parsing on-core %!d(MISSING) kperf for tid 0x%!l(MISSING)lx with content 0x%!l(MISSING)lx: %!s(MISSING)\n"
- "%!'(MISSING)llu WARNING: Ignoring record without a stack for thread 0x%!l(MISSING)lx\n"
- "%!'(MISSING)llu WARNING: Ignoring record without thread info for thread 0x%!l(MISSING)lx\n"
- "%!'(MISSING)llu WARNING: Unable to determine pid for thread 0x%!l(MISSING)lx: %!d(MISSING)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx dispatch queue %!l(MISSING)ld backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx dispatch queue %!l(MISSING)ld backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx exclave info (%!l(MISSING)u exclaves, leaf frame 0x%!l(MISSING)lx) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx exclave info (%!l(MISSING)u exclaves, leaf frame 0x%!l(MISSING)lx) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx ran into non-kperf state at index %!l(MISSING)u, stopping\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx sched info (cpu time %!l(MISSING)ld (%!l(MISSING)ld + %!l(MISSING)ld), state 0x%!x(MISSING), priority %!d(MISSING) (%!d(MISSING)), qos %!d(MISSING), rqos %!d(MISSING), qqoso %!d(MISSING), qosp %!d(MISSING)) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx sched info (cpu time %!l(MISSING)ld (%!l(MISSING)ld + %!l(MISSING)ld), state 0x%!x(MISSING), priority %!d(MISSING) (%!d(MISSING)), qos %!d(MISSING), rqos %!d(MISSING), qqoso %!d(MISSING), qosp %!d(MISSING)) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx snapshot info (io tier %!d(MISSING), passive %!d(MISSING), suspended %!d(MISSING), darwinbg %!d(MISSING), idlewq %!d(MISSING), gfi %!d(MISSING), runnable %!s(MISSING)) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx snapshot info (io tier %!d(MISSING), passive %!d(MISSING), suspended %!d(MISSING), darwinbg %!d(MISSING), idlewq %!d(MISSING), gfi %!d(MISSING), runnable %!s(MISSING)) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx swift task %!l(MISSING)ld backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx swift task %!l(MISSING)ld backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx thread instructions (%!l(MISSING)lu) cycles (%!l(MISSING)lu) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx thread instructions (%!l(MISSING)lu) cycles (%!l(MISSING)lu) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx thread name %!s(MISSING) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx thread name %!s(MISSING) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx user stack (leaf frame 0x%!l(MISSING)lx, swift async leaf 0x%!l(MISSING)lx) backfilled to %!d(MISSING) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "%!'(MISSING)llu thread 0x%!l(MISSING)lx user stack (leaf frame 0x%!l(MISSING)lx, swift async leaf 0x%!l(MISSING)lx) backfilled to all (%!d(MISSING)) thread states (indexes %!l(MISSING)u-%!l(MISSING)u)\n"
- "Logging kperf parsing to %!s(MISSING)"

```
