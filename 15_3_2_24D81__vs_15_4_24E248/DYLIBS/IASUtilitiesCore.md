## IASUtilitiesCore

> `/System/Library/PrivateFrameworks/IASUtilitiesCore.framework/Versions/A/IASUtilitiesCore`

```diff

 657.0.0.0.0
-  __TEXT.__text: 0x380d8
+  __TEXT.__text: 0x371bc
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x169c
-  __TEXT.__const: 0x14e9
-  __TEXT.__cstring: 0x4bd0
+  __TEXT.__objc_methlist: 0x17bc
+  __TEXT.__const: 0x1519
+  __TEXT.__cstring: 0x4d1d
   __TEXT.__gcc_except_tab: 0x4e8
   __TEXT.__oslogstring: 0xc0c
-  __TEXT.__unwind_info: 0xb30
+  __TEXT.__unwind_info: 0xb28
   __TEXT.__objc_classname: 0x204
   __TEXT.__objc_methname: 0x3488
   __TEXT.__objc_methtype: 0xba5
   __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0x1630
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd60
+  __DATA_CONST.__objc_selrefs: 0xdf8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0x878
   __AUTH_CONST.__const: 0x310
   __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x2778
+  __AUTH_CONST.__objc_const: 0x2568
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x1f0
-  __DATA.__data: 0x94a
+  __DATA.__data: 0x95a
   __DATA.__bss: 0xa5
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 782CE654-3EFE-32ED-9CBF-754489DC2120
-  Functions: 1130
-  Symbols:   2655
-  CStrings:  1709
+  UUID: 264744C1-75AF-34CC-BF46-9B3E89ACFAE3
+  Functions: 1421
+  Symbols:   2971
+  CStrings:  1713
 
Symbols:
+ +[IASAuthenticationAgentController sharedController].cold.1
+ +[IASAuthenticationManager sharedManager].cold.1
+ ACMContextGetExternalForm.cold.1
+ IASLogObject.cold.1
+ _AKSGetStashStats
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___der_key_booted_from_uuid
+ ___der_key_config_recovery_params
+ ___der_key_peer_kcv
+ __aks_se_set_secret.cold.1
+ _aks_remote_reset_all_peers
+ _aks_remote_reset_peer
+ _decode_peer_state
+ _der_key_booted_from_uuid
+ _der_key_config_recovery_params
+ _der_key_peer_kcv
+ _iterate_path.cold.1
+ _merge_dict_cb.cold.1
+ _stash_stats_deserialize
+ aks_assert_consume.cold.1
+ aks_assert_drop.cold.1
+ aks_assert_hold.cold.1
+ aks_assert_promote.cold.1
+ aks_change_secret_epilogue.cold.1
+ aks_change_secret_opts.cold.1
+ aks_clear_backup_bag.cold.1
+ aks_delete_xart_leak.cold.1
+ aks_drop_auxiliary_auth_by_handle.cold.1
+ aks_drop_auxiliary_auth_by_uid.cold.1
+ aks_generation.cold.1
+ aks_internal_state.cold.1
+ aks_invalidate_sync_bags.cold.1
+ aks_kext_set_options.cold.1
+ aks_lkgp_recover.cold.1
+ aks_lock_bag.cold.1
+ aks_lock_cx.cold.1
+ aks_lock_device.cold.1
+ aks_lower_iteration_count.cold.1
+ aks_measure_and_seal_cryptex_manifest.cold.1
+ aks_memento_efface_blob.cold.1
+ aks_migrate_s_key.cold.1
+ aks_obliterate_class_d.cold.1
+ aks_oneness_heartbeat.cold.1
+ aks_prewarm_sps.cold.1
+ aks_recover_with_escrow_bag.cold.1
+ aks_register_for_notifications.cold.1
+ aks_remote_peer_drop.cold.1
+ aks_remote_reset_all_peers.cold.1
+ aks_run_internal_test.cold.1
+ aks_se_delete_reset_token.cold.1
+ aks_se_fail.cold.1
+ aks_se_recover.cold.1
+ aks_se_secret_drop.cold.1
+ aks_se_set_healthy.cold.1
+ aks_se_set_nonce.cold.1
+ aks_se_stage_stash.cold.1
+ aks_se_support_in_rm.cold.1
+ aks_se_support_in_rm_is_set.cold.1
+ aks_seal_cryptex_manifest_lock.cold.1
+ aks_set_cx_window.cold.1
+ aks_set_jcop_supports_updated_kud_policy.cold.1
+ aks_set_system_with_passcode.cold.1
+ aks_smartcard_unregister.cold.1
+ aks_stash_commit.cold.1
+ aks_stash_destroy.cold.1
+ aks_stash_enable.cold.1
+ aks_stash_persist.cold.1
+ aks_unload_bag.cold.1
+ aks_unload_session_bags.cold.1
+ aks_unlock_bag.cold.1
+ aks_unlock_device.cold.1
+ circular_queue_init.cold.1
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ get_aks_client_connection.cold.1
+ get_akstest_client_connection.cold.1
+ rfc3394_unwrap.cold.1
+ rfc3394_unwrap.cold.2
+ rfc3394_wrap.cold.1
+ rfc3394_wrap.cold.2
+ updateLogLevelFromKext.cold.1
- ___der_key_config_recovery_flags
- __isNullOrEqualMem2
- _aks_show_allowlist_with_map
- _der_key_config_recovery_flags
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "AKSGetStashStats"
+ "aks_remote_reset_all_peers"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"

```
