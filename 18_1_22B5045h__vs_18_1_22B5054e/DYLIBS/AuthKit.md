## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.100.2.0.0
-  __TEXT.__text: 0xc8118
+493.100.4.0.0
+  __TEXT.__text: 0xcc930
   __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0xafc8
+  __TEXT.__objc_methlist: 0xb258
   __TEXT.__const: 0x2121
-  __TEXT.__cstring: 0xd111
-  __TEXT.__oslogstring: 0x10009
-  __TEXT.__gcc_except_tab: 0x5174
+  __TEXT.__cstring: 0xd5f3
+  __TEXT.__oslogstring: 0x10216
+  __TEXT.__gcc_except_tab: 0x5184
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x3930
-  __TEXT.__objc_classname: 0x1862
-  __TEXT.__objc_methname: 0x1e6c8
-  __TEXT.__objc_methtype: 0x3ed1
-  __TEXT.__objc_stubs: 0xd640
-  __DATA_CONST.__got: 0x950
-  __DATA_CONST.__const: 0x5018
-  __DATA_CONST.__objc_classlist: 0x550
+  __TEXT.__unwind_info: 0x3a10
+  __TEXT.__objc_classname: 0x1942
+  __TEXT.__objc_methname: 0x1f115
+  __TEXT.__objc_methtype: 0x4283
+  __TEXT.__objc_stubs: 0xdbe0
+  __DATA_CONST.__got: 0x988
+  __DATA_CONST.__const: 0x5198
+  __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x1c8
+  __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62e0
+  __DATA_CONST.__objc_selrefs: 0x6460
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x360
-  __DATA_CONST.__objc_arraydata: 0x138
+  __DATA_CONST.__objc_arraydata: 0x148
   __AUTH_CONST.__auth_got: 0x6c8
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x1050
-  __AUTH_CONST.__cfstring: 0xd9c0
-  __AUTH_CONST.__objc_const: 0x22de8
+  __AUTH_CONST.__const: 0x10b0
+  __AUTH_CONST.__cfstring: 0xdee0
+  __AUTH_CONST.__objc_const: 0x24290
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH.__objc_data: 0x1928
-  __DATA.__objc_ivar: 0xe8c
-  __DATA.__data: 0x15a0
-  __DATA.__bss: 0x620
+  __AUTH_CONST.__objc_dictobj: 0x190
+  __AUTH.__objc_data: 0x1ab8
+  __DATA.__objc_ivar: 0xe9c
+  __DATA.__data: 0x1660
+  __DATA.__bss: 0x630
   __DATA_DIRTY.__objc_data: 0x1bf8
-  __DATA_DIRTY.__bss: 0x238
+  __DATA_DIRTY.__bss: 0x240
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5568
-  Symbols:   7543
-  CStrings:  8722
+  Functions: 5652
+  Symbols:   7676
+  CStrings:  8864
 
