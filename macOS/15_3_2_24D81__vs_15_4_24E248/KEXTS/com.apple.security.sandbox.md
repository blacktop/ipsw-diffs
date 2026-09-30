## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-2401.81.2.0.0
-  __TEXT.__const: 0x1e3f3
-  __TEXT.__cstring: 0x74bd
-  __TEXT.__os_log: 0x1c26
-  __TEXT_EXEC.__text: 0x43fcc
+2401.101.1.0.0
+  __TEXT.__os_log: 0x1d47
+  __TEXT.__const: 0x1e5a3
+  __TEXT.__cstring: 0x7626
+  __TEXT_EXEC.__text: 0x45244
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
-  __DATA.__bss: 0x7f120
-  __DATA_CONST.__auth_got: 0x9c0
-  __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x3ad8
-  __DATA_CONST.__kalloc_var: 0x4b0
+  __DATA.__bss: 0x7f128
+  __DATA_CONST.__auth_got: 0x9d0
+  __DATA_CONST.__got: 0xf0
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__const: 0x3ac0
   __DATA_CONST.__kalloc_type: 0x12c0
-  UUID: 47ADDBD1-61EF-381E-BE16-C75492B05357
-  Functions: 871
-  Symbols:   1847
-  CStrings:  1460
+  __DATA_CONST.__kalloc_var: 0x4b0
+  UUID: 460799ED-F203-3112-9706-1E2DA9884890
+  Functions: 869
+  Symbols:   1869
+  CStrings:  1477
 
