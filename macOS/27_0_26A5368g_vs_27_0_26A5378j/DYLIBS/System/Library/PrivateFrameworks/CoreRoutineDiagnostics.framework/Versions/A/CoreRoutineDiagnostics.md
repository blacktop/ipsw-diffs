## CoreRoutineDiagnostics

> `/System/Library/PrivateFrameworks/CoreRoutineDiagnostics.framework/Versions/A/CoreRoutineDiagnostics`

```diff

-  __TEXT.__text: 0xff1c
-  __TEXT.__objc_methlist: 0xb14
+  __TEXT.__text: 0xf900
+  __TEXT.__objc_methlist: 0xabc
   __TEXT.__dlopen_cstrs: 0x6d
-  __TEXT.__const: 0x178
-  __TEXT.__oslogstring: 0x1c9a
-  __TEXT.__cstring: 0x1835
-  __TEXT.__gcc_except_tab: 0x3cc
+  __TEXT.__const: 0x170
+  __TEXT.__gcc_except_tab: 0x3b4
+  __TEXT.__oslogstring: 0x1b2c
+  __TEXT.__cstring: 0x17d6
   __TEXT.__ustring: 0x7c
-  __TEXT.__unwind_info: 0x3b8
+  __TEXT.__unwind_info: 0x3d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e8
+  __DATA_CONST.__objc_selrefs: 0x8c0
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__got: 0x178
-  __AUTH_CONST.__const: 0x360
-  __AUTH_CONST.__cfstring: 0x1960
-  __AUTH_CONST.__objc_const: 0xfc8
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x18e0
+  __AUTH_CONST.__objc_const: 0xed8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xac
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x98
   __DATA.__data: 0x158
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 288
-  Symbols:   897
-  CStrings:  573
+  Functions: 285
+  Symbols:   878
+  CStrings:  558
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[RTRadarUtilities truncateRadarTitle:]
+ -[RTBugCaptureManager isRbcAllowed]
+ -[RTTransactionManager isRTTransactionDiagnosticMode]
+ -[RTTransactionManager isTransactionDiagnosticsSampled]
+ -[RTTransactionManager setTransactionDiagnosticsSampled:]
+ -[RTTransactionManager transactionDiagnosticsSampled]
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table7
+ OBJC_IVAR_$_RTTransactionManager._transactionDiagnosticsSampled
+ ___53-[RTTransactionManager isRTTransactionDiagnosticMode]_block_invoke
+ ___55-[RTTransactionManager isTransactionDiagnosticsSampled]_block_invoke
+ ___57-[RTTransactionManager setTransactionDiagnosticsSampled:]_block_invoke
+ ___block_descriptor_41_e8_32s_e5_v8?0l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0l
+ ___copy_helper_block_e8_32s40r
+ ___destroy_helper_block_e8_32s40r
+ _dispatch_sync
+ _objc_msgSend$isRTTransactionDiagnosticMode
+ _objc_msgSend$isRbcAllowed
+ _objc_msgSend$rangeOfComposedCharacterSequencesForRange:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$truncateRadarTitle:
- +[RTTransaction stringFromCpuMeasurementMode:]
- -[RTTransaction computeCpuPercentage]
- -[RTTransactionProfileData cpuMeasurementMode]
- -[RTTransactionProfileData endCpuSystemTime]
- -[RTTransactionProfileData endCpuUserTime]
- -[RTTransactionProfileData setCpuMeasurementMode:]
- -[RTTransactionProfileData setEndCpuSystemTime:]
- -[RTTransactionProfileData setEndCpuUserTime:]
- -[RTTransactionProfileData setStartCpuSystemTime:]
- -[RTTransactionProfileData setStartCpuUserTime:]
- -[RTTransactionProfileData setTransactionThread:]
- -[RTTransactionProfileData startCpuSystemTime]
- -[RTTransactionProfileData startCpuUserTime]
- -[RTTransactionProfileData transactionThread]
- GCC_except_table27
- GCC_except_table3
- GCC_except_table31
- GCC_except_table46
- GCC_except_table50
- GCC_except_table8
- OBJC_IVAR_$_RTTransactionProfileData._cpuMeasurementMode
- OBJC_IVAR_$_RTTransactionProfileData._endCpuSystemTime
- OBJC_IVAR_$_RTTransactionProfileData._endCpuUserTime
- OBJC_IVAR_$_RTTransactionProfileData._startCpuSystemTime
- OBJC_IVAR_$_RTTransactionProfileData._startCpuUserTime
- OBJC_IVAR_$_RTTransactionProfileData._transactionThread
- ___error
- _getrusage
- _kRTTransactionMetricsKeyCpuMeasurementMode
- _kRTTransactionMetricsKeyCpuPercentage
- _mach_error_string
- _mach_thread_self
- _objc_msgSend$computeCpuPercentage
- _objc_msgSend$cpuMeasurementMode
- _objc_msgSend$endCpuSystemTime
- _objc_msgSend$endCpuUserTime
- _objc_msgSend$setCpuMeasurementMode:
- _objc_msgSend$setEndCpuSystemTime:
- _objc_msgSend$setEndCpuUserTime:
- _objc_msgSend$setStartCpuSystemTime:
- _objc_msgSend$setStartCpuUserTime:
- _objc_msgSend$setTransactionThread:
- _objc_msgSend$startCpuSystemTime
- _objc_msgSend$startCpuUserTime
- _objc_msgSend$stringFromCpuMeasurementMode:
- _objc_msgSend$transactionThread
- _strerror
- _thread_info
CStrings:
+ "%@, %@, truncating radar title to %lu characters (originally %lu characters)"
+ "..."
+ "RTTransactionProfileData: startDate, %@, endDate, %@, startMemory, %.2fMB, endMemory, %.2fMB, peakMemory, %.2fMB, signpostId, %llu, bugCaptureTriggered, %@"
- "All CPU measurements failed for %@"
- "Failed to get resource usage for %@, %s"
- "Invalid CPU measurement for %@: cpuTime, %.6fs (start=%.6fs, end=%.6fs), measurementMode, %@"
- "Process-wide end measurement failed for %@: %s"
- "ProcessWide"
- "Profiling completed for %@, mode, %@"
- "Profiling started for %@, mode, %@"
- "RTTransactionProfileData: startDate, %@, endDate, %@, startMemory, %.2fMB, endMemory, %.2fMB, peakMemory, %.2fMB, cpuMeasurementMode, %@, signpostId, %llu, bugCaptureTriggered, %@"
- "Thread-specific end measurement failed for %@: %s, falling back to process-wide"
- "Thread-specific measurement failed for %@, falling back to process-wide, %s"
- "ThreadSpecific"
- "Unknown(0x%lx)"
- "cpuMeasurementMode"
- "cpuPercentage"

```
