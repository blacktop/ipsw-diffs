## libsystem_platform_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib`

```diff

-359.80.2.0.0
-  __TEXT.__text: 0x79a0
-  __TEXT.__stubs: 0x30
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__resolver_help: 0x1b0
+375.100.10.0.0
+  __TEXT.__text: 0x7b7c
+  __TEXT.__stubs: 0x3c
+  __TEXT.__auth_stubs: 0x1b0
+  __TEXT.__resolver_help: 0x21c
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x759
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__cstring: 0x7f2
+  __TEXT.__unwind_info: 0x1b0
   __TEXT.__eh_frame: 0xd8
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x108
+  __DATA.__script_config: 0x8000
   __DATA.__crash_info: 0x148
-  __DATA_DIRTY.__la_resolver: 0x20
+  __DATA_DIRTY.__la_resolver: 0x28
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x14
   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
-  UUID: 76902A68-9C48-30A9-BD0B-B3A1A81139BC
-  Functions: 254
-  Symbols:   301
-  CStrings:  53
+  UUID: 908C09AB-E5C2-3A6D-B186-E75B6FFA5511
+  Functions: 263
+  Symbols:   313
+  CStrings:  56
 
Symbols:
+ ___restrictions_config
+ __os_security_config_init.cold.2
+ __os_security_config_init.cold.3
+ __os_security_config_init.cold.4
+ _approx_timebase
+ _mach_vm_protect
+ _os_apt_msg_async_task_stopped_4swift
+ _os_apt_msg_async_task_stopped_4swift_dev
+ _os_apt_msg_async_task_stopped_4swift_dev_prodel0
+ _os_apt_msg_async_task_stopped_4swift_nop
+ _os_apt_msg_async_task_stopped_4swift_prodel0
+ _os_script_config_storage
CStrings:
+ "BUG IN LIBPLATFORM: Failed to freeze config."
+ "BUG IN LIBPLATFORM: Failed to freeze script config storage."
+ "BUG IN LIBPLATFORM: Failed to reprotect config."

```
