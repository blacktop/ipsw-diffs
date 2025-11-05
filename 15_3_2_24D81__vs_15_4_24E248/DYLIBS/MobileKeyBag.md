## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag`

```diff

-640.80.3.0.1
-  __TEXT.__text: 0x114ac
+640.101.1.0.0
+  __TEXT.__text: 0x11c48
   __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_methlist: 0x1a0
-  __TEXT.__cstring: 0x5f19
+  __TEXT.__objc_methlist: 0x424
+  __TEXT.__cstring: 0x6102
   __TEXT.__const: 0x490
   __TEXT.__gcc_except_tab: 0x428
   __TEXT.__dlopen_cstrs: 0x66
   __TEXT.__oslogstring: 0x28
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__unwind_info: 0x608
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methname: 0xd12
   __TEXT.__objc_methtype: 0x7b4
   __TEXT.__objc_stubs: 0x960
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__const: 0x400
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d0
+  __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x8
   __AUTH_CONST.__auth_got: 0x6b0
   __AUTH_CONST.__const: 0x750
-  __AUTH_CONST.__cfstring: 0x2e80
-  __AUTH_CONST.__objc_const: 0x768
+  __AUTH_CONST.__cfstring: 0x2ea0
+  __AUTH_CONST.__objc_const: 0x288
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x40
   __DATA.__data: 0x2e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7025128F-E5D4-32F3-8993-ED007E18B278
-  Functions: 352
-  Symbols:   910
-  CStrings:  1307
+  UUID: 4AF2A2B4-9346-3043-8DF6-F9759D98FD86
+  Functions: 413
+  Symbols:   997
+  CStrings:  1317
 
Symbols:
+ HealthPlistCopyOrCreateNew.cold.1
+ HealthPlistCopyOrCreateNew.cold.10
+ HealthPlistCopyOrCreateNew.cold.11
+ HealthPlistCopyOrCreateNew.cold.12
+ HealthPlistCopyOrCreateNew.cold.13
+ HealthPlistCopyOrCreateNew.cold.14
+ HealthPlistCopyOrCreateNew.cold.15
+ HealthPlistCopyOrCreateNew.cold.16
+ HealthPlistCopyOrCreateNew.cold.2
+ HealthPlistCopyOrCreateNew.cold.3
+ HealthPlistCopyOrCreateNew.cold.4
+ HealthPlistCopyOrCreateNew.cold.5
+ HealthPlistCopyOrCreateNew.cold.6
+ HealthPlistCopyOrCreateNew.cold.7
+ HealthPlistCopyOrCreateNew.cold.8
+ HealthPlistCopyOrCreateNew.cold.9
+ HealthPlistTest.cold.1
+ HealthPlistTest.cold.10
+ HealthPlistTest.cold.11
+ HealthPlistTest.cold.12
+ HealthPlistTest.cold.13
+ HealthPlistTest.cold.14
+ HealthPlistTest.cold.15
+ HealthPlistTest.cold.16
+ HealthPlistTest.cold.17
+ HealthPlistTest.cold.18
+ HealthPlistTest.cold.19
+ HealthPlistTest.cold.2
+ HealthPlistTest.cold.20
+ HealthPlistTest.cold.21
+ HealthPlistTest.cold.22
+ HealthPlistTest.cold.23
+ HealthPlistTest.cold.24
+ HealthPlistTest.cold.25
+ HealthPlistTest.cold.26
+ HealthPlistTest.cold.27
+ HealthPlistTest.cold.28
+ HealthPlistTest.cold.29
+ HealthPlistTest.cold.3
+ HealthPlistTest.cold.30
+ HealthPlistTest.cold.31
+ HealthPlistTest.cold.32
+ HealthPlistTest.cold.33
+ HealthPlistTest.cold.34
+ HealthPlistTest.cold.35
+ HealthPlistTest.cold.36
+ HealthPlistTest.cold.37
+ HealthPlistTest.cold.4
+ HealthPlistTest.cold.5
+ HealthPlistTest.cold.6
+ HealthPlistTest.cold.7
+ HealthPlistTest.cold.8
+ HealthPlistTest.cold.9
+ KBSaveKeyBag.cold.1
+ MKBDeviceGetGracePeriod.cold.1
+ MKBDeviceLockAssertion.cold.1
+ MKBDeviceLockAssertion.cold.2
+ MKBKeyBagCreateWithData.cold.1
+ MKBKeyBagHandleGetTypeID.cold.1
+ MKBVerifyPasswordWithContext.cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___analytics_send_stash_presence_block_invoke
+ __block_descriptor_tmp.198
+ __block_descriptor_tmp.207
+ __fv_bind_keybag_to_kek_block_invoke.cold.1
+ _analytics_send_stash_presence
+ _apfs_get_all_crypto_ids.cold.1
+ _apfs_get_all_crypto_ids.cold.2
+ _create_plist_with_version.cold.1
+ _twoSigFigsWithRoundUp
+ effaceBlastableBytes.cold.1
+ loadBlastableBytes.cold.1
+ load_binary_dict.cold.1
+ load_binary_dict.cold.2
+ load_binary_dict.cold.3
+ load_binary_dict.cold.4
+ storeBlastableBytes.cold.1
+ store_binary_dict_fd.cold.1
+ store_binary_dict_fd.cold.2
+ store_binary_dict_fd.cold.3
- __block_descriptor_tmp.196
CStrings:
+ "AnalyticsEvent: present_for_minutes_while_unlocked: %llu, present_for_minutes_while_locked: %llu, automatic_su_enabled: %llu, analytics_failure: %llu"
+ "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, keybag_more_state_peer_records_dirty: %llu, keybag_more_state_peer_records_flush: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu"
+ "analytics_failure"
+ "analytics_send_stash_presence"
+ "automatic_su_enabled"
+ "com.apple.mobile.keybagd.stash_presence"
+ "keybag_more_state_peer_records_dirty"
+ "keybag_more_state_peer_records_flush"
+ "present_for_minutes_while_locked"
+ "present_for_minutes_while_unlocked"
- "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu"

```
