## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-386.458.1.0.0
-  __TEXT.__text: 0x50a10
-  __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_methlist: 0x3954
-  __TEXT.__const: 0x1164
-  __TEXT.__gcc_except_tab: 0x122c
-  __TEXT.__oslogstring: 0x8ac0
-  __TEXT.__cstring: 0x5c64
+404.0.0.0.0
+  __TEXT.__text: 0x533f4
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_methlist: 0x3a54
+  __TEXT.__const: 0x12e4
+  __TEXT.__gcc_except_tab: 0x129c
+  __TEXT.__oslogstring: 0x8e89
+  __TEXT.__cstring: 0x5f63
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x14b8
-  __TEXT.__objc_classname: 0x705
-  __TEXT.__objc_methname: 0x9005
-  __TEXT.__objc_methtype: 0x1c55
-  __TEXT.__objc_stubs: 0x4ee0
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x2e50
-  __DATA_CONST.__objc_classlist: 0x1a0
+  __TEXT.__unwind_info: 0x1560
+  __TEXT.__objc_classname: 0x71f
+  __TEXT.__objc_methname: 0x9229
+  __TEXT.__objc_methtype: 0x1c86
+  __TEXT.__objc_stubs: 0x4fe0
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x2ef8
+  __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x20d0
+  __DATA_CONST.__objc_selrefs: 0x2158
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x850
-  __AUTH_CONST.__const: 0x550
-  __AUTH_CONST.__cfstring: 0x3c40
-  __AUTH_CONST.__objc_const: 0x8958
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__cfstring: 0x3e00
+  __AUTH_CONST.__objc_const: 0x8ab0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2fc
-  __DATA.__data: 0x1050
-  __DATA.__bss: 0x129
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0x1100
+  __DATA.__bss: 0x101
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x9b0
+  __DATA_DIRTY.__objc_data: 0x870
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0x118
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F97253CC-69B7-3F3C-91BA-82BC13D441E3
-  Functions: 2207
-  Symbols:   7430
-  CStrings:  3738
+  UUID: C685877E-1466-3D2E-B654-D9304EE4F483
+  Functions: 2306
+  Symbols:   7671
+  CStrings:  3819
 
