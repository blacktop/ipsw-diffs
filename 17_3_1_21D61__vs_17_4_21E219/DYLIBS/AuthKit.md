## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-466.7.15.0.0
-  __TEXT.__text: 0xb046c
+466.23.1.1.0
+  __TEXT.__text: 0xb3604
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x9b28
-  __TEXT.__const: 0x1760
-  __TEXT.__cstring: 0xba4a
-  __TEXT.__oslogstring: 0xced5
-  __TEXT.__gcc_except_tab: 0x3d50
+  __TEXT.__objc_methlist: 0x9c88
+  __TEXT.__const: 0x1c61
+  __TEXT.__cstring: 0xbeb0
+  __TEXT.__oslogstring: 0xd508
+  __TEXT.__gcc_except_tab: 0x3f1c
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x32ac
-  __TEXT.__objc_classname: 0x15b5
-  __TEXT.__objc_methname: 0x1a659
-  __TEXT.__objc_methtype: 0x3775
-  __TEXT.__objc_stubs: 0xbfe0
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x46d8
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __TEXT.__dlopen_cstrs: 0x5a
+  __TEXT.__unwind_info: 0x3388
+  __TEXT.__objc_classname: 0x15c4
+  __TEXT.__objc_methname: 0x1aa83
+  __TEXT.__objc_methtype: 0x379e
+  __TEXT.__objc_stubs: 0xc060
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x49b8
+  __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b498
-  __DATA_CONST.__objc_selrefs: 0x5758
+  __DATA_CONST.__objc_const: 0x1b668
+  __DATA_CONST.__objc_selrefs: 0x5808
+  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_classrefs: 0x5b8
+  __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0xc0a0
-  __AUTH_CONST.__objc_const: 0x4420
+  __AUTH_CONST.__cfstring: 0xc300
+  __AUTH_CONST.__objc_const: 0x4468
   __AUTH_CONST.__const: 0xf50
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__auth_got: 0x6a8
   __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_protorefs: 0xd0
-  __DATA.__objc_classrefs: 0x5b8
-  __DATA.__objc_superrefs: 0x2d8
-  __DATA.__objc_ivar: 0xd04
-  __DATA.__data: 0x1560
-  __DATA.__bss: 0x360
-  __DATA_DIRTY.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0xd20
+  __DATA.__data: 0x1588
+  __DATA.__bss: 0x388
+  __DATA_DIRTY.__objc_data: 0x1270
   __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5228
-  Symbols:   16990
-  CStrings:  7578
+  Functions: 5313
+  Symbols:   17223
+  CStrings:  7682
 
