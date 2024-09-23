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
+ _OBJC_CLASS_$_AKAccountRecoveryStepSMSVerificationCode
+ _kAKAnalyticsEventServerUIStart
+ _kAKAnalyticsEventNativeRecoveryFinish
+ _kAKAnalyticsEventNativeRecoveryStart
+ _kAKAnalyticsEventGenerateOSVersionAttestationData
+ _kAKAnalyticsEventServerUIFinish
+ _kAKAnalyticsEventSendLivenessNonce
+ _OBJC_METACLASS_$_AKCommandLineURLSession
+ _kAKAnalyticsEventRetrieveDAK
+ _kAKAnalyticsEventOSVersionAttestationRequest
+ _OBJC_METACLASS_$_AKAccountRecoveryStepiCloudSecurityCode
+ _kAKAnalyticsEventAccountRecoveryFinish
+ _OBJC_CLASS_$_AKAccountRecoveryStepVerifyPhoneNumber
+ _OBJC_METACLASS_$_AKAccountRecoveryStepVerifyPhoneNumber
+ _kAKAnalyticsEventAccountRecoveryStart
+ _OBJC_METACLASS_$_AKAccountRecoveryStepChangePassword
+ _OBJC_CLASS_$_NSXMLParser
+ _OBJC_CLASS_$_AKAccountRecoveryStepiCloudSecurityCode
+ _kAKAnalyticsEventGenerateOSBoundRefKey
+ _kAKAnalyticsEventSendAttestedOSVersion
+ _kAKAnalyticsEventUpdateRefkeyWithNonce
+ _kAKAnalyticsEventGenerateDCRT
+ _OBJC_CLASS_$_AKAccountRecoveryStepChangePassword
+ _OBJC_METACLASS_$_AKAccountRecoveryStepSMSVerificationCode
+ _OBJC_CLASS_$_AKCommandLineURLSession
CStrings:
+ "Confirm new password: "
+ "attributtes"
+ "_shouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "aaf_dictionaryByAddingEntriesFromDictionary:"
+ "AKAccountRecoveryStepSMSVerificationCode"
+ "cdpContext:promptToInformUserOfAccountLockOutWithCompletion:"
+ "B24@?0@\"NSString\"8@16"
+ "AKAccountRecoveryStepChangePassword"
+ "_isNewPasswordErrorForData:"
+ "com.apple.authkit.serverUIFinish"
+ "scnt"
+ "Your new password must be different than one of the passwords you have used in the last year."
+ "v32@0:8@\"CDPContext\"16@?<v@?B@\"NSError\">24"
+ "cdpContext:promptToInformUserOfAccountUnlockWithCompletion:"
+ "Recovered info: %!@(MISSING)"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
+ "Failed change password step with unexpected data"
+ "Passcode validated - %!d(MISSING)"
+ "cdpContext:showResetFailedAlertWithUnderlyingError:completion:"
+ "Failed sms verification step with unexpected data"
+ "com.apple.authkit.nativeRecoveryStart"
+ "cdpContext:showError:withCompletion:"
+ "button"
+ "phone number"
+ "v44@0:8@16@24B32@36"
+ "_promptForPhoneNumberWithModel:"
+ "_sendSMSCodeWithModel:completion:"
+ "cdpContext:promptForRecoveryKeyWithSecretValidator:completion:"
+ "v44@0:8@\"CDPContext\"16@\"NSArray\"24B32@\"CDPRemoteDeviceSecretValidator\"36"
+ "ak_attestationErrorWithCode:underlyingError:"
+ "RUIXMLParserDelegate"
+ "AKCommandLineURLSession"
+ "v48@0:8@\"CDPContext\"16B24@\"NSNumber\"28B36@\"CDPRemoteDeviceSecretValidator\"40"
+ "_matchingAttributesWithPhoneNumber:linkRowElements:"
+ "dismissRemoteApprovalWaitingScreenWithAction:"
+ "_verifyLocalSecretWithModel:completion:"
+ "_promptForConfirmPasswordWithModel:"
+ "com.apple.authkit.updateRefkeyWithNonce"
+ "v24@?0B8B12@\"NSError\"16"
+ "new password"
+ "_verifyRemoteSecretWithRecoveryContext:recoveredInfo:recoveryError:model:completion:"
+ "com.apple.authkit.serverUIStart"
+ "Sign Out"
+ "v40@0:8@\"CDPContext\"16@\"NSError\"24@?<v@?q>32"
+ "alert"
+ "cdpContext:presentRecoveryKeyWithValidator:completion:"
+ "Failed verify security code step with unexpected data"
+ "Enter verification code: "
+ "linkRow"
+ "cdpContext:promptForBeneficiaryAccessKeyWithCompletion:"
+ "_verifyNewPasswordWithRowID:confirmRowID:model:completion:"
+ "xmlElement"
+ "Failed verify security code step. Unsupported recovery method."
+ "cdpContext:presentRemoteApprovalWithCompletion:"
+ "presentQuotaScreenWithCompletion:"
+ "Enter new password: "
+ "editableTextRow"
+ "initWithData:"
+ "Failed to change password. Error - %!@(MISSING)"
+ "_promptForRecoveryKeyWithModel:"
+ "v48@0:8@16B24@28B36@40"
+ "cdpContext:promptForAdoptionOfMultipleICSC:"
+ "sharedServerUIURLSession"
+ "cdpRecoveryFlowContext:promptForRemoteSecretWithDevices:validator:"
+ "Enter device passcode: "
+ "Enter one of your trusted phone numbers to continue: "
+ "_promptForPasscodeWithModel:"
+ "cdpContext:promptForRemoteSecretWithDevices:offeringRemoteApproval:validator:"
+ "validateSecret:devices:type:withCompletion:"
+ "com.apple.authkit.generateOSBoundRefKey"
+ "TB,N,V_shouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "CDPStateUIProvider"
+ "com.apple.authkit.sendLivenessNonce"
+ "Received nil flowId in AKAppleIDAuthenticationContext"
+ "confirmRecoveryKey:completion:"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"CDPLocalSecret\"@\"NSError\">24"
+ "cdpContext:promptForLocalSecretWithCompletion:"
+ "validateRecoveryKey:withCompletion:"
+ "_processPhoneNumber:response:model:completion:"
+ "forgotpasscode"
+ "_promptForCountryCode"
+ "cdpContext:promptForRecoveryKeyWithValidator:completion:"
+ "_verifyPinViewWithResponse:model:completion:"
+ "Country code for this account: "
+ "com.apple.authkit.osVersionAttestationReq"
+ "_beginICloudSecurityCodeWithResponse:model:completion:"
+ "com.apple.authkit.nativeRecoveryFinish"
+ "set_shouldRequestToArmDeviceToAllowPCSKeyUpload:"
+ "choose different password"
+ "parse"
+ "passcode"
+ "linkBarItem"
+ "com.apple.authkit.generateOSVersionAttestationData"
+ "T@\"NSString\",C,N,V_countryCode"
+ "v32@0:8@\"CDPContext\"16@?<v@?Q@\"NSError\">24"
+ "AKAccountRecoveryStepiCloudSecurityCode"
+ "v48@0:8@\"CDPContext\"16@\"NSError\"24q32@?<v@?q>40"
+ "_matchingAttributeWithResponse:"
+ "cdpContext:createLocalSecretWithCompletion:"
+ "Recovery context is invalid..."
+ "v40@0:8@\"CDPContext\"16@\"<CDPRemoteDeviceSecretValidatorProtocol>\"24@?<v@?B@\"NSError\">32"
+ "_verifyPhoneNumberWithModel:completion:"
+ "com.apple.authkit.accountRecoveryStart"
+ "Enter recovery key: "
+ "v32@0:8@\"CDPContext\"16@?<v@?>24"
+ "\x11\x1c"
+ "Redirect session is missing continuation header's."
+ "cdpContext:showResetCompletedAlertWithCompletion:"
+ "pinView"
+ "Password changed successfully."
+ "_beginSMSCodeVerificationWithResponse:model:completion:"
+ "_countryCode"
+ "CDPRecoveryKeyUIProvider"
+ "cdpContext:promptForICSCWithIsNumeric:numericLength:isRandom:validator:"
+ "_beginChangePasswordWithResponse:model:completion:"
+ "v24@0:8@?<v@?B@\"CDPLocalSecret\">16"
+ "ak_analyticsEventWithContext:eventName:error:"
+ "v40@0:8@\"CDPContext\"16@\"<CDPRecoveryKeyValidator>\"24@?<v@?B@\"NSError\">32"
+ "ShouldRequestToArmDeviceToAllowPCSKeyUpload"
+ "com.apple.authkit.generateDCRT"
+ "AKAccountRecoveryStepVerifyPhoneNumber"
+ "<%!@(MISSING): %!p(MISSING) {\n\taltDSID: %!@(MISSING),\n\tproxiedAppName: %!@(MISSING),\n\tserviceType: %!@(MISSING),\n\tproxiedDevice: %!@(MISSING),\n\tcompanionDevice: %!@(MISSING),\n\tappProvidedData: %!@(MISSING),\n\tteamID: %!@(MISSING),\n\tappID: %!@(MISSING),\n\trequest: %!@(MISSING),\n\tappProvidedContext: %!@(MISSING),\n\tuserSelection: %!@(MISSING),\n\tclientAuthenticatedExternallyWithPassword: %!@(MISSING),\n\tisAuthorizingForSharedSIWAAccount: %!@(MISSING),\n\t_shouldRequestToArmDeviceToAllowPCSKeyUpload: %!@(MISSING),\n}>"
+ "com.apple.authkit.retrieveDAK"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"AKInheritanceAccessKey\"@\"NSError\">24"
+ "cdpContext:promptForInteractiveAuthenticationWithCompletion:"
+ "_verifyRemoteSecretWithServerInfo:model:completion:"
+ "verification code"
+ "Failed phone number verification step with unexpected data"
+ "Failed verify security code step with error - %!@(MISSING)"
+ "v40@0:8@\"CDPContext\"16@\"NSError\"24@?<v@?Q@\"NSError\">32"
+ "cdpContext:showError:withDefaultIndex:withCompletion:"
+ "Session processing redirect from %!@(MISSING) to %!@(MISSING)"
+ "com.apple.authkit.accountRecoveryFinish"
+ "_promptForSMSCode"
+ "RK validated - %!d(MISSING)"
+ "com.apple.authkit.sendAttestedOSVersion"
+ "_beginVerifyPhoneNumberWithResponse:model:completion:"
+ "v40@0:8@\"CDPRecoveryFlowContext\"16@\"NSArray\"24@\"CDPRemoteDeviceSecretValidator\"32"
+ "_verifySMSCodeWithData:model:completion:"
+ "_verifyClientInfoWithResponse:model:completion:"
+ "setCountryCode:"
+ "change password"
+ "@\"AKAccountRecoveryModel\""
+ "_promptForNewPasswordWithModel:"
- "\x11\x1b"
- "<%!@(MISSING): %!p(MISSING) {\n\taltDSID: %!@(MISSING),\n\tproxiedAppName: %!@(MISSING),\n\tserviceType: %!@(MISSING),\n\tproxiedDevice: %!@(MISSING),\n\tcompanionDevice: %!@(MISSING),\n\tappProvidedData: %!@(MISSING),\n\tteamID: %!@(MISSING),\n\tappID: %!@(MISSING),\n\trequest: %!@(MISSING),\n\tappProvidedContext: %!@(MISSING),\n\tuserSelection: %!@(MISSING),\n\tclientAuthenticatedExternallyWithPassword: %!@(MISSING),\n\tisAuthorizingForSharedSIWAAccount: %!@(MISSING),\n}>"
- "Failed to save account with error: %!@(MISSING)"

```
