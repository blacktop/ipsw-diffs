## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/Versions/A/DMCEnrollmentLibrary`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x19be4
+20.4.18.0.0
+  __TEXT.__text: 0x1fba8
   __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_methlist: 0xfa8
+  __TEXT.__objc_methlist: 0x1160
   __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x20df
-  __TEXT.__cstring: 0x1857
-  __TEXT.__gcc_except_tab: 0x654
+  __TEXT.__oslogstring: 0x233b
+  __TEXT.__cstring: 0x193f
+  __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0x578
+  __TEXT.__unwind_info: 0x6b0
   __TEXT.__objc_classname: 0xf5
-  __TEXT.__objc_methname: 0x5695
-  __TEXT.__objc_methtype: 0x587
-  __TEXT.__objc_stubs: 0x3fc0
-  __DATA_CONST.__got: 0x338
-  __DATA_CONST.__const: 0x280
+  __TEXT.__objc_methname: 0x5efc
+  __TEXT.__objc_methtype: 0x5e5
+  __TEXT.__objc_stubs: 0x4640
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1150
+  __DATA_CONST.__objc_selrefs: 0x1308
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x5e8
+  __DATA_CONST.__objc_arraydata: 0x2e0
   __AUTH_CONST.__auth_got: 0x1a0
-  __AUTH_CONST.__const: 0xb70
-  __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x1030
-  __AUTH_CONST.__objc_intobj: 0x600
-  __AUTH_CONST.__objc_arrayobj: 0x360
+  __AUTH_CONST.__const: 0xc20
+  __AUTH_CONST.__cfstring: 0x1020
+  __AUTH_CONST.__objc_const: 0x1040
+  __AUTH_CONST.__objc_intobj: 0x6a8
+  __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0xf4
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x1a0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96C728B1-F80C-364D-8A25-E376C5C865E1
-  Functions: 481
-  Symbols:   1371
-  CStrings:  1210
+  UUID: B596D684-91D8-351B-9603-19E16227E966
+  Functions: 559
+  Symbols:   1556
+  CStrings:  1302
 
