## com.apple.driver.AppleSEPKeyStore

> `com.apple.driver.AppleSEPKeyStore`

```diff

-2369.0.0.0.7
-  __TEXT.__cstring: 0x51db sha256:8f578a3b0118364210ce6fb2b7b46451719adf36a16528462cc46a542c5924d9
-  __TEXT.__os_log: 0x83 sha256:2a28ec5ed41494257aeeb1555e73ca4688250f3e4591dacc3109941e0c45d55c
-  __TEXT.__const: 0xa7c sha256:61fa42d288f519dd1cbd2cdd0a39c05f735b53f8ec42833f089e68694f66d90d
-  __TEXT_EXEC.__text: 0x43058 sha256:263e3577784e78f16c6e4484190f0bcc92cbb1affc3ec64008004a6d4baa9ee0
+2155.160.10.0.0
+  __TEXT.__cstring: 0x4834 sha256:cb648409f0129a0bb2dcbec1739b7e71da1b511875da0edbf520b226b1b645a0
+  __TEXT.__const: 0x96c sha256:cce8fdf19debb5486fb505273a183ee1d060ce185f3b682fd532b78911dc9d6b
+  __TEXT_EXEC.__text: 0x3db5c sha256:d5a98ebc33d22be688b702dd0bee649cad30500b22e91031d2d26038f7b96253
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x414 sha256:16ee5b28271f93a545f73d14a73875fb52c18b7ed5719a9ebf1fe97e396b5cca
+  __DATA.__data: 0x3a4 sha256:dbd354e49b271cfa5031c2fdb99ef4831cbb0f33840acd39199dbdf6f266e8e7
   __DATA.__common: 0xe8 sha256:c4fcd50d9f0c893c46288b57d8e62b18523145956b249b6ecd6c21718be49065
-  __DATA.__bss: 0x4e0 sha256:2c253d268f274610134a7a0131fbf74a507bb6726c1b2c37193efe293c352e2c
-  __DATA_CONST.__mod_init_func: 0x10 sha256:1e8bad4ddb0548cd3ee313e8acbeb2eca8e3b02d2459332a43ff12e21a8f479e
-  __DATA_CONST.__mod_term_func: 0x10 sha256:cb807d4cc97d29dddcc31035fa678b1075d763517d3d64e406c4057a7f9b6f71
-  __DATA_CONST.__const: 0x4f50 sha256:538684859bdefb0670803b877e0dabc106119f017b3bceb706c4ea8540a92dc5
-  __DATA_CONST.__kalloc_type: 0xe00 sha256:bf4af2fa30314016f1d8506b6444f00c911f118098347598551c14f3a45cc4e3
-  __DATA_CONST.__kalloc_var: 0xa0 sha256:3510e42ce61176bb6bf90a3c5c35b09cafb1f0ffcb6faa7e8b871527fd84c1c3
-  __DATA_CONST.__auth_got: 0x520 sha256:6757163a7873a2f592a98c310698b9001026e703d5333fc8969ef2618551bc52
-  __DATA_CONST.__got: 0xa0 sha256:5b5bdd8666140c987212afe15aa8af610bf1392481c70e44a8dcde9f352bafd0
-  __DATA_CONST.__auth_ptr: 0x18 sha256:cc1b1974753d4ee3c7801f1e533a13c9ed0bc3cd729238a039e0ab87b44daf98
-  UUID: 9CC140F9-8F0F-3B80-980E-2F95FE492D4E
-  Functions: 1098
-  Symbols:   1967
-  CStrings:  444
+  __DATA.__bss: 0x300 sha256:ef115a0e0c15cdc41958ca46b5b14b456115f4baec5e3ca68599d2a8f435e3b8
+  __DATA_CONST.__auth_got: 0x4f8 sha256:6c009b384d2b0e58f88c2aea7525c06a9d17e90c435fc819840a634b5a958beb
+  __DATA_CONST.__got: 0x98 sha256:cf2f0e70808f768126a0675b56b1be1377955e136fe7ab25153a9fd7655d4a6b
+  __DATA_CONST.__auth_ptr: 0x18 sha256:610d16fa8644bde52cc399f725f562710f139764f931cf2f527a826feedb099c
+  __DATA_CONST.__mod_init_func: 0x10 sha256:0d467e1a35f4e38b9591c594c2bd6d2c1fca9a3cbb0ac0a06cb7fe5b656ff40d
+  __DATA_CONST.__mod_term_func: 0x10 sha256:b8e7ebc112898a5d30850cf516f24ec68b51cf6ffbf677d6dd01ae066f6b6758
+  __DATA_CONST.__const: 0x4c88 sha256:187be0e010311310631ffad6cde39e8c9f05562f61ed4e929ab523593a40700a
+  __DATA_CONST.__kalloc_type: 0xe00 sha256:f507c7fcabc99da7d53d069f8909269c24abdf6d3d5b33e9a02da6134f847655
+  __DATA_CONST.__kalloc_var: 0xa0 sha256:254aaa05fdce6fd01a36a6222b50e4e5bf0cce9f453efff392aa0d0cb112105f
+  UUID: 47759DF7-BBC3-363D-BAFB-B71B00CC8844
+  Functions: 1024
+  Symbols:   1843
+  CStrings:  379
 
Symbols:
+ _OUTLINED_FUNCTION_122
+ _ZN13AppleKeyStore11unwrap_dataEy13key_request_tiPKvjjS2_jS2_jS2_jPvPjS4_S3_S4_S3_S4_P18ipc_callback_ctx_t.cold.1
+ _ZN13AppleKeyStore21sep_deliver_msg_gatedEP18ipc_callback_ctx_tjP12ipc_args_all.cold.1
+ _ZN13AppleKeyStore21sep_deliver_msg_gatedEP18ipc_callback_ctx_tjP12ipc_args_all.cold.2
+ _ZN13AppleKeyStore21sep_deliver_msg_gatedEP18ipc_callback_ctx_tjP12ipc_args_all.cold.3
+ _ZN13AppleKeyStore21sep_deliver_msg_gatedEP18ipc_callback_ctx_tjP12ipc_args_all.cold.4
+ _ZN13AppleKeyStore26notify_change_device_stateEihhh.cold.1
+ _ZN13AppleKeyStore26notify_change_device_stateEihhh.cold.2
+ __ZN13AppleKeyStore11check_classEyiPKvjjP18ipc_callback_ctx_t
+ __ZN13AppleKeyStore11unwrap_dataEy13key_request_tiPKvjjS2_jS2_jS2_jPvPjS4_S3_S4_S3_S4_P18ipc_callback_ctx_t
+ __ZN13AppleKeyStore13add_vfs_eventEiPhi
+ __ZN13AppleKeyStore14notify_volumesEiih
+ __ZN13AppleKeyStore15get_stash_statsEPPvPj
+ __ZN13AppleKeyStore15sep_deliver_msgEP18ipc_callback_ctx_tjP12ipc_args_all
+ __ZN13AppleKeyStore15tdm_deliver_msgEP18ipc_callback_ctx_tjP12ipc_args_all
+ __ZN13AppleKeyStore16add_client_eventEijjhh
+ __ZN13AppleKeyStore16get_keybag_statsEPPvPj
+ __ZN13AppleKeyStore16remote_peer_dropEyiPKvj
+ __ZN13AppleKeyStore16smartcard_unlockEyiPKvjS1_jPPvPj
+ __ZN13AppleKeyStore18fv_new_sibling_vekEyP14aks_fv_param_sP13aks_fv_data_sPKhS3_P12aks_fv_key_s
+ __ZN13AppleKeyStore18notify_se_recoveryEij
+ __ZN13AppleKeyStore18smartcard_registerEyiPKvj20aks_smartcard_mode_sS1_jPPvPj
+ __ZN13AppleKeyStore20smartcard_unregisterEyi
+ __ZN13AppleKeyStore21remote_peer_get_stateEyiPKvjPPvPj
+ __ZN13AppleKeyStore21rewrap_data_with_optsEyjPKvjS1_jiiP16aks_fs_context_sS3_jjS1_jPvPjS5_S1_jS1_jP18ipc_callback_ctx_t
+ __ZN13AppleKeyStore21sep_deliver_msg_gatedEP18ipc_callback_ctx_tjP12ipc_args_all
+ __ZN13AppleKeyStore21tdm_deliver_msg_gatedEP18ipc_callback_ctx_tjP12ipc_args_all
+ __ZN13AppleKeyStore24smartcard_request_unlockEyiPKvjPPvPj
+ __ZN13AppleKeyStore25tickle_backup_notify_portEi
+ __ZN13AppleKeyStore26notify_change_device_stateEihhh
+ __ZN13AppleKeyStore27tdm_fillup_callback_contextEP18ipc_callback_ctx_tP14aks_fv_param_s
+ __ZN13AppleKeyStore32tickle_system_keybag_update_portEij
+ __ZN13AppleKeyStore7new_keyEy13key_request_tiPKvjP16aks_fs_context_sjS2_jPvPjS6_S5_S6_S5_S6_S5_S6_S5_S6_S6_P18ipc_callback_ctx_t
+ __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3749
+ __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3782
+ __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3462
+ __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1821
+ __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3491
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2719
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2746
+ __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_1845
+ ____ZN13AppleKeyStore15sep_deliver_msgEP18ipc_callback_ctx_tjP12ipc_args_all_block_invoke
+ ____ZN13AppleKeyStore15tdm_deliver_msgEP18ipc_callback_ctx_tjP12ipc_args_all_block_invoke
+ ____ZN13AppleKeyStore27tdm_fillup_callback_contextEP18ipc_callback_ctx_tP14aks_fv_param_s_block_invoke
+ __block_descriptor_tmp.107
+ __block_descriptor_tmp.136
+ __block_descriptor_tmp.146
+ __block_descriptor_tmp.162
+ __block_descriptor_tmp.166
+ __block_descriptor_tmp.172
+ __block_descriptor_tmp.180
+ __block_descriptor_tmp.215
+ __block_descriptor_tmp.80
+ __ipc_fv_new_sibling_vek
+ __ipc_remote_peer_drop
+ __ipc_remote_peer_get_state
+ __ipc_smartcard_request_unlock
+ __ipc_smartcard_unlock
+ __ipc_smartcard_unregister
+ _code_ipc_escrow_keys_create
+ _code_ipc_fv_new_sibling_vek
+ _code_ipc_smartcard_request_unlock
+ _code_ipc_smartcard_unlock
- _OUTLINED_FUNCTION_100
- _OUTLINED_FUNCTION_116
- _OUTLINED_FUNCTION_123
- _OUTLINED_FUNCTION_127
- _OUTLINED_FUNCTION_128
- _OUTLINED_FUNCTION_129
- _OUTLINED_FUNCTION_130
- _OUTLINED_FUNCTION_131
- _OUTLINED_FUNCTION_132
- _OUTLINED_FUNCTION_133
- _OUTLINED_FUNCTION_135
- _OUTLINED_FUNCTION_136
- _OUTLINED_FUNCTION_137
- _OUTLINED_FUNCTION_138
- _OUTLINED_FUNCTION_139
- _OUTLINED_FUNCTION_140
- _OUTLINED_FUNCTION_141
- _OUTLINED_FUNCTION_142
- _ZN13AppleKeyStore11load_keybagEyPKvjPi.cold.1
- _ZN13AppleKeyStore11unwrap_dataEy13key_request_tiPKvjjS2_jS2_jS2_jPvPjS4_S3_S4_S3_S4_P16ipc_callback_ctx.cold.1
- _ZN13AppleKeyStore14pki_token_listEyiPP6OSData.cold.1
- _ZN13AppleKeyStore17pki_token_requestEyiPK6OSDataS2_PPS0_.cold.1
- _ZN13AppleKeyStore18pki_token_get_infoEyiPK6OSDataPyPPS0_.cold.1
- _ZN13AppleKeyStore18pki_token_registerEyiPK6OSDatabS2_20aks_pki_token_mode_sS2_21aks_pki_token_flags_sPPS0_.cold.1
- _ZN13AppleKeyStore18pki_token_registerEyiPK6OSDatabS2_20aks_pki_token_mode_sS2_21aks_pki_token_flags_sPPS0_.cold.2
- _ZN13AppleKeyStore18sep_wait_for_replyEP16AppleSEPEndpoint.cold.1
- _ZN13AppleKeyStore19pki_token_op_unlockEyiPK6OSDataS2_S2_PPS0_.cold.1
- _ZN13AppleKeyStore19pki_token_op_verifyEyiPK6OSDataS2_S2_S2_PPS0_.cold.1
- _ZN13AppleKeyStore21pki_token_op_registerEyiPK6OSDataS2_S2_S2_20aks_pki_token_mode_sS2_21aks_pki_token_flags_sPPS0_S6_.cold.1
- _ZN13AppleKeyStore21sep_deliver_msg_gatedEP16ipc_callback_ctxjP12ipc_args_all.cold.1
- _ZN13AppleKeyStore21sep_deliver_msg_gatedEP16ipc_callback_ctxjP12ipc_args_all.cold.2
- _ZN13AppleKeyStore21sep_deliver_msg_gatedEP16ipc_callback_ctxjP12ipc_args_all.cold.3
- _ZN13AppleKeyStore21sep_deliver_msg_gatedEP16ipc_callback_ctxjP12ipc_args_all.cold.4
- _ZN13AppleKeyStore22notify_kern_lock_stateEij.cold.1
- _ZN13AppleKeyStore25pki_token_op_set_passwordEyiPK6OSDataS2_S2_S2_PPS0_.cold.1
- _ZN13AppleKeyStore26notify_change_device_stateEiPKhhhh.cold.1
- _ZN13AppleKeyStore26notify_change_device_stateEiPKhhhh.cold.2
- __ZL22config_analytics_table
- __ZL30log_missing_keybag_entitlementPKcS0_
- __ZN12IOUserClient23releaseNotificationPortEP8ipc_port
- __ZN13AppleKeyStore11check_classEyiPKvjjP16ipc_callback_ctx
- __ZN13AppleKeyStore11unwrap_dataEy13key_request_tiPKvjjS2_jS2_jS2_jPvPjS4_S3_S4_S3_S4_P16ipc_callback_ctx
- __ZN13AppleKeyStore13add_vfs_eventEiPhib
- __ZN13AppleKeyStore13get_analyticsEPPvPj
- __ZN13AppleKeyStore14notify_volumesEiPKhihb
- __ZN13AppleKeyStore14pki_token_listEyiPP6OSData
- __ZN13AppleKeyStore15fs_new_key_bulkEP10aks_cred_sjP24aks_new_key_bulk_entry_sjPj
- __ZN13AppleKeyStore15sep_deliver_msgEP16ipc_callback_ctxjP12ipc_args_all
- __ZN13AppleKeyStore15tdm_deliver_msgEP16ipc_callback_ctxjP12ipc_args_all
- __ZN13AppleKeyStore16add_client_eventEiPKhP31notification_timestamp_ticket_tjjhh
- __ZN13AppleKeyStore16remote_peer_dropEyiPKvj20remote_peer_filter_t
- __ZN13AppleKeyStore17pki_token_requestEyiPK6OSDataS2_PPS0_
- __ZN13AppleKeyStore18pki_token_get_infoEyiPK6OSDataPyPPS0_
- __ZN13AppleKeyStore18pki_token_registerEyiPK6OSDatabS2_20aks_pki_token_mode_sS2_21aks_pki_token_flags_sPPS0_
- __ZN13AppleKeyStore19media_key_log_eventEPKcPKhmji
- __ZN13AppleKeyStore19pki_token_op_unlockEyiPK6OSDataS2_S2_PPS0_
- __ZN13AppleKeyStore19pki_token_op_verifyEyiPK6OSDataS2_S2_S2_PPS0_
- __ZN13AppleKeyStore20pki_token_unregisterEyiPK6OSData
- __ZN13AppleKeyStore21pki_token_op_registerEyiPK6OSDataS2_S2_S2_20aks_pki_token_mode_sS2_21aks_pki_token_flags_sPPS0_S6_
- __ZN13AppleKeyStore21remote_peer_get_stateEyiPKvj20remote_peer_filter_tPPvPj
- __ZN13AppleKeyStore21rewrap_data_with_optsEyjPKvjS1_jiiP16aks_fs_context_sS3_jjS1_jPvPjS5_S1_jS1_jP16ipc_callback_ctx
- __ZN13AppleKeyStore21sep_deliver_msg_gatedEP16ipc_callback_ctxjP12ipc_args_all
- __ZN13AppleKeyStore21tdm_deliver_msg_gatedEP16ipc_callback_ctxjP12ipc_args_all
- __ZN13AppleKeyStore22notify_kern_lock_stateEij
- __ZN13AppleKeyStore25pki_token_op_set_passwordEyiPK6OSDataS2_S2_S2_PPS0_
- __ZN13AppleKeyStore26notify_change_device_stateEiPKhhhh
- __ZN13AppleKeyStore27notify_kern_passcode_statusEyi
- __ZN13AppleKeyStore27tdm_fillup_callback_contextEP16ipc_callback_ctxP14aks_fv_param_s
- __ZN13AppleKeyStore31tickle_backup_notify_port_gatedEi
- __ZN13AppleKeyStore35submit_coreanalytics_apfs_cp_actionEyib
- __ZN13AppleKeyStore38tickle_system_keybag_update_port_gatedEij
- __ZN13AppleKeyStore7new_keyEy13key_request_tiPKvjP16aks_fs_context_sjS2_jPvPjS6_S5_S6_S5_S6_S5_S6_S5_S6_S6_P16ipc_callback_ctx
- __ZN19AppleKeyStoreHelper13itemsToOutputEmPP6OSDataP25IOExternalMethodArguments
- __ZN19AppleKeyStoreHelper14itemsFromInputEP25IOExternalMethodArgumentsmPP6OSData
- __ZN19AppleKeyStoreHelper17createPackedItemsEjPP6OSData
- __ZN23AppleKeyStoreUserClient40submit_coreanalytics_set_config_selectorEiPKhj
- __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3895
- __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3928
- __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3609
- __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1983
- __ZZN13AppleKeyStore14notify_volumesEiPKhihbE11_os_log_fmt
- __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3638
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2891
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2918
- __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_2007
- ____ZN13AppleKeyStore15sep_deliver_msgEP16ipc_callback_ctxjP12ipc_args_all_block_invoke
- ____ZN13AppleKeyStore15tdm_deliver_msgEP16ipc_callback_ctxjP12ipc_args_all_block_invoke
- ____ZN13AppleKeyStore18notify_se_recoveryEij_block_invoke_2
- ____ZN13AppleKeyStore22set_backup_notify_portEP8ipc_portP23AppleKeyStoreUserClient_block_invoke
- ____ZN13AppleKeyStore25set_systembag_notify_portEP8ipc_portP23AppleKeyStoreUserClient_block_invoke
- ____ZN13AppleKeyStore27tdm_fillup_callback_contextEP16ipc_callback_ctxP14aks_fv_param_s_block_invoke
- ____ZN13AppleKeyStore31tickle_backup_notify_port_gatedEi_block_invoke
- ____ZN13AppleKeyStore35clear_notification_ports_for_clientEP23AppleKeyStoreUserClient_block_invoke
- ____ZN13AppleKeyStore38tickle_system_keybag_update_port_gatedEij_block_invoke
- ___der_key_config_backoff_delay
- ___der_key_config_bind_kek
- ___der_key_config_escrow_passcode_period
- ___der_key_config_escrow_token_period
- ___der_key_config_graceperiod
- ___der_key_config_prederived_iterations
- ___der_key_config_prederived_passcode
- ___der_key_config_prederived_salt
- ___der_key_config_prederived_type
- ___der_key_group_uuid
- ___der_key_inactivity_reboot_enabled
- ___der_key_oneness_automatic_mode
- ___der_key_passcode
- ___der_key_user_uuid
- __blob_free
- __block_descriptor_tmp.115
- __block_descriptor_tmp.154
- __block_descriptor_tmp.155
- __block_descriptor_tmp.177
- __block_descriptor_tmp.181
- __block_descriptor_tmp.187
- __block_descriptor_tmp.195
- __block_descriptor_tmp.232
- __block_descriptor_tmp.81
- __block_descriptor_tmp.84
- __block_descriptor_tmp.85
- __block_descriptor_tmp.86
- __block_descriptor_tmp.87
- __block_descriptor_tmp.88
- __block_descriptor_tmp.89
- __ipc_new_pfk_data_bulk
- __ipc_remote_peer_drop_v1
- __ipc_remote_peer_get_state_v1
- __ipc_smartcard_get_info
- __ipc_smartcard_list
- __ipc_smartcard_op_register
- __ipc_smartcard_op_set_password
- __ipc_smartcard_op_unlock_v1
- __ipc_smartcard_op_verify
- __ipc_smartcard_register_v1
- __ipc_smartcard_request_v1
- __ipc_smartcard_unregister_v1
- __os_log_default
- __os_log_internal
- _code_ipc_new_pfk_data_bulk
- _code_ipc_smartcard_get_info
- _code_ipc_smartcard_list
- _code_ipc_smartcard_op_register
- _code_ipc_smartcard_op_set_password
- _code_ipc_smartcard_op_unlock
- _code_ipc_smartcard_op_verify
- _code_ipc_smartcard_request
- _decode_pfk_bulk_data
- _decode_primary_identity_state
- _der_dict_get_data
- _der_key_config_backoff_delay
- _der_key_config_bind_kek
- _der_key_config_escrow_passcode_period
- _der_key_config_escrow_token_period
- _der_key_config_graceperiod
- _der_key_config_prederived_iterations
- _der_key_config_prederived_passcode
- _der_key_config_prederived_salt
- _der_key_config_prederived_type
- _der_key_group_uuid
- _der_key_inactivity_reboot_enabled
- _der_key_oneness_automatic_mode
- _der_key_passcode
- _der_key_user_uuid
- _dump_deltas
- _get_kcv
- _ipc_port_release_send
- _stackshot_update_lock_state
- _stackshot_update_passcode_status
- _ticket_update
- dump_deltas._os_log_fmt
- dump_deltas._os_log_fmt.1
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRefugCPpzl8MCJfz6c7cTmL_x15IxVKnorDV6M/Library/Caches/com.apple.xbs/TemporaryDirectory.nvIg2p/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
+ "/AppleInternal/Library/BuildRoots/4~CRefugCPpzl8MCJfz6c7cTmL_x15IxVKnorDV6M/Library/Caches/com.apple.xbs/TemporaryDirectory.nvIg2p/Sources/AppleKeyStore_SEP_kexts/ipc.c"
+ "/AppleInternal/Library/BuildRoots/4~CRefugCPpzl8MCJfz6c7cTmL_x15IxVKnorDV6M/Library/Caches/com.apple.xbs/TemporaryDirectory.nvIg2p/Sources/AppleKeyStore_SEP_kexts/msg.c"
+ "/AppleInternal/Library/BuildRoots/4~CRefugCPpzl8MCJfz6c7cTmL_x15IxVKnorDV6M/Library/Caches/com.apple.xbs/TemporaryDirectory.nvIg2p/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/4~CRefugCPpzl8MCJfz6c7cTmL_x15IxVKnorDV6M/Library/Caches/com.apple.xbs/TemporaryDirectory.nvIg2p/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
+ "1122322"
+ "2155.160.10"
+ "22:43:59"
+ "IODeviceTree:/efi/platform"
+ "Jun  9 2026"
+ "apple-coprocessor-version"
+ "update effacable"
- "\"sep_wait_for_reply called from within sep_action\" @%s:%d"
- "\"submit_coreanalytics_set_config_selector: idx %d != kConfigAnalyticsFieldCount %d\" @%s:%d"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s: (%s) result=0x%x, class=%d, kcv=0x%02x%02x%02x%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %skAppleKeyStoreUnlockDevice=%d%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Can not set flags when using raw passcode%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Cannot set a non NULL uuid with v0 API%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s buffer size %d too small for data size %d%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s decode_primary_identity_state failed%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s handle:%d, result:%x%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s handle:%d, result:%x, flags_out:%llx, hash_out:%p%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s identity_get_primary failed%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s kern_get_extended_state failed%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s process %s (bundle_id: %s) must have %s entitlement for %s%s\n"
- "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAXo7_QHiupSpjNcTAzxlcWpOX2HNn7X4A/Library/Caches/com.apple.xbs/TemporaryDirectory.uwxums/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAXo7_QHiupSpjNcTAzxlcWpOX2HNn7X4A/Library/Caches/com.apple.xbs/TemporaryDirectory.uwxums/Sources/AppleKeyStore_SEP_kexts/ipc.c"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAXo7_QHiupSpjNcTAzxlcWpOX2HNn7X4A/Library/Caches/com.apple.xbs/TemporaryDirectory.uwxums/Sources/AppleKeyStore_SEP_kexts/msg.c"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAXo7_QHiupSpjNcTAzxlcWpOX2HNn7X4A/Library/Caches/com.apple.xbs/TemporaryDirectory.uwxums/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAXo7_QHiupSpjNcTAzxlcWpOX2HNn7X4A/Library/Caches/com.apple.xbs/TemporaryDirectory.uwxums/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAXo7_QHiupSpjNcTAzxlcWpOX2HNn7X4A/Library/Caches/com.apple.xbs/TemporaryDirectory.uwxums/Sources/AppleKeyStore_SEP_kexts/timestamp_ticket.c"
- "01:29:37"
- "112232222222"
- "2369.0.0.0.7"
- "May 27 2026"
- "acm_handle"
- "apfs_to_uea"
- "backoff_delay"
- "bind_kek"
- "com.apple.applekeystore.apfs.cp_action"
- "com.apple.applekeystore.selector.set_config"
- "com.apple.keystore.config.set.backoff_delay"
- "com.apple.keystore.config.set.escrow_passcode_period"
- "com.apple.keystore.config.set.escrow_token_period"
- "com.apple.keystore.config.set.graceperiod"
- "com.apple.keystore.config.set.max_unlock_attempts"
- "com.apple.keystore.config.set.oneness_automatic_mode"
- "com.apple.keystore.config.set.prederived_iterations"
- "com.apple.keystore.config.set.prederived_passcode"
- "com.apple.keystore.config.set.prederived_salt"
- "com.apple.keystore.config.set.prederived_type"
- "cp_action"
- "delta: %s = %x0x"
- "duration_ms"
- "entitled_for_%s"
- "entitled_for_config_set"
- "escrow_passcode_period"
- "escrow_token_period"
- "first_unlock"
- "fs_migrate_media_key_to_class"
- "fs_new_media_key"
- "fs_new_media_key_wrapped_to_class"
- "fs_unwrap_media_key_from_class"
- "fs_unwrap_media_key_from_uid"
- "fv_new_media_key"
- "fv_unwrap_media_key"
- "graceperiod"
- "has_%s"
- "inactivity_reboot"
- "kAppleKeyStoreKeyBagCreate"
- "kAppleKeyStoreKeyBagCreateWithData"
- "kext_to_apfs"
- "max_unlock_attempts"
- "media_key_log_event"
- "no matching volume bag for: handle = %d, action = %d, flags = 0x%x"
- "oneness_automatic_mode"
- "passcode"
- "prederived_iterations"
- "prederived_passcode"
- "prederived_salt"
- "prederived_type"
- "processing(delta_id:%d): last_timestamp=0x%llx"
- "sks_to_kext"
- "source"
- "uea_to_app"
- "user_uuid"

```
