## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-483.120.4.0.0
-  __TEXT.__text: 0x937cc
-  __TEXT.__auth_stubs: 0x1ab0
-  __TEXT.__objc_methlist: 0x5ff0
-  __TEXT.__const: 0x1854
-  __TEXT.__cstring: 0xa48b
-  __TEXT.__oslogstring: 0x19d7
-  __TEXT.__gcc_except_tab: 0x7ec
+635.0.0.0.0
+  __TEXT.__text: 0x967c4
+  __TEXT.__objc_methlist: 0x6250
+  __TEXT.__const: 0x18e4
+  __TEXT.__cstring: 0xaa1d
+  __TEXT.__oslogstring: 0x1e47
+  __TEXT.__gcc_except_tab: 0x6c4
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__swift5_typeref: 0x16a
-  __TEXT.__constg_swiftt: 0x374
-  __TEXT.__swift5_reflstr: 0x146
-  __TEXT.__swift5_fieldmd: 0x128
+  __TEXT.__swift5_typeref: 0x166
+  __TEXT.__constg_swiftt: 0x390
+  __TEXT.__swift5_reflstr: 0x124
+  __TEXT.__swift5_fieldmd: 0x150
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__swift5_proto: 0x40
-  __TEXT.__swift5_types: 0x38
-  __TEXT.__unwind_info: 0x2120
-  __TEXT.__eh_frame: 0x598
-  __TEXT.__objc_classname: 0xf93
-  __TEXT.__objc_methname: 0xce07
-  __TEXT.__objc_methtype: 0x2a03
-  __TEXT.__objc_stubs: 0x71a0
-  __DATA_CONST.__got: 0x920
-  __DATA_CONST.__const: 0x24a8
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__unwind_info: 0x2140
+  __TEXT.__eh_frame: 0x568
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2580
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b58
+  __DATA_CONST.__objc_selrefs: 0x2c90
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x1e0
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xd68
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0x74e0
-  __AUTH_CONST.__objc_const: 0x142d0
+  __DATA_CONST.__got: 0x9a8
+  __AUTH_CONST.__const: 0xc20
+  __AUTH_CONST.__cfstring: 0x78e0
+  __AUTH_CONST.__objc_const: 0x14cb8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x3460
-  __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x624
-  __DATA.__data: 0x1068
-  __DATA.__bss: 0xd31
+  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH.__objc_data: 0x35a0
+  __AUTH.__data: 0x1a8
+  __DATA.__objc_ivar: 0x64c
+  __DATA.__data: 0x11d0
+  __DATA.__bss: 0x761
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: A85C12D1-9DA9-3F33-998D-E9554442486F
-  Functions: 3676
-  Symbols:   12215
-  CStrings:  5113
+  UUID: 90241DAB-007D-34EE-9043-F3198EDA30B2
+  Functions: 3829
+  Symbols:   12502
+  CStrings:  2703
 
