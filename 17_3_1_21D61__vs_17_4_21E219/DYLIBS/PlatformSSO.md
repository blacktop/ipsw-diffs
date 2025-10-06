## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/PlatformSSO`

```diff

-384.60.2.0.0
-  __TEXT.__text: 0xad068
-  __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0x6424
-  __TEXT.__const: 0xfb4
-  __TEXT.__cstring: 0xd594
-  __TEXT.__oslogstring: 0x2924
-  __TEXT.__gcc_except_tab: 0xddc
+384.100.11.0.0
+  __TEXT.__text: 0xafde4
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_methlist: 0x65dc
+  __TEXT.__const: 0xfc4
+  __TEXT.__cstring: 0xd978
+  __TEXT.__oslogstring: 0x2a5c
+  __TEXT.__gcc_except_tab: 0xeb8
   __TEXT.__dlopen_cstrs: 0x162
-  __TEXT.__unwind_info: 0x248c
-  __TEXT.__objc_classname: 0xdf0
-  __TEXT.__objc_methname: 0xe172
-  __TEXT.__objc_methtype: 0x28a2
-  __TEXT.__objc_stubs: 0x97a0
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x29c8
-  __DATA_CONST.__objc_classlist: 0x498
+  __TEXT.__unwind_info: 0x24f4
+  __TEXT.__objc_classname: 0xdfc
+  __TEXT.__objc_methname: 0xe7b0
+  __TEXT.__objc_methtype: 0x294b
+  __TEXT.__objc_stubs: 0x9bc0
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x2a48
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x11e28
-  __DATA_CONST.__objc_selrefs: 0x2f40
-  __DATA_CONST.__objc_arraydata: 0x70
-  __AUTH_CONST.__objc_const: 0x37a0
-  __AUTH_CONST.__cfstring: 0x8d40
-  __AUTH_CONST.__const: 0xb20
-  __AUTH_CONST.__objc_intobj: 0x138
+  __DATA_CONST.__objc_const: 0x120e0
+  __DATA_CONST.__objc_selrefs: 0x30a0
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_classrefs: 0x608
+  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_arraydata: 0x88
+  __AUTH_CONST.__objc_const: 0x37e8
+  __AUTH_CONST.__cfstring: 0x9060
+  __AUTH_CONST.__const: 0xb60
+  __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xa88
-  __AUTH.__objc_data: 0x2df0
-  __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0x5f8
-  __DATA.__objc_superrefs: 0x218
-  __DATA.__objc_ivar: 0x6cc
+  __AUTH_CONST.__auth_got: 0xab0
+  __AUTH.__objc_data: 0x2e40
+  __DATA.__objc_ivar: 0x6fc
   __DATA.__data: 0xed0
   __DATA.__bss: 0x449
   __DATA.__common: 0x20

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: F7971CF9-409F-3AA6-A730-5DA2FF499210
-  Functions: 4645
-  Symbols:   13836
-  CStrings:  5844
+  UUID: E8B9ED62-5C77-3552-BF07-909C0B5471EA
+  Functions: 4707
+  Symbols:   14032
+  CStrings:  5975
 
Symbols:
+ +[POConstantUtil stringForSEPBiometricPolicy:]
+ +[POSecKeyHelper checkIfBiometricConstraintsForSigning:]
+ +[POSecKeyHelper checkIfBiometricConstraintsForSigningForKey:]
+ +[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]
+ +[POSecKeyHelper keyForData:context:]
+ +[POSecKeyHelper keyForData:context:].cold.1
+ -[POAgentAuthenticationProcess __screenUnlockHandler]
+ -[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:].cold.4
+ -[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:].cold.5
+ -[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:].cold.6
+ -[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:].cold.7
+ -[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]
+ -[POAgentAuthenticationProcess _startUserRegistration].cold.2
+ -[POAgentAuthenticationProcess _startUserRegistration].cold.3
+ -[POAgentAuthenticationProcess _startUserRegistration].cold.4
+ -[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]
+ -[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:].cold.1
+ -[POAgentAuthenticationProcess handleKeyRequestSync]
+ -[POAgentAuthenticationProcess handleKeyRequestSync].cold.1
+ -[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]
+ -[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:].cold.1
+ -[POAgentAuthenticationProcess requestUserAuthenticationSyncPassword:completion:]
+ -[POAgentAuthenticationProcess requestUserAuthenticationSyncPassword:completion:].cold.1
+ -[POAgentAuthenticationProcess screenUnlocked]
+ -[POAgentAuthenticationProcess setScreenUnlocked:]
+ -[POAgentAuthenticationProcess set__screenUnlockHandler:]
+ -[POAgentAuthenticationProcess showAlertMessage:messageText:completion:]
+ -[POAgentAuthenticationProcess showAlertMessage:messageText:completion:].cold.1
+ -[POAgentAuthenticationProcess waitForScreenUnlockithCompletion:]
+ -[POAuthenticationContext dealloc]
+ -[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:].cold.2
+ -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:]
+ -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:].cold.1
+ -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:].cold.2
+ -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:].cold.3
+ -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:hash:identity:]
+ -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:hash:identity:].cold.1
+ -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:hash:identity:].cold.2
+ -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:hash:identity:].cold.3
+ -[POLoginConfiguration setUserSEPKeyBiometricPolicy:]
+ -[POLoginConfiguration userSEPKeyBiometricPolicy]
+ -[POLoginJWTBody amr]
+ -[POMutableLoginJWTBody setAmr:]
+ -[PORegistrationContext isNewPasswordUser]
+ -[PORegistrationContext isNewSmartCarddUser]
+ -[PORegistrationContext newUserBindingComplete]
+ -[PORegistrationContext setNewPasswordUser:]
+ -[PORegistrationContext setNewSmartCardUser:]
+ -[PORegistrationContext setNewUserBindingComplete:]
+ -[PORegistrationContext setSmartCardHash:]
+ -[PORegistrationContext setUserSEPKeyInvalid:]
+ -[PORegistrationContext smartCardHash]
+ -[PORegistrationContext userSEPKeyInvalid]
+ -[POTokenHelper canTokenIdLogin:pubKeyHash:]
+ -[POTokenHelper findInfoForTokenId:]
+ -[POTokenHelper findInfoForTokenId:].cold.1
+ -[POTokenHelper findTokenIdForSmartCardAMUser:tokenHash:]
+ -[POTokenHelper findTokenIdForSmartCardAMUser:tokenHash:].cold.1
+ -[POTokenHelper findTokenIdForSmartCardBoundUser:tokenHash:]
+ -[POTokenHelper findTokenIdForSmartCardBoundUser:tokenHash:].cold.1
+ -[POTokenInfo .cxx_destruct]
+ -[POTokenInfo canLogin]
+ -[POTokenInfo keyHash]
+ -[POTokenInfo name]
+ -[POTokenInfo setCanLogin:]
+ -[POTokenInfo setKeyHash:]
+ -[POTokenInfo setName:]
+ -[POTokenInfo setTokenId:]
+ -[POTokenInfo setWrapHash:]
+ -[POTokenInfo tokenId]
+ -[POTokenInfo wrapHash]
+ -[POUserConfiguration sepKeyWithContext:]
+ -[POUserConfiguration setSmartCardHash:]
+ -[POUserConfiguration smartCardHash]
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table204
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table64
+ GCC_except_table74
+ GCC_except_table80
+ _AKS_FV_MDM_RECOVERY_KEY_UUID
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_POTokenInfo
+ _OBJC_CLASS_$_TKClientToken
+ _OBJC_IVAR_$_POAgentAuthenticationProcess.___screenUnlockHandler
+ _OBJC_IVAR_$_POAgentAuthenticationProcess._screenUnlocked
+ _OBJC_IVAR_$_POLoginConfiguration._userSEPKeyBiometricPolicy
+ _OBJC_IVAR_$_PORegistrationContext._newPasswordUser
+ _OBJC_IVAR_$_PORegistrationContext._newSmartCardUser
+ _OBJC_IVAR_$_PORegistrationContext._newUserBindingComplete
+ _OBJC_IVAR_$_PORegistrationContext._smartCardHash
+ _OBJC_IVAR_$_PORegistrationContext._userSEPKeyInvalid
+ _OBJC_IVAR_$_POTokenInfo._canLogin
+ _OBJC_IVAR_$_POTokenInfo._keyHash
+ _OBJC_IVAR_$_POTokenInfo._name
+ _OBJC_IVAR_$_POTokenInfo._tokenId
+ _OBJC_IVAR_$_POTokenInfo._wrapHash
+ _OBJC_IVAR_$_POUserConfiguration._smartCardHash
+ _OBJC_METACLASS_$_POTokenInfo
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _SecAccessConstraintCreateBiometryAny
+ _SecAccessConstraintCreateBiometryCurrentSet
+ _SecAccessConstraintCreateKofN
+ _SecAccessConstraintCreateWatch
+ _SecAccessControlAddConstraintForOperation
+ _SecAccessControlGetConstraint
+ __OBJC_$_INSTANCE_METHODS_POTokenInfo
+ __OBJC_$_INSTANCE_VARIABLES_POTokenInfo
+ __OBJC_$_PROP_LIST_POTokenInfo
+ __OBJC_CLASS_RO_$_POTokenInfo
+ __OBJC_METACLASS_RO_$_POTokenInfo
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.569
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.569.cold.1
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.575
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.575.cold.1
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.579
+ ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.579.cold.1
+ ___100-[POAgentAuthenticationProcess handleScreenUnlockWithCredentialContext:tokenId:atLogin:tokenUnlock:]_block_invoke
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1002
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1002.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1011
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1011.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1015
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1015.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1021
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1021.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1024
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1024.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1027
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1027.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.976
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.976.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.982
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.982.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.988
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.988.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.994
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.994.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.995
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.995.cold.1
+ ___108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.687
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.217
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.217.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.223
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.223.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.229
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.229.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.235
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.235.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.241
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.241.cold.1
+ ___114-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:]_block_invoke.cold.1
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.470
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.470.cold.1
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.476
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.476.cold.1
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.479
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.479.cold.1
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.485
+ ___119-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.454
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.454.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.457
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.457.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.464
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke.cold.1
+ ___123-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]_block_invoke_2
+ ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1118
+ ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1118.cold.1
+ ___21-[POLoginJWTBody amr]_block_invoke
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.41
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.41.cold.1
+ ___36-[POUserConfiguration initWithData:]_block_invoke.178
+ ___37+[POSecKeyHelper keyForData:context:]_block_invoke
+ ___37+[POSecKeyHelper keyForData:context:]_block_invoke.cold.1
+ ___37-[POLoginConfiguration initWithData:]_block_invoke.230
+ ___39-[PODaemonConnection _connectToService]_block_invoke.79
+ ___39-[PODaemonConnection _connectToService]_block_invoke.79.cold.1
+ ___40-[POServiceConnection _connectToService]_block_invoke.75
+ ___40-[POServiceConnection _connectToService]_block_invoke.75.cold.1
+ ___42-[POUIServiceConnection _connectToService]_block_invoke.64
+ ___42-[POUIServiceConnection _connectToService]_block_invoke.64.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.102
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.102.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.106
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.106.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.110
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.110.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.114
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.114.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.119
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.119.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.123
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.123.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.127
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.127.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.131
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.131.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.135
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.135.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.139
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.139.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.143
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.143.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.147
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.147.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.82
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.82.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.86
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.86.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.90
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.90.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.94
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.94.cold.1
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.98
+ ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.98.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.152
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.152.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.156
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.156.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.160
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.160.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.162
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.162.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.166
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.166.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.170
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.170.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.174
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.174.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.175
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.175.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.179
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.179.cold.1
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.183
+ ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.183.cold.1
+ ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.108
+ ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.108.cold.1
+ ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.121
+ ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.121.cold.1
+ ___52-[POAgentAuthenticationProcess handleKeyRequestSync]_block_invoke
+ ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.117
+ ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.117.cold.1
+ ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.93
+ ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.93.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.361.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.370
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.370.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.376
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.380
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.380.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.386
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.386.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.392
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.392.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.396
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.396.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.402
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.408
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.413
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.420
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.420.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.426
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.428
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.428.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.409
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.409.cold.1
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.414
+ ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.414.cold.1
+ ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.619
+ ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.619.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.805
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.805.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.811
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.811.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.815
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.815.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.821
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.821.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.827
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.827.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.833
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.833.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.839
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.839.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.752
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.752.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.758
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.758.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.764
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.764.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.770
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.770.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.776
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.776.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.782
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.782.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.788
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.788.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.792
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.792.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.796
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.796.cold.1
+ ___55-[POConfigurationManager userConfigurationForUserName:]_block_invoke.139
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.337
+ ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.337.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.345
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.345.cold.1
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.349
+ ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.349.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.324
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.329
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.329.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.335
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.339
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.339.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.345
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.345.cold.1
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.351
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.352
+ ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.353
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.295
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.295.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.298
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.298.cold.1
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.299
+ ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.299.cold.1
+ ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1038
+ ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1038.cold.1
+ ___59-[POAgentAuthenticationProcess finishRegistrationWithRetry]_block_invoke.444
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.499
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.499.cold.1
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.505
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.505.cold.1
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.511
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.511.cold.1
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.517
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.517.cold.1
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.523
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.523.cold.1
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.529
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.529.cold.1
+ ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.535
+ ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1057
+ ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1057.cold.1
+ ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.599
+ ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.599.cold.1
+ ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.628
+ ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.628.cold.1
+ ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.634
+ ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke.147
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.221
+ ___60-[POExtensionAgentProcess setLoginConfiguration:completion:]_block_invoke.221.cold.1
+ ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.628
+ ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.628.cold.1
+ ___61-[POConfigurationManager removeUserConfigurationForUserName:]_block_invoke.154
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.261
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.261.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.267
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.267.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.271
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.271.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.275
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.276
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.276.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.280
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.280.cold.1
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.284
+ ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.284.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.686
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.686.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.696
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.696.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.700
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.700.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.704
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.704.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.717
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.717.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.730
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.730.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.734
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.734.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.738
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.738.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.742
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.742.cold.1
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.63
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.63.cold.1
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.67
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.67.cold.1
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.71
+ ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.71.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.850
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.850.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.856
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.856.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.860
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.860.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.866
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.866.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.872
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.872.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.878
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.878.cold.1
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.365
+ ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.365.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.12
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.12.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.16
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.16.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.22
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.22.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.28
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.28.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.33
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.33.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.7
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.7.cold.1
+ ___65+[POSecKeyHelper createSEPKeyForKeyType:userPresence:currentSet:]_block_invoke.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.238
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.238.cold.1
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.246
+ ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.246.cold.1
+ ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1092
+ ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1092.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.310
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.310.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.313
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.313.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.320
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.320.cold.1
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.326
+ ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.326.cold.1
+ ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.271
+ ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke_2
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.174
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.174.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.187
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.196
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.199
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.200
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.200.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.204
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.204.cold.1
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.210
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke_2
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke_3
+ ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke_3.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.900
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.900.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.906
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.906.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.912
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.912.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.918
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.918.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.919
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.919.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.926
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.926.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.935
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.935.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.939
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.939.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.945
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.945.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.951
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.951.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.957
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.957.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.963
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.963.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.969
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.969.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.970
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.970.cold.1
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.588
+ ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.588.cold.1
+ ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.284
+ ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.278
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.292
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.292.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.298
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.298.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.302
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.302.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.308
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.308.cold.1
+ ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.314
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.656.cold.1
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.657.cold.1
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.661
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.667
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.672
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.673
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.668
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.668.cold.1
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1060.cold.1
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1064
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1070
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1075
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1076
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1071
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1071.cold.1
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1129
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1129.cold.1
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1135
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1135.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.631
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.631.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.641
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.642
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.642.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.646
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.651
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.647
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.647.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.652
+ ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.250
+ ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.250.cold.1
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1095.cold.1
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1099
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1105
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1110
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1111
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1106
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1106.cold.1
+ ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1082
+ ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1082.cold.1
+ ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.542
+ ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.542.cold.1
+ ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.548
+ ___block_descriptor_32_e8_v16?0Q8l
+ ___block_descriptor_48_e8_32s40r_e8_v16?0Q8lr40l8s32l8
+ ___block_descriptor_49_e8_32s40s_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_51_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_59_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1000
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.125
+ ___block_literal_global.131
+ ___block_literal_global.1367
+ ___block_literal_global.1371
+ ___block_literal_global.139
+ ___block_literal_global.190
+ ___block_literal_global.198
+ ___block_literal_global.208
+ ___block_literal_global.263
+ ___block_literal_global.265
+ ___block_literal_global.278
+ ___block_literal_global.282
+ ___block_literal_global.301
+ ___block_literal_global.327
+ ___block_literal_global.487
+ ___block_literal_global.499
+ ___block_literal_global.532
+ ___block_literal_global.555
+ ___block_literal_global.96
+ ___block_literal_global.99
+ ___block_literal_global.996
+ __unnamed_array_storage.1009
+ __unnamed_array_storage.566
+ __unnamed_array_storage.570
+ __unnamed_array_storage.576
+ __unnamed_array_storage.747
+ __unnamed_array_storage.933
+ _calloc
+ _firebloom_ccpbkdf2_hmac
+ _kSecAttrAccessibleWhenUnlocked
+ _kSecAttrApplicationLabel
+ _krb5_parse_name_flags
+ _malloc
+ _objc_msgSend$__screenUnlockHandler
+ _objc_msgSend$_handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:
+ _objc_msgSend$canEvaluatePolicy:error:
+ _objc_msgSend$checkIfBiometricConstraintsForSigning:
+ _objc_msgSend$checkIfBiometricConstraintsForSigningForKey:
+ _objc_msgSend$createSEPKeyForKeyType:userPresence:currentSet:
+ _objc_msgSend$evaluateAccessControl:operation:options:error:
+ _objc_msgSend$findTokenIdForSmartCardAMUser:tokenHash:
+ _objc_msgSend$findTokenIdForSmartCardBoundUser:tokenHash:
+ _objc_msgSend$handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:
+ _objc_msgSend$handleKeyRequestSync
+ _objc_msgSend$handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:
+ _objc_msgSend$initWithTokenID:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isNewPasswordUser
+ _objc_msgSend$isNewSmartCarddUser
+ _objc_msgSend$keyForData:context:
+ _objc_msgSend$keyUsage
+ _objc_msgSend$keychainAttributes
+ _objc_msgSend$keys
+ _objc_msgSend$newUserBindingComplete
+ _objc_msgSend$requestUserAuthenticationSyncPassword:completion:
+ _objc_msgSend$retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:
+ _objc_msgSend$retrieveIdentityForTokenId:context:forSigning:hash:identity:
+ _objc_msgSend$screenUnlocked
+ _objc_msgSend$sepKeyWithContext:
+ _objc_msgSend$sessionWithLAContext:error:
+ _objc_msgSend$setAmr:
+ _objc_msgSend$setLocalizedFallbackTitle:
+ _objc_msgSend$setLocalizedReason:
+ _objc_msgSend$setNewPasswordUser:
+ _objc_msgSend$setNewSmartCardUser:
+ _objc_msgSend$setNewUserBindingComplete:
+ _objc_msgSend$setOptionCallerIconPath:
+ _objc_msgSend$setOptionFallbackVisible:
+ _objc_msgSend$setScreenUnlocked:
+ _objc_msgSend$setSmartCardHash:
+ _objc_msgSend$setTouchIDAuthenticationAllowableReuseDuration:
+ _objc_msgSend$setUserSEPKeyInvalid:
+ _objc_msgSend$set__screenUnlockHandler:
+ _objc_msgSend$showAlertMessage:messageText:completion:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$smartCardHash
+ _objc_msgSend$stringForSEPBiometricPolicy:
+ _objc_msgSend$userSEPKeyBiometricPolicy
+ _objc_msgSend$userSEPKeyInvalid
+ _objc_msgSend$waitForScreenUnlockithCompletion:
+ _objc_retain_x6
- +[POSecKeyHelper keyForData:].cold.1
- -[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]
- -[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]
- -[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:].cold.1
- -[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]
- -[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:].cold.1
- -[POAgentAuthenticationProcess requestUserAuthenticationWithCompletion:]
- -[POAgentAuthenticationProcess requestUserAuthenticationWithCompletion:].cold.1
- -[POAgentAuthenticationProcess screenUnlockHandler]
- -[POAgentAuthenticationProcess setScreenUnlockHandler:]
- -[POAgentAuthenticationProcess showAlertMessage:completion:]
- -[POAgentAuthenticationProcess showAlertMessage:completion:].cold.1
- -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:certificate:privateKey:]
- -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:certificate:privateKey:].cold.1
- -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:certificate:privateKey:].cold.2
- -[POKeychainHelper retrieveCertAndKeyForTokenId:context:forSigning:certificate:privateKey:].cold.3
- -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:identity:]
- -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:identity:].cold.1
- -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:identity:].cold.2
- -[POKeychainHelper retrieveIdentityForTokenId:context:forSigning:identity:].cold.3
- -[PORegistrationContext isNewUser]
- -[PORegistrationContext setNewUser:]
- -[POTokenHelper findNameForTokenId:returningHash:wrapHash:]
- -[POTokenHelper findNameForTokenId:returningHash:wrapHash:].cold.1
- -[POTokenHelper findTokenIdForSmartCardAMUser:]
- -[POTokenHelper findTokenIdForSmartCardAMUser:].cold.1
- -[POTokenHelper findTokenIdForSmartCardBoundUser:]
- -[POTokenHelper findTokenIdForSmartCardBoundUser:].cold.1
- GCC_except_table145
- GCC_except_table149
- GCC_except_table194
- _OBJC_IVAR_$_POAgentAuthenticationProcess._screenUnlockHandler
- _OBJC_IVAR_$_PORegistrationContext._newUser
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.528
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.528.cold.1
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.534
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.534.cold.1
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.538
- ___100-[POAgentAuthenticationProcess handleKerberosMappingForTokens:loginConfiguration:userConfiguration:]_block_invoke.538.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1000
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1000.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1006
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1006.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1009
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1009.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1012
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1012.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.958
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.961
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.961.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.967
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.967.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.973.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.979
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.979.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.980
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.980.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.987
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.987.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.996
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.996.cold.1
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.183
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.183.cold.1
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.189
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.189.cold.1
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.195
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.195.cold.1
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.201
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.201.cold.1
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.207
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.207.cold.1
- ___104-[POAgentAuthenticationProcess _handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:]_block_invoke.cold.1
- ___108-[POAgentAuthenticationProcess userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]_block_invoke.646
- ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1103
- ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1103.cold.1
- ___29+[POSecKeyHelper keyForData:]_block_invoke
- ___29+[POSecKeyHelper keyForData:]_block_invoke.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.8
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.8.cold.1
- ___36-[POUserConfiguration initWithData:]_block_invoke.176
- ___37-[POLoginConfiguration initWithData:]_block_invoke.227
- ___39-[PODaemonConnection _connectToService]_block_invoke.78
- ___39-[PODaemonConnection _connectToService]_block_invoke.78.cold.1
- ___40-[POServiceConnection _connectToService]_block_invoke.74
- ___40-[POServiceConnection _connectToService]_block_invoke.74.cold.1
- ___41+[POSecKeyHelper createSEPKeyForKeyType:]_block_invoke
- ___41+[POSecKeyHelper createSEPKeyForKeyType:]_block_invoke.12
- ___41+[POSecKeyHelper createSEPKeyForKeyType:]_block_invoke.12.cold.1
- ___41+[POSecKeyHelper createSEPKeyForKeyType:]_block_invoke.7
- ___41+[POSecKeyHelper createSEPKeyForKeyType:]_block_invoke.7.cold.1
- ___41+[POSecKeyHelper createSEPKeyForKeyType:]_block_invoke.cold.1
- ___42-[POUIServiceConnection _connectToService]_block_invoke.63
- ___42-[POUIServiceConnection _connectToService]_block_invoke.63.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.103
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.103.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.107
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.107.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.112
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.112.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.116
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.116.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.120
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.120.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.124
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.124.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.128
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.128.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.132
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.132.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.136
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.136.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.140
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.140.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.79
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.79.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.83
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.83.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.87
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.87.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.91
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.91.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.95
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.95.cold.1
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.99
- ___46-[POKerberosHelper importKerberosEntry:error:]_block_invoke.99.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.145
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.145.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.149
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.149.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.153
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.153.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.155
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.155.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.159
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.159.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.163
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.163.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.167
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.167.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.168
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.168.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.172
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.172.cold.1
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.176
- ___48-[POKerberosHelper exchangeKerberosTGTForEntry:]_block_invoke.176.cold.1
- ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.107
- ___50-[POConfigurationManager currentUserConfiguration]_block_invoke.107.cold.1
- ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.120
- ___51-[POConfigurationManager currentLoginConfiguration]_block_invoke.120.cold.1
- ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.116
- ___52-[POConfigurationManager currentDeviceConfiguration]_block_invoke.116.cold.1
- ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.92
- ___52-[POServiceLoginManagerConnection _connectToService]_block_invoke.92.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.329
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.329.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.335
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.339
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.339.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.345
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.345.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.351
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.351.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.355
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.355.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.367
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.372
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.379
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.379.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.385
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.387
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke.387.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.368
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.368.cold.1
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.373
- ___54-[POAgentAuthenticationProcess _startUserRegistration]_block_invoke_2.373.cold.1
- ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.578
- ___54-[POAgentAuthenticationProcess isCurrentSSOExtension:]_block_invoke.578.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.790
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.790.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.796
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.796.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.800
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.800.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.806
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.806.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.812
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.812.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.818
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.818.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.824
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.824.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.737
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.737.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.743
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.743.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.749
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.749.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.755
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.755.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.761
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.761.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.767
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.767.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.773
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.773.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.777
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.777.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.781
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.781.cold.1
- ___55-[POConfigurationManager userConfigurationForUserName:]_block_invoke.138
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.325
- ___55-[POExtensionAgentProcess loginUserNameWithCompletion:]_block_invoke.325.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.333
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.333.cold.1
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.337
- ___55-[POExtensionAgentProcess setLoginUserName:completion:]_block_invoke.337.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.292
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.297
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.297.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.303
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.307
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.307.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.313
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.313.cold.1
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.319
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.320
- ___56-[POAgentAuthenticationProcess _startDeviceRegistration]_block_invoke.321
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.289
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.289.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.292
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.292.cold.1
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.293
- ___57-[POExtensionAgentProcess resetDeviceKeysWithCompletion:]_block_invoke.293.cold.1
- ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1023
- ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1023.cold.1
- ___59-[POAgentAuthenticationProcess finishRegistrationWithRetry]_block_invoke.403
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.458
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.458.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.464
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.464.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.470
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.470.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.476
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.476.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.482
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.482.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.488
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.488.cold.1
- ___59-[POAgentAuthenticationProcess handleConfigurationChanged:]_block_invoke.494
- ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1042
- ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1042.cold.1
- ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.558
- ___60-[POAgentAuthenticationProcess handleUnfinishedTGTExchanges]_block_invoke.558.cold.1
- ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.587
- ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.587.cold.1
- ___60-[POAgentAuthenticationProcess requestDidCompleteWithError:]_block_invoke.593
- ___60-[POConfigurationManager saveUserConfiguration:forUserName:]_block_invoke.146
- ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.612
- ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.612.cold.1
- ___61-[POConfigurationManager removeUserConfigurationForUserName:]_block_invoke.153
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.228
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.228.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.234
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.234.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.238
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.238.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.242
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.244
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.244.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.248
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.248.cold.1
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.252
- ___63-[POAgentAuthenticationProcess handleKeyRequestWithCompletion:]_block_invoke.252.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.670
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.670.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.681
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.681.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.685
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.685.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.689
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.689.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.702
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.702.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.715
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.715.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.719
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.719.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.723
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.723.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.727
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.727.cold.1
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.34
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.34.cold.1
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.38
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.38.cold.1
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.42
- ___64+[POSecKeyHelper evaluateTrustForCertificates:rootCertificates:]_block_invoke.42.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.835
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.835.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.841
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.841.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.845
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.845.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.851
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.851.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.857
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.857.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.863
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.863.cold.1
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.353
- ___64-[POExtensionAgentProcess setUserLoginConfiguration:completion:]_block_invoke.353.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.232
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.232.cold.1
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.234
- ___65-[POExtensionAgentProcess setCertificateData:keyType:completion:]_block_invoke.234.cold.1
- ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1077
- ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1077.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.304
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.304.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.307
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.307.cold.1
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.308
- ___67-[POExtensionAgentProcess resetUserSecureEnclaveKeyWithCompletion:]_block_invoke.308.cold.1
- ___67-[POExtensionAgentProcess userNeedsReauthenticationWithCompletion:]_block_invoke.265
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.150
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.151
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.151.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.170
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.170.cold.1
- ___68-[POAgentAuthenticationProcess _doLoginWithPasswordContext:tokenId:]_block_invoke.176
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.882
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.885
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.885.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.891
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.891.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.897.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.903
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.903.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.904
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.904.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.911
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.911.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.920
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.920.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.924
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.924.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.930
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.930.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.933
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.933.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.936
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.936.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.942
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.942.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.954
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.954.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.955
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.955.cold.1
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.547
- ___69-[POAgentAuthenticationProcess handlePendingSSOTokensWithSharedData:]_block_invoke.547.cold.1
- ___70-[POExtensionAgentProcess userRegistrationsNeedsRepairWithCompletion:]_block_invoke.278
- ___72-[POExtensionAgentProcess deviceRegistrationsNeedsRepairWithCompletion:]_block_invoke.272
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.260
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.260.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.266
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.266.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.270
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.270.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.276
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.276.cold.1
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke.282
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.640
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.640.cold.1
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.641
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.641.cold.1
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.645
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.651
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.652
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.652.cold.1
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1045
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1045.cold.1
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1049
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1055
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1061
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1056
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1056.cold.1
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1114
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1114.cold.1
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1120
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1120.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.615
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.615.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.619
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.625
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.626
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.626.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.630
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.631
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.631.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.636
- ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.217
- ___79-[POAgentAuthenticationProcess requestUserAuthenticationWithWindow:completion:]_block_invoke.217.cold.1
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1080
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1080.cold.1
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1084
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1090
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1096
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1091
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1091.cold.1
- ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1067
- ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1067.cold.1
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.429
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.429.cold.1
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.435
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.435.cold.1
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.438
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.438.cold.1
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.444
- ___94-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]_block_invoke.cold.1
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke.413
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke.413.cold.1
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke.416
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke.416.cold.1
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke.423
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke.cold.1
- ___98-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]_block_invoke_2
- ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.501
- ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.501.cold.1
- ___98-[POAgentAuthenticationProcess handleRegistrationViewControllerForExtensionIdentifier:completion:]_block_invoke.507
- ___block_descriptor_50_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.110
- ___block_literal_global.117
- ___block_literal_global.120
- ___block_literal_global.124
- ___block_literal_global.1351
- ___block_literal_global.1355
- ___block_literal_global.138
- ___block_literal_global.201
- ___block_literal_global.262
- ___block_literal_global.264
- ___block_literal_global.277
- ___block_literal_global.281
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.446
- ___block_literal_global.492
- ___block_literal_global.514
- ___block_literal_global.519
- ___block_literal_global.946
- ___block_literal_global.950
- __unnamed_array_storage.732
- __unnamed_array_storage.918
- __unnamed_array_storage.994
- _aks_remote_peer_register
- _cccurve25519_make_key_pair
- _ccder_encode_body
- _ccder_encode_tl
- _cced25519_make_key_pair
- _decode_fv_data
- _decode_fv_key
- _decode_fv_params
- _decode_implicit_raw_octet_string
- _decode_implicit_raw_octet_string_copy
- _decode_implicit_uint64
- _der_decode_any
- _encode_fv_data
- _encode_fv_key
- _encode_fv_params
- _firebloom_cccurve25519
- _firebloom_curve25519_make_key_pair
- _firebloom_ed25519_make_key_pair
- _firebloom_get_sized_copy
- _firebloom_get_sized_len
- _firebloom_ipc_copy_out
- _malloc_type_calloc
- _objc_msgSend$_handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:
- _objc_msgSend$findTokenIdForSmartCardAMUser:
- _objc_msgSend$findTokenIdForSmartCardBoundUser:
- _objc_msgSend$handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:
- _objc_msgSend$handleUserRegistrationForUser:repair:newUser:notified:profile:
- _objc_msgSend$isNewUser
- _objc_msgSend$requestUserAuthenticationWithCompletion:
- _objc_msgSend$retrieveCertAndKeyForTokenId:context:forSigning:certificate:privateKey:
- _objc_msgSend$retrieveIdentityForTokenId:context:forSigning:identity:
- _objc_msgSend$screenUnlockHandler
- _objc_msgSend$setNewUser:
- _objc_msgSend$setOptionCallerIconBundlePath:
- _objc_msgSend$setScreenUnlockHandler:
- _objc_msgSend$showAlertMessage:completion:
CStrings:
+ "\x19\x1f\x1f\b"
+ "\"\x11&\x14"
+ "%s New Password User = %{public}@, New SmartCard User = %{public}@ on %@"
+ "+[POSecKeyHelper keyForData:context:]"
+ ","
+ "-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:]"
+ "-[POAgentAuthenticationProcess handleKeyRequestSync]"
+ "-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:]"
+ "-[POAgentAuthenticationProcess requestUserAuthenticationSyncPassword:completion:]"
+ "-[POAgentAuthenticationProcess showAlertMessage:messageText:completion:]"
+ "-[POTokenHelper findInfoForTokenId:]"
+ "-[POTokenHelper findTokenIdForSmartCardAMUser:tokenHash:]"
+ "-[POTokenHelper findTokenIdForSmartCardBoundUser:tokenHash:]"
+ "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
+ "B24@0:8^{__SecAccessControl=}16"
+ "B52@0:8@16@24B32@36^^{__SecIdentity}44"
+ "B60@0:8@16@24B32@36^^{__SecCertificate}44^^{__SecKey}52"
+ "BIOMETRIC_CHANGED_TEXT"
+ "CUSTOM_FALLBACK_BUTTON_TEXT"
+ "DEFAULT_REGISTRATION_REQUIRED_TEXT"
+ "Error adding biometric constraint."
+ "Error evaluating context"
+ "Error evaluating context for User Secure Enclave Key authentication"
+ "Error with SecAccessConstraintCreateBiometry."
+ "Error with SecAccessConstraintCreateKofN."
+ "Error with SecAccessConstraintCreateWatch."
+ "Failed to create key during reset key because touchID or watch is not available."
+ "Failed to create key during user user registration because touchID or watch is not available."
+ "Failed to save user configuration after biometric failure."
+ "Handling Pending SSO During Migration"
+ "Invalid user secure enclave key biometric policy."
+ "Key policy = %{public}@"
+ "New user binding complete."
+ "New user binding failed."
+ "POTokenInfo"
+ "POUserStateNewPasswordUser"
+ "POUserStateNewSmartCardUser"
+ "POUserStateUserKeyInvalid"
+ "PasswordFallback"
+ "REGISTRATION_FAILED_NO_BIOMETRIC_TEXT"
+ "ReuseDuringUnlock"
+ "System cancelled context"
+ "T@\"NSData\",&,V_smartCardHash"
+ "T@\"NSData\",C,N,V_keyHash"
+ "T@\"NSData\",C,N,V_wrapHash"
+ "T@\"NSData\",C,V_smartCardHash"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",C,N,V_tokenId"
+ "T@?,C,N,V___screenUnlockHandler"
+ "TB,GisNewPasswordUser,V_newPasswordUser"
+ "TB,GisNewSmartCarddUser,V_newSmartCardUser"
+ "TB,N,V_canLogin"
+ "TB,V_newUserBindingComplete"
+ "TB,V_screenUnlocked"
+ "TB,V_userSEPKeyInvalid"
+ "TQ,N,V_userSEPKeyBiometricPolicy"
+ "TouchIDOrWatchAny"
+ "TouchIDOrWatchCurrentSet"
+ "UI is available"
+ "User state is needs registration or key is invalid"
+ "Waiting for UI to be available"
+ "Y\x11"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8@16@24"
+ "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8q16B24B28"
+ "___screenUnlockHandler"
+ "__screenUnlockHandler"
+ "_canLogin"
+ "_handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:tokenHash:"
+ "_keyHash"
+ "_name"
+ "_newPasswordUser"
+ "_newSmartCardUser"
+ "_newUserBindingComplete"
+ "_screenUnlocked"
+ "_smartCardHash"
+ "_tokenId"
+ "_userSEPKeyBiometricPolicy"
+ "_userSEPKeyInvalid"
+ "_wrapHash"
+ "amr"
+ "canEvaluatePolicy:error:"
+ "canLogin"
+ "canTokenIdLogin:pubKeyHash:"
+ "checkIfBiometricConstraintsForSigning:"
+ "checkIfBiometricConstraintsForSigningForKey:"
+ "createSEPKeyForKeyType:userPresence:currentSet:"
+ "cwtch"
+ "evaluateAccessControl:operation:options:error:"
+ "find attribute mapping token id hash"
+ "find bound token id hash"
+ "findInfoForTokenId:"
+ "findTokenIdForSmartCardAMUser:tokenHash:"
+ "findTokenIdForSmartCardBoundUser:tokenHash:"
+ "handleDeviceAndUserRegistrationForRepair:newPasswordUser:newSmartCardUser:notified:profile:"
+ "handleKeyRequestSync"
+ "handleUserRegistrationForUser:repair:newPasswordUser:newSmartCardUser:notified:profile:"
+ "initWithTokenID:"
+ "isNewPasswordUser"
+ "isNewSmartCarddUser"
+ "keyForData:context:"
+ "keyHash"
+ "keyUsage"
+ "keychainAttributes"
+ "krb5_parse_name failed when importing enterprise kerberos entry."
+ "newPasswordUser"
+ "newSmartCardUser"
+ "newUserBindingComplete"
+ "pwd"
+ "requestUserAuthenticationSyncPassword:completion:"
+ "retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:"
+ "retrieveIdentityForTokenId:context:forSigning:hash:identity:"
+ "sc"
+ "screenUnlocked"
+ "sepKeyWithContext:"
+ "sessionWithLAContext:error:"
+ "setAmr:"
+ "setCanLogin:"
+ "setKeyHash:"
+ "setLocalizedFallbackTitle:"
+ "setLocalizedReason:"
+ "setNewPasswordUser:"
+ "setNewSmartCardUser:"
+ "setNewUserBindingComplete:"
+ "setOptionCallerIconPath:"
+ "setOptionFallbackVisible:"
+ "setScreenUnlocked:"
+ "setSmartCardHash:"
+ "setTokenId:"
+ "setTouchIDAuthenticationAllowableReuseDuration:"
+ "setUserSEPKeyBiometricPolicy:"
+ "setUserSEPKeyInvalid:"
+ "setWrapHash:"
+ "set__screenUnlockHandler:"
+ "showAlertMessage:messageText:completion:"
+ "sleepForTimeInterval:"
+ "smartCardHash"
+ "stringForSEPBiometricPolicy:"
+ "tokenId"
+ "userSEPKeyBiometricPolicy"
+ "userSEPKeyInvalid"
+ "v40@0:8B16B20B24B28@32"
+ "v48@0:8@16B24B28B32B36@40"
+ "v64@0:8Q16@24@32@40@48@56"
+ "waitForScreenUnlockithCompletion:"
+ "wrapHash"
- "\x1f\t\x1f\b"
- "\"\x11%\x14"
- "+[POSecKeyHelper keyForData:]"
- "-[POAgentAuthenticationProcess handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:]"
- "-[POAgentAuthenticationProcess handleUserRegistrationForUser:repair:newUser:notified:profile:]"
- "-[POAgentAuthenticationProcess requestUserAuthenticationWithCompletion:]"
- "-[POAgentAuthenticationProcess showAlertMessage:completion:]"
- "-[POTokenHelper findNameForTokenId:returningHash:wrapHash:]"
- "-[POTokenHelper findTokenIdForSmartCardAMUser:]"
- "-[POTokenHelper findTokenIdForSmartCardBoundUser:]"
- "@40@0:8@16^@24^@32"
- "AssertMacros: %s, %s file: %s, line: %d, value: %ld\n"
- "B44@0:8@16@24B32^^{__SecIdentity}36"
- "B52@0:8@16@24B32^^{__SecCertificate}36^^{__SecKey}44"
- "POUserStateNewUser"
- "T@?,C,N,V_screenUnlockHandler"
- "TB,GisNewUser,V_newUser"
- "User state is needs registration"
- "X\x11"
- "_handleLoginResult:authenticationContext:tokens:passwordContext:tokenId:"
- "_newUser"
- "_screenUnlockHandler"
- "find attribute mapping token id"
- "find bound token id"
- "findNameForTokenId:returningHash:wrapHash:"
- "findTokenIdForSmartCardAMUser:"
- "findTokenIdForSmartCardBoundUser:"
- "handleDeviceAndUserRegistrationForRepair:newUser:notified:profile:"
- "handleUserRegistrationForUser:repair:newUser:notified:profile:"
- "isNewUser"
- "newUser"
- "requestUserAuthenticationWithCompletion:"
- "retrieveCertAndKeyForTokenId:context:forSigning:certificate:privateKey:"
- "retrieveIdentityForTokenId:context:forSigning:identity:"
- "screenUnlockHandler"
- "setNewUser:"
- "setOptionCallerIconBundlePath:"
- "setScreenUnlockHandler:"
- "showAlertMessage:completion:"
- "v36@0:8B16B20B24@28"
- "v44@0:8@16B24B28B32@36"
- "v56@0:8Q16@24@32@40@48"

```