Symbols:
+ _ZL17_copy_root_volumev.cold.1
+ __MergedGlobals
+ ___copy_helper_block_8_32r40r48r56r64r72r80r88r
+ ___copy_helper_block_8_32r40r48r56r64r72r80r88r96r
+ ___destroy_helper_block_8_32r40r48r56r64r72r80r88r
+ ___destroy_helper_block_8_32r40r48r56r64r72r80r88r96r
+ ___extensions_update_path_block_invoke
+ __block_descriptor_tmp.1.2316
+ __block_descriptor_tmp.113
+ __block_descriptor_tmp.115
+ __block_descriptor_tmp.12.1438
+ __block_descriptor_tmp.12.2504
+ __block_descriptor_tmp.12.2547
+ __block_descriptor_tmp.1293
+ __block_descriptor_tmp.13.1675
+ __block_descriptor_tmp.1346
+ __block_descriptor_tmp.14.816
+ __block_descriptor_tmp.1407
+ __block_descriptor_tmp.1518
+ __block_descriptor_tmp.16.979
+ __block_descriptor_tmp.1673
+ __block_descriptor_tmp.20.2518
+ __block_descriptor_tmp.21.2934
+ __block_descriptor_tmp.2322
+ __block_descriptor_tmp.24
+ __block_descriptor_tmp.2400
+ __block_descriptor_tmp.25.1413
+ __block_descriptor_tmp.2501
+ __block_descriptor_tmp.2531
+ __block_descriptor_tmp.2586
+ __block_descriptor_tmp.27.2519
+ __block_descriptor_tmp.273
+ __block_descriptor_tmp.28
+ __block_descriptor_tmp.2928
+ __block_descriptor_tmp.32
+ __block_descriptor_tmp.323
+ __block_descriptor_tmp.326
+ __block_descriptor_tmp.33
+ __block_descriptor_tmp.37
+ __block_descriptor_tmp.40
+ __block_descriptor_tmp.453
+ __block_descriptor_tmp.465
+ __block_descriptor_tmp.5.2536
+ __block_descriptor_tmp.5.2933
+ __block_descriptor_tmp.52
+ __block_descriptor_tmp.66
+ __block_descriptor_tmp.66.2644
+ __block_descriptor_tmp.7.1674
+ __block_descriptor_tmp.8.2941
+ __block_descriptor_tmp.810
+ __block_descriptor_tmp.854
+ __block_descriptor_tmp.9.2420
+ __block_descriptor_tmp.96
+ __block_descriptor_tmp.978
+ __block_literal_global.1291
+ __block_literal_global.2315
+ __block_literal_global.2502
+ __block_literal_global.2544
+ __block_literal_global.2562
+ __match_any_user_intent_file_extension_locked
+ _apply_data_volume_path_translation
+ _enforce_root_and_role_account_protections
+ _extensions_update_path
+ _get_vnode_fsid_and_fileid
+ _is_root_translation_enabled
+ _link_operations
+ _macl_check_creator_tracking_eligibility
+ _macl_check_path
+ _macl_check_volume
+ _macl_prepare_privilege_escalation_check
+ _match_sandcastle_home_directory_ancestor
+ _operation_would_elevate_privilege
+ _proc_getexecutablevnode_noblock
+ _proc_orig_ppidversion
+ _proc_original_ppid
+ _psignal_sigkill_with_reason
+ _sandbox_suspend
+ _sandcastle_match_pattern_exact
+ _sstrdup
+ _suspension_count
+ _swap_vnode_macl
+ _syscall_check_finder_automation
+ _syscall_enable_root_translation
+ _userspace_boot_handler
+ _ustackshots_pending
+ approval_do_callout._os_log_fmt.100
+ approval_do_callout._os_log_fmt.98
+ approval_response_wait._os_log_fmt.103
+ check_system_data_volume_mount._os_log_fmt
+ collection_init._os_log_fmt.20
+ derive_socket_info.kalloc_type_view_1900
+ derive_summary._os_log_fmt.67
+ eval_modifier_descriptor._os_log_fmt.276
+ extension_create.kalloc_type_view_1121
+ extension_release.kalloc_type_view_1349
+ extension_set_create_class_locked.kalloc_type_view_673
+ extension_set_create_class_locked.kalloc_type_view_677
+ extension_set_create_storage_class_locked.kalloc_type_view_705
+ extension_set_new.kalloc_type_view_409
+ extension_set_release.kalloc_type_view_513
+ extension_set_release.kalloc_type_view_531
+ extension_set_release.kalloc_type_view_537
+ free_queued_events.kalloc_type_view_1418
+ handle_microstackshot.kalloc_type_view_1792
+ hook_vnode_notify_setflags.last_flags
+ hook_vnode_notify_setflags.last_uniqueid
+ is_root_device_same_as_boot_device._os_log_fmt.29
+ macl_lock_group.1354
+ operation_names.2676
+ pending_approval_entry_create.kalloc_type_view_1427
+ pending_approval_entry_create.kalloc_type_view_1435
+ pending_approval_entry_release.kalloc_type_view_1406
+ proc_apply_sandbox._os_log_fmt.29
+ proc_apply_sandbox._os_log_fmt.32
+ profile_depends_on_named_builtin._os_log_fmt.43
+ profile_init._os_log_fmt.16
+ profile_init_from_collection._os_log_fmt.62
+ profile_populate_base_profile._os_log_fmt.42
+ re_cache_init.kalloc_type_view_2142
+ rootless_protect_device.cold.1
+ sandbox_lock_grp.1412
+ sb_user_approval._os_log_fmt.14
+ schedule_microstackshot._os_log_fmt.110
+ schedule_microstackshot._os_log_fmt.112
+ schedule_microstackshot.kalloc_type_view_1627
+ schedule_microstackshot.kalloc_type_view_1640
+ schedule_microstackshot.kalloc_type_view_1654
+ send_event_to_sandboxd._os_log_fmt.113
+ send_rootless_file_flags_telemetry._os_log_fmt
+ string_table_iterate._os_log_fmt.12
+ submit_queued_events_to_sandboxd.kalloc_type_view_1508
+ syscall_check_finder_automation._os_log_fmt
+ syscall_check_finder_automation._os_log_fmt.11
+ syscall_enable_root_translation._os_log_fmt
+ syscall_enable_root_translation._os_log_fmt.309
+ syscall_enable_root_translation._os_log_fmt.310
+ syscall_extension_issue._os_log_fmt.59
+ syscall_set_userland_profile._os_log_fmt.307
+ thread_ustackshot_destroy.kalloc_type_view_1570
+ userspace_boot_handler._os_log_fmt
+ validate_flag_counts._os_log_fmt.58
+ variables_populate._os_log_fmt.47
+ variables_populate.kalloc_type_view_2273
- __ZL22protected_devices_lock
- __ZL22protected_devices_root
- __ZL29protected_devices_initialized
- __ZZ23rootless_protect_deviceE31reported_null_protected_devices
- ___copy_helper_block_8_32r40r48r56r64r72r80r
- ___destroy_helper_block_8_32r40r48r56r64r72r80r
- ___syscall_extension_update_file_block_invoke
- ___syscall_extension_update_file_by_fileid_block_invoke
- __block_descriptor_tmp.1.3004
- __block_descriptor_tmp.101
- __block_descriptor_tmp.12.2530
- __block_descriptor_tmp.12.3192
- __block_descriptor_tmp.12.3235
- __block_descriptor_tmp.120
- __block_descriptor_tmp.13.2763
- __block_descriptor_tmp.13.815
- __block_descriptor_tmp.14.2607
- __block_descriptor_tmp.16.978
- __block_descriptor_tmp.20.3206
- __block_descriptor_tmp.21.3622
- __block_descriptor_tmp.23.2390
- __block_descriptor_tmp.2383
- __block_descriptor_tmp.2437
- __block_descriptor_tmp.2498
- __block_descriptor_tmp.25.2505
- __block_descriptor_tmp.26.2504
- __block_descriptor_tmp.2606
- __block_descriptor_tmp.27.3207
- __block_descriptor_tmp.271
- __block_descriptor_tmp.2761
- __block_descriptor_tmp.3012
- __block_descriptor_tmp.3088
- __block_descriptor_tmp.318
- __block_descriptor_tmp.3189
- __block_descriptor_tmp.321
- __block_descriptor_tmp.3219
- __block_descriptor_tmp.3275
- __block_descriptor_tmp.34
- __block_descriptor_tmp.35
- __block_descriptor_tmp.3616
- __block_descriptor_tmp.39
- __block_descriptor_tmp.39.3252
- __block_descriptor_tmp.454
- __block_descriptor_tmp.466
- __block_descriptor_tmp.5.3224
- __block_descriptor_tmp.5.3621
- __block_descriptor_tmp.51
- __block_descriptor_tmp.65
- __block_descriptor_tmp.65.3333
- __block_descriptor_tmp.7.2762
- __block_descriptor_tmp.8.3629
- __block_descriptor_tmp.809
- __block_descriptor_tmp.853
- __block_descriptor_tmp.9.3108
- __block_descriptor_tmp.91
- __block_descriptor_tmp.94
- __block_descriptor_tmp.977
- __block_literal_global.2381
- __block_literal_global.3003
- __block_literal_global.3190
- __block_literal_global.3232
- __block_literal_global.3250
- __extensions_notify_create_block_invoke.13
- __match_byteset
- __match_user_intent_file_extension_locked
- _data_volume_equivalent_mount_path
- _is_root_volume_authenticated
- _match_user_intent_extension
- _path_operations
- _sandbox_getspawnattrs
- _set_data_volume_equivalent_mount
- _ustackshots_count
- _vnode_getname_printable
- _vnode_putname_printable
- approval_do_callout._os_log_fmt.97
- approval_do_callout._os_log_fmt.99
- approval_response_wait._os_log_fmt.101
- collection_init._os_log_fmt.16
- derive_socket_info.kalloc_type_view_1885
- derive_summary._os_log_fmt.66
- eval_modifier_descriptor._os_log_fmt.275
- extension_create.kalloc_type_view_1042
- extension_release.kalloc_type_view_1270
- extension_set_create_class_locked.kalloc_type_view_675
- extension_set_create_class_locked.kalloc_type_view_679
- extension_set_create_storage_class_locked.kalloc_type_view_707
- extension_set_new.kalloc_type_view_411
- extension_set_release.kalloc_type_view_515
- extension_set_release.kalloc_type_view_533
- extension_set_release.kalloc_type_view_539
- free_queued_events.kalloc_type_view_1404
- handle_microstackshot.kalloc_type_view_1770
- is_root_device_same_as_boot_device._os_log_fmt.28
- macl_lock_group.2445
- operation_names.3365
- pending_approval_entry_create.kalloc_type_view_1425
- pending_approval_entry_create.kalloc_type_view_1433
- pending_approval_entry_release.kalloc_type_view_1404
- proc_apply_sandbox._os_log_fmt.27
- profile_depends_on_named_builtin._os_log_fmt.42
- profile_init._os_log_fmt.14
- profile_init_from_collection._os_log_fmt.61
- profile_populate_base_profile._os_log_fmt.40
- re_cache_init.kalloc_type_view_2127
- sandbox_lock_grp.2503
- sb_user_approval._os_log_fmt.12
- schedule_microstackshot._os_log_fmt.109
- schedule_microstackshot._os_log_fmt.111
- schedule_microstackshot.kalloc_type_view_1604
- schedule_microstackshot.kalloc_type_view_1617
- schedule_microstackshot.kalloc_type_view_1631
- send_event_to_sandboxd._os_log_fmt.112
- set_data_volume_equivalent_mount._os_log_fmt
- string_table_iterate._os_log_fmt.11
- submit_queued_events_to_sandboxd.kalloc_type_view_1490
- syscall_extension_issue._os_log_fmt.61
- syscall_set_userland_profile._os_log_fmt.304
- thread_ustackshot_destroy.kalloc_type_view_1552
- validate_flag_counts._os_log_fmt.57
- variables_populate._os_log_fmt.45
- variables_populate.kalloc_type_view_2258
CStrings:
+ "%s is not the volume root"
+ "%s set rootless flags on %s with flags=%lu"
+ "%s: invalid flags: 0x%llx"
+ "3211111"
+ "<redacted>"
+ "com.apple.private.security.enforce-132000394-policy"
+ "enabling 132000394 policy enforcement for %s[%d]"
+ "failed to resolve %s: %d"
+ "kTCCServiceMediaLibrary-telemetry-"
+ "kTCCServiceSystemPolicyAppData-telemetry-container-creation"
+ "mach_vm_deferred_reclamation_buffer_allocate"
+ "mach_vm_deferred_reclamation_buffer_flush"
+ "mach_vm_deferred_reclamation_buffer_resize"
+ "mach_vm_deferred_reclamation_buffer_update_reclaimable_bytes"
+ "not enabling root translation: data volume is APFS"
+ "process-info-sandbox-container"
+ "sb_role_account_protections"
+ "syscall_check_finder_automation"
+ "system data volume mounted"
+ "thread_raise_exception"
+ "unsupported extension type"
+ "userspace boot"
- "\"unsupported mask type #%d\" @%s:%d"
- "32211111"
- "ipc-posix-issue-extension"
- "kTCCServiceMediaLibrary-telemetry"
- "set_data_volume_equivalent_mount"

```
