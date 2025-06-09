## libsystem_trace_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib`

```diff

-1643.120.5.0.0
-  __TEXT.__text: 0xa380
+1815.0.0.0.0
+  __TEXT.__text: 0xa3a4
   __TEXT.__auth_stubs: 0x220
   __TEXT.__const: 0x55
   __TEXT.__cstring: 0x3fd

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: AF2D182E-AAFF-3241-8C5F-00DA6DE828BF
+  UUID: 9141AA46-F5B0-3C1C-9C8B-642FE081A1C2
   Functions: 70
   Symbols:   119
   CStrings:  106
Symbols:
+ __os_trace_malloc_typed
+ __os_trace_realloc_typed
- __os_trace_malloc
- __os_trace_realloc
Functions:
~ _os_trace_blob_grow : 460 -> 476
~ _os_log_fmt_delimit : 1380 -> 1392
~ __os_trace_memdup : 60 -> 68

```
