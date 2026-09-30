## libsystem_kernel.dylib

> `/usr/lib/system/libsystem_kernel.dylib`

```diff

-11417.122.4.0.0
-  __TEXT.__text: 0x33190
-  __TEXT.__const: 0xc40
-  __TEXT.__cstring: 0x4e67
-  __TEXT.__unwind_info: 0xb28
+12377.0.81.0.3
+  __TEXT.__text: 0x333cc
+  __TEXT.__const: 0xc30
+  __TEXT.__cstring: 0x4e30
+  __TEXT.__unwind_info: 0xb08
   __DATA_CONST.__const: 0x20c8
-  __AUTH_CONST.__const: 0x120
-  __DATA.__crash_info: 0x40
+  __AUTH_CONST.__const: 0x150
+  __DATA.__crash_info: 0x148
   __DATA.__data: 0x1c0
-  __DATA.__common: 0x28
-  __DATA.__bss: 0x28
+  __DATA.__common: 0x30
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__data: 0x14
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x680
-  UUID: 9E195BE1-1733-345E-A9BF-50D0D7059647
-  Functions: 1484
-  Symbols:   1699
-  CStrings:  656
+  UUID: 48C00F13-E3CA-3263-9FB9-C7866075C6AE
+  Functions: 1499
+  Symbols:   1721
+  CStrings:  658
 
Symbols:
+ ___os_nexus_config_flow
+ __system_version_compat_check_path_suffix
+ __system_version_compat_open_shim
+ _eth_rule_iterate
+ _exclaves_aoe_message_loop
+ _exclaves_aoe_setup
+ _exclaves_aoe_work_loop
+ _funmount
+ _inet_rule_iterate
+ _mach_memory_entry_get_page_counts
+ _mach_vm_reclaim_update_kernel_accounting_trap
+ _os_channel_flow_adv_get_feedback
+ _os_channel_get_upp_buffer_stats
+ _os_nexus_flow_set_connection_idle
+ _os_packet_set_wake_flag
+ _posix_spawn_file_actions_addchdir
+ _posix_spawn_file_actions_addfchdir
+ _posix_spawnattr_set_conclavememlimit_ext
+ _system_version_compat_check_path_suffix
+ _system_version_compat_mode
+ _traffic_rule_types
- _kAccountingThreshold
- _mach_vm_deferred_reclamation_buffer_update_reclaimable_bytes
- _pkt_subtype_assert_fail
- _pkt_type_assert_fail
CStrings:
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "/private/preboot/Cryptexes/OS/System/Library/CoreServices/SystemVersion.plist"
+ "SystemVersion.plist"
+ "SystemVersionCompat.plist"
+ "iOSSystemVersion.plist"
- "assertion failed: (((struct __user_buflet *)(uintptr_t)bprev)) == ((void*)0) || (((struct __user_buflet *)(uintptr_t)bprev)) == ((((struct __user_quantum *)(((uint64_t)(ph) & (~((uint64_t)0xf)))))))->qum_buf"
- "invalid packet subtype"
- "invalid packet type"

```