Symbols:
+ +[DMCEnrollmentFlowController enrollmentFlowControllerWithPresenter:managedConfigurationHelper:rmStoreHelper:]
+ +[DMCEnrollmentFlowController(Utilities) _createInvalidErSSODeclarationsError]
+ -[DMCEnrollmentDirtyState clearDirtyRMStoreForErSSO]
+ -[DMCEnrollmentDirtyState dirtyRMStoreForErSSO]
+ -[DMCEnrollmentDirtyState setDirtyRMStoreForErSSO]
+ -[DMCEnrollmentFlowController _analyzeESSODetails:]
+ -[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]
+ -[DMCEnrollmentFlowController _ensureDeviceActivation]
+ -[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]
+ -[DMCEnrollmentFlowController _initiateDEPPushTokenSync]
+ -[DMCEnrollmentFlowController _installESSOConfigurationWithProfileData:declarations:devicePasscode:personaID:]
+ -[DMCEnrollmentFlowController _installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:]
+ -[DMCEnrollmentFlowController _linkESSOStore:rmAccountIdentifier:profileIdentifier:]
+ -[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]
+ -[DMCEnrollmentFlowController _restoreLanguage:locale:]
+ -[DMCEnrollmentFlowController _updateCloudConfigWithRMAccountIdentifier:]
+ -[DMCEnrollmentFlowController _waitForESSODeclarations]
+ -[DMCEnrollmentFlowController initWithPresenter:managedConfigurationHelper:rmStoreHelper:]
+ -[DMCEnrollmentFlowController rmStoreHelper]
+ -[DMCEnrollmentFlowController setRmStoreHelper:]
+ -[DMCEnrollmentFlowController setSoftwareUpdateInfo:]
+ -[DMCEnrollmentFlowController softwareUpdateInfo]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_ESSO_firstPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_ESSO_secondPartSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_ESSO_secondPartSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_firstPartSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_secondPartSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_secondPartSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_firstPart_commonSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_installAppSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_postEnrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_secondPart_commonSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_secondPart_commonSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_consentAndCreatePersonaSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_postEnrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_secondPart_commonSteps_default]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_secondPart_commonSteps_orgToken]
+ -[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_fetchEnrollmentProfileSteps]
+ -[DMCEnrollmentFlowController(Sequence) _MAID_fetchEnrollmentProfileSteps]
+ -[DMCEnrollmentFlowController(Sequence) _createRMAccountSteps]
+ -[DMCEnrollmentFlowController(Sequence) _enrollmentSteps]
+ -[DMCEnrollmentFlowController(Sequence) _ephemeralAuthSteps]
+ -[DMCEnrollmentFlowController(Sequence) _fetchAndAnalyzeCloudConfigSteps]
+ -[DMCEnrollmentFlowController(Sequence) _permanentAuthSteps]
+ -[DMCEnrollmentFlowController(Sequence) _postEnrollmentSteps].cold.1
+ -[DMCEnrollmentFlowController(Sequence) _signInMAIDSteps]
+ -[DMCEnrollmentFlowController(Sequence) _silentAuthSteps]
+ -[DMCEnrollmentFlowController(Sequence) _stepsWithUI].cold.1
+ -[DMCEnrollmentFlowController(Utilities) _errorTranslation].cold.1
+ -[DMCEnrollmentFlowController(Utilities) _trustedErrors].cold.1
+ GCC_except_table108
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table125
+ GCC_except_table130
+ GCC_except_table150
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table193
+ GCC_except_table196
+ GCC_except_table199
+ GCC_except_table203
+ GCC_except_table207
+ GCC_except_table212
+ GCC_except_table218
+ GCC_except_table33
+ GCC_except_table55
+ GCC_except_table67
+ GCC_except_table75
+ GCC_except_table83
+ GCC_except_table87
+ GCC_except_table90
+ GCC_except_table93
+ OBJC_IVAR_$_DMCEnrollmentFlowController._rmStoreHelper
+ OBJC_IVAR_$_DMCEnrollmentFlowController._softwareUpdateInfo
+ _ADE_RTS_commonSteps.onceToken
+ _ADE_RTS_commonSteps.ret
+ _ADE_commonSteps.onceToken
+ _ADE_commonSteps.ret
+ _ADxE_ABE_ESSO_firstPartSteps.onceToken
+ _ADxE_ABE_ESSO_firstPartSteps.ret
+ _ADxE_ABE_ESSO_secondPartSteps_default.onceToken
+ _ADxE_ABE_ESSO_secondPartSteps_default.ret
+ _ADxE_ABE_ESSO_secondPartSteps_orgToken.onceToken
+ _ADxE_ABE_ESSO_secondPartSteps_orgToken.ret
+ _ADxE_ABE_firstPartSteps.onceToken
+ _ADxE_ABE_firstPartSteps.ret
+ _ADxE_ABE_secondPartSteps_default.onceToken
+ _ADxE_ABE_secondPartSteps_default.ret
+ _ADxE_ABE_secondPartSteps_orgToken.onceToken
+ _ADxE_ABE_secondPartSteps_orgToken.ret
+ _ADxE_ESSO_firstPart_commonSteps.onceToken
+ _ADxE_ESSO_firstPart_commonSteps.ret
+ _ADxE_ESSO_secondPart_commonSteps_default.onceToken
+ _ADxE_ESSO_secondPart_commonSteps_default.ret
+ _ADxE_ESSO_secondPart_commonSteps_orgToken.onceToken
+ _ADxE_ESSO_secondPart_commonSteps_orgToken.ret
+ _ADxE_secondPart_commonSteps_default.onceToken
+ _ADxE_secondPart_commonSteps_default.ret
+ _ADxE_secondPart_commonSteps_orgToken.onceToken
+ _ADxE_secondPart_commonSteps_orgToken.ret
+ _ADxE_thirdParty_ESSO_firstPartSteps.onceToken
+ _ADxE_thirdParty_ESSO_firstPartSteps.ret
+ _ADxE_thirdParty_firstPartSteps.onceToken
+ _ADxE_thirdParty_firstPartSteps.ret
+ _OBJC_CLASS_$_NSPredicate
+ _ORGO_MACBuddy_firstPartSteps.onceToken
+ _ORGO_MACBuddy_firstPartSteps.ret
+ _ORGO_MACBuddy_secondPartSteps.onceToken
+ _ORGO_MACBuddy_secondPartSteps.ret
+ _ORGO_MAIDEnrollmentSteps.onceToken
+ _ORGO_MAIDEnrollmentSteps.ret
+ _ORGO_MAIDEnrollmentSteps_orgToken.onceToken
+ _ORGO_MAIDEnrollmentSteps_orgToken.ret
+ __115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.94
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.105
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.109
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.118
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke.126
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.110
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.119
+ __125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2.127
+ __127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.156
+ __127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.158
+ __127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.159
+ __137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.160
+ __137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.163
+ __137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.164
+ __54-[DMCEnrollmentFlowController _askForPasscodeIfNeeded]_block_invoke.70
+ __68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.207
+ __68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.208
+ __85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.182
+ ___111-[DMCEnrollmentFlowController _installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:]_block_invoke
+ ___111-[DMCEnrollmentFlowController _installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:]_block_invoke_2
+ ___114-[DMCEnrollmentFlowController _preflightEnrollmentWithEnrollmentType:isRenewalFlow:isPostRestoration:isPostBuddy:]_block_invoke
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_3
+ ___125-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_4
+ ___50-[DMCEnrollmentFlowController _cleanupDirtyState:]_block_invoke
+ ___54-[DMCEnrollmentFlowController _ensureDeviceActivation]_block_invoke
+ ___54-[DMCEnrollmentFlowController _ensureDeviceActivation]_block_invoke_2
+ ___55-[DMCEnrollmentFlowController _restoreLanguage:locale:]_block_invoke
+ ___55-[DMCEnrollmentFlowController _restoreLanguage:locale:]_block_invoke_2
+ ___55-[DMCEnrollmentFlowController _waitForESSODeclarations]_block_invoke
+ ___55-[DMCEnrollmentFlowController _waitForESSODeclarations]_block_invoke_2
+ ___56-[DMCEnrollmentFlowController _initiateDEPPushTokenSync]_block_invoke
+ ___56-[DMCEnrollmentFlowController _initiateDEPPushTokenSync]_block_invoke_2
+ ___57-[DMCEnrollmentFlowController(Sequence) _ADE_commonSteps]_block_invoke
+ ___60-[DMCEnrollmentFlowController(Sequence) _ephemeralAuthSteps]_block_invoke
+ ___60-[DMCEnrollmentFlowController(Sequence) _permanentAuthSteps]_block_invoke
+ ___61-[DMCEnrollmentFlowController(Sequence) _ADE_RTS_commonSteps]_block_invoke
+ ___65-[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_firstPartSteps]_block_invoke
+ ___66-[DMCEnrollmentFlowController(Sequence) _ORGO_MAIDEnrollmentSteps]_block_invoke
+ ___67-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]_block_invoke
+ ___67-[DMCEnrollmentFlowController _extensionIDsFromDeclarationProfiles]_block_invoke_2
+ ___70-[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_ESSO_firstPartSteps]_block_invoke
+ ___70-[DMCEnrollmentFlowController(Sequence) _ORGO_MACBuddy_firstPartSteps]_block_invoke
+ ___71-[DMCEnrollmentFlowController(Sequence) _ORGO_MACBuddy_secondPartSteps]_block_invoke
+ ___72-[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_firstPartSteps]_block_invoke
+ ___73-[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_firstPart_commonSteps]_block_invoke
+ ___74-[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_secondPartSteps_default]_block_invoke
+ ___75-[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_secondPartSteps_orgToken]_block_invoke
+ ___75-[DMCEnrollmentFlowController(Sequence) _ORGO_MAIDEnrollmentSteps_orgToken]_block_invoke
+ ___77-[DMCEnrollmentFlowController(Sequence) _ADxE_secondPart_commonSteps_default]_block_invoke
+ ___77-[DMCEnrollmentFlowController(Sequence) _ADxE_thirdParty_ESSO_firstPartSteps]_block_invoke
+ ___78-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke
+ ___78-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke_2
+ ___78-[DMCEnrollmentFlowController(Sequence) _ADxE_secondPart_commonSteps_orgToken]_block_invoke
+ ___79-[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_ESSO_secondPartSteps_default]_block_invoke
+ ___80-[DMCEnrollmentFlowController(Sequence) _ADxE_ABE_ESSO_secondPartSteps_orgToken]_block_invoke
+ ___82-[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_secondPart_commonSteps_default]_block_invoke
+ ___83-[DMCEnrollmentFlowController(Sequence) _ADxE_ESSO_secondPart_commonSteps_orgToken]_block_invoke
+ ___84-[DMCEnrollmentFlowController _linkESSOStore:rmAccountIdentifier:profileIdentifier:]_block_invoke
+ ___84-[DMCEnrollmentFlowController _linkESSOStore:rmAccountIdentifier:profileIdentifier:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e36_B24?0"ACAccount"8"NSDictionary"16l
+ ___block_descriptor_48_e8_32s40w_e8_v12?0B8l
+ __block_literal_global.175
+ __block_literal_global.73
+ _ephemeralAuthSteps.onceToken
+ _ephemeralAuthSteps.ret
+ _kCCRemoteManagementAccountIdentifierKey
+ _kDMCErrorDetailsSUInfoKey
+ _kRMBridgeAppStoreIDKey
+ _kRMBridgeBundleIDKey
+ _objc_msgSend$_ADE_RTS_commonSteps
+ _objc_msgSend$_ADxE_ABE_ESSO_firstPartSteps
+ _objc_msgSend$_ADxE_ABE_ESSO_secondPartSteps_default
+ _objc_msgSend$_ADxE_ABE_ESSO_secondPartSteps_orgToken
+ _objc_msgSend$_ADxE_ABE_firstPartSteps
+ _objc_msgSend$_ADxE_ABE_secondPartSteps_default
+ _objc_msgSend$_ADxE_ABE_secondPartSteps_orgToken
+ _objc_msgSend$_ADxE_ESSO_firstPart_commonSteps
+ _objc_msgSend$_ADxE_ESSO_installAppSteps
+ _objc_msgSend$_ADxE_ESSO_postEnrollmentSteps
+ _objc_msgSend$_ADxE_ESSO_secondPart_commonSteps_default
+ _objc_msgSend$_ADxE_ESSO_secondPart_commonSteps_orgToken
+ _objc_msgSend$_ADxE_consentAndCreatePersonaSteps
+ _objc_msgSend$_ADxE_postEnrollmentSteps
+ _objc_msgSend$_ADxE_secondPart_commonSteps_default
+ _objc_msgSend$_ADxE_secondPart_commonSteps_orgToken
+ _objc_msgSend$_ADxE_thirdParty_fetchEnrollmentProfileSteps
+ _objc_msgSend$_MAID_fetchEnrollmentProfileSteps
+ _objc_msgSend$_analyzeESSODetails:
+ _objc_msgSend$_askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:
+ _objc_msgSend$_createRMAccountSteps
+ _objc_msgSend$_enrollmentSteps
+ _objc_msgSend$_ensureDeviceActivation
+ _objc_msgSend$_ephemeralAuthSteps
+ _objc_msgSend$_extensionIDsFromDeclarationProfiles
+ _objc_msgSend$_fetchAndAnalyzeCloudConfigSteps
+ _objc_msgSend$_initiateDEPPushTokenSync
+ _objc_msgSend$_installESSOConfigurationWithProfileData:declarations:devicePasscode:personaID:
+ _objc_msgSend$_installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:
+ _objc_msgSend$_linkESSOStore:rmAccountIdentifier:profileIdentifier:
+ _objc_msgSend$_permanentAuthSteps
+ _objc_msgSend$_promptForSoftwareUpdateWithSoftwareUpdateInfo:
+ _objc_msgSend$_restoreLanguage:locale:
+ _objc_msgSend$_signInMAIDSteps
+ _objc_msgSend$_silentAuthSteps
+ _objc_msgSend$_updateCloudConfigWithRMAccountIdentifier:
+ _objc_msgSend$_waitForESSODeclarations
+ _objc_msgSend$clearDirtyRMStoreForErSSO
+ _objc_msgSend$createErSSOStoreWithDeclarations:chosenBundleID:personaID:isUserEnrollment:completionHandler:
+ _objc_msgSend$declarations
+ _objc_msgSend$dirtyRMStoreForErSSO
+ _objc_msgSend$dmc_RemoteManagementAccounts
+ _objc_msgSend$enrollmentFlowController:didUpdateEnrollmentMethod:
+ _objc_msgSend$ensureActivationWithCompletionHandler:
+ _objc_msgSend$extensibleSSOProfileIdentifiersWithCompletionHandler:
+ _objc_msgSend$extensionIDsFromESSOProfileIdentifiers:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$initWithPresenter:managedConfigurationHelper:rmStoreHelper:
+ _objc_msgSend$initiateDEPPushTokenSyncWithCompletionHandler:
+ _objc_msgSend$isProvisionallyEnrolledWithCloudConfig:
+ _objc_msgSend$languageStrings
+ _objc_msgSend$linkErSSOStoreToMDMWithProfileIdentifier:accountIdentifier:completionHandler:
+ _objc_msgSend$localeString
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$removeErSSOStoreWithCompletionHandler:
+ _objc_msgSend$requestDeviceErasureWithCompletionHandler:
+ _objc_msgSend$requestSoftwareUpdateWithInfoDictionary:completionHandler:
+ _objc_msgSend$requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:
+ _objc_msgSend$rmStoreHelper
+ _objc_msgSend$setDirtyRMStoreForErSSO
+ _objc_msgSend$setSoftwareUpdateInfo:
+ _objc_msgSend$softwareUpdateInfo
+ _objc_msgSend$unassignFromDEPWithCompletionHandler:
+ _objc_msgSend$updateCloudConfigurationWithRMAccountIdentifier:
+ _objc_msgSend$updateLanguage:locale:completionHandler:
+ _objc_msgSend$waitForActiveAndValidDeclarationsInErSSOStoreWithTimeout:completionHandler:
+ _permanentAuthSteps.onceToken
+ _permanentAuthSteps.ret
- -[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]
- -[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]
- -[DMCEnrollmentFlowController expectedBuildVersion]
- -[DMCEnrollmentFlowController expectedOSVersion]
- -[DMCEnrollmentFlowController setExpectedBuildVersion:]
- -[DMCEnrollmentFlowController setExpectedOSVersion:]
- -[DMCEnrollmentFlowController(Sequence) _ADxE_MAID_firstPartSteps]
- -[DMCEnrollmentFlowController(Sequence) _ADxE_MAID_secondPartSteps_default]
- -[DMCEnrollmentFlowController(Sequence) _ADxE_MAID_secondPartSteps_orgToken]
- -[DMCEnrollmentFlowController(Sequence) _ORGO_pre_enrollment_steps]
- GCC_except_table100
- GCC_except_table114
- GCC_except_table119
- GCC_except_table128
- GCC_except_table142
- GCC_except_table145
- GCC_except_table168
- GCC_except_table171
- GCC_except_table174
- GCC_except_table178
- GCC_except_table182
- GCC_except_table187
- GCC_except_table30
- GCC_except_table45
- GCC_except_table57
- GCC_except_table65
- GCC_except_table73
- GCC_except_table82
- GCC_except_table85
- GCC_except_table88
- GCC_except_table94
- GCC_except_table97
- OBJC_IVAR_$_DMCEnrollmentFlowController._expectedBuildVersion
- OBJC_IVAR_$_DMCEnrollmentFlowController._expectedOSVersion
- __110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke.105
- __110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke.96
- __110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_2.106
- __115-[DMCEnrollmentFlowController _exchangeMAIDForBearerTokenWithRMAccountIdentifier:authParams:anchorCertificateRefs:]_block_invoke.87
- __127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.135
- __127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.137
- __127-[DMCEnrollmentFlowController _correlateMAIDWithAltDSID:withRMAccount:isProfileLocked:organizationName:friendlyName:personaID:]_block_invoke.138
- __137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.139
- __137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.142
- __137-[DMCEnrollmentFlowController _updateAccountsWithRMIdentifier:managedAppleID:profileIdentifier:organizationName:enrollmentURL:personaID:]_block_invoke.143
- __54-[DMCEnrollmentFlowController _askForPasscodeIfNeeded]_block_invoke.63
- __68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke.185
- __68-[DMCEnrollmentFlowController _ensureWiFiConnectionWithWiFiProfile:]_block_invoke_2.186
- __85-[DMCEnrollmentFlowController _fetchCloudConfigWithEnrollmentType:isReturnToService:]_block_invoke.158
- ___110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke
- ___110-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_2
- ___98-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]_block_invoke
- ___98-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]_block_invoke_2
- __block_literal_global.173
- __block_literal_global.76
- _kDMCErrorDetailsBuildVersionKey
- _kDMCErrorDetailsOSVersionKey
- _objc_msgSend$_ADxE_MAID_firstPartSteps
- _objc_msgSend$_ADxE_MAID_secondPartSteps_default
- _objc_msgSend$_ADxE_MAID_secondPartSteps_orgToken
- _objc_msgSend$_ORGO_pre_enrollment_steps
- _objc_msgSend$_askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:
- _objc_msgSend$_promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:
- _objc_msgSend$dmc_visibleRemoteManagementAccounts
- _objc_msgSend$expectedBuildVersion
- _objc_msgSend$expectedOSVersion
- _objc_msgSend$initWithPresenter:managedConfigurationHelper:
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:
- _objc_msgSend$setExpectedBuildVersion:
- _objc_msgSend$setExpectedOSVersion:
CStrings:
+ "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _restoreLanguage:locale:]_block_invoke_2"
+ "@\"<DMCEnrollmentFlowRMBridge>\""
+ "@40@0:8@16@24@32"
+ "AnalyzeESSODetails"
+ "AppStoreID"
+ "Cleaning up dirty ErSSO RMStore"
+ "Client %{public}@ does not implement %{public}@"
+ "DMC_INVALID_ERSSO_DECLARATIONS"
+ "ESSO configuration profile identifiers: %{public}@"
+ "EnsureActivation"
+ "ErSSO cannot link store with error: %{public}@"
+ "ErSSO configuration profile identifiers: %{public}@"
+ "ErSSO declarations installation failed with error: %{public}@"
+ "ErSSO declarations profile identifiers failed with error: %{public}@"
+ "ErSSO declarations wait failed with error: %{public}@"
+ "Failed to initiate DEP push token sync with error: %{public}@"
+ "Failed to update language & locale due to error: %{public}@"
+ "InitiateDEPPushTokenSync"
+ "InstallESSOConfiguration"
+ "Installing ErSSO configuration profile"
+ "Installing ErSSO declarations"
+ "Invalid ErSSO RMStore helper"
+ "LinkESSOStore"
+ "Missing ErSSO configuration"
+ "Multiple RM accounts exist on the device: %{public}@!"
+ "Not able to set language & locale"
+ "RMStoreForErSSO"
+ "RestoreLanguageAndLocale"
+ "T@\"<DMCEnrollmentFlowRMBridge>\",&,N,V_rmStoreHelper"
+ "T@\"NSDictionary\",&,N,V_softwareUpdateInfo"
+ "TB,R"
+ "UpdateCloudConfigWithRMAccount"
+ "UpdateESSOApplication"
+ "_ADxE_ABE_ESSO_firstPartSteps"
+ "_ADxE_ABE_ESSO_secondPartSteps_default"
+ "_ADxE_ABE_ESSO_secondPartSteps_orgToken"
+ "_ADxE_ABE_firstPartSteps"
+ "_ADxE_ABE_secondPartSteps_default"
+ "_ADxE_ABE_secondPartSteps_orgToken"
+ "_ADxE_ESSO_firstPart_commonSteps"
+ "_ADxE_ESSO_installAppSteps"
+ "_ADxE_ESSO_postEnrollmentSteps"
+ "_ADxE_ESSO_secondPart_commonSteps_default"
+ "_ADxE_ESSO_secondPart_commonSteps_orgToken"
+ "_ADxE_consentAndCreatePersonaSteps"
+ "_ADxE_postEnrollmentSteps"
+ "_ADxE_secondPart_commonSteps_default"
+ "_ADxE_secondPart_commonSteps_orgToken"
+ "_ADxE_thirdParty_fetchEnrollmentProfileSteps"
+ "_MAID_fetchEnrollmentProfileSteps"
+ "_analyzeESSODetails:"
+ "_askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:"
+ "_createInvalidErSSODeclarationsError"
+ "_createRMAccountSteps"
+ "_enrollmentSteps"
+ "_ensureDeviceActivation"
+ "_ephemeralAuthSteps"
+ "_extensionIDsFromDeclarationProfiles"
+ "_fetchAndAnalyzeCloudConfigSteps"
+ "_initiateDEPPushTokenSync"
+ "_installESSOConfigurationWithProfileData:declarations:devicePasscode:personaID:"
+ "_installESSODeclarations:devicePasscode:chosenBundleID:personaID:enrollmentType:"
+ "_linkESSOStore:rmAccountIdentifier:profileIdentifier:"
+ "_permanentAuthSteps"
+ "_promptForSoftwareUpdateWithSoftwareUpdateInfo:"
+ "_restoreLanguage:locale:"
+ "_rmStoreHelper"
+ "_signInMAIDSteps"
+ "_silentAuthSteps"
+ "_softwareUpdateInfo"
+ "_updateCloudConfigWithRMAccountIdentifier:"
+ "_waitForESSODeclarations"
+ "clearDirtyRMStoreForErSSO"
+ "createErSSOStoreWithDeclarations:chosenBundleID:personaID:isUserEnrollment:completionHandler:"
+ "declarations"
+ "dirtyRMStoreForErSSO"
+ "dmc_RemoteManagementAccounts"
+ "enrollmentFlowController:didUpdateEnrollmentMethod:"
+ "enrollmentFlowControllerWithPresenter:managedConfigurationHelper:rmStoreHelper:"
+ "ensureActivationWithCompletionHandler:"
+ "extensibleSSOProfileIdentifiersWithCompletionHandler:"
+ "extensionIDsFromESSOProfileIdentifiers:"
+ "filteredArrayUsingPredicate:"
+ "initWithPresenter:managedConfigurationHelper:rmStoreHelper:"
+ "initiateDEPPushTokenSyncWithCompletionHandler:"
+ "isProvisionallyEnrolledWithCloudConfig:"
+ "languageStrings"
+ "linkErSSOStoreToMDMWithProfileIdentifier:accountIdentifier:completionHandler:"
+ "localeString"
+ "predicateWithBlock:"
+ "presenter didn't implement requestUserConsentWithProfileData:managedAppleID:completionHandler:"
+ "removeErSSOStoreWithCompletionHandler:"
+ "requestDeviceErasureWithCompletionHandler:"
+ "requestSoftwareUpdateWithInfoDictionary:completionHandler:"
+ "requestUserConsentWithProfileData:managedAppleID:enrollmentType:completionHandler:"
+ "rmStoreHelper"
+ "setDirtyRMStoreForErSSO"
+ "setRmStoreHelper:"
+ "setSoftwareUpdateInfo:"
+ "softwareUpdateInfo"
+ "unassignFromDEPWithCompletionHandler:"
+ "updateCloudConfigurationWithRMAccountIdentifier:"
+ "updateLanguage:locale:completionHandler:"
+ "v52@0:8@16@24@32B40Q44"
+ "v56@0:8@16@24@32@40Q48"
+ "waitForActiveAndValidDeclarationsInErSSOStoreWithTimeout:completionHandler:"
- "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_2"
- "-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]_block_invoke_2"
- "Cannot complete reauthentication."
- "Client doesn't support isDeviceConfigured method, returning..."
- "ERROR_PROFILE_REQUIRED_APP_ID_INVALID"
- "Enrollment profile contains a required app ID that is different from the esso app's iTunes store ID. Aborting..."
- "InstallESSOConfigurationProfile"
- "Nothing to restore, continue..."
- "T@\"NSString\",&,N,V_expectedBuildVersion"
- "T@\"NSString\",&,N,V_expectedOSVersion"
- "_ADxE_MAID_firstPartSteps"
- "_ADxE_MAID_secondPartSteps_default"
- "_ADxE_MAID_secondPartSteps_orgToken"
- "_ORGO_pre_enrollment_steps"
- "_askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:"
- "_expectedBuildVersion"
- "_expectedOSVersion"
- "_promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:"
- "dmc_visibleRemoteManagementAccounts"
- "expectedBuildVersion"
- "expectedOSVersion"
- "isEqualToNumber:"
- "requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:"
- "setExpectedBuildVersion:"
- "setExpectedOSVersion:"

```
