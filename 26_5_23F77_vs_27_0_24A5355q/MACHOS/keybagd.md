## keybagd

> `/usr/libexec/keybagd`

```diff

-674.100.13.0.0
-  __TEXT.__text: 0x21bc8
-  __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__objc_stubs: 0x1020
+695.0.0.0.0
+  __TEXT.__text: 0x215f4
+  __TEXT.__auth_stubs: 0x14b0
+  __TEXT.__objc_stubs: 0x1040
   __TEXT.__objc_methlist: 0x814
-  __TEXT.__cstring: 0x9baa
+  __TEXT.__cstring: 0x9a23
   __TEXT.__const: 0x1a8
-  __TEXT.__gcc_except_tab: 0x474
-  __TEXT.__objc_methname: 0x181c
-  __TEXT.__objc_classname: 0xa7
+  __TEXT.__gcc_except_tab: 0x478
+  __TEXT.__objc_methname: 0x182e
+  __TEXT.__objc_classname: 0xa6
   __TEXT.__objc_methtype: 0x967
   __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__oslogstring: 0x281
-  __TEXT.__unwind_info: 0x798
-  __DATA_CONST.__auth_got: 0xa60
-  __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x1050
-  __DATA_CONST.__cfstring: 0x4ea0
+  __TEXT.__unwind_info: 0x788
+  __DATA_CONST.__const: 0x1010
+  __DATA_CONST.__cfstring: 0x4e60
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__auth_got: 0xa68
+  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x870
-  __DATA.__objc_selrefs: 0x650
+  __DATA.__objc_selrefs: 0x658
   __DATA.__objc_ivar: 0x2c
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x1fa

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: EEF0BFC1-6F21-33D3-A75B-605F8727D152
-  Functions: 710
-  Symbols:   399
-  CStrings:  2125
+  UUID: CFB327BC-9F09-345F-A3D8-491F0F56FB7A
+  Functions: 701
+  Symbols:   400
+  CStrings:  2117
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x26
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x26
- _AKSGetKeyBagStats
- _AKSGetStashStats
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "AKSIdentityGetPrimary_failure"
+ "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, keybag_more_state_peer_records_dirty: %llu, keybag_more_state_peer_records_flush: %llu, keybag_more_state_se_input_uid_bound: %llu, keybag_more_state_cache_flow_enabled: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu, aks_get_configuration_failure: %llu, handle: %llu, is_primary_user: %llu, is_shared_ipad: %llu, supports_enhanced_apfs: %llu, AKSIdentityGetPrimary_failure: %llu"
+ "SecureElement"
+ "aks_get_configuration_failure"
+ "endSessionAndWait"
+ "handle"
+ "is_primary_user"
+ "is_shared_ipad"
+ "keybag_more_state_cache_flow_enabled"
+ "keybag_more_state_se_input_uid_bound"
+ "supports_enhanced_apfs"
- "0dnM19zBqLw5ZPhIo4GEkg"
- "AnalyticsEvent: present_for_minutes_while_unlocked: %llu, present_for_minutes_while_locked: %llu, automatic_su_enabled: %llu, analytics_failure: %llu"
- "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, keybag_more_state_peer_records_dirty: %llu, keybag_more_state_peer_records_flush: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu"
- "AnalyticsEvent: report_version: %llu, kAppleKeyStoreDeviceBag_count: %llu, kAppleKeyStoreBackupBag_count: %llu, kAppleKeyStoreEscrowBag_count: %llu, kAppleKeyStoreOTABackupBag_count: %llu, kAppleKeyStoreAsymmetricBackupBag_count: %llu, analytics_failure: %llu"
- "analytics_failure"
- "analytics_send_keybag_count_stats"
- "analytics_send_stash_presence"
- "automatic_su_enabled"
- "com.apple.mobile.keybagd.keybag_count_stats"
- "com.apple.mobile.keybagd.stash_presence"
- "kAppleKeyStoreAsymmetricBackupBag_count"
- "kAppleKeyStoreBackupBag_count"
- "kAppleKeyStoreDeviceBag_count"
- "kAppleKeyStoreEscrowBag_count"
- "kAppleKeyStoreOTABackupBag_count"
- "present_for_minutes_while_locked"
- "present_for_minutes_while_unlocked"

```
