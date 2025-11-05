## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Versions/A/PlatformSSO`

```diff

-417.80.4.0.0
-  __TEXT.__text: 0x8fab4
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x3268
-  __TEXT.__const: 0x168
-  __TEXT.__gcc_except_tab: 0x20a0
-  __TEXT.__cstring: 0xbc18
-  __TEXT.__oslogstring: 0x3b6f
+417.100.37.0.0
+  __TEXT.__text: 0x98c1c
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0x3b34
+  __TEXT.__const: 0x180
+  __TEXT.__gcc_except_tab: 0x2070
+  __TEXT.__cstring: 0xc739
+  __TEXT.__oslogstring: 0x3ff2
   __TEXT.__dlopen_cstrs: 0x41a
-  __TEXT.__unwind_info: 0x1990
+  __TEXT.__unwind_info: 0x1b48
   __TEXT.__objc_classname: 0x415
-  __TEXT.__objc_methname: 0xb6bb
-  __TEXT.__objc_methtype: 0x1c26
-  __TEXT.__objc_stubs: 0x9180
-  __DATA_CONST.__got: 0x560
-  __DATA_CONST.__const: 0x5b0
+  __TEXT.__objc_methname: 0xbe12
+  __TEXT.__objc_methtype: 0x1cd6
+  __TEXT.__objc_stubs: 0x9720
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x5c0
   __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28b0
+  __DATA_CONST.__objc_selrefs: 0x2ae0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x760
-  __AUTH_CONST.__const: 0x1a30
-  __AUTH_CONST.__cfstring: 0x56a0
-  __AUTH_CONST.__objc_const: 0x8dd0
-  __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_arraydata: 0xa0
+  __AUTH_CONST.__auth_got: 0x770
+  __AUTH_CONST.__const: 0x1b10
+  __AUTH_CONST.__cfstring: 0x5c60
+  __AUTH_CONST.__objc_const: 0x8138
+  __AUTH_CONST.__objc_intobj: 0x180
+  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0xaa0
-  __DATA.__objc_ivar: 0x340
+  __DATA.__objc_ivar: 0x344
   __DATA.__data: 0x600
   __DATA.__bss: 0x400
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/CryptoTokenKit.framework/Versions/A/CryptoTokenKit
+  - /System/Library/Frameworks/DeviceCheck.framework/Versions/A/DeviceCheck
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/GSS.framework/Versions/A/GSS
   - /System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication

   - /System/Library/PrivateFrameworks/AppSSO.framework/Versions/A/AppSSO
   - /System/Library/PrivateFrameworks/AppSSOCore.framework/Versions/A/AppSSOCore
   - /System/Library/PrivateFrameworks/AppSupport.framework/Versions/A/AppSupport
+  - /System/Library/PrivateFrameworks/DeviceIdentity.framework/Versions/A/DeviceIdentity
   - /System/Library/PrivateFrameworks/Heimdal.framework/Versions/A/Heimdal
   - /System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B86742ED-24F7-390D-853B-0BE123C07C69
-  Functions: 2614
-  Symbols:   6154
-  CStrings:  4231
+  UUID: 14BC3FBF-82A8-3647-A626-FA07531BA88E
+  Functions: 2770
+  Symbols:   6586
+  CStrings:  4424
 
Symbols:
+ +[POAgentProcess retainedContexts].cold.1
+ +[POConfigurationManager sharedInstance].cold.1
+ +[PODaemonConnection xpcQueue].cold.1
+ +[PODaemonProcess _prebootSyncQueue].cold.1
+ +[POServiceConnection xpcQueue].cold.1
+ +[POServiceLoginManagerConnection xpcQueue].cold.1
+ +[POUIServiceConnection xpcQueue].cold.1
+ -[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:].cold.9
+ -[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]
+ -[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:].cold.1
+ -[POAgentAuthenticationProcess faileDevicRegistrationAfterRegistrationWithUserInteraction:]
+ -[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:].cold.4
+ -[POAgentAuthenticationProcess handlePreviousRefreshTokens]
+ -[POAgentAuthenticationProcess handleUserLogOut]
+ -[POAgentAuthenticationProcess handleUserLogOut].cold.1
+ -[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]
+ -[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:].cold.1
+ -[POAgentProcess verifyAgentEntitlement].cold.2
+ -[POAuthPluginProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:]
+ -[POConfigurationManager createTemporaryUser:passwordContext:]
+ -[POConfigurationManager createTemporaryUser:passwordContext:].cold.1
+ -[POConfigurationManager createTemporaryUserLocalAccount:]
+ -[POConfigurationManager createTemporaryUserLocalAccount:].cold.1
+ -[POConfigurationManager resetTemporaryAccount]
+ -[POConfigurationManager resetTemporaryAccount].cold.1
+ -[POConfigurationManager updateTemporaryAccountName:altSecurityIdentity:]
+ -[POConfigurationManager updateTemporaryAccountName:altSecurityIdentity:].cold.1
+ -[PODaemonConnection createTemporaryUser:passwordContext:completion:]
+ -[PODaemonConnection resetTemporaryAccount:]
+ -[PODaemonConnection updateTemporaryAccountName:altSecurityIdentity:completion:]
+ -[PODaemonProcess createAppSSOCachePathWithCompletion:].cold.2
+ -[PODaemonProcess createTemporaryUser:passwordContext:completion:]
+ -[PODaemonProcess resetTemporaryAccount:]
+ -[PODaemonProcess resetTemporaryAccount]
+ -[PODaemonProcess resetTemporaryAccount].cold.1
+ -[PODaemonProcess resetTemporaryAccount].cold.2
+ -[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]
+ -[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:].cold.1
+ -[PODeviceConfiguration(POProfile) updateWithProfile:]
+ -[PODirectoryServices createTemporaryUser:password:error:]
+ -[PODirectoryServices createTemporaryUser:password:error:].cold.1
+ -[PODirectoryServices createTemporaryUser:password:error:].cold.2
+ -[PODirectoryServices findPlatformSSOAltSecurityIdentityForUserName:]
+ -[PODirectoryServices findPlatformSSOAltSecurityIdentityForUserName:].cold.1
+ -[PODirectoryServices isUserPlatformSSOTemporaryUser:]
+ -[PODirectoryServices isUserPlatformSSOTemporaryUser:].cold.1
+ -[PODirectoryServices setFullName:forUser:]
+ -[PODirectoryServices setFullName:forUser:].cold.1
+ -[POExtensionAgentProcess _keyForKeyType:error:]
+ -[POExtensionAgentProcess _keyForKeyType:error:].cold.1
+ -[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]
+ -[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:].cold.1
+ -[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:].cold.2
+ -[POExtensionAgentProcess init]
+ -[POLoginManager attestKey:clientData:completion:]
+ -[POLoginManager attestKey:clientData:completion:].cold.1
+ -[POLoginManager attestPendingKey:clientData:completion:]
+ -[POLoginManager attestPendingKey:clientData:completion:].cold.1
+ -[POLoginProcess authenticateTemporaryPasswordUser]
+ -[POLoginProcess authenticateTemporaryPasswordUser].cold.1
+ -[POLoginProcess authenticateTemporarySmartCardUser]
+ -[POLoginProcess authenticateTemporarySmartCardUser].cold.1
+ -[POProfile allowDeviceIdentifiersInAttestation]
+ -[POProfile setAllowDeviceIdentifiersInAttestation:]
+ -[POServiceConnection authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]
+ -[POServiceLoginManagerConnection attestKey:pending:clientDataHash:completion:]
+ -[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]
+ -[POUnlockProcess handlePasswordAuthenticationForTemporaryUser].cold.1
+ -[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]
+ -[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser].cold.1
+ -[POUnlockProcess unlockIsForTemporaryUser]
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table118
+ GCC_except_table12
+ GCC_except_table122
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table144
+ GCC_except_table152
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table180
+ GCC_except_table190
+ GCC_except_table20
+ GCC_except_table200
+ GCC_except_table240
+ GCC_except_table249
+ GCC_except_table260
+ GCC_except_table261
+ GCC_except_table268
+ GCC_except_table273
+ GCC_except_table314
+ GCC_except_table323
+ GCC_except_table343
+ GCC_except_table557
+ GCC_except_table560
+ GCC_except_table88
+ OBJC_IVAR_$_POProfile._allowDeviceIdentifiersInAttestation
+ PO_LOG_POAgentAuthenticationProcess.cold.1
+ PO_LOG_POAgentListener.cold.1
+ PO_LOG_POAgentProcess.cold.1
+ PO_LOG_POAuthPluginProcess.cold.1
+ PO_LOG_POConfigurationManager.cold.1
+ PO_LOG_POConfigurationUtil.cold.1
+ PO_LOG_PODaemonConnection.cold.1
+ PO_LOG_PODaemonProcess.cold.1
+ PO_LOG_PODirectoryServices.cold.1
+ PO_LOG_POExtension.cold.1
+ PO_LOG_POExtensionAgentProcess.cold.1
+ PO_LOG_POKerberosHelper.cold.1
+ PO_LOG_POLoginManager.cold.1
+ PO_LOG_POLoginProcess.cold.1
+ PO_LOG_POLoginUser.cold.1
+ PO_LOG_POProfile.cold.1
+ PO_LOG_PORemoteUserGroupManager.cold.1
+ PO_LOG_POServiceConnection.cold.1
+ PO_LOG_POServiceLoginManagerConnection.cold.1
+ PO_LOG_POUIServiceConnection.cold.1
+ PO_LOG_POUISettingsManager.cold.1
+ PO_LOG_POUnlockProcess.cold.1
+ PO_LOG_POUserGroupManager.cold.1
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
+ TKUnbindUser.cold.2
+ TKUnlockKeybag.cold.4
+ TKUnlockKeybag.cold.5
+ TKUnlockKeybag.cold.6
+ TKValidateAttributeMatchingConfig.cold.5
+ TKValidateAttributeMatchingConfig.cold.6
+ TKValidateAttributeMatchingConfig.cold.7
+ TKValidateAttributeMatchingConfig.cold.8
+ TKValidateAttributeMatchingConfig.cold.9
+ _NSApp
+ _OBJC_CLASS_$_DCAppAttestDeviceService
+ _POTokenValueShortName
+ _SecCertificateCopyData
+ _SecCertificateCreateWithData
+ __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.949
+ __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.949.cold.1
+ __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.954
+ __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.954.cold.1
+ __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.958
+ __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.958.cold.1
+ __100-[POAgentAuthenticationProcess handleUserAuthorizationNeededForAccountDisplayName:bundleIdentifier:]_block_invoke.536
+ __100-[POAgentAuthenticationProcess handleUserAuthorizationNeededForAccountDisplayName:bundleIdentifier:]_block_invoke.536.cold.1
+ __107-[POAgentProcess performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.52.cold.1
+ __108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.1084
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.345
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.345.cold.1
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.349
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.349.cold.1
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.350
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.350.cold.1
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.351
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.351.cold.1
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.355
+ __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.355.cold.1
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.359
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.359.cold.1
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.360
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.360.cold.1
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.361
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.361.cold.1
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.362
+ __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.362.cold.1
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.255
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.255.cold.1
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.261
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.261.cold.1
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.267
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.267.cold.1
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.273
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.273.cold.1
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.279
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.279.cold.1
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.285
+ __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.285.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.245
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.245.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.248
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.248.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.251
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.252
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.252.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.253
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.253.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.259
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.259.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.265
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.265.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.271
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.271.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.277
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.277.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.280
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.280.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.283
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.283.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.286
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.286.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.289
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.289.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.290
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.290.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.291
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.291.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.cold.1
+ __116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke_2.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.168
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.168.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.172
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.172.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.180
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.180.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.195
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.195.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.203
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.203.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.204
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.204.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.208
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.208.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.212
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.212.cold.1
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.213
+ __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.213.cold.1
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.781
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.781.cold.1
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.787
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.787.cold.1
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.793
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.793.cold.1
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.796
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.796.cold.1
+ __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.802
+ __121-[POServiceConnection authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke.cold.1
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.759
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.759.cold.1
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.765
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.765.cold.1
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.768
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.768.cold.1
+ __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.775
+ __129-[POAgentAuthenticationProcess handleUserCredentialNeededAtLogin:smartCard:accountDisplayName:bundleIdentifier:returningContext:]_block_invoke.523
+ __129-[POAgentAuthenticationProcess handleUserCredentialNeededAtLogin:smartCard:accountDisplayName:bundleIdentifier:returningContext:]_block_invoke.523.cold.1
+ __39-[PODaemonConnection _connectToService]_block_invoke.145
+ __39-[PODaemonConnection _connectToService]_block_invoke.145.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.452
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.452.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.456
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.456.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.460
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.460.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.464
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.464.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.468
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.468.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.473
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.473.cold.1
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.483
+ __40-[PODaemonProcess resetTemporaryAccount]_block_invoke.cold.1
+ __40-[POServiceConnection _connectToService]_block_invoke.94
+ __40-[POServiceConnection _connectToService]_block_invoke.94.cold.1
+ __43-[PODirectoryServices setFullName:forUser:]_block_invoke.107
+ __43-[PODirectoryServices setFullName:forUser:]_block_invoke.107.cold.1
+ __43-[PODirectoryServices setFullName:forUser:]_block_invoke.cold.1
+ __44-[PODaemonConnection resetTemporaryAccount:]_block_invoke.cold.1
+ __47-[PODirectoryServices setPasswordHint:forUser:]_block_invoke.111
+ __47-[PODirectoryServices setPasswordHint:forUser:]_block_invoke.111.cold.1
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.10
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.10.cold.1
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.18
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.18.cold.1
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.29
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.29.cold.1
+ __48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke.cold.1
+ __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke.129
+ __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke.94
+ __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke_2.130
+ __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke_2.130.cold.1
+ __50-[POAgentAuthenticationProcess showRegistrationUI]_block_invoke.452
+ __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.131
+ __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.131.cold.1
+ __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.131.cold.2
+ __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.131.cold.3
+ __51-[POLoginProcess authenticateTemporaryPasswordUser]_block_invoke.51
+ __51-[POLoginProcess authenticateTemporaryPasswordUser]_block_invoke.51.cold.1
+ __51-[POLoginProcess authenticateTemporaryPasswordUser]_block_invoke.cold.1
+ __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.261
+ __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.261.cold.1
+ __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.265
+ __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.265.cold.1
+ __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.269
+ __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.269.cold.1
+ __52-[POLoginProcess authenticateTemporarySmartCardUser]_block_invoke.36
+ __52-[POLoginProcess authenticateTemporarySmartCardUser]_block_invoke.36.cold.1
+ __52-[POLoginProcess authenticateTemporarySmartCardUser]_block_invoke.43
+ __52-[POLoginProcess authenticateTemporarySmartCardUser]_block_invoke.43.cold.1
+ __52-[POLoginProcess authenticateTemporarySmartCardUser]_block_invoke.cold.1
+ __52-[POServiceLoginManagerConnection _connectToService]_block_invoke.94
+ __52-[POServiceLoginManagerConnection _connectToService]_block_invoke.94.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.627
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.627.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.634
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.634.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.643
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.643.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.649
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.649.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.655
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.655.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.661
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.665
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.665.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.671
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.671.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.677
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.677.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.681
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.681.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.693
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.693.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.699
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.716
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.734
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.736
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.736.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.709
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.709.cold.1
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.720
+ __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.720.cold.1
+ __54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.1015
+ __54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.1015.cold.1
+ __54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.432
+ __54-[PODirectoryServices isUserPlatformSSOTemporaryUser:]_block_invoke.cold.1
+ __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.597
+ __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.597.cold.1
+ __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.601
+ __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.601.cold.1
+ __55-[POConfigurationManager tokensForExtensionIdentifier:]_block_invoke.227
+ __55-[POConfigurationManager tokensForExtensionIdentifier:]_block_invoke.227.cold.1
+ __55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.442
+ __55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.442.cold.1
+ __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.450
+ __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.450.cold.1
+ __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.454
+ __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.454.cold.1
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.545
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.549
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.564
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.564.cold.1
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.570.cold.1
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.576
+ __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.580
+ __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.400
+ __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.400.cold.1
+ __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.403
+ __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.403.cold.1
+ __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.404
+ __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.404.cold.1
+ __58-[POConfigurationManager createTemporaryUserLocalAccount:]_block_invoke.195
+ __58-[POConfigurationManager createTemporaryUserLocalAccount:]_block_invoke.195.cold.1
+ __58-[POConfigurationManager createTemporaryUserLocalAccount:]_block_invoke.202
+ __58-[POConfigurationManager createTemporaryUserLocalAccount:]_block_invoke.202.cold.1
+ __58-[POConfigurationManager createTemporaryUserLocalAccount:]_block_invoke.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.228
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.228.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.229
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.229.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.230
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.230.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.234
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.234.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.238
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.238.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.249
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.249.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.250
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.250.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.251
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.251.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.252
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.252.cold.1
+ __58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke.cold.1
+ __58-[PODirectoryServices verifyLocalAccountPassword:forUser:]_block_invoke.27
+ __58-[PODirectoryServices verifyLocalAccountPassword:forUser:]_block_invoke.27.cold.1
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.478
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.478.cold.1
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.481
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.481.cold.1
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.482
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.482.cold.1
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.485
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.485.cold.1
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.488
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.488.cold.1
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.494
+ __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.494.cold.1
+ __59-[POAgentAuthenticationProcess finishRegistrationWithRetry]_block_invoke.751
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.319
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.319.cold.1
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.325
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.325.cold.1
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.331
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.331.cold.1
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.337
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.337.cold.1
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.337.cold.2
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.338
+ __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.338.cold.1
+ __59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.969
+ __59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.969.cold.1
+ __59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke.cold.1
+ __60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.995
+ __60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.995.cold.1
+ __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.1019
+ __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.1019.cold.1
+ __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.1025
+ __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.1025.cold.1
+ __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.1031
+ __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.124
+ __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.124.cold.1
+ __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.128
+ __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.128.cold.1
+ __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.132
+ __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.132.cold.1
+ __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.87
+ __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.87.cold.1
+ __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.95
+ __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.95.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.273
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.273.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.280
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.280.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.281
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.281.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.282
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.282.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.286
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.286.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.287
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.287.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.297
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.297.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.301
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.301.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.305
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.305.cold.1
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.309
+ __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.309.cold.1
+ __62-[POAgentAuthenticationProcess showAlertWithError:completion:]_block_invoke.381
+ __62-[PODirectoryServices setPlatformSSOUniqueIdentifier:forUser:]_block_invoke.103
+ __62-[PODirectoryServices setPlatformSSOUniqueIdentifier:forUser:]_block_invoke.103.cold.1
+ __62-[PODirectoryServices setPlatformSSOUniqueIdentifier:forUser:]_block_invoke.99
+ __62-[PODirectoryServices setPlatformSSOUniqueIdentifier:forUser:]_block_invoke.99.cold.1
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.405
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.405.cold.1
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.409
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.409.cold.1
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.413
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.413.cold.1
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.417
+ __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.417.cold.1
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.16
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.16.cold.1
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.25
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.25.cold.1
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.33
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.33.cold.1
+ __63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke.cold.1
+ __64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.470
+ __64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.470.cold.1
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.41
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.41.cold.1
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.47
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.47.cold.1
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.51
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.51.cold.1
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.58
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.58.cold.1
+ __64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke.cold.1
+ __65-[PODirectoryServices removePlatformSSOAdminGroupReturningError:]_block_invoke.322
+ __65-[PODirectoryServices removePlatformSSOAdminGroupReturningError:]_block_invoke.322.cold.1
+ __66-[PODaemonProcess createTemporaryUser:passwordContext:completion:]_block_invoke.cold.1
+ __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.821
+ __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke_2.cold.1
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.415
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.415.cold.1
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.418
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.418.cold.1
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.419
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.419.cold.1
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.425
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.425.cold.1
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.431
+ __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.431.cold.1
+ __67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.373
+ __67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.377
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.179.cold.1
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.183
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.183.cold.1
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.187
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.208
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.208.cold.1
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.221
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.232
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.235
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.238
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.238.cold.1
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.242
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.242.cold.1
+ __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.248
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.836
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.836.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.842
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.842.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.848
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.848.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.854
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.854.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.860
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.860.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.866
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.866.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.872
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.872.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.878
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.878.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.881
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.884
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke.cold.1
+ __68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke_2.885
+ __68-[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:]_block_invoke.352
+ __68-[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:]_block_invoke.352.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.509
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.509.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.513
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.513.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.519
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.519.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.524
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.524.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.530
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.530.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.536
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.536.cold.1
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.542
+ __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.542.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.505
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.505.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.508
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.508.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.509
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.509.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.512
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.512.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.515
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.515.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.519
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.519.cold.1
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.522
+ __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.522.cold.1
+ __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.981
+ __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.981.cold.1
+ __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.987
+ __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.987.cold.1
+ __69-[PODaemonConnection createTemporaryUser:passwordContext:completion:]_block_invoke.cold.1
+ __69-[PODirectoryServices findPlatformSSOAltSecurityIdentityForUserName:]_block_invoke.cold.1
+ __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.155
+ __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.155.cold.1
+ __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.161
+ __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.161.cold.1
+ __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.168
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.427
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.427.cold.1
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.431
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.431.cold.1
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.436
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.436.cold.1
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.440
+ __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.440.cold.1
+ __70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.389
+ __71-[POConfigurationManager setTokens:extensionIdentifier:returningError:]_block_invoke.236
+ __71-[POConfigurationManager setTokens:extensionIdentifier:returningError:]_block_invoke.236.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.318
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.318.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.325
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.325.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.331
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.331.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.335
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.335.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.341
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.341.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.352
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.352.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.356
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.356.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.362
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.362.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke.cold.1
+ __71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke_2.cold.1
+ __72-[POAgentAuthenticationProcess showAlertMessage:messageText:completion:]_block_invoke.379
+ __72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.297
+ __72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.297.cold.1
+ __72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.383
+ __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.465
+ __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.465.cold.1
+ __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.471
+ __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.471.cold.1
+ __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.477
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.329
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.329.cold.1
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.331
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.331.cold.1
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.336
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.336.cold.1
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.340
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.340.cold.1
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.344
+ __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.344.cold.1
+ __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.139
+ __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.139.cold.1
+ __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.143
+ __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.143.cold.1
+ __77-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.491
+ __77-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.491.cold.1
+ __77-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.497
+ __77-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.497.cold.1
+ __77-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.cold.1
+ __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.51
+ __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.51.cold.1
+ __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.52
+ __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.52.cold.1
+ __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.84
+ __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.84.cold.1
+ __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.91
+ __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.91.cold.1
+ __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.370
+ __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.370.cold.1
+ __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.376
+ __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.377
+ __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.153
+ __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.153.cold.1
+ __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.157
+ __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.157.cold.1
+ __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.161
+ __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.161.cold.1
+ __79-[POServiceLoginManagerConnection attestKey:pending:clientDataHash:completion:]_block_invoke.cold.1
+ __80-[PODaemonConnection updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke.cold.1
+ __81-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:atLogin:]_block_invoke.73
+ __81-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:atLogin:]_block_invoke.73.cold.1
+ __81-[POAgentAuthenticationProcess requestUserAuthenticationSyncPassword:completion:]_block_invoke.357
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.908
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.908.cold.1
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.912
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.912.cold.1
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.918
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.918.cold.1
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.924
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.924.cold.1
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.930
+ __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.930.cold.1
+ __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.142
+ __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.142.cold.1
+ __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.146
+ __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.146.cold.1
+ __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.31
+ __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.31.cold.1
+ __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.39
+ __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.39.cold.1
+ __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.41
+ __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.41.cold.1
+ __91-[POAgentAuthenticationProcess requestSmartCardForBinding:tokenId:tokenHash:wrapTokenHash:]_block_invoke.361
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.254
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.254.cold.1
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.266
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.266.cold.1
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.270
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.270.cold.1
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.274
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.274.cold.1
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.278
+ __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.278.cold.1
+ __98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.896
+ __98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.896.cold.1
+ __98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.902
+ __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.299
+ __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.299.cold.1
+ __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.303
+ __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.303.cold.1
+ __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.309
+ __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.309.cold.1
+ __MergedGlobals
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_PODeviceConfiguration_$_POProfile
+ __OBJC_$_CATEGORY_PODeviceConfiguration_$_POProfile
+ ___110-[POAuthPluginProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:]_block_invoke
+ ___110-[POAuthPluginProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:]_block_invoke_2
+ ___116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke
+ ___116-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke_2
+ ___121-[POServiceConnection authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]_block_invoke
+ ___40-[PODaemonProcess resetTemporaryAccount]_block_invoke
+ ___43-[PODirectoryServices setFullName:forUser:]_block_invoke
+ ___44-[PODaemonConnection resetTemporaryAccount:]_block_invoke
+ ___45-[PODaemonProcess handleConfigurationChanged]_block_invoke
+ ___47-[POConfigurationManager resetTemporaryAccount]_block_invoke
+ ___48-[POAgentAuthenticationProcess handleUserLogOut]_block_invoke
+ ___48-[POExtensionAgentProcess _keyForKeyType:error:]_block_invoke
+ ___50-[POLoginManager attestKey:clientData:completion:]_block_invoke
+ ___50-[POLoginManager attestKey:clientData:completion:]_block_invoke_2
+ ___51-[POLoginProcess authenticateTemporaryPasswordUser]_block_invoke
+ ___52-[POLoginProcess authenticateTemporarySmartCardUser]_block_invoke
+ ___54-[PODirectoryServices isUserPlatformSSOTemporaryUser:]_block_invoke
+ ___57-[POLoginManager attestPendingKey:clientData:completion:]_block_invoke
+ ___57-[POLoginManager attestPendingKey:clientData:completion:]_block_invoke_2
+ ___58-[POConfigurationManager createTemporaryUserLocalAccount:]_block_invoke
+ ___58-[PODirectoryServices createTemporaryUser:password:error:]_block_invoke
+ ___59-[POAgentAuthenticationProcess handlePreviousRefreshTokens]_block_invoke
+ ___62-[POConfigurationManager createTemporaryUser:passwordContext:]_block_invoke
+ ___63-[POUnlockProcess handlePasswordAuthenticationForTemporaryUser]_block_invoke
+ ___64-[POUnlockProcess handleSmartCardAuthenticationForTemporaryUser]_block_invoke
+ ___66-[PODaemonProcess createTemporaryUser:passwordContext:completion:]_block_invoke
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke
+ ___68-[POAgentAuthenticationProcess _handleConfigurationChanged:startup:]_block_invoke_2
+ ___69-[PODaemonConnection createTemporaryUser:passwordContext:completion:]_block_invoke
+ ___69-[PODirectoryServices findPlatformSSOAltSecurityIdentityForUserName:]_block_invoke
+ ___71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke
+ ___71-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]_block_invoke_2
+ ___73-[POConfigurationManager updateTemporaryAccountName:altSecurityIdentity:]_block_invoke
+ ___77-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke
+ ___79-[POServiceLoginManagerConnection attestKey:pending:clientDataHash:completion:]_block_invoke
+ ___80-[PODaemonConnection updateTemporaryAccountName:altSecurityIdentity:completion:]_block_invoke
+ ___91-[POAgentAuthenticationProcess faileDevicRegistrationAfterRegistrationWithUserInteraction:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_42_e8_32s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e5_v8?0l
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e69_v56?0Q8"NSData"16"NSString"24"NSArray"32"NSString"40"NSError"48l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s
+ ___soft_CP_GetBootstrapTokenWithOptions
+ ___soft_CP_SupportsBootstrapToken
+ __block_literal_global.128
+ __block_literal_global.137
+ __block_literal_global.1496
+ __block_literal_global.1500
+ __block_literal_global.159
+ __block_literal_global.163
+ __block_literal_global.224
+ __block_literal_global.234
+ __block_literal_global.241
+ __block_literal_global.392
+ __block_literal_global.40
+ __block_literal_global.443
+ __block_literal_global.447
+ __block_literal_global.482
+ __block_literal_global.485
+ __block_literal_global.548
+ __block_literal_global.730
+ __block_literal_global.766
+ __block_literal_global.804
+ __block_literal_global.935
+ __getSystemVolumeUuid_block_invoke.cold.5
+ __getSystemVolumeUuid_block_invoke.cold.6
+ __getSystemVolumeUuid_block_invoke.cold.7
+ __getSystemVolumeUuid_block_invoke.cold.8
+ __getUidForAgent_block_invoke.cold.4
+ __getUidForAgent_block_invoke.cold.5
+ __soft_CP_GetBootstrapTokenWithOptions.cold.1
+ __soft_CP_SupportsBootstrapToken.cold.1
+ _kMAOptionsBAANetworkTimeoutInterval
+ _kMAOptionsBAANonce
+ _kMAOptionsBAAOIDEDANonce
+ _kMAOptionsBAAOIDEDASerialNumber
+ _kMAOptionsBAAOIDEDAUDID
+ _kMAOptionsBAAOIDSToInclude
+ _kMAOptionsBAAPerformOperationsOverIPC
+ _kMAOptionsBAAValidity
+ _kPlatformSSOAltSecurityIdPrefix
+ _kPlatformSSOTemporaryAccount
+ _kTemporaryUserAccountName
+ _kTemporaryUserFullName
+ _objc_msgSend$_checkForCachedAttestationForExtensionIdentifier:keyHash:
+ _objc_msgSend$_deleteAllCachedAttestations
+ _objc_msgSend$_deleteCachedAttestationForExtensionIdentifier:key:
+ _objc_msgSend$_handleConfigurationChanged:startup:
+ _objc_msgSend$_keyForKeyType:error:
+ _objc_msgSend$_saveAttestationToKeychain:extensionIdentifier:keyHash:error:
+ _objc_msgSend$_savePendingSSOTokensData:forIdentifier:error:
+ _objc_msgSend$_saveStashedSSOTokensData:forIdentifier:error:
+ _objc_msgSend$activateIgnoringOtherApps:
+ _objc_msgSend$allowDeviceIdentifiersInAttestation
+ _objc_msgSend$attestKey:clientDataHash:options:completionHandler:
+ _objc_msgSend$attestKey:pending:clientDataHash:completion:
+ _objc_msgSend$authenticateTemporaryPasswordUser
+ _objc_msgSend$authenticateTemporarySmartCardUser
+ _objc_msgSend$authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:
+ _objc_msgSend$authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:
+ _objc_msgSend$createTemporaryUser:password:error:
+ _objc_msgSend$createTemporaryUser:passwordContext:
+ _objc_msgSend$createTemporaryUser:passwordContext:completion:
+ _objc_msgSend$createTemporaryUserLocalAccount:
+ _objc_msgSend$decryptTemporaryAccountCredential
+ _objc_msgSend$encryptAndSaveTemporaryAccountCredential:
+ _objc_msgSend$faileDevicRegistrationAfterRegistrationWithUserInteraction:
+ _objc_msgSend$findPlatformSSOAltSecurityIdentityForUserName:
+ _objc_msgSend$handlePasswordAuthenticationForTemporaryUser
+ _objc_msgSend$handlePreviousRefreshTokens
+ _objc_msgSend$handleSmartCardAuthenticationForTemporaryUser
+ _objc_msgSend$includePreviousRefreshTokenInLoginRequest
+ _objc_msgSend$isConfigurationActiveForExtensionIdentifier:completion:
+ _objc_msgSend$isSupported
+ _objc_msgSend$isTemporaryAccountUserName:
+ _objc_msgSend$isUserPlatformSSOTemporaryUser:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$platformSSOProfile
+ _objc_msgSend$publicKeyHashForKey:
+ _objc_msgSend$removeTokensFromKeychainWithService:username:system:
+ _objc_msgSend$resetTemporaryAccount
+ _objc_msgSend$resetTemporaryAccount:
+ _objc_msgSend$retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:
+ _objc_msgSend$setAllowDeviceIdentifiersInAttestation:
+ _objc_msgSend$setContextBool:withFlags:forKey:
+ _objc_msgSend$setFullName:forUser:
+ _objc_msgSend$sharedService
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$supportsCreateTemporaryUsers
+ _objc_msgSend$unlockIsForTemporaryUser
+ _objc_msgSend$updateTemporaryAccountName:altSecurityIdentity:
+ _objc_msgSend$updateTemporaryAccountName:altSecurityIdentity:completion:
+ _objc_msgSend$updateWithProfile:
+ binderWorker.cold.5
+ binderWorker.cold.6
+ binderWorker.cold.7
+ binderWorker.cold.8
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
+ getUidForAgent.cold.1
+ isEnforcementOverriden.cold.1
+ isEnforcementOverriden.cold.2
+ isMemberOfGroup.cold.5
+ isMemberOfGroup.cold.6
+ isMemberOfGroup.cold.7
+ isMemberOfGroup.cold.8
+ setupConnection.cold.2
+ setupConnection.cold.3
- -[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:].cold.2
- -[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:].cold.3
- -[POExtensionAgentProcess attestKey:clientDataHash:completion:]
- -[POExtensionAgentProcess attestKey:clientDataHash:completion:].cold.1
- -[POExtensionAgentProcess copyDeviceAttestationCertificateWithCompletion:]
- -[POExtensionAgentProcess copyDeviceAttestationCertificateWithCompletion:].cold.1
- -[POLoginManager attestKey:clientDataHash:completion:]
- -[POLoginManager attestKey:clientDataHash:completion:].cold.1
- -[POLoginManager copyDeviceAttestationCertificate]
- -[POLoginManager copyDeviceAttestationCertificate].cold.1
- -[POServiceLoginManagerConnection attestKey:clientDataHash:completion:]
- -[POServiceLoginManagerConnection copyDeviceAttestationCertificateWithCompletion:]
- GCC_except_table101
- GCC_except_table114
- GCC_except_table116
- GCC_except_table120
- GCC_except_table126
- GCC_except_table127
- GCC_except_table128
- GCC_except_table131
- GCC_except_table132
- GCC_except_table137
- GCC_except_table151
- GCC_except_table160
- GCC_except_table162
- GCC_except_table173
- GCC_except_table179
- GCC_except_table182
- GCC_except_table238
- GCC_except_table247
- GCC_except_table258
- GCC_except_table259
- GCC_except_table266
- GCC_except_table290
- GCC_except_table298
- GCC_except_table321
- GCC_except_table40
- GCC_except_table54
- GCC_except_table543
- GCC_except_table546
- GCC_except_table6
- GCC_except_table63
- TKCopyTokenEndpoints.cold.1
- __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.920
- __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.920.cold.1
- __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.925
- __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.925.cold.1
- __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.929
- __100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.929.cold.1
- __100-[POAgentAuthenticationProcess handleScreenUnlockWithCredentialContext:tokenId:atLogin:tokenUnlock:]_block_invoke.68
- __100-[POAgentAuthenticationProcess handleScreenUnlockWithCredentialContext:tokenId:atLogin:tokenUnlock:]_block_invoke.cold.1
- __100-[POAgentAuthenticationProcess handleUserAuthorizationNeededForAccountDisplayName:bundleIdentifier:]_block_invoke.526
- __100-[POAgentAuthenticationProcess handleUserAuthorizationNeededForAccountDisplayName:bundleIdentifier:]_block_invoke.526.cold.1
- __108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.1044
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.296
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.296.cold.1
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.300
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.300.cold.1
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.301
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.301.cold.1
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.302
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.302.cold.1
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.306
- __111-[PODirectoryServices _setGroups:groupNodeType:groupNodeName:forUser:userNodeType:userNodeName:returningError:]_block_invoke.306.cold.1
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.310
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.310.cold.1
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.311
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.311.cold.1
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.312
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.312.cold.1
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.313
- __113-[PODirectoryServices isUser:userNodeType:userNodeName:memberofGroup:groupNodeType:groupNodeName:returningError:]_block_invoke.313.cold.1
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.247
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.247.cold.1
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.253
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.253.cold.1
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.259
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.259.cold.1
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.265
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.265.cold.1
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.271
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.271.cold.1
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.277
- __114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.277.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.157
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.157.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.161
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.161.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.169
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.169.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.173
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.173.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.192
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.192.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.193
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.193.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.197
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.197.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.201
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.201.cold.1
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.202
- __118-[PODirectoryServices createUser:password:name:loginUserName:recordUUID:idpIdentifier:returningCreatedUserName:error:]_block_invoke.202.cold.1
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.773
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.773.cold.1
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.779
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.779.cold.1
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.785
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.785.cold.1
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.788
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.788.cold.1
- __119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.794
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.751
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.751.cold.1
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.757
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.757.cold.1
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.760
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.760.cold.1
- __123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.767
- __129-[POAgentAuthenticationProcess handleUserCredentialNeededAtLogin:smartCard:accountDisplayName:bundleIdentifier:returningContext:]_block_invoke.513
- __129-[POAgentAuthenticationProcess handleUserCredentialNeededAtLogin:smartCard:accountDisplayName:bundleIdentifier:returningContext:]_block_invoke.513.cold.1
- __39-[PODaemonConnection _connectToService]_block_invoke.142
- __39-[PODaemonConnection _connectToService]_block_invoke.142.cold.1
- __40-[POServiceConnection _connectToService]_block_invoke.91
- __40-[POServiceConnection _connectToService]_block_invoke.91.cold.1
- __47-[PODirectoryServices setPasswordHint:forUser:]_block_invoke.100
- __47-[PODirectoryServices setPasswordHint:forUser:]_block_invoke.100.cold.1
- __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke.122
- __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke.98
- __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke_2.123
- __50-[POAgentAuthenticationProcess handleAgentStartup]_block_invoke_2.123.cold.1
- __50-[POAgentAuthenticationProcess showRegistrationUI]_block_invoke.442
- __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.126
- __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.126.cold.1
- __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.126.cold.2
- __51-[POAgentAuthenticationProcess handleNetworkChange]_block_invoke.126.cold.3
- __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.214
- __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.214.cold.1
- __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.218
- __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.218.cold.1
- __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.222
- __52-[PODirectoryServices _removeAllPlatformSSORecords:]_block_invoke.222.cold.1
- __52-[POServiceLoginManagerConnection _connectToService]_block_invoke.96
- __52-[POServiceLoginManagerConnection _connectToService]_block_invoke.96.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.619
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.619.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.626
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.626.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.635
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.635.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.641
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.641.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.647
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.647.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.653
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.657
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.657.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.663
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.663.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.669
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.669.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.673
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.673.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.685
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.685.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.691
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.700
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.720
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.720.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.726
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.701
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.701.cold.1
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.712
- __54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.712.cold.1
- __54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.975
- __54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.975.cold.1
- __54-[PODaemonProcess saveAppSSOConfiguration:completion:]_block_invoke.427
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.10
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.10.cold.1
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.18
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.18.cold.1
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.29
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.29.cold.1
- __54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke.cold.1
- __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.589
- __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.589.cold.1
- __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.593
- __55-[POAgentAuthenticationProcess requestSmartCardForUser]_block_invoke.593.cold.1
- __55-[POConfigurationManager tokensForExtensionIdentifier:]_block_invoke.209
- __55-[POConfigurationManager tokensForExtensionIdentifier:]_block_invoke.209.cold.1
- __55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.388
- __55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.388.cold.1
- __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.396
- __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.396.cold.1
- __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.400
- __55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.400.cold.1
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.535
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.539
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.544
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.544.cold.1
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.550
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.550.cold.1
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.566
- __56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.577
- __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.346
- __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.346.cold.1
- __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.349
- __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.349.cold.1
- __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.350
- __57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.350.cold.1
- __58-[PODirectoryServices verifyLocalAccountPassword:forUser:]_block_invoke.21
- __58-[PODirectoryServices verifyLocalAccountPassword:forUser:]_block_invoke.21.cold.1
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.424
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.424.cold.1
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.427
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.427.cold.1
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.428
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.428.cold.1
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.431
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.431.cold.1
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.434
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.434.cold.1
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.440
- __58-[POExtensionAgentProcess rotateKeyForKeyType:completion:]_block_invoke.440.cold.1
- __59-[POAgentAuthenticationProcess finishRegistrationWithRetry]_block_invoke.743
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.311
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.311.cold.1
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.317
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.317.cold.1
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.323
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.323.cold.1
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.329
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.329.cold.1
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.329.cold.2
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.330
- __59-[POAgentAuthenticationProcess handleEncryptionKeyRotation]_block_invoke.330.cold.1
- __60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.955
- __60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.955.cold.1
- __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.979
- __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.979.cold.1
- __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.985
- __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.985.cold.1
- __60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.991
- __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.113
- __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.113.cold.1
- __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.117
- __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.117.cold.1
- __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.121
- __60-[PODirectoryServices removePlatformSSOUser:returningError:]_block_invoke.121.cold.1
- __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.84
- __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.84.cold.1
- __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.92
- __60-[PODirectoryServices setAltSecurityIdentity:forIdentifier:]_block_invoke.92.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.226
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.226.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.233
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.233.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.234
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.234.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.235
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.235.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.239
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.239.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.240
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.240.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.248
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.248.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.252
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.252.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.256
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.256.cold.1
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.260
- __61-[PODirectoryServices createOrUpdateAdminGroups:otherGroups:]_block_invoke.260.cold.1
- __62-[POAgentAuthenticationProcess showAlertWithError:completion:]_block_invoke.373
- __62-[PODirectoryServices setPlatformSSOUniqueIdentifier:forUser:]_block_invoke.96
- __62-[PODirectoryServices setPlatformSSOUniqueIdentifier:forUser:]_block_invoke.96.cold.1
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.379
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.379.cold.1
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.385
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.385.cold.1
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.393
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.403.cold.1
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.407
- __63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.407.cold.1
- __64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.416
- __64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.416.cold.1
- __65-[PODirectoryServices removePlatformSSOAdminGroupReturningError:]_block_invoke.273
- __65-[PODirectoryServices removePlatformSSOAdminGroupReturningError:]_block_invoke.273.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.813
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.813.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.819
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.819.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.831
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.831.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.837
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.837.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.843
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.843.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.849
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.849.cold.1
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.852
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke.855
- __67-[POAgentAuthenticationProcess handleConfigurationChanged:startup:]_block_invoke_2.856
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.361
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.361.cold.1
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.364
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.364.cold.1
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.365
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.365.cold.1
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.371
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.371.cold.1
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.377
- __67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.377.cold.1
- __67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.319
- __67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.323
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.167
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.167.cold.1
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.171
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.171.cold.1
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.200
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.200.cold.1
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.213
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.224
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.227
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.230
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.230.cold.1
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.234
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.234.cold.1
- __68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.240
- __68-[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:]_block_invoke.344
- __68-[POAgentAuthenticationProcess handleKeyUpdatesWithPasswordContext:]_block_invoke.344.cold.1
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.450
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.450.cold.1
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.454
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.454.cold.1
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.460
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.460.cold.1
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.465
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.465.cold.1
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.471
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.471.cold.1
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.478
- __68-[PODaemonProcess _configurationChanged:removedExtensionIdentifier:]_block_invoke.478.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.451.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.454
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.454.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.455
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.455.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.458
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.458.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.461
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.461.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.465
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.465.cold.1
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.468
- __68-[POExtensionAgentProcess completeRotationKeyForKeyType:completion:]_block_invoke.468.cold.1
- __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.938
- __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.938.cold.1
- __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.944
- __69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.944.cold.1
- __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.147
- __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.147.cold.1
- __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.153
- __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.153.cold.1
- __70-[POAgentAuthenticationProcess _doRefreshWithPasswordContext:tokenId:]_block_invoke.160
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.417
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.417.cold.1
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.421
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.421.cold.1
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.426
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.426.cold.1
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.430
- __70-[POAgentAuthenticationProcess handleTokenBindingWithPasswordContext:]_block_invoke.430.cold.1
- __70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.335
- __71-[POConfigurationManager setTokens:extensionIdentifier:returningError:]_block_invoke.218
- __71-[POConfigurationManager setTokens:extensionIdentifier:returningError:]_block_invoke.218.cold.1
- __71-[POServiceLoginManagerConnection attestKey:clientDataHash:completion:]_block_invoke.cold.1
- __72-[POAgentAuthenticationProcess showAlertMessage:messageText:completion:]_block_invoke.371
- __72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.248
- __72-[POAgentProcess _saveCredentialForUserName:passwordContext:completion:]_block_invoke.248.cold.1
- __72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.329
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.445
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.445.cold.1
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.451
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.451.cold.1
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.467
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.280
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.280.cold.1
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.282
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.282.cold.1
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.287
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.287.cold.1
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.291
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.291.cold.1
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.295
- __74-[PODirectoryServices _updateSearchPolicyToAddPlatformSSO:returningError:]_block_invoke.295.cold.1
- __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.128
- __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.128.cold.1
- __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.132
- __74-[PODirectoryServices addRecord:toGroup:nodeType:nodeName:returningError:]_block_invoke.132.cold.1
- __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.45
- __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.45.cold.1
- __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.46
- __78-[PODirectoryServices _setLocalAccountPasswordForUser:newPassword:node:error:]_block_invoke.46.cold.1
- __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.88
- __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.88.cold.1
- __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.95
- __79-[POAgentAuthenticationProcess _doUnlockForTokenWithCredentialContext:atLogin:]_block_invoke.95.cold.1
- __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.362
- __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.362.cold.1
- __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.368
- __79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.369
- __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.142
- __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.142.cold.1
- __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.146
- __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.146.cold.1
- __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.150
- __79-[PODirectoryServices removeRecord:fromGroup:nodeType:nodeName:returningError:]_block_invoke.150.cold.1
- __81-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:atLogin:]_block_invoke.77
- __81-[POAgentAuthenticationProcess doUnlockForPasswordWithCredentialContext:atLogin:]_block_invoke.77.cold.1
- __81-[POAgentAuthenticationProcess requestUserAuthenticationSyncPassword:completion:]_block_invoke.349
- __82-[POServiceLoginManagerConnection copyDeviceAttestationCertificateWithCompletion:]_block_invoke.cold.1
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.879
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.879.cold.1
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.883
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.883.cold.1
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.889
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.889.cold.1
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.895
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.895.cold.1
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.901
- __86-[POAgentAuthenticationProcess handleRemovingRegistrationForExtension:alreadyDeleted:]_block_invoke.901.cold.1
- __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.130
- __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.130.cold.1
- __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.134
- __86-[POAgentAuthenticationProcess performLoginForCurrentUserWithPasswordContext:tokenId:]_block_invoke.134.cold.1
- __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.25
- __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.25.cold.1
- __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.29
- __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.29.cold.1
- __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.33
- __88-[PODirectoryServices setLocalAccountPasswordForUser:oldPassword:withNewPassword:error:]_block_invoke.33.cold.1
- __91-[POAgentAuthenticationProcess requestSmartCardForBinding:tokenId:tokenHash:wrapTokenHash:]_block_invoke.353
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.236
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.236.cold.1
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.242
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.242.cold.1
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.248
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.248.cold.1
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.252
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.252.cold.1
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.256
- __93-[POConfigurationManager handleUpdatingGroupsAndAuthorizationForProfile:deviceConfiguration:]_block_invoke.256.cold.1
- __98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.867
- __98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.867.cold.1
- __98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.873
- __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.287
- __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.287.cold.1
- __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.291
- __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.291.cold.1
- __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.301
- __98-[POAgentAuthenticationProcess handleUserAuthorizationUsing:userName:tokens:configurationManager:]_block_invoke.301.cold.1
- ___50-[POLoginManager copyDeviceAttestationCertificate]_block_invoke
- ___54-[POExtensionAgentProcess keyProxyEndpointForKeyType:]_block_invoke
- ___54-[POLoginManager attestKey:clientDataHash:completion:]_block_invoke
- ___71-[POServiceLoginManagerConnection attestKey:clientDataHash:completion:]_block_invoke
- ___82-[POServiceLoginManagerConnection copyDeviceAttestationCertificateWithCompletion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16l
- ___block_descriptor_48_e8_32r40r_e39_v24?0^{__SecCertificate=}8"NSError"16l
- __block_literal_global.113
- __block_literal_global.114
- __block_literal_global.124
- __block_literal_global.1453
- __block_literal_global.1457
- __block_literal_global.160
- __block_literal_global.216
- __block_literal_global.226
- __block_literal_global.242
- __block_literal_global.370
- __block_literal_global.38
- __block_literal_global.391
- __block_literal_global.395
- __block_literal_global.428
- __block_literal_global.538
- __block_literal_global.675
- __block_literal_global.698
- __block_literal_global.796
- __block_literal_global.906
- _objc_msgSend$attestKey:clientDataHash:completion:
- _objc_msgSend$copyDeviceAttestationCertificateWithCompletion:
- _objc_msgSend$removeTokensFromKeychainWithService:username:
- _objc_msgSend$retrieveTokensFromKeychainForService:username:returningTokens:metaData:
- _tk_log.log
- _tk_log.onceToken
CStrings:
+ "%@%@"
+ "%s uid = %{public}d, tokenId = %{public}@, context = %{public}@, sccontext = %{public}@, bcontext = %{public}@ on %@"
+ "%s userName = %{public}@, tokenId = %{public}@, passwordContext = %{public}@, smartCardContext = %{public}@ on %@"
+ "-[POAgentAuthenticationProcess faileDevicRegistrationAfterRegistrationWithUserInteraction:]"
+ "-[POAgentAuthenticationProcess handlePreviousRefreshTokens]"
+ "-[POAgentAuthenticationProcess handleUserLogOut]"
+ "-[POAgentProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:]"
+ "-[POAuthPluginProcess authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:]"
+ "-[POConfigurationManager createTemporaryUser:passwordContext:]"
+ "-[POConfigurationManager resetTemporaryAccount]"
+ "-[POConfigurationManager updateTemporaryAccountName:altSecurityIdentity:]"
+ "-[PODaemonProcess createTemporaryUser:passwordContext:completion:]"
+ "-[PODaemonProcess resetTemporaryAccount]"
+ "-[PODaemonProcess updateTemporaryAccountName:altSecurityIdentity:completion:]"
+ "-[PODirectoryServices createTemporaryUser:password:error:]"
+ "-[PODirectoryServices findPlatformSSOAltSecurityIdentityForUserName:]"
+ "-[PODirectoryServices isUserPlatformSSOTemporaryUser:]"
+ "-[PODirectoryServices setFullName:forUser:]"
+ "-[POExtensionAgentProcess _keyForKeyType:error:]"
+ "-[POExtensionAgentProcess attestKey:pending:clientDataHash:completion:]"
+ "-[POLoginManager attestKey:clientData:completion:]"
+ "-[POLoginManager attestPendingKey:clientData:completion:]"
+ "AllowDeviceIdentifiersInAttestation"
+ "Attestation did not return certificates."
+ "Attestation failed."
+ "Attestation is not supported on this device."
+ "Attestation not available for key."
+ "Authenticate Temporary Password User"
+ "Authenticate Temporary SmartCard User"
+ "Authenticating for temporary SmartCard user"
+ "Authenticating for temporary password user"
+ "Bootstrap token not provided"
+ "Error removing unique identity."
+ "Error setting full name."
+ "Error temporary user home directory already exists."
+ "Error updating temporary account password."
+ "Failed to cache attestation."
+ "Failed to create temporary user during device registration."
+ "Failed to create temporary user with profile changes in configuration changed."
+ "Failed to remove SSO tokens."
+ "Failed to reset altSecurityIdentity for temporary user."
+ "Failed to reset full name for temporary user."
+ "Failed to reset groups for temporary user."
+ "Failed to reset pending SSO tokens for temporary user."
+ "Failed to reset stashed SSO tokens for temporary user."
+ "Failed to reset unique identifier for temporary user."
+ "Failed to retrieve credential."
+ "Failed to retrieve device configuration."
+ "Failed to save alt security identity for temporary user"
+ "Failed to save temporary account credential."
+ "Failed to save temporary user configuration during device registration."
+ "Failed to save temporary user credential during device registration."
+ "Failed to save user configuration after clearing tokens."
+ "Failed to save user configuration after creating temporary account."
+ "Failed to save user configuraton for temporary user."
+ "Failed to set name of temporary user."
+ "Failed to update temporary user."
+ "Falied to get hash for key."
+ "Key not found for attestation."
+ "Missing temporary account credential."
+ "No Platform SSO Profiles in configuration changed."
+ "No Platform SSO temporary user account."
+ "No key updates for temporary users"
+ "No user registration for temporary user"
+ "Not configured for Platform SSO in configuration changed."
+ "Not running registration for the temporary user."
+ "PSSOCreateTemporaryUser"
+ "Password context found"
+ "PlatformSSO:"
+ "Q40@0:8@16@24^@32"
+ "Q56@0:8@16@24@32@40@48"
+ "Requesting attestation"
+ "Resetting temporary account"
+ "Returning %{public}lu cached certificates."
+ "Returning %{public}lu certificates."
+ "Returning cached attestation"
+ "Returning to registration"
+ "SC context found"
+ "SSO Extension missing in configuration changed."
+ "SSO is not ready for configuration"
+ "SSO is ready for configuration"
+ "TB,V_allowDeviceIdentifiersInAttestation"
+ "Temporary account created"
+ "Temporary account credential invalid"
+ "Temporary account reset complete"
+ "Temporary user already exists."
+ "Temporary user is not enabled."
+ "Temporary user not found."
+ "Token id found"
+ "User is current temporary user."
+ "User is temporary user."
+ "User is the temporary SSO account"
+ "User logout"
+ "Using previous refresh token after login"
+ "Verifying device encryption key"
+ "Verifying device sigining key"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8q16^@24"
+ "_allowDeviceIdentifiersInAttestation"
+ "_checkForCachedAttestationForExtensionIdentifier:keyHash:"
+ "_deleteAllCachedAttestations"
+ "_deleteCachedAttestationForExtensionIdentifier:key:"
+ "_handleConfigurationChanged:startup:"
+ "_keyForKeyType:error:"
+ "_saveAttestationToKeychain:extensionIdentifier:keyHash:error:"
+ "_savePendingSSOTokensData:forIdentifier:error:"
+ "_saveStashedSSOTokensData:forIdentifier:error:"
+ "activateIgnoringOtherApps:"
+ "allowDeviceIdentifiersInAttestation"
+ "attestKey:clientData:completion:"
+ "attestKey:clientDataHash:options:completionHandler:"
+ "attestKey:pending:clientDataHash:completion:"
+ "attestPendingKey:clientData:completion:"
+ "attestation"
+ "authenticateTemporaryPasswordUser"
+ "authenticateTemporarySmartCardUser"
+ "authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:"
+ "authenticateTemporaryUserAccount:passwordContext:smartCardContext:tokenId:loginContext:completion:"
+ "com.apple.PlatformSSO.resetGuest"
+ "com.apple.logoutContinued"
+ "com.apple.restartInitiated"
+ "com.apple.shutdownInitiated"
+ "createTemporaryUser:password:error:"
+ "createTemporaryUser:passwordContext:"
+ "createTemporaryUser:passwordContext:completion:"
+ "createTemporaryUserLocalAccount:"
+ "decryptTemporaryAccountCredential"
+ "dsAttrTypeNative:PlatformSSOTemporaryUser"
+ "dsAttrTypeNative:_guest"
+ "encryptAndSaveTemporaryAccountCredential:"
+ "faileDevicRegistrationAfterRegistrationWithUserInteraction:"
+ "failed to create data vault: %{public}@"
+ "findPlatformSSOAltSecurityIdentityForUserName:"
+ "handlePasswordAuthenticationForTemporaryUser"
+ "handlePreviousRefreshTokens"
+ "handleSmartCardAuthenticationForTemporaryUser"
+ "handleUserLogOut"
+ "identifier for temporary user not found"
+ "includePreviousRefreshTokenInLoginRequest"
+ "isConfigurationActiveForExtensionIdentifier:completion:"
+ "isSupported"
+ "isTemporaryAccountUserName:"
+ "isUserPlatformSSOTemporaryUser:"
+ "objectAtIndexedSubscript:"
+ "pending attestation"
+ "platformSSOProfile"
+ "publicKeyHashForKey:"
+ "removeTokensFromKeychainWithService:username:system:"
+ "resetTemporaryAccount"
+ "resetTemporaryAccount:"
+ "retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:"
+ "setAllowDeviceIdentifiersInAttestation:"
+ "setContextBool:withFlags:forKey:"
+ "setFullName:forUser:"
+ "sharedService"
+ "substringFromIndex:"
+ "supportsCreateTemporaryUsers"
+ "true"
+ "unlockIsForTemporaryUser"
+ "updateTemporaryAccountName:altSecurityIdentity:"
+ "updateTemporaryAccountName:altSecurityIdentity:completion:"
+ "updateWithProfile:"
+ "v44@0:8q16B24@\"NSData\"28@?<v@?@\"NSArray\"@\"NSError\">36"
+ "v44@0:8q16B24@28@?36"
+ "v64@0:8@\"NSString\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40@\"NSData\"48@?<v@?Q@\"NSError\">56"
- "%s uid = %{public}d, context = %{public}@, sccontext = %{public}@, bcontext = %{public}@ on %@"
- "-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke"
- "-[POExtensionAgentProcess attestKey:clientDataHash:completion:]"
- "-[POExtensionAgentProcess copyDeviceAttestationCertificateWithCompletion:]"
- "-[POLoginManager attestKey:clientDataHash:completion:]"
- "-[POLoginManager copyDeviceAttestationCertificate]"
- "Failed to clear SSO tokens after login."
- "Item found"
- "PlatformSSO:%@"
- "Verifying device keys"
- "attestKey:clientDataHash:completion:"
- "copyDeviceAttestationCertificate"
- "copyDeviceAttestationCertificateWithCompletion:"
- "removeTokensFromKeychainWithService:username:"
- "retrieveTokensFromKeychainForService:username:returningTokens:metaData:"
- "v24@0:8@?<v@?^{__SecCertificate=}@\"NSError\">16"
- "v24@?0^{__SecCertificate=}8@\"NSError\"16"
- "v40@0:8q16@\"NSData\"24@?<v@?@\"NSData\"@\"NSError\">32"

```
