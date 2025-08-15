## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

-519.0.0.0.0
-  __TEXT.__text: 0xa118
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__const: 0x188
-  __TEXT.__cstring: 0xb19
-  __TEXT.__unwind_info: 0x300
+519.102.1.0.0
+  __TEXT.__text: 0xa8ac
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__const: 0x198
+  __TEXT.__cstring: 0xd7a
+  __TEXT.__unwind_info: 0x32c
   __DATA_CONST.__got: 0x30
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x228
   __DATA.__data: 0x8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x14
+  __DATA.__bss: 0x403c
   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__common: 0x38
-  __DATA_DIRTY.__bss: 0x1030
+  __DATA_DIRTY.__bss: 0x8020
   - /usr/lib/system/libdyld.dylib
+  - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 8F9C865B-29F5-346B-ADD5-FDE40E008C66
-  Functions: 325
-  Symbols:   567
-  CStrings:  56
+  UUID: 524D87C4-EA5D-38A0-9E9A-17369B9B8724
+  Functions: 339
+  Symbols:   594
+  CStrings:  65
 
Symbols:
+ ___pthread_init.cold.4
+ __dyld_register_for_bulk_image_loads
+ __pthread_jit_config
+ __pthread_jit_config_lock
+ __pthread_jit_write_protect_bulk_image_load_callback
+ __pthread_jit_write_protect_bulk_image_load_callback.cold.1
+ __pthread_jit_write_protect_freeze_config
+ __pthread_jit_write_protect_freeze_config.cold.1
+ __pthread_workqueue_allow_send_signals
+ _getsectiondata
+ _pthread_attr_setworkinterval_np
+ _pthread_jit_write_freeze_callbacks_np
+ _pthread_jit_write_freeze_callbacks_np.cold.1
+ _pthread_jit_write_freeze_callbacks_np.cold.2
+ _pthread_jit_write_protect_supported_np
+ _pthread_jit_write_with_callback_np
+ _pthread_jit_write_with_callback_np.cold.1
+ _pthread_jit_write_with_callback_np.cold.2
CStrings:
+ "BUG IN CLIENT OF LIBPTHREAD: Too many pthread jit write callbacks"
+ "BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() already called"
+ "BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_freeze_callbacks_np() called but freeze-late entitlement is missing"
+ "BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() callback not in allowlist"
+ "BUG IN CLIENT OF LIBPTHREAD: pthread_jit_write_with_callback_np() called before pthread_jit_write_freeze_callbacks_np()"
+ "BUG IN LIBPTHREAD: jit config vm_map PERMANENT failed"
+ "BUG IN LIBPTHREAD: jit config vm_protect() failed"
+ "__DATA_CONST"
+ "__pth_jit_func"

```
