## MallocStackLogging

> `/System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging`

```diff

-64573.4.1.0.0
-  __TEXT.__text: 0x92a0
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__const: 0x138
-  __TEXT.__cstring: 0x2091
-  __TEXT.__unwind_info: 0x288
+64575.66.1.0.0
+  __TEXT.__text: 0x9248
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x2107
+  __TEXT.__unwind_info: 0x278
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x98
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH.__data: 0x88
   __DATA.__data: 0x8
-  __DATA.__bss: 0x3100
-  __DATA.__common: 0x48
+  __DATA.__bss: 0x30e0
+  __DATA.__common: 0x40
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_blocks.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
-  UUID: FC5838D5-A5AB-3E2B-B0DB-116586E8C5B8
-  Functions: 229
-  Symbols:   591
+  UUID: 7CE93BA7-A255-3414-8D2F-28D192FF6A41
+  Functions: 234
+  Symbols:   602
   CStrings:  213
 
Symbols:
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _my_mkstemps
+ _radix_tree_insert_recursive.cold.5
+ _strlen
CStrings:
+ "previous_refcount >= refs && \"Detected possible double free or buffer overrun of heap allocation. Consider reproducing with ASan enabled.\""
+ "process is not in a debuggable environment; MallocStackLoggingDirectory will be determined by the framework\n"
- "previous_refcount >= refs"
- "process is not in a debuggable environment; unsetting MallocStackLoggingDirectory environment variable\n"

```
