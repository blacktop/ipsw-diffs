## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_DIRTY.__data`

```diff

-553.0.1.0.0
-  __TEXT.__text: 0xacf8
-  __TEXT.__const: 0x150
+553.40.2.0.0
+  __TEXT.__text: 0xac74
+  __TEXT.__const: 0x160
   __TEXT.__cstring: 0xe11
   __TEXT.__unwind_info: 0x368
   __TEXT.__auth_stubs: 0x460
   __DATA_CONST.__got: 0x38
   __AUTH_CONST.__auth_got: 0x230
   __AUTH_CONST.__auth_ptr: 0x8
-  __DATA.__data: 0x14
+  __DATA.__data: 0x8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x8044
   __DATA.__common: 0x2

   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  Functions: 316
-  Symbols:   450
+  Functions: 315
+  Symbols:   449
   CStrings:  68
 
Symbols:
- get_xprr_version.cached_xprr_version
Functions:
~ ___pthread_init : 1240 -> 1212
~ _pthread_jit_write_protect_np : 392 -> 400
~ _pthread_jit_write_protect_supported_np : 48 -> 24
~ _pthread_jit_write_with_callback_np : 304 -> 292
~ _pthread_jit_write_freeze_callbacks_np : 156 -> 132
- _OUTLINED_FUNCTION_1
~ pthread_jit_write_protect_np.cold.3 : 260 -> 244
~ pthread_jit_write_with_callback_np.cold.2 : 612 -> 596
```
