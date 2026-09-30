## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

```diff

-11215.81.4.0.0
-  __TEXT.__text: 0x3340c
-  __TEXT.__const: 0xb78
-  __TEXT.__cstring: 0x5a5f
-  __TEXT.__unwind_info: 0xb30
-  __DATA_CONST.__const: 0x22f0
+11417.101.15.0.0
+  __TEXT.__text: 0x33834
+  __TEXT.__const: 0xc60
+  __TEXT.__cstring: 0x5b94
+  __TEXT.__unwind_info: 0xb18
+  __DATA_CONST.__const: 0x2380
   __AUTH_CONST.__const: 0x120
-  __DATA.__data: 0x1c0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x40
+  __DATA.__data: 0x1c0
   __DATA.__common: 0x38
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__bss: 0x34
-  __DATA_DIRTY.__common: 0x684
-  UUID: EEE9D0D3-DFFC-37CB-9CED-B27CD0286D8C
-  Functions: 1487
-  Symbols:   1657
-  CStrings:  725
+  __DATA_DIRTY.__common: 0x67c
+  UUID: 225CB279-20A9-381D-A163-D2BE263F5327
+  Functions: 1492
+  Symbols:   1669
+  CStrings:  736
 
Symbols:
+ ___oslog_coproc
+ ___oslog_coproc_reg
+ ___statfs_ext_impl
+ _err_codes_vm_reclaim
+ _err_vm_sub
+ _fstatfs_ext
+ _mach_vm_deferred_reclamation_buffer_allocate
+ _mach_vm_deferred_reclamation_buffer_flush
+ _mach_vm_deferred_reclamation_buffer_resize
+ _mach_vm_reclaim_is_reusable
+ _mach_vm_reclaim_query_state
+ _mach_vm_reclaim_ring_allocate
+ _mach_vm_reclaim_ring_capacity
+ _mach_vm_reclaim_ring_flush
+ _mach_vm_reclaim_ring_resize
+ _mach_vm_reclaim_round_capacity
+ _mach_vm_reclaim_try_cancel
+ _mach_vm_reclaim_try_enter
+ _os_log_coprocessor_as_kernel
+ _os_log_coprocessor_register_as_kernel
+ _statfs_ext
+ abort.572
+ abort.574
+ abort.591
- _mach_vm_deferred_reclamation_buffer_init
- _mach_vm_deferred_reclamation_buffer_synchronize
- _mach_vm_reclaim_is_available
- _mach_vm_reclaim_is_reclaimed
- _mach_vm_reclaim_mark_free
- _mach_vm_reclaim_mark_free_with_id
- _mach_vm_reclaim_mark_used
- _mach_vm_reclaim_ringbuffer_init
- _mach_vm_reclaim_synchronize
- abort.561
- abort.563
- abort.580
CStrings:
+ "(vm/?) unknown subsystem error"
+ "(vm/kernel)"
+ "(vm/reclaim)"
+ "(vm/reclaim) invalid argument"
+ "(vm/reclaim) invalid reclaim ID"
+ "(vm/reclaim) invalid region size"
+ "(vm/reclaim) invalid ring"
+ "(vm/reclaim) invalid ring capacity"
+ "(vm/reclaim) no error"
+ "(vm/reclaim) operation not supported"
+ "(vm/reclaim) ring already instantiated"
+ "assertion failed: (((struct __user_buflet *)(uintptr_t)bprev)) == ((void*)0) || (((struct __user_buflet *)(uintptr_t)bprev)) == ((((struct __user_quantum *)(((uint64_t)(ph) & (~((uint64_t)0xf)))))))->qum_buf"
+ "mach_vm_reclaim_try_enter failed"
- "assertion failed: (((struct __user_buflet *)(uintptr_t)bprev)) == ((void *)0) || (((struct __user_buflet *)(uintptr_t)bprev)) == ((((struct __user_quantum *)(((uint64_t)(ph) & (~((uint64_t)0xf)))))))->qum_buf"
- "mach_vm_reclaim_mark_free failed"

```
