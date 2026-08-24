## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Versions/A/PlatformSSO`

```diff

-643.0.33.0.0
-  __TEXT.__text: 0x11570c
-  __TEXT.__objc_methlist: 0x47cc
-  __TEXT.__const: 0x2140
-  __TEXT.__gcc_except_tab: 0x1fe8
-  __TEXT.__cstring: 0xe59f
-  __TEXT.__oslogstring: 0x9878
+643.1.1.0.0
+  __TEXT.__text: 0x11ed7c
+  __TEXT.__objc_methlist: 0x481c
+  __TEXT.__const: 0x2180
+  __TEXT.__gcc_except_tab: 0x206c
+  __TEXT.__cstring: 0xea84
+  __TEXT.__oslogstring: 0xaa08
   __TEXT.__dlopen_cstrs: 0x42d
-  __TEXT.__swift5_typeref: 0x6bc
+  __TEXT.__swift5_typeref: 0x6ca
   __TEXT.__swift5_fieldmd: 0x8bc
   __TEXT.__constg_swiftt: 0xbc8
   __TEXT.__swift5_reflstr: 0x8da

   __TEXT.__swift5_types: 0x6c
   __TEXT.__swift_as_entry: 0x2c0
   __TEXT.__swift_as_ret: 0x2b8
-  __TEXT.__swift_as_cont: 0x2a0
+  __TEXT.__swift_as_cont: 0x2a4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x270
+  __TEXT.__swift5_capture: 0x280
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x31a8
-  __TEXT.__eh_frame: 0x4088
+  __TEXT.__unwind_info: 0x3250
+  __TEXT.__eh_frame: 0x4278
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3368
+  __DATA_CONST.__objc_selrefs: 0x3398
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe8
   __DATA_CONST.__objc_arraydata: 0xa0
-  __DATA_CONST.__got: 0x998
-  __AUTH_CONST.__const: 0x2d10
-  __AUTH_CONST.__cfstring: 0x62a0
+  __DATA_CONST.__got: 0x9b0
+  __AUTH_CONST.__const: 0x2d90
+  __AUTH_CONST.__cfstring: 0x6480
   __AUTH_CONST.__objc_const: 0xa9e8
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xca0
+  __AUTH_CONST.__auth_got: 0xcd0
   __AUTH.__objc_data: 0x960
   __AUTH.__data: 0xeb8
   __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x7b0
-  __DATA.__bss: 0xea8
+  __DATA.__data: 0x7d0
+  __DATA.__bss: 0xec8
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x130

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4219
-  Symbols:   5601
-  CStrings:  2134
+  Functions: 4262
+  Symbols:   5637
+  CStrings:  2210
 
Symbols:
+ -[POAgentProcess flagUserForBinding:configurationManager:reason:]
+ -[POConfigurationManager platformSSOSecureTokenNeedsResetForUser:]
+ -[POConfigurationManager resetPlatformSSOSecureTokenForUser:password:wrapHash:error:]
+ -[PODaemonProcess _localUserNameForUniqueIdentifier:]
+ -[PODaemonProcess _removePlatformSSOSecureTokenBeforeRemovingConfigurationForIdentifier:]
+ -[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]
+ -[PORegistrationManager dealloc]
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table148
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table175
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table210
+ GCC_except_table213
+ GCC_except_table225
+ GCC_except_table235
+ GCC_except_table268
+ GCC_except_table276
+ GCC_except_table277
+ GCC_except_table88
+ GCC_except_table94
+ __57-[PORegistrationManager resetRegistrationWithCompletion:]_block_invoke
+ __60-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]_block_invoke
+ __65-[POAgentProcess flagUserForBinding:configurationManager:reason:]_block_invoke
+ __85-[POConfigurationManager resetPlatformSSOSecureTokenForUser:password:wrapHash:error:]_block_invoke
+ __89-[PODaemonProcess _removePlatformSSOSecureTokenBeforeRemovingConfigurationForIdentifier:]_block_invoke_2
+ ___60-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]_block_invoke
+ ___65-[POAgentProcess flagUserForBinding:configurationManager:reason:]_block_invoke
+ ___85-[POConfigurationManager resetPlatformSSOSecureTokenForUser:password:wrapHash:error:]_block_invoke
+ ___89-[PODaemonProcess _removePlatformSSOSecureTokenBeforeRemovingConfigurationForIdentifier:]_block_invoke
+ ___89-[PODaemonProcess _removePlatformSSOSecureTokenBeforeRemovingConfigurationForIdentifier:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b56r
+ ___swift__destructor
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ _dispatch_after
+ _objc_msgSend$_localUserNameForUniqueIdentifier:
+ _objc_msgSend$_removePlatformSSOSecureTokenBeforeRemovingConfigurationForIdentifier:
+ _objc_msgSend$flagUserForBinding:configurationManager:reason:
+ _objc_msgSend$platformSSOSecureTokenNeedsResetForUser:
+ _objc_msgSend$resetPlatformSSOSecureTokenForUser:password:wrapHash:error:
+ _objc_msgSend$unbindTokenForUsername:hash:returningError:
+ _objc_msgSend$verifyOwnSecureTokenPassword:forUser:
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic SaySSG
+ _symbolic Sccy___________pG So13POLoginResultV s5ErrorP
+ _symbolic So6NSDataCSg
- GCC_except_table113
- GCC_except_table123
- GCC_except_table125
- GCC_except_table127
- GCC_except_table129
- GCC_except_table131
- GCC_except_table133
- GCC_except_table135
- GCC_except_table143
- GCC_except_table151
- GCC_except_table160
- GCC_except_table162
- GCC_except_table170
- GCC_except_table171
- GCC_except_table177
- GCC_except_table183
- GCC_except_table190
- GCC_except_table191
- GCC_except_table197
- GCC_except_table200
- GCC_except_table206
- GCC_except_table208
- GCC_except_table221
- GCC_except_table231
- GCC_except_table264
- GCC_except_table272
- GCC_except_table273
- GCC_except_table87
- GCC_except_table96
- _symbolic Sccy____________pt_____G So13POLoginResultV s5ErrorP s5NeverO
CStrings:
+ "-[POConfigurationManager platformSSOSecureTokenNeedsResetForUser:]"
+ "-[POConfigurationManager resetPlatformSSOSecureTokenForUser:password:wrapHash:error:]"
+ "-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]"
+ "Account's own secure token is not in sync after the token change; repairing with the bootstrap token"
+ "Authentication flow: Password change failed - %s"
+ "Authentication flow: Password change failed with result %{public}s"
+ "Authentication flow: Performing Platform SSO Biometric Login"
+ "Authentication flow: Performing Platform SSO Password Login, sessionType=%{public}s"
+ "Authentication flow: routing to FileVault token unlock, sessionType=%{public}s, user=%{private,mask.hash}s"
+ "Authentication flow: routing to admin unlock, sessionType=%{public}s, user=%{private,mask.hash}s"
+ "Authentication flow: routing to temporary session unlock, sessionType=%{public}s, user=%{private,mask.hash}s"
+ "Authentication flow: routing to user SEP key auth, sessionType=%{public}s, user=%{private,mask.hash}s"
+ "Biometric auth credential is missing"
+ "Could not read PlatformSSO secure token status: %d"
+ "Could not resolve GUID for user."
+ "Could not resolve local user for identifier %{public}@; leaving Platform SSO secure token bound."
+ "Error removing user picture path."
+ "Failed to recreate PlatformSSO secure token."
+ "Failed to remove Platform SSO secure token before configuration removal."
+ "Failed to reset PlatformSSO secure token during binding."
+ "Failed to reset profile picture for temporary user."
+ "Failed to save user configuration after deferring token binding."
+ "Failed to save user configuration while flagging for binding repair."
+ "Failed to unbind previous CTK token identity after key rotation."
+ "Flagging user for binding repair: %{public}s"
+ "Flagging user for binding repair; keybag may be ahead of the volume key."
+ "Login Policy: Login Result = %{public}s"
+ "Login Policy: denied, reason=authenticationNotAllowed, auth grace period expired"
+ "Login Policy: denied, reason=authenticationNotAllowed, no auth grace period"
+ "Missing parameters for secure token reset."
+ "Missing token id for secure token reset."
+ "New password does not authenticate the local account after SecureToken update; keybag and volume key may be diverged."
+ "Own secure token did not accept the password."
+ "PlatformSSO secure token KEK is needed but invalid; reset required for user %{public}@"
+ "PlatformSSO secure token reset (removed and recreated) for user %{public}@"
+ "Refusing to bind token: credential does not match the local account password."
+ "Removing PlatformSSO secure token returned %d (continuing to recreate)"
+ "Removing additional Platform SSO secure token before removing configuration: identifier = %{public}@, tokenId = %{public}@"
+ "SecureToken update failed after keybag was changed"
+ "attemptIdPAuthentication: Login result = %{public}s"
+ "attemptIdPAuthentication: reason=offline, offline grace period not allowed"
+ "attemptPSSOV1IdPAuthentication: Login result = %{public}s"
+ "authenticateTemporaryOpenIDUser: result=%{public}s"
+ "authenticateTemporaryPasswordUser: result=%{public}s"
+ "cancel(%{public}s)"
+ "cancel: session=%{public}s"
+ "createAuthenticationFlow: session=%{public}s flow=embedded"
+ "createAuthenticationFlow: session=%{public}s flow=login"
+ "createAuthenticationFlow: session=%{public}s reason=unsupported"
+ "createNewOpenIDUser: result=%{public}s"
+ "createNewPasswordUser: Create user result = %{public}s"
+ "createNewPasswordUser: user created, user=%{private,mask.hash}s"
+ "credentialSubmitted(fallback, %{public}s): %{public}s"
+ "credentialSubmitted(primary, %{public}s): %{public}s"
+ "credentialSubmitted(secondary, %{public}s): %{public}s"
+ "credentialSubmitted: local account auth"
+ "credentialSubmitted: outcome=success"
+ "credentialSubmitted: outcome=success session=%{public}s tokensReturned=%{bool,public}d"
+ "credentialSubmitted: path=%{public}s"
+ "credentialSubmitted: reason=invalidCredentials"
+ "credentialSubmitted: result=%{public}s"
+ "credentialSubmitted: session=%{public}s elevation=%{bool,public}d"
+ "credentialSubmitted: session=%{public}s result=%{public}s"
+ "credentialSubmitted: session=%{public}s runScope=%{public}s"
+ "failed to encode token data for admin unlock"
+ "failed to encode token data for secure enclave key authentication"
+ "finish(%{public}s): overallResult=%{public}s"
+ "finish: flow outcome=failure, uid=%{public}u"
+ "finish: flow outcome=success, uid=%{public}u"
+ "finish: session=%{public}s"
+ "generateBaseSystemFlow: session=%{public}s reason=unsupported"
+ "generateFlow: session=%{public}s ready"
+ "handleAdminUnlockAuthentication: OD auth failed, reason=accountBackoff, code=%{public}ld"
+ "handleAdminUnlockAuthentication: OD auth failed, reason=accountDisabled, code=%{public}ld"
+ "handleAdminUnlockAuthentication: OD auth failed, reason=accountExpired, code=%{public}ld"
+ "handleAdminUnlockAuthentication: OD auth failed, reason=accountLockout, code=%{public}ld"
+ "handleAdminUnlockAuthentication: OD auth failed, reason=authenticationFailed, code=%{public}ld"
+ "handleAdminUnlockAuthentication: outcome=success, path=adminBuiltin, user=%{private,mask.hash}s"
+ "handleAuthenticationShouldBeAttempted: denied, reason=onlineAuthRequired"
+ "handleLocalPasswordAuthentication: OD auth failed, reason=accountBackoff, code=%{public}ld"
+ "handleLocalPasswordAuthentication: OD auth failed, reason=accountDisabled, code=%{public}ld"
+ "handleLocalPasswordAuthentication: OD auth failed, reason=accountExpired, code=%{public}ld"
+ "handleLocalPasswordAuthentication: OD auth failed, reason=accountLockout, code=%{public}ld"
+ "handleLocalPasswordAuthentication: OD auth failed, reason=authenticationFailed, code=%{public}ld"
+ "handleOfflineAuthenticationRequired: denied, reason=onlineAuthRequired, offline grace period not allowed"
+ "handleOfflineGracePeriod: denied, reason=onlineAuthRequired"
+ "handleOfflineGracePeriod: denied, reason=onlineAuthRequired, offline grace period expired"
+ "handleOpenIDAuthentication: result=%{public}s"
+ "handleSuccessfulElevationResponse: outcome=keybagVerified uid=%{public}u"
+ "handleSuccessfulElevationResponse: outcome=success user=%{private,mask.hash}s"
+ "handleSuccessfulResponse: keybag unlocked, type=password, uid=%{public}u"
+ "handleSuccessfulResponse: keybag unlocked, type=token, uid=%{public}u"
+ "handleSuccessfulResponse: keychain unlocked, type=password, uid=%{public}u"
+ "handleSuccessfulResponse: outcome=success, sessionType=%{public}s, path=newUserLogin, user=%{private,mask.hash}s"
+ "handleTokenAuthAfterBuiltInAuthenticate: routing to token auth after builtin failed, sessionType=%{public}s"
+ "handleUserSEPKeyUserAuthentication: OD auth failed, reason=accountBackoff, code=%{public}ld"
+ "handleUserSEPKeyUserAuthentication: OD auth failed, reason=accountDisabled, code=%{public}ld"
+ "handleUserSEPKeyUserAuthentication: OD auth failed, reason=accountExpired, code=%{public}ld"
+ "handleUserSEPKeyUserAuthentication: OD auth failed, reason=accountLockout, code=%{public}ld"
+ "handleUserSEPKeyUserAuthentication: OD auth failed, reason=authenticationFailed, code=%{public}ld"
+ "handleUserSEPKeyUserAuthentication: Unexpected error - %s"
+ "handleUserSEPKeyUserAuthentication: outcome=success, sessionType=%{public}s, path=sepKeyBuiltin, user=%{private,mask.hash}s"
+ "loadAuthenticators: session=%{public}s active=%{public}s primary=%{public}s secondary=%{public}s"
+ "local account credential did not verify after SecureToken update"
+ "password change committed ok"
+ "resolveResult: session=%{public}s outcome=primarySucceeded secondary=%{public}s"
+ "shouldRun: registration not completed"
+ "userNameEntered: result=%{public}s"
+ "userNameEntered: systemSession=true"
- "Authentication flow: Login Result = %s"
- "Authentication flow: Password change failed with unexpected result"
- "Authentication flow: Result = %s"
- "Authentication flow: User SEP key authentication detected for user %s"
- "Login Policy: Login Result = %s"
- "OpenID Authorization Request: Result = %s"
- "PODefaultAuthenticationFlow"
- "Password change failed"
- "attemptIdPAuthentication: Login result = %s"
- "attemptIdPAuthentication: Offline grace period not allowed, returning offline status"
- "attemptPSSOV1IdPAuthentication: Login result = %s"
- "authenticateTemporaryOpenIDUser: Authentication result = %s"
- "authenticateTemporaryPasswordUser: Authentication result = %s"
- "createNewOpenIDUser: Create user result = %s"
- "createNewPasswordUser: Create user result = %s"
- "failed to encode token data for user secure enclave key user"
- "handleAdminUnlockAuthentication: Account has expired %s"
- "handleAdminUnlockAuthentication: Account is disabled %s"
- "handleAdminUnlockAuthentication: Account is in backoff %s"
- "handleAdminUnlockAuthentication: Account is locked out %s"
- "handleAdminUnlockAuthentication: Invalid credentials for user %s"
- "handleAdminUnlockAuthentication: Successfully encoded SEP key context"
- "handleAdminUnlockAuthentication: Successfully encoded admin unlock context"
- "handleAuthenticationShouldBeAttempted: User state requires online authentication"
- "handleLocalPasswordAuthentication: Account has expired %s"
- "handleLocalPasswordAuthentication: Account is disabled %s"
- "handleLocalPasswordAuthentication: Account is in backoff %s"
- "handleLocalPasswordAuthentication: Account is locked out %s"
- "handleLocalPasswordAuthentication: Invalid credentials for user %s"
- "handleOfflineAuthenticationRequired: Offline grace period not allowed, requiring online auth"
- "handleOfflineGracePeriod: Grace period expired, requiring online authentication"
- "handleOfflineGracePeriod: User state requires online authentication"
- "handleTokenAuthAfterBuiltInAuthenticate: Built-in authentication failed, attempting token authentication"
```
