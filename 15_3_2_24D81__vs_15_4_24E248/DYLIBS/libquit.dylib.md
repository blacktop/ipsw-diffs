## libquit.dylib

> `/usr/lib/libquit.dylib`

```diff

-383.2.0.0.0
-  __TEXT.__text: 0x17a0
+383.5.0.0.0
+  __TEXT.__text: 0x16d4
   __TEXT.__auth_stubs: 0x280
   __TEXT.__const: 0x68
   __TEXT.__oslogstring: 0x20a
   __TEXT.__cstring: 0x33
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__got: 0x40
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x160
   __AUTH_CONST.__auth_got: 0x140
   __AUTH_CONST.__const: 0x80

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libspindump.dylib
-  UUID: E5F3E2E1-1ABB-334D-9A36-4E6B3E862BC4
-  Functions: 37
-  Symbols:   114
+  UUID: 940658A8-6A8A-39DF-81F4-5C5BF9D5C7BA
+  Functions: 43
+  Symbols:   138
   CStrings:  16
 
Symbols:
+ LQCachePort.cold.1
+ LQForceQuit.cold.1
+ LQForceQuit.cold.2
+ LQReportCpuResource.cold.1
+ LQReportCpuResource.cold.2
+ LQReportPotentialHang.cold.1
+ LQReportPotentialHang.cold.2
+ LQReportPotentialSpin.cold.2
+ LQReportPotentialSpin.cold.3
+ _LQKill.cold.1
+ _LQKill.cold.2
+ _LQKill.cold.3
+ _LQKill.cold.4
+ _LQPidIsUnresponsive.cold.3
+ _LQPidIsUnresponsive.cold.4
+ ___LQForceQuitLikely_block_invoke.cold.1
+ ___LQForceQuit_block_invoke.cold.1
+ ___LQForceQuit_block_invoke.cold.2
+ ___LQForceQuit_block_invoke.cold.3
+ ___LQForceQuit_block_invoke.cold.4
+ ___LQForceQuit_block_invoke.cold.5
+ ___LQKill_block_invoke.cold.1
+ ___LQKill_block_invoke_2.cold.1
+ __spindump_mach_port_block_invoke.cold.2

```
