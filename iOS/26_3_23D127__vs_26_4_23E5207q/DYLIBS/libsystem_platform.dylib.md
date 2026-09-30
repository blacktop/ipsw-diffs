## libsystem_platform.dylib

> `/usr/lib/system/libsystem_platform.dylib`

```diff

-359.80.2.0.0
-  __TEXT.__text: 0x6870
-  __TEXT.__stubs: 0x30
-  __TEXT.__auth_stubs: 0x200
-  __TEXT.__resolver_help: 0x1b0
+375.100.10.0.0
+  __TEXT.__text: 0x6b44
+  __TEXT.__stubs: 0x3c
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__resolver_help: 0x21c
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x7d9
+  __TEXT.__cstring: 0x872
   __TEXT.__unwind_info: 0x238
   __DATA_CONST.__got: 0x18
-  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__auth_got: 0x110
   __AUTH_CONST.__const: 0x108
+  __DATA.__script_config: 0x8000
   __DATA.__crash_info: 0x148
-  __DATA_DIRTY.__la_resolver: 0x20
+  __DATA_DIRTY.__la_resolver: 0x28
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x18
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_kernel.dylib
-  UUID: 440513F7-C74E-35A6-A34A-D06A9DF88547
-  Functions: 262
-  Symbols:   407
-  CStrings:  66
+  UUID: 8909B8D1-8FDF-31C9-BFC6-B8881230F252
+  Functions: 272
+  Symbols:   428
+  CStrings:  69
 
Symbols:
+ ___os_security_config_init.cold.2
+ ___os_security_config_init.cold.3
+ ___os_security_config_init.cold.4
+ ___restrictions_config
+ ___sigaltstack
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
