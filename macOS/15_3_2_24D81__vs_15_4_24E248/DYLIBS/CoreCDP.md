## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/CoreCDP`

```diff

-386.234.0.0.0
-  __TEXT.__text: 0x5601c
+386.457.0.0.0
+  __TEXT.__text: 0x5594c
   __TEXT.__auth_stubs: 0xe70
-  __TEXT.__objc_methlist: 0x2e4c
-  __TEXT.__const: 0x1144
-  __TEXT.__gcc_except_tab: 0x1228
+  __TEXT.__objc_methlist: 0x3954
+  __TEXT.__const: 0x1174
+  __TEXT.__gcc_except_tab: 0x1218
   __TEXT.__oslogstring: 0x8ac2
-  __TEXT.__cstring: 0x5a52
+  __TEXT.__cstring: 0x5b66
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1470
+  __TEXT.__unwind_info: 0x14f8
   __TEXT.__objc_classname: 0x705
-  __TEXT.__objc_methname: 0x8e89
+  __TEXT.__objc_methname: 0x8ed5
   __TEXT.__objc_methtype: 0x1c55
-  __TEXT.__objc_stubs: 0x4da0
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1dd8
+  __TEXT.__objc_stubs: 0x4e00
+  __DATA_CONST.__got: 0x4c0
+  __DATA_CONST.__const: 0x1dd0
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fe8
+  __DATA_CONST.__objc_selrefs: 0x20b0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__auth_got: 0x748
-  __AUTH_CONST.__const: 0x1790
-  __AUTH_CONST.__cfstring: 0x3b80
-  __AUTH_CONST.__objc_const: 0x9bb0
+  __AUTH_CONST.__const: 0x1760
+  __AUTH_CONST.__cfstring: 0x3b40
+  __AUTH_CONST.__objc_const: 0x8708
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x870
   __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x1040
+  __DATA.__data: 0x1050
   __DATA.__bss: 0x151
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x7d0

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A386D4E2-60BB-3711-AFC2-8376AE03AB0A
-  Functions: 2037
-  Symbols:   4886
-  CStrings:  3696
+  UUID: 6BF4C7B0-3008-3067-858D-861C3A9EA193
+  Functions: 2240
+  Symbols:   5109
+  CStrings:  3699
 
Symbols:
+ +[CDPAccount sharedInstance].cold.1
+ +[CDPAnalyticsReporterRTC rtcAnalyticsReporter].cold.1
+ +[CDPEDPConfigProvider sharedInstance].cold.1
+ +[CDPLocalDevice sharedInstance].cold.1
+ +[CDPRecoveryKeyCache sharedInstance].cold.1
+ +[CDPUtilities isGuitarfishEnabled].cold.1
+ +[CDPUtilities isInternalBuild].cold.1
+ +[CDPUtilities isVirtualMachine].cold.1
+ +[CDPUtilities shouldClearRKCacheAfterGeneration].cold.1
+ +[CDPWalrusNotificationHandler sharedInstance].cold.1
+ +[CDPWebAccessNotificationHandler sharedInstance].cold.1
+ +[CDPWebAccessStateCache sharedInstance].cold.1
+ -[CDPLocalDevice currentProcessHasEntitlement:].cold.3
+ CDPDeviceClassToLocKey.cold.1
+ CDPLocalizedStringInTable.cold.1
+ _AKSGetStashStats
+ _CDPLogSystem.cold.1
+ _CDPLogSystemAnalytics.cold.1
+ _CDPSignpostGetNanoseconds.cold.1
+ _CDPSignpostLogSystem.cold.1
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
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ __69-[CDPCustodianRecoveryController startRecoverySessionWithCompletion:]_block_invoke.cold.1
+ ___block_descriptor_48_e8_32bs40w_e55_v24?0"AACustodianRecoveryRequestContext"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e49_v24?0"AACustodianDataRecoveryKeys"8"NSError"16l
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
+ _kCDPAnalyticsEscrowRecordCreationStartEvent
+ _merge_dict_cb.cold.1
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$fetchCustodianRecoveryKeysWithContext:completion:
+ _objc_msgSend$isGuitarfishEnabled
+ _objc_msgSend$setAccountIsGuitarfish:
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
+ initCDPDLocalDeviceSecretProxyImpl.cold.1
+ rfc3394_unwrap.cold.1
+ rfc3394_unwrap.cold.2
+ rfc3394_wrap.cold.1
+ rfc3394_wrap.cold.2
- -[CDPEscrowRecordViability updatedViabiltyWithRecord:].cold.1
- GCC_except_table8
- __69-[CDPCustodianRecoveryController startRecoverySessionWithCompletion:]_block_invoke.27
- __69-[CDPCustodianRecoveryController startRecoverySessionWithCompletion:]_block_invoke.27.cold.1
- ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_56_e8_32s40bs48w_e55_v24?0"AACustodianRecoveryRequestContext"8"NSError"16l
- ___block_descriptor_56_e8_32s40s48bs_e49_v24?0"AACustodianDataRecoveryKeys"8"NSError"16l
- ___der_key_config_recovery_flags
- _aks_show_allowlist_with_map
- _der_key_config_recovery_flags
- _kCDPAnalyticsFetchCustodianRecoveryInfoEvent
- _kCDPAnalyticsRecoveryCreateSessionEvent
- _kCDPAnalyticsValidateRecoveryCodeEvent
- _objc_msgSend$decodeFloatForKey:
- _objc_msgSend$encodeFloat:forKey:
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "/System/AppleInternal/Library/Frameworks/UserManagement.framework/UserManagement"
+ "AKSGetStashStats"
+ "aks_remote_reset_all_peers"
+ "com.apple.corecdp.icscCreationStart"
+ "decodeDoubleForKey:"
+ "encodeDouble:forKey:"
+ "fetchCustodianRecoveryKeysWithContext:completion:"
+ "setAccountIsGuitarfish:"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "com.apple.corecdp.recoveryContact.owner.createSession"
- "com.apple.corecdp.recoveryContact.owner.fetchCustodianRecoveryInfo"
- "com.apple.corecdp.recoveryContact.owner.validateCode"
- "decodeFloatForKey:"
- "encodeFloat:forKey:"

```
