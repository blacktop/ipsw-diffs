## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore`

```diff

-417.80.4.0.0
-  __TEXT.__text: 0xbd084
-  __TEXT.__auth_stubs: 0x1f60
-  __TEXT.__objc_methlist: 0x5c1c
-  __TEXT.__const: 0x1500
-  __TEXT.__cstring: 0xcd5c
-  __TEXT.__oslogstring: 0x36cc
-  __TEXT.__gcc_except_tab: 0xf4c
+417.100.37.0.0
+  __TEXT.__text: 0xbeea4
+  __TEXT.__auth_stubs: 0x1f50
+  __TEXT.__objc_methlist: 0x61e0
+  __TEXT.__const: 0x1540
+  __TEXT.__cstring: 0xd2ac
+  __TEXT.__oslogstring: 0x383c
+  __TEXT.__gcc_except_tab: 0xfcc
   __TEXT.__dlopen_cstrs: 0x294
   __TEXT.__swift5_typeref: 0x16e
   __TEXT.__constg_swiftt: 0x348

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x2510
-  __TEXT.__eh_frame: 0x690
+  __TEXT.__unwind_info: 0x2690
+  __TEXT.__eh_frame: 0x6c0
   __TEXT.__objc_classname: 0xdd8
-  __TEXT.__objc_methname: 0xc8b1
-  __TEXT.__objc_methtype: 0x2ce1
-  __TEXT.__objc_stubs: 0x7f20
+  __TEXT.__objc_methname: 0xccde
+  __TEXT.__objc_methtype: 0x2d77
+  __TEXT.__objc_stubs: 0x8080
   __DATA_CONST.__got: 0xa30
-  __DATA_CONST.__const: 0x1f08
+  __DATA_CONST.__const: 0x1f68
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2bd0
+  __DATA_CONST.__objc_selrefs: 0x2d58
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x200
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xfc0
+  __AUTH_CONST.__auth_got: 0xfb8
   __AUTH_CONST.__const: 0x16e0
-  __AUTH_CONST.__cfstring: 0x7ba0
-  __AUTH_CONST.__objc_const: 0x15118
+  __AUTH_CONST.__cfstring: 0x7e20
+  __AUTH_CONST.__objc_const: 0x148c0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3590
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x5ec
-  __DATA.__data: 0x1058
-  __DATA.__bss: 0xfb8
+  __DATA.__objc_ivar: 0x5f8
+  __DATA.__data: 0x1068
+  __DATA.__bss: 0xfc0
   __DATA.__common: 0x91
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 40B1B9BF-DDDB-3BB6-8F9C-D2D98795A3E2
-  Functions: 3871
-  Symbols:   8735
-  CStrings:  5729
+  UUID: 9D073E19-3C12-3B61-A8C9-D54D1774A3DC
+  Functions: 4266
+  Symbols:   9279
+  CStrings:  5816
 
Symbols:
+ +[POBaseSystemSupport fvunlockMode].cold.1
+ +[POBaseSystemSupport getSystemVolumeUuid].cold.1
+ +[POCoreConfigurationUtil isInternalBuild].cold.1
+ +[PODaemonCoreConnection xpcQueue].cold.1
+ +[POInternalProtocols interfaceWithInternalProtocol:].cold.1
+ +[POSecKeyHelper publicKeyHashForKey:]
+ +[POServiceCoreConnection xpcQueue].cold.1
+ +[POXSDefinitions definitionForType:].cold.1
+ +[POXSNamespaces prefixForNamespaceURI:].cold.1
+ -[POAgentCoreProcess verifyAgentEntitlement].cold.2
+ -[POConfigurationCoreManager initWithUserName:identifierProvider:sharedOnly:volume:].cold.1
+ -[POConfigurationCoreManager isTemporaryAccountUserName:]
+ -[POConfigurationCoreManager isTemporaryAccountUserName:].cold.1
+ -[POConfigurationCoreManager isTemporaryAccountUserName:].cold.2
+ -[POConfigurationCoreManager setUserName:]
+ -[PODeviceConfiguration allowDeviceIdentifiersInAttestation]
+ -[PODeviceConfiguration decryptTemporaryAccountCredential]
+ -[PODeviceConfiguration decryptTemporaryAccountCredential].cold.1
+ -[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]
+ -[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:].cold.1
+ -[PODeviceConfiguration setAllowDeviceIdentifiersInAttestation:]
+ -[PODeviceConfiguration setTemporaryAccountCredential:]
+ -[PODeviceConfiguration supportsCreateTemporaryUsers]
+ -[PODeviceConfiguration supportsCreateTemporaryUsers].cold.1
+ -[PODeviceConfiguration temporaryAccountCredential]
+ -[POJWTSigning encodeAndSignJWT:key:certificate:]
+ -[POJWTSigning signData:usingKey:]
+ -[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]
+ -[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:].cold.1
+ -[POKeychainHelper _deleteAllCachedAttestations]
+ -[POKeychainHelper _deleteAllCachedAttestations].cold.1
+ -[POKeychainHelper _deleteCachedAttestationForExtensionIdentifier:key:]
+ -[POKeychainHelper _deleteCachedAttestationForExtensionIdentifier:keyHash:]
+ -[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]
+ -[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:].cold.1
+ -[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:error:]
+ -[POKeychainHelper removeTokensFromKeychainWithService:username:system:]
+ -[POKeychainHelper removeTokensFromKeychainWithService:username:system:].cold.1
+ -[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:]
+ -[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:].cold.1
+ -[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:].cold.2
+ -[POLoginProcessBase setContextBool:withFlags:forKey:]
+ -[POPlatformSSOCoreListener listener:shouldAcceptNewConnection:].cold.2
+ -[POXSDateDefinition stringFromValue:].cold.1
+ -[POXSDateDefinition valueFromString:].cold.1
+ -[POXSDateTimeDefinition valueFromString:].cold.1
+ -[POXSRFC3339DateDefinition stringFromValue:].cold.1
+ -[POXSRFC3339DateDefinition valueFromString:].cold.1
+ -[POXSTimeDefinition valueFromString:].cold.1
+ ACMContextGetExternalForm.cold.1
+ GCC_except_table114
+ GCC_except_table175
+ GCC_except_table349
+ GCC_except_table404
+ GCC_except_table50
+ GCC_except_table56
+ GCC_except_table62
+ GCC_except_table65
+ GCC_except_table68
+ GCC_except_table9
+ LA_LOG_EndpointProvider.cold.1
+ OBJC_IVAR_$_POConfigurationCoreManager._userLock
+ OBJC_IVAR_$_PODeviceConfiguration._allowDeviceIdentifiersInAttestation
+ OBJC_IVAR_$_PODeviceConfiguration._temporaryAccountCredential
+ PO_LOG_POACMHelper.cold.1
+ PO_LOG_POAgentCoreProcess.cold.1
+ PO_LOG_POAuthPluginCoreProcess.cold.1
+ PO_LOG_POAuthenticationProcess.cold.1
+ PO_LOG_POBaseSystemLoginProcess.cold.1
+ PO_LOG_POBaseSystemSupport.cold.1
+ PO_LOG_POConfigurationManager.cold.1
+ PO_LOG_POConfigurationVersion.cold.1
+ PO_LOG_POCoreConfigurationUtil.cold.1
+ PO_LOG_POCredentialUtil.cold.1
+ PO_LOG_PODaemonCoreConnection.cold.1
+ PO_LOG_PODaemonCoreProcess.cold.1
+ PO_LOG_PODeviceConfiguration.cold.1
+ PO_LOG_PODiagnostics.cold.1
+ PO_LOG_POJWT.cold.1
+ PO_LOG_POJWTEncryption.cold.1
+ PO_LOG_POJWTHeader.cold.1
+ PO_LOG_POJWTSigning.cold.1
+ PO_LOG_POKeyBag.cold.1
+ PO_LOG_POKeyWrap.cold.1
+ PO_LOG_POKeychainHelper.cold.1
+ PO_LOG_POLoginConfiguration.cold.1
+ PO_LOG_POLoginProcess.cold.1
+ PO_LOG_POLoginUserCore.cold.1
+ PO_LOG_POPrebootDeviceConfiguration.cold.1
+ PO_LOG_POPreferences.cold.1
+ PO_LOG_POPreloginUserProvider.cold.1
+ PO_LOG_POSecKeyHelper.cold.1
+ PO_LOG_POServiceCoreConnection.cold.1
+ PO_LOG_POTokenHelper.cold.1
+ PO_LOG_POUserConfiguration.cold.1
+ PO_LOG_POUserLoginConfiguration.cold.1
+ PO_LOG_POUserLoginState.cold.1
+ PO_LOG_POUserUnlockKey.cold.1
+ PO_LOG_POWSTrustProcess.cold.1
+ PO_LOG_POXMLHelper.cold.1
+ TKAddSecureToken.cold.10
+ TKAddSecureToken.cold.11
+ TKAddSecureToken.cold.12
+ TKAddSecureToken.cold.13
+ TKAddSecureToken.cold.14
+ TKAddSecureToken.cold.15
+ TKAddSecureToken.cold.8
+ TKAddSecureToken.cold.9
+ TKBindUser.cold.2
+ TKBindUserAm.cold.2
+ TKCopyAvailableTokensInfo.cold.3
+ TKCopyAvailableTokensInfo.cold.4
+ TKCopyAvailableTokensInfo.cold.5
+ TKCopyAvailableTokensInfo.cold.6
+ TKCopyLegacyBindings.cold.10
+ TKCopyLegacyBindings.cold.11
+ TKCopyLegacyBindings.cold.12
+ TKCopyLegacyBindings.cold.7
+ TKCopyLegacyBindings.cold.8
+ TKCopyLegacyBindings.cold.9
+ TKCopySmartCardConfiguration.cold.6
+ TKCopySmartCardConfiguration.cold.7
+ TKCopySmartCardConfiguration.cold.8
+ TKCopySmartCardConfiguration.cold.9
+ TKGetSmartcardSetting.cold.1
+ TKGetSmartcardSetting.cold.2
+ TKGetSmartcardSettingForUser.cold.1
+ TKGetSmartcardSettingForUser.cold.2
+ TKGetSmartcardSettingForUser.cold.3
+ TKGetSmartcardSettingForUser.cold.4
+ TKGetSmartcardSettingForUser.cold.5
+ TKGetSmartcardSettingForUser.cold.6
+ TKGetSmartcardSettingForUser.cold.7
+ TKGetSmartcardSettingForUser.cold.8
+ TKGetSmartcardSettingForUser.cold.9
+ TKGetSmartcardSettingWorker.cold.1
+ TKGetSmartcardSettingWorker.cold.2
+ TKGetSmartcardSettingWorker.cold.3
+ TKGetSmartcardSettingWorker.cold.4
+ TKIsUserBound.cold.4
+ TKIsUserBound.cold.5
+ TKIsUserBound.cold.6
+ TKPerformLogin.cold.10
+ TKPerformLogin.cold.11
+ TKPerformLogin.cold.6
+ TKPerformLogin.cold.7
+ TKPerformLogin.cold.8
+ TKPerformLogin.cold.9
+ TKReadSecureTokenData.cold.10
+ TKReadSecureTokenData.cold.11
+ TKReadSecureTokenData.cold.6
+ TKReadSecureTokenData.cold.7
+ TKReadSecureTokenData.cold.8
+ TKReadSecureTokenData.cold.9
+ TKSmartCardSecureTokenRemove.cold.5
+ TKSmartCardSecureTokenRemove.cold.6
+ TKSmartCardSecureTokenRemove.cold.7
+ TKSmartCardSecureTokenRemove.cold.8
+ TKSmartCardSecureTokenRemove.cold.9
+ TKSmartCardSecureTokenStatus.cold.5
+ TKSmartCardSecureTokenStatus.cold.6
+ TKSmartCardSecureTokenStatus.cold.7
+ TKSmartCardSecureTokenStatus.cold.8
+ TKSmartCardSecureTokenStatus.cold.9
+ TKTokenCreateInternal.cold.2
+ TKTokenGetTypeID.cold.1
+ TKUnbindUser.cold.2
+ TKUnlockKeybag.cold.4
+ TKUnlockKeybag.cold.5
+ TKUnlockKeybag.cold.6
+ TKValidateAttributeMatchingConfig.cold.5
+ TKValidateAttributeMatchingConfig.cold.6
+ TKValidateAttributeMatchingConfig.cold.7
+ TKValidateAttributeMatchingConfig.cold.8
+ TKValidateAttributeMatchingConfig.cold.9
+ TK_LOG_ctkclnt.cold.1
+ _AKSGetStashStats
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
+ _POTokenValueShortName
+ __103-[POAgentCoreProcess exchangeKeyWithPublicKeyData:userName:passwordContext:responseContext:completion:]_block_invoke_2.cold.1
+ __34-[_POJWTBodyBase initWithJWTData:]_block_invoke.cold.2
+ __38-[PODeviceConfiguration initWithData:]_block_invoke.135
+ __48-[PODeviceConfiguration setDeviceEncryptionKey:]_block_invoke.cold.1
+ __48-[POKeychainHelper _deleteAllCachedAttestations]_block_invoke.cold.1
+ __49-[POConfigurationCoreManager deviceConfiguration]_block_invoke.83
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.101
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.101.cold.1
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.105
+ __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.105.cold.1
+ __54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.68
+ __54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.68.cold.1
+ __55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.76
+ __55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.76.cold.1
+ __56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.72
+ __56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.72.cold.1
+ __56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.103
+ __56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.103.cold.1
+ __56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.99
+ __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.78
+ __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.78.cold.1
+ __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.85
+ __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.85.cold.1
+ __58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.38
+ __58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.38.cold.1
+ __58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.cold.1
+ __59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.88
+ __59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.92
+ __59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.92.cold.1
+ __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.71
+ __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.71.cold.1
+ __63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.117
+ __63-[POConfigurationCoreManager saveStashedSSOTokens:forUserName:]_block_invoke.125
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.141
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.141.cold.1
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.147
+ __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.147.cold.1
+ __66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.121
+ __66-[POConfigurationCoreManager retrieveStashedSSOTokensForUserName:]_block_invoke.129
+ __66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.23
+ __66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.23.cold.1
+ __66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.29
+ __66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.29.cold.1
+ __66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.cold.1
+ __67-[POConfigurationCoreManager updateLoginTypeForUserName:loginType:]_block_invoke.116
+ __71-[POConfigurationCoreManager saveStashedDecryptionContext:forUserName:]_block_invoke.133
+ __71-[POKeychainHelper _deleteCachedAttestationForExtensionIdentifier:key:]_block_invoke.cold.1
+ __72-[POKeychainHelper removeTokensFromKeychainWithService:username:system:]_block_invoke.27
+ __72-[POKeychainHelper removeTokensFromKeychainWithService:username:system:]_block_invoke.27.cold.1
+ __72-[POKeychainHelper removeTokensFromKeychainWithService:username:system:]_block_invoke.cold.1
+ __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.155
+ __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.155.cold.1
+ __74-[POConfigurationCoreManager retrieveStashedDecryptionContextForUserName:]_block_invoke.134
+ __75-[POKeychainHelper _deleteCachedAttestationForExtensionIdentifier:keyHash:]_block_invoke.cold.1
+ __77-[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]_block_invoke.45
+ __77-[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]_block_invoke.45.cold.1
+ __77-[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]_block_invoke.cold.1
+ __84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.108
+ __84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.108.cold.1
+ __84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.114
+ __97-[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]_block_invoke.38
+ __97-[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]_block_invoke.38.cold.1
+ __97-[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]_block_invoke.cold.1
+ __98-[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:]_block_invoke.cold.1
+ __MergedGlobals
+ ___48-[PODeviceConfiguration setDeviceEncryptionKey:]_block_invoke
+ ___48-[POKeychainHelper _deleteAllCachedAttestations]_block_invoke
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke
+ ___71-[POKeychainHelper _deleteCachedAttestationForExtensionIdentifier:key:]_block_invoke
+ ___72-[POKeychainHelper removeTokensFromKeychainWithService:username:system:]_block_invoke
+ ___75-[POKeychainHelper _deleteCachedAttestationForExtensionIdentifier:keyHash:]_block_invoke
+ ___77-[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]_block_invoke
+ ___97-[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]_block_invoke
+ ___98-[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:]_block_invoke
+ ___der_key_booted_from_uuid
+ ___der_key_config_recovery_params
+ ___der_key_peer_kcv
+ ___getTKCTKDConnectionClass_block_invoke
+ __aks_se_set_secret.cold.1
+ __block_literal_global.156
+ __block_literal_global.231
+ __block_literal_global.336
+ __block_literal_global.358
+ __block_literal_global.81
+ __block_literal_global.87
+ __getSystemVolumeUuid_block_invoke.cold.5
+ __getSystemVolumeUuid_block_invoke.cold.6
+ __getSystemVolumeUuid_block_invoke.cold.7
+ __getSystemVolumeUuid_block_invoke.cold.8
+ __getTKCTKDConnectionClass_block_invoke.cold.1
+ __getUidForAgent_block_invoke.cold.4
+ __getUidForAgent_block_invoke.cold.5
+ _aks_remote_reset_all_peers
+ _aks_remote_reset_peer
+ _decode_peer_state
+ _der_key_booted_from_uuid
+ _der_key_config_recovery_params
+ _der_key_peer_kcv
+ _iterate_path.cold.1
+ _kAttestationCacheTimeInterval
+ _kAttestationDate
+ _kAttestationEntryName
+ _kTemporaryUserAccountName
+ _kTemporaryUserFullName
+ _merge_dict_cb.cold.1
+ _objc_msgSend$_deleteCachedAttestationForExtensionIdentifier:keyHash:
+ _objc_msgSend$_saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:
+ _objc_msgSend$allowDeviceIdentifiersInAttestation
+ _objc_msgSend$dataWithPropertyList:format:options:error:
+ _objc_msgSend$decryptTemporaryAccountCredential
+ _objc_msgSend$encryptAndSaveTemporaryAccountCredential:
+ _objc_msgSend$initWithCTKDEndpoint:targetUID:
+ _objc_msgSend$initWithTokenID:ctkdConnection:
+ _objc_msgSend$isTemporaryAccountUserName:
+ _objc_msgSend$publicKeyHashForKey:
+ _objc_msgSend$removeTokensFromKeychainWithService:username:system:
+ _objc_msgSend$retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:
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
+ binderWorker.cold.5
+ binderWorker.cold.6
+ binderWorker.cold.7
+ binderWorker.cold.8
+ circular_queue_init.cold.1
+ der_key_validate.cold.1
+ der_key_validate.cold.2
+ fvunlockPrefs.cold.2
+ fvunlockPrefs.cold.3
+ getOdCustomEnforcementAttribute.cold.13
+ getOdCustomEnforcementAttribute.cold.14
+ getOdCustomEnforcementAttribute.cold.15
+ getOdCustomEnforcementAttribute.cold.16
+ getOdCustomEnforcementAttribute.cold.17
+ getOdCustomEnforcementAttribute.cold.18
+ getOdCustomEnforcementAttribute.cold.19
+ getOdCustomEnforcementAttribute.cold.20
+ getSystemVolumeUuid.cold.1
+ getTKCTKDConnectionClass.softClass
+ getUidForAgent.cold.1
+ get_aks_client_connection.cold.1
+ get_akstest_client_connection.cold.1
+ isEnforcementOverriden.cold.1
+ isEnforcementOverriden.cold.2
+ isMemberOfGroup.cold.5
+ isMemberOfGroup.cold.6
+ isMemberOfGroup.cold.7
+ isMemberOfGroup.cold.8
+ provideEndpoint.cold.4
+ provideEndpoint.cold.5
+ rfc3394_unwrap.cold.1
+ rfc3394_unwrap.cold.2
+ rfc3394_wrap.cold.1
+ rfc3394_wrap.cold.2
+ setupConnection.cold.2
+ setupConnection.cold.3
+ updateLogLevelFromKext.cold.1
- -[POAuthenticationContext dealloc]
- -[PODaemonCoreProcess _pendingSSOTokensForIdentifer:error:].cold.2
- -[POKeychainHelper removeTokensFromKeychainWithService:username:]
- -[POKeychainHelper removeTokensFromKeychainWithService:username:].cold.1
- -[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:]
- -[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:].cold.1
- -[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:].cold.2
- GCC_except_table110
- GCC_except_table177
- GCC_except_table347
- GCC_except_table401
- GCC_except_table49
- GCC_except_table52
- GCC_except_table55
- GCC_except_table58
- GCC_except_table8
- TKCopyTokenEndpoints.cold.1
- __38-[PODeviceConfiguration initWithData:]_block_invoke.102
- __49-[POConfigurationCoreManager deviceConfiguration]_block_invoke.82
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.100
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.100.cold.1
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.104
- __53-[PODaemonCoreProcess _saveUserLoginStateList:error:]_block_invoke.104.cold.1
- __54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.67
- __54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.67.cold.1
- __55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.75
- __55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.75.cold.1
- __56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.71
- __56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.71.cold.1
- __56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.102
- __56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.102.cold.1
- __56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.98
- __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.77
- __56-[PODaemonCoreProcess _userLoginStateListDataWithError:]_block_invoke.77.cold.1
- __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.84
- __58-[PODaemonCoreProcess _parseUserLoginStateListData:error:]_block_invoke.84.cold.1
- __59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.87
- __59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.91
- __59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.91.cold.1
- __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.70
- __61-[PODaemonCoreProcess _userConfigurationForIdentifier:error:]_block_invoke.70.cold.1
- __63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.116
- __63-[POConfigurationCoreManager saveStashedSSOTokens:forUserName:]_block_invoke.124
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.140
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.140.cold.1
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.144
- __63-[PODaemonCoreProcess _saveCachedContextsToDiskWithCompletion:]_block_invoke.144.cold.1
- __65-[POKeychainHelper removeTokensFromKeychainWithService:username:]_block_invoke.21
- __65-[POKeychainHelper removeTokensFromKeychainWithService:username:]_block_invoke.21.cold.1
- __65-[POKeychainHelper removeTokensFromKeychainWithService:username:]_block_invoke.cold.1
- __66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.120
- __66-[POConfigurationCoreManager retrieveStashedSSOTokensForUserName:]_block_invoke.128
- __67-[POConfigurationCoreManager updateLoginTypeForUserName:loginType:]_block_invoke.115
- __71-[POConfigurationCoreManager saveStashedDecryptionContext:forUserName:]_block_invoke.132
- __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.154
- __73-[PODaemonCoreProcess verifyTokenForUserName:passwordContext:completion:]_block_invoke.154.cold.1
- __74-[POConfigurationCoreManager retrieveStashedDecryptionContextForUserName:]_block_invoke.133
- __84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.107
- __84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.107.cold.1
- __84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.113
- __91-[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:]_block_invoke.cold.1
- ___65-[POKeychainHelper removeTokensFromKeychainWithService:username:]_block_invoke
- ___91-[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:]_block_invoke
- ___der_key_config_recovery_flags
- __block_literal_global.155
- __block_literal_global.226
- __block_literal_global.312
- __block_literal_global.335
- __block_literal_global.39
- __block_literal_global.80
- __isNullOrEqualMem2
- _aks_show_allowlist_with_map
- _der_key_config_recovery_flags
- _objc_msgSend$removeTokensFromKeychainWithService:username:
- _tk_log.log
- _tk_log.onceToken
CStrings:
+ "%@:%@"
+ "%s file = %{public}@, data = %{public}@, %{public}@ on %@"
+ "%s shared = %{public}@, createUsersEnabled = %{public}@, newUserAuthorizationMode = %{public}@ on %@"
+ "-[POConfigurationCoreManager isTemporaryAccountUserName:]"
+ "-[PODeviceConfiguration supportsCreateTemporaryUsers]"
+ "-[POKeychainHelper _checkForCachedAttestationForExtensionIdentifier:keyHash:]"
+ "-[POKeychainHelper _saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:]"
+ "-[POKeychainHelper retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:]"
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
+ "@\"NSObject\""
+ "AKSGetStashStats"
+ "B48@0:8@16@24@32^@40"
+ "B56@0:8@16@24@32@40^@48"
+ "Cached attestation not found."
+ "Cached attestation too old."
+ "Class getTKCTKDConnectionClass(void)_block_invoke"
+ "Completed saving data to: %{public}@, %{public}@"
+ "Configuriation for: %{public}@"
+ "Creating configuration manager"
+ "Deleting cached attestations"
+ "Encryption algorithm not supported."
+ "Failed to deserialize attestation data"
+ "Failed to encrypt temporary account credential when updating encryption key."
+ "Failed to encrypt temporary account credential."
+ "Failed to remove cached attestation."
+ "Failed to remove cached attestations."
+ "Failed to save attestation data in cache."
+ "Failed to serialize attestation data"
+ "Falied to get hash for key."
+ "Missing device encryption public key."
+ "Platform SSO Temporary User"
+ "T@\"NSData\",C,V_temporaryAccountCredential"
+ "T@\"NSString\",&,V_userName"
+ "TB,N,V_allowDeviceIdentifiersInAttestation"
+ "TKCTKDConnection"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_deviceEncryptionKey"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_deviceSigningKey"
+ "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},R,N"
+ "Temporary"
+ "User is Platform SSO temporary account"
+ "_allowDeviceIdentifiersInAttestation"
+ "_checkForCachedAttestationForExtensionIdentifier:keyHash:"
+ "_deleteAllCachedAttestations"
+ "_deleteCachedAttestationForExtensionIdentifier:key:"
+ "_deleteCachedAttestationForExtensionIdentifier:keyHash:"
+ "_saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:"
+ "_saveAttestationToKeychain:extensionIdentifier:keyHash:error:"
+ "_temporaryAccountCredential"
+ "_userLock"
+ "aks_remote_reset_all_peers"
+ "allowDeviceIdentifiersInAttestation"
+ "com.apple.PlatformSSO.AccountShortName"
+ "com.apple.platformsso.attestation"
+ "dataWithPropertyList:format:options:error:"
+ "decryptTemporaryAccountCredential"
+ "encryptAndSaveTemporaryAccountCredential"
+ "encryptAndSaveTemporaryAccountCredential:"
+ "failed to decrypt temporary account credential."
+ "i36@0:8@16@24B32"
+ "i52@0:8@16@24B32^@36^@44"
+ "initWithCTKDEndpoint:targetUID:"
+ "initWithTokenID:ctkdConnection:"
+ "isTemporaryAccountUserName:"
+ "kAttestationDate"
+ "publicKeyHashForKey:"
+ "removeTokensFromKeychainWithService:username:system:"
+ "retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:"
+ "setAllowDeviceIdentifiersInAttestation:"
+ "setContextBool:withFlags:forKey:"
+ "setTemporaryAccountCredential:"
+ "supportsCreateTemporaryUsers"
+ "temporary"
+ "temporaryAccountCredential"
+ "temporary_session"
+ "v32@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
+ "v32@0:8B16I20r*24"
- "-[POKeychainHelper retrieveTokensFromKeychainForService:username:returningTokens:metaData:]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "Completed saving data to: %{public}@"
- "Creating configuraton manager"
- "T@\"NSString\",R,V_userName"
- "T^{__SecKey=},N,V_deviceEncryptionKey"
- "T^{__SecKey=},N,V_deviceSigningKey"
- "T^{__SecKey=},R,N"
- "i32@0:8@16@24"
- "i48@0:8@16@24^@32^@40"
- "removeTokensFromKeychainWithService:username:"
- "retrieveTokensFromKeychainForService:username:returningTokens:metaData:"

```
