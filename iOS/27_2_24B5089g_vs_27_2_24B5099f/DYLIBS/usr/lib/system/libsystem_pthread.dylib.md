## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

 553.40.2.0.0
-  __TEXT.__text: 0xa348
+  __TEXT.__text: 0xa2cc
   __TEXT.__const: 0x160
   __TEXT.__cstring: 0xdbd
   __TEXT.__unwind_info: 0x420
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x228
-  __DATA.__data: 0x10
+  __DATA.__data: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x40

   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  Functions: 312
-  Symbols:   397
+  Functions: 311
+  Symbols:   396
   CStrings:  67
 
Symbols:
- _get_xprr_version.cached_xprr_version
Functions:
~ ___pthread_init : 1216 -> 1188
~ _pthread_jit_write_protect_supported_np : 48 -> 24
~ _pthread_jit_write_with_callback_np : 292 -> 280
~ _pthread_jit_write_freeze_callbacks_np : 144 -> 120
- _OUTLINED_FUNCTION_1
~ _pthread_jit_write_with_callback_np.cold.2 : 612 -> 596
```
