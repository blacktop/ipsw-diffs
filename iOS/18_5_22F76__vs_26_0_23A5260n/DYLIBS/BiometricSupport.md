## BiometricSupport

> `/System/Library/PrivateFrameworks/BiometricSupport.framework/BiometricSupport`

```diff

-511.100.15.0.0
-  __TEXT.__text: 0x55188
-  __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x254c
-  __TEXT.__const: 0x10e4
-  __TEXT.__cstring: 0x63f0
-  __TEXT.__oslogstring: 0x329b
-  __TEXT.__gcc_except_tab: 0x112c
-  __TEXT.__unwind_info: 0xfa8
-  __TEXT.__objc_classname: 0x2f9
-  __TEXT.__objc_methname: 0x608c
-  __TEXT.__objc_methtype: 0x14bf
-  __TEXT.__objc_stubs: 0x4ac0
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x1a30
-  __DATA_CONST.__objc_classlist: 0xc8
+544.0.0.0.0
+  __TEXT.__text: 0x5999c
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_methlist: 0x288c
+  __TEXT.__const: 0x1274
+  __TEXT.__cstring: 0x6767
+  __TEXT.__oslogstring: 0x3695
+  __TEXT.__gcc_except_tab: 0x1328
+  __TEXT.__unwind_info: 0x1058
+  __TEXT.__objc_classname: 0x33f
+  __TEXT.__objc_methname: 0x6c43
+  __TEXT.__objc_methtype: 0x1594
+  __TEXT.__objc_stubs: 0x4d60
+  __DATA_CONST.__got: 0x320
+  __DATA_CONST.__const: 0x1a38
+  __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1978
+  __DATA_CONST.__objc_selrefs: 0x1b50
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x7e8
-  __AUTH_CONST.__const: 0x150
-  __AUTH_CONST.__cfstring: 0x1ee0
-  __AUTH_CONST.__objc_const: 0x3840
-  __AUTH_CONST.__objc_intobj: 0xb10
+  __AUTH_CONST.__auth_got: 0x820
+  __AUTH_CONST.__const: 0x1b0
+  __AUTH_CONST.__cfstring: 0x1f60
+  __AUTH_CONST.__objc_const: 0x3e50
+  __AUTH_CONST.__objc_intobj: 0xb28
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x22c
-  __DATA.__data: 0xb08
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x284
+  __DATA.__data: 0xbb8
   __DATA.__common: 0x28
-  __DATA.__bss: 0x49
-  __DATA_DIRTY.__objc_data: 0x5f0
+  __DATA.__bss: 0x69
+  __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__common: 0x10
-  __DATA_DIRTY.__bss: 0x40
+  __DATA_DIRTY.__common: 0x30
+  __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2DACB950-6F21-34D2-B023-22DC7A3BE320
-  Functions: 1789
-  Symbols:   5587
-  CStrings:  2713
+  UUID: 403BBD0F-6967-3B4D-8C78-BAF6D8FE4D49
+  Functions: 1923
+  Symbols:   5972
+  CStrings:  2855
 
Symbols:
+ +[GraylistedClientABCIssue reportClient:withProcessName:clientUUID:platform:forReporter:]
+ +[LegacyEntitlementABCIssue reportClient:withProcessName:clientUUID:platform:forReporter:]
+ +[MissingPermissionABCIssue reportPermission:client:processName:clientUUID:platform:forReporter:]
+ +[WatchdogTimer watchdogWithName:]
+ +[WatchdogTimer watchdogWithName:timeout:]
+ -[BiometricKitCoreAnalyticsEvent postEventExtendedBy:]
+ -[BiometricKitCoreAnalyticsLockState .cxx_destruct]
+ -[BiometricKitCoreAnalyticsLockState biometryUnlockTotal]
+ -[BiometricKitCoreAnalyticsLockState initWithName:]
+ -[BiometricKitCoreAnalyticsLockState init]
+ -[BiometricKitCoreAnalyticsLockState isBiometryUnlockEnabledForUser:]
+ -[BiometricKitCoreAnalyticsLockState isBiometryUnlockEnabledForUser:].cold.1
+ -[BiometricKitCoreAnalyticsLockState isBiometryUnlockEnabledForUser:].cold.2
+ -[BiometricKitCoreAnalyticsLockState isPasscodeNeededForUser:]
+ -[BiometricKitCoreAnalyticsLockState lockStateUpdated:forUser:]
+ -[BiometricKitCoreAnalyticsLockState passcodeAuthenticatedBiometryAvailable]
+ -[BiometricKitCoreAnalyticsLockState passcodeAuthenticatedBiometryUnavailable]
+ -[BiometricKitCoreAnalyticsLockState passcodeAuthenticatedTotal]
+ -[BiometricKitCoreAnalyticsLockState passcodeNedded:]
+ -[BiometricKitCoreAnalyticsLockState passcodeUnlockBiometryAvailable]
+ -[BiometricKitCoreAnalyticsLockState passcodeUnlockBiometryDisabled]
+ -[BiometricKitCoreAnalyticsLockState passcodeUnlockBiometryUnavailable]
+ -[BiometricKitCoreAnalyticsLockState passcodeUnlockTotal]
+ -[BiometricKitCoreAnalyticsLockState passcodeValidatedBiometryAvailable]
+ -[BiometricKitCoreAnalyticsLockState passcodeValidatedBiometryUnavailable]
+ -[BiometricKitCoreAnalyticsLockState passcodeValidatedTotal]
+ -[BiometricKitCoreAnalyticsLockState postEvent]
+ -[BiometricKitCoreAnalyticsLockState remoteUnlockBiometryAvailable]
+ -[BiometricKitCoreAnalyticsLockState remoteUnlockBiometryDisabled]
+ -[BiometricKitCoreAnalyticsLockState remoteUnlockBiometryUnavailable]
+ -[BiometricKitCoreAnalyticsLockState remoteUnlockTotal]
+ -[BiometricKitCoreAnalyticsLockState reset]
+ -[BiometricKitCoreAnalyticsLockState serviceMatchWithServer:]
+ -[BiometricKitCoreAnalyticsLockState serviceMatchWithServer:].cold.1
+ -[BiometricKitCoreAnalyticsLockState setBiometryUnlockTotal:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeAuthenticatedBiometryAvailable:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeAuthenticatedBiometryUnavailable:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeAuthenticatedTotal:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeUnlockBiometryAvailable:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeUnlockBiometryDisabled:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeUnlockBiometryUnavailable:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeUnlockTotal:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeValidatedBiometryAvailable:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeValidatedBiometryUnavailable:]
+ -[BiometricKitCoreAnalyticsLockState setPasscodeValidatedTotal:]
+ -[BiometricKitCoreAnalyticsLockState setRemoteUnlockBiometryAvailable:]
+ -[BiometricKitCoreAnalyticsLockState setRemoteUnlockBiometryDisabled:]
+ -[BiometricKitCoreAnalyticsLockState setRemoteUnlockBiometryUnavailable:]
+ -[BiometricKitCoreAnalyticsLockState setRemoteUnlockTotal:]
+ -[BiometricKitCoreAnalyticsLockState setUnlockTotal:]
+ -[BiometricKitCoreAnalyticsLockState unlockTotal]
+ -[BiometricKitCoreAnalyticsLockState wasPasscodeNeededForUser:]
+ -[BiometricKitXPCExportedClientObject uuid]
+ -[BiometricKitXPCExportedObject clientThrottleRatio:].cold.1
+ -[BiometricKitXPCExportedObject currentPlatform]
+ -[BiometricKitXPCExportedObject prewarmCamera:client:replyBlock:]
+ -[BiometricKitXPCExportedObject prewarmCamera:client:replyBlock:].cold.1
+ -[BiometricKitXPCExportedObject prewarmCamera:client:replyBlock:].cold.2
+ -[BiometricKitXPCExportedObject prewarmCamera:client:replyBlock:].cold.3
+ -[BiometricKitXPCServer getSystemProtectedConfigurationWithClient:].cold.2
+ -[BiometricKitXPCServer prewarmCamera:withClient:]
+ -[EntitlementABCIssue clientUUID]
+ -[EntitlementABCIssue initWithClient:processName:clientUUID:platform:forReporter:]
+ -[EntitlementABCIssue platform]
+ -[EntitlementABCIssue setClientUUID:]
+ -[EntitlementABCIssue setPlatform:]
+ -[EntitlementABCIssueReporter reportGraylistedClient:withProcessName:clientUUID:platform:]
+ -[EntitlementABCIssueReporter reportLegacyClient:withProcessName:clientUUID:platform:]
+ -[EntitlementABCIssueReporter reportMissingPermission:forClientName:processName:clientUUID:platform:]
+ -[MissingPermissionABCIssue initWithPermission:client:processName:clientUUID:platform:forReporter:]
+ -[WatchdogTimer .cxx_destruct]
+ -[WatchdogTimer cancel]
+ -[WatchdogTimer dealloc]
+ -[WatchdogTimer initWithName:timeout:]
+ -[WatchdogTimer initWithName:timeout:].cold.1
+ -[WatchdogTimerItem .cxx_destruct]
+ -[WatchdogTimerItem endTime]
+ -[WatchdogTimerItem name]
+ -[WatchdogTimerItem setEndTime:]
+ -[WatchdogTimerItem setName:]
+ -[WatchdogTimerItem setStartTime:]
+ -[WatchdogTimerItem startTime]
+ GCC_except_table11
+ GCC_except_table13
+ GCC_except_table135
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table229
+ GCC_except_table304
+ GCC_except_table36
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table4
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table525
+ GCC_except_table528
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table57
+ GCC_except_table80
+ GCC_except_table82
+ GCC_except_table9
+ _OBJC_CLASS_$_BiometricKitCoreAnalyticsLockState
+ _OBJC_CLASS_$_WatchdogTimer
+ _OBJC_CLASS_$_WatchdogTimerItem
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._biometryUnlockTotal
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeAuthenticatedBiometryAvailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeAuthenticatedBiometryUnavailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeAuthenticatedTotal
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeUnlockBiometryAvailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeUnlockBiometryDisabled
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeUnlockBiometryUnavailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeUnlockTotal
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeValidatedBiometryAvailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeValidatedBiometryUnavailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._passcodeValidatedTotal
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._remoteUnlockBiometryAvailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._remoteUnlockBiometryDisabled
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._remoteUnlockBiometryUnavailable
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._remoteUnlockTotal
+ _OBJC_IVAR_$_BiometricKitCoreAnalyticsLockState._unlockTotal
+ _OBJC_IVAR_$_EntitlementABCIssue._clientUUID
+ _OBJC_IVAR_$_EntitlementABCIssue._platform
+ _OBJC_IVAR_$_WatchdogTimer._item
+ _OBJC_IVAR_$_WatchdogTimerItem._endTime
+ _OBJC_IVAR_$_WatchdogTimerItem._name
+ _OBJC_IVAR_$_WatchdogTimerItem._startTime
+ _OBJC_METACLASS_$_BiometricKitCoreAnalyticsLockState
+ _OBJC_METACLASS_$_WatchdogTimer
+ _OBJC_METACLASS_$_WatchdogTimerItem
+ __OBJC_$_CLASS_METHODS_WatchdogTimer
+ __OBJC_$_INSTANCE_METHODS_BiometricKitCoreAnalyticsLockState
+ __OBJC_$_INSTANCE_METHODS_WatchdogTimer
+ __OBJC_$_INSTANCE_METHODS_WatchdogTimerItem
+ __OBJC_$_INSTANCE_VARIABLES_BiometricKitCoreAnalyticsLockState
+ __OBJC_$_INSTANCE_VARIABLES_WatchdogTimer
+ __OBJC_$_INSTANCE_VARIABLES_WatchdogTimerItem
+ __OBJC_$_PROP_LIST_BiometricKitCoreAnalyticsLockState
+ __OBJC_$_PROP_LIST_WatchdogTimerItem
+ __OBJC_CLASS_RO_$_BiometricKitCoreAnalyticsLockState
+ __OBJC_CLASS_RO_$_WatchdogTimer
+ __OBJC_CLASS_RO_$_WatchdogTimerItem
+ __OBJC_METACLASS_RO_$_BiometricKitCoreAnalyticsLockState
+ __OBJC_METACLASS_RO_$_WatchdogTimer
+ __OBJC_METACLASS_RO_$_WatchdogTimerItem
+ ___38-[WatchdogTimer initWithName:timeout:]_block_invoke
+ ___38-[WatchdogTimer initWithName:timeout:]_block_invoke_2
+ ___53-[BiometricKitXPCExportedObject clientThrottleRatio:]_block_invoke
+ ___54-[BiometricKitCoreAnalyticsEvent postEventExtendedBy:]_block_invoke
+ ___60-[BiometricKitXPCServer listener:shouldAcceptNewConnection:]_block_invoke.606
+ ___61-[BiometricKitCoreAnalyticsLockState serviceMatchWithServer:]_block_invoke
+ ___61-[BiometricKitCoreAnalyticsLockState serviceMatchWithServer:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_76_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_84_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.169
+ ___block_literal_global.155
+ ___block_literal_global.171
+ ___block_literal_global.27
+ ___der_key_label
+ ___der_key_memento_expiry_bucket_0m_20m
+ ___der_key_memento_expiry_bucket_0m_2m
+ ___der_key_memento_expiry_bucket_10m_inf
+ ___der_key_memento_expiry_bucket_20m_60m
+ ___der_key_memento_expiry_bucket_24h_48h
+ ___der_key_memento_expiry_bucket_2m_4m
+ ___der_key_memento_expiry_bucket_48h_72h
+ ___der_key_memento_expiry_bucket_4m_6m
+ ___der_key_memento_expiry_bucket_60m_24h
+ ___der_key_memento_expiry_bucket_6m_8m
+ ___der_key_memento_expiry_bucket_72h_inf
+ ___der_key_memento_expiry_bucket_8m_10m
+ ___der_key_memento_expiry_counter
+ ___der_key_memento_expiry_state
+ ___der_key_primary_group_uuid
+ ___der_key_primary_user_uuid
+ ___der_key_sw_tag
+ ___der_key_timestamp
+ ___der_key_username
+ ___der_key_wkukey_kcv
+ __aks_backup_enable_volume
+ __aks_change_secret_epilogue
+ __aks_change_secret_epilogue.cold.1
+ __aks_recover_with_escrow_bag
+ __aks_recover_with_escrow_bag.cold.1
+ __aks_se_get_reset_token_for_memento_secret
+ __aks_set_configuration
+ __aks_set_system_with_passcode
+ __aks_set_system_with_passcode.cold.1
+ __aks_unlock_bag
+ __aks_unlock_bag.cold.1
+ __aks_unlock_with_sync_bag
+ __akslog_context
+ __currentLockStateForUser
+ __current_pid
+ __merge_dict_cb.cold.2
+ __previousLockStateForUser
+ __server
+ __unlockTokenForUser
+ __watchdogTimerItems
+ __watchdogTimerQueue
+ __watchdogTimerSource
+ _absoluteToNanoseconds
+ _aks_backup_enable_volume_with_acm
+ _aks_change_secret_epilogue_with_acm
+ _aks_change_secret_epilogue_with_opts
+ _aks_change_secret_with_kek
+ _aks_change_secret_with_kek.cold.1
+ _aks_create_bag_with_acm
+ _aks_create_escrow_bag_with_acm
+ _aks_create_sync_bag_with_acm
+ _aks_enable_cache_flow
+ _aks_enable_cache_flow.cold.1
+ _aks_get_icsc_srp
+ _aks_recover_with_escrow_bag_with_acm
+ _aks_reset_iteration_count
+ _aks_reset_iteration_count.cold.1
+ _aks_se_get_passcode_derivation
+ _aks_se_get_reset_token_for_memento_secret_with_acm
+ _aks_se_get_reset_token_for_memento_secret_with_opts
+ _aks_se_memento_secret_drop
+ _aks_se_memento_secret_drop.cold.1
+ _aks_se_recover_with_acm
+ _aks_se_recover_with_acm.cold.1
+ _aks_se_recover_with_opts
+ _aks_set_configuration_with_acm
+ _aks_set_configuration_with_opts
+ _aks_set_system_with_acm
+ _aks_set_system_with_opts
+ _aks_unlock_bag_with_acm
+ _aks_unlock_device_with_acm
+ _aks_unlock_device_with_acm.cold.1
+ _aks_unlock_device_with_opts
+ _aks_unlock_with_sync_bag_with_acm
+ _aks_verify_password_memento_with_acm
+ _aks_verify_password_with_acm
+ _aks_verify_password_with_opts
+ _ccder_sizeof_implicit_raw_octet_string
+ _clientThrottleRatio:.once
+ _copy_raw_secret
+ _decode_icsc_params_internal
+ _der_key_label
+ _der_key_memento_expiry_bucket_0m_20m
+ _der_key_memento_expiry_bucket_0m_2m
+ _der_key_memento_expiry_bucket_10m_inf
+ _der_key_memento_expiry_bucket_20m_60m
+ _der_key_memento_expiry_bucket_24h_48h
+ _der_key_memento_expiry_bucket_2m_4m
+ _der_key_memento_expiry_bucket_48h_72h
+ _der_key_memento_expiry_bucket_4m_6m
+ _der_key_memento_expiry_bucket_60m_24h
+ _der_key_memento_expiry_bucket_6m_8m
+ _der_key_memento_expiry_bucket_72h_inf
+ _der_key_memento_expiry_bucket_8m_10m
+ _der_key_memento_expiry_counter
+ _der_key_memento_expiry_state
+ _der_key_primary_group_uuid
+ _der_key_primary_user_uuid
+ _der_key_sw_tag
+ _der_key_timestamp
+ _der_key_username
+ _der_key_wkukey_kcv
+ _dispatch_suspend
+ _encode_icsc_params_internal
+ _get_akslog_context
+ _get_akslog_pid
+ _initWithName:timeout:.onceToken
+ _kBiometricKitCoreAnalyticsLockStateEventName
+ _mach_absolute_time
+ _nanosecondsToAbsolute
+ _objc_msgSend$_setError
+ _objc_msgSend$cancel
+ _objc_msgSend$clientUUID
+ _objc_msgSend$currentPlatform
+ _objc_msgSend$endTime
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithClient:processName:clientUUID:platform:forReporter:
+ _objc_msgSend$initWithName:timeout:
+ _objc_msgSend$initWithPermission:client:processName:clientUUID:platform:forReporter:
+ _objc_msgSend$isBiometryUnlockEnabledForUser:
+ _objc_msgSend$passcodeNedded:
+ _objc_msgSend$platform
+ _objc_msgSend$position
+ _objc_msgSend$postEventExtendedBy:
+ _objc_msgSend$prewarmCamera:withClient:
+ _objc_msgSend$reportClient:withProcessName:clientUUID:platform:forReporter:
+ _objc_msgSend$reportGraylistedClient:withProcessName:clientUUID:platform:
+ _objc_msgSend$reportLegacyClient:withProcessName:clientUUID:platform:
+ _objc_msgSend$reportMissingPermission:forClientName:processName:clientUUID:platform:
+ _objc_msgSend$reportPermission:client:processName:clientUUID:platform:forReporter:
+ _objc_msgSend$setClientUUID:
+ _objc_msgSend$setEndTime:
+ _objc_msgSend$setPlatform:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setStartTime:
+ _objc_msgSend$startTime
+ _objc_msgSend$watchdogWithName:
+ _objc_setProperty_nonatomic_copy
+ _ref_key_create_request_to_class
+ _se_derivation_request_deserialize
+ _se_derivation_request_serialization_len
+ _se_derivation_request_serialize
+ _set_akslog_context
+ _set_akslog_pid
+ _vsnprintf
- +[GraylistedClientABCIssue reportClient:withProcessName:forReporter:]
- +[LegacyEntitlementABCIssue reportClient:withProcessName:forReporter:]
- +[MissingPermissionABCIssue reportPermission:client:processName:forReporter:]
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.10
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.11
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.12
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.13
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.14
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.15
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.16
- -[BiometricKitXPCServer filterIdentities:withFilter:].cold.9
- -[BiometricKitXPCServer getBiometryAvailability:forUser:withClient:].cold.1
- -[BiometricKitXPCServer getCatacombSaveListForComponents:list:].cold.1
- -[BiometricKitXPCServer getIdentitiesDatabaseHashForUser:withClient:].cold.1
- -[BiometricKitXPCServer getIdentitiesDatabaseHashForUser:withClient:].cold.2
- -[BiometricKitXPCServer getIdentitiesDatabaseUUIDForUser:withClient:].cold.1
- -[BiometricKitXPCServer getIdentitiesDatabaseUUIDForUser:withClient:].cold.2
- -[EntitlementABCIssue initWithClient:processName:forReporter:]
- -[EntitlementABCIssueReporter reportGraylistedClient:withProcessName:]
- -[EntitlementABCIssueReporter reportLegacyClient:withProcessName:]
- -[EntitlementABCIssueReporter reportMissingPermission:forClientName:processName:]
- -[MissingPermissionABCIssue initWithPermission:client:processName:forReporter:]
- GCC_except_table130
- GCC_except_table152
- GCC_except_table155
- GCC_except_table221
- GCC_except_table299
- GCC_except_table31
- GCC_except_table32
- GCC_except_table33
- GCC_except_table42
- GCC_except_table44
- GCC_except_table46
- GCC_except_table48
- GCC_except_table50
- GCC_except_table52
- GCC_except_table533
- GCC_except_table536
- GCC_except_table54
- GCC_except_table77
- GCC_except_table79
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _OUTLINED_FUNCTION_75
- ___43-[BiometricKitCoreAnalyticsEvent postEvent]_block_invoke
- ___60-[BiometricKitXPCServer listener:shouldAcceptNewConnection:]_block_invoke.603
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_68_e8_32s40s48bs56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48bs56r_e5_v8?0ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_76_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.171
- ___block_literal_global.157
- ___block_literal_global.173
- _aks_change_secret_epilogue.cold.1
- _aks_change_secret_opts.cold.1
- _aks_recover_with_escrow_bag.cold.1
- _aks_set_system_with_passcode.cold.1
- _aks_unlock_bag.cold.1
- _der_key_validate
- _der_key_validate.cold.1
- _der_key_validate.cold.2
- _get_aks_log_pid
- _objc_msgSend$initWithClient:processName:forReporter:
- _objc_msgSend$initWithPermission:client:processName:forReporter:
- _objc_msgSend$reportClient:withProcessName:forReporter:
- _objc_msgSend$reportGraylistedClient:withProcessName:
- _objc_msgSend$reportLegacyClient:withProcessName:
- _objc_msgSend$reportMissingPermission:forClientName:processName:
- _objc_msgSend$reportPermission:client:processName:forReporter:
CStrings:
+ "%@: client=<%p>, status=%d, priority=%ld"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s Unwrapped DER backup bag%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n"
+ "-[BiometricKitXPCExportedObject prewarmCamera:client:replyBlock:]"
+ "-[BiometricKitXPCExportedObject terminate]"
+ "/Library/Caches/com.apple.xbs/Sources/BiometricSupport/BiometricSupport/Analytics/BiometricKitCoreAnalyticsLockState.m"
+ "@\"WatchdogTimerItem\""
+ "@24@0:8r*16"
+ "@28@0:8r*16I24"
+ "@56@0:8@16@24@32@40@48"
+ "@60@0:8i16@20@28@36@44@52"
+ "B20@0:8I16"
+ "BKClientUUID"
+ "BiometricKitCoreAnalyticsEvent(%@) postEventExtendedBy: %@\n"
+ "BiometricKitCoreAnalyticsLockState"
+ "BiometricKitCoreAnalyticsLockState lockStateUpdated forUser: %u currentLockState: %u previousLockState: %u\n"
+ "BiometricKitCoreAnalyticsLockState lockStateUpdated result: %u\n"
+ "BiometricKitXPCServer::init\n"
+ "BiometricKitXPCServer::init -> %@\n"
+ "C24@0:8I16I20"
+ "Client %@[uuid=%@] with PID %d does have legacy entitlement com.apple.private.bmk.allow, please set one of fine grained entitlements com.apple.private.biometrickit.allow-*\n"
+ "GraylistedClient/%@/%@/%@"
+ "LegacyEntitlement/%@/%@/%@"
+ "MissingPermissionABCIssue/%@/%@/%@/%d"
+ "T@\"NSNumber\",&,N,V_biometryUnlockTotal"
+ "T@\"NSNumber\",&,N,V_passcodeAuthenticatedBiometryAvailable"
+ "T@\"NSNumber\",&,N,V_passcodeAuthenticatedBiometryUnavailable"
+ "T@\"NSNumber\",&,N,V_passcodeAuthenticatedTotal"
+ "T@\"NSNumber\",&,N,V_passcodeUnlockBiometryAvailable"
+ "T@\"NSNumber\",&,N,V_passcodeUnlockBiometryDisabled"
+ "T@\"NSNumber\",&,N,V_passcodeUnlockBiometryUnavailable"
+ "T@\"NSNumber\",&,N,V_passcodeUnlockTotal"
+ "T@\"NSNumber\",&,N,V_passcodeValidatedBiometryAvailable"
+ "T@\"NSNumber\",&,N,V_passcodeValidatedBiometryUnavailable"
+ "T@\"NSNumber\",&,N,V_passcodeValidatedTotal"
+ "T@\"NSNumber\",&,N,V_remoteUnlockBiometryAvailable"
+ "T@\"NSNumber\",&,N,V_remoteUnlockBiometryDisabled"
+ "T@\"NSNumber\",&,N,V_remoteUnlockBiometryUnavailable"
+ "T@\"NSNumber\",&,N,V_remoteUnlockTotal"
+ "T@\"NSNumber\",&,N,V_unlockTotal"
+ "T@\"NSString\",&,N,V_clientUUID"
+ "T@\"NSString\",&,N,V_platform"
+ "T@\"NSString\",C,N,V_name"
+ "TQ,N,V_endTime"
+ "TQ,N,V_startTime"
+ "Watchdog timer fired for '%@' after %f seconds"
+ "WatchdogTimer"
+ "WatchdogTimerItem"
+ "[_server performGetSKSLockStateCommand:identity.userID outState:&lockStateForUser] == 0 "
+ "__PasscodeChangedNotificationCallback(observer:%p)\n"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "_biometryUnlockTotal"
+ "_clientUUID"
+ "_endTime"
+ "_item"
+ "_name"
+ "_passcodeAuthenticatedBiometryAvailable"
+ "_passcodeAuthenticatedBiometryUnavailable"
+ "_passcodeAuthenticatedTotal"
+ "_passcodeUnlockBiometryAvailable"
+ "_passcodeUnlockBiometryDisabled"
+ "_passcodeUnlockBiometryUnavailable"
+ "_passcodeUnlockTotal"
+ "_passcodeValidatedBiometryAvailable"
+ "_passcodeValidatedBiometryUnavailable"
+ "_passcodeValidatedTotal"
+ "_platform"
+ "_remoteUnlockBiometryAvailable"
+ "_remoteUnlockBiometryDisabled"
+ "_remoteUnlockBiometryUnavailable"
+ "_remoteUnlockTotal"
+ "_setError"
+ "_startTime"
+ "_unlockTotal"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
+ "archiveCatacombDataForComponent:toArchiver: -> err:0x%x\n"
+ "biometryUnlockTotal"
+ "cacheAccessories -> err:0x%x\n"
+ "cacheCatacombInfo -> err:0x%x\n"
+ "cacheUserAccountsInfo: currentAccountUserID:%d, hasMultipleUserAccounts:%d, valid:%u\n"
+ "cancel"
+ "cancelWithClient -> err:0x%x\n"
+ "checkCatacombForUser: %u\n"
+ "checkCatacombForUser: -> err:0x%x\n"
+ "checkTemplatesValidityForUser: %u\n"
+ "checkTemplatesValidityForUser: -> err:0x%x\n"
+ "clearTemplateListForUser: %u\n"
+ "clientName=%@,processName=%@,clientUUID=%@,platform=%@,permission=%d,v=3"
+ "clientName=%@,processName=%@,clientUUID=%@,platform=%@,v=3"
+ "clientUUID"
+ "com.apple.biometrickit.lockStateAnalytics"
+ "com.apple.biometrickitd.watchdogQueue"
+ "currentPlatform"
+ "detectPresenceWithOptions:withClient: %@, %@\n"
+ "detectPresenceWithOptions:withClient: -> err:0x%x\n"
+ "didDisplayPearlGlassesBannerNotificationRecently: %f\n"
+ "didDisplayPearlGlassesBannerNotificationRecently: -> %d\n"
+ "disconnectingClient: %@\n"
+ "displayPearlInterlockIssueNotification: %d\n"
+ "displayPearlInterlockIssueNotification: -> %d\n"
+ "displayStateChanged: -> err:0x%x\n"
+ "doSharedMemoryTransfers -> err:0x%x\n"
+ "dropUnlockTokenWithClient: %@ -> err:0x%x\n"
+ "endTime"
+ "enroll:forUser:withOptions:withClient: %d, %u, %@, %@\n"
+ "enroll:forUser:withOptions:withClient: -> err:0x%x\n"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "filterIdentities:withFilter: %@, %@\n"
+ "filterIdentities:withFilter: -> err:0x%x, filteredIdentities:%@\n"
+ "forceBioLockoutForUser:withOptions:withClient: %u, %@, %@ -> err:0x%x\n"
+ "forceBioLockoutForUser:withOptions:withClient: %u, %p, %@\n"
+ "getBioLockoutState:forUser:withClient: %p, %u, %@\n"
+ "getBioLockoutState:forUser:withClient: -, %u, %@ -> err:0x%x, state:%u\n"
+ "getBiometryAvailability:forUser:withClient: %p, %u, %@\n"
+ "getBiometryAvailability:forUser:withClient: -, %u, %@ -> err:0x%x, availability:%ld\n"
+ "getBytes:range:"
+ "getCatacombSaveListForComponents:list: -> err:0x%x (list:%@)\n"
+ "getDeviceHardwareState:withClient: %p, %@\n"
+ "getDeviceHardwareState:withClient: -> err:0x%x, state:%d\n"
+ "getExpressModeState:forUser:withClient: %p, %u, %@\n"
+ "getExpressModeState:forUser:withClient: -> err:0x%x, state:%ld\n"
+ "getFreeIdentityCount:forUser:accessoryGroup:client: %p, %u, %@, %@\n"
+ "getFreeIdentityCount:forUser:accessoryGroup:client: -> err:0x%x, count:%ld\n"
+ "getFreeIdentityCount:forUser:withClient: %d, %u, %@\n"
+ "getFreeIdentityCount:forUser:withClient: %d, %u, %@ -> %u\n"
+ "getIdentitiesDatabaseHashForUser:withClient: %u, %@\n"
+ "getIdentitiesDatabaseHashForUser:withClient: %u, %@ -> %@ (err:0x%x)\n"
+ "getIdentitiesDatabaseUUIDForUser:withClient: %u, %@\n"
+ "getIdentitiesDatabaseUUIDForUser:withClient: %u, %@ -> %@ (err:0x%x)\n"
+ "getIdentityFromUUID:withClient: %p(%@), %@\n"
+ "getIdentityFromUUID:withClient: -, %@ -> %{public}@\n"
+ "getIdentityObject: -> %@\n"
+ "getIdentityObjectByUserID:UUID: %u, %@\n"
+ "getLastMatchEvent:withClient: %@ -> err:0x%x, event:%@\n"
+ "getLastMatchEvent:withClient: %p, %@\n"
+ "getMaxIdentityCount:withClient: %d, %@\n"
+ "getMaxIdentityCount:withClient: %d, %@ -> %u\n"
+ "getPreferencesValue:forKey: %p, %@\n"
+ "getPreferencesValue:forKey: -> err:0x%x, {%@: %@}\n"
+ "getProtectedConfigurationForUser:withClient: %u, %@\n"
+ "getProtectedConfigurationForUser:withClient: %u, %@ -> %@ (err:0x%x)\n"
+ "getSystemProtectedConfigurationWithClient: %@ -> %@ (err:0x%x)\n"
+ "getUserKeybagUUIDForUID: %u\n"
+ "getUserUUIDForUID:userUUID: %u, %p\n"
+ "getUserUUIDForUID:userUUID: -, %u -> err:0x%x, userUUID:%@\n"
+ "getUserUUIDsForUIDs:userUUIDs: %@, - -> err:0x%x, userUUIDs:%@\n"
+ "getUserUUIDsForUIDs:userUUIDs: %p(%@), %p\n"
+ "handleCatacombUnlock -> err:0x%x\n"
+ "handleFirstUnlock -> err:0x%x\n"
+ "hasError"
+ "i32@0:8Q16@24"
+ "identities:withClient: %p(%@), %@\n"
+ "identities:withClient: -, %@ -> %@\n"
+ "identitiesOfUser: %u\n"
+ "initWithClient:processName:clientUUID:platform:forReporter:"
+ "initWithName:timeout:"
+ "initWithPermission:client:processName:clientUUID:platform:forReporter:"
+ "isBiometryUnlockEnabledForUser:"
+ "isPasscodeNeededForUser:"
+ "isValidUser: %u\n"
+ "isValidUser: -> err:0x%x\n"
+ "isXARTAvailableWithClient: %@ -> %d (err:0x%x)\n"
+ "listAccessories:client: %p, %@\n"
+ "listAccessories:client: -> err:0x%x, accessories:%@\n"
+ "listener:shouldAcceptNewConnection: %p(%@), %p(%@)\n"
+ "loadCatacomb -> err:0x%x\n"
+ "loadCatacombAfterFirstUnlock\n"
+ "loadCatacombAfterFirstUnlock -> err:0x%x\n"
+ "loadCatacombForComponent: -> err:0x%x\n"
+ "loadCatacombForUser: -> err:0x%x\n"
+ "lockStateUpdated:forUser:"
+ "logCatacombHashForUser: %u -> %02x%02x*** (length:%lu)\n"
+ "logCatacombHashForUser: %u -> %@\n"
+ "logCatacombUUIDForUser: %u -> %02X%02X***\n"
+ "logCatacombUUIDForUser: %u -> %@\n"
+ "match:withOptions:withClient: %@, %@, %@\n"
+ "match:withOptions:withClient: -> err:0x%x\n"
+ "notifyAppIsInactive:withClient: %d, %@ -> void\n"
+ "osStateHandler: -> %p\n"
+ "osStateHandler: hints(osh_version:%d, osh_requestor:'%s', osh_api:%d, osh_reason:%d)\n"
+ "parseAuthDict:toAuthData: %@, %p\n"
+ "parseAuthDict:toAuthData: -> err:0x%x\n"
+ "passcodeAuthenticatedBiometryAvailable"
+ "passcodeAuthenticatedBiometryUnavailable"
+ "passcodeAuthenticatedTotal"
+ "passcodeNedded:"
+ "passcodeUnlockBiometryAvailable"
+ "passcodeUnlockBiometryDisabled"
+ "passcodeUnlockBiometryUnavailable"
+ "passcodeUnlockTotal"
+ "passcodeValidatedBiometryAvailable"
+ "passcodeValidatedBiometryUnavailable"
+ "passcodeValidatedTotal"
+ "pauseBioOperation: -> err:0x%x\n"
+ "platform"
+ "position"
+ "postEventExtendedBy:"
+ "prewarmCamera:client:replyBlock:"
+ "prewarmCamera:withClient:"
+ "processBioOperation: -> err:0x%x\n"
+ "readCatacombState -> 0x%x\n"
+ "registerDelegate:withClient: %d, %@ -> void\n"
+ "remoteUnlockBiometryAvailable"
+ "remoteUnlockBiometryDisabled"
+ "remoteUnlockBiometryUnavailable"
+ "remoteUnlockTotal"
+ "removeAllIdentitiesForUser:withOptions:withClient: %u, %p, %@\n"
+ "removeAllIdentitiesForUser:withOptions:withClient: -> err:0x%x\n"
+ "removeIdentity:withOptions:withClient: %{public}@, %p, %@\n"
+ "removeIdentity:withOptions:withClient: -> err:0x%x\n"
+ "removeUser: %u\n"
+ "removeUser: -> err:0x%x\n"
+ "reportClient:withProcessName:clientUUID:platform:forReporter:"
+ "reportGraylistedClient:withProcessName:clientUUID:platform:"
+ "reportLegacyClient:withProcessName:clientUUID:platform:"
+ "reportMissingPermission:forClientName:processName:clientUUID:platform:"
+ "reportPermission:client:processName:clientUUID:platform:forReporter:"
+ "rescheduleTimerMain\n"
+ "rescheduleTimerMain -> void\n"
+ "rescheduleTimerMain: examining issue %@ nextAction=%@\n"
+ "restoreAndSyncTemplates -> err:0x%x\n"
+ "resumeQueuedBioOperation -> void\n"
+ "saveCatacombForComponents: %{public}@\n"
+ "saveCatacombForComponents: -> err:0x%x\n"
+ "saveCatacombForIdentity: -> err:0x%x\n"
+ "saveCatacombIfDirtyWithInterval:andDelay: %f, %f\n"
+ "saveCatacombIfDirtyWithInterval:andDelay: -> err:0x%x\n"
+ "saveTemplateListAfterTemplateUpdate -> err:0x%x\n"
+ "server != ((void*)0)"
+ "serviceMatchWithServer:"
+ "serviceStatus:type:inValue: %u, 0x%x, 0x%x\n"
+ "serviceStatus:type:inValue: MCDMExtractMessageData: %u, %llu, %u, %p, %zu, %@, %llu(0x%llx), %llu\n"
+ "serviceStatus:version:ordinal:data:timestamp: 0x%x, 0x%x, 0x%llx, %@, %llu\n"
+ "setBiometryUnlockTotal:"
+ "setClientUUID:"
+ "setEndTime:"
+ "setPasscodeAuthenticatedBiometryAvailable:"
+ "setPasscodeAuthenticatedBiometryUnavailable:"
+ "setPasscodeAuthenticatedTotal:"
+ "setPasscodeUnlockBiometryAvailable:"
+ "setPasscodeUnlockBiometryDisabled:"
+ "setPasscodeUnlockBiometryUnavailable:"
+ "setPasscodeUnlockTotal:"
+ "setPasscodeValidatedBiometryAvailable:"
+ "setPasscodeValidatedBiometryUnavailable:"
+ "setPasscodeValidatedTotal:"
+ "setPlatform:"
+ "setPosition:"
+ "setPreferencesValue:forKey: -> %d, {%@: %@}\n"
+ "setPreferencesValue:forKey: {%@: %@}\n"
+ "setProtectedConfiguration:forUser:withOptions:withClient: %@, %u, %p, %@\n"
+ "setProtectedConfiguration:forUser:withOptions:withClient: %@, %u, %p, %@ -> err:0x%x\n"
+ "setRemoteUnlockBiometryAvailable:"
+ "setRemoteUnlockBiometryDisabled:"
+ "setRemoteUnlockBiometryUnavailable:"
+ "setRemoteUnlockTotal:"
+ "setStartTime:"
+ "setSystemProtectedConfiguration:withOptions:withClient: %@, %p, %@\n"
+ "setSystemProtectedConfiguration:withOptions:withClient: %@, %p, %@ -> err:0x%x\n"
+ "setUnlockTotal:"
+ "singleEnrolledUser\n"
+ "singleEnrolledUser -> %u\n"
+ "startBioOperation: -> err:0x%x\n"
+ "startEnrollOperation: -> err:0x%x\n"
+ "startMatchOperation: -> err:0x%x\n"
+ "startPresenceDetectOperation: -> err:0x%x\n"
+ "startTime"
+ "suspendAllConnections: %d (_suspended:%d)\n"
+ "suspendAllConnections: -> void (_suspended:%d)\n"
+ "syncTemplateListForUser: %u\n"
+ "syncTemplateListForUser: -> err:0x%x\n"
+ "unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities: -> err:0x%x\n"
+ "unlockTotal"
+ "updateActiveOperationNotificationWithOverride: BKActiveOperationNotification: %d\n"
+ "updateExpressModeStateNotification (_expressModeState: %ld)\n"
+ "updateIdentity:withOptions:withClient: %{public}@, %p, %@\n"
+ "updateIdentity:withOptions:withClient: -> err:0x%x\n"
+ "updatePropertiesOfIdentities -> err:0x%x\n"
+ "v40@0:8Q16Q24@?32"
+ "v40@0:8Q16Q24@?<v@?i>32"
+ "v48@0:8@16@24@32@40"
+ "v52@0:8i16@20@28@36@44"
+ "v56@0:8@16@24@32@40@48"
+ "v60@0:8i16@20@28@36@44@52"
+ "wasPasscodeNeededForUser:"
+ "watchdogWithName:"
+ "watchdogWithName:timeout:"
- "%@: client=<%p>, status=%u, priority=%ld"
- "%s%s:%s%s%s%s%u:%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s %sdump %s (len = %zd)%s%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to load in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag with prederived secret: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unlock in-kernel backup bag: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Failed to unwrap backup bag as DER: 0x%08x%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s Unwrapped DER backup bag%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 1%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s bad 2%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s fail%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s ioreg: %d, boot_arg: %d%s\n"
- "%s%s:%s%s%s%s%u:%s%u:%s overflow%s\n"
- "@44@0:8i16@20@28@36"
- "BiometricKitCoreAnalyticsEvent(%@) postEvent\n"
- "BiometricKitXPCServer init: -> %p\n"
- "Client %@ with PID %d does have legacy entitlement com.apple.private.bmk.allow, please set one of fine grained entitlements com.apple.private.biometrickit.allow-*\n"
- "__PasscodeChangedNotificationCallback %p %p %@ %p %@\n"
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"
- "archiveCatacombDataForComponent:toArchiver: -> %d\n"
- "cacheAccessories -> %d\n"
- "cacheCatacombInfo -> %d\n"
- "cacheUserAccountsInfo: currentAccountUserID = %d, hasMultipleUserAccounts = %u, valid = %u\n"
- "cancelWithClient: -> %d\n"
- "checkCatacombForUser: %d\n"
- "checkCatacombForUser: -> %d\n"
- "checkTemplatesValidityForUser: %d\n"
- "checkTemplatesValidityForUser: -> %d\n"
- "clearTemplateListForUser: %d\n"
- "clientName=%@,processName=%@,permission=%d,v=2"
- "clientName=%@,processName=%@,v=2"
- "der_key_validate"
- "detectPresenceWithOptions:withClient: %@ %@\n"
- "detectPresenceWithOptions:withClient: -> %d\n"
- "didDisplayPearlGlassesBannerNotificationRecently -> %d\n"
- "didDisplayPearlGlassesBannerNotificationRecently:%f\n"
- "disconnecting client: %@\n"
- "displayStateChanged: -> %d\n"
- "doSharedMemoryTransfers -> %{errno}d\n"
- "dropUnlockTokenWithClient: -> %d\n"
- "enroll:forUser:withOptions:withClient: %d %d %@ %@\n"
- "enroll:forUser:withOptions:withClient: -> %d\n"
- "failed to open connection to %s\n"
- "false"
- "filterIdentities:withFilter: %@ %@\n"
- "filterIdentities:withFilter: -> %d (%@)\n"
- "forceBioLockoutForUser:withClient: -> %d\n"
- "forceBioLockoutForUser:withOptions:withClient: %d %p %@\n"
- "getBioLockoutState:forUser:withClient: %d %@\n"
- "getBioLockoutState:forUser:withClient: -> %ld (%d)\n"
- "getBiometryAvailability: -> %ld (%d)\n"
- "getBiometryAvailability:forUser:withClient: %p %d %@\n"
- "getCatacombSaveListForComponents:list: -> %d (list = %@)\n"
- "getDeviceHardwareState:withClient: %p %@\n"
- "getDeviceHardwareState:withClient: -> %d %d\n"
- "getExpressModeState:forUser:withClient: %d %@\n"
- "getExpressModeState:forUser:withClient: -> %ld (%d)\n"
- "getFreeIdentityCount:forUser:accessoryGroup:client: %p %u %@ %@\n"
- "getFreeIdentityCount:forUser:accessoryGroup:client: -> %lu %d\n"
- "getFreeIdentityCount:forUser:withClient: %d %d %@\n"
- "getFreeIdentityCount:forUser:withClient: -> %u\n"
- "getIdentitiesDatabaseHashForUser:withClient: %d %@\n"
- "getIdentitiesDatabaseHashForUser:withClient: -> %@ (%d)\n"
- "getIdentitiesDatabaseUUIDForUser:withClient: %d %@\n"
- "getIdentitiesDatabaseUUIDForUser:withClient: -> %@ (%d)\n"
- "getIdentityFromUUID:withClient: %p(%@) %@\n"
- "getIdentityFromUUID:withClient: -> %{public}@\n"
- "getIdentityObject: -> %p(%@)\n"
- "getIdentityObjectByUserID:UUID: %d %@\n"
- "getLastMatchEvent:withClient: %p %@\n"
- "getLastMatchEvent:withClient: -> %@ %d\n"
- "getMaxIdentityCount:withClient: %d %@\n"
- "getMaxIdentityCount:withClient: -> %u\n"
- "getPreferencesValue:%@ forKey:%@ -> %d\n"
- "getPreferencesValue:%p forKey:%@\n"
- "getProtectedConfigurationForUser:withClient: %d %@\n"
- "getProtectedConfigurationForUser:withClient: -> %@ (%d)\n"
- "getSystemProtectedConfigurationWithClient: -> %@ (%d)\n"
- "getUserKeybagUUIDForUID: %d\n"
- "getUserUUIDForUID(%d): -> %d, userUUID = %@\n"
- "getUserUUIDForUID: %d\n"
- "getUserUUIDsForUIDs(%@): -> %d, userUUIDs = %@\n"
- "getUserUUIDsForUIDs: %p(%@)\n"
- "handleCatacombUnlock: -> %d\n"
- "handleFirstUnlock: -> %d\n"
- "identities:withClient: %p(%@) %@\n"
- "identities:withClient: -> %@\n"
- "identitiesOfUser: %d\n"
- "init\n"
- "initWithClient:processName:forReporter:"
- "initWithPermission:client:processName:forReporter:"
- "isValidUser\n"
- "isValidUser -> %d\n"
- "listAccessories:client: %p %@\n"
- "listAccessories:client: -> %@ %d\n"
- "listener:shouldAcceptNewConnection: %p(%@) %p(%@)\n"
- "loadCatacomb -> %d\n"
- "loadCatacombAfterFirstUnlock: -> %d\n"
- "loadCatacombForComponent: -> %d\n"
- "loadCatacombForUser: -> %d\n"
- "logCatacombHashForUser:%u -> %02x%02x*** (len=%lu)\n"
- "logCatacombHashForUser:%u -> %@\n"
- "logCatacombUUIDForUser:%u -> %02X%02X***\n"
- "logCatacombUUIDForUser:%u -> %@\n"
- "match:withOptions:withClient: %@ %@ %@\n"
- "match:withOptions:withClient: -> %d\n"
- "notifyAppIsInactive:withClient: %d %@ -> void\n"
- "osStateHandler -> %p\n"
- "osStateHandler <- hints(osh_version:%d, osh_requestor:'%s', osh_api:%d, osh_reason:%d)\n"
- "parseAuthDict:toAuthData: %@ %p\n"
- "parseAuthDict:toAuthData: -> %d\n"
- "pauseBioOperation: -> %d\n"
- "postPearlInterlockFollowUpItem\n"
- "postPearlInterlockFollowUpItem -> %d\n"
- "processBioOperation:withPriority:withParams:withClient: -> %d\n"
- "readCatacombState -> %d\n"
- "registerDelegate:withClient: %d %@ -> void\n"
- "removeAllIdentitiesForUser:withOptions:withClient: %d %p %@\n"
- "removeAllIdentitiesForUser:withOptions:withClient: -> %d\n"
- "removeIdentity:withOptions:withClient: %p(%{public}@) %p %@\n"
- "removeIdentity:withOptions:withClient: -> %d\n"
- "removeUser: %d\n"
- "removeUser: -> %d\n"
- "reportClient:withProcessName:forReporter:"
- "reportGraylistedClient:withProcessName:"
- "reportLegacyClient:withProcessName:"
- "reportMissingPermission:forClientName:processName:"
- "reportPermission:client:processName:forReporter:"
- "rescheduleTimer\n"
- "rescheduleTimer ->\n"
- "rescheduleTimer: examining issue %@ nextAction=%@\n"
- "restoreAndSyncTemplates -> %d\n"
- "resumeQueuedBioOperation: -> void\n"
- "saveCatacombForComponents -> %d\n"
- "saveCatacombForComponents: %p(%{public}@)\n"
- "saveCatacombForIdentity: -> %d\n"
- "saveCatacombIfDirtyWithInterval:andDelay: %f %f\n"
- "saveCatacombIfDirtyWithInterval:andDelay: -> %d\n"
- "saveTemplateListAfterTemplateUpdate -> %d\n"
- "serviceStatus:type:inValue: %u 0x%x %u(0x%x)\n"
- "serviceStatus:type:inValue: MCDMExtractMessageData %u %llu %u %p %zu %@ %llu(0x%llx) %llu\n"
- "serviceStatus:version:ordinal:data:timestamp: 0x%x 0x%x 0x%llx %@ %llu\n"
- "setPreferencesValue:%@ forKey:%@\n"
- "setPreferencesValue:%@ forKey:%@ -> %@\n"
- "setProtectedConfiguration:forUser:withOptions:withClient: %@ %d %p %@\n"
- "setProtectedConfiguration:forUser:withOptions:withClient: -> %d\n"
- "setSystemProtectedConfiguration:withOptions:withClient: %@ %p %@\n"
- "setSystemProtectedConfiguration:withOptions:withClient: -> %d\n"
- "singleEnrolledUser: -> %d\n"
- "startBioOperation: -> %d\n"
- "startEnrollOperation: -> %d\n"
- "startMatchOperation: -> %d\n"
- "startPresenceDetectOperation: -> %d\n"
- "suspendAllConnections: %u (suspended:%u)\n"
- "suspendAllConnections: -> void (suspended:%u)\n"
- "syncTemplateListForUser: %d\n"
- "syncTemplateListForUser: -> %d\n"
- "true"
- "unarchiveCatacombDataForComponent:fromUnarchiver:secureData:identities: -> %d\n"
- "updateActiveOperationNotificationWithOverride: posted value = %d\n"
- "updateExpressModeStateNotification %ld\n"
- "updateIdentity:withOptions:withClient: %p(%{public}@) %p %@\n"
- "updateIdentity:withOptions:withClient: -> %d\n"
- "updatePropertiesOfIdentities: -> void\n"
- "v36@0:8i16@20@28"
- "v44@0:8i16@20@28@36"

```
