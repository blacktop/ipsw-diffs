## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-640.40.2.0.0
-  __TEXT.__text: 0x1c1e8
+640.60.3.0.0
+  __TEXT.__text: 0x1cc8c
   __TEXT.__auth_stubs: 0x13c0
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__cstring: 0x80cc
+  __TEXT.__cstring: 0x914f
   __TEXT.__const: 0x506
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x640
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x898
+  __TEXT.__unwind_info: 0x8a0
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x1509
   __TEXT.__objc_methtype: 0x9b0
   __TEXT.__objc_stubs: 0x10e0
   __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x800
+  __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__auth_got: 0x9f0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x6c0
-  __AUTH_CONST.__cfstring: 0x4e00
+  __AUTH_CONST.__cfstring: 0x4e20
   __AUTH_CONST.__objc_const: 0xd98
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x40

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 548
-  Symbols:   979
-  CStrings:  1318
+  Functions: 550
+  Symbols:   981
+  CStrings:  1389
 
CStrings:
+ "AKSIdentityGetSessionTimeWindowsFailure"
+ "AnalyticsEvent: report_version: %!l(MISSING)lu, grace_period: %!l(MISSING)lu, failed_unlock_attempts: %!l(MISSING)lu, max_unlock_attempts: %!l(MISSING)lu, recovery_iterations: %!l(MISSING)lu, recovery_target_iterations: %!l(MISSING)lu, recovery_wc_protected: %!l(MISSING)lu, recovery_restricted: %!l(MISSING)lu, recovery_ps_protected: %!l(MISSING)lu, recovery_akpu_protected: %!l(MISSING)lu, recovery_auto: %!l(MISSING)lu, memento_supported: %!l(MISSING)lu, memento_exists: %!l(MISSING)lu, memento_passcode_generation: %!l(MISSING)lu, passcode_generation: %!l(MISSING)lu, inactivity_reboot_enabled: %!l(MISSING)lu, oneness_automatic_mode: %!l(MISSING)lu, user_uuid_mismatch: %!l(MISSING)lu, zero_user_uuid: %!l(MISSING)lu, group_uuid_mismatch: %!l(MISSING)lu, zero_group_uuid: %!l(MISSING)lu, keybag_state_no_pin: %!l(MISSING)lu, keybag_state_been_unlocked: %!l(MISSING)lu, keybag_state_passcode_threshold: %!l(MISSING)lu, keybag_state_mesa_token: %!l(MISSING)lu, keybag_state_recovery_required: %!l(MISSING)lu, keybag_state_not_recoverable: %!l(MISSING)lu, keybag_state_stash_unlocked: %!l(MISSING)lu, keybag_state_escrow_unwrap_required: %!l(MISSING)lu, keybag_state_smdk_entangled: %!l(MISSING)lu, keybag_state_staged_manifest: %!l(MISSING)lu, keybag_state_se_unrecoverable: %!l(MISSING)lu, keybag_state_se_recovery_required: %!l(MISSING)lu, keybag_state_se_entangled: %!l(MISSING)lu, keybag_state_se_healthy: %!l(MISSING)lu, keybag_state_se_been_unlocked: %!l(MISSING)lu, keybag_state_art_loaded: %!l(MISSING)lu, keybag_state_xart_unlock_policy: %!l(MISSING)lu, keybag_state_xart_policy_cached: %!l(MISSING)lu, keybag_state_xart_policy_dirty: %!l(MISSING)lu, keybag_state_xart_policy_enforced: %!l(MISSING)lu, keybag_state_ps_entangled: %!l(MISSING)lu, keybag_state_from_xart: %!l(MISSING)lu, keybag_state_allow_test_keys: %!l(MISSING)lu, keybag_state_remote_session_unlocked: %!l(MISSING)lu, keybag_state_has_group_seed: %!l(MISSING)lu, keybag_state_been_passcode_unlocked: %!l(MISSING)lu, keybag_state_has_auto_recovery: %!l(MISSING)lu, keybag_state_has_lkgp_recovery: %!l(MISSING)lu, keybag_state_has_fv_recovery: %!l(MISSING)lu, keybag_state_has_memento_blob: %!l(MISSING)lu, keybag_more_state_cx_expiring: %!l(MISSING)lu, keybag_more_state_cx_expired: %!l(MISSING)lu, keybag_more_state_recovery_ps_fua_cached: %!l(MISSING)lu, keybag_more_state_unlocked_with_escrow: %!l(MISSING)lu, keybag_more_state_oneness_assert: %!l(MISSING)lu, hours_since_locked: %!l(MISSING)lu, cx_hours_remaining: %!l(MISSING)lu, days_since_passcode_change: %!l(MISSING)lu, memento_flags_blob_exists: %!l(MISSING)lu, memento_flags_se: %!l(MISSING)lu, memento_flags_ps: %!l(MISSING)lu, memento_flags_se_reset_token: %!l(MISSING)lu, memento_flags_tombstone: %!l(MISSING)lu, memento_failed_unlock_attempts: %!l(MISSING)lu, memento_se_slot: %!l(MISSING)lu, aks_get_extended_device_state_failure: %!l(MISSING)lu, AKSIdentityGetSessionTimeWindowsFailure: %!l(MISSING)lu, aks_get_seconds_since_passcode_change_failure: %!l(MISSING)lu, aks_memento_get_state_failure: %!l(MISSING)lu"
+ "aks_get_extended_device_state_failure"
+ "aks_get_seconds_since_passcode_change_failure"
+ "aks_memento_get_state_failure"
+ "analytics_send_user_keybag"
+ "com.apple.mobile.keybagd.user_keybag"
+ "cx_hours_remaining"
+ "failed_unlock_attempts"
+ "grace_period"
+ "group_uuid_mismatch"
+ "inactivity_reboot_enabled"
+ "keybag_more_state_cx_expired"
+ "keybag_more_state_cx_expiring"
+ "keybag_more_state_oneness_assert"
+ "keybag_more_state_recovery_ps_fua_cached"
+ "keybag_more_state_unlocked_with_escrow"
+ "keybag_state_allow_test_keys"
+ "keybag_state_art_loaded"
+ "keybag_state_been_passcode_unlocked"
+ "keybag_state_been_unlocked"
+ "keybag_state_escrow_unwrap_required"
+ "keybag_state_from_xart"
+ "keybag_state_has_auto_recovery"
+ "keybag_state_has_fv_recovery"
+ "keybag_state_has_group_seed"
+ "keybag_state_has_lkgp_recovery"
+ "keybag_state_has_memento_blob"
+ "keybag_state_mesa_token"
+ "keybag_state_no_pin"
+ "keybag_state_not_recoverable"
+ "keybag_state_passcode_threshold"
+ "keybag_state_ps_entangled"
+ "keybag_state_recovery_required"
+ "keybag_state_remote_session_unlocked"
+ "keybag_state_se_been_unlocked"
+ "keybag_state_se_entangled"
+ "keybag_state_se_healthy"
+ "keybag_state_se_recovery_required"
+ "keybag_state_se_unrecoverable"
+ "keybag_state_smdk_entangled"
+ "keybag_state_staged_manifest"
+ "keybag_state_stash_unlocked"
+ "keybag_state_xart_policy_cached"
+ "keybag_state_xart_policy_dirty"
+ "keybag_state_xart_policy_enforced"
+ "keybag_state_xart_unlock_policy"
+ "max_unlock_attempts"
+ "memento_exists"
+ "memento_failed_unlock_attempts"
+ "memento_flags_blob_exists"
+ "memento_flags_ps"
+ "memento_flags_se"
+ "memento_flags_se_reset_token"
+ "memento_flags_tombstone"
+ "memento_passcode_generation"
+ "memento_se_slot"
+ "memento_supported"
+ "oneness_automatic_mode"
+ "passcode_generation"
+ "recovery_akpu_protected"
+ "recovery_auto"
+ "recovery_iterations"
+ "recovery_ps_protected"
+ "recovery_restricted"
+ "recovery_target_iterations"
+ "recovery_wc_protected"
+ "report_version"
+ "user_uuid_mismatch"
+ "zero_group_uuid"
+ "zero_user_uuid"

```
