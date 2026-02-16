## libsystem_sanitizers.dylib

> `/usr/lib/system/libsystem_sanitizers.dylib`

```diff

-25.0.0.0.0
-  __TEXT.__text: 0x63ec
-  __TEXT.__auth_stubs: 0x190
+26.0.0.0.0
+  __TEXT.__text: 0x6340
+  __TEXT.__auth_stubs: 0x1c0
   __TEXT.__const: 0x160
-  __TEXT.__cstring: 0xa74
+  __TEXT.__cstring: 0xacc
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x90
-  __AUTH_CONST.__auth_got: 0xc8
+  __DATA_CONST.__const: 0xb0
+  __AUTH_CONST.__auth_got: 0xe0
   __AUTH_CONST.__const: 0xd0
   __AUTH.__data: 0x30
   __DATA.__common: 0x18
-  __DATA.__bss: 0x548
+  __DATA.__bss: 0x550
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_c.dylib

   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  UUID: 223A31A1-41C7-3DC1-ABAC-3B5B471D6FA5
-  Functions: 204
-  Symbols:   451
-  CStrings:  129
+  UUID: 5160857B-6E84-3811-804C-12A5BA6D5766
+  Functions: 207
+  Symbols:   455
+  CStrings:  133
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __ZN6config3env6Parser11getTrialValILm44EEEPKcS4_RAT__S3_RA128_c
+ __ZN6config3env6Parser8unsetEnvILm44EEEvPPKcRAT__S3_
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.1
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.10
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.2
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.3
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.4
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.5
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.6
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.7
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.8
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE10loggerFuncEjmmmmj.cold.9
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE14previousLoggerE
+ __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEXadL_ZN9mach_timeL9hasPassedEyEEE8stopTimeE
+ __ZNK6config3env6Parser6getValILm44EEEPKcRAT__S3_
+ __ZNK6config3env6Parser9getNumberILm44EmXadL_Z7strtoulEEEET0_RAT__KcS3_
+ __sanitizers_init.cold.1
+ _mach_approximate_time
+ _mach_timebase_info
+ _strlen
- __ZN10ASanShadow11bzeroShadowEPKvm
- __ZN10ASanShadow12memsetShadowEPvim
- __ZN4asan15ReportGenerator25addStackUseAfterScopeInfoERNS_6ReportE
- __ZN4asan15ReportGenerator26addStackBufferOverflowInfoERNS_6ReportE
- __ZN4asan15ReportGenerator27addStackBufferUnderflowInfoERNS_6ReportE
- __ZN4asan18initLibmallocHooksEP6Shadow
- __ZN4asan20initReportGenerationEPK6ShadowPKNS_15GlobalsRegistryE
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.1
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.10
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.11
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.12
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.2
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.3
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.4
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.5
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.6
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.7
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.8
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE10loggerFuncEjmmmmj.cold.9
- __ZN9libmalloc12MallocLoggerIXadL_ZL7onAllocmmjEEXadL_ZL9onDeallocmjEEE14previousLoggerE
- __ZNK10ASanShadow14addressIsInMemEm
- __ZNK10ASanShadow16shadowForAddressEm
- __ZNK10ASanShadow17addressIsInShadowEm
- ___cxa_pure_virtual
CStrings:
+ "SanitizersAllocationTracesDurationInSeconds"
+ "kr == 0"
+ "mach_time.h"
+ "millisecondsToMachTicks"
+ "trace_extractor.h"
- "trace_collector.h"

```
