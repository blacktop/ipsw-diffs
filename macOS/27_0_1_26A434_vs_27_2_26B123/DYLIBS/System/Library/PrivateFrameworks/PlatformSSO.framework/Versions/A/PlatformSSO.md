## PlatformSSO

> `/System/Library/PrivateFrameworks/PlatformSSO.framework/Versions/A/PlatformSSO`

```diff

-643.1.2.0.0
-  __TEXT.__text: 0x11ed88
-  __TEXT.__objc_methlist: 0x481c
-  __TEXT.__const: 0x2180
-  __TEXT.__gcc_except_tab: 0x206c
-  __TEXT.__cstring: 0xea84
-  __TEXT.__oslogstring: 0xaa08
-  __TEXT.__dlopen_cstrs: 0x42d
-  __TEXT.__swift5_typeref: 0x6ca
-  __TEXT.__swift5_fieldmd: 0x8bc
-  __TEXT.__constg_swiftt: 0xbc8
-  __TEXT.__swift5_reflstr: 0x8da
+643.40.34.0.0
+  __TEXT.__text: 0x1289c0
+  __TEXT.__objc_methlist: 0x4ae4
+  __TEXT.__const: 0x2260
+  __TEXT.__gcc_except_tab: 0x2210
+  __TEXT.__cstring: 0xf564
+  __TEXT.__oslogstring: 0xbf76
+  __TEXT.__dlopen_cstrs: 0x47b
+  __TEXT.__swift5_typeref: 0x76e
+  __TEXT.__swift5_fieldmd: 0x934
+  __TEXT.__constg_swiftt: 0xc6c
+  __TEXT.__swift5_reflstr: 0x94a
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_protos: 0x20
-  __TEXT.__swift5_proto: 0x7c
-  __TEXT.__swift5_types: 0x6c
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__swift5_proto: 0x80
+  __TEXT.__swift5_types: 0x74
   __TEXT.__swift_as_entry: 0x2c0
-  __TEXT.__swift_as_ret: 0x2b8
-  __TEXT.__swift_as_cont: 0x2a4
+  __TEXT.__swift_as_ret: 0x2bc
+  __TEXT.__swift_as_cont: 0x2a8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x280
+  __TEXT.__swift5_capture: 0x27c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x3250
-  __TEXT.__eh_frame: 0x4278
+  __TEXT.__unwind_info: 0x3410
+  __TEXT.__eh_frame: 0x42b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5b8
-  __DATA_CONST.__objc_classlist: 0x178
+  __DATA_CONST.__const: 0x5d0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3398
+  __DATA_CONST.__objc_selrefs: 0x35a8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_arraydata: 0xa0
-  __DATA_CONST.__got: 0x9b0
-  __AUTH_CONST.__const: 0x2d90
-  __AUTH_CONST.__cfstring: 0x6480
-  __AUTH_CONST.__objc_const: 0xa9e8
+  __DATA_CONST.__got: 0x9f0
+  __AUTH_CONST.__const: 0x2ea8
+  __AUTH_CONST.__cfstring: 0x6820
+  __AUTH_CONST.__objc_const: 0xad80
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xcd0
+  __AUTH_CONST.__auth_got: 0xce8
   __AUTH_CONST.__auth_ptr: 0x248
-  __AUTH.__objc_data: 0x960
-  __AUTH.__data: 0xeb8
-  __DATA.__objc_ivar: 0x414
-  __DATA.__data: 0x7d0
-  __DATA.__bss: 0xec8
+  __AUTH.__objc_data: 0x9b0
+  __AUTH.__data: 0xf88
+  __DATA.__objc_ivar: 0x440
+  __DATA.__data: 0x7e0
+  __DATA.__bss: 0xef8
   __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x130

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4262
-  Symbols:   5637
-  CStrings:  2210
+  Functions: 4405
+  Symbols:   5837
+  CStrings:  2322
 
Symbols:
+ +[POSoftwareUpdateCredentialPolicy credentialsWanted]
+ +[POSoftwareUpdateCredentialPolicy harvestPassword:forUserId:]
+ -[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:error:]
+ -[POAgentAuthenticationProcess keychainAccess]
+ -[POAgentAuthenticationProcess postAuthenticationNotificationForEvaluationError:]
+ -[POAgentAuthenticationProcess repairKeybagRegistrationIfNeededWithPasswordContext:]
+ -[POAgentAuthenticationProcess requestUserRegistrationRepairIfNeeded]
+ -[POAgentAuthenticationProcess setKeychainAccess:]
+ -[POAgentAuthenticationProcess setUserRegistrationRepairLock:]
+ -[POAgentAuthenticationProcess setUserRegistrationRepairRequested:]
+ -[POAgentAuthenticationProcess shouldRunConfigurationChangeOnUnlock]
+ -[POAgentAuthenticationProcess userRegistrationRepairLock]
+ -[POAgentAuthenticationProcess userRegistrationRepairRequested]
+ -[POAgentProcess configurationManagerForUserName:]
+ -[POAgentProcess keychainAccess]
+ -[POAgentProcess repairTokenBindingForUser:passwordContextData:configurationManager:]
+ -[POAgentProcess setKeychainAccess:]
+ -[POAgentProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]
+ -[POAgentProcess updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]
+ -[POAuthPluginProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]
+ -[POConfigurationManager keychainAccess]
+ -[POConfigurationManager platformSSOSecureTokenNeedsResetForUser:pin:]
+ -[POConfigurationManager resetTempSessionAccount]
+ -[POConfigurationManager setKeychainAccess:]
+ -[POConfigurationManager verifyOwnSecureTokenPasswordForUser:passwordContext:error:]
+ -[PODaemonConnection resetTempSessionAccountWithCompletion:]
+ -[PODaemonConnection verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]
+ -[PODaemonProcess resetTempSessionAccountWithCompletion:]
+ -[PODaemonProcess verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]
+ -[PODirectoryServices .cxx_destruct]
+ -[PODirectoryServices init]
+ -[PODirectoryServices keychainAccess]
+ -[PODirectoryServices setKeychainAccess:]
+ -[PODirectoryServices verifyOwnSecureTokenPassword:forUser:error:]
+ -[POLoginProcess isCreatingNewUserForCurrentCredential]
+ -[POLoginProcess resolvedLocalUserName]
+ -[POProfile additionalHTTPHeaders]
+ -[POProfile alwaysUseLoginUI]
+ -[POProfile setAlwaysUseLoginUI:]
+ -[PORegistrationManager claimDeviceRegistrationStart]
+ -[PORegistrationManager claimRegistrationStartResumingUnfinishedDeviceRegistration:]
+ -[PORegistrationManager claimUserRegistrationStart]
+ -[PORegistrationManager publishRegistrationContext:claim:]
+ -[PORegistrationManager publishRegistrationContextWithState:claim:]
+ -[PORegistrationManager registrationContextLock]
+ -[PORegistrationManager registrationGeneration]
+ -[PORegistrationManager registrationIsInProgress]
+ -[PORegistrationManager registrationStarting]
+ -[PORegistrationManager releaseRegistrationStart:]
+ -[PORegistrationManager setRegistrationContextLock:]
+ -[PORegistrationManager setRegistrationGeneration:]
+ -[PORegistrationManager setRegistrationStarting:]
+ -[PORegistrationManager setUserAuthPluginProcess:]
+ -[PORegistrationManager storeCredentialContext:]
+ -[PORegistrationManager updatePasswordHint]
+ -[POServiceConnection updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]
+ -[POUnlockProcess denyUnlockForUnsatisfiedBiometricPolicy]
+ -[POUnlockProcess unlockKeybagWithTokenId:publicKeyHash:]
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table125
+ GCC_except_table14
+ GCC_except_table143
+ GCC_except_table144
+ GCC_except_table149
+ GCC_except_table150
+ GCC_except_table152
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table169
+ GCC_except_table171
+ GCC_except_table174
+ GCC_except_table18
+ GCC_except_table185
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table201
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table222
+ GCC_except_table237
+ GCC_except_table249
+ GCC_except_table283
+ GCC_except_table291
+ GCC_except_table292
+ GCC_except_table6
+ GCC_except_table60
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table66
+ GCC_except_table84
+ GCC_except_table91
+ GCC_except_table92
+ GCC_except_table97
+ OBJC_IVAR_$_POAgentAuthenticationProcess._keychainAccess
+ OBJC_IVAR_$_POAgentAuthenticationProcess._userRegistrationRepairLock
+ OBJC_IVAR_$_POAgentAuthenticationProcess._userRegistrationRepairRequested
+ OBJC_IVAR_$_POAgentProcess._keychainAccess
+ OBJC_IVAR_$_POConfigurationManager._keychainAccess
+ OBJC_IVAR_$_PODirectoryServices._keychainAccess
+ OBJC_IVAR_$_POProfile._additionalHTTPHeaders
+ OBJC_IVAR_$_POProfile._alwaysUseLoginUI
+ OBJC_IVAR_$_PORegistrationManager._registrationContextLock
+ OBJC_IVAR_$_PORegistrationManager._registrationGeneration
+ OBJC_IVAR_$_PORegistrationManager._registrationStarting
+ OSUpdateLibraryCore.frameworkLibrary
+ PO_LOG_POSoftwareUpdateCredentialPolicy
+ PO_LOG_POSoftwareUpdateCredentialPolicy.log
+ PO_LOG_POSoftwareUpdateCredentialPolicy.once
+ _CFNumberCreate
+ _CFNumberGetValue
+ _LAErrorDomain
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_POKeychainAccess
+ _OBJC_CLASS_$_POSoftwareUpdateCredentialPolicy
+ _OBJC_METACLASS_$_POSoftwareUpdateCredentialPolicy
+ _ODFrameworkErrorDomain
+ _POExtensionNormalizedTeamIdentifier
+ _PO_LOG_POSoftwareUpdateCredentialPolicy
+ __104-[POServiceConnection updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]_block_invoke
+ __43-[PORegistrationManager updatePasswordHint]_block_invoke
+ __48-[PORegistrationManager storeCredentialContext:]_block_invoke
+ __57-[POUnlockProcess unlockKeybagWithTokenId:publicKeyHash:]_block_invoke
+ __60-[PODaemonConnection resetTempSessionAccountWithCompletion:]_block_invoke
+ __66-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:error:]_block_invoke
+ __80-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:error:]_block_invoke
+ __80-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:error:]_block_invoke_2
+ __82-[PODaemonProcess verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]_block_invoke
+ __84-[POAgentAuthenticationProcess repairKeybagRegistrationIfNeededWithPasswordContext:]_block_invoke
+ __85-[POAgentProcess repairTokenBindingForUser:passwordContextData:configurationManager:]_block_invoke
+ __85-[PODaemonConnection verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]_block_invoke
+ __91-[POAgentProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]_block_invoke
+ __91-[POAgentProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]_block_invoke_2
+ __OBJC_$_CLASS_METHODS_POSoftwareUpdateCredentialPolicy
+ __OBJC_$_CLASS_PROP_LIST_POSoftwareUpdateCredentialPolicy
+ __OBJC_$_INSTANCE_VARIABLES_PODirectoryServices
+ __OBJC_CLASS_RO_$_POSoftwareUpdateCredentialPolicy
+ __OBJC_METACLASS_RO_$_POSoftwareUpdateCredentialPolicy
+ ___104-[POServiceConnection updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:]_block_invoke
+ ___43-[PORegistrationManager updatePasswordHint]_block_invoke
+ ___48-[PORegistrationManager storeCredentialContext:]_block_invoke
+ ___49-[POConfigurationManager resetTempSessionAccount]_block_invoke
+ ___57-[POUnlockProcess unlockKeybagWithTokenId:publicKeyHash:]_block_invoke
+ ___60-[PODaemonConnection resetTempSessionAccountWithCompletion:]_block_invoke
+ ___66-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:error:]_block_invoke
+ ___69-[POAgentAuthenticationProcess requestUserRegistrationRepairIfNeeded]_block_invoke
+ ___80-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:error:]_block_invoke
+ ___80-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:error:]_block_invoke_2
+ ___82-[PODaemonProcess verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]_block_invoke
+ ___84-[POAgentAuthenticationProcess repairKeybagRegistrationIfNeededWithPasswordContext:]_block_invoke
+ ___84-[POConfigurationManager verifyOwnSecureTokenPasswordForUser:passwordContext:error:]_block_invoke
+ ___85-[POAgentProcess repairTokenBindingForUser:passwordContextData:configurationManager:]_block_invoke
+ ___85-[PODaemonConnection verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]_block_invoke
+ ___91-[POAgentProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]_block_invoke
+ ___91-[POAgentProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]_block_invoke_2
+ ___OSUpdateLibraryCore_block_invoke
+ ___PO_LOG_POSoftwareUpdateCredentialPolicy_block_invoke
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s96s104s112bs_e47_v32?0Q8"POAuthenticationContext"16"NSData"24l
+ ___block_descriptor_56_e8_32s40s48s_e14_"NSError"8?0l
+ ___block_descriptor_57_e8_32s40s48bs_e20_v24?0Q8"NSError"16l
+ ___block_descriptor_65_e8_32s40s48s56s_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v24?0Q8"NSError"16l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e9_B16?0^8l
+ ___copy_helper_block_e8_32s40s48s56s64b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112b
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s
+ ___getSUOSULoginCredentialPolicyClass_block_invoke
+ ___swift_memcpy128_8
+ _audit_stringOSUpdate
+ _getSUOSULoginCredentialPolicyClass
+ _kPOErrorDomain
+ _krb5_get_init_creds_opt_set_tkt_life
+ _objc_msgSend$accountDisplayNameForDeviceConfiguration:loginConfiguration:
+ _objc_msgSend$addSecureTokenForUserName:password:tokenId:wrapPublicKeyHash:
+ _objc_msgSend$additionalHTTPHeaders
+ _objc_msgSend$alwaysUseLoginUI
+ _objc_msgSend$bindingProtocol
+ _objc_msgSend$biometricPolicyIsUnsatisfied:
+ _objc_msgSend$changeLoginKeychainPassword:newPassword:
+ _objc_msgSend$claimDeviceRegistrationStart
+ _objc_msgSend$claimRegistrationStartResumingUnfinishedDeviceRegistration:
+ _objc_msgSend$claimUserRegistrationStart
+ _objc_msgSend$configurationManagerForUserName:
+ _objc_msgSend$credentialsWanted
+ _objc_msgSend$currentLoginCredentialPolicy
+ _objc_msgSend$denyUnlockForUnsatisfiedBiometricPolicy
+ _objc_msgSend$dictionary
+ _objc_msgSend$domain
+ _objc_msgSend$handleUserNeedsReauthenticationAfterDelay:error:
+ _objc_msgSend$harvestPassword:forUserId:
+ _objc_msgSend$isCreatingNewUserForCurrentCredential
+ _objc_msgSend$isNewAccountPendingRegistration
+ _objc_msgSend$keybagBindingInfoForTokenId:uid:
+ _objc_msgSend$keybagNeedsPairingForTokenId:uid:
+ _objc_msgSend$keybagRotatingKeyPresentForUserName:pubKeyHash:
+ _objc_msgSend$keychainAccess
+ _objc_msgSend$loadKeybagForUserId:
+ _objc_msgSend$loginKeychainForUserName:password:
+ _objc_msgSend$pairKeybagWithTokenId:pubKeyHash:pin:userPassword:uid:
+ _objc_msgSend$platformSSOSecureTokenNeedsResetForUser:pin:
+ _objc_msgSend$postAuthenticationNotificationForEvaluationError:
+ _objc_msgSend$publishRegistrationContext:claim:
+ _objc_msgSend$readSecureTokenDataForUserName:tokenId:pin:
+ _objc_msgSend$registrationContextLock
+ _objc_msgSend$registrationGeneration
+ _objc_msgSend$registrationIsInProgress
+ _objc_msgSend$registrationStarting
+ _objc_msgSend$releaseRegistrationStart:
+ _objc_msgSend$removeSecureTokenForUserName:
+ _objc_msgSend$repairKeybagRegistrationIfNeededWithPasswordContext:
+ _objc_msgSend$repairTokenBindingForUser:passwordContextData:configurationManager:
+ _objc_msgSend$requestUserRegistrationRepairIfNeeded
+ _objc_msgSend$resetLoginKeychainWithPassword:resetSearchList:
+ _objc_msgSend$resetTempSessionAccount
+ _objc_msgSend$resetTempSessionAccountWithCompletion:
+ _objc_msgSend$resolvedLocalUserName
+ _objc_msgSend$secureTokenStatusForUserName:needed:valid:
+ _objc_msgSend$setAdditionalHTTPHeaders:
+ _objc_msgSend$setAlwaysUseLoginUI:
+ _objc_msgSend$setCredential:type:error:
+ _objc_msgSend$setExternalizedLocalAuthenticationContextData:
+ _objc_msgSend$setOptionUserId:
+ _objc_msgSend$setRegistrationGeneration:
+ _objc_msgSend$setRegistrationStarting:
+ _objc_msgSend$setUserRegistrationRepairRequested:
+ _objc_msgSend$shouldRunConfigurationChangeOnUnlock
+ _objc_msgSend$storeCredentialContext:
+ _objc_msgSend$stringForUserState:
+ _objc_msgSend$unlockKeyBagWithTokenId:pubKeyHash:pin:uid:
+ _objc_msgSend$unlockKeybagWithTokenId:publicKeyHash:
+ _objc_msgSend$updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:
+ _objc_msgSend$updateLocalAccountPassword:oldPasswordContextData:passwordContextData:completion:
+ _objc_msgSend$updatePasswordHint
+ _objc_msgSend$userRegistrationRepairLock
+ _objc_msgSend$userRegistrationRepairRequested
+ _objc_msgSend$validatedAdditionalHTTPHeaders:
+ _objc_msgSend$verifyOwnSecureTokenPassword:forUser:error:
+ _objc_msgSend$verifyOwnSecureTokenPasswordForUser:passwordContext:completion:
+ _objc_msgSend$verifyOwnSecureTokenPasswordForUser:passwordContext:error:
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_storeEnumTagSinglePayloadGeneric
+ _symbolic $s11PlatformSSO36POSoftwareUpdateCredentialHarvestingP
+ _symbolic ScCy_____6result_______pSg5errort_____G So13POLoginResultV s5ErrorP s5NeverO
+ _symbolic _____ 11PlatformSSO32PODefaultLoginAuthenticationFlowC16EmptyResultCause33_951AFF0CEBAFBE17F65C3243B9B516A9LLO
+ _symbolic _____ 11PlatformSSO40DefaultSoftwareUpdateCredentialHarvesterV
+ _symbolic _____6result_______pSg5errort So13POLoginResultV s5ErrorP
+ _symbolic ______p 11PlatformSSO36POSoftwareUpdateCredentialHarvestingP
+ _symbolic _____y______pSgG s23_ContiguousArrayStorageC 15PlatformSSOCore15POAuthenticatorP
+ getSUOSULoginCredentialPolicyClass.softClass
- -[POConfigurationManager platformSSOSecureTokenNeedsResetForUser:]
- -[PORegistrationManager storeCredentialAndUpdatePasswordHint]
- GCC_except_table101
- GCC_except_table104
- GCC_except_table115
- GCC_except_table116
- GCC_except_table121
- GCC_except_table124
- GCC_except_table126
- GCC_except_table139
- GCC_except_table141
- GCC_except_table147
- GCC_except_table148
- GCC_except_table161
- GCC_except_table164
- GCC_except_table175
- GCC_except_table176
- GCC_except_table181
- GCC_except_table182
- GCC_except_table196
- GCC_except_table202
- GCC_except_table204
- GCC_except_table210
- GCC_except_table213
- GCC_except_table225
- GCC_except_table235
- GCC_except_table268
- GCC_except_table276
- GCC_except_table277
- GCC_except_table41
- GCC_except_table56
- GCC_except_table82
- GCC_except_table88
- GCC_except_table89
- GCC_except_table99
- _OBJC_CLASS_$_POBaseSystemSupport
- _SecKeychainChangePassword
- _SecKeychainEraseUnlockKeyWithPubKeyHash
- _SecKeychainLogin
- _SecKeychainResetLogin
- __60-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]_block_invoke
- __61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke
- __72-[POAgentProcess updateLocalAccountPassword:passwordContext:completion:]_block_invoke
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke
- __74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke_2
- ___60-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]_block_invoke
- ___61-[PORegistrationManager storeCredentialAndUpdatePasswordHint]_block_invoke
- ___72-[POAgentProcess updateLocalAccountPassword:passwordContext:completion:]_block_invoke
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke
- ___74-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]_block_invoke_2
- ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96s104bs_e47_v32?0Q8"POAuthenticationContext"16"NSData"24l
- ___block_descriptor_44_e8_32s_e14_"NSError"8?0l
- _objc_msgSend$lengthOfBytesUsingEncoding:
- _objc_msgSend$platformSSOSecureTokenNeedsResetForUser:
- _objc_msgSend$prebootVolumePathForUUID:shouldUnmount:
- _objc_msgSend$storeCredentialAndUpdatePasswordHint
- _objc_msgSend$systemVolumeDiskIdentifierForVolumeGroupIdentifier:
- _objc_msgSend$verifyOwnSecureTokenPassword:forUser:
- _objc_msgSend$volumeUUID
CStrings:
+ "\v"
+ " submission failed"
+ "%s failed to encode the credential on %@"
+ "%s failed to externalize the credential context, uid:%{public}@ on %@"
+ "%s failed to set the boot password credential, uid:%{public}@ error:%{public}@ on %@"
+ "%s failed to set the secure passphrase credential, uid:%{public}@ error:%{public}@ on %@"
+ ")#Z"
+ "+[POSoftwareUpdateCredentialPolicy harvestPassword:forUserId:]"
+ "-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:error:]"
+ "-[POAuthPluginProcess updateLocalAccountPassword:oldPasswordContext:passwordContext:completion:]"
+ "-[POConfigurationManager platformSSOSecureTokenNeedsResetForUser:pin:]"
+ "-[POConfigurationManager resetTempSessionAccount]"
+ "-[POConfigurationManager verifyOwnSecureTokenPasswordForUser:passwordContext:error:]"
+ "-[PODaemonProcess verifyOwnSecureTokenPasswordForUser:passwordContext:completion:]"
+ "-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:error:]"
+ "/System/Library/PrivateFrameworks/OSUpdate.framework/Contents/MacOS/OSUpdate"
+ "A registration check was already requested for this user"
+ "A registration is already in progress (state = %{public}@), not asking for a registration check"
+ "A registration is already running for this new user; not running the registration checks on unlock"
+ "AdditionalHTTPHeaders"
+ "AllowWebLoginPasswordSync is set but the IdP supplied no extractable password; skipping the password sync"
+ "AlwaysUseLoginUI"
+ "Auth rights already checked for this build"
+ "Auth rights check failed, screen unlock may not use Platform SSO: %{public}@"
+ "Auth rights checked successfully"
+ "Authentication flow: Unlocking keybag with token (%{public}u)"
+ "B16@?0^@8"
+ "Binding credential context is not externalized"
+ "Binding repair is pending but no extractable credential is available; deferring to the next login that supplies one"
+ "Bootstrap token is not supported; not verifying the secure token because the divergence could not be repaired."
+ "Cannot continue the FileVault token unlock; returning to the login prompt."
+ "Could not verify the new password against the account's own secure token; not repairing with the bootstrap token: %{public}@"
+ "Could not verify the password against the account's own secure token; not escalating to the forced password change: %{public}@"
+ "Could not verify the password against the own secure token."
+ "Failed to build the token unlock blob."
+ "Failed to create the screensaver right version"
+ "Failed to migrate the keybag registration to the current protocol."
+ "Failed to pair the keybag during token binding for user."
+ "Failed to reset temp session account index."
+ "Failed to restore user configuration after a deferred keybag migration."
+ "Failed to save user configuration after key update."
+ "Failed to save user configuration after re-pairing the token."
+ "Failed to unlock the keybag with the token."
+ "Falling back to password-authorized local account password change"
+ "Incomplete token unlock configuration (key hash %{public}@, certificate %{public}@, unlock data %{public}@, token id %{public}@); nothing to pair"
+ "Invalid user id for keybag unlock."
+ "Key rotation and binding both succeeded; clearing the binding repair flag"
+ "Keybag has no current registration for this token (POKeybagBindingProtocol %{public}ld); pairing it with the verified local account password"
+ "Keybag has no usable registration for this token; pairing before the keybag password change"
+ "Keybag migration deferred; leaving the user state as it was rather than marking a binding owed"
+ "Keybag needs pairing and the submitted credential is not the local account password"
+ "Keybag pairing failed, so the keybag password cannot be changed with the token: "
+ "Keybag registration for the current token is up to date"
+ "Keybag registration for the current token needs repair (%{public}@); pairing it with the local account password"
+ "Keybag rekey failed at login; falling back to the password-authorized local account password change"
+ "Keybag unlocked with token"
+ "Local account password change failed for user, including the forced change"
+ "Local account password sync failed; continuing with the existing account password"
+ "Local user found"
+ "Login Policy: denied, TouchID is required and cannot be satisfied on the built-in credential path"
+ "Login Policy: the account is pending registration, deferring to the local credential"
+ "Login type %{public}ld does not pair with a password; nothing to repair"
+ "Missing credential for token keybag unlock."
+ "Missing token values for keybag unlock."
+ "No authenticator result to route"
+ "No configuration; nothing to repair"
+ "No device configuration to back-fill"
+ "No extractable credential is available for binding; skipping the key request so the existing token pairing is left intact"
+ "No extractable credential; deferring the keybag repair to the next unlock or login that supplies one"
+ "No keybag repair for temporary users"
+ "No temporary account bound to the unlocking user, falling back to the rotation index"
+ "No uid for the user; cannot pair the keybag."
+ "No usable old credential was supplied; using the stashed credential"
+ "Not flagging %{public}@ for binding repair: token unlock is not supported, so there is nothing to bind (%{public}s)"
+ "OpenID Authorization Request: Performing auth in the system session for an elevation prompt"
+ "Own secure token rejected the password."
+ "POSoftwareUpdateCredentialPolicy"
+ "Password missing"
+ "Password sync required but no credential context is available; continuing with the existing account password"
+ "Password update fallback result: %{public}@"
+ "PlatformSSO secure token KEK resolves and cannot be test-unwrapped; leaving it alone"
+ "PlatformSSO secure token KEK resolves but cannot be unwrapped (%d); it is wrapped to a key this account no longer has, so it has to be recreated"
+ "Registration has failed, not asking for a registration check"
+ "Reset Temp session to: 0"
+ "SUOSULoginCredentialPolicy"
+ "Syncing the local account password to the IdP password"
+ "The account's own secure token rejected this password; retrying with the forced password change"
+ "The configuration changed while this registration was starting; not publishing it"
+ "The federationUserPreauthenticationURL is missing for dynamic OpenID."
+ "The new credential context cannot be externalized"
+ "Token binding is owed for %{public}@; using password authentication instead of token unlock"
+ "Token binding is owed; token unlock is unavailable and the IdP password cannot be synced during login. Sign in with the local account password to repair it."
+ "Token binding updated for the new password; clearing binding repair flag"
+ "Token re-paired after password-authorized fallback; clearing binding repair flag"
+ "Token unlock is not supported; nothing to pair"
+ "Unlocking keybag with token for uid: %{public}@"
+ "User registration is not usable (state = %{public}@), running the registration checks"
+ "User registration needs to be repaired before the user can authenticate."
+ "User registration no longer needs repair (state = %{public}@)"
+ "another registration is already starting"
+ "finishSuccessfulUserRegistration()"
+ "handleTokenAuthAfterSuccessfulIdPAuthentication: IdP authentication SUCCEEDED but login cannot complete: the token binding is owed (POUserStateNeedsBinding), so the token cannot unlock the keychain, and the IdP password cannot be synced to the local account here — no user session yet, and no old password or bound token to authorize the change. The user must sign in with the LOCAL account password, which repairs the binding and clears this state; the IdP password works again afterwards."
+ "keybag pairing failed before the keybag password change"
+ "login right already uses the Platform SSO mechanism, no changes"
+ "login right updated to use the Platform SSO mechanism"
+ "missing"
+ "no credential was submitted"
+ "no rotating key in the login configuration"
+ "nothing registered"
+ "present"
+ "resolveResult(%{public}s): nothing to route, %{public}s"
+ "screensaver right already uses the Platform SSO rule, no changes"
+ "screensaver right currently uses rule %{public}@, updating to psso-screensaver"
+ "screensaver right updated to use the Platform SSO rule, version %lld"
+ "shouldRun(%{public}s, %{public}s): false - OpenID not configured, or missing required values"
+ "shouldRun(%{public}s, %{public}s): false - account is exempt from Platform SSO policy"
+ "softlink:o:path:/System/Library/PrivateFrameworks/OSUpdate.framework/OSUpdate"
+ "softwareUpdateHarvest: harvested=%{bool,public}d, sessionType=%{public}s, uid=%{public}u"
+ "softwareUpdateHarvest: skipped, reason=rootUid"
+ "softwareUpdateHarvest: skipped, reason=temporaryUser"
+ "the flow was cancelled"
+ "the legacy v1 protocol"
+ "token binding failed after password-authorized change"
+ "token re-pair after the password-authorized fallback did not take"
+ "unlockKeybagAtLoginWindow: keybag load failed, uid=%{public}u"
+ "unlockKeybagAtLoginWindow: keybag unlock failed, type=token, uid=%{public}u, result=%{public}d"
+ "unlockKeybagAtLoginWindow: keybag unlocked, type=token, uid=%{public}u"
+ "version"
+ "\xf0\xf0Q"
- "\n"
- ")#Y"
- "-[POAgentAuthenticationProcess handleUserNeedsReauthenticationAfterDelay:]"
- "-[POConfigurationManager platformSSOSecureTokenNeedsResetForUser:]"
- "-[PODirectoryServices verifyOwnSecureTokenPassword:forUser:]"
- "/%@/%@%@"
- "Creating context for synced user credential"
- "Failed to remove old preboot path"
- "Own secure token did not accept the password."
- "Preboot volume path: %{public}@"
- "Remove previous keychain binding, if it exists"
- "Rule already checked"
- "Rule successfully checked"
- "User registration already in progress: %{public}@"
- "failed to remove previous keychain binding: %{public}d"
- "shouldRun(%{public}s, %{public}s): false - OpenID not configured"
- "\xf0\xf01"
```
