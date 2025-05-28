## libsystem_platform.dylib

> `/usr/lib/system/libsystem_platform.dylib`

```diff

-306.0.1.0.0
-  __TEXT.__text: 0x5634
-  __TEXT.__auth_stubs: 0x1e0
+316.100.10.0.0
+  __TEXT.__text: 0x5a34
+  __TEXT.__auth_stubs: 0x1f0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x733
-  __TEXT.__unwind_info: 0x1bc
+  __TEXT.__cstring: 0x75b
+  __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__got: 0x18
   __AUTH_CONST.__const: 0x108
-  __AUTH_CONST.__auth_got: 0xf0
+  __AUTH_CONST.__auth_got: 0xf8
   __DATA.__crash_info: 0x40
   __DATA_DIRTY.__common: 0x18
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_kernel.dylib
-  Functions: 217
-  Symbols:   334
-  CStrings:  60
+  Functions: 224
+  Symbols:   343
+  CStrings:  61
 
Symbols:
+ ___ulock_wait2
+ __os_unfair_lock_trylock_with_options_slow
+ _os_sync_wait_on_address
+ _os_sync_wait_on_address_with_deadline
+ _os_sync_wait_on_address_with_timeout
+ _os_sync_wake_by_address_all
+ _os_sync_wake_by_address_any
+ _os_unfair_lock_trylock_with_options
CStrings:
+ "BUG IN LIBPLATFORM: ulock_wait2 failure"

```