Symbols:
+ +[POCoreConfigurationUtil platformSSOEnabledForUsername:]
+ -[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]
+ -[POAuthenticationContext callbackResponse]
+ -[POAuthenticationContext setCallbackResponse:]
+ -[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]
+ -[POAuthenticationProcess addRedirectURIAndLoginHintToAuthorizationURL:context:]
+ -[POAuthenticationProcess addRedirectURIAndLoginHintToAuthorizationURL:context:].cold.1
+ -[POAuthenticationProcess createSignedOpenIDAuthorizationRequestWithURL:authorizationRequestValues:deviceConfiguration:error:]
+ -[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]
+ -[POAuthenticationProcess performOpenIDLoginUsingContext:completion:].cold.1
+ -[POAuthenticationProcess performOpenIDLoginUsingContext:completion:].cold.2
+ -[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]
+ -[POAuthenticationProcess retrieveOpenIDAuthorizationRequestUsingContext:completion:]
+ -[POAuthenticationProcess retrieveOpenIDAuthorizationRequestUsingContext:completion:].cold.1
+ -[POAuthorizationRequestJWT .cxx_destruct]
+ -[POAuthorizationRequestJWT decodedBody]
+ -[POAuthorizationRequestJWT description]
+ -[POAuthorizationRequestJWT initWithString:]
+ -[POAuthorizationRequestJWT mutableCopy]
+ -[POAuthorizationRequestJWT setDecodedBody:]
+ -[POAuthorizationRequestJWT updateDecodedBody]
+ -[POAuthorizationRequestJWTBody client_id]
+ -[POAuthorizationRequestJWTBody mutableCopy]
+ -[POAuthorizationRequestJWTBody nonce]
+ -[POAuthorizationRequestJWTBody redirect_uri]
+ -[POAuthorizationRequestJWTBody response_type]
+ -[POAuthorizationRequestJWTBody scope]
+ -[POAuthorizationRequestJWTBody state]
+ -[POConfigurationCoreManager savePendingSSOTokens:forUserName:].cold.2
+ -[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]
+ -[PODaemonCoreConnection updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.2
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.3
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.4
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.5
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.6
+ -[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:].cold.7
+ -[PODaemonCoreProcess updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]
+ -[PODaemonCoreProcess updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:].cold.1
+ -[PODaemonCoreProcess writeData:toPath:saveError:].cold.3
+ -[PODeviceConfiguration allowQRCodeAsOfflinePassword]
+ -[PODeviceConfiguration allowWebLoginPasswordSync]
+ -[PODeviceConfiguration biometricIsRequired]
+ -[PODeviceConfiguration setAllowQRCodeAsOfflinePassword:]
+ -[PODeviceConfiguration setAllowWebLoginPasswordSync:]
+ -[PODeviceConfiguration setWebLoginURLAllowList:]
+ -[PODeviceConfiguration webLoginURLAllowList]
+ -[POLoginConfiguration authorizationURLKeypath]
+ -[POLoginConfiguration authorizationURL]
+ -[POLoginConfiguration fallbackFederationType]
+ -[POLoginConfiguration setAuthorizationURL:]
+ -[POLoginConfiguration setAuthorizationURLKeypath:]
+ -[POLoginConfiguration setFallbackFederationType:]
+ -[POLoginJWTBody subject_token]
+ -[POLoginJWTBody subject_token_type]
+ -[POMutableAuthorizationRequestJWT .cxx_destruct]
+ -[POMutableAuthorizationRequestJWT body]
+ -[POMutableAuthorizationRequestJWT description]
+ -[POMutableAuthorizationRequestJWT setBody:]
+ -[POMutableAuthorizationRequestJWTBody addCustomClaims:]
+ -[POMutableAuthorizationRequestJWTBody setClient_id:]
+ -[POMutableAuthorizationRequestJWTBody setNonce:]
+ -[POMutableAuthorizationRequestJWTBody setRedirect_uri:]
+ -[POMutableAuthorizationRequestJWTBody setResponse_type:]
+ -[POMutableAuthorizationRequestJWTBody setScope:]
+ -[POMutableAuthorizationRequestJWTBody setState:]
+ -[POMutableLoginJWTBody setSubject_token:]
+ -[POMutableLoginJWTBody setSubject_token_type:]
+ -[POTokenHelper findTokenIdForAccessKeyUser:tokenHash:]
+ -[POTokenHelper findTokenIdForAccessKeyUser:tokenHash:].cold.1
+ -[POUserLoginState context]
+ -[POUserLoginState setContext:]
+ GCC_except_table126
+ GCC_except_table151
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table57
+ _OBJC_CLASS_$_POAuthorizationRequestJWT
+ _OBJC_CLASS_$_POAuthorizationRequestJWTBody
+ _OBJC_CLASS_$_POMutableAuthorizationRequestJWT
+ _OBJC_CLASS_$_POMutableAuthorizationRequestJWTBody
+ _OBJC_IVAR_$_POAuthenticationContext._callbackResponse
+ _OBJC_IVAR_$_POAuthorizationRequestJWT._decodedBody
+ _OBJC_IVAR_$_PODeviceConfiguration._allowQRCodeAsOfflinePassword
+ _OBJC_IVAR_$_PODeviceConfiguration._allowWebLoginPasswordSync
+ _OBJC_IVAR_$_PODeviceConfiguration._webLoginURLAllowList
+ _OBJC_IVAR_$_POLoginConfiguration._authorizationURL
+ _OBJC_IVAR_$_POLoginConfiguration._authorizationURLKeypath
+ _OBJC_IVAR_$_POLoginConfiguration._fallbackFederationType
+ _OBJC_IVAR_$_POMutableAuthorizationRequestJWT._body
+ _OBJC_IVAR_$_POUserLoginState._context
+ _OBJC_METACLASS_$_POAuthorizationRequestJWT
+ _OBJC_METACLASS_$_POAuthorizationRequestJWTBody
+ _OBJC_METACLASS_$_POMutableAuthorizationRequestJWT
+ _OBJC_METACLASS_$_POMutableAuthorizationRequestJWTBody
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ __OBJC_$_INSTANCE_METHODS_POAuthorizationRequestJWT
+ __OBJC_$_INSTANCE_METHODS_POAuthorizationRequestJWTBody
+ __OBJC_$_INSTANCE_METHODS_POMutableAuthorizationRequestJWT
+ __OBJC_$_INSTANCE_METHODS_POMutableAuthorizationRequestJWTBody
+ __OBJC_$_INSTANCE_VARIABLES_POAuthorizationRequestJWT
+ __OBJC_$_INSTANCE_VARIABLES_POMutableAuthorizationRequestJWT
+ __OBJC_$_PROP_LIST_POAuthorizationRequestJWT
+ __OBJC_$_PROP_LIST_POAuthorizationRequestJWTBody
+ __OBJC_$_PROP_LIST_POMutableAuthorizationRequestJWT
+ __OBJC_$_PROP_LIST_POMutableAuthorizationRequestJWTBody
+ __OBJC_CLASS_PROTOCOLS_$_POMutableAuthorizationRequestJWTBody
+ __OBJC_CLASS_RO_$_POAuthorizationRequestJWT
+ __OBJC_CLASS_RO_$_POAuthorizationRequestJWTBody
+ __OBJC_CLASS_RO_$_POMutableAuthorizationRequestJWT
+ __OBJC_CLASS_RO_$_POMutableAuthorizationRequestJWTBody
+ __OBJC_METACLASS_RO_$_POAuthorizationRequestJWT
+ __OBJC_METACLASS_RO_$_POAuthorizationRequestJWTBody
+ __OBJC_METACLASS_RO_$_POMutableAuthorizationRequestJWT
+ __OBJC_METACLASS_RO_$_POMutableAuthorizationRequestJWTBody
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1075
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1078
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1078.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1084
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1084.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1090
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1090.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1096
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1096.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1097
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1097.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1104
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1104.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1110
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1110.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1114
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1114.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1118
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1118.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1121
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1121.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1124
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1124.cold.1
+ ___101-[PODaemonCoreConnection updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]_block_invoke
+ ___101-[PODaemonCoreConnection updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]_block_invoke.cold.1
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.348
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.348.cold.1
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.357
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.357.cold.1
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.367
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.367.cold.1
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.371
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.371.cold.1
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.381
+ ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.381.cold.1
+ ___104-[POJWTEncryptionECDHE_A256GCM decodeAndDecryptJWT:privateKey:otherInfo:psk:psk_id:authPublicKey:error:]_block_invoke.78
+ ___104-[POJWTEncryptionECDHE_A256GCM decodeAndDecryptJWT:privateKey:otherInfo:psk:psk_id:authPublicKey:error:]_block_invoke.78.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.106
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.106.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.113
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.113.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.119
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.119.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.125
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.125.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.131
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.131.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.137
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.137.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.143
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.143.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.89
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.89.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.93
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.93.cold.1
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.99
+ ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.99.cold.1
+ ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.1224
+ ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.1224.cold.1
+ ___126-[POAuthenticationProcess createSignedOpenIDAuthorizationRequestWithURL:authorizationRequestValues:deviceConfiguration:error:]_block_invoke
+ ___126-[POAuthenticationProcess createSignedOpenIDAuthorizationRequestWithURL:authorizationRequestValues:deviceConfiguration:error:]_block_invoke.cold.1
+ ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1215
+ ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1215.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.101
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.104
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.104.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.115
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.124
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.124.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.128
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.129
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.129.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.133
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.134
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.134.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.138
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.138.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.94
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.94.cold.1
+ ___160-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.cold.1
+ ___31-[POLoginJWTBody subject_token]_block_invoke
+ ___36-[POLoginJWTBody subject_token_type]_block_invoke
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.41
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.41.cold.1
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.60
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.60.cold.1
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.64
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.64.cold.1
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.68
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.68.cold.1
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.73
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.73.cold.1
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.77
+ ___36-[POTokenHelper insertTokenForUser:]_block_invoke.77.cold.1
+ ___36-[POUserConfiguration initWithData:]_block_invoke.158
+ ___37-[POLoginConfiguration initWithData:]_block_invoke.306
+ ___38-[POAuthorizationRequestJWTBody nonce]_block_invoke
+ ___38-[POAuthorizationRequestJWTBody scope]_block_invoke
+ ___38-[POAuthorizationRequestJWTBody state]_block_invoke
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke.192
+ ___42-[POAuthorizationRequestJWTBody client_id]_block_invoke
+ ___43-[PODaemonCoreConnection _connectToService]_block_invoke.82.cold.1
+ ___43-[PODaemonCoreConnection _connectToService]_block_invoke.84
+ ___43-[PODaemonCoreConnection _connectToService]_block_invoke.84.cold.1
+ ___43-[PODaemonCoreConnection _connectToService]_block_invoke.87
+ ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.104
+ ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.104.cold.1
+ ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.99
+ ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.99.cold.1
+ ___44-[POServiceCoreConnection _connectToService]_block_invoke.67
+ ___44-[POServiceCoreConnection _connectToService]_block_invoke.67.cold.1
+ ___45-[POAuthorizationRequestJWTBody redirect_uri]_block_invoke
+ ___46-[POAuthorizationRequestJWTBody response_type]_block_invoke
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.102
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.102.cold.1
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.111
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.111.cold.1
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.120
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.120.cold.1
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.129
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.129.cold.1
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.78
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.78.cold.1
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.87
+ ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.87.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.835
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.835.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.841
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.841.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.845
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.845.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.851
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.851.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.857
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.857.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.863
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.863.cold.1
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.869
+ ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.869.cold.1
+ ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.68
+ ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.68.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.782
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.782.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.788
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.788.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.794
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.794.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.800
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.800.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.806
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.806.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.812
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.812.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.818
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.818.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.822
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.822.cold.1
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.826
+ ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.826.cold.1
+ ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.76
+ ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.76.cold.1
+ ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.72
+ ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.72.cold.1
+ ___56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.95
+ ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1135
+ ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1135.cold.1
+ ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1154
+ ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1154.cold.1
+ ___59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.87
+ ___60-[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:]_block_invoke.83
+ ___60-[PODaemonCoreProcess _pendingSSOTokensForIdentifier:error:]_block_invoke.83.cold.1
+ ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.661
+ ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.661.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.716
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.716.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.726
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.726.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.730
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.730.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.734
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.734.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.747
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.747.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.760
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.760.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.764
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.764.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.768
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.768.cold.1
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.772
+ ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.772.cold.1
+ ___63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.113
+ ___63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.113.cold.1
+ ___63-[POConfigurationCoreManager saveStashedSSOTokens:forUserName:]_block_invoke.121
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.880
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.880.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.886
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.886.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.890
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.890.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.896
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.896.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.902
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.902.cold.1
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.908
+ ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.908.cold.1
+ ___66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.117
+ ___66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.117.cold.1
+ ___66-[POConfigurationCoreManager retrieveStashedSSOTokensForUserName:]_block_invoke.125
+ ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1189
+ ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1189.cold.1
+ ___67-[POConfigurationCoreManager updateLoginTypeForUserName:loginType:]_block_invoke.109
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1004
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1007
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1007.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1013
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1013.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1019
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1019.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1025
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1025.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1026
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1026.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1033
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1033.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1039
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1039.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1043
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1043.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1047
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1047.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1050
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1050.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1053
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1053.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1059
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1059.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1065
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1065.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1071
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1071.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1072
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.1072.cold.1
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.982
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.983
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.986
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.987
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.987.cold.1
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.990
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke.cold.1
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke_2
+ ___69-[POAuthenticationProcess performOpenIDLoginUsingContext:completion:]_block_invoke_2.cold.1
+ ___70-[POAuthenticationProcess performTokenRefreshUsingContext:completion:]_block_invoke.143
+ ___70-[POAuthenticationProcess performTokenRefreshUsingContext:completion:]_block_invoke.143.cold.1
+ ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.546
+ ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.546.cold.1
+ ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.552
+ ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.552.cold.1
+ ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.558
+ ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.558.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.398
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.398.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.399
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.399.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.406
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.406.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.418
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.418.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.422
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.422.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.432
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.432.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.445.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.452
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.452.cold.1
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.456
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.463
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke_2
+ ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke_2.cold.1
+ ___71-[POAuthenticationProcess performPasswordLoginUsingContext:completion:]_block_invoke.33
+ ___71-[POAuthenticationProcess performPasswordLoginUsingContext:completion:]_block_invoke.33.cold.1
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.689
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.689.cold.1
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.690
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.690.cold.1
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.694
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.700
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.705
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.706
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.701
+ ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.701.cold.1
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1157
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1157.cold.1
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1161
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1167
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1172
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1173
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1168
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1168.cold.1
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1242
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1242.cold.1
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1248
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1248.cold.1
+ ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.921
+ ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.921.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.664
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.664.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.668
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.674
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.675
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.675.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.679
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.684
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.680
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.680.cold.1
+ ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.685
+ ___77-[POAuthenticationProcess performNonceRequestWithContext:request:completion:]_block_invoke.489
+ ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke.916
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.490
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.490.cold.1
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.494
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.500
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.505
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.506
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.506.cold.1
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.510
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.501
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.501.cold.1
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.515
+ ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.177.cold.1
+ ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.183
+ ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.190
+ ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.190.cold.1
+ ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke_2.184
+ ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke_2.184.cold.1
+ ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.45
+ ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.48
+ ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.48.cold.1
+ ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.67
+ ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.67.cold.1
+ ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.199
+ ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.199.cold.1
+ ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.210
+ ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.210.cold.1
+ ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.214
+ ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.214.cold.1
+ ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.277
+ ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.277.cold.1
+ ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.292
+ ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.293
+ ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke_2.288
+ ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke_2.288.cold.1
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1192
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1192.cold.1
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1196
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1202
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1207
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1208
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1203
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1203.cold.1
+ ___85-[POAuthenticationProcess _performDynamicWSTrustPasswordLoginWithContext:completion:]_block_invoke.154
+ ___85-[POAuthenticationProcess retrieveOpenIDAuthorizationRequestUsingContext:completion:]_block_invoke
+ ___85-[POAuthenticationProcess retrieveOpenIDAuthorizationRequestUsingContext:completion:]_block_invoke.cold.1
+ ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1179
+ ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1179.cold.1
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke.947
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke.950
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke.950.cold.1
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke.954
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke.cold.1
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke_2
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke_2.955
+ ___88-[POAuthenticationProcess _retrieveDynamicOpenIDAuthorizationURLWithContext:completion:]_block_invoke_2.cold.1
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.237
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.237.cold.1
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.241
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.257
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.257.cold.1
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.261
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.271
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.250
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.250.cold.1
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.263
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.263.cold.1
+ ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.272
+ ___92-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]_block_invoke
+ ___92-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]_block_invoke.101
+ ___92-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]_block_invoke.101.cold.1
+ ___92-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]_block_invoke.107
+ ___92-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]_block_invoke.cold.1
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.322
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.322.cold.1
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.332
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.337
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.339
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke_2.333
+ ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke_2.333.cold.1
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.963
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.963.cold.1
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.964
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.967
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.969
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.970
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.970.cold.1
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.971
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.978
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke.cold.1
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.968
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.968.cold.1
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.979
+ ___95-[POAuthenticationProcess performOpenIDPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.cold.1
+ ___block_descriptor_48_e8_32s40r_e20_v20?0B8"NSError"12lr40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e35_v32?0Q8"NSURL"16"NSDictionary"24ls48l8s32l8s40l8
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.152
+ ___block_descriptor_tmp.155
+ ___block_descriptor_tmp.182
+ ___block_literal_global.104
+ ___block_literal_global.118
+ ___block_literal_global.124
+ ___block_literal_global.1508
+ ___block_literal_global.1512
+ ___block_literal_global.152
+ ___block_literal_global.154
+ ___block_literal_global.157
+ ___block_literal_global.184
+ ___block_literal_global.218
+ ___block_literal_global.226
+ ___block_literal_global.247
+ ___block_literal_global.258
+ ___block_literal_global.404
+ ___block_literal_global.49
+ ___block_literal_global.500
+ ___block_literal_global.52
+ ___block_literal_global.60
+ ___block_literal_global.618
+ ___block_literal_global.86
+ ___block_literal_global.89
+ ___block_literal_global.94
+ ___der_key_expert_hidden_keys_support
+ ___stderrp
+ ___swift_memcpy1_1
+ ___swift_noop_void_return
+ __aks_remote_peer_drop
+ __aks_remote_peer_drop.cold.1
+ __aks_remote_peer_get_state
+ _aks_pki_token_challenge_get_ec_pub
+ _aks_pki_token_challenge_get_mode
+ _aks_pki_token_challenge_get_usk
+ _aks_pki_token_challenge_get_version
+ _aks_pki_token_get_info
+ _aks_pki_token_list
+ _aks_pki_token_op_register
+ _aks_pki_token_op_set_password
+ _aks_pki_token_op_unlock
+ _aks_pki_token_op_verify
+ _aks_pki_token_register
+ _aks_pki_token_register_internal
+ _aks_pki_token_request_challenge
+ _aks_pki_token_unregister
+ _aks_pki_token_unregister.cold.1
+ _aks_remote_peer_drop_v2
+ _aks_remote_peer_get_state_v2
+ _aks_se_get_reset_sig.cold.1
+ _aks_se_get_reset_sig.cold.2
+ _associated conformance 15PlatformSSOCore0A11SSOFeaturesOSHAASQ
+ _decode_continuity_peer_modify_internal_params
+ _decode_pfk_bulk_data
+ _der_key_expert_hidden_keys_support
+ _encode_continuity_peer_modify_internal_params
+ _kPOUserLoginStateContextDisplayName
+ _kPOUserLoginStateContextLoginUsername
+ _kPSSOAHPXPCServiceName
+ _kPSSOPAMServiceName
+ _kPlatformSSOOpenIDRedirectScheme
+ _kPlatformSSOOpenIDRedirectURI
+ _kSecurityAgentUid
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_retrieveDynamicOpenIDAuthorizationURLWithContext:completion:
+ _objc_msgSend$_verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:
+ _objc_msgSend$addRedirectURIAndLoginHintToAuthorizationURL:context:
+ _objc_msgSend$allowQRCodeAsOfflinePassword
+ _objc_msgSend$allowWebLoginPasswordSync
+ _objc_msgSend$authorizationURL
+ _objc_msgSend$authorizationURLKeypath
+ _objc_msgSend$callbackResponse
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$createSignedOpenIDAuthorizationRequestWithURL:authorizationRequestValues:deviceConfiguration:error:
+ _objc_msgSend$fallbackFederationType
+ _objc_msgSend$performOpenIDLoginUsingContext:completion:
+ _objc_msgSend$performOpenIDPreAuthenticationRequestWithContext:request:completion:
+ _objc_msgSend$requestWithURL:
+ _objc_msgSend$requestWithURL:cachePolicy:timeoutInterval:
+ _objc_msgSend$setCallbackResponse:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setSubject_token:
+ _objc_msgSend$setSubject_token_type:
+ _objc_msgSend$setWithObjects:
+ _objc_msgSend$updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:
+ _objc_msgSend$updateLoginStateForUserName:state:loginDate:loginType:context:
+ _objc_msgSend$webLoginURLAllowList
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _swift_lookUpClassMethod
+ _swift_release_x20
+ _swift_release_x23
+ _swift_retain_x20
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_willThrowTypedImpl
+ _symbolic _____ 15PlatformSSOCore0A11SSOFeaturesO
- -[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]
- -[PODaemonCoreConnection updateLoginStateForIdentifier:state:loginDate:loginType:completion:]
- -[PODaemonCoreProcess updateLoginStateForIdentifier:state:loginDate:loginType:completion:]
- -[PODaemonCoreProcess updateLoginStateForIdentifier:state:loginDate:loginType:completion:].cold.1
- -[POUserLoginState setlastLogin:]
- GCC_except_table123
- GCC_except_table147
- GCC_except_table348
- GCC_except_table39
- GCC_except_table390
- GCC_except_table403
- GCC_except_table44
- GCC_except_table47
- GCC_except_table50
- GCC_except_table53
- GCC_except_table56
- GCC_except_table91
- _AKSGetKeyBagStats
- _AKSGetStashStats
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1000
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1000.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1006
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1006.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1012
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1012.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1013
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1013.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1020
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1020.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1026
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1026.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1030
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1030.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1034
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1034.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1037
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1037.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1040
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1040.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.991
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.994
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.994.cold.1
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.342
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.342.cold.1
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.351
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.351.cold.1
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.355
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.355.cold.1
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.365
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.365.cold.1
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.369
- ___104-[POAuthenticationProcess validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:]_block_invoke.369.cold.1
- ___104-[POJWTEncryptionECDHE_A256GCM decodeAndDecryptJWT:privateKey:otherInfo:psk:psk_id:authPublicKey:error:]_block_invoke.79
- ___104-[POJWTEncryptionECDHE_A256GCM decodeAndDecryptJWT:privateKey:otherInfo:psk:psk_id:authPublicKey:error:]_block_invoke.79.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.100
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.100.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.107
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.107.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.114
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.114.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.120
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.120.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.126
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.126.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.132
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.132.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.138
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.138.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.144
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.144.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.90
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.90.cold.1
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.94
- ___113-[POJWTEncryptionECDHE_A256GCM encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:]_block_invoke.94.cold.1
- ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.1140
- ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.1140.cold.1
- ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1131
- ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1131.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.101
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.104
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.104.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.115
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.124
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.124.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.128
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.129
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.129.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.133
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.133.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.94
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.94.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.42
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.42.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.61
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.61.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.65
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.65.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.69
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.69.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.74
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.74.cold.1
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.78
- ___36-[POTokenHelper insertTokenForUser:]_block_invoke.78.cold.1
- ___36-[POUserConfiguration initWithData:]_block_invoke.159
- ___37-[POLoginConfiguration initWithData:]_block_invoke.300
- ___38-[PODeviceConfiguration initWithData:]_block_invoke.186
- ___43-[PODaemonCoreConnection _connectToService]_block_invoke.77
- ___43-[PODaemonCoreConnection _connectToService]_block_invoke.77.cold.1
- ___43-[PODaemonCoreConnection _connectToService]_block_invoke.79
- ___43-[PODaemonCoreConnection _connectToService]_block_invoke.79.cold.1
- ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.100
- ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.100.cold.1
- ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.105
- ___44-[POMutableJWTHeader addEphemeralPublicKey:]_block_invoke.105.cold.1
- ___44-[POServiceCoreConnection _connectToService]_block_invoke.64
- ___44-[POServiceCoreConnection _connectToService]_block_invoke.64.cold.1
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.105
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.105.cold.1
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.114
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.114.cold.1
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.123
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.123.cold.1
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.72
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.72.cold.1
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.81
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.81.cold.1
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.90
- ___47-[POAuthenticationProcess findAlgorithmForKey:]_block_invoke.90.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.816
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.816.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.822
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.822.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.826
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.826.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.832
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.832.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.838
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.838.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.844
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.844.cold.1
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.850
- ___54-[POAuthenticationProcess validatePartyUInfo:context:]_block_invoke.850.cold.1
- ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.69
- ___54-[POConfigurationCoreManager currentUserConfiguration]_block_invoke.69.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.763
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.763.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.769
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.769.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.775
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.775.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.781
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.781.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.787
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.787.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.793
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.793.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.799
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.799.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.803
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.803.cold.1
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.807
- ___55-[POAuthenticationProcess validateIdToken:context:key:]_block_invoke.807.cold.1
- ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.77
- ___55-[POConfigurationCoreManager currentLoginConfiguration]_block_invoke.77.cold.1
- ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.73
- ___56-[POConfigurationCoreManager currentDeviceConfiguration]_block_invoke.73.cold.1
- ___56-[POConfigurationCoreManager userLoginStateForUserName:]_block_invoke.96
- ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1051
- ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1051.cold.1
- ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1070
- ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1070.cold.1
- ___59-[POConfigurationCoreManager userConfigurationForUserName:]_block_invoke.88
- ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.642
- ___61-[POAuthenticationProcess createLoginRequestWithContext:jwt:]_block_invoke.642.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.697
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.697.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.707
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.707.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.711
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.711.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.715
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.715.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.728
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.728.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.741
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.741.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.745
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.745.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.749
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.749.cold.1
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.753
- ___63-[POAuthenticationProcess findKey:inJWKSData:rootCertificates:]_block_invoke.753.cold.1
- ___63-[POConfigurationCoreManager savePendingSSOTokens:forUserName:]_block_invoke.111
- ___63-[POConfigurationCoreManager saveStashedSSOTokens:forUserName:]_block_invoke.119
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.861
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.861.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.867
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.867.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.871
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.871.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.877
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.877.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.883
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.883.cold.1
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.889
- ___64-[POAuthenticationProcess validatePartyVInfo:context:publicKey:]_block_invoke.889.cold.1
- ___66-[POConfigurationCoreManager retrievePendingSSOTokensForUserName:]_block_invoke.115
- ___66-[POConfigurationCoreManager retrieveStashedSSOTokensForUserName:]_block_invoke.123
- ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1105
- ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1105.cold.1
- ___67-[POConfigurationCoreManager updateLoginTypeForUserName:loginType:]_block_invoke.110
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.920
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.923
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.923.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.929
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.929.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.935
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.935.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.941
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.941.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.942
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.942.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.949
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.949.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.955
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.955.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.959
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.959.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.963
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.963.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.966
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.966.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.969
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.969.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.975
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.975.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.981
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.981.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.987
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.987.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.988
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.988.cold.1
- ___70-[POAuthenticationProcess performTokenRefreshUsingContext:completion:]_block_invoke.131
- ___70-[POAuthenticationProcess performTokenRefreshUsingContext:completion:]_block_invoke.137.cold.1
- ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.539
- ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.539.cold.1
- ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.545
- ___71-[POAuthenticationProcess createLoginJWTWithContext:embeddedAssertion:]_block_invoke.545.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.386
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.386.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.393
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.393.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.400
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.400.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.412
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.412.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.416
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.416.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.420
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.420.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.433
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.433.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.446
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.446.cold.1
- ___71-[POAuthenticationProcess performLoginWithContext:loginJWT:completion:]_block_invoke.451.cold.1
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.670
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.670.cold.1
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.671
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.671.cold.1
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.675
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.681
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.686
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke.687
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.682
- ___74-[POAuthenticationProcess retrieveSigningKeyWithContext:keyId:completion:]_block_invoke_2.682.cold.1
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1073
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1073.cold.1
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1077
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1083
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1088
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1089
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1084
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1084.cold.1
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1158
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1158.cold.1
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1164
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1164.cold.1
- ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.902
- ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.902.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.645
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.645.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.649
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.655
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.656
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.656.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.660
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke.665
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.661
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.661.cold.1
- ___77-[POAuthenticationProcess performLoginRequestWithContext:request:completion:]_block_invoke_2.666
- ___77-[POAuthenticationProcess performNonceRequestWithContext:request:completion:]_block_invoke.482
- ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke.897
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.483
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.483.cold.1
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.487
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.493
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.498
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.499
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.499.cold.1
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke.503
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.494
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.494.cold.1
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.508
- ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.159
- ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.165.cold.1
- ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.184
- ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke.184.cold.1
- ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke_2.178
- ___78-[POAuthenticationProcess _performWSTrustPasswordLoginWithContext:completion:]_block_invoke_2.178.cold.1
- ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.39
- ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.42
- ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.42.cold.1
- ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.49
- ___81-[POAuthenticationProcess _performEmbeddedAssertionLoginUsingContext:completion:]_block_invoke.49.cold.1
- ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.193
- ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.193.cold.1
- ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.204
- ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.204.cold.1
- ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.208
- ___81-[POAuthenticationProcess _performEncryptedPasswordLoginUsingContext:completion:]_block_invoke.208.cold.1
- ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.271
- ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.271.cold.1
- ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.275
- ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke.286
- ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke_2.282
- ___82-[POAuthenticationProcess performWSTrustMexRequestWithContext:request:completion:]_block_invoke_2.282.cold.1
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1108
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1108.cold.1
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1112
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1118
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1123
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1124
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1119
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1119.cold.1
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.102
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.102.cold.1
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.108
- ___84-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]_block_invoke.cold.1
- ___85-[POAuthenticationProcess _performDynamicWSTrustPasswordLoginWithContext:completion:]_block_invoke.148
- ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1095
- ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1095.cold.1
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.231
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.231.cold.1
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.235
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.243
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.251
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.251.cold.1
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke.265
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.244
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.244.cold.1
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.257
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.257.cold.1
- ___89-[POAuthenticationProcess performPreAuthenticationRequestWithContext:request:completion:]_block_invoke_2.266
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.316
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.316.cold.1
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.320
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.331
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke.333
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke_2.327
- ___93-[POAuthenticationProcess performWSTrustAuthenticationRequestWithContext:request:completion:]_block_invoke_2.327.cold.1
- ___93-[PODaemonCoreConnection updateLoginStateForIdentifier:state:loginDate:loginType:completion:]_block_invoke
- ___93-[PODaemonCoreConnection updateLoginStateForIdentifier:state:loginDate:loginType:completion:]_block_invoke.cold.1
- ___block_descriptor_tmp.128
- ___block_descriptor_tmp.140
- ___block_descriptor_tmp.151
- ___block_descriptor_tmp.154
- ___block_descriptor_tmp.181
- ___block_literal_global.102
- ___block_literal_global.114
- ___block_literal_global.125
- ___block_literal_global.1418
- ___block_literal_global.1422
- ___block_literal_global.153
- ___block_literal_global.156
- ___block_literal_global.158
- ___block_literal_global.183
- ___block_literal_global.219
- ___block_literal_global.227
- ___block_literal_global.245
- ___block_literal_global.254
- ___block_literal_global.405
- ___block_literal_global.482
- ___block_literal_global.50
- ___block_literal_global.51
- ___block_literal_global.601
- ___block_literal_global.61
- ___block_literal_global.81
- ___block_literal_global.87
- ___block_literal_global.90
- ___block_literal_global.95
- __swift_dead_method_stub
- _aks_fv_new_sibling_vek
- _aks_remote_peer_drop.cold.1
- _aks_smartcard_unregister.cold.1
- _objc_msgSend$_verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:
- _objc_msgSend$updateLoginStateForIdentifier:state:loginDate:loginType:completion:
- _seconds_to_day
- _stash_stats_deserialize
- _swift_release_n
- _symbolic _____Sg 9CryptoKit10Curve25519O7SigningO9PublicKeyV
- _symbolic ______pSg 10Foundation15ContiguousBytesP
CStrings:
+ "%s contextData length = %lu on %@"
+ "%s fileURL = %{public}@ on %@"
+ "%s identifier = %{public}@, context = %{public}@ on %@"
+ "%s state: %{public}@, loginDate: %{public}@, loginType: %{public}@, context: %{public}@ on %@"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n"
+ ", "
+ "-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:callbackResponse:deviceConfiguration:loginConfiguration:forAuthorization:completion:]"
+ "-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:context:]"
+ "-[PODaemonCoreProcess updateLoginStateForIdentifier:state:loginDate:loginType:context:completion:]"
+ "-[PODaemonCoreProcess writeData:toPath:saveError:]"
+ "-[POTokenHelper findTokenIdForAccessKeyUser:tokenHash:]"
+ "AllowOpenIDForTouchIDFallback"
+ "Authorization URL: %{public}@"
+ "Failed to create signed authorization request."
+ "Failed to get data protection class for given path %s with errno %s (%d)\n"
+ "Failed to sign authorization request."
+ "File did not exist (ENOENT): %{public}@"
+ "Missing authorization response."
+ "None (%@)"
+ "OpenID login failed"
+ "POLoginTypeOpenID"
+ "POLoginTypeTemporarySessionFVUnlock"
+ "POUserStateNewOpenIDUser"
+ "POUserStateNewSecureEnclaveUser"
+ "PlatformSSO_OpenIDAuth"
+ "Preauthentication response contains authorizationRequest values"
+ "Requesting OpenID authorization request"
+ "RequireTouchID"
+ "RequireTouchIDOrWatch"
+ "Sending OpenID preauthentication request: %{public}@"
+ "Starting OpenID authentication"
+ "Successfully removed file: %{public}@"
+ "Using authorizationURL: %{private}@"
+ "_aks_remote_peer_drop"
+ "_aks_remote_peer_get_state"
+ "aks_pki_token_get_info"
+ "aks_pki_token_list"
+ "aks_pki_token_op_register"
+ "aks_pki_token_op_set_password"
+ "aks_pki_token_op_unlock"
+ "aks_pki_token_op_verify"
+ "aks_pki_token_register_internal"
+ "aks_pki_token_request_challenge"
+ "aks_pki_token_unregister"
+ "authorizationRequest"
+ "authorizationURL"
+ "cached tokenData size = %{public}@ for identifier: %{public}@"
+ "com.apple.PlatformSSO.AuthenticationHintsProvider"
+ "com.apple.PlatformSSO://callback"
+ "decode_pfk_bulk_data"
+ "decode_pfk_bulk_entry"
+ "displayName"
+ "invalid federationType"
+ "invalid federationType for OpenID"
+ "loaded tokenData size = %{public}@"
+ "loginUsername"
+ "login_hint"
+ "mapped userName to identifier: %{public}@"
+ "nil (will clear)"
+ "no pending tokens found in cache for identifier: %{public}@"
+ "pending sso tokens loaded successfully from file: %{public}@, size = %{public}@"
+ "pending tokens found in cache, size = %{public}@"
+ "platformSSOLoginUI"
+ "platformsso-authorization-request+jwt"
+ "psso"
+ "redirect_uri"
+ "request=%@"
+ "response_type"
+ "retrievePendingSSOTokens XPC call returned no data for userName: %{public}@, error: %{public}@"
+ "retrievePendingSSOTokens XPC call succeeded for userName: %{public}@, size = %{public}@"
+ "retrieving sso tokens from disk at: %{public}@"
+ "savePendingSSOTokens XPC call failed for userName: %{public}@, error: %{public}@"
+ "savePendingSSOTokens XPC call succeeded for userName: %{public}@"
+ "subject_token"
+ "subject_token_type"
+ "tokenData size = %{public}@"
+ "urn:apple:platformsso:authorization-code-response"
+ "urn:ietf:params:oauth:grant-type:token-exchange"
+ "v32@?0Q8@\"NSURL\"16@\"NSDictionary\"24"
- "#16@0:8"
- "#24@0:8@16"
- "%s file = %{public}@, data = %{public}@, %{public}@ on %@"
- "%s state: %{public}@, loginDate: %{public}@, loginDate: %{public}@ on %@"
- ","
- "-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]"
- "-[POConfigurationCoreManager updateLoginStateForUserName:state:loginDate:loginType:]"
- "-[PODaemonCoreProcess updateLoginStateForIdentifier:state:loginDate:loginType:completion:]"
- ".cxx_destruct"
- "?"
- "@\"<POJWKSStorageProvider>\""
- "@\"<POMutableJWTBody>\""
- "@\"<POUserIdentifierProvider>\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSData\"24@0:8@\"NSString\"16"
- "@\"NSData\"32@0:8@\"NSData\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
- "@\"NSData\"40@0:8@\"NSData\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^@32"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMapTable\""
- "@\"NSMutableArray\""
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSObject\""
- "@\"NSOperationQueue\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"40@0:8@\"POMutableJWT\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecCertificate=}32"
- "@\"NSString\"48@0:8@\"POMutableJWT\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecCertificate=}32^@40"
- "@\"NSString\"80@0:8@\"POMutableJWT\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@\"NSString\"32@\"NSData\"40@\"NSData\"48^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}56@\"NSData\"64^@72"
- "@\"NSURL\""
- "@\"NSURLSession\""
- "@\"NSXPCConnection\""
- "@\"POAssertionJWTBody\""
- "@\"POAuthenticationProcess\""
- "@\"POConfigurationVersion\""
- "@\"PODaemonCoreConnection\""
- "@\"PODeviceConfiguration\""
- "@\"POIDTokenJWTBody\""
- "@\"POJWTHeader\""
- "@\"POKeyExchangeRequestJWTBody\""
- "@\"POKeyExchangeResponseJWTBody\""
- "@\"POKeyRequestJWTBody\""
- "@\"POKeyResponseJWTBody\""
- "@\"POKeychainHelper\""
- "@\"POLoginConfiguration\""
- "@\"POLoginJWTBody\""
- "@\"POLoginResponseJWTBody\""
- "@\"POMutableAssertionJWTBody\""
- "@\"POMutableIDTokenJWTBody\""
- "@\"POMutableJWTHeader\""
- "@\"POMutableKeyExchangeRequestJWTBody\""
- "@\"POMutableKeyExchangeResponseJWTBody\""
- "@\"POMutableKeyRequestJWTBody\""
- "@\"POMutableKeyResponseJWTBody\""
- "@\"POMutableLoginJWTBody\""
- "@\"POSOAPCode\""
- "@\"POSOAPEnvelope\""
- "@\"POSOAPFaultDetail\""
- "@\"POSOAPReason\""
- "@\"POSOAPSubcode\""
- "@\"POSOAPText\""
- "@\"POServiceCoreConnection\""
- "@\"POTokenHelper\""
- "@\"POUserConfiguration\""
- "@\"POUserLoginConfiguration\""
- "@\"POWSTrustAppliesToType\""
- "@\"POWSTrustEndpointReferenceType\""
- "@\"POWSTrustKeyIdentifierType\""
- "@\"POWSTrustProcess\""
- "@\"POWSTrustReferenceType\""
- "@\"POWSTrustRequestedSecurityTokenType\""
- "@\"POWSTrustSecurityTokenReferenceType\""
- "@\"POWSTrustTimestampType\""
- "@\"POWSTrustUsernameTokenType\""
- "@\"POXMLContext\""
- "@\"POXMLXPathContext\""
- "@\"POXMLXPathResult\""
- "@\"POXSDefinition\"16@0:8"
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8#16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSData\"16"
- "@24@0:8@\"NSDictionary\"16"
- "@24@0:8@16"
- "@24@0:8I16B20"
- "@24@0:8Q16"
- "@24@0:8^@16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8^{__SecCertificate=}16"
- "@24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16^{__SecCertificate=}24"
- "@32@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
- "@32@0:8^{__CFString=}16@24"
- "@32@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16^@24"
- "@32@0:8q16@24"
- "@36@0:8@16@24B32"
- "@36@0:8B16@20@28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24#32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32"
- "@40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32"
- "@40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^@32"
- "@40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecCertificate=}32"
- "@40@0:8^{__CFString=}16@24@32"
- "@40@0:8q16@24@32"
- "@40@0:8r^{__CFString=}16@24@32"
- "@44@0:8@16@24B32@36"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32^{__SecCertificate=}40"
- "@48@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecCertificate=}32^@40"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32^{__SecCertificate=}40^@48"
- "@80@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32@40@48^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}56@64^@72"
- "@88@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@40@48@56^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}64@72^@80"
- "@?"
- "@?16@0:8"
- "AKSGetKeyBagStats"
- "AKSGetStashStats"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B24@0:8^{__SecAccessControl=}16"
- "B24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
- "B28@0:8^{__CFString=}16B24"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@\"POJWT\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
- "B32@0:8@16@24"
- "B32@0:8@16Q24"
- "B32@0:8@16^@24"
- "B32@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
- "B40@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32"
- "B40@0:8@\"NSData\"16@\"NSData\"24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24^@32"
- "B40@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32"
- "B40@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^^{__SecKey}32"
- "B48@0:8@16@24@32^@40"
- "B48@0:8@16@24^^{__SecCertificate}32^^{__SecKey}40"
- "B48@0:8@16Q24@32Q40"
- "B48@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32^@40"
- "B52@0:8@16@24B32@36^^{__SecIdentity}44"
- "B56@0:8@16@24@32@40^@48"
- "B56@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24^^{__SecCertificate}32^@40^@48"
- "B60@0:8@16@24B32@36^^{__SecCertificate}44^^{__SecKey}52"
- "B64@0:8@16@24@32^@40^@48^@56"
- "B72@0:8@\"POJWT\"16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@\"NSString\"32@\"NSData\"40@\"NSData\"48^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}56^@64"
- "B72@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32@40@48^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}56^@64"
- "B80@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@40@48@56^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}64^@72"
- "Base64URL"
- "HTTPBody"
- "HTTPMethod"
- "I16@0:8"
- "JSONObjectWithData:options:error:"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "NSXPCListenerDelegate"
- "POAnalytics"
- "POAssertionJWTBody"
- "POAssertionTokenJWT"
- "POBaseSystemSupport"
- "POConcatKDF"
- "POConfigurationCoreManager"
- "POConstantCoreUtil"
- "PODaemonCoreProtocol"
- "POError"
- "POIDTokenJWT"
- "POIDTokenJWTBody"
- "POInternalProtocols"
- "POJWKSStorageProvider"
- "POJWTEncryptionAlgorithm"
- "POJWTEncryptionECDHE_A256GCM"
- "POJWTSigningAlgorithm"
- "POKerberosMapping"
- "POKerberosStatus"
- "POKeyExchangeRequestJWT"
- "POKeyExchangeRequestJWTBody"
- "POKeyExchangeResponseJWT"
- "POKeyExchangeResponseJWTBody"
- "POKeyRequestJWT"
- "POKeyRequestJWTBody"
- "POKeyResponseJWT"
- "POKeyResponseJWTBody"
- "POLoginJWTBody"
- "POLoginResponseJWTBody"
- "POLoginResponseTokenJWT"
- "POLoginTokenJWT"
- "POMemoryJWKSStorageProvider"
- "POMutableAssertionJWTBody"
- "POMutableAssertionTokenJWT"
- "POMutableIDTokenJWT"
- "POMutableIDTokenJWTBody"
- "POMutableJWT"
- "POMutableJWTBody"
- "POMutableJWTHeader"
- "POMutableKeyExchangeRequestJWT"
- "POMutableKeyExchangeRequestJWTBody"
- "POMutableKeyExchangeResponseJWT"
- "POMutableKeyExchangeResponseJWTBody"
- "POMutableKeyRequestJWT"
- "POMutableKeyRequestJWTBody"
- "POMutableKeyResponseJWT"
- "POMutableKeyResponseJWTBody"
- "POMutableLoginJWTBody"
- "POMutableLoginResponseJWTBody"
- "POMutableLoginResponseTokenJWT"
- "POMutableLoginTokenJWT"
- "POMutableTokenConfigJWTBody"
- "POMutableWrappedTokenJWTBody"
- "POPlatformSSOCoreListener"
- "POSOAPBody"
- "POSOAPCode"
- "POSOAPDocument"
- "POSOAPEnvelope"
- "POSOAPFault"
- "POSOAPFaultDetail"
- "POSOAPHeader"
- "POSOAPReason"
- "POSOAPSubcode"
- "POSOAPText"
- "POServiceCoreProtocol"
- "POSessionDelegate"
- "POTokenConfigJWTBody"
- "POTokenInfo"
- "POWSTrust13RequestSecurityTokenResponseCollectionType"
- "POWSTrust13RequestSecurityTokenResponseType"
- "POWSTrust13RequestSecurityTokenType"
- "POWSTrust2005RequestSecurityTokenResponseType"
- "POWSTrust2005RequestSecurityTokenType"
- "POWSTrustActionType"
- "POWSTrustAppliesToType"
- "POWSTrustBaseRequestType"
- "POWSTrustEndpointReferenceType"
- "POWSTrustKeyIdentifierType"
- "POWSTrustMessageIDType"
- "POWSTrustMexResponse"
- "POWSTrustReferenceType"
- "POWSTrustRelatesToType"
- "POWSTrustReplyToType"
- "POWSTrustRequest"
- "POWSTrustRequestedSecurityTokenType"
- "POWSTrustResponse"
- "POWSTrustSecurityTokenReferenceType"
- "POWSTrustSecurityType"
- "POWSTrustTimestampType"
- "POWSTrustToType"
- "POWSTrustUsernameTokenType"
- "POWrappedTokenJWTBody"
- "POXMLContext"
- "POXMLNode"
- "POXMLXPathContext"
- "POXMLXPathResult"
- "POXSBase64BinaryDefinition"
- "POXSBooleanDefinition"
- "POXSChoiceDefinition"
- "POXSComplexTypeDefinition"
- "POXSDateDefinition"
- "POXSDateFormatterFactory"
- "POXSDateTimeDefinition"
- "POXSDefinition"
- "POXSDefinitionProvider"
- "POXSDefinitions"
- "POXSDoubleDefinition"
- "POXSDurationDefinition"
- "POXSElement"
- "POXSIntegerDefinition"
- "POXSNamespaces"
- "POXSNullDefinition"
- "POXSRFC3339DateDefinition"
- "POXSRawDataDefinition"
- "POXSRedactionInformation"
- "POXSSimpleTypeDefinition"
- "POXSStringDefinition"
- "POXSTimeDefinition"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q32@0:8@16@24"
- "Q40@0:8@16@24^@32"
- "SHA256"
- "SOAPBaseDocument"
- "Saving data to: %{public}@"
- "T#,R"
- "T#,R,N,V_type"
- "T@\"<POJWKSStorageProvider>\",&,N,V_jwksStorageProvider"
- "T@\"<POJWKSStorageProvider>\",&,V_jwksStorageProvider"
- "T@\"<POMutableJWTBody>\",&,V_body"
- "T@\"<POUserIdentifierProvider>\",&,V_userIdentifierProvider"
- "T@\"NSArray\",&,D"
- "T@\"NSArray\",&,D,N"
- "T@\"NSArray\",&,N,V_RequestSecurityTokenResponse"
- "T@\"NSArray\",C,N,V_Body"
- "T@\"NSArray\",C,N,V_Header"
- "T@\"NSArray\",C,N,V_administratorGroups"
- "T@\"NSArray\",C,N,V_createUserLoginTypes"
- "T@\"NSArray\",C,N,V_customDecryptionRequestValues"
- "T@\"NSArray\",C,N,V_customFederationUserPreauthenticationRequestValues"
- "T@\"NSArray\",C,N,V_customKeyExchangeRequestValues"
- "T@\"NSArray\",C,N,V_customKeyRequestValues"
- "T@\"NSArray\",C,N,V_customLoginRequestValues"
- "T@\"NSArray\",C,N,V_customNonceRequestValues"
- "T@\"NSArray\",C,N,V_customRefreshRequestValues"
- "T@\"NSArray\",C,N,V_jwksTrustedRootCertificates"
- "T@\"NSArray\",C,N,V_kerberosTicketMappings"
- "T@\"NSArray\",C,N,V_nonPlatformSSOAccounts"
- "T@\"NSArray\",C,N,V_otherGroups"
- "T@\"NSArray\",C,V_kerberosStatus"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,D"
- "T@\"NSArray\",R,V_kSupportedLoginResponseAlgorithms"
- "T@\"NSArray\",R,V_temporarySessionAccounts"
- "T@\"NSData\",&,D"
- "T@\"NSData\",&,N,V__accessTokenReaderIssuerCertificateData"
- "T@\"NSData\",&,N,V__accessTokenTerminalIdentityCertData"
- "T@\"NSData\",&,N,V__accessTokenTerminalIdentityKeyData"
- "T@\"NSData\",&,N,V__deviceEncryptionKeyData"
- "T@\"NSData\",&,N,V__deviceSigningKeyData"
- "T@\"NSData\",&,N,V__hpkeAuthPublicKeyData"
- "T@\"NSData\",&,N,V__loginRequestEncryptionPublicKeyData"
- "T@\"NSData\",&,N,V_loginRequestEncryptionAPVPrefix"
- "T@\"NSData\",&,V__sepKeyData"
- "T@\"NSData\",C,N,V_accessTokenReaderGroupIdentifier"
- "T@\"NSData\",C,N,V_accessTokenReaderTerminalCapabilityIdentifier"
- "T@\"NSData\",C,N,V_deviceConfigurationData"
- "T@\"NSData\",C,N,V_deviceContext"
- "T@\"NSData\",C,N,V_encryptionKeyData"
- "T@\"NSData\",C,N,V_hpkePsk"
- "T@\"NSData\",C,N,V_hpkePsk_id"
- "T@\"NSData\",C,N,V_keyHash"
- "T@\"NSData\",C,N,V_loginConfigurationData"
- "T@\"NSData\",C,N,V_loginRequestHpkePsk"
- "T@\"NSData\",C,N,V_loginRequestHpkePsk_id"
- "T@\"NSData\",C,N,V_wrapHash"
- "T@\"NSData\",C,V__credential"
- "T@\"NSData\",C,V__loginContext"
- "T@\"NSData\",C,V__setupContext"
- "T@\"NSData\",C,V__setupPINContext"
- "T@\"NSData\",C,V__setupWrapHash"
- "T@\"NSData\",C,V_smartCardHash"
- "T@\"NSData\",C,V_userDecryptionKeyHash"
- "T@\"NSData\",C,V_userUnlockHash"
- "T@\"NSData\",N,C"
- "T@\"NSData\",R,C,N"
- "T@\"NSDate\",&,D"
- "T@\"NSDate\",&,N,V_Created"
- "T@\"NSDate\",&,N,V_Expires"
- "T@\"NSDate\",&,N,V_created"
- "T@\"NSDate\",&,N,V_expires"
- "T@\"NSDate\",&,N,V_lastLogin"
- "T@\"NSDate\",&,N,V_lastLoginDate"
- "T@\"NSDate\",&,N,V_lastUpdated"
- "T@\"NSDate\",&,N,V_tokenExpires"
- "T@\"NSDate\",C,N,V_authGracePeriodStart"
- "T@\"NSDate\",C,N,V_lastCheckDate"
- "T@\"NSDate\",C,N,V_lastEncryptionKeyChange"
- "T@\"NSDate\",C,N,V_serverNonceReceived"
- "T@\"NSDate\",R"
- "T@\"NSDate\",R,D"
- "T@\"NSDate\",R,N,V_encryptionKeySaveDate"
- "T@\"NSDictionary\",&,D"
- "T@\"NSDictionary\",&,V_customAssertionRequestBodyClaims"
- "T@\"NSDictionary\",&,V_customAssertionRequestHeaderClaims"
- "T@\"NSDictionary\",&,V_customKeyExchangeRequestBodyClaims"
- "T@\"NSDictionary\",&,V_customKeyExchangeRequestHeaderClaims"
- "T@\"NSDictionary\",&,V_customKeyRequestBodyClaims"
- "T@\"NSDictionary\",&,V_customKeyRequestHeaderClaims"
- "T@\"NSDictionary\",&,V_customLoginRequestBodyClaims"
- "T@\"NSDictionary\",&,V_customLoginRequestHeaderClaims"
- "T@\"NSDictionary\",&,V_customRefreshRequestBodyClaims"
- "T@\"NSDictionary\",&,V_customRefreshRequestHeaderClaims"
- "T@\"NSDictionary\",C,N,V_authorizationGroups"
- "T@\"NSDictionary\",C,N,V_tokenToUserMapping"
- "T@\"NSDictionary\",R"
- "T@\"NSDictionary\",R,D"
- "T@\"NSMutableData\",&,D"
- "T@\"NSMutableData\",&,N,V_password"
- "T@\"NSMutableData\",&,V_passwordData"
- "T@\"NSMutableData\",R,D"
- "T@\"NSMutableDictionary\",&,V_cache"
- "T@\"NSMutableDictionary\",&,V_data"
- "T@\"NSMutableDictionary\",C,V_temporaryAccountCredentials"
- "T@\"NSNumber\",&,D"
- "T@\"NSNumber\",&,N,V_userSepSigningAlgorithm"
- "T@\"NSNumber\",C,N,V_encryptionAlgorithm"
- "T@\"NSNumber\",C,N,V_loginFrequency"
- "T@\"NSNumber\",C,N,V_loginRequestEncryptionAlgorithm"
- "T@\"NSNumber\",C,N,V_pendingEncryptionAlgorithm"
- "T@\"NSNumber\",C,N,V_pendingSigningAlgorithm"
- "T@\"NSNumber\",C,N,V_serverNonceExpirationTime"
- "T@\"NSNumber\",C,N,V_signingAlgorithm"
- "T@\"NSNumber\",C,V_sdkVersionString"
- "T@\"NSNumber\",N,R"
- "T@\"NSNumber\",N,R,VencryptionAlgorithm"
- "T@\"NSNumber\",R,D"
- "T@\"NSNumber\",R,N"
- "T@\"NSNumber\",R,N,V_encryptionAlgorithm"
- "T@\"NSOperationQueue\",R,V_completionQueue"
- "T@\"NSString\",&,D"
- "T@\"NSString\",&,N,V_action"
- "T@\"NSString\",&,N,V_assertion"
- "T@\"NSString\",&,N,V_clientNameKeyName"
- "T@\"NSString\",&,N,V_encryptionKeyTypeKeyName"
- "T@\"NSString\",&,N,V_endpointURN"
- "T@\"NSString\",&,N,V_faultCodeValue"
- "T@\"NSString\",&,N,V_faultReason"
- "T@\"NSString\",&,N,V_faultSubCodeValue"
- "T@\"NSString\",&,N,V_keyIdentifier"
- "T@\"NSString\",&,N,V_messageBufferKeyName"
- "T@\"NSString\",&,N,V_nonce"
- "T@\"NSString\",&,N,V_realmKeyName"
- "T@\"NSString\",&,N,V_securityExtensionPrefix"
- "T@\"NSString\",&,N,V_serviceNameKeyName"
- "T@\"NSString\",&,N,V_sessionKeyKeyName"
- "T@\"NSString\",&,N,V_ticketKeyPath"
- "T@\"NSString\",&,N,V_to"
- "T@\"NSString\",&,N,V_tokenType"
- "T@\"NSString\",&,N,V_userName"
- "T@\"NSString\",&,V_cacheName"
- "T@\"NSString\",&,V_rawAuthenticationTag"
- "T@\"NSString\",&,V_rawBody"
- "T@\"NSString\",&,V_rawCipherText"
- "T@\"NSString\",&,V_rawEncryptedKey"
- "T@\"NSString\",&,V_rawHeader"
- "T@\"NSString\",&,V_rawIV"
- "T@\"NSString\",&,V_rawSignature"
- "T@\"NSString\",&,V_realm"
- "T@\"NSString\",&,V_ticketKeyPath"
- "T@\"NSString\",&,V_upn"
- "T@\"NSString\",&,V_userName"
- "T@\"NSString\",&,V_volume"
- "T@\"NSString\",&,V_volumeUUID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C"
- "T@\"NSString\",C,N,V_Address"
- "T@\"NSString\",C,N,V_Id"
- "T@\"NSString\",C,N,V_KeyType"
- "T@\"NSString\",C,N,V_Password"
- "T@\"NSString\",C,N,V_RequestType"
- "T@\"NSString\",C,N,V_TokenType"
- "T@\"NSString\",C,N,V_Username"
- "T@\"NSString\",C,N,V_Value"
- "T@\"NSString\",C,N,V_ValueType"
- "T@\"NSString\",C,N,V_accountDisplayName"
- "T@\"NSString\",C,N,V_additionalAuthorizationScopes"
- "T@\"NSString\",C,N,V_additionalScopes"
- "T@\"NSString\",C,N,V_apv"
- "T@\"NSString\",C,N,V_audience"
- "T@\"NSString\",C,N,V_bindingName"
- "T@\"NSString\",C,N,V_customRequestJWTParameterName"
- "T@\"NSString\",C,N,V_defaultUserDomain"
- "T@\"NSString\",C,N,V_encryptionContext"
- "T@\"NSString\",C,N,V_endpointURLString"
- "T@\"NSString\",C,N,V_extensionIdentifier"
- "T@\"NSString\",C,N,V_faultactor"
- "T@\"NSString\",C,N,V_faultcode"
- "T@\"NSString\",C,N,V_faultstring"
- "T@\"NSString\",C,N,V_federationMexURLKeypath"
- "T@\"NSString\",C,N,V_federationPredicate"
- "T@\"NSString\",C,N,V_federationRequestURN"
- "T@\"NSString\",C,N,V_groupRequestClaimName"
- "T@\"NSString\",C,N,V_groupResponseClaimName"
- "T@\"NSString\",C,N,V_invalidCredentialPredicate"
- "T@\"NSString\",C,N,V_loginUserName"
- "T@\"NSString\",C,N,V_mustUnderstand"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_nonce"
- "T@\"NSString\",C,N,V_nonceResponseKeypath"
- "T@\"NSString\",C,N,V_policyName"
- "T@\"NSString\",C,N,V_portName"
- "T@\"NSString\",C,N,V_previousRefreshTokenClaimName"
- "T@\"NSString\",C,N,V_refreshToken"
- "T@\"NSString\",C,N,V_requestIdentifier"
- "T@\"NSString\",C,N,V_resumedEmbeddedAssertion"
- "T@\"NSString\",C,N,V_scope"
- "T@\"NSString\",C,N,V_serverNonce"
- "T@\"NSString\",C,N,V_serverNonceClaimName"
- "T@\"NSString\",C,N,V_stringValue"
- "T@\"NSString\",C,N,V_tokenId"
- "T@\"NSString\",C,N,V_tokenTypeNamespace"
- "T@\"NSString\",C,N,V_transport"
- "T@\"NSString\",C,N,V_uniqueIdentifierClaimName"
- "T@\"NSString\",C,N,V_userName"
- "T@\"NSString\",C,N,V_wsTrustFederationNonce"
- "T@\"NSString\",C,V_smartCardTokenId"
- "T@\"NSString\",C,V_ssoExtensionIdentifier"
- "T@\"NSString\",C,V_uniqueIdentifier"
- "T@\"NSString\",C,V_userDecryptionContext"
- "T@\"NSString\",C,V_userUnlockData"
- "T@\"NSString\",N,C"
- "T@\"NSString\",R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_contentPropertyName"
- "T@\"NSString\",R,C,N,V_elementName"
- "T@\"NSString\",R,C,N,V_namespaceURI"
- "T@\"NSString\",R,D"
- "T@\"NSString\",R,N,V_clientID"
- "T@\"NSString\",R,N,V_issuer"
- "T@\"NSString\",R,V_alg"
- "T@\"NSString\",R,V_algorithmName"
- "T@\"NSString\",R,V_uniqueIdentifier"
- "T@\"NSString\",R,V_userIdentifier"
- "T@\"NSURL\",C,N,V_decryptionEndpointURL"
- "T@\"NSURL\",C,N,V_federationMexURL"
- "T@\"NSURL\",C,N,V_federationUserPreauthenticationURL"
- "T@\"NSURL\",C,N,V_jwksEndpointURL"
- "T@\"NSURL\",C,N,V_keyEndpointURL"
- "T@\"NSURL\",C,N,V_nonceEndpointURL"
- "T@\"NSURL\",C,N,V_refreshEndpointURL"
- "T@\"NSURL\",C,N,V_tokenEndpointURL"
- "T@\"NSURL\",C,N,V_wsTrustFederationMexURL"
- "T@\"NSURL\",C,N,V_wsTrustFederationURL"
- "T@\"NSURLSession\",&,N,V_urlSession"
- "T@\"NSXPCConnection\",&,V_xpcConnection"
- "T@\"POAssertionJWTBody\",&,V_decodedBody"
- "T@\"POAuthenticationProcess\",&,V_authenticationProcess"
- "T@\"POConfigurationVersion\",&,V_deviceConfigurationVersion"
- "T@\"POConfigurationVersion\",&,V_loginConfigurationVersion"
- "T@\"POConfigurationVersion\",&,V_userConfigurationVersion"
- "T@\"PODeviceConfiguration\",&,N,V_deviceConfiguration"
- "T@\"PODeviceConfiguration\",R"
- "T@\"PODeviceConfiguration\",R,V_currentDeviceConfiguration"
- "T@\"POIDTokenJWTBody\",&,V_decodedBody"
- "T@\"POJWTHeader\",&,V_decodedHeader"
- "T@\"POKeyExchangeRequestJWTBody\",&,V_decodedBody"
- "T@\"POKeyExchangeResponseJWTBody\",&,V_decodedBody"
- "T@\"POKeyRequestJWTBody\",&,V_decodedBody"
- "T@\"POKeyResponseJWTBody\",&,V_decodedBody"
- "T@\"POKeychainHelper\",&,V_keychainHelper"
- "T@\"POLoginConfiguration\",&,N,V_loginConfiguration"
- "T@\"POLoginConfiguration\",R,V_currentLoginConfiguration"
- "T@\"POLoginJWTBody\",&,V_decodedBody"
- "T@\"POLoginResponseJWTBody\",&,V_body"
- "T@\"POLoginResponseJWTBody\",&,V_decodedBody"
- "T@\"POMutableAssertionJWTBody\",&,V_body"
- "T@\"POMutableIDTokenJWTBody\",&,V_body"
- "T@\"POMutableJWTHeader\",&,V_header"
- "T@\"POMutableKeyExchangeRequestJWTBody\",&,V_body"
- "T@\"POMutableKeyExchangeResponseJWTBody\",&,V_body"
- "T@\"POMutableKeyRequestJWTBody\",&,V_body"
- "T@\"POMutableKeyResponseJWTBody\",&,V_body"
- "T@\"POMutableLoginJWTBody\",&,V_body"
- "T@\"POSOAPCode\",&,N,V_Code"
- "T@\"POSOAPEnvelope\",&,N,V_Envelope"
- "T@\"POSOAPFaultDetail\",&,N,V_detail"
- "T@\"POSOAPReason\",&,N,V_Reason"
- "T@\"POSOAPSubcode\",&,N,V_Subcode"
- "T@\"POSOAPText\",&,N,V_Text"
- "T@\"POTokenHelper\",&,V_tokenHelper"
- "T@\"POUserConfiguration\",R,V_currentUserConfiguration"
- "T@\"POUserLoginConfiguration\",&,V_userLoginConfiguration"
- "T@\"POWSTrustAppliesToType\",&,N,V_AppliesTo"
- "T@\"POWSTrustEndpointReferenceType\",&,N,V_EndpointReference"
- "T@\"POWSTrustKeyIdentifierType\",&,N,V_KeyIdentifier"
- "T@\"POWSTrustProcess\",&,N,V_wstrustProcess"
- "T@\"POWSTrustReferenceType\",&,N,V_RequestedAttachedReference"
- "T@\"POWSTrustReferenceType\",&,N,V_RequestedUnattachedReference"
- "T@\"POWSTrustRequestedSecurityTokenType\",&,N,V_RequestedSecurityToken"
- "T@\"POWSTrustSecurityTokenReferenceType\",&,N,V_SecurityTokenReference"
- "T@\"POWSTrustTimestampType\",&,N,V_Lifetime"
- "T@\"POWSTrustTimestampType\",&,N,V_Timestamp"
- "T@\"POWSTrustUsernameTokenType\",&,N,V_UsernameToken"
- "T@\"POXMLContext\",&,N,V_xmldocContext"
- "T@\"POXMLXPathContext\",&,N,V_xpathContext"
- "T@\"POXMLXPathResult\",&,N,V_xpathResultSet"
- "T@?,C,V_invalidationHandler"
- "T@?,C,V_lockHandler"
- "T@?,C,V_startupCompletion"
- "T@?,C,V_unlockCompletion"
- "TB,N,GisFault,V_fault"
- "TB,N,V__accessTokenTerminalIdentityKeySEP"
- "TB,N,V__accessTokenTerminalIdentityKeySystem"
- "TB,N,V_allowDeviceIdentifiersInAttestation"
- "TB,N,V_canLogin"
- "TB,N,V_federated"
- "TB,N,V_includePreviousRefreshTokenInLoginRequest"
- "TB,N,V_parseWSTrust13"
- "TB,N,V_parseWSTrust2005"
- "TB,N,V_waitForConnectivity"
- "TB,R"
- "TB,R,GisJWE,V_jwe"
- "TB,R,GisNewUser,V_newUser"
- "TB,R,N"
- "TB,V_allowAccessTokenExpressMode"
- "TB,V_authorizationEnabled"
- "TB,V_baseSystem"
- "TB,V_createFirstUserDuringSetupEnabled"
- "TB,V_createUsersEnabled"
- "TB,V_exchangeRequired"
- "TB,V_failedToConnect"
- "TB,V_firstUnlock"
- "TB,V_forLogin"
- "TB,V_importSuccessful"
- "TB,V_registrationCompleted"
- "TB,V_sharedDeviceKeys"
- "TB,V_sharedOnly"
- "TB,V_synchronizeProfilePicture"
- "TB,V_temporarySessionQuickLogin"
- "TB,V_useOldPrebootPath"
- "TI,N,V_callerUid"
- "TI,V_uid"
- "TQ,N,V_federationType"
- "TQ,N,V_fileVaultPolicy"
- "TQ,N,V_loginPolicy"
- "TQ,N,V_loginType"
- "TQ,N,V_state"
- "TQ,N,V_unlockPolicy"
- "TQ,N,V_userSEPKeyBiometricPolicy"
- "TQ,N,V_version"
- "TQ,R"
- "TQ,V_loginType"
- "TQ,V_wsTrustVersion"
- "T^{__CFString=},R,V_algorithm"
- "T^{__SecCertificate=}"
- "T^{__SecCertificate=},N,V_deviceEncryptionCertificate"
- "T^{__SecCertificate=},N,V_deviceSigningCertificate"
- "T^{__SecCertificate=},N,V_embeddedAssertionCertificate"
- "T^{__SecCertificate=},N,V_sepKeyCertificate"
- "T^{__SecCertificate=},V_userDecryptionCertificate"
- "T^{__SecCertificate=},V_userUnlockCertificate"
- "T^{__SecIdentity=}"
- "T^{__SecIdentity=},R,D"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_deviceEncryptionKey"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_deviceSigningKey"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},R,N"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_prebootKey"
- "T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_sepKey"
- "T^{__SecKey=},D,N"
- "T^{__SecKey=},N,V_embeddedAssertionSigningKey"
- "T^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii},N,V_xmldoc"
- "T^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS},N,V_node"
- "T^{_xmlXPathContext=^{_xmlDoc}^{_xmlNode}ii^{_xmlHashTable}ii^{_xmlXPathType}ii^{_xmlHashTable}ii^{_xmlXPathAxis}^^{_xmlNs}i^viii^{_xmlNode}^{_xmlNode}^{_xmlHashTable}^?^v^v**^?^v^^{_xmlNs}i^v^?{_xmlError=ii*i*i***ii^v^v}^{_xmlNode}^{_xmlDict}i^vQQi},N,V_xpathCtx"
- "T^{_xmlXPathObject=i^{_xmlNodeSet}id*^vi^vi},N,V_xpathObj"
- "Td,V_timeoutIntervalForResource"
- "Ti,R,V_version"
- "Tq,N,V_offlineGracePeriod"
- "Tq,N,V_requireAuthGracePeriod"
- "Tq,N,V_retriesRemaining"
- "Tq,N,V_retryDelay"
- "Tq,R,N"
- "Tq,V_newUserAuthorizationMode"
- "Tq,V_protocolVersion"
- "Tq,V_state"
- "Tq,V_userAuthorizationMode"
- "URL"
- "URLByAppendingPathComponent:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "XMLData"
- "XMLDataWithOptions:"
- "XMLString"
- "XMLStringWithOptions:"
- "^{_NSZone=}16@0:8"
- "^{__CFString=}"
- "^{__CFString=}16@0:8"
- "^{__CFString=}24@0:8@16"
- "^{__SecCertificate=}"
- "^{__SecCertificate=}16@0:8"
- "^{__SecCertificate=}24@0:8@16"
- "^{__SecCertificate=}32@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@24"
- "^{__SecIdentity=}16@0:8"
- "^{__SecIdentity=}32@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16^{__SecCertificate=}24"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@0:8@16"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}28@0:8@16B24"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8@16@24"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@0:8@16B24B28"
- "^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}40@0:8@16@24@32"
- "^{__SecKey=}"
- "^{__SecKey=}16@0:8"
- "^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}"
- "^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}16@0:8"
- "^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}"
- "^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16@0:8"
- "^{_xmlXPathContext=^{_xmlDoc}^{_xmlNode}ii^{_xmlHashTable}ii^{_xmlXPathType}ii^{_xmlHashTable}ii^{_xmlXPathAxis}^^{_xmlNs}i^viii^{_xmlNode}^{_xmlNode}^{_xmlHashTable}^?^v^v**^?^v^^{_xmlNs}i^v^?{_xmlError=ii*i*i***ii^v^v}^{_xmlNode}^{_xmlDict}i^vQQi}"
- "^{_xmlXPathContext=^{_xmlDoc}^{_xmlNode}ii^{_xmlHashTable}ii^{_xmlXPathType}ii^{_xmlHashTable}ii^{_xmlXPathAxis}^^{_xmlNs}i^viii^{_xmlNode}^{_xmlNode}^{_xmlHashTable}^?^v^v**^?^v^^{_xmlNs}i^v^?{_xmlError=ii*i*i***ii^v^v}^{_xmlNode}^{_xmlDict}i^vQQi}16@0:8"
- "^{_xmlXPathObject=i^{_xmlNodeSet}id*^vi^vi}"
- "^{_xmlXPathObject=i^{_xmlNodeSet}id*^vi^vi}16@0:8"
- "_Address"
- "_AppliesTo"
- "_Body"
- "_Code"
- "_Created"
- "_EndpointReference"
- "_Envelope"
- "_Expires"
- "_Header"
- "_Id"
- "_KeyIdentifier"
- "_KeyType"
- "_Lifetime"
- "_POJWTBodyBase"
- "_Password"
- "_Reason"
- "_RequestSecurityTokenResponse"
- "_RequestType"
- "_RequestedAttachedReference"
- "_RequestedSecurityToken"
- "_RequestedUnattachedReference"
- "_SecurityTokenReference"
- "_Subcode"
- "_Text"
- "_Timestamp"
- "_TokenType"
- "_TtC15PlatformSSOCore15POCryptoKitHPKE"
- "_TtC15PlatformSSOCore16POPrebootDataKey"
- "_TtC15PlatformSSOCore17POSmartCardHelper"
- "_TtC15PlatformSSOCore18POCurve25519Verify"
- "_TtC15PlatformSSOCore20POUserUnlockKeySwift"
- "_TtC15PlatformSSOCore30POCryptoKitAlgorithmCurve25519"
- "_TtC15PlatformSSOCore39POCryptoKitHPKE_P256_SHA256_AES_GCM_128"
- "_TtC15PlatformSSOCore39POCryptoKitHPKE_P256_SHA256_AES_GCM_256"
- "_TtC15PlatformSSOCore39POCryptoKitHPKE_P384_SHA384_AES_GCM_256"
- "_TtC15PlatformSSOCore44POCryptoKitHPKE_Curve25519_SHA256_ChachaPoly"
- "_Username"
- "_UsernameToken"
- "_Value"
- "_ValueType"
- "_XMLAttributeStringWithPrefix:name:value:options:appendingToString:"
- "_XMLAttributesStringWithComplexType:options:appendingToString:"
- "_XMLQualifiedNameForNamespace:elementName:options:appendingToString:"
- "_XMLStringWithComplexType:options:appendingToString:"
- "_XMLStringWithOptions:appendingToString:"
- "__accessTokenReaderIssuerCertificateData"
- "__accessTokenTerminalIdentityCertData"
- "__accessTokenTerminalIdentityKeyData"
- "__accessTokenTerminalIdentityKeySEP"
- "__accessTokenTerminalIdentityKeySystem"
- "__credential"
- "__deviceEncryptionKeyData"
- "__deviceSigningKeyData"
- "__hpkeAuthPublicKeyData"
- "__loginContext"
- "__loginRequestEncryptionPublicKeyData"
- "__sepKeyData"
- "__setupContext"
- "__setupPINContext"
- "__setupWrapHash"
- "__ssoExtensionIdentifier"
- "_accessTokenReaderGroupIdentifier"
- "_accessTokenReaderIssuerCertificateData"
- "_accessTokenReaderTerminalCapabilityIdentifier"
- "_accessTokenTerminalIdentityCertData"
- "_accessTokenTerminalIdentityKeyData"
- "_accessTokenTerminalIdentityKeySEP"
- "_accessTokenTerminalIdentityKeySystem"
- "_accountDisplayName"
- "_action"
- "_additionalAuthorizationScopes"
- "_additionalScopes"
- "_administratorGroups"
- "_alg"
- "_algorithm"
- "_algorithmName"
- "_allowAccessTokenExpressMode"
- "_allowDeviceIdentifiersInAttestation"
- "_apv"
- "_assertion"
- "_attributeAttributes"
- "_attributeForName:ofAttributeWithName:"
- "_attributeForName:ofElementWithName:"
- "_attributeForName:ofNodeWithName:attributes:"
- "_attributes"
- "_audience"
- "_authGracePeriodStart"
- "_authenticationProcess"
- "_authorizationEnabled"
- "_authorizationGroups"
- "_baseSystem"
- "_bindingName"
- "_body"
- "_cache"
- "_cacheName"
- "_callerUid"
- "_canLogin"
- "_checkForCachedAttestationForExtensionIdentifier:keyHash:"
- "_clientID"
- "_clientNameKeyName"
- "_completionQueue"
- "_connectToService"
- "_contentPropertyName"
- "_createFirstUserDuringSetupEnabled"
- "_createUserLoginTypes"
- "_createUsersEnabled"
- "_created"
- "_credential"
- "_currentDeviceConfiguration"
- "_currentLoginConfiguration"
- "_currentUserConfiguration"
- "_customAssertionRequestBodyClaims"
- "_customAssertionRequestHeaderClaims"
- "_customDecryptionRequestValues"
- "_customFederationUserPreauthenticationRequestValues"
- "_customKeyExchangeRequestBodyClaims"
- "_customKeyExchangeRequestHeaderClaims"
- "_customKeyExchangeRequestValues"
- "_customKeyRequestBodyClaims"
- "_customKeyRequestHeaderClaims"
- "_customKeyRequestValues"
- "_customLoginRequestBodyClaims"
- "_customLoginRequestHeaderClaims"
- "_customLoginRequestValues"
- "_customNonceRequestValues"
- "_customRefreshRequestBodyClaims"
- "_customRefreshRequestHeaderClaims"
- "_customRefreshRequestValues"
- "_customRequestJWTParameterName"
- "_data"
- "_dataForUserLoginStateList:error:"
- "_decodedBody"
- "_decodedHeader"
- "_decryptionEndpointURL"
- "_defaultConfigurationPath"
- "_defaultUserDomain"
- "_deleteAllCachedAttestations"
- "_deleteCachedAttestationForExtensionIdentifier:key:"
- "_deleteCachedAttestationForExtensionIdentifier:keyHash:"
- "_descriptionForValue:prefix:"
- "_detail"
- "_deviceConfiguration"
- "_deviceConfigurationData"
- "_deviceConfigurationForIdentifier:"
- "_deviceConfigurationVersion"
- "_deviceContext"
- "_deviceEncryptionCertificate"
- "_deviceEncryptionKey"
- "_deviceEncryptionKeyData"
- "_deviceSigningCertificate"
- "_deviceSigningKey"
- "_deviceSigningKeyData"
- "_elementAttributes"
- "_elementName"
- "_elements"
- "_embeddedAssertionCertificate"
- "_embeddedAssertionSigningKey"
- "_encryptAndSaveTemporaryAccountCredential:account:key:"
- "_encryptionAlgorithm"
- "_encryptionContext"
- "_encryptionKeyData"
- "_encryptionKeySaveDate"
- "_encryptionKeyTypeKeyName"
- "_endpointURLString"
- "_endpointURN"
- "_exchangeRequired"
- "_expires"
- "_extensionIdentifier"
- "_failedToConnect"
- "_fault"
- "_faultCodeValue"
- "_faultReason"
- "_faultSubCodeValue"
- "_faultactor"
- "_faultcode"
- "_faultstring"
- "_federated"
- "_federationMexURL"
- "_federationMexURLKeypath"
- "_federationPredicate"
- "_federationRequestURN"
- "_federationType"
- "_federationUserPreauthenticationURL"
- "_fileVaultPolicy"
- "_firstUnlock"
- "_forLogin"
- "_groupRequestClaimName"
- "_groupResponseClaimName"
- "_header"
- "_hpkeAuthPublicKeyData"
- "_hpkePsk"
- "_hpkePsk_id"
- "_importSuccessful"
- "_includePreviousRefreshTokenInLoginRequest"
- "_initWithClientId:issuer:tokenEndpointURL:jwksEndpointURL:audience:"
- "_invalidCredentialPredicate"
- "_invalidationHandler"
- "_issuer"
- "_items"
- "_jwe"
- "_jwksEndpointURL"
- "_jwksStorageProvider"
- "_jwksTrustedRootCertificates"
- "_kSupportedLoginResponseAlgorithms"
- "_kerberosStatus"
- "_kerberosTicketMappings"
- "_keyEndpointURL"
- "_keyHash"
- "_keyIdentifier"
- "_keychainHelper"
- "_lastCheckDate"
- "_lastEncryptionKeyChange"
- "_lastLogin"
- "_lastLoginDate"
- "_lastUpdated"
- "_lockHandler"
- "_loginConfiguration"
- "_loginConfigurationData"
- "_loginConfigurationForIdentifier:"
- "_loginConfigurationVersion"
- "_loginContext"
- "_loginFrequency"
- "_loginPolicy"
- "_loginRequestEncryptionAPVPrefix"
- "_loginRequestEncryptionAlgorithm"
- "_loginRequestEncryptionPublicKeyData"
- "_loginRequestHpkePsk"
- "_loginRequestHpkePsk_id"
- "_loginType"
- "_loginUserName"
- "_messageBufferKeyName"
- "_mustUnderstand"
- "_name"
- "_namespaceURI"
- "_namespaces"
- "_newUser"
- "_newUserAuthorizationMode"
- "_node"
- "_nonPlatformSSOAccounts"
- "_nonce"
- "_nonceEndpointURL"
- "_nonceResponseKeypath"
- "_notifyToken"
- "_offlineGracePeriod"
- "_otherGroups"
- "_parseUserLoginStateListData:error:"
- "_parseWSTrust13"
- "_parseWSTrust2005"
- "_password"
- "_passwordData"
- "_pendingEncryptionAlgorithm"
- "_pendingSSOTokensForIdentifier:error:"
- "_pendingSigningAlgorithm"
- "_performDynamicWSTrustPasswordLoginWithContext:completion:"
- "_performEmbeddedAssertionLoginUsingContext:completion:"
- "_performEncryptedPasswordLoginUsingContext:completion:"
- "_performNonceRequestWithContext:request:completion:"
- "_performPasswordLoginUsingContext:completion:"
- "_performWSTrustPasswordLoginWithContext:completion:"
- "_platformSSOOldTriggerFile"
- "_policyName"
- "_portName"
- "_prebootKey"
- "_previousRefreshTokenClaimName"
- "_properties"
- "_protocolVersion"
- "_rawAuthenticationTag"
- "_rawBody"
- "_rawCipherText"
- "_rawEncryptedKey"
- "_rawHeader"
- "_rawIV"
- "_rawSignature"
- "_realm"
- "_realmKeyName"
- "_refreshEndpointURL"
- "_refreshToken"
- "_registrationCompleted"
- "_removeStashedUserLoginStateListDataWithError:"
- "_requestIdentifier"
- "_requireAuthGracePeriod"
- "_resumedEmbeddedAssertion"
- "_retriesRemaining"
- "_retryDelay"
- "_saveAttestationToKeychain:extensionIdentifier:keyHash:attestationDate:error:"
- "_saveAttestationToKeychain:extensionIdentifier:keyHash:error:"
- "_savePendingSSOTokensData:forIdentifier:error:"
- "_saveStashedDecryptionContextData:forIdentifier:error:"
- "_saveStashedSSOTokensData:forIdentifier:error:"
- "_saveUserLoginStateList:error:"
- "_scope"
- "_sdkVersionString"
- "_securityExtensionPrefix"
- "_sepKey"
- "_sepKeyCertificate"
- "_sepKeyData"
- "_serverNonce"
- "_serverNonceClaimName"
- "_serverNonceExpirationTime"
- "_serverNonceReceived"
- "_serviceConnection"
- "_serviceNameKeyName"
- "_sessionKeyKeyName"
- "_setAttribute:forName:ofAttributeWithName:"
- "_setAttribute:forName:ofElementWithName:"
- "_setAttribute:forName:ofNodeWithName:attributes:"
- "_setQueue:"
- "_setStateAndNotify:type:"
- "_setTargetUserIdentifier:"
- "_setupContext"
- "_setupPINContext"
- "_setupWrapHash"
- "_sharedDeviceKeys"
- "_sharedOnly"
- "_signingAlgorithm"
- "_smartCardHash"
- "_smartCardTokenId"
- "_ssoExtensionIdentifier"
- "_startupCompletion"
- "_stashedSSOTokensForIdentifier:error:"
- "_stashedUserLoginStateListDataWithError:"
- "_stashedUserLoginStateListWithError:"
- "_state"
- "_stringSuitableForHTML:"
- "_stringValue"
- "_synchronizeProfilePicture"
- "_temporaryAccountCredentials"
- "_temporarySessionAccounts"
- "_temporarySessionQuickLogin"
- "_ticketKeyPath"
- "_timeoutIntervalForResource"
- "_to"
- "_token"
- "_tokenEndpointURL"
- "_tokenExpires"
- "_tokenHelper"
- "_tokenId"
- "_tokenToUserMapping"
- "_tokenType"
- "_tokenTypeNamespace"
- "_transport"
- "_type"
- "_types"
- "_uid"
- "_uniqueIdentifier"
- "_uniqueIdentifierClaimName"
- "_unlockCompletion"
- "_unlockPolicy"
- "_upn"
- "_urlSession"
- "_useOldPrebootPath"
- "_userAuthorizationMode"
- "_userConfigurationForIdentifier:error:"
- "_userConfigurationVersion"
- "_userDecryptionCertificate"
- "_userDecryptionContext"
- "_userDecryptionKeyHash"
- "_userIdentifier"
- "_userIdentifierProvider"
- "_userLock"
- "_userLoginConfiguration"
- "_userLoginStateForIdentifier:error:"
- "_userLoginStateListDataWithError:"
- "_userLoginStateListWithError:"
- "_userName"
- "_userSEPKeyBiometricPolicy"
- "_userSepSigningAlgorithm"
- "_userUnlockCertificate"
- "_userUnlockData"
- "_userUnlockHash"
- "_verifyCurve25519EncryptionKey:"
- "_verifyCurve25519SigningKey:"
- "_verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:"
- "_version"
- "_volume"
- "_volumeUUID"
- "_waitForConnectivity"
- "_wrapHash"
- "_wsTrustFederationMexURL"
- "_wsTrustFederationNonce"
- "_wsTrustFederationURL"
- "_wsTrustVersion"
- "_wstrustProcess"
- "_xmldoc"
- "_xmldocContext"
- "_xpathContext"
- "_xpathCtx"
- "_xpathObj"
- "_xpathResultSet"
- "_xpcConnection"
- "absoluteString"
- "accessKeyReaderIssuerCertificate"
- "accessTokenReaderGroupIdentifier"
- "accessTokenReaderTerminalCapabilityIdentifier"
- "accessTokenTerminalIdentity"
- "accountDisplayName"
- "action"
- "addAttributeWithName:type:"
- "addAttributeWithName:type:isSpecifiedKey:"
- "addAttributeWithName:type:namespaceURI:"
- "addCharactersInRange:"
- "addCharactersInString:"
- "addCryptoHeadersToJWTBody:context:"
- "addCustomClaims:"
- "addElementWithName:namespaceURI:type:"
- "addElementWithName:namespaceURI:type:isSpecifiedKey:"
- "addElementWithName:namespaceURI:type:maxOccurs:minOccurs:"
- "addElementWithName:namespaceURI:type:maxOccurs:minOccurs:flattenMultiValue:"
- "addEntriesFromDictionary:"
- "addEphemeralPublicKey:"
- "addNamespaceWithURI:"
- "addObject:"
- "addObjectsFromArray:"
- "addOperationWithBlock:"
- "addRequiredScope:"
- "addTokenConfigurationForTokenInstanceID:"
- "addTokens:metaData:toKeychainForService:username:"
- "addTokens:metaData:toKeychainForService:username:system:"
- "addUnboundedElementWithName:namespaceURI:type:"
- "addValue:forHTTPHeaderField:"
- "addValuesTo:"
- "addValuesToHeader:"
- "additionalAuthorizationScopes"
- "additionalScopes"
- "administratorGroups"
- "aks_fv_new_sibling_vek"
- "aks_remote_peer_drop"
- "aks_remote_peer_get_state"
- "aks_smartcard_register"
- "aks_smartcard_request_unlock"
- "aks_smartcard_unlock"
- "aks_smartcard_unregister"
- "aks_stash_escrow"
- "algValue"
- "algorithm"
- "algorithmForString:"
- "algorithmName"
- "algorithmWithAlg:enc:"
- "algorithmWithEncryptionAlgorithm:"
- "algorithmWithIdentifier:"
- "algorithmWithSigningAlgorithm:"
- "allData"
- "allHTTPHeaderFields"
- "allKeys"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "allowAccessTokenExpressMode"
- "allowDeviceIdentifiersInAttestation"
- "allowedElementKeys"
- "analyticsForDeviceRegistrationInBuddy:"
- "analyticsForLoginConfiguration:"
- "analyticsForLoginManager:"
- "analyticsForLoginType:result:"
- "analyticsForPasswordChange:credentialNeeded:result:"
- "analyticsForRegistrationType:options:result:"
- "analyticsForSetupAssistantLoginType:result:"
- "analyticsForStatus"
- "analyticsForTempSessionLoginType:result:"
- "analyticsForTestMessages"
- "analyticsForUserRegistrationInBuddy:"
- "appSSOEnabled"
- "appendBytes:length:"
- "appendData:"
- "appendFormat:"
- "appendString:"
- "applyResumeData:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayByAddingObject:"
- "arrayByAddingObjectsFromArray:"
- "arrayWithObjects:count:"
- "attributes"
- "audArray"
- "audience"
- "auditSessionIdentifier"
- "authGracePeriodStart"
- "authenticationMethod"
- "authenticationProcess"
- "authorizationEnabled"
- "authorizationGroups"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "base64URLtokenHashForUser:"
- "baseSystem"
- "bindingName"
- "body"
- "bodyData"
- "boolValue"
- "boolValueForKey:defaultValue:"
- "buddyTestMode"
- "bytes"
- "cache"
- "cacheName"
- "calendar"
- "callerUid"
- "canLogin"
- "canTokenIdLogin:pubKeyHash:"
- "certificateForData:"
- "characterAtIndex:"
- "characterSetWithCharactersInString:"
- "checkIfBiometricConstraintsForSigning:"
- "checkIfBiometricConstraintsForSigningForKey:"
- "checkVersion"
- "cipherSuite"
- "class"
- "clientID"
- "clientNameKeyName"
- "code"
- "compare:"
- "completeAccessTokenLoginUsingContext:completion:"
- "completionQueue"
- "components:fromDate:"
- "componentsSeparatedByString:"
- "componentsWithString:"
- "compressedDataUsingAlgorithm:error:"
- "concatKDFWithKey:algorithm:partyUInfo:partyVInfo:"
- "configurationWithOpenIdConfigurationURL:clientID:issuer:completion:"
- "configurationWithOpenIdConfigurationURL:identityProviderURL:clientId:issuer:completion:"
- "conformsToProtocol:"
- "connectionInvalidated"
- "containsObject:"
- "containsString:"
- "content"
- "contentPropertyName"
- "contentsOfDirectoryAtPath:error:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAuthenticationContextUsingLoginConfiguration:deviceConfiguration:userName:"
- "createAuthenticationContextUsingLoginConfiguration:deviceConfiguration:userName:resumeData:"
- "createEmbeddedAssertionWithContext:"
- "createEmbeddedPasswordAssertionWithContext:"
- "createEncryptionKeyForAlgorithm:"
- "createFirstUserDuringSetupEnabled"
- "createKeyAndReturnError:"
- "createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:"
- "createKeyExchangeRequestWithContext:jwt:"
- "createKeyRequestJWTWithContext:"
- "createKeyRequestWithContext:jwt:"
- "createLoginJWTWithContext:embeddedAssertion:"
- "createLoginRequestWithContext:jwt:"
- "createNonceRequestWithContext:"
- "createPartyVInfoWithNonce:apvKey:"
- "createPartyVInfoWithNonce:prefixData:apvPublicKey:"
- "createPreAuthenticationRequestWithContext:"
- "createRefreshJWTWithContext:"
- "createSEPEncryptionKeyForAlgorithm:shared:"
- "createSEPEncryptionKeyForAlgorithm:shared:preboot:"
- "createSEPSigningKeyForAlgorithm:shared:"
- "createSEPSigningKeyForAlgorithm:shared:preboot:"
- "createTestMessagesForLoginConfiguration:certificate:"
- "createUnlockKeyWithPublicKey:error:"
- "createUnlockKeyWithPublicKey:userName:returningCertificate:hash:encryptedData:"
- "createUserLoginTypes"
- "createUserSEPSigningKeyForAlgorithm:"
- "createUserSEPSigningKeyForAlgorithm:userPresence:currentSet:"
- "createUsersEnabled"
- "createWSTrust13Request:"
- "createWSTrust13RequestWithContext:"
- "createWSTrust13Response:"
- "createWSTrust2005Request:"
- "createWSTrust2005RequestWithContext:"
- "createWSTrust2005Response:"
- "createWSTrustFault:"
- "createWSTrustMexRequestWithContext:"
- "credentialOfType:reply:"
- "currentDeviceConfiguration"
- "currentLoginConfiguration"
- "currentUserConfiguration"
- "customAssertionRequestBodyClaims"
- "customAssertionRequestHeaderClaims"
- "customDecryptionRequestValues"
- "customFederationUserPreauthenticationRequestValues"
- "customKeyExchangeRequestBodyClaims"
- "customKeyExchangeRequestHeaderClaims"
- "customKeyExchangeRequestValues"
- "customKeyRequestBodyClaims"
- "customKeyRequestHeaderClaims"
- "customKeyRequestValues"
- "customLoginRequestBodyClaims"
- "customLoginRequestHeaderClaims"
- "customLoginRequestValues"
- "customNonceRequestValues"
- "customRefreshRequestBodyClaims"
- "customRefreshRequestHeaderClaims"
- "customRefreshRequestValues"
- "customRequestJWTParameterName"
- "d16@0:8"
- "data"
- "dataForCertificate:"
- "dataForEphemeralKey:"
- "dataForKey:"
- "dataForKey:error:"
- "dataRepresentation"
- "dataRepresentationForDisplay:"
- "dataTaskWithRequest:completionHandler:"
- "dataTaskWithURL:completionHandler:"
- "dataToHex:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithContentsOfURL:"
- "dataWithJSONObject:options:error:"
- "dataWithLength:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateFromComponents:"
- "dateFromString:"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "decodeAndDecryptJWT:encryptionAlgorithm:privateKey:otherInfo:psk:psk_id:authPublicKey:error:"
- "decodeAndDecryptJWT:privateKey:otherInfo:psk:psk_id:authPublicKey:error:"
- "decodeEphemeralPublicKey"
- "decodeObjectOfClass:forKey:"
- "decodedBody"
- "decodedHeader"
- "decompressedDataUsingAlgorithm:error:"
- "decryptPendingSSOTokens:UsingPrivateKey:sharedData:"
- "decryptTemporaryAccountCredentialForAccount:"
- "decryptWithData:key:error:"
- "decryptionEndpointURL"
- "defaultManager"
- "defaultUserDomain"
- "definition"
- "definitionForType:"
- "description"
- "descriptionForValue:"
- "detail"
- "deviceConfiguration"
- "deviceConfigurationData"
- "deviceConfigurationForIdentifier:completion:"
- "deviceConfigurationVersion"
- "deviceContext"
- "deviceEncryptionCertificate"
- "deviceEncryptionIdentity"
- "deviceEncryptionKey"
- "deviceEncryptionKeyWithContext:"
- "deviceEncryptionPublicKey"
- "deviceSigningCertificate"
- "deviceSigningIdentity"
- "deviceSigningKey"
- "deviceSigningKeyWithContext:"
- "deviceSigningPublicKey"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryRepresentationForDisplay:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleValue"
- "driverConfigurations"
- "effectiveUserIdentifier"
- "elementForValue:"
- "elementName"
- "elements"
- "elementsNeedRedaction"
- "embeddedAssertionCertificate"
- "embeddedAssertionSigningKey"
- "encodeAndEncryptJWT:encryptionAlgorithm:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:"
- "encodeAndEncryptJWT:publicKey:otherInfo:psk:psk_id:authPrivateKey:auth_kid:error:"
- "encodeAndSignJWT:algorithm:key:certificate:"
- "encodeAndSignJWT:algorithm:key:certificate:error:"
- "encodeAndSignJWT:key:certificate:"
- "encodeAndSignJWT:key:certificate:error:"
- "encodeAndSignJWT:signingAlgorithm:key:certificate:"
- "encodeAndSignJWT:signingAlgorithm:key:certificate:error:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encryptAndSaveTemporaryAccountCredential:account:"
- "encryptPendingSSOTokens:usingPublicKey:sharedData:encryptedTokens:"
- "encryptWithData:key:error:"
- "encryptedKeyData"
- "encryptionAlgorithm"
- "encryptionContext"
- "encryptionKeyData"
- "encryptionKeySaveDate"
- "encryptionKeyTypeKeyName"
- "endpointURLString"
- "endpointURN"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "ephemeralKeyForData:"
- "ephemeralPublicKeyForData:"
- "ephemeralSessionConfiguration"
- "ephemeralX25529PublicKeyForData:"
- "errorWithCode:description:"
- "errorWithCode:underlyingError:description:"
- "evaluateTrustForCertificates:rootCertificates:"
- "evaluateWithObject:"
- "evaluateXPath:"
- "exchangeRequired"
- "expires"
- "extensionIdentifier"
- "extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:"
- "extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:"
- "failedToConnect"
- "fault"
- "faultCodeValue"
- "faultReason"
- "faultSubCodeValue"
- "federated"
- "federationMexURL"
- "federationMexURLKeypath"
- "federationPredicate"
- "federationRequestURN"
- "federationUserPreauthenticationURL"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "fileVaultPolicy"
- "findAlgorithmForKey:"
- "findInfoForTokenId:"
- "findKey:inJWKSData:rootCertificates:"
- "findTokenIdForSmartCardAMUser:tokenHash:"
- "findTokenIdForSmartCardBoundUser:tokenHash:"
- "firstObject"
- "firstUnlock"
- "flattenMultiValueElementWithName:"
- "forLogin"
- "forceExtensionSDKVersion"
- "forceKerberosTGTExchange"
- "getBytes:range:"
- "getCharacters:"
- "getDriverConfiguration"
- "getLoginTypeForUser:"
- "getLoginTypeForUser:completion:"
- "getTokenInfo"
- "groupRequestClaimName"
- "groupResponseClaimName"
- "hasPrefix:"
- "hasSuffix:"
- "hasTemporaryAccountCredentialForAccount:"
- "hash"
- "header"
- "host"
- "hpkeAuthPublicKey"
- "hpkePsk"
- "hpkePsk_id"
- "i16@0:8"
- "i36@0:8@16@24B32"
- "i48@0:8@16@24@32@40"
- "i52@0:8@16@24@32@40B48"
- "i52@0:8@16@24B32^@36^@44"
- "identityForKey:andCertificate:"
- "importSuccessful"
- "increaseVersionWithMessage:"
- "init"
- "initForBaseSystem:"
- "initForLogin:identifierProvider:jwksStroageProvider:"
- "initWithBase64EncodedString:options:"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithCalendarIdentifier:"
- "initWithCertificate:objectID:"
- "initWithClientID:issuer:tokenEndpointURL:jwksEndpointURL:audience:"
- "initWithCoder:"
- "initWithConfigurationType:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDictionary:"
- "initWithDomain:authenticationContext:"
- "initWithDomain:code:userInfo:"
- "initWithElementName:namespaceURI:type:"
- "initWithExternalizedContext:"
- "initWithExternalizedContext:userSession:"
- "initWithIdentifierProvider:"
- "initWithJWTData:"
- "initWithKeyOptions:valueOptions:capacity:"
- "initWithLength:"
- "initWithLocaleIdentifier:"
- "initWithLoginUserName:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "initWithName:"
- "initWithSecKeyAlgorithm:algorithmName:alg:"
- "initWithString:"
- "initWithTokenID:"
- "initWithTrust:"
- "initWithURL:cachePolicy:timeoutInterval:"
- "initWithURL:resolvingAgainstBaseURL:"
- "initWithUid:forLogin:"
- "initWithUniqueIdentifier:"
- "initWithUserName:identifierProvider:sharedOnly:"
- "initWithUserName:identifierProvider:sharedOnly:volume:"
- "initWithVolume:"
- "initWithXMLContext:"
- "initWithXPCConnection:baseSystem:"
- "initWithXPCConnection:identifierProvider:jwksStroageProvider:"
- "initialize"
- "insertTokenForUser:"
- "insertTokenForUserName:completion:"
- "intValue"
- "integerValue"
- "interfaceWithInternalProtocol:"
- "interfaceWithProtocol:"
- "internalErrorWithMessage:"
- "invalidCredentialPredicate"
- "invalidate"
- "invalidationHandler"
- "invert"
- "isAtEnd"
- "isCredentialFault"
- "isEncryptionAlgorithm:validForKey:"
- "isEqual:"
- "isEqualToData:"
- "isEqualToNumber:"
- "isEqualToString:"
- "isEqualToTimeZone:"
- "isFault"
- "isInternalBuild"
- "isJWE"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isNewUser"
- "isPlatformSSOUserName:"
- "isProxy"
- "isSEPKey:"
- "isServerNonceExpiredOrMissing"
- "isSpecifiedKeyForAttributeName:"
- "isSpecifiedKeyForElementName:"
- "isSubclassOfClass:"
- "isSystemKey:"
- "isTemporaryAccountUserName:"
- "isUserKeybagUnlocked"
- "isValidJSONObject:"
- "jwe"
- "jwksCacheForExtensionIdentifier:"
- "jwksEndpointURL"
- "jwksStorageProvider"
- "jwksTrustedRootCertificates"
- "kSupportedLoginResponseAlgorithms"
- "kerberosStatus"
- "kerberosTicketMappings"
- "keyData"
- "keyEndpointURL"
- "keyForData:"
- "keyForData:context:"
- "keyHash"
- "keyIdentifier"
- "keyUsage"
- "keychainAttributes"
- "keychainHelper"
- "lastCheckDate"
- "lastEncryptionKeyChange"
- "lastLogin"
- "lastLoginDate"
- "lastObject"
- "lastUpdated"
- "length"
- "listener:shouldAcceptNewConnection:"
- "loadXMLDocument:"
- "lockHandler"
- "loginConfiguration"
- "loginConfigurationData"
- "loginConfigurationForIdentifier:completion:"
- "loginConfigurationVersion"
- "loginFrequency"
- "loginPolicy"
- "loginRequestEncryptionAPVPrefix"
- "loginRequestEncryptionAlgorithm"
- "loginRequestEncryptionPublicKey"
- "loginRequestHpkePsk"
- "loginRequestHpkePsk_id"
- "loginType"
- "longLongValue"
- "lowercaseString"
- "maskName:"
- "maxCountForElementName:"
- "mergedConfigurationWithUserLoginConfiguration:"
- "messageBufferKeyName"
- "minCountForElementName:"
- "mutableBytes"
- "mutableCopy"
- "mutableCopyWithZone:"
- "nameSpacePrefixForHref:"
- "namespaceForAttributeName:"
- "namespaceURI"
- "namespaces"
- "newDateFormatter"
- "newDateFormatters"
- "newDateTimeFormatterWithTimeZoneStyle:"
- "newDateTimeFormatters"
- "newTimeFormatterWithTimeZoneStyle:"
- "newTimeFormatters"
- "newUser"
- "newUserAuthorizationMode"
- "node"
- "nodeCount"
- "nodes"
- "nonPlatformSSOAccounts"
- "nonceEndpointURL"
- "nonceResponseKeypath"
- "notificationForType:"
- "numberValueForKey:defaultValue:"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "objectEnumerator"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "offlineGracePeriod"
- "orderedSetWithArray:"
- "otherGroups"
- "parent"
- "parseMexResponse:namespaces:policyXPath:action:"
- "parseUserNameFromMailboxData:"
- "parseWSTrust13"
- "parseWSTrust2005"
- "parseWSTrustMexResponse:version:"
- "parseWSTrustRequest:version:"
- "parseWSTrustResponse:version:"
- "passwordData"
- "passwordDataFromContext:error:"
- "passwordStringFromData:"
- "path"
- "pendingEncryptionAlgorithm"
- "pendingSigningAlgorithm"
- "percentEncodedQuery"
- "performAccessTokenSigningUsingContext:completion:"
- "performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:"
- "performKeyExchangeRequestWithContext:request:completion:"
- "performKeyRequestUsingContext:completion:"
- "performKeyRequestWithContext:request:completion:"
- "performLoginRequestWithContext:request:completion:"
- "performLoginWithContext:loginJWT:completion:"
- "performNonceRequestWithContext:request:completion:"
- "performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:"
- "performPasswordLogin:passwordContext:updateLocalAccountPassword:completion:"
- "performPasswordLoginUsingContext:completion:"
- "performPreAuthenticationRequestWithContext:request:completion:"
- "performSEPKeyLoginUsingContext:completion:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSmartCardLoginUsingContext:completion:"
- "performTokenRefreshUsingContext:completion:"
- "performWSTrustAuthenticationRequestWithContext:request:completion:"
- "performWSTrustMexRequestWithContext:request:completion:"
- "platformSSODevModeEnabled"
- "platformSSODevModeTriggerFile"
- "platformSSODevModeTriggerFilePath"
- "platformSSOEnabled"
- "platformSSOTriggerFile"
- "platformSSOTriggerFilePath"
- "policyName"
- "portName"
- "postAHPCacheRefreshNotification"
- "prebootEncryptionAlgorithm"
- "prebootKey"
- "predicateWithFormat:"
- "prefixForNamespaceURI:"
- "prepareForAccessTokenLoginUsingContext:completion:"
- "previousRefreshTokenClaimName"
- "print"
- "printKey:"
- "propertyForName:"
- "propertyListWithData:options:format:error:"
- "protectionSpace"
- "protocolVersion"
- "psso_DisplayRequest"
- "psso_base64URLEncodedString"
- "psso_initWithBase64URLEncodedString:"
- "psso_sha256Hash"
- "psso_sha256HashString"
- "publicKeyHashForKey:"
- "q16@0:8"
- "q24@0:8@16"
- "queryItemWithName:value:"
- "queryItems"
- "rangeOfCharacterFromSet:options:range:"
- "rangeOfString:"
- "rawAuthenticationTag"
- "rawBody"
- "rawCipherText"
- "rawEncryptedKey"
- "rawHeader"
- "rawIV"
- "rawSignature"
- "rawXMLString"
- "realm"
- "realmKeyName"
- "recordFromData:"
- "refreshEndpointURL"
- "refreshToken"
- "registerNamespaces:"
- "registrationCompleted"
- "release"
- "remoteObjectInterface"
- "removeAllTokens"
- "removeItemAtPath:error:"
- "removeItemAtURL:error:"
- "removeObject:"
- "removeObjectForKey:"
- "removeTokenConfigurationForTokenInstanceID:"
- "removeTokenForUser:"
- "removeTokensFromKeychainWithService:username:system:"
- "requestIdentifier"
- "requireAuthGracePeriod"
- "requireRootCAInSystemTrustStore"
- "respondsToSelector:"
- "resume"
- "resumeData"
- "resumedEmbeddedAssertion"
- "retain"
- "retainCount"
- "retriesRemaining"
- "retrieveCertAndKeyForTokenId:context:certificate:privateKey:"
- "retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:"
- "retrieveIdentityForTokenId:context:forSigning:hash:identity:"
- "retrievePendingSSOTokenForIdentifier:completion:"
- "retrievePendingSSOTokensForUserName:"
- "retrieveSigningKeyWithContext:keyId:completion:"
- "retrieveStashedDecryptionContextForIdentifier:completion:"
- "retrieveStashedSSOTokenForIdentifier:completion:"
- "retrieveStashedSSOTokensForUserName:"
- "retrieveTokensFromKeychainForService:username:system:returningTokens:metaData:"
- "retryDelay"
- "saveCachedContextsToDiskWithCompletion:"
- "savePendingSSOTokens:forUserName:"
- "savePendingSSOTokens:identifier:completion:"
- "saveStashedDecryptionContext:identifier:completion:"
- "saveStashedSSOTokens:forUserName:"
- "saveStashedSSOTokens:identifier:completion:"
- "scanDouble:"
- "scanLocation"
- "scanString:intoString:"
- "sdkVersionString"
- "securityExtensionPrefix"
- "self"
- "selfSignedCertWithPrivateKey:subjectName:"
- "sepKey"
- "sepKeyCertificate"
- "sepKeyWithContext:"
- "sequenceOfRecordsFromData:"
- "serverNonce"
- "serverNonceClaimName"
- "serverNonceExpirationTime"
- "serverNonceReceived"
- "serverTrust"
- "serviceNameKeyName"
- "sessionKeyKeyName"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "sessionWithLAContext:error:"
- "setAccessKeyReaderIssuerCertificate:"
- "setAccessTokenReaderGroupIdentifier:"
- "setAccessTokenReaderTerminalCapabilityIdentifier:"
- "setAccessTokenTerminalIdentity:"
- "setAccountDisplayName:"
- "setAction:"
- "setAdditionalAuthorizationScopes:"
- "setAdditionalScopes:"
- "setAddress:"
- "setAdministratorGroups:"
- "setAlg:"
- "setAllowAccessTokenExpressMode:"
- "setAllowDeviceIdentifiersInAttestation:"
- "setAllowedUnits:"
- "setAmr:"
- "setApplicationTag:"
- "setAppliesTo:"
- "setApu:"
- "setApv:"
- "setAssertion:"
- "setAttributes:ofItemAtPath:error:"
- "setAud:"
- "setAudArray:"
- "setAudience:"
- "setAuthGracePeriodStart:"
- "setAuthenticationProcess:"
- "setAuthorizationEnabled:"
- "setAuthorizationGroups:"
- "setAzp:"
- "setBaseSystem:"
- "setBindingName:"
- "setBody:"
- "setBodyData:"
- "setCache:"
- "setCacheName:"
- "setCallerUid:"
- "setCanDecrypt:"
- "setCanLogin:"
- "setCanPerformKeyExchange:"
- "setCanSign:"
- "setCertificate:"
- "setCipherText:"
- "setClass:forSelector:argumentIndex:ofReply:"
- "setClientNameKeyName:"
- "setClient_id:"
- "setCode:"
- "setConfigurationData:"
- "setConstraints:"
- "setContentPropertyName:type:"
- "setCreateFirstUserDuringSetupEnabled:"
- "setCreateUserLoginTypes:"
- "setCreateUsersEnabled:"
- "setCreated:"
- "setCredential:type:"
- "setCty:"
- "setCustomAssertionRequestBodyClaims:"
- "setCustomAssertionRequestBodyClaims:returningError:"
- "setCustomAssertionRequestHeaderClaims:"
- "setCustomAssertionRequestHeaderClaims:returningError:"
- "setCustomDecryptionRequestBodyClaims:returningError:"
- "setCustomDecryptionRequestHeaderClaims:returningError:"
- "setCustomDecryptionRequestValues:"
- "setCustomFederationUserPreauthenticationRequestValues:"
- "setCustomKeyExchangeRequestBodyClaims:"
- "setCustomKeyExchangeRequestBodyClaims:returningError:"
- "setCustomKeyExchangeRequestHeaderClaims:"
- "setCustomKeyExchangeRequestHeaderClaims:returningError:"
- "setCustomKeyExchangeRequestValues:"
- "setCustomKeyRequestBodyClaims:"
- "setCustomKeyRequestBodyClaims:returningError:"
- "setCustomKeyRequestHeaderClaims:"
- "setCustomKeyRequestHeaderClaims:returningError:"
- "setCustomKeyRequestValues:"
- "setCustomLoginRequestBodyClaims:"
- "setCustomLoginRequestBodyClaims:returningError:"
- "setCustomLoginRequestHeaderClaims:"
- "setCustomLoginRequestHeaderClaims:returningError:"
- "setCustomLoginRequestValues:"
- "setCustomNonceRequestValues:"
- "setCustomRefreshRequestBodyClaims:"
- "setCustomRefreshRequestBodyClaims:returningError:"
- "setCustomRefreshRequestHeaderClaims:"
- "setCustomRefreshRequestHeaderClaims:returningError:"
- "setCustomRefreshRequestValues:"
- "setCustomRequestJWTParameterName:"
- "setData:"
- "setDateFormat:"
- "setDecodedBody:"
- "setDecodedHeader:"
- "setDecryptionEndpointURL:"
- "setDefaultUserDomain:"
- "setDelegate:"
- "setDetail:"
- "setDeviceConfiguration:"
- "setDeviceConfigurationData:"
- "setDeviceConfigurationVersion:"
- "setDeviceContext:"
- "setDeviceEncryptionCertificate:"
- "setDeviceEncryptionKey:"
- "setDeviceSigningCertificate:"
- "setDeviceSigningKey:"
- "setEmbeddedAssertionCertificate:"
- "setEmbeddedAssertionSigningKey:"
- "setEnc:"
- "setEncapsulatedKey:"
- "setEncryptedKeyData:"
- "setEncryptionAlgorithm:"
- "setEncryptionContext:"
- "setEncryptionKeyData:"
- "setEncryptionKeyTypeKeyName:"
- "setEndpointReference:"
- "setEndpointURLString:"
- "setEndpointURN:"
- "setEnvelope:"
- "setEpk:"
- "setExchangeRequired:"
- "setExp:"
- "setExpires:"
- "setExpires_in:"
- "setExpires_on:"
- "setExportedInterface:"
- "setExportedObject:"
- "setExtensionIdentifier:"
- "setFailedToConnect:"
- "setFault:"
- "setFaultCodeValue:"
- "setFaultReason:"
- "setFaultSubCodeValue:"
- "setFaultactor:"
- "setFaultcode:"
- "setFaultstring:"
- "setFederated:"
- "setFederationMexURL:"
- "setFederationMexURLKeypath:"
- "setFederationPredicate:"
- "setFederationRequestURN:"
- "setFederationType:"
- "setFederationUserPreauthenticationURL:"
- "setFileVaultPolicy:"
- "setFirstUnlock:"
- "setForLogin:"
- "setFormatOptions:"
- "setFragment:"
- "setGrant_type:"
- "setGroupRequestClaimName:"
- "setGroupResponseClaimName:"
- "setGroups:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHeader:"
- "setHpkeAuthPublicKey:"
- "setHpkePsk:"
- "setHpkePsk_id:"
- "setIat:"
- "setId:"
- "setId_token:"
- "setIdpTokenId:"
- "setImportSuccessful:"
- "setIncludePreviousRefreshTokenInLoginRequest:"
- "setInteractionNotAllowed:"
- "setInterruptionHandler:"
- "setInvalidCredentialPredicate:"
- "setInvalidationHandler:"
- "setIsSpecifiedKey:onElementWithName:"
- "setIss:"
- "setJwksCache:forExtensionIdentifier:"
- "setJwksEndpointURL:"
- "setJwksStorageProvider:"
- "setJwksTrustedRootCertificates:"
- "setKerberosStatus:"
- "setKerberosTicketMappings:"
- "setKey:"
- "setKeyData:"
- "setKeyEndpointURL:"
- "setKeyHash:"
- "setKeyIdentifier:"
- "setKeySizeInBits:"
- "setKeyType:"
- "setKey_context:"
- "setKey_purpose:"
- "setKeychainHelper:"
- "setKeychainItems:"
- "setKid:"
- "setLabel:"
- "setLastCheckDate:"
- "setLastEncryptionKeyChange:"
- "setLastLogin:"
- "setLastLoginDate:"
- "setLastUpdated:"
- "setLenient:"
- "setLifetime:"
- "setLocale:"
- "setLockHandler:"
- "setLoginConfiguration:"
- "setLoginConfigurationData:"
- "setLoginConfigurationVersion:"
- "setLoginFrequency:"
- "setLoginPolicy:"
- "setLoginRequestEncryptionAPVPrefix:"
- "setLoginRequestEncryptionAlgorithm:"
- "setLoginRequestEncryptionPublicKey:"
- "setLoginRequestHpkePsk:"
- "setLoginRequestHpkePsk_id:"
- "setLoginType:"
- "setLoginUserName:"
- "setMessageBufferKeyName:"
- "setMustUnderstand:"
- "setName:"
- "setName:namespaceURI:forType:"
- "setNbf:"
- "setNewUserAuthorizationMode:"
- "setNode:"
- "setNonPlatformSSOAccounts:"
- "setNonce:"
- "setNonceEndpointURL:"
- "setNonceResponseKeypath:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOfflineGracePeriod:"
- "setOtherGroups:"
- "setOther_publickey:"
- "setP2c:"
- "setP2s:"
- "setParseWSTrust13:"
- "setParseWSTrust2005:"
- "setPassword:"
- "setPasswordData:"
- "setPendingEncryptionAlgorithm:"
- "setPendingSigningAlgorithm:"
- "setPlatformSSOUnavailable"
- "setPolicyName:"
- "setPortName:"
- "setPrebootKey:"
- "setPreferred_username:"
- "setPreviousRefreshTokenClaimName:"
- "setProperty:forName:"
- "setProtocolVersion:"
- "setPublicKeyData:"
- "setPublicKeyHash:"
- "setQuery:"
- "setQueryItems:"
- "setRawAuthenticationTag:"
- "setRawBody:"
- "setRawCipherText:"
- "setRawEncryptedKey:"
- "setRawHeader:"
- "setRawIV:"
- "setRawSignature:"
- "setRealm:"
- "setRealmKeyName:"
- "setReason:"
- "setRefreshEndpointURL:"
- "setRefreshToken:"
- "setRefresh_token:"
- "setRefresh_token_expires_in:"
- "setRegistrationCompleted:"
- "setRemoteObjectInterface:"
- "setRequestIdentifier:"
- "setRequestSecurityTokenResponse:"
- "setRequestType:"
- "setRequest_nonce:"
- "setRequest_type:"
- "setRequestedAttachedReference:"
- "setRequestedSecurityToken:"
- "setRequestedUnattachedReference:"
- "setRequireAuthGracePeriod:"
- "setResumedEmbeddedAssertion:"
- "setRetriesRemaining:"
- "setRetryDelay:"
- "setScanLocation:"
- "setScope:"
- "setSdkVersionString:"
- "setSecurityExtensionPrefix:"
- "setSecurityTokenReference:"
- "setSepKey:"
- "setSepKeyCertificate:"
- "setServerNonce:"
- "setServerNonceClaimName:"
- "setServerNonceExpirationTime:"
- "setServerNonceReceived:"
- "setServiceNameKeyName:"
- "setSessionKeyKeyName:"
- "setSharedDeviceKeys:"
- "setSharedOnly:"
- "setSigningAlgorithm:"
- "setSmartCardHash:"
- "setSmartCardTokenId:"
- "setSsoExtensionIdentifier:"
- "setStartupCompletion:"
- "setState:"
- "setStringValue:"
- "setSub:"
- "setSubcode:"
- "setSuitableForLogin:"
- "setSynchronizeProfilePicture:"
- "setTaskDescription:"
- "setTemporaryAccountCredentials:"
- "setTemporarySessionQuickLogin:"
- "setText:"
- "setTicketKeyPath:"
- "setTimeZone:"
- "setTimeoutIntervalForResource:"
- "setTimestamp:"
- "setTo:"
- "setTokenEndpointURL:"
- "setTokenExpires:"
- "setTokenHelper:"
- "setTokenId:"
- "setTokenToUserMapping:"
- "setTokenType:"
- "setTokenTypeNamespace:"
- "setToken_type:"
- "setTransport:"
- "setTyp:"
- "setType:forName:"
- "setUid:"
- "setUniqueIdentifier:"
- "setUniqueIdentifierClaimName:"
- "setUnitsStyle:"
- "setUnlockCompletion:"
- "setUnlockData:"
- "setUnlockHash:"
- "setUnlockPolicy:"
- "setUpn:"
- "setUrlSession:"
- "setUseOldPrebootPath:"
- "setUserAuthorizationMode:"
- "setUserConfigurationVersion:"
- "setUserDecryptionCertificate:"
- "setUserDecryptionContext:"
- "setUserDecryptionKeyHash:"
- "setUserIdentifierProvider:"
- "setUserLoginConfiguration:"
- "setUserName:"
- "setUserSEPKeyBiometricPolicy:"
- "setUserSepSigningAlgorithm:"
- "setUserUnlockCertificate:"
- "setUserUnlockData:"
- "setUserUnlockHash:"
- "setUsername:"
- "setUsernameToken:"
- "setValue:"
- "setValue:forKey:"
- "setValueType:"
- "setVersion:"
- "setVolume:"
- "setVolumeUUID:"
- "setWaitForConnectivity:"
- "setWaitsForConnectivity:"
- "setWithArray:"
- "setWrapHash:"
- "setWsTrustFederationMexURL:"
- "setWsTrustFederationNonce:"
- "setWsTrustFederationURL:"
- "setWsTrustVersion:"
- "setWstrustProcess:"
- "setX5c:"
- "setX5t:"
- "setXmldoc:"
- "setXmldocContext:"
- "setXpathContext:"
- "setXpathCtx:"
- "setXpathObj:"
- "setXpathResultSet:"
- "setXpcConnection:"
- "set__ssoExtensionIdentifier:"
- "set_accessTokenReaderIssuerCertificateData:"
- "set_accessTokenTerminalIdentityCertData:"
- "set_accessTokenTerminalIdentityKeyData:"
- "set_accessTokenTerminalIdentityKeySEP:"
- "set_accessTokenTerminalIdentityKeySystem:"
- "set_credential:"
- "set_deviceEncryptionKeyData:"
- "set_deviceSigningKeyData:"
- "set_hpkeAuthPublicKeyData:"
- "set_loginContext:"
- "set_loginRequestEncryptionPublicKeyData:"
- "set_preventsAppSSO:"
- "set_sepKeyData:"
- "set_setupContext:"
- "set_setupPINContext:"
- "set_setupWrapHash:"
- "setlastLogin:"
- "sharedDeviceKeys"
- "sharedOnly"
- "signData:usingKey:"
- "signData:usingKey:error:"
- "signedData"
- "signingAlgorithm"
- "sleepForTimeInterval:"
- "smartCardHash"
- "smartCardTokenId"
- "ssoExtensionIdentifier"
- "startObservingKeyBagLockStatusChanges"
- "startupCompletion"
- "statusCode"
- "stopObservingKeyBagLockStatusChanges"
- "string"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByReplacingCharactersInRange:withString:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringByTrimmingCharactersInSet:"
- "stringForEncryptionAlgorithm:"
- "stringForKeyType:"
- "stringForLoginPolicy:"
- "stringForLoginPolicyState:"
- "stringForLoginResult:"
- "stringForLoginType:"
- "stringForSEPBiometricPolicy:"
- "stringForSigningAlgorithm:"
- "stringForUserAuthorizationMode:"
- "stringForUserState:"
- "stringFromDate:"
- "stringFromTimeInterval:"
- "stringFromValue:"
- "stringRepresentation"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "subdataWithRange:"
- "superclass"
- "supportsAccessKey"
- "supportsAuthorization"
- "supportsCreateFirstUserDuringSetup"
- "supportsCreateNewUsers"
- "supportsCreateTemporaryUsers"
- "supportsSecureCoding"
- "supportsTokenUnlock"
- "synchronizeProfilePicture"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "systemKeyForData:"
- "systemKeyForData:context:"
- "taskDescription"
- "temporaryAccountCredentials"
- "temporarySessionAccounts"
- "temporarySessionQuickLogin"
- "ticketKeyPath"
- "timeIntervalSince1970"
- "timeIntervalSinceNow"
- "timeZone"
- "timeZoneWithAbbreviation:"
- "timeoutIntervalForResource"
- "to"
- "tokenConfigurations"
- "tokenEndpointURL"
- "tokenExpires"
- "tokenHashDataForUser:"
- "tokenHashForUser:"
- "tokenHelper"
- "tokenId"
- "tokenIsAccessKey:"
- "tokenToUserMapping"
- "tokenType"
- "tokenTypeNamespace"
- "typeForName:"
- "types"
- "uid"
- "unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:"
- "uniqueIdentifier"
- "uniqueIdentifierClaimName"
- "uniqueIdentifierForUserName:"
- "unlockCompletion"
- "unlockKey:privateKey:returningKey:"
- "unlockKeyWithEncryptedKey:privateKey:error:"
- "unlockPolicy"
- "unlockTokenId"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "unwrapBlob:"
- "updateDecodedBody"
- "updateLoginStateForIdentifier:state:loginDate:loginType:completion:"
- "updateLoginStateForUserName:state:loginDate:loginType:"
- "updateLoginTypeForUserName:loginType:"
- "updateTriggerFile"
- "updateVersion"
- "upn"
- "urlSession"
- "use"
- "useOldPrebootPath"
- "useVolume:completion:"
- "userAuthorizationMode"
- "userAuthorizationModeWithString:"
- "userConfigurationForIdentifier:completion:"
- "userConfigurationForUserName:"
- "userConfigurationVersion"
- "userDecryptionCertificate"
- "userDecryptionContext"
- "userDecryptionKeyHash"
- "userDeviceConfiguration"
- "userIdentifier"
- "userIdentifierProvider"
- "userInfo"
- "userLoginConfiguration"
- "userLoginStateForIdentifier:completion:"
- "userLoginStateForUserName:"
- "userSEPKeyBiometricPolicy"
- "userSepSigningAlgorithm"
- "userUnlockCertificate"
- "userUnlockData"
- "userUnlockHash"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{__SecCertificate=}16"
- "v24@0:8^{__SecIdentity=}16"
- "v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16"
- "v24@0:8^{__SecKey=}16"
- "v24@0:8^{_xmlDoc=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}ii^{_xmlDtd}^{_xmlDtd}^{_xmlNs}**^v^v*i^{_xmlDict}^vii}16"
- "v24@0:8^{_xmlNode=^vi*^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlNode}^{_xmlDoc}^{_xmlNs}*^{_xmlAttr}^{_xmlNs}^vSS}16"
- "v24@0:8^{_xmlXPathContext=^{_xmlDoc}^{_xmlNode}ii^{_xmlHashTable}ii^{_xmlXPathType}ii^{_xmlHashTable}ii^{_xmlXPathAxis}^^{_xmlNs}i^viii^{_xmlNode}^{_xmlNode}^{_xmlHashTable}^?^v^v**^?^v^^{_xmlNs}i^v^?{_xmlError=ii*i*i***ii^v^v}^{_xmlNode}^{_xmlDict}i^vQQi}16"
- "v24@0:8^{_xmlXPathObject=i^{_xmlNodeSet}id*^vi^vi}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8B16B20B24"
- "v32@0:8#16@24"
- "v32@0:8@\"NSData\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"POUserConfiguration\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"POUserLoginState\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?Q@\"NSError\">24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@16#24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24"
- "v32@0:8Q16@24"
- "v32@0:8Q16q24"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?Q@\"NSData\"@\"NSString\"@\"NSArray\"@\"NSString\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSData\"24@?<v@?Q@\"NSError\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@16#24@32"
- "v40@0:8@16@24#32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@32"
- "v40@0:8@16q24q32"
- "v44@0:8@16@24B32@?36"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24#32@40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24Q32@40"
- "v48@0:8@16@24q32@?40"
- "v52@0:8@16@24@32B40@?44"
- "v56@0:8@\"NSString\"16@\"NSNumber\"24@\"NSDate\"32@\"NSNumber\"40@?<v@?B@\"NSError\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@16@24#32Q40Q48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32Q40@48"
- "v56@0:8@16@24^@32^@40^@48"
- "v56@0:8@16@24q32q40q48"
- "v60@0:8@16@24#32Q40Q48B56"
- "v76@0:8@16@24@32@40@48@56B64@?68"
- "validateIdToken:context:key:"
- "validatePartyUInfo:context:"
- "validatePartyVInfo:context:publicKey:"
- "validateWSTrustAuthenticationResponseWithContext:response:returningAssertion:"
- "validateWSTrustMexResponseWithContext:response:"
- "value"
- "valueForEntitlement:"
- "valueForKey:"
- "valueForKeyPath:"
- "valueForProperty:"
- "valueFromString:"
- "verifiedKeyWithPrebootData:error:"
- "verifyAgentEntitlement"
- "verifyJWTSignature:algorithm:key:"
- "verifyJWTSignature:key:"
- "verifyJWTSignature:signingAlgorithm:key:"
- "verifyKey:"
- "verifyLoginUserEntitlement"
- "verifyPasswordChangeEntitlement"
- "verifyPasswordLogin:passwordContext:"
- "verifyPasswordLogin:passwordContext:completion:"
- "verifyPasswordUser:passwordContext:completion:"
- "verifyPasswordUser:passwordContext:tokens:"
- "verifySecurityEntitlement"
- "verifySignature:onData:usingCertificateString:"
- "verifySignature:onData:usingKey:"
- "verifyTokenForUserName:passwordContext:completion:"
- "volume"
- "volumeUUID"
- "waitForConnectivity"
- "waitForKeyBagFirstUnlockOnStartupWithCompletion:"
- "waitForKeyBagUnlockWithCompletion:"
- "waitForTokenAvailable:"
- "whitespaceAndNewlineCharacterSet"
- "wrapBlob:"
- "wrapHash"
- "writeData:toPath:saveError:"
- "writeToFile:options:error:"
- "writeToURL:options:error:"
- "writeTriggerFileToPath:"
- "wsTrustFederationMexURL"
- "wsTrustFederationNonce"
- "wsTrustFederationURL"
- "wsTrustVersion"
- "wstrustProcess"
- "xmldoc"
- "xmldocContext"
- "xpathContext"
- "xpathCtx"
- "xpathObj"
- "xpathResultSet"
- "xpcConnection"
- "xpcQueue"
- "zeroPassword"
- "zone"

```
