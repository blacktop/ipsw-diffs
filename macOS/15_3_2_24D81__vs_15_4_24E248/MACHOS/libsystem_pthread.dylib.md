## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

-535.0.0.0.0
+536.0.0.0.0
   __TEXT.__text: 0xaa90
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__const: 0x188
+  __TEXT.__const: 0x120
   __TEXT.__cstring: 0xdce
-  __TEXT.__unwind_info: 0x348
+  __TEXT.__unwind_info: 0x358
   __DATA_CONST.__got: 0x38
   __AUTH_CONST.__auth_got: 0x230
   __DATA.__data: 0x8

   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 642FAF7A-874E-37E6-8ABA-2B0CC09A3025
-  Functions: 309
-  Symbols:   462
+  UUID: 8D27EC9A-D919-31A4-8DF8-31A2FD2E593C
+  Functions: 313
+  Symbols:   469
   CStrings:  66
 
Symbols:
+ __pthread_qos_class_to_thread_qos
+ _pthread_joiner_prepost_wake.cold.1
+ _pthread_qos_class_and_override_decode.cold.1
+ pthread_override_qos_class_end_np.cold.1
+ pthread_override_qos_class_start_np.cold.1
+ sched_yield.cold.1

```
