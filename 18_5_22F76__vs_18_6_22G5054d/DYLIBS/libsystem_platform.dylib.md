## libsystem_platform.dylib

> `/usr/lib/system/libsystem_platform.dylib`

```diff

-349.0.0.0.0
-  __TEXT.__text: 0x6040
+349.140.6.0.0
+  __TEXT.__text: 0x6260
   __TEXT.__stubs: 0x30
-  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__resolver_help: 0x1b0
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x75e
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0x795
+  __TEXT.__unwind_info: 0x240
   __DATA_CONST.__got: 0x18
-  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__auth_got: 0x100
   __AUTH_CONST.__const: 0x108
   __DATA.__crash_info: 0x40
   __DATA_DIRTY.__la_resolver: 0x20
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0x18
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_kernel.dylib
-  UUID: 2FEF24DE-6723-3799-A5C5-9E3DF1CD2600
-  Functions: 248
-  Symbols:   382
-  CStrings:  62
+  UUID: 992E3DF3-5AE1-3496-A1DD-F0C4F26D01D9
+  Functions: 253
+  Symbols:   391
+  CStrings:  64
 
Symbols:
+ ___os_security_config_init
+ ___os_security_config_init.cold.1
+ ___security_config
+ _os_security_config_get
+ _os_security_config_get_for_proc
+ _os_security_config_get_for_task
+ _task_info
CStrings:
+ "Could not parse security_config string"
+ "security_config"

```
