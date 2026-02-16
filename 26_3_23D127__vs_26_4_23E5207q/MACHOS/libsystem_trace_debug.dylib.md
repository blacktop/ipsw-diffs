## libsystem_trace_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_trace_debug.dylib`

```diff

-1815.80.2.0.0
-  __TEXT.__text: 0xa3a4
+1861.100.16.0.0
+  __TEXT.__text: 0xa3f4
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x55
+  __TEXT.__const: 0x5d
   __TEXT.__cstring: 0x3fd
   __TEXT.__unwind_info: 0x138
   __DATA_CONST.__got: 0x20

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  UUID: E10C1554-2A0A-39F5-92CE-AC9E86A9275A
-  Functions: 70
+  UUID: 0F694DBE-CE66-305C-B421-8F23AA002B67
+  Functions: 71
   Symbols:   119
   CStrings:  106
 
Functions:
~ __os_log_fmt_flatten_to_blob : 644 -> 664
~ _os_log_fmt_flatten : 3912 -> 3908
~ __os_log_fmt_flatten_data : 460 -> 452
~ _os_log_fmt_convert_trace : 384 -> 388
~ __os_log_fmt_compose_scalar : 1984 -> 1892
+ sub_8508
~ __os_log_to_kernel : 576 -> 656

```
