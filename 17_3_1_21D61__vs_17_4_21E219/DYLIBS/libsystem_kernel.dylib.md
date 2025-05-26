## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

```diff

-10002.82.4.0.0
-  __TEXT.__text: 0x32444
-  __TEXT.__const: 0xb20
-  __TEXT.__cstring: 0x4c93
-  __TEXT.__unwind_info: 0x92c
-  __DATA_CONST.__const: 0x2028
+10063.102.14.0.0
+  __TEXT.__text: 0x32a50
+  __TEXT.__const: 0xb50
+  __TEXT.__cstring: 0x4cc3
+  __TEXT.__unwind_info: 0x94c
+  __DATA_CONST.__const: 0x2030
   __AUTH_CONST.__const: 0x120
   __DATA.__data: 0x1c8
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x28
-  __DATA.__bss: 0x24
+  __DATA.__bss: 0x1c
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0x680
   __DATA_DIRTY.__bss: 0x48
-  Functions: 1452
-  Symbols:   1654
-  CStrings:  640
+  Functions: 1469
+  Symbols:   1671
+  CStrings:  642
 
Symbols:
+ _exclaves_audio_buffer_copyout
+ _exclaves_audio_buffer_create
+ _exclaves_inbound_buffer_copyin
+ _exclaves_inbound_buffer_create
+ _exclaves_launch_conclave
+ _exclaves_lookup_service
+ _exclaves_notification_create
+ _exclaves_outbound_buffer_copyout
+ _exclaves_outbound_buffer_create
+ _exclaves_sensor_create
+ _exclaves_sensor_start
+ _exclaves_sensor_status
+ _exclaves_sensor_stop
+ _mach_vm_reclaim_is_reclaimed
+ _posix_spawnattr_set_kqworklooplimit_ext
+ _posix_spawnattr_set_use_sec_transition_shims_np
+ _proc_terminate_with_audittoken
CStrings:
+ "assertion failed: (((struct __user_buflet *)(uintptr_t)bprev)) == ((void*)0) || (((struct __user_buflet *)(uintptr_t)bprev)) == ((((struct __user_quantum *)(((uint64_t)(ph) & (~((uint64_t)0xf)))))))->qum_buf"
+ "has_sec_transition:"
+ "managedappdistributiond"
- "assertion failed: (((struct __user_buflet *)(uintptr_t)bprev)) == ((void*)0) || (((struct __user_buflet *)(uintptr_t)bprev)) == (((struct __user_quantum *)((uint64_t)(ph) & (~((uint64_t)0xf)))))->qum_buf"

```
