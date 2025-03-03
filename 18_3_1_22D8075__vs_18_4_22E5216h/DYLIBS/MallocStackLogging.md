## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64567.3.3.0.0
-  __TEXT.__text: 0x8ea4
-  __TEXT.__auth_stubs: 0x6b0
-  __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x1dd8
-  __TEXT.__unwind_info: 0x258
+64570.56.1.0.0
+  __TEXT.__text: 0x912c
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__const: 0x118
+  __TEXT.__cstring: 0x1f69
+  __TEXT.__unwind_info: 0x270
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x98
-  __AUTH_CONST.__auth_got: 0x358
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH.__data: 0x88
   __DATA.__data: 0x8
-  __DATA.__bss: 0x30e8
-  __DATA.__common: 0x40
+  __DATA.__bss: 0x3100
+  __DATA.__common: 0x48
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib
+  - /usr/lib/system/libsystem_darwin.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  Functions: 224
-  Symbols:   343
-  CStrings:  199
+  Functions: 229
+  Symbols:   352
+  CStrings:  206
 
Symbols:
+ _os_variant_has_internal_diagnostics
+ _proc_pidinfo
CStrings:
+ "/var/db/disableLiteModeMemoryResourceExceptionHandling"
+ "/var/db/enableLiteModeMemoryResourceExceptionHandling"
+ "PROC_LIMIT_WARN mode: Too many allocations have been tracked by lite stack logging. Disabling stack logging.\n"
+ "collisions < 0"
+ "com.apple.Symbolication"
+ "msl_handle_memory_pressure_event: approaching memory limit. Starting stack-logging.\n"
+ "msl_handle_memory_pressure_event: stopping stack-logging\n"

```
