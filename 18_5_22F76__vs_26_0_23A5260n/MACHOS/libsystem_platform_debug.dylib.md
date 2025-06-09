## libsystem_platform_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_platform_debug.dylib`

```diff

-349.0.0.0.0
-  __TEXT.__text: 0x70a0
+357.0.0.0.0
+  __TEXT.__text: 0x74e0
   __TEXT.__stubs: 0x30
-  __TEXT.__auth_stubs: 0x180
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__resolver_help: 0x1b0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x6de
-  __TEXT.__unwind_info: 0x198
+  __TEXT.__cstring: 0x746
+  __TEXT.__unwind_info: 0x1a8
   __TEXT.__eh_frame: 0xd8
   __DATA_CONST.__got: 0x10
-  __AUTH_CONST.__auth_got: 0xc0
+  __AUTH_CONST.__auth_got: 0xd0
   __AUTH_CONST.__const: 0x108
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA_DIRTY.__la_resolver: 0x20
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x14
   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
-  UUID: 63B8E796-2880-327C-8A90-6744ABBDBE69
-  Functions: 240
-  Symbols:   285
-  CStrings:  49
+  UUID: 24C6F397-0B34-3E23-97CA-B1CC2B3199EE
+  Functions: 248
+  Symbols:   296
+  CStrings:  52
 
Symbols:
+ ___os_security_config_init
+ ___security_config
+ __os_security_config_init.cold.1
+ __simple_snprintf
+ __simple_vsnprintf
+ __snprintf_out_of_space
+ _os_security_config_get
+ _os_security_config_get_for_proc
+ _os_security_config_get_for_task
+ _proc_pidinfo
+ _task_info
CStrings:
+ "BUG IN LIBPLATFORM: Overflow in _simple_snprintf"
+ "Could not parse security_config string"
+ "security_config"

```
