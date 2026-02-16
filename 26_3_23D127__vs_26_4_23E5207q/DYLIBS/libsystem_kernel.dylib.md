## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

```diff

-12377.82.2.0.0
-  __TEXT.__text: 0x33270
-  __TEXT.__const: 0xc38
-  __TEXT.__cstring: 0x5c13
-  __TEXT.__unwind_info: 0xb10
-  __DATA_CONST.__const: 0x28c8
+12377.100.591.502.1
+  __TEXT.__text: 0x33f28
+  __TEXT.__const: 0xc60
+  __TEXT.__cstring: 0x5ccf
+  __TEXT.__unwind_info: 0xb18
+  __DATA_CONST.__const: 0x28d0
   __AUTH_CONST.__const: 0x150
   __DATA.__crash_info: 0x148
   __DATA.__data: 0x1c0
-  __DATA.__common: 0x28
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x2c
+  __DATA.__common: 0x30
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x680
-  UUID: 8D830129-2CBE-32A9-B61E-CE493EECB399
-  Functions: 1504
-  Symbols:   1723
-  CStrings:  910
+  UUID: F9023A5C-B8CD-3E65-A72D-DF5C5D33815C
+  Functions: 1525
+  Symbols:   1748
+  CStrings:  914
 
Symbols:
+ __kernelrpc_mach_vm_reallocate
+ __kernelrpc_vm_reallocate
+ __simple_getenv
+ __simple_getenv.19
+ _abort.344
+ _abort.389
+ _abort.507
+ _commpage_pfz_base
+ _exclaves_aoe_enumerate_and_setup_services
+ _exclaves_aoe_get_all_service_infos
+ _exclaves_aoe_message_loop_with_service_id
+ _exclaves_aoe_work_loop_with_service_id
+ _exclaves_arbitrated_buffer_copyout
+ _exclaves_arbitrated_buffer_create
+ _exclaves_daemon_notification_deregister
+ _exclaves_daemon_notification_register
+ _mach_memory_info_redacted
+ _mach_vm_reallocate
+ _os_custom_x18_abi
+ _os_custom_x18_abi_get
+ _posix_spawnattr_set_telemetry_np
+ _thread_resume2
+ _thread_set_x86_64_compat
+ _thread_suspend2
+ _update_tpidr
+ _vm_reallocate
- _abort.499
- _abort.501
- _abort.512
CStrings:
+ "(os/kern) access to unmapped guard-object slot attempted"
+ "Deferred Reclaim"
+ "attempted to switch out of already disabled custom x18 ABI mode"
+ "attempted to switch to already enabled custom x18 ABI mode"
+ "pfz"
- "VM_MEMORY_22"

```
