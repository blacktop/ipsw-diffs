## com.apple.driver.AppleSEPKeyStore

> `com.apple.driver.AppleSEPKeyStore`

```diff

-2155.122.1.0.0
-  __TEXT.__cstring: 0x452f sha256:e894dd30b0112c5d2c9ced85e8f5ba0a94259486cfa0ad55a72a84ff7e5de682
-  __TEXT.__const: 0x96c sha256:cce8fdf19debb5486fb505273a183ee1d060ce185f3b682fd532b78911dc9d6b
-  __TEXT_EXEC.__text: 0x3c958 sha256:a1e7fb35cd7653d382fd2c51461f5d6aee0ade8de12a99973434172d28aeff43
+2369.0.0.0.7
+  __TEXT.__cstring: 0x4dbe sha256:87628dd9ee380079f0873243de4f575a5ad512ac2675b1a6c0bf579780088ca8
+  __TEXT.__os_log: 0x83 sha256:2a28ec5ed41494257aeeb1555e73ca4688250f3e4591dacc3109941e0c45d55c
+  __TEXT.__const: 0xa7c sha256:61fa42d288f519dd1cbd2cdd0a39c05f735b53f8ec42833f089e68694f66d90d
+  __TEXT_EXEC.__text: 0x3fa30 sha256:f9fdbcc8cd2264c369b668fd6b20e198458ae228a45c19b64ea261fe3c61068d
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3a4 sha256:2b9c1961300316f93e6fe4bdab8077afe190aab1e869c8364a08584207ec0b48
+  __DATA.__data: 0x414 sha256:074e83b52945fd297017245b53c2faad1e5d371b86cd50e2855f43497f8ac1b1
   __DATA.__common: 0xe8 sha256:c4fcd50d9f0c893c46288b57d8e62b18523145956b249b6ecd6c21718be49065
-  __DATA.__bss: 0x31c sha256:ff8a7cfd199be01b74d6c4c0994cc26bbe4dde81714da2b933d075dcc2088920
-  __DATA_CONST.__auth_got: 0x4f8 sha256:07ef03ce32776c366c7e9b20d3352ccceff045b02e33836e67a4d0c3fc0a1baf
-  __DATA_CONST.__got: 0x90 sha256:07c6c3d45eab7bae2c1185050aac14b0436c63709d952ce81ce0430dca0a7b1c
-  __DATA_CONST.__auth_ptr: 0x18 sha256:7f024bd6e3227b6ea0f8cad09ff620db241b63aa5b960c1f2c70c92a4b6c7f6e
-  __DATA_CONST.__mod_init_func: 0x10 sha256:94c3128db4aca5e8890832439916d61b90971b67e3310236f028030072fbd6fe
-  __DATA_CONST.__mod_term_func: 0x10 sha256:9eaa68b4cf2ffda4967a3c752bd89128579c467e6f9cc26123b0dc873e0f6cc2
-  __DATA_CONST.__const: 0x3ac8 sha256:2705ee7b6d3468ce6dec3810b94e1dfc952b0679644e3cff8c2dac253fd3c3fa
-  __DATA_CONST.__kalloc_type: 0xd80 sha256:b8d2230b862caafec96ae9bccac26fce1da673ff8361c70c3c77627c1ccc7c5d
-  __DATA_CONST.__kalloc_var: 0xa0 sha256:c612b7da13317ff99dcf091234ddc8f3af5d73283c56f2c4a60fdebf303c7bcd
-  UUID: C68BE14F-EDCC-3D19-A0FD-1B8E116141B1
-  Functions: 1014
+  __DATA.__bss: 0x500 sha256:bfe492baf731a0dbf6e1e050f5bc3fe8c1b049383194dcdf82f023bfa409f462
+  __DATA_CONST.__mod_init_func: 0x10 sha256:8f2c5fa7e2733c6b6e6a0b63271cb5c647fee7e28776f51adc7db28363d61c9a
+  __DATA_CONST.__mod_term_func: 0x10 sha256:db3faf1cb460f5b47977e5cf18bc0f26be6dcb6fa4812f9f322600d9097a984e
+  __DATA_CONST.__const: 0x3d90 sha256:02ef70ff7cc3814cd6506421a5ba2c13efec89a41ebecccfe3d7504052b4807b
+  __DATA_CONST.__kalloc_type: 0xd80 sha256:088a58549de57ee2c8544b6c26616bf5bc814d69ba2aa05e9384cbde83ead01b
+  __DATA_CONST.__kalloc_var: 0xa0 sha256:2d2929adb197c47b8358ed8d5d8da5f7ad1bd3e6db8be72341d864c90b1f1634
+  __DATA_CONST.__auth_got: 0x520 sha256:d48d2470b6d007bc01b56f62eabc1356d698e6805e035eff1d894d7daf7170ec
+  __DATA_CONST.__got: 0x98 sha256:cc2293a9a83bec8c9e030630bd95d281513c207d24a63f0d05720eba7d7e2a2c
+  __DATA_CONST.__auth_ptr: 0x18 sha256:d0a10f49159fa122a49b969c2f2478fc8f2751fa0530e36c53395e33b0a75e09
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
