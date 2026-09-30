## DMCEnrollmentLibrary

> `/System/Library/PrivateFrameworks/DMCEnrollmentLibrary.framework/DMCEnrollmentLibrary`

```diff

-5.2.7.0.0
-  __TEXT.__text: 0x18ca8
+20.4.16.0.0
+  __TEXT.__text: 0x1ea44
   __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_methlist: 0xfa8
+  __TEXT.__objc_methlist: 0x1160
   __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0x22ab
-  __TEXT.__cstring: 0x19dd
-  __TEXT.__gcc_except_tab: 0x6b0
+  __TEXT.__oslogstring: 0x25b5
+  __TEXT.__cstring: 0x1ad4
+  __TEXT.__gcc_except_tab: 0x820
   __TEXT.__dlopen_cstrs: 0xae
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__unwind_info: 0x6c8
   __TEXT.__objc_classname: 0xf5
-  __TEXT.__objc_methname: 0x5994
-  __TEXT.__objc_methtype: 0x587
-  __TEXT.__objc_stubs: 0x4420
-  __DATA_CONST.__got: 0x348
-  __DATA_CONST.__const: 0xc98
+  __TEXT.__objc_methname: 0x623c
+  __TEXT.__objc_methtype: 0x5e5
+  __TEXT.__objc_stubs: 0x4b20
+  __DATA_CONST.__got: 0x350
+  __DATA_CONST.__const: 0xd58
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1220
+  __DATA_CONST.__objc_selrefs: 0x13f0
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__objc_arraydata: 0x5f8
+  __DATA_CONST.__objc_arraydata: 0x2f0
   __AUTH_CONST.__auth_got: 0x2a8
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x1030
-  __AUTH_CONST.__objc_intobj: 0x600
-  __AUTH_CONST.__objc_arrayobj: 0x360
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x10a0
+  __AUTH_CONST.__objc_const: 0x1040
+  __AUTH_CONST.__objc_intobj: 0x6a8
+  __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_dictobj: 0x28
   __DATA.__objc_ivar: 0xf4
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x1c8
   __DATA_DIRTY.__objc_data: 0x230
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 462
-  Symbols:   676
-  CStrings:  1138
+  Functions: 540
+  Symbols:   762
+  CStrings:  1227
 
Symbols:
+ _OBJC_CLASS_$_NSPredicate
+ _kCCRemoteManagementAccountIdentifierKey
+ _kDMCErrorDetailsSUInfoKey
+ _kRMBridgeAppStoreIDKey
+ _kRMBridgeBundleIDKey
- _kDMCErrorDetailsBuildVersionKey
- _kDMCErrorDetailsOSVersionKey
CStrings:
+ "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:enrollmentType:]_block_invoke_7"
+ "-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithSoftwareUpdateInfo:]_block_invoke_2"
+ "-[DMCEnrollmentFlowController _restoreLanguage:locale:]_block_invoke_2"
+ "1\x17\x12\x13\x1f\a"
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
+ "ErSSO declaration AppIDs do not match: %{public}@ and %{public}@"
+ "ErSSO declaration AppStoreIDs do not match: %{public}@ and %{public}@"
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
+ "Invalid ErSSO declarations: %{public}@"
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
+ "appDetailsFromDeclarations:error:"
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
+ "isEqualToSet:"
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
- "-[DMCEnrollmentFlowController _askForUserConsentWithProfileData:managedAppleID:cloudConfig:isReturnToService:]_block_invoke_3"
- "-[DMCEnrollmentFlowController _promptForSoftwareUpdateWithExpectedOSVersion:expectedBuildVersion:]_block_invoke_2"
- "1\x16\x12\x13\x1f\b"
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
- "requestSoftwareUpdateWithOSVersion:buildVersion:completionHandler:"
- "setExpectedBuildVersion:"
- "setExpectedOSVersion:"

```
