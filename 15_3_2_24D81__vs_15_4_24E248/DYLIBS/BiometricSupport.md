## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/Versions/A/BiometricSupport`

```diff

-506.60.1.0.0
-  __TEXT.__text: 0x3b2bc
+511.100.15.0.0
+  __TEXT.__text: 0x3b60c
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x1ed4
-  __TEXT.__const: 0x10c4
-  __TEXT.__gcc_except_tab: 0x1140
-  __TEXT.__cstring: 0x5055
-  __TEXT.__oslogstring: 0x3097
-  __TEXT.__unwind_info: 0xc80
-  __TEXT.__objc_classname: 0x2af
-  __TEXT.__objc_methname: 0x5bf7
-  __TEXT.__objc_methtype: 0x1330
-  __TEXT.__objc_stubs: 0x4760
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x1678
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__objc_methlist: 0x2474
+  __TEXT.__const: 0x10f4
+  __TEXT.__gcc_except_tab: 0x1178
+  __TEXT.__cstring: 0x4bba
+  __TEXT.__oslogstring: 0x30b4
+  __TEXT.__unwind_info: 0xcd8
+  __TEXT.__objc_classname: 0x2ca
+  __TEXT.__objc_methname: 0x5cfc
+  __TEXT.__objc_methtype: 0x1339
+  __TEXT.__objc_stubs: 0x4820
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__const: 0x1688
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17f8
+  __DATA_CONST.__objc_selrefs: 0x18a0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0x288
+  __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x4d0
-  __AUTH_CONST.__cfstring: 0x2200
-  __AUTH_CONST.__objc_const: 0x4000
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x20c
-  __DATA.__data: 0xa38
+  __AUTH_CONST.__cfstring: 0x1c20
+  __AUTH_CONST.__objc_const: 0x36e8
+  __AUTH_CONST.__objc_intobj: 0xb10
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x210
+  __DATA.__data: 0xa48
   __DATA.__common: 0x28
-  __DATA.__bss: 0x61
+  __DATA.__bss: 0x69
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__common: 0x10
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 53048842-FF1A-3D59-8D3B-D342BCC00958
-  Functions: 1075
-  Symbols:   2861
-  CStrings:  2512
+  UUID: EDC7F8FF-617C-3461-9CFC-A509BB78E8A4
+  Functions: 1371
+  Symbols:   3196
+  CStrings:  2434
 
Symbols:
+ +[GraylistedClientABCIssue reportClient:withProcessName:forReporter:]
+ +[LegacyEntitlementABCIssue reportClient:withProcessName:forReporter:]
+ +[MissingPermissionABCIssue reportPermission:client:processName:forReporter:]
+ -[BiometricKitXPCExportedClientObject processName]
+ -[BiometricKitXPCExportedObject clientThrottleRatio:]
+ -[BiometricKitXPCExportedObject disconnect:replyBlock:].cold.1
+ -[BiometricKitXPCExportedObject getPreferencesValueForKey:client:replyBlock:].cold.1
+ -[BiometricKitXPCExportedObject getPreferencesValueForKey:client:replyBlock:].cold.2
+ -[BiometricKitXPCExportedObject hashClientName:]
+ -[BiometricKitXPCServer getAccessoryObject:].cold.1
+ -[BiometricKitXPCServer getProtectedConfigurationForUser:withClient:].cold.1
+ -[BiometricKitXPCServer getSystemProtectedConfigurationWithClient:].cold.1
+ -[BiometricKitXPCServer handleCatacombUnlock].cold.1
+ -[BiometricKitXPCServer listener:shouldAcceptNewConnection:].cold.1
+ -[BiometricKitXPCServer listener:shouldAcceptNewConnection:].cold.2
+ -[BiometricKitXPCServer osStateHandler:].cold.1
+ -[BiometricKitXPCServer pauseBioOperation:].cold.1
+ -[BiometricKitXPCServer startBioOperation:].cold.1
+ -[BiometricKitXPCServer startBioOperation:].cold.2
+ -[EntitlementABCIssue initWithClient:processName:forReporter:]
+ -[EntitlementABCIssue processName]
+ -[EntitlementABCIssue setProcessName:]
+ -[EntitlementABCIssueReporter reportGraylistedClient:withProcessName:]
+ -[EntitlementABCIssueReporter reportLegacyClient:withProcessName:]
+ -[EntitlementABCIssueReporter reportMissingPermission:forClientName:processName:]
+ -[GraylistedClientABCIssue abcReason]
+ -[GraylistedClientABCIssue context]
+ -[GraylistedClientABCIssue tag]
+ -[MissingPermissionABCIssue initWithPermission:client:processName:forReporter:]
+ GCC_except_table10
+ GCC_except_table117
+ GCC_except_table3
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table377
+ GCC_except_table380
+ GCC_except_table44
+ GCC_except_table48
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table87
+ OBJC_IVAR_$_EntitlementABCIssue._processName
+ _AKSGetStashStats
+ _OBJC_CLASS_$_GraylistedClientABCIssue
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_METACLASS_$_GraylistedClientABCIssue
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
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
+ _OUTLINED_FUNCTION_2
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
+ _OUTLINED_FUNCTION_3
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
+ __OBJC_$_CLASS_METHODS_GraylistedClientABCIssue
+ __OBJC_$_INSTANCE_METHODS_GraylistedClientABCIssue
+ __OBJC_CLASS_RO_$_GraylistedClientABCIssue
+ __OBJC_METACLASS_RO_$_GraylistedClientABCIssue
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
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$clientThrottleRatio:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$hashClientName:
+ _objc_msgSend$initWithClient:processName:forReporter:
+ _objc_msgSend$initWithPermission:client:processName:forReporter:
+ _objc_msgSend$processName
+ _objc_msgSend$reportClient:withProcessName:forReporter:
+ _objc_msgSend$reportGraylistedClient:withProcessName:
+ _objc_msgSend$reportLegacyClient:withProcessName:
+ _objc_msgSend$reportMissingPermission:forClientName:processName:
+ _objc_msgSend$reportPermission:client:processName:forReporter:
+ _objc_msgSend$setProcessName:
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
+ clientThrottleRatio:.graylisted
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ get_aks_client_connection.cold.1
+ get_akstest_client_connection.cold.1
+ rfc3394_unwrap.cold.1
+ rfc3394_unwrap.cold.2
+ rfc3394_wrap.cold.1
+ rfc3394_wrap.cold.2
- +[LegacyEntitlementABCIssue reportClient:forReporter:]
- +[MissingPermissionABCIssue reportPermission:client:forReporter:]
- -[BiometricKitXPCExportedObject legacyAllowlisted:]
- -[EntitlementABCIssue initWithClient:forReporter:]
- -[EntitlementABCIssueReporter reportLegacyClient:]
- -[EntitlementABCIssueReporter reportMissingPermission:forClientName:]
- -[MissingPermissionABCIssue initWithPermission:client:forReporter:]
- GCC_except_table115
- GCC_except_table29
- GCC_except_table30
- GCC_except_table42
- GCC_except_table46
- GCC_except_table50
- GCC_except_table56
- GCC_except_table9
- ___der_key_config_recovery_flags
- _aks_show_allowlist_with_map
- _der_key_config_recovery_flags
- _objc_msgSend$initWithClient:forReporter:
- _objc_msgSend$initWithPermission:client:forReporter:
- _objc_msgSend$legacyAllowlisted:
- _objc_msgSend$reportClient:forReporter:
- _objc_msgSend$reportLegacyClient:
- _objc_msgSend$reportMissingPermission:forClientName:
- _objc_msgSend$reportPermission:client:forReporter:
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "<uknown_process_name>"
+ "<unknown_process_name>"
+ "@44@0:8i16@20@28@36"
+ "AKSGetStashStats"
+ "BioGraylistedClient"
+ "Client %@/%@ throttling value=%d\n"
+ "GraylistedClient/%@/%@"
+ "GraylistedClientABCIssue"
+ "GraylistedClientConnection"
+ "Invalid bundleId %@\n"
+ "LegacyEntitlement/%@/%@"
+ "MissingPermissionABCIssue/%@/%@/%d"
+ "T@\"NSString\",&,N,V_processName"
+ "_processName"
+ "aks_remote_reset_all_peers"
+ "cStringUsingEncoding:"
+ "clientName=%@,processName=%@,permission=%d,v=2"
+ "clientName=%@,processName=%@,v=2"
+ "clientThrottleRatio:"
+ "componentsSeparatedByString:"
+ "hashClientName:"
+ "iOS"
+ "iOS,macOS,visionOS|10"
+ "iOS,macOS|1"
+ "iOS,macOS|10"
+ "iOS,macOS|100"
+ "iOS,visionOS|1"
+ "iOS,visionOS|10"
+ "iOS,visionOS|100"
+ "iOS,visionOS|1000"
+ "iOS,visionOS|10000"
+ "iOS,visionOS|100000"
+ "iOS|1"
+ "iOS|10"
+ "iOS|100"
+ "iOS|100000"
+ "initWithClient:processName:forReporter:"
+ "initWithPermission:client:processName:forReporter:"
+ "macOS|1"
+ "macOS|10"
+ "macOS|100"
+ "macOS|1000"
+ "processName"
+ "reportClient:withProcessName:forReporter:"
+ "reportGraylistedClient:withProcessName:"
+ "reportLegacyClient:withProcessName:"
+ "reportMissingPermission:forClientName:processName:"
+ "reportPermission:client:processName:forReporter:"
+ "setProcessName:"
+ "v44@0:8i16@20@28@36"
+ "visionOS,iOS|1"
+ "visionOS,iOS|10"
+ "visionOS,iOS|100"
+ "visionOS,iOS|1000"
+ "visionOS|1"
+ "visionOS|10"
+ "visionOS|100"
+ "|"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "@36@0:8i16@20@28"
- "ABSEApp"
- "ACMTest"
- "AccessibilityUIServer"
- "Client %@ allowlisted=%d\n"
- "LegacyEntitlement/%@"
- "MiniLauncher"
- "MissingPermissionABCIssue/%@/%d"
- "OysterTool"
- "clientName=%@"
- "clientName=%@,permission=%d"
- "com.apple.AMSEngagementViewService"
- "com.apple.Accessibility-Settings.extension"
- "com.apple.AppStore"
- "com.apple.AppleMediaServices.FollowUpExtension"
- "com.apple.AppleMediaServicesPurchasesTestsHost"
- "com.apple.AppleMediaServicesUITestsHost"
- "com.apple.BluetoothSettings"
- "com.apple.BluetoothSettingsApp"
- "com.apple.BluetoothUIServer"
- "com.apple.Bridge"
- "com.apple.CompanionViewService"
- "com.apple.CoreAuthUI"
- "com.apple.EraseAssistant"
- "com.apple.Fitness"
- "com.apple.HDSViewService"
- "com.apple.HeadphoneProxService"
- "com.apple.InCallService"
- "com.apple.LocalAuthenticationTests.xctrunner"
- "com.apple.ManagedClient"
- "com.apple.MesaStoreDemo"
- "com.apple.Mica-Player"
- "com.apple.MobileStore"
- "com.apple.MuseBuddy"
- "com.apple.Music"
- "com.apple.OysterDemo"
- "com.apple.Passbook"
- "com.apple.PreBoard"
- "com.apple.Preferences"
- "com.apple.RemoteiCloudQuotaUI"
- "com.apple.SetupAssistant"
- "com.apple.SharingViewService"
- "com.apple.SurfBoard"
- "com.apple.SymphonyMusic"
- "com.apple.TV"
- "com.apple.Touch-ID-Settings.extension"
- "com.apple.amsaccountsd"
- "com.apple.appstored"
- "com.apple.backboardd"
- "com.apple.bookassetd"
- "com.apple.companiond"
- "com.apple.coreauthd"
- "com.apple.corespeechd"
- "com.apple.coretelephony"
- "com.apple.family"
- "com.apple.iCloudQuota.ICQFollowup"
- "com.apple.iCloudQuotaUI.RemoteiCloudQuotaUI"
- "com.apple.icloud.FindMyDevice.FindMyDeviceHelperXPCService"
- "com.apple.icloud.findmydeviced"
- "com.apple.internal.applepayautomation.APAmacOSTests.xctrunner"
- "com.apple.internal.voyager.xctrunner"
- "com.apple.internal.xctestinternalangel"
- "com.apple.ios.StoreKitUIService"
- "com.apple.ist.ds.appleconnect2"
- "com.apple.ist.ds.appleconnect2.agent"
- "com.apple.itunesstored"
- "com.apple.managedconfiguration.profiled"
- "com.apple.migrationpluginwrapper"
- "com.apple.news"
- "com.apple.passd"
- "com.apple.paymentservices.testui"
- "com.apple.podcasts"
- "com.apple.presenced"
- "com.apple.purplebuddy"
- "com.apple.routined"
- "com.apple.sharingd"
- "com.apple.springboard"
- "com.apple.stocks"
- "com.apple.storekitd"
- "com.apple.supportapp"
- "com.apple.susuiservice"
- "com.apple.systempreferences"
- "com.apple.tv"
- "initWithClient:forReporter:"
- "initWithPermission:client:forReporter:"
- "keybagd"
- "legacyAllowlisted:"
- "reportClient:forReporter:"
- "reportLegacyClient:"
- "reportMissingPermission:forClientName:"
- "reportPermission:client:forReporter:"
- "ssetest"
- "v28@0:8i16@20"

```
