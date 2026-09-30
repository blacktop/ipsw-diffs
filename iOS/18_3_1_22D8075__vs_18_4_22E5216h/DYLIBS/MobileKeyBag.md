## MobileKeyBag

> `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`

```diff

-640.80.3.0.1
-  __TEXT.__text: 0x1d56c
+640.100.21.0.0
+  __TEXT.__text: 0x1dd9c
   __TEXT.__auth_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0x268
-  __TEXT.__cstring: 0x9533
+  __TEXT.__objc_methlist: 0x5c4
+  __TEXT.__cstring: 0x971c
   __TEXT.__const: 0x506
   __TEXT.__oslogstring: 0x28
   __TEXT.__gcc_except_tab: 0x640
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x8b8
+  __TEXT.__unwind_info: 0x938
   __TEXT.__objc_classname: 0x4e
   __TEXT.__objc_methname: 0x1509
   __TEXT.__objc_methtype: 0x9b0
   __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x108
-  __DATA_CONST.__const: 0x840
+  __DATA_CONST.__got: 0xe0
+  __DATA_CONST.__const: 0x860
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x520
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x9f0
-  __AUTH_CONST.__auth_ptr: 0x18
+  __AUTH_CONST.__auth_ptr: 0x40
   __AUTH_CONST.__const: 0x700
-  __AUTH_CONST.__cfstring: 0x4fa0
-  __AUTH_CONST.__objc_const: 0xd98
+  __AUTH_CONST.__cfstring: 0x4fc0
+  __AUTH_CONST.__objc_const: 0x718
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x4

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 558
-  Symbols:   989
-  CStrings:  1422
+  Functions: 666
+  Symbols:   1123
+  CStrings:  1431
 
Symbols:
+ _memcmp
- _objc_retain_x28
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