Symbols:
+ +[AKAuthorizationController shouldProcessURL:].cold.2
+ -[AKAccountManager _isSilentBurnCDPRepairEnabledForAccount:]
+ -[AKAccountManager _isSilentBurnCDPRepairEnabledForAccount:].cold.1
+ -[AKAccountManager aidaServiceOwnermanager]
+ -[AKAccountManager get3PRegulatoryOverride:]
+ -[AKAccountManager get3PRegulatoryOverride:].cold.1
+ -[AKAccountManager isSilentBurnCDPRepairEnabledForAccount:]
+ -[AKAccountManager isSilentBurnCDPRepairEnabledForAccount:].cold.1
+ -[AKAccountManager isSilentBurnCDPRepairEnabledForAccount:].cold.2
+ -[AKAccountManager isSiwaEnabledForChildAccount:]
+ -[AKAccountManager isSiwaEnabledForChildAccount:].cold.1
+ -[AKAccountManager set3PRegulatoryOverride:forAccount:]
+ -[AKAccountManager set3PRegulatoryOverride:forAccount:].cold.1
+ -[AKAccountManager setBeneficiaryLastModified:forAccount:]
+ -[AKAccountManager setBeneficiaryLastModified:forAccount:].cold.1
+ -[AKAccountManager setIsSiwaEnabled:forChildAccount:]
+ -[AKAccountManager setIsSiwaEnabled:forChildAccount:].cold.1
+ -[AKAccountManager setSilentBurnCDPRepairEnabled:forAccount:]
+ -[AKAccountManager setSilentBurnCDPRepairEnabled:forAccount:].cold.1
+ -[AKAccountStore accountTypeWithAccountTypeIdentifier:error:]
+ -[AKAccountStore accountsWithAccountType:options:error:]
+ -[AKAccountStore credentialForAccount:error:]
+ -[AKAccountStore credentialForAccount:serviceID:error:]
+ -[AKAccountStore isAccountDeamonConnectionError:]
+ -[AKAuthorizationController _appleOwnedDomains].cold.1
+ -[AKAuthorizationController _nativeTakeoverURLs].cold.1
+ -[AKConfiguration forceSilentBurnCDPRepairEnabled]
+ -[AKConfiguration setForceSilentBurnCDPRepairEnabled:]
+ -[AKFeatureManager init].cold.9
+ -[AKFeatureManager isTiburonU13Enabled]
+ -[AKMediaServicesController .cxx_destruct]
+ -[AKMediaServicesController init]
+ -[AKURLBag baaSigningSamplingRate]
+ -[AKURLBag isBAAAnalyticsDisabled]
+ -[AKURLBag manageSiwaForChildUrl]
+ -[AKUserInformation isSiwaForChildEnabled]
+ -[AKUserInformation setIsSiwaForChildEnabled:]
+ -[AKUserInformation setSilentBurnCDPRepairEnabled:]
+ -[AKUserInformation setSilentEscrowRecordRepairEnabledV2:]
+ -[AKUserInformation setThirdPartyRegulatoryOverride:]
+ -[AKUserInformation setUserAgeRange:]
+ -[AKUserInformation silentBurnCDPRepairEnabled]
+ -[AKUserInformation silentEscrowRecordRepairEnabledV2]
+ -[AKUserInformation thirdPartyRegulatoryOverride]
+ -[AKUserInformation userAgeRange]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table147
+ GCC_except_table157
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table212
+ GCC_except_table215
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table222
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table227
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table258
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table271
+ GCC_except_table272
+ GCC_except_table273
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table77
+ GCC_except_table98
+ GCC_except_table99
+ _ACErrorDomain
+ _AK3PRegulatoryOverrideKey
+ _AKAuthentication3PRegulatoryOverrideKey
+ _AKBeneficiaryInfoKeychainAccessGroup
+ _AKContinutationKeyGenKey
+ _AKEphemeralAuthKey
+ _AKInformationBeneficiaryWrappedKeyKey
+ _AKShortLivedTokenKey
+ _AKSilentBurnCDPRepairEnabledKey
+ _AKURLBagKeyManageSiwaForChildUrl
+ _AppStoreComponentsLibrary
+ _AppStoreComponentsLibraryCore
+ _AppStoreComponentsLibraryCore.frameworkLibrary
+ _AppleIDSSOAuthenticationLibrary
+ _AppleIDSSOAuthenticationLibraryCore
+ _AppleIDSSOAuthenticationLibraryCore.frameworkLibrary
+ _BASepAppRoot
+ _BASepAppRootPublicKey
+ _BASepAppRootSKID
+ _BASepAppRootSPKI
+ _CTEvaluateBAA
+ _CTEvaluateBAASepApp
+ _CTGetBAARootType
+ _CTGetBAASubCAType
+ _MFi4RootSKID
+ _OBJC_CLASS_$_AKAccountStore
+ _OBJC_IVAR_$_AKAccountManager._aidaServiceOwnermanager
+ _OBJC_IVAR_$_AKAccountManager._serialQueue
+ _OBJC_IVAR_$_AKFeatureManager._cachedIsTiburonU13Enabled
+ _OBJC_IVAR_$_AKMediaServicesController._group
+ _OBJC_IVAR_$_AKUserInformation._isSiwaForChildEnabled
+ _OBJC_IVAR_$_AKUserInformation._silentEscrowRecordRepairEnabledV2
+ _OBJC_IVAR_$_AKUserInformation._thirdPartyRegulatoryOverride
+ _OBJC_IVAR_$_AKUserInformation._userAgeRange
+ _OBJC_METACLASS_$_ACAccountStore
+ _OBJC_METACLASS_$_AKAccountStore
+ _SDeviceIdentityIsSupported
+ _SDeviceIdentityIsSupported.cold.1
+ _X509ExtensionParseCertifiedChipIntermediate
+ _X509PolicyBAASepApp
+ __OBJC_$_INSTANCE_METHODS_AKAccountStore
+ __OBJC_$_INSTANCE_VARIABLES_AKMediaServicesController
+ __OBJC_CLASS_RO_$_AKAccountStore
+ __OBJC_METACLASS_RO_$_AKAccountStore
+ ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.81
+ ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.81.cold.1
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.299
+ ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.298
+ ___43-[AKAccountManager aidaServiceOwnermanager]_block_invoke
+ ___43-[AKUserInformation _parseBeneficiaryInfo:]_block_invoke.cold.1
+ ___45-[AKCarouselAlertClientConnection connection]_block_invoke.54
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.319
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.319.cold.1
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.319.cold.2
+ ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.110
+ ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.110.cold.1
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.29
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.1
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.2
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.3
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.4
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.5
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.6
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.30.cold.7
+ ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke_2.cold.1
+ ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.276
+ ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke.147
+ ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.109
+ ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.109.cold.1
+ ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.105
+ ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.105.cold.1
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.280
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.280.cold.1
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.281
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.281.cold.1
+ ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.281.cold.2
+ ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.103
+ ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.103.cold.1
+ ___69-[AKAppleIDAuthenticationController _authenticationServiceConnection]_block_invoke.327
+ ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.291
+ ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.107
+ ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.107.cold.1
+ ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.98
+ ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.98.cold.1
+ ___70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.275
+ ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.321
+ ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.112
+ ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.112.cold.1
+ ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.79
+ ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.79.cold.1
+ ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.102
+ ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.102.cold.1
+ ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.322
+ ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.242
+ ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.244
+ ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.309
+ ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.309.cold.1
+ ___72-[AKAppleIDPasskeyController setupAppleIDPasskeyWithContext:completion:]_block_invoke.69
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.332
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.332.cold.1
+ ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.273
+ ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.264
+ ___73-[AKAppleIDPasskeyController appleIDPasskeyStatusWithContext:completion:]_block_invoke.74
+ ___73-[AKAppleIDPasskeyController verifyAppleIDPasskeyWithContext:completion:]_block_invoke.72
+ ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke_2.cold.9
+ ___73-[AKCarouselAlertClientConnection presentAlertWithDictionary:completion:]_block_invoke.56
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.315
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.315.cold.1
+ ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.316
+ ___75-[AKAppleIDPasskeyController unenrollAppleIDPasskeyWithContext:completion:]_block_invoke.73
+ ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.100
+ ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.100.cold.1
+ ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.258
+ ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.307
+ ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.307.cold.1
+ ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.277
+ ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.270
+ ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.292
+ ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.283
+ ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.269
+ ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.308
+ ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.308.cold.1
+ ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.101
+ ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.101.cold.1
+ ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.267
+ ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.297
+ ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.294
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.329
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.329.cold.1
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.330
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.330.cold.1
+ ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.296
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.313
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.313.cold.1
+ ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.314
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.331
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.331.cold.1
+ ___81-[AKAppleIDAuthenticationController persistMasterKeyVerifier:context:completion:]_block_invoke.310
+ ___81-[AKAppleIDAuthenticationController persistMasterKeyVerifier:context:completion:]_block_invoke.310.cold.1
+ ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.279
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.302
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.302.cold.1
+ ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.303
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.304
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.304.cold.1
+ ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.305
+ ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.306
+ ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.113
+ ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.113.cold.1
+ ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.328
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.248
+ ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.249
+ ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.282
+ ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.289
+ ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.323
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.295
+ ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.295.cold.1
+ ___91-[AKAuthorizationController establishConnectionWithNotificationHandlerEndpoint:completion:]_block_invoke.47
+ ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.288
+ ___93-[AKAuthorizationController establishConnectionWithStateBroadcastHandlerEndpoint:completion:]_block_invoke.48
+ ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.287
+ ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke.271
+ ___AppStoreComponentsLibraryCore_block_invoke
+ ___AppleIDSSOAuthenticationLibraryCore_block_invoke
+ ___block_descriptor_72_e8_32s40s48bs_e38_v24?0"ASCLockupRequest"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.199
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.251
+ ___block_literal_global.261
+ ___block_literal_global.266
+ ___block_literal_global.318
+ ___block_literal_global.322
+ ___block_literal_global.59
+ ___getAIDAServiceOwnersManagerClass_block_invoke
+ ___getAIDAServiceOwnersManagerClass_block_invoke.cold.1
+ ___getAIDAServiceTypeStoreSymbolLoc_block_invoke
+ ___getASCArtworkClass_block_invoke
+ ___getASCArtworkClass_block_invoke.cold.1
+ ___getASCArtworkCropBoundingBoxSymbolLoc_block_invoke
+ ___getASCArtworkDecorationNoneSymbolLoc_block_invoke
+ ___getASCArtworkDecorationRoundedRectSymbolLoc_block_invoke
+ ___getASCArtworkFormatPNGSymbolLoc_block_invoke
+ ___getASCArtworkTemplateKeyCropSymbolLoc_block_invoke
+ ___getASCArtworkTemplateKeyFormatSymbolLoc_block_invoke
+ ___getASCArtworkTemplateKeyHeightSymbolLoc_block_invoke
+ ___getASCArtworkTemplateKeyWidthSymbolLoc_block_invoke
+ ___getASCLockupContextStandardSymbolLoc_block_invoke
+ ___getASCLockupRequestClass_block_invoke
+ ___getASCLockupRequestClass_block_invoke.cold.1
+ ___getASCLockupViewGroupClass_block_invoke
+ ___getASCLockupViewGroupClass_block_invoke.cold.1
+ ___get_ASCLockupKeyIconSymbolLoc_block_invoke
+ ___get_ASCLockupKeyTitleSymbolLoc_block_invoke
+ __baa_sep_app_root_public_key
+ __baa_sep_app_root_skid
+ __baa_sep_app_root_spki
+ __baa_system_root_skid
+ __baa_user_root_skid
+ __mfi4_root_skid
+ __unnamed_array_storage.582
+ _audit_stringDeviceIdentity
+ _getAIDAServiceOwnersManagerClass
+ _getAIDAServiceOwnersManagerClass.softClass
+ _getAIDAServiceTypeStore
+ _getAIDAServiceTypeStore.cold.1
+ _getAIDAServiceTypeStoreSymbolLoc
+ _getAIDAServiceTypeStoreSymbolLoc.ptr
+ _getASCArtworkClass
+ _getASCArtworkClass.softClass
+ _getASCArtworkCropBoundingBox
+ _getASCArtworkCropBoundingBox.cold.1
+ _getASCArtworkCropBoundingBoxSymbolLoc
+ _getASCArtworkCropBoundingBoxSymbolLoc.ptr
+ _getASCArtworkDecorationNone
+ _getASCArtworkDecorationNone.cold.1
+ _getASCArtworkDecorationNoneSymbolLoc
+ _getASCArtworkDecorationNoneSymbolLoc.ptr
+ _getASCArtworkDecorationRoundedRect
+ _getASCArtworkDecorationRoundedRect.cold.1
+ _getASCArtworkDecorationRoundedRectSymbolLoc
+ _getASCArtworkDecorationRoundedRectSymbolLoc.ptr
+ _getASCArtworkFormatPNG
+ _getASCArtworkFormatPNG.cold.1
+ _getASCArtworkFormatPNGSymbolLoc
+ _getASCArtworkFormatPNGSymbolLoc.ptr
+ _getASCArtworkTemplateKeyCrop
+ _getASCArtworkTemplateKeyCrop.cold.1
+ _getASCArtworkTemplateKeyCropSymbolLoc
+ _getASCArtworkTemplateKeyCropSymbolLoc.ptr
+ _getASCArtworkTemplateKeyFormat
+ _getASCArtworkTemplateKeyFormat.cold.1
+ _getASCArtworkTemplateKeyFormatSymbolLoc
+ _getASCArtworkTemplateKeyFormatSymbolLoc.ptr
+ _getASCArtworkTemplateKeyHeight
+ _getASCArtworkTemplateKeyHeight.cold.1
+ _getASCArtworkTemplateKeyHeightSymbolLoc
+ _getASCArtworkTemplateKeyHeightSymbolLoc.ptr
+ _getASCArtworkTemplateKeyWidth
+ _getASCArtworkTemplateKeyWidth.cold.1
+ _getASCArtworkTemplateKeyWidthSymbolLoc
+ _getASCArtworkTemplateKeyWidthSymbolLoc.ptr
+ _getASCLockupContextStandard
+ _getASCLockupContextStandard.cold.1
+ _getASCLockupContextStandardSymbolLoc
+ _getASCLockupContextStandardSymbolLoc.ptr
+ _getASCLockupRequestClass
+ _getASCLockupRequestClass.softClass
+ _getASCLockupViewGroupClass
+ _getASCLockupViewGroupClass.softClass
+ _get_ASCLockupKeyIcon
+ _get_ASCLockupKeyIcon.cold.1
+ _get_ASCLockupKeyIconSymbolLoc
+ _get_ASCLockupKeyIconSymbolLoc.ptr
+ _get_ASCLockupKeyTitle
+ _get_ASCLockupKeyTitle.cold.1
+ _get_ASCLockupKeyTitleSymbolLoc
+ _get_ASCLockupKeyTitleSymbolLoc.ptr
+ _kAKAnalyticsEventBAACachedSigning
+ _kAKAnalyticsEventBAAHostSigning
+ _kAKAnalyticsEventBAASigning
+ _kAKAnalyticsEventContinuationTokenCreate
+ _kAKAnalyticsEventHeartbeatTokenCreate
+ _kAKAnalyticsEventPasswordResetTokenCreate
+ _objc_msgSend$_isSilentBurnCDPRepairEnabledForAccount:
+ _objc_msgSend$_lockupDictionaryForRequest:includingKeys:withCompletionBlock:
+ _objc_msgSend$_lockupRequestForBundleID:withContext:completionBlock:
+ _objc_msgSend$accountForService:
+ _objc_msgSend$aidaServiceOwnermanager
+ _objc_msgSend$altDSIDForAccount:service:
+ _objc_msgSend$credentialWithError:
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$decoration
+ _objc_msgSend$forceSilentBurnCDPRepairEnabled
+ _objc_msgSend$initWithAccountStore:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithObjects:
+ _objc_msgSend$isAccountDeamonConnectionError:
+ _objc_msgSend$isTiburonU13Enabled
+ _objc_msgSend$makeURLWithSubstitutions:
+ _objc_msgSend$setIsSiwaForChildEnabled:
+ _objc_msgSend$setThirdPartyRegulatoryOverride:
+ _objc_msgSend$setUserAgeRange:
- -[AKAccountManager preferredAccountUsingStoreServiceFromAccounts:]
- -[AKAccountManager setBeneficaryLastModified:forAccount:]
- -[AKAccountManager setBeneficaryLastModified:forAccount:].cold.1
- -[AKMediaServicesController _artworkURLFromResult:size:updatingIconContext:]
- -[AKURLBag easyStudentSignInDisabled]
- GCC_except_table114
- GCC_except_table115
- GCC_except_table116
- GCC_except_table118
- GCC_except_table119
- GCC_except_table122
- GCC_except_table141
- GCC_except_table143
- GCC_except_table153
- GCC_except_table156
- GCC_except_table159
- GCC_except_table160
- GCC_except_table161
- GCC_except_table162
- GCC_except_table163
- GCC_except_table166
- GCC_except_table172
- GCC_except_table179
- GCC_except_table190
- GCC_except_table191
- GCC_except_table232
- GCC_except_table237
- GCC_except_table238
- GCC_except_table239
- GCC_except_table240
- GCC_except_table241
- GCC_except_table242
- GCC_except_table243
- GCC_except_table245
- GCC_except_table246
- GCC_except_table247
- GCC_except_table82
- GCC_except_table89
- GCC_except_table93
- _DeviceIdentityLibraryCore
- _OBJC_IVAR_$_AKURLBag._easyStudentSignInDisabled
- __DeviceIdentityCreateHostSignature
- __DeviceIdentityCreateHostSignature.cold.1
- __DeviceIdentityIsSupported
- __DeviceIdentityIsSupported.cold.1
- ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.79
- ___102-[AKWalrusController postWalrusStateUpdateToServerWithContext:urlBagKey:username:password:completion:]_block_invoke.79.cold.1
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forAppleID:completion:]_block_invoke.296
- ___105-[AKAppleIDAuthenticationController updateStateWithExternalAuthenticationResponse:forContext:completion:]_block_invoke.295
- ___45-[AKCarouselAlertClientConnection connection]_block_invoke.52
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.316
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.316.cold.1
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.316.cold.2
- ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.109
- ___61-[AKPrivateEmailController removePrivateEmailKey:completion:]_block_invoke.109.cold.1
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.30
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.30.cold.1
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.30.cold.2
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.cold.1
- ___64-[AKMediaServicesController appIconForBundleID:size:completion:]_block_invoke.cold.2
- ___65-[AKAppleIDAuthenticationController deviceListWithContext:error:]_block_invoke.273
- ___66-[AKAppleIDServerResourceLoadDelegate _signRequestWithBAAHeaders:]_block_invoke_2
- ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.108
- ___66-[AKPrivateEmailController privateEmailListVersionWithCompletion:]_block_invoke.108.cold.1
- ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.104
- ___67-[AKPrivateEmailController getContextForRequestContext:completion:]_block_invoke.104.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.277
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.277.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.278
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.278.cold.1
- ___68-[AKAppleIDAuthenticationController performSilentTTRFor:completion:]_block_invoke.278.cold.2
- ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.102
- ___68-[AKPrivateEmailController fetchPrivateEmailWithContext:completion:]_block_invoke.102.cold.1
- ___69-[AKAppleIDAuthenticationController _authenticationServiceConnection]_block_invoke.324
- ___69-[AKAppleIDAuthenticationController generateLoginCodeWithCompletion:]_block_invoke.288
- ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.106
- ___69-[AKPrivateEmailController deletePrivateEmailDatabaseWithCompletion:]_block_invoke.106.cold.1
- ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.97
- ___69-[AKPrivateEmailController lookupPrivateEmailWithContext:completion:]_block_invoke.97.cold.1
- ___70-[AKAppleIDAuthenticationController deviceListWithContext:completion:]_block_invoke.272
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.318
- ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.111
- ___70-[AKPrivateEmailController listAllPrivateEmailsForAltDSID:completion:]_block_invoke.111.cold.1
- ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.77
- ___70-[AKWalrusController verifyEnableWalrusAllowedWithContext:completion:]_block_invoke.77.cold.1
- ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.101
- ___71-[AKPrivateEmailController registerPrivateEmailWithContext:completion:]_block_invoke.101.cold.1
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.319
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.239
- ___72-[AKAppleIDAuthenticationController authenticateWithContext:completion:]_block_invoke.241
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.306
- ___72-[AKAppleIDAuthenticationController verifyMasterKey:context:completion:]_block_invoke.306.cold.1
- ___72-[AKAppleIDPasskeyController setupAppleIDPasskeyWithContext:completion:]_block_invoke.68
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.329
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.329.cold.1
- ___73-[AKAppleIDAuthenticationController fetchAuthModeWithContext:completion:]_block_invoke.270
- ___73-[AKAppleIDAuthenticationController setAppleIDWithDSID:inUse:forService:]_block_invoke.261
- ___73-[AKAppleIDPasskeyController appleIDPasskeyStatusWithContext:completion:]_block_invoke.73
- ___73-[AKAppleIDPasskeyController verifyAppleIDPasskeyWithContext:completion:]_block_invoke.71
- ___73-[AKCarouselAlertClientConnection presentAlertWithDictionary:completion:]_block_invoke.55
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.312
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.312.cold.1
- ___74-[AKAppleIDAuthenticationController isCreateAppleIDAllowedWithCompletion:]_block_invoke.313
- ___75-[AKAppleIDPasskeyController unenrollAppleIDPasskeyWithContext:completion:]_block_invoke.72
- ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.99
- ___75-[AKPrivateEmailController fetchPrivateEmailForAltDSID:withKey:completion:]_block_invoke.99.cold.1
- ___76-[AKAppleIDAuthenticationController setAppleIDWithAltDSID:inUse:forService:]_block_invoke.255
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.304
- ___76-[AKAppleIDAuthenticationController teardownFollowUpWithContext:completion:]_block_invoke.304.cold.1
- ___77-[AKAppleIDAuthenticationController fetchAuthorizedAppListWithContext:error:]_block_invoke.274
- ___77-[AKAppleIDAuthenticationController getUserInformationForAltDSID:completion:]_block_invoke.267
- ___77-[AKAppleIDAuthenticationController validateLoginCode:forAppleID:completion:]_block_invoke.289
- ___77-[AKAppleIDAuthenticationController warmUpVerificationSessionWithCompletion:]_block_invoke.280
- ___78-[AKAppleIDAuthenticationController getUserInformationWithContext:completion:]_block_invoke.266
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.305
- ___78-[AKAppleIDAuthenticationController renewRecoveryTokenWithContext:completion:]_block_invoke.305.cold.1
- ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.100
- ___78-[AKPrivateEmailController registerPrivateEmailForAltDSID:withKey:completion:]_block_invoke.100.cold.1
- ___79-[AKAppleIDAuthenticationController fetchUserInformationForAltDSID:completion:]_block_invoke.264
- ___79-[AKAppleIDAuthenticationController reportSignOutForAllAppleIDsWithCompletion:]_block_invoke.294
- ___80-[AKAppleIDAuthenticationController performCircleRequestWithContext:completion:]_block_invoke.291
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.326
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.326.cold.1
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.327
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.327.cold.1
- ___80-[AKAppleIDAuthenticationController reportSignOutForAppleID:service:completion:]_block_invoke.293
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.308
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.310
- ___80-[AKAppleIDAuthenticationController validateVettingToken:forAltDSID:completion:]_block_invoke.310.cold.1
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.328
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.328.cold.1
- ___81-[AKAppleIDAuthenticationController persistMasterKeyVerifier:context:completion:]_block_invoke.307
- ___81-[AKAppleIDAuthenticationController persistMasterKeyVerifier:context:completion:]_block_invoke.307.cold.1
- ___82-[AKAppleIDAuthenticationController deleteAuthorizationDatabaseWithAltDSID:error:]_block_invoke.276
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.299
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.299.cold.1
- ___82-[AKAppleIDAuthenticationController getServerUILoadDelegateForAltDSID:completion:]_block_invoke.300
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.301
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.301.cold.1
- ___83-[AKAppleIDAuthenticationController getServerUILoadDelegateWithContext:completion:]_block_invoke.302
- ___83-[AKAppleIDAuthenticationController synchronizeFollowUpItemsForContext:completion:]_block_invoke.303
- ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.112
- ___83-[AKPrivateEmailController fetchSignInWithApplePrivateEmailWithContext:completion:]_block_invoke.112.cold.1
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.325
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.245
- ___85-[AKAppleIDAuthenticationController endProximityAuthenticationForContext:completion:]_block_invoke.246
- ___89-[AKAppleIDAuthenticationController revokeAuthorizationForApplicationWithClientID:error:]_block_invoke.279
- ___90-[AKAppleIDAuthenticationController checkSecurityUpgradeEligibilityForContext:completion:]_block_invoke.286
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.320
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.292
- ___90-[AKAppleIDAuthenticationController performCheckInForAccountWithAltDSID:event:completion:]_block_invoke.292.cold.1
- ___91-[AKAuthorizationController establishConnectionWithNotificationHandlerEndpoint:completion:]_block_invoke.41
- ___92-[AKAppleIDAuthenticationController configurationInfoWithIdentifiers:forAltDSID:completion:]_block_invoke.285
- ___93-[AKAuthorizationController establishConnectionWithStateBroadcastHandlerEndpoint:completion:]_block_invoke.42
- ___94-[AKAppleIDAuthenticationController setConfigurationInfo:forIdentifier:forAltDSID:completion:]_block_invoke.284
- ___96-[AKAppleIDAuthenticationController updateUserInformationForAltDSID:userInformation:completion:]_block_invoke.268
- ___block_descriptor_72_e8_32s40s48bs_e36_v24?0"AMSMediaResult"8"NSError"16ls32l8s48l8s40l8
- ___block_literal_global.189
- ___block_literal_global.219
- ___block_literal_global.221
- ___block_literal_global.248
- ___block_literal_global.258
- ___block_literal_global.260
- ___block_literal_global.313
- ___block_literal_global.315
- ___getAMSBagClass_block_invoke
- ___getAMSBagClass_block_invoke.cold.1
- ___getAMSMediaArtworkClass_block_invoke
- ___getAMSMediaArtworkClass_block_invoke.cold.1
- ___getAMSMediaArtworkCropStyleBoundedBoxSymbolLoc_block_invoke
- ___getAMSMediaArtworkFormatPNGSymbolLoc_block_invoke
- ___getAMSMediaResultClass_block_invoke
- ___getAMSMediaResultClass_block_invoke.cold.1
- ___getAMSMediaTaskClass_block_invoke
- ___getAMSMediaTaskClass_block_invoke.cold.1
- ___getAMSMediaTaskPlatformMacSymbolLoc_block_invoke
- ___getAMSMediaTaskPlatformiPadSymbolLoc_block_invoke
- ___getAMSMediaTaskPlatformiPhoneSymbolLoc_block_invoke
- ___getAMSPromiseClass_block_invoke
- ___getAMSPromiseClass_block_invoke.cold.1
- __unnamed_array_storage.581
- _getAMSBagClass
- _getAMSBagClass.softClass
- _getAMSMediaArtworkClass
- _getAMSMediaArtworkClass.softClass
- _getAMSMediaArtworkCropStyleBoundedBox
- _getAMSMediaArtworkCropStyleBoundedBox.cold.1
- _getAMSMediaArtworkCropStyleBoundedBoxSymbolLoc
- _getAMSMediaArtworkCropStyleBoundedBoxSymbolLoc.ptr
- _getAMSMediaArtworkFormatPNG
- _getAMSMediaArtworkFormatPNG.cold.1
- _getAMSMediaArtworkFormatPNGSymbolLoc
- _getAMSMediaArtworkFormatPNGSymbolLoc.ptr
- _getAMSMediaResultClass
- _getAMSMediaResultClass.softClass
- _getAMSMediaTaskClass
- _getAMSMediaTaskClass.softClass
- _getAMSMediaTaskPlatformMac
- _getAMSMediaTaskPlatformMac.cold.1
- _getAMSMediaTaskPlatformMacSymbolLoc
- _getAMSMediaTaskPlatformMacSymbolLoc.ptr
- _getAMSMediaTaskPlatformiPad
- _getAMSMediaTaskPlatformiPad.cold.1
- _getAMSMediaTaskPlatformiPadSymbolLoc
- _getAMSMediaTaskPlatformiPadSymbolLoc.ptr
- _getAMSMediaTaskPlatformiPhone
- _getAMSMediaTaskPlatformiPhone.cold.1
- _getAMSMediaTaskPlatformiPhoneSymbolLoc
- _getAMSMediaTaskPlatformiPhoneSymbolLoc.ptr
- _getAMSPromiseClass
- _getAMSPromiseClass.softClass
- _getDeviceIdentityCreateHostSignatureSymbolLoc
- _getDeviceIdentityIsSupportedSymbolLoc
- _malloc
- _objc_msgSend$URLWithSize:cropStyle:format:
- _objc_msgSend$_artworkURLFromResult:size:updatingIconContext:
- _objc_msgSend$addFinishBlock:
- _objc_msgSend$artworkDictionary
- _objc_msgSend$bagForProfile:profileVersion:
- _objc_msgSend$bagSubProfile
- _objc_msgSend$bagSubProfileVersion
- _objc_msgSend$initWithType:clientIdentifier:clientVersion:bag:
- _objc_msgSend$perform
- _objc_msgSend$preferredAccountUsingStoreServiceFromAccounts:
- _objc_msgSend$responseDataItems
- _objc_msgSend$setAdditionalPlatforms:
- _objc_msgSend$setBundleIdentifiers:
- _objc_msgSend$setIncludedResultKeys:
- _objc_msgSend$sharedCacheEnabledAnisetteFreeSession
CStrings:
+ "\x04\x11\x11\x11\x12"
+ "\x0e\x16!\x1f\x0f\b"
+ "%.0f"
+ "%{private}@"
+ "/AppleInternal/Library/Frameworks/AppStoreComponents.framework/AppStoreComponents"
+ "/AppleInternal/Library/Frameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication"
+ "/System/Library/Frameworks/AppStoreComponents.framework/AppStoreComponents"
+ "/System/Library/Frameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication"
+ "/System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents"
+ "/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication"
+ "3PRegulatoryOverride"
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tthirdPartyRegulatoryOverride: %@,\n}>"
+ "@\"AIDAServiceOwnersManager\""
+ "@\"AKAccountStore\""
+ "@\"ASCLockupViewGroup\""
+ "@40@0:8@16Q24^@32"
+ "AIDAServiceOwnersManager"
+ "AIDAServiceTypeStore"
+ "AKAccountManagerQueue.read.write"
+ "AKAccountStore"
+ "AKForceSilentBurnCDPRepairEnabled"
+ "AKMediaServicesController Lockup Group"
+ "ASCArtwork"
+ "ASCArtworkCropBoundingBox"
+ "ASCArtworkDecorationNone"
+ "ASCArtworkDecorationRoundedRect"
+ "ASCArtworkFormatPNG"
+ "ASCArtworkTemplateKeyCrop"
+ "ASCArtworkTemplateKeyFormat"
+ "ASCArtworkTemplateKeyHeight"
+ "ASCArtworkTemplateKeyWidth"
+ "ASCLockupContextStandard"
+ "ASCLockupRequest"
+ "ASCLockupViewGroup"
+ "Added additional BAA headers for request - %@"
+ "Adding beneficiaryInfo for UUID: %@"
+ "Allowing underage user to perform request"
+ "Apple owned domains fetched"
+ "Apple owned domains: %@"
+ "Authorize URLs: %@"
+ "BAA is not enabled for URL key - %{public}@"
+ "Begin passcode auth eligibility check"
+ "Checking app SSO request type"
+ "Checking if url is apple owned"
+ "Exception caught when fetching AK3PRegulatoryOverride property: %@"
+ "Exception caught when fetching SiwA enabled property: %@"
+ "Exception caught when fetching silenBurnCDPRepairEnabled property: %@"
+ "Exception caught when setting AK3PRegulatoryOverride property: %@"
+ "Exception caught when setting SiwA enabled property: %@"
+ "Exception caught when setting silenBurnCDPRepairEnabled property: %@"
+ "Failed to fetch lockup dictionary for bundleID %@ with error %@"
+ "Failed to fetch lockup request for bundleID %@ with error %@"
+ "Feature TiburonU13 is supported. Is TiburonU13 enabled - %@"
+ "Fetching apple owned domains..."
+ "Fetching native takeover URLs"
+ "Lockup dictionary result: %@"
+ "Native takeover URLs fetched"
+ "Native takeover URLs: %@"
+ "Retrying Account operations..."
+ "Retrying credential fetch operation..."
+ "Retrying credential fetch with service id..."
+ "Retrying fetching account type operation..."
+ "Setting masking style to AKIconMaskingStyleMasked for artwork decoration style ASCArtworkDecorationRoundedRect"
+ "Setting masking style to AKIconMaskingStyleUnknown for artwork decoration style %@"
+ "Setting masking style to AKIconMaskingStyleUnmasked for artwork decoration style ASCArtworkDecorationNone"
+ "Should process URL called"
+ "Should show authoirzation flow: %@"
+ "Signing request with BAA headers for key - %{public}@"
+ "Silent burn in mini-buddy is force disabled"
+ "Silent burn in mini-buddy is force enabled"
+ "T@\"NSNumber\",C,N,V_isSiwaForChildEnabled"
+ "T@\"NSNumber\",C,N,V_silentEscrowRecordRepairEnabledV2"
+ "T@\"NSNumber\",C,N,V_thirdPartyRegulatoryOverride"
+ "T@\"NSString\",?,R,C"
+ "TB,R,N,GisEasyStudentSignInDisabled"
+ "TB,R,N,GisTiburonU13Enabled"
+ "TQ,N,V_userAgeRange"
+ "TiburonU13"
+ "URL is not apple owned"
+ "URL shouldn't be processed"
+ "_ASCLockupKeyIcon"
+ "_ASCLockupKeyTitle"
+ "_aidaServiceOwnermanager"
+ "_cachedIsTiburonU13Enabled"
+ "_isSilentBurnCDPRepairEnabledForAccount:"
+ "_isSiwAEnabled"
+ "_isSiwaForChildEnabled"
+ "_lockupDictionaryForRequest:includingKeys:withCompletionBlock:"
+ "_lockupRequestForBundleID:withContext:completionBlock:"
+ "_serialQueue"
+ "_silentEscrowRecordRepairEnabledV2"
+ "_thirdPartyRegulatoryOverride"
+ "_userAgeRange"
+ "accountForService:"
+ "aidaServiceOwnermanager"
+ "altDSIDForAccount:service:"
+ "baa-sign-sampling"
+ "baaAnalyticsDisabled"
+ "baaSigningSamplingRate"
+ "ckgen"
+ "com.apple.authkit.baa.signing"
+ "com.apple.authkit.baa.signing.cached"
+ "com.apple.authkit.baa.signing.host"
+ "com.apple.authkit.token.ck.create"
+ "com.apple.authkit.token.hb.create"
+ "com.apple.authkit.token.prk.create"
+ "com.apple.inheritance.cryptoaccess"
+ "credentialForAccount:serviceID:error:"
+ "credentialWithError:"
+ "dataWithContentsOfURL:options:error:"
+ "decoration"
+ "forceSilentBurnCDPRepairEnabled"
+ "get3PRegulatoryOverride:"
+ "initWithAccountStore:"
+ "initWithName:"
+ "initWithObjects:"
+ "isAccountDeamonConnectionError:"
+ "isBAAAnalyticsDisabled"
+ "isSilentBurnCDPRepairEnabledForAccount:"
+ "isSiwaEnabled"
+ "isSiwaEnabledForChildAccount:"
+ "isSiwaForChildEnabled"
+ "isTiburonU13Enabled"
+ "makeURLWithSubstitutions:"
+ "manageSiwaForChildUrl"
+ "set3PRegulatoryOverride:forAccount:"
+ "setBeneficiaryLastModified:forAccount:"
+ "setForceSilentBurnCDPRepairEnabled:"
+ "setIsSiwaEnabled:forChildAccount:"
+ "setIsSiwaForChildEnabled:"
+ "setSilentBurnCDPRepairEnabled:"
+ "setSilentBurnCDPRepairEnabled:forAccount:"
+ "setSilentEscrowRecordRepairEnabledV2:"
+ "setThirdPartyRegulatoryOverride:"
+ "setUserAgeRange:"
+ "silenBurnMiniBuddyEnabled"
+ "silentBurnCDPRepairEnabled"
+ "slt"
+ "softlink:r:path:/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity"
+ "thirdPartyRegulatoryOverride"
+ "tiburonU13Enabled"
+ "userAgeRange"
+ "v24@?0@\"ASCLockupRequest\"8@\"NSError\"16"
+ "wrappedKey"
- "\x03\x11\x11\x11\x11"
- "\x0f\x04!\x1f\x0f\x06"
- "/AppleInternal/Library/Frameworks/DeviceIdentity.framework/DeviceIdentity"
- "/System/Library/Frameworks/DeviceIdentity.framework/DeviceIdentity"
- "/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n}>"
- "@\"ACAccountStore\""
- "@48@0:8@16{CGSize=dd}24@40"
- "AMSBag"
- "AMSMediaArtwork"
- "AMSMediaArtworkCropStyleBoundedBox"
- "AMSMediaArtworkFormatPNG"
- "AMSMediaResult"
- "AMSMediaResult: %@"
- "AMSMediaTask"
- "AMSMediaTask for bundleID %@ artwork resulted in error %@"
- "AMSMediaTaskPlatformMac"
- "AMSMediaTaskPlatformiPad"
- "AMSMediaTaskPlatformiPhone"
- "AMSPromise"
- "Begin passcode auth eligiblity check"
- "Signing request with BAA headers"
- "TB,R,N,GisEasyStudentSignInDisabled,V_easyStudentSignInDisabled"
- "URLWithSize:cropStyle:format:"
- "_artworkURLFromResult:size:updatingIconContext:"
- "_easyStudentSignInDisabled"
- "addFinishBlock:"
- "artwork"
- "artworkDictionary"
- "bagForProfile:profileVersion:"
- "bagSubProfile"
- "bagSubProfileVersion"
- "initWithType:clientIdentifier:clientVersion:bag:"
- "ios"
- "osx"
- "perform"
- "platformAttributes"
- "preferredAccountUsingStoreServiceFromAccounts:"
- "responseDataItems"
- "setAdditionalPlatforms:"
- "setBeneficaryLastModified:forAccount:"
- "setBundleIdentifiers:"
- "setIncludedResultKeys:"
- "v24@?0@\"AMSMediaResult\"8@\"NSError\"16"

```
