## keybagd

> `/usr/libexec/keybagd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-674.160.2.0.0
-  __TEXT.__text: 0x10fdc
-  __TEXT.__auth_stubs: 0xdf0
+674.160.5.0.0
+  __TEXT.__text: 0x11514
+  __TEXT.__auth_stubs: 0xe00
   __TEXT.__objc_stubs: 0x8c0
   __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x5735
+  __TEXT.__cstring: 0x5aa4
   __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__objc_classname: 0x6b
   __TEXT.__objc_methname: 0xf56
   __TEXT.__objc_methtype: 0x769
   __TEXT.__dlopen_cstrs: 0x11e
   __TEXT.__oslogstring: 0x9d
-  __TEXT.__unwind_info: 0x428
-  __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x180
+  __TEXT.__unwind_info: 0x430
+  __DATA_CONST.__auth_got: 0x710
+  __DATA_CONST.__got: 0x1a0
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__cfstring: 0x1f80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 354
-  Symbols:   280
-  CStrings:  841
+  Functions: 355
+  Symbols:   285
+  CStrings:  856
 
Symbols:
+ _aks_get_internal_info
+ _kAKSInternalInfoGroupSeedGeneration
+ _kAKSInternalInfoGroupSeedWrappingType
+ _kAKSInternalInfoGroupUserCount
+ _kAKSInternalInfoVolumeBagVEKCacheStatus
CStrings:
+ "-[KBXPCService changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:]_block_invoke_2"
+ "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, keybag_more_state_peer_records_dirty: %llu, keybag_more_state_peer_records_flush: %llu, keybag_more_state_se_input_uid_bound: %llu, keybag_more_state_cache_flow_enabled: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu, keybag_more_state_group_seed_proposed: %llu, keybag_more_state_group_seed_needs_roll: %llu, group_seed_generation: %llu, group_seed_wrapping_type: %llu, group_user_count: %llu, volume_bag_vek_cache_status: %llu, aks_get_internal_info_failure: %llu, vek_user_bound: %llu, vek_sys_bound: %llu, vek_proposed: %llu, vek_group_uuid_match: %llu, vek_group_seed_generation: %llu, vek_blob_state_failure: %llu"
+ "aks_get_internal_info_failure"
+ "group_seed_generation"
+ "group_seed_wrapping_type"
+ "group_user_count"
+ "keybag_more_state_cache_flow_enabled"
+ "keybag_more_state_group_seed_needs_roll"
+ "keybag_more_state_group_seed_proposed"
+ "keybag_more_state_se_input_uid_bound"
+ "vek_blob_state_failure"
+ "vek_group_seed_generation"
+ "vek_group_uuid_match"
+ "vek_proposed"
+ "vek_sys_bound"
+ "vek_user_bound"
+ "volume_bag_vek_cache_status"
- "-[KBXPCService changeSystemSecretWithEscrow:fromOldSecret:oldSize:toNewSecret:newSize:opaqueData:keepstate:withACM:reply:]_block_invoke"
- "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, keybag_more_state_peer_records_dirty: %llu, keybag_more_state_peer_records_flush: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu"
```