Symbols:
+ _OBJC_METACLASS_$_AKAccountRecoveryStepSMSVerificationCode
+ _kAKAnalyticsEventNativeRecoveryFinish
+ _kAKAnalyticsEventRetrieveDAK
+ _OBJC_METACLASS_$_AKAccountRecoveryStepiCloudSecurityCode
+ _kAKAnalyticsEventSendAttestedOSVersion
+ _OBJC_CLASS_$_AKCommandLineURLSession
+ _OBJC_METACLASS_$_AKAccountRecoveryStepVerifyPhoneNumber
+ _kAKAnalyticsEventOSVersionAttestationRequest
+ _kAKAnalyticsEventServerUIStart
+ _kAKAnalyticsEventGenerateDCRT
+ _OBJC_CLASS_$_AKAccountRecoveryStepChangePassword
+ _kAKAnalyticsEventGenerateOSVersionAttestationData
+ _kAKAnalyticsEventNativeRecoveryStart
+ _OBJC_CLASS_$_AKAccountRecoveryStepSMSVerificationCode
+ _OBJC_METACLASS_$_AKCommandLineURLSession
+ _OBJC_CLASS_$_AKAccountRecoveryStepiCloudSecurityCode
+ _kAKAnalyticsEventAccountRecoveryFinish
+ _OBJC_CLASS_$_NSXMLParser
+ _kAKAnalyticsEventSendLivenessNonce
+ _kAKAnalyticsEventGenerateOSBoundRefKey
+ _OBJC_METACLASS_$_AKAccountRecoveryStepChangePassword
+ _OBJC_CLASS_$_AKAccountRecoveryStepVerifyPhoneNumber
+ _kAKAnalyticsEventAccountRecoveryStart
+ _kAKAnalyticsEventUpdateRefkeyWithNonce
+ _kAKAnalyticsEventServerUIFinish
CStrings:
+ "_verifySMSCodeWithData:model:completion:"
+ "Recovery context is invalid..."
+ "forgotpasscode"
+ "cdpContext:promptForInteractiveAuthenticationWithCompletion:"
+ "set_shouldRequestToArmDeviceToAllowPCSKeyUpload:"
+ "_verifyPhoneNumberWithModel:completion:"
+ "AKAccountRecoveryStepChangePassword"
+ "initWithData:"
+ "ShouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "v44@0:8@\"CDPContext\"16@\"NSArray\"24B32@\"CDPRemoteDeviceSecretValidator\"36"
+ "v44@0:8@16@24B32@36"
+ "phone number"
+ "_verifyRemoteSecretWithRecoveryContext:recoveredInfo:recoveryError:model:completion:"
+ "com.apple.authkit.generateDCRT"
+ "_promptForPasscodeWithModel:"
+ "com.apple.authkit.osVersionAttestationReq"
+ "alert"
+ "com.apple.authkit.generateOSBoundRefKey"
+ "new password"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "cdpContext:promptForBeneficiaryAccessKeyWithCompletion:"
+ "AKAccountRecoveryStepVerifyPhoneNumber"
+ "attributtes"
+ "Failed phone number verification step with unexpected data"
+ "v40@0:8@\"CDPContext\"16@\"<CDPRemoteDeviceSecretValidatorProtocol>\"24@?<v@?B@\"NSError\">32"
+ "Failed to change password. Error - %!@(MISSING)"
+ "Enter one of your trusted phone numbers to continue: "
+ "Session processing redirect from %!@(MISSING) to %!@(MISSING)"
+ "com.apple.authkit.nativeRecoveryFinish"
+ "Received nil flowId in AKAppleIDAuthenticationContext"
+ "linkRow"
+ "ak_attestationErrorWithCode:underlyingError:"
+ "parse"
+ "com.apple.authkit.sendAttestedOSVersion"
+ "cdpContext:showError:withDefaultIndex:withCompletion:"
+ "CDPStateUIProvider"
+ "cdpContext:promptToInformUserOfAccountUnlockWithCompletion:"
+ "aaf_dictionaryByAddingEntriesFromDictionary:"
+ "v32@0:8@\"CDPContext\"16@?<v@?Q@\"NSError\">24"
+ "linkBarItem"
+ "cdpContext:createLocalSecretWithCompletion:"
+ "Your new password must be different than one of the passwords you have used in the last year."
+ "\x11\x1c"
+ "validateRecoveryKey:withCompletion:"
+ "pinView"
+ "com.apple.authkit.nativeRecoveryStart"
+ "Failed sms verification step with unexpected data"
+ "editableTextRow"
+ "Enter new password: "
+ "@\"AKAccountRecoveryModel\""
+ "_promptForPhoneNumberWithModel:"
+ "Failed verify security code step. Unsupported recovery method."
+ "cdpContext:showError:withCompletion:"
+ "presentQuotaScreenWithCompletion:"
+ "AKAccountRecoveryStepSMSVerificationCode"
+ "AKCommandLineURLSession"
+ "com.apple.authkit.accountRecoveryStart"
+ "verification code"
+ "ak_analyticsEventWithContext:eventName:error:"
+ "_verifyClientInfoWithResponse:model:completion:"
+ "v40@0:8@\"CDPRecoveryFlowContext\"16@\"NSArray\"24@\"CDPRemoteDeviceSecretValidator\"32"
+ "Passcode validated - %!d(MISSING)"
+ "AKAccountRecoveryStepiCloudSecurityCode"
+ "scnt"
+ "Failed verify security code step with unexpected data"
+ "validateSecret:devices:type:withCompletion:"
+ "v48@0:8@\"CDPContext\"16@\"NSError\"24q32@?<v@?q>40"
+ "v48@0:8@\"CDPContext\"16B24@\"NSNumber\"28B36@\"CDPRemoteDeviceSecretValidator\"40"
+ "Failed change password step with unexpected data"
+ "_shouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "cdpContext:promptForRecoveryKeyWithSecretValidator:completion:"
+ "cdpContext:promptToInformUserOfAccountLockOutWithCompletion:"
+ "cdpContext:promptForLocalSecretWithCompletion:"
+ "_beginChangePasswordWithResponse:model:completion:"
+ "v24@0:8@?<v@?B@\"CDPLocalSecret\">16"
+ "_promptForCountryCode"
+ "cdpContext:presentRecoveryKeyWithValidator:completion:"
+ "_matchingAttributesWithPhoneNumber:linkRowElements:"
+ "B24@?0@\"NSString\"8@16"
+ "_promptForNewPasswordWithModel:"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"AKInheritanceAccessKey\"@\"NSError\">24"
+ "cdpContext:promptForICSCWithIsNumeric:numericLength:isRandom:validator:"
+ "T@\"NSString\",C,N,V_countryCode"
+ "Password changed successfully."
+ "_verifyRemoteSecretWithServerInfo:model:completion:"
+ "Failed verify security code step with error - %!@(MISSING)"
+ "_beginVerifyPhoneNumberWithResponse:model:completion:"
+ "v32@0:8@\"CDPContext\"16@?<v@?>24"
+ "Redirect session is missing continuation header's."
+ "_matchingAttributeWithResponse:"
+ "v24@?0B8B12@\"NSError\"16"
+ "CDPRecoveryKeyUIProvider"
+ "_isNewPasswordErrorForData:"
+ "_verifyPinViewWithResponse:model:completion:"
+ "cdpContext:showResetCompletedAlertWithCompletion:"
+ "dismissRemoteApprovalWaitingScreenWithAction:"
+ "cdpContext:promptForAdoptionOfMultipleICSC:"
+ "Confirm new password: "
+ "_verifyNewPasswordWithRowID:confirmRowID:model:completion:"
+ "cdpContext:showResetFailedAlertWithUnderlyingError:completion:"
+ "_promptForSMSCode"
+ "com.apple.authkit.serverUIStart"
+ "v40@0:8@\"CDPContext\"16@\"<CDPRecoveryKeyValidator>\"24@?<v@?B@\"NSError\">32"
+ "cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:"
+ "cdpRecoveryFlowContext:promptForRemoteSecretWithDevices:validator:"
+ "com.apple.authkit.serverUIFinish"
+ "_processPhoneNumber:response:model:completion:"
+ "com.apple.authkit.updateRefkeyWithNonce"
+ "cdpContext:promptForRecoveryKeyWithValidator:completion:"
+ "confirmRecoveryKey:completion:"
+ "com.apple.authkit.sendLivenessNonce"
+ "passcode"
+ "button"
+ "v48@0:8@16B24@28B36@40"
+ "change password"
+ "_sendSMSCodeWithModel:completion:"
+ "RK validated - %!d(MISSING)"
+ "v40@0:8@\"CDPContext\"16@\"NSError\"24@?<v@?q>32"
+ "TB,N,V_shouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "Country code for this account: "
+ "_beginICloudSecurityCodeWithResponse:model:completion:"
+ "v40@0:8@\"CDPContext\"16@\"NSError\"24@?<v@?Q@\"NSError\">32"
+ "<%!@(MISSING): %!p(MISSING) {\n\taltDSID: %!@(MISSING),\n\tproxiedAppName: %!@(MISSING),\n\tserviceType: %!@(MISSING),\n\tproxiedDevice: %!@(MISSING),\n\tcompanionDevice: %!@(MISSING),\n\tappProvidedData: %!@(MISSING),\n\tteamID: %!@(MISSING),\n\tappID: %!@(MISSING),\n\trequest: %!@(MISSING),\n\tappProvidedContext: %!@(MISSING),\n\tuserSelection: %!@(MISSING),\n\tclientAuthenticatedExternallyWithPassword: %!@(MISSING),\n\tisAuthorizingForSharedSIWAAccount: %!@(MISSING),\n\t_shouldRequestToArmDeviceToAllowPCSKeyUpload: %!@(MISSING),\n}>"
+ "_promptForRecoveryKeyWithModel:"
+ "Sign Out"
+ "cdpContext:presentRemoteApprovalWithCompletion:"
+ "RUIXMLParserDelegate"
+ "Enter recovery key: "
+ "Recovered info: %!@(MISSING)"
+ "Enter verification code: "
+ "v32@0:8@\"CDPContext\"16@?<v@?B@\"NSError\">24"
+ "_promptForConfirmPasswordWithModel:"
+ "_verifyLocalSecretWithModel:completion:"
+ "com.apple.authkit.accountRecoveryFinish"
+ "sharedServerUIURLSession"
+ "com.apple.authkit.generateOSVersionAttestationData"
+ "xmlElement"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"CDPLocalSecret\"@\"NSError\">24"
+ "Enter device passcode: "
+ "_countryCode"
+ "com.apple.authkit.retrieveDAK"
+ "choose different password"
+ "_beginSMSCodeVerificationWithResponse:model:completion:"
+ "setCountryCode:"
- "<%!@(MISSING): %!p(MISSING) {\n\taltDSID: %!@(MISSING),\n\tproxiedAppName: %!@(MISSING),\n\tserviceType: %!@(MISSING),\n\tproxiedDevice: %!@(MISSING),\n\tcompanionDevice: %!@(MISSING),\n\tappProvidedData: %!@(MISSING),\n\tteamID: %!@(MISSING),\n\tappID: %!@(MISSING),\n\trequest: %!@(MISSING),\n\tappProvidedContext: %!@(MISSING),\n\tuserSelection: %!@(MISSING),\n\tclientAuthenticatedExternallyWithPassword: %!@(MISSING),\n\tisAuthorizingForSharedSIWAAccount: %!@(MISSING),\n}>"
- "\x11\x1b"
- "Failed to save account with error: %!@(MISSING)"

```
