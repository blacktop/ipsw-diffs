## libpmsample.dylib

> `/usr/lib/libpmsample.dylib`

```diff

-278.0.0.0.0
-  __TEXT.__text: 0x159c
-  __TEXT.__auth_stubs: 0x3b0
+281.0.0.0.0
+  __TEXT.__text: 0x16b4
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x223
-  __TEXT.__unwind_info: 0xc0
+  __TEXT.__cstring: 0x23b
+  __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__got: 0x60
   __DATA_CONST.__const: 0x168
   __AUTH_CONST.__const: 0xc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x1e0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x8
-  __DATA_DIRTY.__bss: 0x68
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libpmenergy.dylib
-  Functions: 35
-  Symbols:   84
+  Functions: 46
+  Symbols:   96
   CStrings:  24
 
Symbols:
+ _bzero
+ _pm_sample_pid_version
+ _pm_sample_task_and_pid_version
+ _pm_sample_task_version
+ _pm_samples_copy_version
+ _pm_samples_delta_version
+ _pm_samples_destroy_version
+ _pm_samples_get_version
+ _pm_samples_init_version
+ _pm_samples_num_tasks_version
+ _pm_samples_sample_version
+ _pm_samples_to_array_version
+ _pm_task_subtract_version
- _pm_task_subtract
CStrings:
+ "pm_sample_all_internal_version"
+ "pm_samples_copy_version"
+ "pm_samples_delta_version"
- "pm_sample_all_internal"
- "pm_samples_copy"
- "pm_samples_delta"

```
