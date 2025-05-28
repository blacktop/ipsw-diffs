## libsystem_sandbox.dylib

> `/usr/lib/system/libsystem_sandbox.dylib`

```diff

-2169.0.12.0.0
-  __TEXT.__text: 0x3048
+2169.40.22.0.1
+  __TEXT.__text: 0x3190
   __TEXT.__auth_stubs: 0x2f0
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x627
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__cstring: 0x62e
+  __TEXT.__unwind_info: 0x1a4
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x40
   __AUTH_CONST.__auth_got: 0x178

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  Functions: 126
-  Symbols:   219
-  CStrings:  56
+  Functions: 129
+  Symbols:   223
+  CStrings:  57
 
Symbols:
+ _sandbox_check_process_signal_target
+ _sandbox_check_self_signal_target
+ _sandbox_check_signal_target_internal
CStrings:
+ "signal"

```
