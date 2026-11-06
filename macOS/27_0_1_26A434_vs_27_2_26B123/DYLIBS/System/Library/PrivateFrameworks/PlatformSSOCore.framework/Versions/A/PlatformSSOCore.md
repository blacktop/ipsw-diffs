## PlatformSSOCore

> `/System/Library/PrivateFrameworks/PlatformSSOCore.framework/Versions/A/PlatformSSOCore`

```diff

-643.1.2.0.0
-  __TEXT.__text: 0x101878
-  __TEXT.__objc_methlist: 0x71d0
-  __TEXT.__const: 0x33d8
-  __TEXT.__cstring: 0xf5f7
-  __TEXT.__oslogstring: 0x6293
-  __TEXT.__gcc_except_tab: 0x114c
+643.40.34.0.0
+  __TEXT.__text: 0x107bfc
+  __TEXT.__objc_methlist: 0x7468
+  __TEXT.__const: 0x3540
+  __TEXT.__cstring: 0xfd67
+  __TEXT.__oslogstring: 0x719c
+  __TEXT.__ustring: 0x2c
+  __TEXT.__gcc_except_tab: 0x1144
   __TEXT.__dlopen_cstrs: 0x363
-  __TEXT.__swift5_typeref: 0x66e
-  __TEXT.__constg_swiftt: 0xbb8
-  __TEXT.__swift5_reflstr: 0x92a
-  __TEXT.__swift5_fieldmd: 0x9a4
-  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_typeref: 0x694
+  __TEXT.__constg_swiftt: 0xc04
+  __TEXT.__swift5_reflstr: 0x98a
+  __TEXT.__swift5_fieldmd: 0x9f0
+  __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0xb4
-  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0xd0
   __TEXT.__swift_as_cont: 0x118
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x3578
-  __TEXT.__eh_frame: 0x2088
+  __TEXT.__swift5_mpenum: 0x48
+  __TEXT.__unwind_info: 0x3678
+  __TEXT.__eh_frame: 0x2100
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f90
-  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__const: 0x1fb0
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3720
+  __DATA_CONST.__objc_selrefs: 0x3930
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x230
-  __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xb60
-  __AUTH_CONST.__const: 0x2df8
-  __AUTH_CONST.__cfstring: 0x8b80
-  __AUTH_CONST.__objc_const: 0x17928
-  __AUTH_CONST.__objc_intobj: 0x270
+  __DATA_CONST.__objc_superrefs: 0x238
+  __DATA_CONST.__objc_arraydata: 0x130
+  __DATA_CONST.__got: 0xba0
+  __AUTH_CONST.__const: 0x2f78
+  __AUTH_CONST.__cfstring: 0x9160
+  __AUTH_CONST.__objc_const: 0x17c70
+  __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x60
-  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0x1078
-  __AUTH_CONST.__auth_ptr: 0x2b8
-  __AUTH.__objc_data: 0x3438
-  __AUTH.__data: 0x928
-  __DATA.__objc_ivar: 0x704
-  __DATA.__data: 0x14e8
-  __DATA.__bss: 0x1760
+  __AUTH_CONST.__auth_got: 0x10c0
+  __AUTH_CONST.__auth_ptr: 0x2c0
+  __AUTH.__objc_data: 0x34d8
+  __AUTH.__data: 0x958
+  __DATA.__objc_ivar: 0x728
+  __DATA.__data: 0x1528
+  __DATA.__bss: 0x17d0
   __DATA.__common: 0x89
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x140

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5700
-  Symbols:   8785
-  CStrings:  2646
+  Functions: 5815
+  Symbols:   8973
+  CStrings:  2753
 
Symbols:
+ +[POBaseSystemSupport backoffStateForUser:domains:counters:]
+ +[POBaseSystemSupport dataVolumeDevicePath]
+ +[POConstantCoreUtil validatedAdditionalHTTPHeaders:]
+ +[POCoreConfigurationUtil accountDisplayNameForDeviceConfiguration:loginConfiguration:]
+ +[POCoreConfigurationUtil alwaysUseLoginUIOverride]
+ +[POCoreConfigurationUtil shouldUsePlatformSSOLoginUIForDeviceConfiguration:]
+ +[POKeychainAccess isRunningInTestProcess]
+ -[POAuthenticationProcess addAdditionalHTTPHeadersToRequest:context:]
+ -[PODeviceConfiguration additionalHTTPHeaders]
+ -[PODeviceConfiguration alwaysUseLoginUI]
+ -[PODeviceConfiguration requiresPlatformSSOLoginUI]
+ -[PODeviceConfiguration setAdditionalHTTPHeaders:]
+ -[PODeviceConfiguration setAlwaysUseLoginUI:]
+ -[PODeviceConfiguration supportsOpenID]
+ -[POKeyBag loadKeybagForUserId:]
+ -[POKeybagBindingInfo .cxx_destruct]
+ -[POKeybagBindingInfo bindingProtocol]
+ -[POKeybagBindingInfo flags]
+ -[POKeybagBindingInfo matchesPublicKeyOfCertificate:]
+ -[POKeybagBindingInfo needsPairing]
+ -[POKeybagBindingInfo pairingQueryAvailable]
+ -[POKeybagBindingInfo registeredPublicKeyHash]
+ -[POKeybagBindingInfo registeredTokenIds]
+ -[POKeybagBindingInfo setBindingProtocol:]
+ -[POKeybagBindingInfo setFlags:]
+ -[POKeybagBindingInfo setNeedsPairing:]
+ -[POKeybagBindingInfo setPairingQueryAvailable:]
+ -[POKeybagBindingInfo setRegisteredPublicKeyHash:]
+ -[POKeybagBindingInfo setRegisteredTokenIds:]
+ -[POKeybagBindingInfo setTokenInfoStatus:]
+ -[POKeybagBindingInfo tokenInfoStatus]
+ -[POKeychainAccess addSecureTokenForUserName:password:tokenId:wrapPublicKeyHash:]
+ -[POKeychainAccess changeLoginKeychainPassword:newPassword:]
+ -[POKeychainAccess eraseUnlockKeyWithPublicKeyHash:]
+ -[POKeychainAccess loginKeychainForUserName:password:]
+ -[POKeychainAccess readSecureTokenDataForUserName:tokenId:pin:]
+ -[POKeychainAccess removeSecureTokenForUserName:]
+ -[POKeychainAccess resetLoginKeychainWithPassword:resetSearchList:]
+ -[POKeychainAccess secureTokenStatusForUserName:needed:valid:]
+ -[POKeychainHelper .cxx_destruct]
+ -[POKeychainHelper init]
+ -[POKeychainHelper keychainAccess]
+ -[POKeychainHelper setKeychainAccess:]
+ -[POLoginProcessBase biometricPolicyIsUnsatisfied:]
+ -[POLoginProcessBase hasVerifiedBiometricContext]
+ -[POLoginProcessBase isNewAccountPendingRegistration]
+ -[POLoginProcessBase isUserCreatedDuringSetupAssistant]
+ -[POLoginProcessBase isWithinAuthenticationGracePeriod:]
+ -[POTokenHelper fileVaultNeedsPairingForUid:]
+ -[POTokenHelper findInfoForTokenId:uid:]
+ -[POTokenHelper keybagBindingInfoForTokenId:uid:]
+ -[POTokenHelper keybagNeedsPairingForTokenId:uid:]
+ -[POTokenHelper keybagRotatingKeyPresentForUserName:pubKeyHash:]
+ -[POTokenHelper pairKeybagWithTokenId:pubKeyHash:pin:userPassword:uid:]
+ GCC_except_table11
+ GCC_except_table140
+ GCC_except_table165
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table42
+ GCC_except_table62
+ OBJC_IVAR_$_PODeviceConfiguration._additionalHTTPHeaders
+ OBJC_IVAR_$_PODeviceConfiguration._alwaysUseLoginUI
+ OBJC_IVAR_$_POKeybagBindingInfo._bindingProtocol
+ OBJC_IVAR_$_POKeybagBindingInfo._flags
+ OBJC_IVAR_$_POKeybagBindingInfo._needsPairing
+ OBJC_IVAR_$_POKeybagBindingInfo._pairingQueryAvailable
+ OBJC_IVAR_$_POKeybagBindingInfo._registeredPublicKeyHash
+ OBJC_IVAR_$_POKeybagBindingInfo._registeredTokenIds
+ OBJC_IVAR_$_POKeybagBindingInfo._tokenInfoStatus
+ OBJC_IVAR_$_POKeychainHelper._keychainAccess
+ POIsReservedHTTPHeaderField.onceToken
+ POIsReservedHTTPHeaderField.reservedFields
+ POIsValidHTTPHeaderFieldName.illegalFieldCharacters
+ POIsValidHTTPHeaderFieldName.onceToken
+ POIsValidHTTPHeaderFieldValue.illegalValueCharacters
+ POIsValidHTTPHeaderFieldValue.onceToken
+ PO_LOG_POConstantCoreUtil
+ PO_LOG_POConstantCoreUtil.log
+ PO_LOG_POConstantCoreUtil.once
+ PO_LOG_POKeychainAccess
+ PO_LOG_POKeychainAccess.log
+ PO_LOG_POKeychainAccess.once
+ _NSClassFromString
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_POKeybagBindingInfo
+ _OBJC_CLASS_$_POKeychainAccess
+ _OBJC_CLASS_$_TKCTKDConnection
+ _OBJC_METACLASS_$_POKeybagBindingInfo
+ _OBJC_METACLASS_$_POKeychainAccess
+ _PO_LOG_POConstantCoreUtil
+ _PO_LOG_POKeychainAccess
+ _SecKeychainChangePassword
+ _SecKeychainCopyLogin
+ _SecKeychainEraseUnlockKeyWithPubKeyHash
+ _SecKeychainResetLogin
+ __32-[POKeyBag loadKeybagForUserId:]_block_invoke
+ __48-[PODeviceConfiguration setDeviceEncryptionKey:]_block_invoke
+ __53+[POConstantCoreUtil validatedAdditionalHTTPHeaders:]_block_invoke
+ __60-[POKeychainAccess changeLoginKeychainPassword:newPassword:]_block_invoke
+ __69-[POAuthenticationProcess addAdditionalHTTPHeadersToRequest:context:]_block_invoke
+ __71-[POTokenHelper pairKeybagWithTokenId:pubKeyHash:pin:userPassword:uid:]_block_invoke
+ __OBJC_$_CLASS_METHODS_POKeychainAccess
+ __OBJC_$_CLASS_PROP_LIST_POKeychainAccess
+ __OBJC_$_INSTANCE_METHODS_POKeybagBindingInfo
+ __OBJC_$_INSTANCE_METHODS_POKeychainAccess
+ __OBJC_$_INSTANCE_VARIABLES_POKeybagBindingInfo
+ __OBJC_$_INSTANCE_VARIABLES_POKeychainHelper
+ __OBJC_$_PROP_LIST_POKeybagBindingInfo
+ __OBJC_$_PROP_LIST_POKeychainHelper
+ __OBJC_CLASS_RO_$_POKeybagBindingInfo
+ __OBJC_CLASS_RO_$_POKeychainAccess
+ __OBJC_METACLASS_RO_$_POKeybagBindingInfo
+ __OBJC_METACLASS_RO_$_POKeychainAccess
+ ___32-[POKeyBag loadKeybagForUserId:]_block_invoke
+ ___42+[POKeychainAccess isRunningInTestProcess]_block_invoke
+ ___53+[POConstantCoreUtil validatedAdditionalHTTPHeaders:]_block_invoke
+ ___60-[POKeychainAccess changeLoginKeychainPassword:newPassword:]_block_invoke
+ ___69-[POAuthenticationProcess addAdditionalHTTPHeadersToRequest:context:]_block_invoke
+ ___71-[POTokenHelper pairKeybagWithTokenId:pubKeyHash:pin:userPassword:uid:]_block_invoke
+ ___POAdditionalHTTPHeadersForDisplay_block_invoke
+ ___POIsReservedHTTPHeaderField_block_invoke
+ ___POIsValidHTTPHeaderFieldName_block_invoke
+ ___POIsValidHTTPHeaderFieldValue_block_invoke
+ ___PO_LOG_POConstantCoreUtil_block_invoke
+ ___PO_LOG_POKeychainAccess_block_invoke
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSString"16^B24l
+ ___der_key_state_abs_last_mesa_auth
+ ___der_key_state_abs_last_mesa_unlock
+ ___der_key_state_abs_last_passcode_auth
+ ___der_key_state_abs_last_passcode_unlock
+ ___der_key_state_abs_lock_time
+ __os_log_fault_impl
+ _der_key_state_abs_last_mesa_auth
+ _der_key_state_abs_last_mesa_unlock
+ _der_key_state_abs_last_passcode_auth
+ _der_key_state_abs_last_passcode_unlock
+ _der_key_state_abs_lock_time
+ _get_enum_tag_for_layout_string 15PlatformSSOCore10POHintTypeO7ContextO
+ _kPOErrorDomain
+ _objc_msgSend$accountDisplayNameForDeviceConfiguration:loginConfiguration:
+ _objc_msgSend$addAdditionalHTTPHeadersToRequest:context:
+ _objc_msgSend$additionalHTTPHeaders
+ _objc_msgSend$alwaysUseLoginUI
+ _objc_msgSend$alwaysUseLoginUIOverride
+ _objc_msgSend$backoffStateForUser:domains:counters:
+ _objc_msgSend$biometricIsRequired
+ _objc_msgSend$characterSetWithRange:
+ _objc_msgSend$countForObject:
+ _objc_msgSend$dataVolumeDevicePath
+ _objc_msgSend$driverConfigurationsWithCTKDConnection:
+ _objc_msgSend$environment
+ _objc_msgSend$fileVaultNeedsPairing:
+ _objc_msgSend$findInfoForTokenId:uid:
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$getTokenInfo:tokenID:flags:pubKeyHash:
+ _objc_msgSend$hasVerifiedBiometricContext
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isLAAuth
+ _objc_msgSend$isNewAccountPendingRegistration
+ _objc_msgSend$isRunningInTestProcess
+ _objc_msgSend$isUserCreatedDuringSetupAssistant
+ _objc_msgSend$isWithinAuthenticationGracePeriod:
+ _objc_msgSend$keybagNeedsPairing:tokenID:
+ _objc_msgSend$keybagRotatingKey:
+ _objc_msgSend$keychainAccess
+ _objc_msgSend$lengthOfBytesUsingEncoding:
+ _objc_msgSend$listTokens:
+ _objc_msgSend$loadKeybagForUserId:
+ _objc_msgSend$loginKeychainForUserName:password:
+ _objc_msgSend$needsPairing
+ _objc_msgSend$pairKeybag:loginContext:
+ _objc_msgSend$pairingQueryAvailable
+ _objc_msgSend$processInfo
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfComposedCharacterSequencesForRange:
+ _objc_msgSend$registeredPublicKeyHash
+ _objc_msgSend$registeredTokenIds
+ _objc_msgSend$requiresPlatformSSOLoginUI
+ _objc_msgSend$setBindingProtocol:
+ _objc_msgSend$setFlags:
+ _objc_msgSend$setNeedsPairing:
+ _objc_msgSend$setPairingQueryAvailable:
+ _objc_msgSend$setRegisteredPublicKeyHash:
+ _objc_msgSend$setRegisteredTokenIds:
+ _objc_msgSend$setTokenInfoStatus:
+ _objc_msgSend$setValue:forHTTPHeaderField:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$supportsOpenID
+ _objc_msgSend$tokenInfoStatus
+ _objc_msgSend$validatedAdditionalHTTPHeaders:
+ _objc_msgSend$valueForHTTPHeaderField:
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_opt_respondsToSelector
+ _symbolic Si5count_t
+ _symbolic _____ 15PlatformSSOCore37PODefaultBaseSystemAuthenticationFlowC16EmptyResultCause33_E0BB9AAF438611B3E2B311B84B5155B5LLO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg_ABt 10Foundation3URLV
+ dataVolumeDevicePath.cachedDevicePath
+ isRunningInTestProcess.isTest
+ isRunningInTestProcess.onceToken
- +[POBaseSystemSupport isUserInBackoff:timeRemaining:]
- -[POUserConfiguration newUser]
- GCC_except_table138
- GCC_except_table163
- GCC_except_table34
- GCC_except_table36
- GCC_except_table41
- GCC_except_table60
- OBJC_IVAR_$_POUserConfiguration._newUser
- ___swift_memcpy16_8
- _objc_msgSend$driverConfigurations
- _objc_msgSend$driverConfigurationsWithClient:
- _objc_msgSend$initWithTokenID:serverEndpoint:targetUID:
- _objc_msgSend$isUserInBackoff:timeRemaining:
CStrings:
+ " submission failed"
+ "!#$%&'*+-.^_`|~"
+ "%@…%@ (%@ characters)"
+ "%s IdP display name from the login configuration, the profile sets no AccountDisplayName on %@"
+ "%s Platform SSO login UI: %{public}@, alwaysUseLoginUI:%{public}@ openID:%{public}@ biometricRequired:%{public}@ loginType:%{public}@ on %@"
+ "%s Platform SSO login UI: always, set by local override on %@"
+ "%s no IdP display name in the device or login configuration on %@"
+ "%s tokenID = %{public}@ on %@"
+ "%s tokenId = %{public}@, uid = %{public}@ on %@"
+ "+[POBaseSystemSupport backoffStateForUser:domains:counters:]"
+ "+[POCoreConfigurationUtil accountDisplayNameForDeviceConfiguration:loginConfiguration:]"
+ "+[POCoreConfigurationUtil shouldUsePlatformSSOLoginUIForDeviceConfiguration:]"
+ "-[PODeviceConfiguration supportsOpenID]"
+ "-[POTokenHelper findInfoForTokenId:uid:]"
+ "-[POTokenHelper keybagBindingInfoForTokenId:uid:]"
+ "-[POTokenHelper keybagRotatingKeyPresentForUserName:pubKeyHash:]"
+ "-[POTokenHelper pairKeybagWithTokenId:pubKeyHash:pin:userPassword:uid:]"
+ "00000000-0000-0000-0000-"
+ "Added %{public}@ of %{public}@ additional HTTP headers to request: %{public}@"
+ "Additional HTTP header is already set on the request; not overwriting it."
+ "AdditionalHTTPHeaders entry is not a string pair; discarding it."
+ "AdditionalHTTPHeaders field collides with another entry that differs only in case; discarding all of them."
+ "AdditionalHTTPHeaders field is not a valid header name; discarding it."
+ "AdditionalHTTPHeaders field is reserved; discarding it."
+ "AdditionalHTTPHeaders is not a dictionary; ignoring it."
+ "AdditionalHTTPHeaders value is not a valid header value; discarding it."
+ "AlwaysUseLoginUI"
+ "Authentication flow: OpenID not configured or missing required values"
+ "Could not read the secure token data: %d %{public}@"
+ "CryptoTokenKit has no keybag pairing query; leaving the pairing state undetermined"
+ "Failed to copy the login keychain."
+ "Failed to pair the keybag for the user token."
+ "Headers: %@, Limit: %@"
+ "Invalid user identifier, cannot read backoff state"
+ "Keybag needs pairing for the user token: %{public}@"
+ "Keybag paired for the user token"
+ "Keybag password change failed for token %{public}@ (key hash %{public}@): %{public}d. Registered keybag tokens: %{public}@"
+ "Login Policy: %{public}@ requires a biometric factor that was not provided"
+ "Login Policy: biometric policy does not apply to AccessKey authentication"
+ "Login Policy: biometric policy does not apply to SmartCard authentication"
+ "Login Policy: biometric policy does not apply to an account pending registration"
+ "Login Policy: biometric policy does not apply to temporary session accounts"
+ "Login Policy: biometric requirement satisfied by LA authentication"
+ "Login Policy: does not have auth grace period"
+ "Login Policy: grace period expired"
+ "Login Policy: la authentication with an unusable externalized LAContext"
+ "Login Policy: la authentication with no externalized LAContext"
+ "Login Policy: registration incomplete and outside the authentication grace period"
+ "Login Policy: registration incomplete, within the authentication grace period"
+ "Login Policy: the account is pending registration, deferring to the local credential"
+ "Missing device encryption key."
+ "Missing temporary account credential."
+ "No authenticator result to route"
+ "No keybag rotating key in the login configuration for %{public}@"
+ "No login configuration for the user; treating the keybag rotating key as present"
+ "POConstantCoreUtil"
+ "POKeychainAccess"
+ "Refusing to change the login keychain password from a test process. Inject POKeychainAccessMock instead - running this would change the credential store of the machine running the test."
+ "Refusing to create a secure token from a test process. Inject POKeychainAccessMock instead - running this would change the credential store of the machine running the test."
+ "Refusing to erase the token unlock key from a test process. Inject POKeychainAccessMock instead - running this would change the credential store of the machine running the test."
+ "Refusing to remove a secure token from a test process. Inject POKeychainAccessMock instead - running this would change the credential store of the machine running the test."
+ "Refusing to reset the login keychain from a test process. Inject POKeychainAccessMock instead - running this would change the credential store of the machine running the test."
+ "Refusing to unlock or rekey the login keychain from a test process. Inject POKeychainAccessMock instead - running this would change the credential store of the machine running the test."
+ "Registered keybag tokens: %{public}@"
+ "Resetting the login keychain"
+ "TKLoginConfiguration"
+ "TKLoginConfiguration is unavailable; treating the keybag rotating key as present"
+ "Too many entries in AdditionalHTTPHeaders; ignoring all of them."
+ "Unable to decrypt temporary account credential with the outgoing key; dropping entry."
+ "Unable to get APFS record for %{public}@: %d (%{public}s)"
+ "Unable to resolve data volume for group %{public}@"
+ "User is %{public}s, %u of %u failed attempts, %us remaining (console %u attempts %us, other %u attempts %us)"
+ "User is not enrolled in xART policy, no backoff state"
+ "XCTestConfigurationFilePath"
+ "XCTestSessionIdentifier"
+ "accept"
+ "accept-encoding"
+ "authentication-info"
+ "authorization"
+ "connection"
+ "content-encoding"
+ "content-length"
+ "content-type"
+ "cookie"
+ "cookie2"
+ "credentialSubmitted: account has exhausted its unlock attempts"
+ "credentialSubmitted: account is in backoff, %{public}us remaining"
+ "expect"
+ "getLoginHints: backoff state unavailable, no lockout hint shown"
+ "host"
+ "in backoff"
+ "isRunningInTestProcess is true"
+ "keep-alive"
+ "no credential was submitted"
+ "not in backoff"
+ "not required"
+ "out of attempts"
+ "proxy-authenticate"
+ "proxy-authentication-info"
+ "proxy-authorization"
+ "required"
+ "resolveResult(%{public}s): nothing to route, %{public}s"
+ "set-cookie"
+ "set-cookie2"
+ "soapaction"
+ "te"
+ "the flow was cancelled"
+ "trailer"
+ "transfer-encoding"
+ "upgrade"
+ "www-authenticate"
+ "xART policy is missing, cannot determine backoff state"
+ "xART policy is not enforced, no backoff applies"
- "+[POBaseSystemSupport isUserInBackoff:timeRemaining:]"
- "-[POTokenHelper findInfoForTokenId:]"
- "Unable to get APFS record: %08x"
- "User has to many failed attempts"
- "User is in backoff"
- "User is not in backoff"
```
