## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/PlatformSSOCore`

```diff

-417.120.4.0.0
-  __TEXT.__text: 0x9a7e0
-  __TEXT.__auth_stubs: 0x1bd0
-  __TEXT.__objc_methlist: 0x5c28
-  __TEXT.__const: 0x1574
-  __TEXT.__cstring: 0xb805
-  __TEXT.__oslogstring: 0x19cf
-  __TEXT.__gcc_except_tab: 0x780
+483.0.6.0.1
+  __TEXT.__text: 0x8d8f4
+  __TEXT.__auth_stubs: 0x1ae0
+  __TEXT.__objc_methlist: 0x5ea8
+  __TEXT.__const: 0x1704
+  __TEXT.__cstring: 0xa32c
+  __TEXT.__oslogstring: 0x1a07
+  __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__swift5_typeref: 0x16e
+  __TEXT.__swift5_typeref: 0x158
   __TEXT.__constg_swiftt: 0x348
   __TEXT.__swift5_reflstr: 0x146
   __TEXT.__swift5_fieldmd: 0x118

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x2158
-  __TEXT.__eh_frame: 0x6c0
-  __TEXT.__objc_classname: 0xd48
-  __TEXT.__objc_methname: 0xbba7
-  __TEXT.__objc_methtype: 0x288e
-  __TEXT.__objc_stubs: 0x6be0
-  __DATA_CONST.__got: 0x938
-  __DATA_CONST.__const: 0x2440
-  __DATA_CONST.__objc_classlist: 0x4b8
+  __TEXT.__unwind_info: 0x1fb8
+  __TEXT.__eh_frame: 0x5b8
+  __TEXT.__objc_classname: 0xd3d
+  __TEXT.__objc_methname: 0xc7b2
+  __TEXT.__objc_methtype: 0x28de
+  __TEXT.__objc_stubs: 0x7000
+  __DATA_CONST.__got: 0x920
+  __DATA_CONST.__const: 0x2420
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28d0
+  __DATA_CONST.__objc_selrefs: 0x2ab8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__auth_got: 0xdf8
-  __AUTH_CONST.__const: 0x7d0
-  __AUTH_CONST.__cfstring: 0x71e0
-  __AUTH_CONST.__objc_const: 0x13e58
-  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__auth_got: 0xd80
+  __AUTH_CONST.__const: 0x780
+  __AUTH_CONST.__cfstring: 0x7300
+  __AUTH_CONST.__objc_const: 0x14188
+  __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x3450
+  __AUTH.__objc_data: 0x3400
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x5c4
-  __DATA.__data: 0xfa2
-  __DATA.__bss: 0xd18
-  __DATA.__common: 0x90
+  __DATA.__objc_ivar: 0x610
+  __DATA.__data: 0x1040
+  __DATA.__bss: 0xd31
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: AD86FEE9-1B73-31B0-BE56-2A11944189B3
-  Functions: 3772
-  Symbols:   12208
-  CStrings:  5091
+  UUID: B7CA57D7-F8ED-38A1-8294-B1ABEE04BC87
+  Functions: 3583
+  Symbols:   11910
+  CStrings:  5044
 
Symbols:
+ +[POPreferences buddyTestMode]
+ +[POPreferences skipPreMDMDeviceRegistration]
+ +[POSecKeyHelper isSystemKey:]
+ +[POTokenHelper parseUserNameFromMailboxData:]
+ +[POTokenHelper parseUserNameFromMailboxData:].cold.1
+ +[POTokenHelper parseUserNameFromMailboxData:].cold.2
+ +[POTokenHelper parseUserNameFromMailboxData:].cold.3
+ +[POTokenHelper parseUserNameFromMailboxData:].cold.4
+ +[POTokenHelper parseUserNameFromMailboxData:].cold.5
+ +[POTokenHelper tokenIsAccessKey:]
+ -[POAgentCoreProcess callerUid]
+ -[POAgentCoreProcess setCallerUid:]
+ -[POAuthenticationContext applyResumeData:]
+ -[POAuthenticationContext isServerNonceExpiredOrMissing]
+ -[POAuthenticationContext resumeData]
+ -[POAuthenticationContext resumeData].cold.1
+ -[POAuthenticationContext resumedEmbeddedAssertion]
+ -[POAuthenticationContext serverNonceReceived]
+ -[POAuthenticationContext setResumedEmbeddedAssertion:]
+ -[POAuthenticationContext setServerNonceReceived:]
+ -[POAuthenticationProcess completeAccessTokenLoginUsingContext:completion:]
+ -[POAuthenticationProcess createAuthenticationContextUsingLoginConfiguration:deviceConfiguration:userName:resumeData:]
+ -[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]
+ -[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]
+ -[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:].cold.1
+ -[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]
+ -[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]
+ -[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:].cold.1
+ -[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:].cold.2
+ -[PODeviceConfiguration _accessTokenTerminalIdentityCertData]
+ -[PODeviceConfiguration _accessTokenTerminalIdentityKeyData]
+ -[PODeviceConfiguration _accessTokenTerminalIdentityKeySEP]
+ -[PODeviceConfiguration _accessTokenTerminalIdentityKeySystem]
+ -[PODeviceConfiguration accessTokenReaderGroupIdentifier]
+ -[PODeviceConfiguration accessTokenTerminalIdentity]
+ -[PODeviceConfiguration allowAccessTokenExpressMode]
+ -[PODeviceConfiguration createFirstUserDuringSetupEnabled]
+ -[PODeviceConfiguration createUserLoginTypes]
+ -[PODeviceConfiguration hasTemporaryAccountCredential]
+ -[PODeviceConfiguration lastCheckDate]
+ -[PODeviceConfiguration setAccessTokenReaderGroupIdentifier:]
+ -[PODeviceConfiguration setAccessTokenTerminalIdentity:]
+ -[PODeviceConfiguration setAllowAccessTokenExpressMode:]
+ -[PODeviceConfiguration setCreateFirstUserDuringSetupEnabled:]
+ -[PODeviceConfiguration setCreateUserLoginTypes:]
+ -[PODeviceConfiguration setLastCheckDate:]
+ -[PODeviceConfiguration setSynchronizeProfilePicture:]
+ -[PODeviceConfiguration set_accessTokenTerminalIdentityCertData:]
+ -[PODeviceConfiguration set_accessTokenTerminalIdentityKeyData:]
+ -[PODeviceConfiguration set_accessTokenTerminalIdentityKeySEP:]
+ -[PODeviceConfiguration set_accessTokenTerminalIdentityKeySystem:]
+ -[PODeviceConfiguration supportsAccessKey]
+ -[PODeviceConfiguration supportsAccessKey].cold.1
+ -[PODeviceConfiguration supportsCreateFirstUserDuringSetup]
+ -[PODeviceConfiguration supportsCreateFirstUserDuringSetup].cold.1
+ -[PODeviceConfiguration synchronizeProfilePicture]
+ -[POJWTSigning encodeAndSignJWT:key:certificate:error:].cold.1
+ -[POLoginConfiguration serverNonceExpirationTime]
+ -[POLoginConfiguration setServerNonceExpirationTime:]
+ -[POServiceCoreConnection performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:]
+ -[POUserConfiguration _loginContext]
+ -[POUserConfiguration _setupContext]
+ -[POUserConfiguration _setupPINContext]
+ -[POUserConfiguration _setupWrapHash]
+ -[POUserConfiguration lastCheckDate]
+ -[POUserConfiguration setLastCheckDate:]
+ -[POUserConfiguration set_loginContext:]
+ -[POUserConfiguration set_setupContext:]
+ -[POUserConfiguration set_setupPINContext:]
+ -[POUserConfiguration set_setupWrapHash:]
+ GCC_except_table123
+ GCC_except_table147
+ GCC_except_table348
+ GCC_except_table403
+ _OBJC_CLASS_$_LAStorage
+ _OBJC_CLASS_$_TKBERTLVRecord
+ _OBJC_IVAR_$_POAgentCoreProcess._callerUid
+ _OBJC_IVAR_$_POAuthenticationContext._resumedEmbeddedAssertion
+ _OBJC_IVAR_$_POAuthenticationContext._serverNonceReceived
+ _OBJC_IVAR_$_PODeviceConfiguration.__accessTokenTerminalIdentityCertData
+ _OBJC_IVAR_$_PODeviceConfiguration.__accessTokenTerminalIdentityKeyData
+ _OBJC_IVAR_$_PODeviceConfiguration.__accessTokenTerminalIdentityKeySEP
+ _OBJC_IVAR_$_PODeviceConfiguration.__accessTokenTerminalIdentityKeySystem
+ _OBJC_IVAR_$_PODeviceConfiguration._accessTokenReaderGroupIdentifier
+ _OBJC_IVAR_$_PODeviceConfiguration._allowAccessTokenExpressMode
+ _OBJC_IVAR_$_PODeviceConfiguration._createFirstUserDuringSetupEnabled
+ _OBJC_IVAR_$_PODeviceConfiguration._createUserLoginTypes
+ _OBJC_IVAR_$_PODeviceConfiguration._lastCheckDate
+ _OBJC_IVAR_$_PODeviceConfiguration._synchronizeProfilePicture
+ _OBJC_IVAR_$_POLoginConfiguration._serverNonceExpirationTime
+ _OBJC_IVAR_$_POUserConfiguration.__loginContext
+ _OBJC_IVAR_$_POUserConfiguration.__setupContext
+ _OBJC_IVAR_$_POUserConfiguration.__setupPINContext
+ _OBJC_IVAR_$_POUserConfiguration.__setupWrapHash
+ _OBJC_IVAR_$_POUserConfiguration._lastCheckDate
+ _PO_LOG_POAuthenticationContext
+ _PO_LOG_POAuthenticationContext.cold.1
+ _PO_LOG_POAuthenticationContext.log
+ _PO_LOG_POAuthenticationContext.once
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1006
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1006.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1012
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1012.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1013
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1013.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1020
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1020.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1026
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1026.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1030
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1030.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1034
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1034.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1037
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1037.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1040
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1040.cold.1
+ ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.991
+ ___116-[POServiceCoreConnection performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:]_block_invoke
+ ___116-[POServiceCoreConnection performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:]_block_invoke.cold.1
+ ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke
+ ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.1140
+ ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.1140.cold.1
+ ___121-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]_block_invoke.cold.1
+ ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke
+ ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1131
+ ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1131.cold.1
+ ___134-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:]_block_invoke.cold.1
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.111.cold.1
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.115
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.116.cold.1
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.120.cold.1
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.124
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.124.cold.1
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.128
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.129
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.129.cold.1
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.133
+ ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.133.cold.1
+ ___30+[POPreferences buddyTestMode]_block_invoke
+ ___30+[POPreferences buddyTestMode]_block_invoke.cold.1
+ ___36-[POUserConfiguration initWithData:]_block_invoke.157
+ ___37-[POAuthenticationContext resumeData]_block_invoke
+ ___37-[POAuthenticationContext resumeData]_block_invoke.cold.1
+ ___37-[POLoginConfiguration initWithData:]_block_invoke.300
+ ___38-[PODeviceConfiguration initWithData:]_block_invoke.172
+ ___43-[POAuthenticationContext applyResumeData:]_block_invoke
+ ___43-[POAuthenticationContext applyResumeData:]_block_invoke.cold.1
+ ___45+[POPreferences skipPreMDMDeviceRegistration]_block_invoke
+ ___45+[POPreferences skipPreMDMDeviceRegistration]_block_invoke.cold.1
+ ___52-[PODeviceConfiguration accessTokenTerminalIdentity]_block_invoke
+ ___52-[PODeviceConfiguration accessTokenTerminalIdentity]_block_invoke.cold.1
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.29
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.29.cold.1
+ ___56-[PODeviceConfiguration setAccessTokenTerminalIdentity:]_block_invoke.cold.1
+ ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1051
+ ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1051.cold.1
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.54
+ ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.54.cold.1
+ ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1070
+ ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1070.cold.1
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.38
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.38.cold.1
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.44
+ ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.44.cold.1
+ ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1105
+ ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1105.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.920
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.935
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.935.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.941
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.941.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.942
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.942.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.949
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.949.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.955
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.955.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.959
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.959.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.966
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.966.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.981
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.981.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.987
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.987.cold.1
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.988
+ ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.988.cold.1
+ ___75-[POAuthenticationProcess completeAccessTokenLoginUsingContext:completion:]_block_invoke
+ ___75-[POAuthenticationProcess completeAccessTokenLoginUsingContext:completion:]_block_invoke.cold.1
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1073
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1073.cold.1
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1083
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1088
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1089
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1084
+ ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1084.cold.1
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1158
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1158.cold.1
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1164
+ ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1164.cold.1
+ ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke
+ ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.902
+ ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.902.cold.1
+ ___76-[POAuthenticationProcess performAccessTokenSigningUsingContext:completion:]_block_invoke.cold.1
+ ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke
+ ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke.897
+ ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke.cold.1
+ ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke_2
+ ___77-[POAuthenticationProcess prepareForAccessTokenLoginUsingContext:completion:]_block_invoke_2.cold.1
+ ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.508
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1108
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1108.cold.1
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1118
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1123
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1124
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1119
+ ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1119.cold.1
+ ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1095
+ ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1095.cold.1
+ ___PO_LOG_POAuthenticationContext_block_invoke
+ ___block_descriptor_56_e8_32s40bs_e8_v16?0Q8ls40l8s32l8
+ ___block_descriptor_tmp.153
+ ___block_descriptor_tmp.169
+ ___block_literal_global.102
+ ___block_literal_global.1418
+ ___block_literal_global.1422
+ ___block_literal_global.155
+ ___block_literal_global.171
+ ___block_literal_global.254
+ ___block_literal_global.443
+ ___block_literal_global.601
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
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PlatformSSOCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PlatformSSOCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PlatformSSOCore
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
+ _buddyTestMode.buddyTestMode
+ _buddyTestMode.onceToken
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
+ _objc_msgSend$_accessTokenTerminalIdentityKeySEP
+ _objc_msgSend$_accessTokenTerminalIdentityKeySystem
+ _objc_msgSend$accessTokenReaderGroupIdentifier
+ _objc_msgSend$allowAccessTokenExpressMode
+ _objc_msgSend$applyResumeData:
+ _objc_msgSend$completeAccessTokenLoginUsingContext:completion:
+ _objc_msgSend$compressedDataUsingAlgorithm:error:
+ _objc_msgSend$createAuthenticationContextUsingLoginConfiguration:deviceConfiguration:userName:resumeData:
+ _objc_msgSend$createFirstUserDuringSetupEnabled
+ _objc_msgSend$createUserLoginTypes
+ _objc_msgSend$dataForKey:error:
+ _objc_msgSend$decompressedDataUsingAlgorithm:error:
+ _objc_msgSend$effectiveUserIdentifier
+ _objc_msgSend$ephemeralKeyForData:
+ _objc_msgSend$extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:
+ _objc_msgSend$initWithDomain:authenticationContext:
+ _objc_msgSend$isSEPKey:
+ _objc_msgSend$isSystemKey:
+ _objc_msgSend$keychainHelper
+ _objc_msgSend$performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:
+ _objc_msgSend$recordFromData:
+ _objc_msgSend$resumeData
+ _objc_msgSend$resumedEmbeddedAssertion
+ _objc_msgSend$retrieveCertAndKeyForTokenId:context:forSigning:hash:certificate:privateKey:
+ _objc_msgSend$sequenceOfRecordsFromData:
+ _objc_msgSend$serverNonceExpirationTime
+ _objc_msgSend$serverNonceReceived
+ _objc_msgSend$setResumedEmbeddedAssertion:
+ _objc_msgSend$setServerNonceReceived:
+ _objc_msgSend$supportsCreateFirstUserDuringSetup
+ _objc_msgSend$supportsCreateNewUsers
+ _objc_msgSend$supportsCreateTemporaryUsers
+ _objc_msgSend$synchronizeProfilePicture
+ _objc_msgSend$tag
+ _objc_msgSend$tokenIsAccessKey:
+ _ref_key_create_request_to_class
+ _se_derivation_request_deserialize
+ _se_derivation_request_serialization_len
+ _se_derivation_request_serialize
+ _set_akslog_context
+ _set_akslog_pid
+ _skipPreMDMDeviceRegistration.onceToken
+ _skipPreMDMDeviceRegistration.skipPreMDMDeviceRegistration
+ _swift_release_n
+ _swift_setDeallocating
+ _vsnprintf
- +[POACMHelper clearSmartCardPIN]
- +[POACMHelper createPlatformSSOSystemKey:]
- +[POACMHelper platformSSOSystemKey]
- +[POACMHelper platformSSOSystemKey].cold.1
- -[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]
- GCC_except_table13
- GCC_except_table146
- GCC_except_table335
- _ACMContextAddCredential
- _ACMContextAddCredentialWithScope
- _ACMContextContainsCredentialType
- _ACMContextContainsCredentialTypeEx
- _ACMContextContainsPassphraseCredentialWithPurpose
- _ACMContextCreate
- _ACMContextCreateWithExternalForm
- _ACMContextCredentialGetProperty
- _ACMContextDelete
- _ACMContextGetData
- _ACMContextGetDataEx
- _ACMContextGetDataProperty
- _ACMContextGetExternalForm
- _ACMContextGetExternalForm.cold.1
- _ACMContextGetInfo
- _ACMContextGetTrackingNumber
- _ACMContextRemoveCredentialsByType
- _ACMContextRemoveCredentialsByTypeAndScope
- _ACMContextRemoveCredentialsByValue
- _ACMContextRemoveCredentialsByValueAndScope
- _ACMContextRemovePassphraseCredentialsByPurposeAndScope
- _ACMContextReplacePassphraseCredentialsWithScope
- _ACMContextSetData
- _ACMContextSetDataEx
- _ACMContextVerifyAclConstraint
- _ACMContextVerifyAclConstraintForOperation
- _ACMContextVerifyPolicy
- _ACMContextVerifyPolicyEx
- _ACMContextVerifyPolicyWithPreflight
- _ACMCredentialCreate
- _ACMCredentialDelete
- _ACMCredentialGetProperty
- _ACMCredentialGetPropertyData
- _ACMCredentialGetType
- _ACMCredentialSetProperty
- _ACMGetAclAuthMethod
- _ACMGetEnvironmentVariable
- _ACMGlobalContextAddCredential
- _ACMGlobalContextCredentialGetProperty
- _ACMGlobalContextRemoveCredentialsByType
- _ACMGlobalContextVerifyPolicy
- _ACMKernelControl
- _ACMParseAclAndCopyConstraintCharacteristics
- _ACMPing
- _ACMRequirementGetPriority
- _ACMRequirementGetProperties
- _ACMRequirementGetProperty
- _ACMRequirementGetPropertyData
- _ACMRequirementGetState
- _ACMRequirementGetSubrequirements
- _ACMRequirementGetType
- _ACMSEPControl
- _ACMSEPControlEx
- _ACMSetEnvironmentVariable
- _ACMSetEnvironmentVariableWithAccessPolicy
- _CompareCredentials
- _CopyCredential
- _DeallocCredentialList
- _DeserializeAddCredential
- _DeserializeAddCredentialType
- _DeserializeCredential
- _DeserializeCredentialList
- _DeserializeGetContextProperty
- _DeserializeProcessAcl
- _DeserializeRemoveCredential
- _DeserializeReplacePassphraseCredential
- _DeserializeRequirement
- _DeserializeVerifyAclConstraint
- _DeserializeVerifyPolicy
- _GetSerializedAddCredentialSize
- _GetSerializedCredentialSize
- _GetSerializedGetContextPropertySize
- _GetSerializedProcessAclSize
- _GetSerializedRemoveCredentialSize
- _GetSerializedReplacePassphraseCredentialSize
- _GetSerializedRequirementSize
- _GetSerializedVerifyAclConstraintSize
- _GetSerializedVerifyPolicySize
- _IOConnectCallScalarMethod
- _IOConnectCallStructMethod
- _LibCall_ACMContexAddCredentialWithScope
- _LibCall_ACMContexRemoveCredentialsByTypeAndScope
- _LibCall_ACMContextCreate
- _LibCall_ACMContextCreateWithExternalForm
- _LibCall_ACMContextCredentialGetProperty
- _LibCall_ACMContextDelete
- _LibCall_ACMContextGetData
- _LibCall_ACMContextGetInfo
- _LibCall_ACMContextLoadFromImage
- _LibCall_ACMContextRemoveCredentialsByValueAndScope
- _LibCall_ACMContextSetData
- _LibCall_ACMContextUnloadToImage
- _LibCall_ACMContextUnloadToImage_Block
- _LibCall_ACMContextVerifyAclConstraint
- _LibCall_ACMContextVerifyAclConstraintForOperation
- _LibCall_ACMContextVerifyPolicyAndCopyRequirementEx
- _LibCall_ACMContextVerifyPolicyEx
- _LibCall_ACMContextVerifyPolicyEx_Block
- _LibCall_ACMContextVerifyPolicyWithPreflight_Block
- _LibCall_ACMContextVerifyPolicy_Block
- _LibCall_ACMCredentialCreate
- _LibCall_ACMCredentialDelete
- _LibCall_ACMCredentialGetPropertyData
- _LibCall_ACMCredentialGetType
- _LibCall_ACMCredentialSetProperty
- _LibCall_ACMGetAclAuthMethod_Block
- _LibCall_ACMGetEnvironmentVariable
- _LibCall_ACMGetEnvironmentVariable_Block
- _LibCall_ACMGlobalContextCredentialGetProperty
- _LibCall_ACMGlobalContextCredentialGetProperty_Block
- _LibCall_ACMGlobalContextVerifyPolicyEx
- _LibCall_ACMGlobalContextVerifyPolicy_Block
- _LibCall_ACMKernDoubleClickNotify
- _LibCall_ACMKernelControl
- _LibCall_ACMKernelControl.cold.1
- _LibCall_ACMKernelControl_Block
- _LibCall_ACMPing
- _LibCall_ACMPublishTrustedAccessories
- _LibCall_ACMRequirementDelete
- _LibCall_ACMRequirementGetPriority
- _LibCall_ACMRequirementGetPropertyData
- _LibCall_ACMRequirementGetState
- _LibCall_ACMRequirementGetType
- _LibCall_ACMSEPControl
- _LibCall_ACMSEPControl_Block
- _LibCall_ACMSecContextGetUnlockSecret
- _LibCall_ACMSecContextProcessAcl
- _LibCall_ACMSecContextProcessAclAndCopyAuthMethod
- _LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement
- _LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser
- _LibCall_ACMSecSetBiometryAvailability
- _LibCall_ACMSecSetBuiltinBiometry
- _LibCall_ACMSetEnvironmentVariable
- _LibCall_ACMTRMLoadState
- _LibCall_ACMTRMLoadState_Block
- _LibCall_ACMTRMSaveState
- _LibCall_BuildCommand
- _LibSer_ContextCredentialGetProperty_Deserialize
- _LibSer_ContextCredentialGetProperty_GetSize
- _LibSer_ContextCredentialGetProperty_Serialize
- _LibSer_DeleteContext_Deserialize
- _LibSer_DeleteContext_GetSize
- _LibSer_DeleteContext_Serialize
- _LibSer_GetAclAuthMethod_Deserialize
- _LibSer_GetAclAuthMethod_GetSize
- _LibSer_GetAclAuthMethod_Serialize
- _LibSer_GetUnlockSecretResponse_Deserialize
- _LibSer_GetUnlockSecretResponse_GetSize
- _LibSer_GetUnlockSecretResponse_Serialize
- _LibSer_GetUnlockSecret_Deserialize
- _LibSer_GetUnlockSecret_GetSize
- _LibSer_GetUnlockSecret_Serialize
- _LibSer_GlobalContextCredentialGetProperty_Deserialize
- _LibSer_GlobalContextCredentialGetProperty_GetSize
- _LibSer_GlobalContextCredentialGetProperty_Serialize
- _LibSer_RemoveCredentialByType_Deserialize
- _LibSer_RemoveCredentialByType_GetSize
- _LibSer_RemoveCredentialByType_Serialize
- _LibSer_SEPControlResponse_Deserialize
- _LibSer_SEPControlResponse_GetSize
- _LibSer_SEPControlResponse_Serialize
- _LibSer_SEPControl_Deserialize
- _LibSer_SEPControl_GetSize
- _LibSer_SEPControl_Serialize
- _LibSer_StorageAnyCmd_DeserializeCommonFields
- _LibSer_StorageGetData_Deserialize
- _LibSer_StorageGetData_GetSize
- _LibSer_StorageGetData_Serialize
- _LibSer_StorageSetData_Deserialize
- _LibSer_StorageSetData_GetSize
- _LibSer_StorageSetData_Serialize
- _OBJC_CLASS_$_POACMHelper
- _OBJC_METACLASS_$_POACMHelper
- _OUTLINED_FUNCTION_75
- _PO_LOG_POACMHelper
- _PO_LOG_POACMHelper.cold.1
- _PO_LOG_POACMHelper.log
- _PO_LOG_POACMHelper.once
- _SerializeAddCredential
- _SerializeCredential
- _SerializeCredentialList
- _SerializeGetContextProperty
- _SerializeProcessAcl
- _SerializeRemoveCredential
- _SerializeReplacePassphraseCredential
- _SerializeRequirement
- _SerializeVerifyAclConstraint
- _SerializeVerifyPolicy
- _Util_AllocCredential
- _Util_AllocRequirement
- _Util_CreateRequirement
- _Util_DeallocCredential
- _Util_DeallocRequirement
- _Util_GetBitCount
- _Util_KeybagLockStateToEnvVar
- _Util_ReadFromBuffer
- _Util_SafeDeallocParameters
- _Util_WriteToBuffer
- _Util_hexDumpToStrHelper
- _Util_hexDumpToStrHelper.cold.1
- _Util_hexDumpToStrHelper.cold.2
- _Util_isNonNullEqualMemory
- _Util_isNullOrZeroMemory
- __MergedGlobals
- __OBJC_$_CLASS_METHODS_POACMHelper
- __OBJC_CLASS_RO_$_POACMHelper
- __OBJC_METACLASS_RO_$_POACMHelper
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1001
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1001.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1008
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1008.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1014
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1014.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1018
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1018.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1022
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1022.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1025
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1025.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1028
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.1028.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.979
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.982
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.982.cold.1
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.988
- ___100-[POAuthenticationProcess performKeyExchangeRequestUsingContext:otherPartyPublicKeyData:completion:]_block_invoke.988.cold.1
- ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke
- ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1119
- ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.1119.cold.1
- ___123-[POAuthenticationProcess extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:]_block_invoke.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.110
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.110.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.114
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.114.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.118
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.119
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.119.cold.1
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.123
- ___143-[POAgentCoreProcess _verifyLogin:passwordContext:smartCardContext:tokenId:deviceConfiguration:loginConfiguration:forAuthorization:completion:]_block_invoke.123.cold.1
- ___32+[POACMHelper clearSmartCardPIN]_block_invoke
- ___32+[POACMHelper clearSmartCardPIN]_block_invoke.cold.1
- ___35+[POACMHelper platformSSOSystemKey]_block_invoke
- ___35+[POACMHelper platformSSOSystemKey]_block_invoke.1
- ___35+[POACMHelper platformSSOSystemKey]_block_invoke.1.cold.1
- ___36-[POUserConfiguration initWithData:]_block_invoke.147
- ___37-[POLoginConfiguration initWithData:]_block_invoke.297
- ___38-[PODeviceConfiguration initWithData:]_block_invoke.135
- ___42+[POACMHelper createPlatformSSOSystemKey:]_block_invoke
- ___42+[POACMHelper createPlatformSSOSystemKey:]_block_invoke.cold.1
- ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1039
- ___58-[POAuthenticationProcess createKeyRequestJWTWithContext:]_block_invoke.1039.cold.1
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.38
- ___58-[PODeviceConfiguration decryptTemporaryAccountCredential]_block_invoke.38.cold.1
- ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1058
- ___59-[POAuthenticationProcess createKeyRequestWithContext:jwt:]_block_invoke.1058.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.23
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.23.cold.1
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.29
- ___66-[PODeviceConfiguration encryptAndSaveTemporaryAccountCredential:]_block_invoke.29.cold.1
- ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1093
- ___67-[POAuthenticationProcess createKeyExchangeRequestWithContext:jwt:]_block_invoke.1093.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.908
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.911
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.911.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.917
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.917.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.930
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.930.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.937
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.937.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.943
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.943.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.947
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.947.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.951
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.951.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.954
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.954.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.957
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.957.cold.1
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.976
- ___68-[POAuthenticationProcess performKeyRequestUsingContext:completion:]_block_invoke.976.cold.1
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1061
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1061.cold.1
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1065
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1071
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke.1076
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1072
- ___75-[POAuthenticationProcess performKeyRequestWithContext:request:completion:]_block_invoke_2.1072.cold.1
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1130
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1130.cold.1
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1136
- ___76-[POAuthenticationProcess URLSession:didReceiveChallenge:completionHandler:]_block_invoke.1136.cold.1
- ___78-[POAuthenticationProcess _performNonceRequestWithContext:request:completion:]_block_invoke_2.507
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1096
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1096.cold.1
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1100
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1106
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke.1111
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1107
- ___83-[POAuthenticationProcess performKeyExchangeRequestWithContext:request:completion:]_block_invoke_2.1107.cold.1
- ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1083
- ___86-[POAuthenticationProcess createKeyExchangeRequestJWTWithContext:otherPartyPublicKey:]_block_invoke.1083.cold.1
- ___PO_LOG_POACMHelper_block_invoke
- ___block_descriptor_40_e8_32r_e13_v24?0r^v8Q16lr32l8
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.171
- ___block_literal_global.100
- ___block_literal_global.1383
- ___block_literal_global.1387
- ___block_literal_global.156
- ___block_literal_global.173
- ___block_literal_global.22
- ___block_literal_global.236
- ___block_literal_global.356
- ___block_literal_global.594
- __allocatedMem.0
- __allocatedMem.2
- __allocatedMem.3
- __logLevel
- __os_log_default
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_PlatformSSOCore
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_PlatformSSOCore
- _aclRequiresPasscodeInternal
- _acm_explicit_bzero
- _acm_get_mem
- _acm_mem_alloc
- _acm_mem_alloc_data
- _acm_mem_alloc_info
- _acm_mem_free
- _acm_mem_free_data
- _acm_mem_free_info
- _aks_change_secret_epilogue.cold.1
- _aks_change_secret_opts.cold.1
- _aks_recover_with_escrow_bag.cold.1
- _aks_set_system_with_passcode.cold.1
- _aks_unlock_bag.cold.1
- _checkParameter
- _der_key_validate
- _der_key_validate.cold.1
- _der_key_validate.cold.2
- _deserializeParameters
- _gACMLoggingLevel
- _gAllocatedBytes
- _getLengthOfParameters
- _get_aks_log_pid
- _init
- _ioKitTransport
- _malloc_type_calloc
- _objc_msgSend$extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:
- _objc_msgSend$initWithBytes:length:
- _performCommand
- _processAclCommandInternal
- _serializeParameters
- _strnlen
- _swift_allocError
- _swift_deallocObject
- _swift_errorRetain
- _swift_getObjCClassMetadata
- _symbolic SaySsG
- _symbolic _____ SS5IndexV
- _symbolic _____Sg 9CryptoKit3AESO3GCMO5NonceV
- _updateLogLevelFromKext
- _updateLogLevelFromKext.cold.1
- _verifyAclConstraintForOperationCommandInternal
- _verifyAclConstraintInternal
CStrings:
+ "%s asid= %{public}d, euid= %{public}d on %@"
+ "%s shared = %{public}@, createUsersInSetupAssistantEnabled = %{public}@ on %@"
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
+ "&"
+ "-[POAuthenticationProcess extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:]"
+ "-[PODeviceConfiguration supportsAccessKey]"
+ "-[PODeviceConfiguration supportsCreateFirstUserDuringSetup]"
+ "Access key login failed"
+ "B64@0:8@16@24@32^@40^@48^@56"
+ "BuddyTestMode"
+ "Complete NFC login"
+ "Configuration for: %{public}@"
+ "Error compressing resume data"
+ "Error with SecIdentityCopyCertificate."
+ "Error with SecIdentityCopyPrivateKey."
+ "Failed to create certificate or key"
+ "Failed to parse mailbox data"
+ "Failed to parse sso tokens"
+ "Failed to retrieve auth data"
+ "Incorrect username tag"
+ "Invalid mailbox data size: %lu"
+ "Missing id_token."
+ "POLoginTypeAccessKey"
+ "Perform NFC signing"
+ "PlatformSSO_AccessKeyAuth"
+ "Prepare NFC login authentication"
+ "Resume data compression: %{public}@, %{public}@"
+ "Signing Data: %ld"
+ "T@\"NSArray\",C,N,V_createUserLoginTypes"
+ "T@\"NSData\",&,N,V__accessTokenTerminalIdentityCertData"
+ "T@\"NSData\",&,N,V__accessTokenTerminalIdentityKeyData"
+ "T@\"NSData\",C,N,V_accessTokenReaderGroupIdentifier"
+ "T@\"NSData\",C,V__loginContext"
+ "T@\"NSData\",C,V__setupContext"
+ "T@\"NSData\",C,V__setupPINContext"
+ "T@\"NSData\",C,V__setupWrapHash"
+ "T@\"NSDate\",C,N,V_lastCheckDate"
+ "T@\"NSDate\",C,N,V_serverNonceReceived"
+ "T@\"NSNumber\",C,N,V_serverNonceExpirationTime"
+ "T@\"NSString\",C,N,V_apv"
+ "T@\"NSString\",C,N,V_encryptionContext"
+ "T@\"NSString\",C,N,V_nonce"
+ "T@\"NSString\",C,N,V_refreshToken"
+ "T@\"NSString\",C,N,V_requestIdentifier"
+ "T@\"NSString\",C,N,V_resumedEmbeddedAssertion"
+ "T@\"NSString\",C,N,V_scope"
+ "T@\"NSString\",C,N,V_serverNonce"
+ "T@\"NSString\",C,N,V_tokenTypeNamespace"
+ "T@\"NSString\",C,N,V_userName"
+ "T@\"NSString\",C,N,V_wsTrustFederationNonce"
+ "T@\"NSURL\",C,N,V_wsTrustFederationMexURL"
+ "T@\"NSURL\",C,N,V_wsTrustFederationURL"
+ "TB,N,V__accessTokenTerminalIdentityKeySEP"
+ "TB,N,V__accessTokenTerminalIdentityKeySystem"
+ "TB,V_allowAccessTokenExpressMode"
+ "TB,V_createFirstUserDuringSetupEnabled"
+ "TB,V_synchronizeProfilePicture"
+ "TI,N,V_callerUid"
+ "T^{__SecIdentity=}"
+ "Unsupported platform"
+ "Username is to big"
+ "__accessTokenTerminalIdentityCertData"
+ "__accessTokenTerminalIdentityKeyData"
+ "__accessTokenTerminalIdentityKeySEP"
+ "__accessTokenTerminalIdentityKeySystem"
+ "__loginContext"
+ "__setupContext"
+ "__setupPINContext"
+ "__setupWrapHash"
+ "_accessTokenReaderGroupIdentifier"
+ "_accessTokenTerminalIdentityCertData"
+ "_accessTokenTerminalIdentityKeyData"
+ "_accessTokenTerminalIdentityKeySEP"
+ "_accessTokenTerminalIdentityKeySystem"
+ "_aks_backup_enable_volume"
+ "_aks_change_secret_epilogue"
+ "_aks_recover_with_escrow_bag"
+ "_aks_se_get_reset_token_for_memento_secret"
+ "_aks_set_configuration"
+ "_aks_set_system_with_passcode"
+ "_aks_unlock_bag"
+ "_aks_unlock_with_sync_bag"
+ "_allowAccessTokenExpressMode"
+ "_callerUid"
+ "_createFirstUserDuringSetupEnabled"
+ "_createUserLoginTypes"
+ "_lastCheckDate"
+ "_loginContext"
+ "_resumedEmbeddedAssertion"
+ "_serverNonceExpirationTime"
+ "_serverNonceReceived"
+ "_setupContext"
+ "_setupPINContext"
+ "_setupWrapHash"
+ "_synchronizeProfilePicture"
+ "accessKeyReaderGroupIdentifier"
+ "accessTokenReaderGroupIdentifier"
+ "accessTokenTerminalIdentity"
+ "aks_change_secret_with_kek"
+ "aks_enable_cache_flow"
+ "aks_get_icsc_srp"
+ "aks_reset_iteration_count"
+ "aks_se_get_passcode_derivation"
+ "aks_se_memento_secret_drop"
+ "aks_se_recover_with_acm"
+ "aks_unlock_device_with_acm"
+ "allowAccessKeyExpressMode"
+ "allowAccessTokenExpressMode"
+ "applyResumeData:"
+ "buddyTestMode"
+ "buddyTestMode=%{public}s"
+ "callerUid"
+ "com.apple.PlatformSSO.AccessKey"
+ "completeAccessTokenLoginUsingContext:completion:"
+ "compressedDataUsingAlgorithm:error:"
+ "createAuthenticationContextUsingLoginConfiguration:deviceConfiguration:userName:resumeData:"
+ "createFirstUserDuringSetupEnabled"
+ "createUserLoginTypes"
+ "dataForKey:error:"
+ "decompressedDataUsingAlgorithm:error:"
+ "effectiveUserIdentifier"
+ "extractGroupsAndSubUsingAuthorizationWithLoginConfiguration:tokens:returningGroups:identifier:refreshToken:"
+ "extractNewUserValuesFromTokens:deviceConfiguration:loginUserName:returningName:userName:error:"
+ "failed to open connection to %s: %d\n"
+ "failed to open userclient via %s: %d\n"
+ "hasTemporaryAccountCredential"
+ "initWithDomain:authenticationContext:"
+ "isServerNonceExpiredOrMissing"
+ "isSystemKey:"
+ "lastCheckDate"
+ "mailboxdata: %@"
+ "parseUserNameFromMailboxData:"
+ "performAccessTokenSigningUsingContext:completion:"
+ "performPasswordLogin:loginUserName:passwordContext:updateLocalAccountPassword:completion:"
+ "prepareForAccessTokenLoginUsingContext:completion:"
+ "recordFromData:"
+ "resumeData"
+ "resumedEmbeddedAssertion"
+ "sequenceOfRecordsFromData:"
+ "serverNonceExpirationTime"
+ "serverNonceReceived"
+ "setAccessTokenReaderGroupIdentifier:"
+ "setAccessTokenTerminalIdentity:"
+ "setAllowAccessTokenExpressMode:"
+ "setCallerUid:"
+ "setCreateFirstUserDuringSetupEnabled:"
+ "setCreateUserLoginTypes:"
+ "setLastCheckDate:"
+ "setResumedEmbeddedAssertion:"
+ "setServerNonceExpirationTime:"
+ "setServerNonceReceived:"
+ "setSynchronizeProfilePicture:"
+ "set_accessTokenTerminalIdentityCertData:"
+ "set_accessTokenTerminalIdentityKeyData:"
+ "set_accessTokenTerminalIdentityKeySEP:"
+ "set_accessTokenTerminalIdentityKeySystem:"
+ "set_loginContext:"
+ "set_setupContext:"
+ "set_setupPINContext:"
+ "set_setupWrapHash:"
+ "skipPreMDMDeviceRegistration"
+ "skipPreMDMDeviceRegistration=%{public}s"
+ "supportsAccessKey"
+ "supportsCreateFirstUserDuringSetup"
+ "synchronizeProfilePicture"
+ "tokenIsAccessKey:"
+ "v24@0:8^{__SecIdentity=}16"
+ "v52@0:8@16@24@32B40@?44"
- "%02x "
- "%s asid= %{public}d on %@"
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
- "%s: %s (len=%u): acl:"
- "%s: %s (len=%u): operation:"
- "%s: %s: CS[%u] %s.\n"
- "%s: %s: CS[%u] acquired.\n"
- "%s: %s: CS[%u] created.\n"
- "%s: %s: acl = %p, aclLength = %zu.\n"
- "%s: %s: called.\n"
- "%s: %s: cmd(%u) on CS[%u] -> err 0x%x (%d).\n"
- "%s: %s: cmd(%u) on CS[%u] -> ok.\n"
- "%s: %s: command = %u.\n"
- "%s: %s: constraintState = %p.\n"
- "%s: %s: context = %p.\n"
- "%s: %s: log level set to %d.\n"
- "%s: %s: maxGlobalCredentialAge = %u.\n"
- "%s: %s: mem: type=%s ptr=%p size=%u (total=%u raw=%u data=%u types=%u) %s:%d (%s).\n"
- "%s: %s: operation = %p, operationLength = %zu.\n"
- "%s: %s: parameters = %p, parameterCount = %u.\n"
- "%s: %s: requirePasscode = %p.\n"
- "%s: %s: returning, -> ctx = %p.\n"
- "%s: %s: returning, err = %ld, code=%u.\n"
- "%s: %s: returning, err = %ld, var=%u.\n"
- "%s: %s: returning, err = %ld.\n"
- "%s: %s: returning.\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/CommonUtil.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCallBlock.c"
- "/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibSerialization.c"
- "0123456789abcdef"
- "<data>"
- "ACM"
- "ACM not available"
- "ACMContextAddCredential"
- "ACMContextAddCredentialWithScope"
- "ACMContextContainsCredentialType"
- "ACMContextContainsCredentialTypeEx"
- "ACMContextContainsPassphraseCredentialWithPurpose"
- "ACMContextCreate"
- "ACMContextCreateWithExternalForm"
- "ACMContextCredentialGetProperty"
- "ACMContextDelete"
- "ACMContextGetData"
- "ACMContextGetDataEx"
- "ACMContextGetDataProperty"
- "ACMContextGetExternalForm"
- "ACMContextGetInfo"
- "ACMContextRemoveCredentialsByType"
- "ACMContextRemoveCredentialsByTypeAndScope"
- "ACMContextRemoveCredentialsByValue"
- "ACMContextRemoveCredentialsByValueAndScope"
- "ACMContextRemovePassphraseCredentialsByPurposeAndScope"
- "ACMContextReplacePassphraseCredentialsWithScope"
- "ACMContextSetData"
- "ACMContextSetDataEx"
- "ACMContextVerifyPolicy"
- "ACMContextVerifyPolicyEx"
- "ACMContextVerifyPolicyWithPreflight"
- "ACMCredential"
- "ACMCredential - ACMCredentialDataAP"
- "ACMCredential - ACMCredentialDataBiometryMatchAttempted"
- "ACMCredential - ACMCredentialDataBiometryMatched"
- "ACMCredential - ACMCredentialDataContinuityUnlock"
- "ACMCredential - ACMCredentialDataKextDenyList"
- "ACMCredential - ACMCredentialDataPasscodeValidated"
- "ACMCredential - ACMCredentialDataPasscodeValidated2"
- "ACMCredential - ACMCredentialDataPassphraseEntered"
- "ACMCredential - ACMCredentialDataPassphraseExtractable"
- "ACMCredential - ACMCredentialDataSecureIntent"
- "ACMCredential - ACMCredentialDataSignature"
- "ACMCredential - ACMCredentialDataUserOutputDisplayed"
- "ACMCredentialGetProperty"
- "ACMGetAclAuthMethod"
- "ACMGetEnvironmentVariable"
- "ACMGlobalContextAddCredential"
- "ACMGlobalContextCredentialGetProperty"
- "ACMGlobalContextRemoveCredentialsByType"
- "ACMGlobalContextVerifyPolicy"
- "ACMHandleWithPayload"
- "ACMKernelControl"
- "ACMLib"
- "ACMParseAclAndCopyConstraintCharacteristics"
- "ACMRequirement"
- "ACMRequirement - ACMRequirementDataAP"
- "ACMRequirement - ACMRequirementDataAccessGroups"
- "ACMRequirement - ACMRequirementDataAnd"
- "ACMRequirement - ACMRequirementDataBiometryMatchAttempted"
- "ACMRequirement - ACMRequirementDataBiometryMatched"
- "ACMRequirement - ACMRequirementDataBiometryMatchedWithAttributes"
- "ACMRequirement - ACMRequirementDataKeyRef"
- "ACMRequirement - ACMRequirementDataKofN"
- "ACMRequirement - ACMRequirementDataKofNWithAttributes"
- "ACMRequirement - ACMRequirementDataOr"
- "ACMRequirement - ACMRequirementDataPasscodeValidated"
- "ACMRequirement - ACMRequirementDataPasscodeValidatedWithAttributes"
- "ACMRequirement - ACMRequirementDataPassphraseEntered"
- "ACMRequirement - ACMRequirementDataPushButtonWithAttributes"
- "ACMRequirement - ACMRequirementDataRatchet"
- "ACMRequirement - ACMRequirementDataSecureIntent"
- "ACMRequirement - ACMRequirementDataSecureStateWithAttributes"
- "ACMRequirement - ACMRequirementDataUserOutputDisplayed"
- "ACMRequirementGetProperties"
- "ACMRequirementGetProperty"
- "ACMRequirementGetSubrequirements"
- "ACMSetEnvironmentVariable"
- "ACMSetEnvironmentVariableWithAccessPolicy"
- "AppleCredentialManager"
- "CommonUtil.c"
- "Configuriation for: %{public}@"
- "DeallocCredentialList"
- "DeserializeCredentialList"
- "DeserializeProcessAcl"
- "DeserializeVerifyAclConstraint"
- "DeserializeVerifyPolicy"
- "Failed to clear PIN"
- "Failed to retrieve system key"
- "Failed to seal encryption key"
- "Failed to set system key"
- "LibCall.c"
- "LibCall_ACMContexAddCredentialWithScope"
- "LibCall_ACMContexRemoveCredentialsByTypeAndScope"
- "LibCall_ACMContextCreate"
- "LibCall_ACMContextCreateWithExternalForm"
- "LibCall_ACMContextCredentialGetProperty"
- "LibCall_ACMContextDelete"
- "LibCall_ACMContextGetData"
- "LibCall_ACMContextGetInfo"
- "LibCall_ACMContextLoadFromImage"
- "LibCall_ACMContextRemoveCredentialsByValueAndScope"
- "LibCall_ACMContextSetData"
- "LibCall_ACMContextUnloadToImage"
- "LibCall_ACMContextUnloadToImage_Block"
- "LibCall_ACMContextVerifyPolicyAndCopyRequirementEx"
- "LibCall_ACMContextVerifyPolicyEx"
- "LibCall_ACMContextVerifyPolicyEx_Block"
- "LibCall_ACMContextVerifyPolicyWithPreflight_Block"
- "LibCall_ACMGetAclAuthMethod_Block"
- "LibCall_ACMGetEnvironmentVariable"
- "LibCall_ACMGetEnvironmentVariable_Block"
- "LibCall_ACMGlobalContextCredentialGetProperty"
- "LibCall_ACMGlobalContextCredentialGetProperty_Block"
- "LibCall_ACMGlobalContextVerifyPolicyEx"
- "LibCall_ACMGlobalContextVerifyPolicy_Block"
- "LibCall_ACMKernDoubleClickNotify"
- "LibCall_ACMKernelControl"
- "LibCall_ACMKernelControl_Block"
- "LibCall_ACMPing"
- "LibCall_ACMPublishTrustedAccessories"
- "LibCall_ACMRequirementDelete"
- "LibCall_ACMSEPControl"
- "LibCall_ACMSEPControl_Block"
- "LibCall_ACMSecContextGetUnlockSecret"
- "LibCall_ACMSecContextVerifyAclConstraintAndCopyRequirement"
- "LibCall_ACMSecCredentialProviderEnrollmentStateChangedForUser"
- "LibCall_ACMSecSetBiometryAvailability"
- "LibCall_ACMSecSetBuiltinBiometry"
- "LibCall_ACMSetEnvironmentVariable"
- "LibCall_ACMTRMLoadState"
- "LibCall_ACMTRMLoadState_Block"
- "LibCall_ACMTRMSaveState"
- "LibCall_BuildCommand"
- "Missing system key"
- "NULL"
- "POACMHelper"
- "T@\"NSString\",&,N,V_apv"
- "T@\"NSString\",&,N,V_encryptionContext"
- "T@\"NSString\",&,N,V_refreshToken"
- "T@\"NSString\",&,N,V_requestIdentifier"
- "T@\"NSString\",&,N,V_scope"
- "T@\"NSString\",&,N,V_serverNonce"
- "T@\"NSString\",&,N,V_tokenTypeNamespace"
- "T@\"NSString\",&,N,V_wsTrustFederationNonce"
- "T@\"NSURL\",&,N,V_wsTrustFederationMexURL"
- "T@\"NSURL\",&,N,V_wsTrustFederationURL"
- "Util_AllocCredential"
- "Util_AllocRequirement"
- "Util_CreateRequirement"
- "Util_DeallocCredential"
- "Util_DeallocRequirement"
- "Util_ReadFromBuffer"
- "Util_SafeDeallocParameters"
- "Util_WriteToBuffer"
- "Util_hexDumpToStrHelper"
- "aclRequiresPasscodeInternal"
- "acm_mem_alloc_info"
- "acm_mem_free_info"
- "aks_backup_enable_volume"
- "aks_change_secret_epilogue"
- "aks_change_secret_opts"
- "aks_recover_with_escrow_bag"
- "aks_se_get_reset_token_for_memento_secret"
- "aks_set_configuration"
- "aks_set_system_with_passcode"
- "aks_unlock_bag"
- "aks_unlock_with_sync_bag"
- "array of ACMCredentialRef"
- "array of ACMParameter"
- "clearSmartCardPIN"
- "commandCursor == commandBuffer + sizeof(commandBuffer)"
- "createPlatformSSOSystemKey:"
- "deleted"
- "der_key_validate"
- "deserializeParameters"
- "destroyed"
- "dst || !dstCapacity"
- "extractGroupsAndSubUsingAuthorizationWithContext:tokens:returningGroups:identifier:refreshToken:"
- "failed to open connection to %s\n"
- "getLengthOfParameters"
- "initWithBytes:length:"
- "ioKitTransport"
- "performCommand"
- "platformSSOSystemKey"
- "processAclCommandInternal"
- "processAclInternal"
- "serializeParameters"
- "src || !srcLen"
- "updateLogLevelFromKext"
- "v24@?0r^v8Q16"
- "verifyAclConstraintForOperationCommandInternal"
- "verifyAclConstraintInternal"

```
