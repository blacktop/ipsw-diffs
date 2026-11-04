## libsystem_networkextension.dylib

> `/usr/lib/system/libsystem_networkextension.dylib`

```diff

-2365.40.3.0.2
-  __TEXT.__text: 0x16484
+2365.60.12.0.0
+  __TEXT.__text: 0x13a84
   __TEXT.__const: 0x110
   __TEXT.__cstring: 0x19e7
   __TEXT.__oslogstring: 0x2e90
   __TEXT.__unwind_info: 0x4e0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xd10
+  __DATA_CONST.__const: 0xd30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x28
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x178
+  __DATA_DIRTY.__bss: 0x170
   __DATA_DIRTY.__common: 0x2
   - /usr/lib/system/libcommonCrypto.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libxpc.dylib
-  Functions: 277
-  Symbols:   501
+  Functions: 279
+  Symbols:   506
   CStrings:  545
 
Symbols:
+ ___ne_log_register_fork_handler_block_invoke
+ __os_log_default
+ _g_large_log_obj
+ _g_log_obj
+ _ne_log_fork_child_handler
+ _ne_log_register_fork_handler.g_fork_init
+ _pthread_atfork
- _ne_log_large_obj.large_log_obj
- _ne_log_obj.log_obj
```