Symbols:
+ +[CDPPrivacySensitiveObject sensitiveObjectWrappingObject:]
+ +[CDPUtilities isADPInBuddyEnabled]
+ +[CDPUtilities isADPInBuddyEnabled].cold.1
+ +[CDPUtilities isNaturalUIEnabled]
+ +[CDPUtilities isNaturalUIEnabled].cold.1
+ +[CDPUtilities isSEPBasedICSCHealingEnabled]
+ +[CDPUtilities isSEPBasedICSCHealingEnabled].cold.1
+ +[CDPUtilities isSolariumEnabled]
+ +[CDPUtilities isSolariumEnabled].cold.1
+ +[CDPUtilities sosCompatibilityEnabled]
+ +[CDPUtilities sosCompatibilityEnabled].cold.1
+ -[CDPCircleProxyImpl requestToJoinCircle:].cold.2
+ -[CDPCircleProxyImpl requestToJoinCircle:].cold.3
+ -[CDPCircleProxyImpl requestToJoinCircle:].cold.4
+ -[CDPCircleProxyImpl requestToJoinCircle:].cold.5
+ -[CDPCircleProxyImpl requestToJoinCircle:].cold.6
+ -[CDPPrivacySensitiveObject .cxx_destruct]
+ -[CDPPrivacySensitiveObject description]
+ -[CDPPrivacySensitiveObject initWithObject:]
+ -[CDPPrivacySensitiveObject wrappedObject]
+ -[CDPSOSCircleProxyImpl viewMemberForAllUserFacingViews:]
+ -[CDPSOSCircleProxyImpl viewMemberForCreditCards:]
+ -[CDPSOSCircleProxyImpl viewMemberForOtherSyncable:]
+ -[CDPSOSCircleProxyImpl viewMemberForWiFi:]
+ -[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]
+ -[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]
+ GCC_except_table108
+ GCC_except_table121
+ GCC_except_table123
+ GCC_except_table126
+ GCC_except_table129
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table41
+ _AKDidAccountRecovery
+ _OBJC_CLASS_$_CDPPrivacySensitiveObject
+ _OBJC_IVAR_$_CDPPrivacySensitiveObject._wrappedObject
+ _OBJC_METACLASS_$_CDPPrivacySensitiveObject
+ __OBJC_$_CLASS_METHODS_CDPPrivacySensitiveObject
+ __OBJC_$_INSTANCE_METHODS_CDPPrivacySensitiveObject
+ __OBJC_$_INSTANCE_VARIABLES_CDPPrivacySensitiveObject
+ __OBJC_$_PROP_LIST_CDPPrivacySensitiveObject
+ __OBJC_CLASS_RO_$_CDPPrivacySensitiveObject
+ __OBJC_METACLASS_RO_$_CDPPrivacySensitiveObject
+ ___33+[CDPUtilities isSolariumEnabled]_block_invoke
+ ___34+[CDPUtilities isNaturalUIEnabled]_block_invoke
+ ___35+[CDPUtilities isADPInBuddyEnabled]_block_invoke
+ ___35+[CDPUtilities isADPInBuddyEnabled]_block_invoke.cold.1
+ ___36-[CDPAccount isOTEnabledForContext:]_block_invoke.47
+ ___44+[CDPUtilities isSEPBasedICSCHealingEnabled]_block_invoke
+ ___44+[CDPUtilities isSEPBasedICSCHealingEnabled]_block_invoke.cold.1
+ ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.61
+ ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke.86
+ ___51+[CDPAccount isICDPEnabledForDSID:checkWithServer:]_block_invoke.35
+ ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.63
+ ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.78
+ ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.84
+ ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.84.cold.1
+ ___67-[CDPStateController createEDPLivenessDictionaryWithContext:error:]_block_invoke.88
+ ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.79
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.60
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke.cold.1
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke_2
+ ___72-[CDPStateController anyRecoveryKeysAreOctagonDistrustedWithCompletion:]_block_invoke_2.cold.1
+ ___73-[CDPStateUIProviderProxy cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.43
+ ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.80
+ ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.76
+ ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.77
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.90
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke.90.cold.1
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke_2
+ ___82-[CDPStateController performEscrowRecordCheckWithContext:isBackground:completion:]_block_invoke_2.cold.1
+ ___block_descriptor_48_e8_32bs40r_e20_v24?0Q8"NSError"16lr40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.169
+ ___block_literal_global.155
+ ___block_literal_global.171
+ ___block_literal_global.175
+ ___block_literal_global.46
+ ___block_literal_global.82
+ ___block_literal_global.83
+ ___block_literal_global.87
+ ___block_literal_global.91
+ ___block_literal_global.95
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
+ __current_pid
+ __merge_dict_cb.cold.2
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
+ _encode_icsc_params_internal
+ _get_akslog_context
+ _get_akslog_pid
+ _isADPInBuddyEnabled.enabled
+ _isADPInBuddyEnabled.once
+ _isNaturalUIEnabled.allowFeature
+ _isNaturalUIEnabled.predicate
+ _isSEPBasedICSCHealingEnabled.enabled
+ _isSEPBasedICSCHealingEnabled.once
+ _isSolariumEnabled.allowFeature
+ _isSolariumEnabled.predicate
+ _kCDPAnalyticsADPOfferAccept
+ _kCDPAnalyticsADPOfferDecline
+ _kCDPAnalyticsADPOfferEligibilityDataMigratorEvent
+ _kCDPAnalyticsADPOfferEligibilityEvent
+ _kCDPAnalyticsADPOfferEscapeOfferSelectedEvent
+ _kCDPAnalyticsADPOfferFinishEvent
+ _kCDPAnalyticsADPOfferLandingEvent
+ _kCDPAnalyticsWalrusRepairFinishEvent
+ _kCDPAnalyticsWalrusRepairStartEvent
+ _objc_msgSend$anyRecoveryKeysAreOctagonDistrustedWithContext:completion:
+ _objc_msgSend$escrowCheckForContext:isBackground:completion:
+ _objc_msgSend$establish:error:
+ _objc_msgSend$initWithObject:
+ _objc_msgSend$isSolariumEnabled
+ _objc_msgSend$viewMemberForAutofillPasswords:
+ _objc_msgSend$viewMemberForCreditCards:
+ _objc_msgSend$viewMemberForOtherSyncable:
+ _objc_msgSend$viewMemberForWiFi:
+ _ref_key_create_request_to_class
+ _se_derivation_request_deserialize
+ _se_derivation_request_serialization_len
+ _se_derivation_request_serialize
+ _set_akslog_context
+ _set_akslog_pid
+ _vsnprintf
- -[CDPContext initWithAccount:].cold.6
- -[CDPContext initWithAccount:].cold.7
- GCC_except_table109
- GCC_except_table119
- GCC_except_table122
- GCC_except_table125
- GCC_except_table128
- GCC_except_table131
- GCC_except_table134
- GCC_except_table136
- GCC_except_table139
- GCC_except_table144
- GCC_except_table37
- _OUTLINED_FUNCTION_75
- ___36-[CDPAccount isOTEnabledForContext:]_block_invoke.44
- ___48-[CDPStateController generateRandomRecoveryKey:]_block_invoke.59
- ___50-[CDPStateController fetchEDPTokenWithCompletion:]_block_invoke.84
- ___51+[CDPAccount isICDPEnabledForDSID:checkWithServer:]_block_invoke.32
- ___62-[CDPAccountRepresentation isICDPEnabledByCheckingWithServer:]_block_invoke.60
- ___66-[CDPStateController startSilentEscrowRecordRepairWithCompletion:]_block_invoke.76
- ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.82
- ___66-[CDPStateController validateEDPIdentitiesWithContext:completion:]_block_invoke.82.cold.1
- ___67-[CDPStateController createEDPLivenessDictionaryWithContext:error:]_block_invoke.87
- ___68-[CDPStateController performSilentEscrowRecordRepairWithCompletion:]_block_invoke.77
- ___73-[CDPStateUIProviderProxy cdpContext:promptForLocalSecretWithCompletion:]_block_invoke.40
- ___74-[CDPStateController updateLastSilentEscrowRecordRepairAttemptDate:error:]_block_invoke.78
- ___76-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:error:]_block_invoke.74
- ___81-[CDPStateController shouldPerformSilentEscrowRecordRepairUsingCache:completion:]_block_invoke.75
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.171
- ___block_literal_global.150
- ___block_literal_global.157
- ___block_literal_global.173
- ___block_literal_global.40
- ___block_literal_global.80
- _aks_change_secret_epilogue.cold.1
- _aks_change_secret_opts.cold.1
- _aks_recover_with_escrow_bag.cold.1
- _aks_set_system_with_passcode.cold.1
- _aks_unlock_bag.cold.1
- _der_key_validate
- _der_key_validate.cold.1
- _der_key_validate.cold.2
- _get_aks_log_pid
- _objc_msgSend$requestToJoinCircle:
CStrings:
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
+ "<PRIVACY SENSITIVE>"
+ "@"
+ "ADPInBuddy"
+ "ADPInBuddy: %{BOOL}d"
+ "Are there any RKs distrusted in Octagon? - %{BOOL}d"
+ "BEGIN [%lld]: CliqueEstablish  enableTelemetry=YES "
+ "CDPCircleProxyImpl requestToJoinCircle cliqueStatus is %@. No need to establish a new clique."
+ "CDPCircleProxyImpl requestToJoinCircle establish failed with error=%@"
+ "CDPCircleProxyImpl requestToJoinCircle establish finished with success=%@, error=%@"
+ "CDPCircleProxyImpl requestToJoinCircle establish succeeded."
+ "CDPCircleProxyImpl requestToJoinCircle fetchCliqueStatus failed with error=%@"
+ "CDPPrivacySensitiveObject"
+ "Checking if any Recovery Keys are Octagon distrusted"
+ "CliqueEstablish"
+ "END [%lld] %fs: CliqueEstablish  Error=%{public,signpost.telemetry:number1,name=Error}d "
+ "Failed to check if any Recovery Keys are distrusted in Octagon due to error %@"
+ "Failed to perform escrow record check: %@"
+ "HealthCheck"
+ "NO"
+ "NaturalUI"
+ "OnBoardingKit"
+ "Performing escrow check..."
+ "SEPBasedICSCHealingEnabled"
+ "SEPBasedICSCHealingEnabled: %{BOOL}d"
+ "Security"
+ "Solarium"
+ "Successfully performed escrow record check"
+ "SwiftUI"
+ "T@,R,V_wrappedObject"
+ "Vv36@0:8@\"CDPContext\"16B24@?<v@?Q@\"NSError\">28"
+ "WalrusStateChange"
+ "XPC Error while checking escrow record viability: %@"
+ "XPC Error while checking if any Recovery Keys are distrusted in Octagon: %@"
+ "YES"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "_wrappedObject"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
+ "anyRecoveryKeysAreOctagonDistrustedWithCompletion:"
+ "anyRecoveryKeysAreOctagonDistrustedWithContext:completion:"
+ "cdp/any-rk-ot-distrusted"
+ "cliqueStatus is %@, Requesting to join circle with OT establish"
+ "com.apple.corecdp.adpOfferEligibility"
+ "com.apple.corecdp.adpOfferEligibilityDataMigrator"
+ "com.apple.corecdp.adpOfferFinish"
+ "com.apple.corecdp.adpOfferLanding"
+ "com.apple.corecdp.walrusRepairFinish"
+ "com.apple.corecdp.walrusRepairStart"
+ "com.apple.dataaccess.adpOffer.accept"
+ "com.apple.dataaccess.adpOffer.decline"
+ "com.apple.dataaccess.adpOffer.escapeOfferSelected"
+ "deferSOSFromSignInAndSOSCompatible: error=%@ when checking for SOS compatibility mode."
+ "escrowCheckForContext:isBackground:completion:"
+ "establish:error:"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "initWithObject:"
+ "isADPInBuddyEnabled"
+ "isNaturalUIEnabled"
+ "isSEPBasedICSCHealingEnabled"
+ "isSolariumEnabled"
+ "performEscrowRecordCheckWithContext:isBackground:completion:"
+ "sensitiveObjectWrappingObject:"
+ "sosCompatibilityEnabled"
+ "viewMemberForAllUserFacingViews:"
+ "viewMemberForCreditCards:"
+ "viewMemberForOtherSyncable:"
+ "viewMemberForWiFi:"
+ "wrappedObject"
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
- "Requesting to join circle with OT requestToJoinCircle"
- "SOS Compat: AKAccountManager hasSOSActiveDeviceForAccount is True. Setting it in CDPContext."
- "SOS Compat: AKAccountManager isSOSNeededForAccount is True. Setting it in CDPContext."
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"
- "der_key_validate"
- "failed to open connection to %s\n"

```
