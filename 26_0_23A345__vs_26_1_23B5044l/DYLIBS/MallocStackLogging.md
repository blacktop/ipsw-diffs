## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64572.137.1.0.0
-  __TEXT.__text: 0x9150
-  __TEXT.__auth_stubs: 0x6c0
+64572.146.1.0.0
+  __TEXT.__text: 0x92c0
+  __TEXT.__auth_stubs: 0x720
   __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x1fb6
-  __TEXT.__unwind_info: 0x288
-  __DATA_CONST.__got: 0x48
+  __TEXT.__cstring: 0x2091
+  __TEXT.__unwind_info: 0x290
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x98
-  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH.__data: 0x88
   __DATA.__data: 0x8
   __DATA.__bss: 0x3100

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  UUID: 3956A9DE-29A5-3E09-AA54-0A5CF13079F9
-  Functions: 228
-  Symbols:   582
-  CStrings:  208
+  UUID: F82255E0-16EF-3073-906F-0A19DE0D1958
+  Functions: 229
+  Symbols:   591
+  CStrings:  213
 
Symbols:
+ _SANDBOX_CHECK_NO_REPORT
+ _csops_audittoken
+ _is_debuggability_unrestrained
+ _os_variant_allows_internal_security_policies
+ _sandbox_check
+ _syscall
+ _task_info
+ _unsetenv
Functions:
+ _is_debuggability_unrestrained
~ _msl_cache_environment : 440 -> 492
~ _create_log_file : 1184 -> 1092
CStrings:
+ "AMFI"
+ "Unable to retrieve boot-args. Recommend checking sandbox violations\n"
+ "process is not in a debuggable environment; unsetting MallocStackLoggingDirectory environment variable\n"
+ "security.codesigning.config"
+ "syscall-unix"

```
