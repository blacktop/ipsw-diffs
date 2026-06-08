## com.apple.driver.AppleSEPKeyStore

> `com.apple.driver.AppleSEPKeyStore`

```diff

-2155.122.1.0.0
-  __TEXT.__cstring: 0x452f
-  __TEXT.__const: 0x96c
-  __TEXT_EXEC.__text: 0x3c958
+2369.0.0.0.7
+  __TEXT.__cstring: 0x4dbe
+  __TEXT.__os_log: 0x83
+  __TEXT.__const: 0xa7c
+  __TEXT_EXEC.__text: 0x3fa30
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3a4
+  __DATA.__data: 0x414
   __DATA.__common: 0xe8
-  __DATA.__bss: 0x31c
-  __DATA_CONST.__auth_got: 0x4f8
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA.__bss: 0x500
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x3ac8
+  __DATA_CONST.__const: 0x3d90
   __DATA_CONST.__kalloc_type: 0xd80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: C68BE14F-EDCC-3D19-A0FD-1B8E116141B1
-  Functions: 1014
+  __DATA_CONST.__auth_got: 0x520
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__auth_ptr: 0x18
+  UUID: 46091A80-A4E2-3EA9-BA7F-05246C5D8E9B
+  Functions: 1057
   Symbols:   0
-  CStrings:  370
+  CStrings:  433
 
CStrings:
+ "\"sep_wait_for_reply called from within sep_action\" @%s:%d"
+ "\"submit_coreanalytics_set_config_selector: idx %d != kConfigAnalyticsFieldCount %d\" @%s:%d"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s: (%s) result=0x%x, class=%d, kcv=0x%02x%02x%02x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %skAppleKeyStoreUnlockDevice=%d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s buffer size %d too small for data size %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s decode_primary_identity_state failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_get_primary failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kern_get_extended_state failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s process %s (bundle_id: %s) must have %s entitlement for %s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore/timestamp_ticket.c"
+ "112232222222"
+ "121111121222121211112121221111122121121221111222111111211222222"
+ "22:58:59"
+ "2369.0.0.0.7"
+ "May 27 2026"
+ "acm_handle"
+ "apfs_to_uea"
+ "backoff_delay"
+ "bind_kek"
+ "com.apple.applekeystore.apfs.cp_action"
+ "com.apple.applekeystore.selector.set_config"
+ "com.apple.keystore.config.set.backoff_delay"
+ "com.apple.keystore.config.set.escrow_passcode_period"
+ "com.apple.keystore.config.set.escrow_token_period"
+ "com.apple.keystore.config.set.graceperiod"
+ "com.apple.keystore.config.set.max_unlock_attempts"
+ "com.apple.keystore.config.set.oneness_automatic_mode"
+ "com.apple.keystore.config.set.prederived_iterations"
+ "com.apple.keystore.config.set.prederived_passcode"
+ "com.apple.keystore.config.set.prederived_salt"
+ "com.apple.keystore.config.set.prederived_type"
+ "cp_action"
+ "delta: %s = %x0x"
+ "duration_ms"
+ "entitled_for_%s"
+ "entitled_for_config_set"
+ "escrow_passcode_period"
+ "escrow_token_period"
+ "first_unlock"
+ "fs_migrate_media_key_to_class"
+ "fs_new_media_key"
+ "fs_new_media_key_wrapped_to_class"
+ "fs_unwrap_media_key_from_class"
+ "fs_unwrap_media_key_from_uid"
+ "fv_new_media_key"
+ "fv_unwrap_media_key"
+ "graceperiod"
+ "has_%s"
+ "inactivity_reboot"
+ "kAppleKeyStoreKeyBagCreate"
+ "kAppleKeyStoreKeyBagCreateWithData"
+ "kext_to_apfs"
+ "max_unlock_attempts"
+ "media_key_log_event"
+ "no matching volume bag for: handle = %d, action = %d, flags = 0x%x"
+ "oneness_automatic_mode"
+ "passcode"
+ "prederived_iterations"
+ "prederived_passcode"
+ "prederived_salt"
+ "prederived_type"
+ "processing(delta_id:%d): last_timestamp=0x%llx"
+ "sks_to_kext"
+ "source"
+ "uea_to_app"
+ "user_uuid"
- "1122322"
- "1211111212221212111121212211122121121221111222111111211222222"
- "20:36:37"
- "2155.122.1"
- "Apr 23 2026"
- "update effacable"

```
