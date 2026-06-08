## libsystem_darwin.dylib

> `/usr/lib/system/libsystem_darwin.dylib`

```diff

-1752.120.2.0.0
-  __TEXT.__text: 0x64c8
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1e58
+1782.0.0.0.0
+  __TEXT.__text: 0x65ac
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0x1ebc
   __TEXT.__oslogstring: 0x8d4
-  __TEXT.__unwind_info: 0x1d0
-  __DATA_CONST.__got: 0x38
-  __DATA_CONST.__const: 0x2930
-  __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0x180
+  __TEXT.__unwind_info: 0x1d8
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x2950
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1a0
+  __AUTH_CONST.__auth_got: 0x2b0
   __DATA.__data: 0x10
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x48
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: AF4F1CB1-72DD-32B7-8A3F-32369CD3DE39
-  Functions: 171
-  Symbols:   452
-  CStrings:  483
+  UUID: 164C9B77-94A4-378C-A122-26290CA39E73
+  Functions: 174
+  Symbols:   462
+  CStrings:  487
 
Symbols:
+ ___os_lockdown_mode_enabled_block_invoke
+ ___os_lockdown_mode_enabled_block_invoke.cold.1
+ _abort_report_np
+ _os_lockdown_mode_enabled
+ _os_lockdown_mode_enabled.cold.1
+ _os_lockdown_mode_enabled.lockdown_mode_enabled
+ _os_lockdown_mode_enabled.once
- _OUTLINED_FUNCTION_24
CStrings:
+ "%s:%s:%u: %s"
+ "lockdown_mode.c"
+ "os_lockdown_mode_enabled_block_invoke"
+ "security.mac.lockdown_mode_state"

```
