## keybagd

> `/usr/libexec/keybagd`

```diff

-640.80.3.0.1
-  __TEXT.__text: 0x10084
-  __TEXT.__auth_stubs: 0xd40
-  __TEXT.__objc_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x2f0
+640.101.1.0.0
+  __TEXT.__text: 0x10a98
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x58c
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x4fd3
-  __TEXT.__gcc_except_tab: 0x18c
+  __TEXT.__cstring: 0x5280
+  __TEXT.__gcc_except_tab: 0x19c
   __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methname: 0xee4
+  __TEXT.__objc_methname: 0xf06
   __TEXT.__objc_methtype: 0x742
-  __TEXT.__dlopen_cstrs: 0xc4
+  __TEXT.__dlopen_cstrs: 0x11e
   __TEXT.__oslogstring: 0x9d
-  __TEXT.__unwind_info: 0x3a0
-  __DATA_CONST.__auth_got: 0x6b0
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__cfstring: 0x1ee0
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__auth_got: 0x6b8
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__auth_ptr: 0x40
+  __DATA_CONST.__const: 0x8f8
+  __DATA_CONST.__cfstring: 0x1f00
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xb28
-  __DATA.__objc_selrefs: 0x368
+  __DATA.__objc_const: 0x628
+  __DATA.__objc_selrefs: 0x418
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x164
-  __DATA.__bss: 0xac
+  __DATA.__bss: 0xc0
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 296AAD31-62FC-373C-891E-7AE7D9C9D003
-  Functions: 272
-  Symbols:   269
-  CStrings:  1055
+  UUID: ED843341-F561-3EE5-BEB9-F2F2323F303F
+  Functions: 325
+  Symbols:   270
+  CStrings:  1071
 
Symbols:
+ _AKSGetStashStats
CStrings:
+ "/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Contents/MacOS/SoftwareUpdate"
+ "AnalyticsEvent: present_for_minutes_while_unlocked: %llu, present_for_minutes_while_locked: %llu, automatic_su_enabled: %llu, analytics_failure: %llu"
+ "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, keybag_more_state_peer_records_dirty: %llu, keybag_more_state_peer_records_flush: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu"
+ "Class getSUPreferenceManagerClass(void)_block_invoke"
+ "SUPreferenceManager"
+ "analytics_failure"
+ "analytics_send_stash_presence"
+ "automatic_su_enabled"
+ "automaticallyInstallMacOSUpdates"
+ "com.apple.mobile.keybagd.stash_presence"
+ "defaultManager"
+ "keybag_more_state_peer_records_dirty"
+ "keybag_more_state_peer_records_flush"
+ "present_for_minutes_while_locked"
+ "present_for_minutes_while_unlocked"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SoftwareUpdate.framework/SoftwareUpdate"
+ "void *SoftwareUpdateLibrary(void)"
- "AnalyticsEvent: report_version: %llu, grace_period: %llu, failed_unlock_attempts: %llu, max_unlock_attempts: %llu, recovery_iterations: %llu, recovery_target_iterations: %llu, recovery_wc_protected: %llu, recovery_restricted: %llu, recovery_ps_protected: %llu, recovery_akpu_protected: %llu, recovery_auto: %llu, memento_supported: %llu, memento_exists: %llu, memento_passcode_generation: %llu, passcode_generation: %llu, inactivity_reboot_enabled: %llu, oneness_automatic_mode: %llu, user_uuid_mismatch: %llu, zero_user_uuid: %llu, group_uuid_mismatch: %llu, zero_group_uuid: %llu, keybag_state_no_pin: %llu, keybag_state_been_unlocked: %llu, keybag_state_passcode_threshold: %llu, keybag_state_mesa_token: %llu, keybag_state_recovery_required: %llu, keybag_state_not_recoverable: %llu, keybag_state_stash_unlocked: %llu, keybag_state_escrow_unwrap_required: %llu, keybag_state_smdk_entangled: %llu, keybag_state_staged_manifest: %llu, keybag_state_se_unrecoverable: %llu, keybag_state_se_recovery_required: %llu, keybag_state_se_entangled: %llu, keybag_state_se_healthy: %llu, keybag_state_se_been_unlocked: %llu, keybag_state_art_loaded: %llu, keybag_state_xart_unlock_policy: %llu, keybag_state_xart_policy_cached: %llu, keybag_state_xart_policy_dirty: %llu, keybag_state_xart_policy_enforced: %llu, keybag_state_ps_entangled: %llu, keybag_state_from_xart: %llu, keybag_state_allow_test_keys: %llu, keybag_state_remote_session_unlocked: %llu, keybag_state_has_group_seed: %llu, keybag_state_been_passcode_unlocked: %llu, keybag_state_has_auto_recovery: %llu, keybag_state_has_lkgp_recovery: %llu, keybag_state_has_fv_recovery: %llu, keybag_state_has_memento_blob: %llu, keybag_more_state_cx_expiring: %llu, keybag_more_state_cx_expired: %llu, keybag_more_state_recovery_ps_fua_cached: %llu, keybag_more_state_unlocked_with_escrow: %llu, keybag_more_state_oneness_assert: %llu, hours_since_locked: %llu, cx_hours_remaining: %llu, days_since_passcode_change: %llu, memento_flags_blob_exists: %llu, memento_flags_se: %llu, memento_flags_ps: %llu, memento_flags_se_reset_token: %llu, memento_flags_tombstone: %llu, memento_failed_unlock_attempts: %llu, memento_se_slot: %llu, aks_get_extended_device_state_failure: %llu, AKSIdentityGetSessionTimeWindowsFailure: %llu, aks_get_seconds_since_passcode_change_failure: %llu, aks_memento_get_state_failure: %llu"
- "distantFuture"

```
