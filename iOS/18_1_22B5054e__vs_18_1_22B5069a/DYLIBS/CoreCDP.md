## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-386.100.11.2.0
-  __TEXT.__text: 0x4b95c
-  __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_methlist: 0x2b34
+386.100.23.0.0
+  __TEXT.__text: 0x51238
+  __TEXT.__auth_stubs: 0x1070
+  __TEXT.__objc_methlist: 0x2e30
   __TEXT.__const: 0x1124
-  __TEXT.__gcc_except_tab: 0x10fc
-  __TEXT.__oslogstring: 0x8226
-  __TEXT.__cstring: 0x5098
+  __TEXT.__gcc_except_tab: 0x126c
+  __TEXT.__oslogstring: 0x8f72
+  __TEXT.__cstring: 0x5a58
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1340
-  __TEXT.__objc_classname: 0x6eb
-  __TEXT.__objc_methname: 0x83f8
-  __TEXT.__objc_methtype: 0x19d3
-  __TEXT.__objc_stubs: 0x49e0
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x2c68
-  __DATA_CONST.__objc_classlist: 0x198
-  __DATA_CONST.__objc_catlist: 0x28
+  __TEXT.__unwind_info: 0x1468
+  __TEXT.__objc_classname: 0x705
+  __TEXT.__objc_methname: 0x8f59
+  __TEXT.__objc_methtype: 0x1ca0
+  __TEXT.__objc_stubs: 0x4ea0
+  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__const: 0x2e98
+  __DATA_CONST.__objc_classlist: 0x1a0
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dd8
+  __DATA_CONST.__objc_selrefs: 0x2000
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x90
-  __AUTH_CONST.__auth_got: 0x810
+  __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x530
-  __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x96d0
+  __AUTH_CONST.__const: 0x550
+  __AUTH_CONST.__cfstring: 0x3c00
+  __AUTH_CONST.__objc_const: 0x9df0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2bc
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x2f8
   __DATA.__data: 0x1038
-  __DATA.__bss: 0x111
+  __DATA.__bss: 0x129
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x960
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0x98
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1889
-  Symbols:   2683
-  CStrings:  2991
+  Functions: 2006
+  Symbols:   2853
+  CStrings:  3252
 
Symbols:
+ _AKEDPStateKey
+ _AKPasswordVersionKey
+ _AKSRPIterationCountKey
+ _AKSRPProtocolKey
+ _AKSRPSaltKey
+ _CDPEDPCofigKey
+ _CDPEDPTokenKey
+ _CDPEDPTokenMediumKey
+ _CDPEDPTokenTitleKey
+ _CDPReplaceEDPTokens
+ _CDP_FOLLOWUP_CDP_EDP_REPAIR
+ _CDP_FOLLOWUP_EDP_ONLY_REPAIR
+ _OBJC_CLASS_$_AKGlobalConfig
+ _OBJC_CLASS_$_CDPEDPConfigProvider
+ _OBJC_METACLASS_$_CDPEDPConfigProvider
+ _PCSGuitarfishChangePassword
+ _PCSGuitarfishGetRecoveryTokenInfo
+ _PCSGuitarfishRepairIdentities
+ _PCSGuitarfishResetProtectedData
+ _PCSGuitarfishSetupIdentities
+ _PCSGuitarfishValidateIdentities
+ _SecureBackupIsGuitarfishEnabled
+ _kCDPAnalyticsEDPChangePasswordEvent
+ _kCDPAnalyticsEDPEligibility
+ _kCDPAnalyticsEDPHealth
+ _kCDPAnalyticsEDPPasswordValidationEvent
+ _kCDPAnalyticsEDPRecoveryTokenDontHaveKeyAlertEscapeOptionTappedEvent
+ _kCDPAnalyticsEDPRecoveryTokenDontHaveKeyAlertPresentedEvent
+ _kCDPAnalyticsEDPRecoveryTokenEntryScreenEscapeOptionTappedEvent
+ _kCDPAnalyticsEDPRecoveryTokenEntryScreenLandingEvent
+ _kCDPAnalyticsEDPRecoveryTokenFetchEvent
+ _kCDPAnalyticsEDPRecoveryTokenInformationalScreenEscapeOptionTappedEvent
+ _kCDPAnalyticsEDPRecoveryTokenInformationalScreenLandingEvent
+ _kCDPAnalyticsEDPRecoveryTokenValidationEvent
+ _kCDPAnalyticsEDPRepairFinishEvent
+ _kCDPAnalyticsEDPRepairStartEvent
+ _kCDPAnalyticsEDPResetProtectedDataEvent
+ _kCDPAnalyticsEDPSendRecoveryTokenEvent
+ _kCDPAnalyticsEDPSetupIdentitiesEvent
+ _kCDPAnalyticsEDPSpyglassPaneEmailButtonTappedEvent
+ _kCDPAnalyticsEDPSpyglassPaneLandingEvent
+ _kCDPEventCountry
+ _kEDPDataAccessDontHaveDataAccessKey
+ _kEDPDataAccessDontHaveKey
+ _kEDPDataAccessTryAgainLater
+ _kPCSSetupRawPassword
CStrings:
+ "\x02v\x13!\x15u'"
+ "\x06"
+ "\tInteractive Auth Button String: %!@(MISSING)\n"
+ "\tedpState: %!l(MISSING)d\n"
+ "\tforceInteractiveCDPEDPRepair: %!d(MISSING)\n"
+ "\toldPassword is %!@(MISSING) missing\n"
+ "\tpassword is %!@(MISSING) missing\n"
+ "\tpasswordVersion: %!@(MISSING)\n"
+ "\tsrpIteration is %!@(MISSING) missing\n"
+ "\tsrpProtocol is %!@(MISSING) missing\n"
+ "\tsrpSalt is %!@(MISSING) missing\n"
+ "\x13"
+ "\"%!s(MISSING) in CDPStateUIProviderProxy: Failed to prompt for EDP recovery token due to incomplete UI provider\""
+ "\"%!s(MISSING): Calling into daemon validator to repair EDP state\""
+ "\"%!s(MISSING): Calling into daemon validator to validate recovery token\""
+ "\"Attempted to prompt for EDP recovery token while in beneficiary flow. Doing nothing.\""
+ "\"CLI: Enter the recovery code provided by your custodian...\""
+ "\"CLI: Entered recovery code: %!@(MISSING)\""
+ "\"CLI: Recovery code validated. Validating recovery info...\""
+ "\"CLI: Reenter the recovery code provided by your custodian...\""
+ "\"CLI: Reentered recovery code: %!@(MISSING)\""
+ "\"CLI: The recovery code is not valid\""
+ "\"CLI: Validate recovery code failed with error: %!@(MISSING)\""
+ "\"CLI: Validating the recovery code...\""
+ "\"Checking for EDP health status\""
+ "\"Creating EDP liveness health payload...\""
+ "\"Creating context for CDP & EDP Repair CFU\""
+ "\"Creating context for DSID %!{(MISSING)mask.hash}@\""
+ "\"Creating context for EDP Only Repair CFU\""
+ "\"EDP config is not a dictionary\""
+ "\"EDP repair completed didRepair=%!{(MISSING)BOOL}d error=%!@(MISSING)\""
+ "\"Error getting cached EDP config. Error - %!@(MISSING)\""
+ "\"Error getting fresh EDP config. Error - %!@(MISSING)\""
+ "\"Failed to validate EDP identities with error: %!@(MISSING)\""
+ "\"Failed to validate EDP identities: %!{(MISSING)public}@, healthState: %!l(MISSING)d\""
+ "\"Failed to validate token with error: %!@(MISSING)\""
+ "\"Fetching EDP Token...\""
+ "\"Guitarfish Enabled: %!{(MISSING)BOOL}d\""
+ "\"No EDP config found in global config.\""
+ "\"No account found for DSID %!{(MISSING)mask.hash}@\""
+ "\"Recovery token was valid!\""
+ "\"Requesting repair of EDP state...\""
+ "\"Uploading EDP Token...\""
+ "\"XPC Error while creating EDP liveness health payload: %!@(MISSING)\""
+ "\"XPC Error while repairing EDP state: %!@(MISSING)\""
+ "\"_context.altDSID exists. Passing to PCS...\""
+ "\"_context.altDSID is nil.\""
+ "-"
+ "-[CDPRemoteDeviceSecretValidator repairEDPStateWithContext:completion:]"
+ "-[CDPRemoteDeviceSecretValidator validateEDPRecoveryToken:withContext:completion:]"
+ "-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]"
+ "-[CDPStateUIProviderProxy cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:]_block_invoke"
+ "A recovery token is required to repair EDP"
+ "BEGIN [%!l(MISSING)ld]: GuitarfishChangePassword  enableTelemetry=YES "
+ "BEGIN [%!l(MISSING)ld]: GuitarfishGetRecoveryTokenInfo  enableTelemetry=YES "
+ "BEGIN [%!l(MISSING)ld]: GuitarfishRepair  enableTelemetry=YES "
+ "BEGIN [%!l(MISSING)ld]: GuitarfishResetProtectedData  enableTelemetry=YES "
+ "BEGIN [%!l(MISSING)ld]: GuitarfishSetup  enableTelemetry=YES "
+ "BEGIN [%!l(MISSING)ld]: GuitarfishValidate  enableTelemetry=YES "
+ "BEGIN [%!l(MISSING)ld]: RepairEDPState  enableTelemetry=YES "
+ "CDPEDPConfigProvider"
+ "EDP_RECOVERY_KEY"
+ "EDP_RECOVERY_KEY_MEDIUM"
+ "EDP_RECOVERY_KEY_TITLECASE"
+ "END [%!l(MISSING)ld] %!f(MISSING)s: GuitarfishChangePassword  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "END [%!l(MISSING)ld] %!f(MISSING)s: GuitarfishGetRecoveryTokenInfo  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "END [%!l(MISSING)ld] %!f(MISSING)s: GuitarfishRepair  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "END [%!l(MISSING)ld] %!f(MISSING)s: GuitarfishResetProtectedData  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "END [%!l(MISSING)ld] %!f(MISSING)s: GuitarfishSetup  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "END [%!l(MISSING)ld] %!f(MISSING)s: GuitarfishValidate  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "END [%!l(MISSING)ld] %!f(MISSING)s: RepairEDPState  Error=%!{(MISSING)public,signpost.telemetry:number1,name=Error}d "
+ "GuitarfishChangePassword"
+ "GuitarfishGetRecoveryTokenInfo"
+ "GuitarfishRepair"
+ "GuitarfishResetProtectedData"
+ "GuitarfishSetup"
+ "GuitarfishValidate"
+ "Localizable-EDP"
+ "NOT"
+ "RepairEDPState"
+ "T@\"NSData\",C,N"
+ "T@\"NSData\",C,N,V_srpSalt"
+ "T@\"NSNumber\",C,N,V_passwordVersion"
+ "T@\"NSNumber\",C,N,V_srpIteration"
+ "T@\"NSString\",&,N,V_edpRecoveryToken"
+ "T@\"NSString\",C,N,V_interactiveAuthDefaultButtonString"
+ "T@\"NSString\",C,N,V_recoveryToken"
+ "T@\"NSString\",C,N,V_srpProtocol"
+ "T@\"NSString\",C,V_tokenName"
+ "T@\"NSString\",C,V_tokenNameMedium"
+ "T@\"NSString\",C,V_tokenNameTitle"
+ "TB,N,V__alwaysPromptForEDPRecoveryToken"
+ "TB,N,V__forceEDPReset"
+ "TB,N,V_forceInteractiveCDPEDPRepair"
+ "TB,V_fetchCompleted"
+ "TQ,N,V_edpHealth"
+ "TQ,N,V_edpState"
+ "__PRETTY_FUNCTION__ \": Rejecting out-of-range EDP state (%!@(MISSING)).\""
+ "__PRETTY_FUNCTION__ \": Unable to obtain the edpStateForAccount because AKAccountManager (%!@(MISSING)) doesn't respond to selector.\""
+ "__PRETTY_FUNCTION__ \": Unable to obtain the passwordVersionForAccount because AKAccountManager (%!@(MISSING)) doesn't respond to selector.\""
+ "__PRETTY_FUNCTION__ \": Unable to obtain the srpProtocolForAccount because AKAccountManager (%!@(MISSING)) doesn't respond to selector.\""
+ "__alwaysPromptForEDPRecoveryToken"
+ "__forceEDPReset"
+ "_alwaysPromptForEDPRecoveryToken"
+ "_edpHealth"
+ "_edpRecoveryToken"
+ "_edpState"
+ "_extractTokenNameFromConfig:finalize:"
+ "_fetchCompleted"
+ "_forceEDPReset"
+ "_forceInteractiveCDPEDPRepair"
+ "_interactiveAuthDefaultButtonString"
+ "_parseEDPStateFromRawState:"
+ "_passwordVersion"
+ "_rawEDPHealthForAccount:"
+ "_recoveryToken"
+ "_srpIteration"
+ "_srpProtocol"
+ "_srpSalt"
+ "_tokenName"
+ "_tokenNameMedium"
+ "_tokenNameTitle"
+ "_updateEDPAttributesFromAccountCache"
+ "_updateEDPAttributesFromAccountCacheWithAccount:"
+ "_updateEDPWithAuthenticationResults:"
+ "cdp/edp-health-liveness-payload"
+ "cdp/edp-health-status"
+ "cdp/edp-state-repair"
+ "cdp/fetch-edp-token"
+ "cdp/upload-edp-token"
+ "cdpContext:promptForEDPRecoveryTokenWithValidator:successfulCDPRecoveryContinuationHandler:"
+ "cdp_indicatesEDPRecoveryTokenIsNeeded"
+ "com.apple.corecdp.edpEmailRecoveryTokenButtonTapped"
+ "com.apple.corecdp.edpRecoveryTokenInputEscapeOptionTapped"
+ "com.apple.corecdp.edpRecoveryTokenInputLanding"
+ "com.apple.corecdp.edpRecoveryTokenSpyglassLanding"
+ "com.apple.corecdp.edpRepairEntry"
+ "com.apple.corecdp.edpRepairFinish"
+ "com.apple.corecdp.edpResetProtectedData"
+ "com.apple.corecdp.fetchRecoveryToken"
+ "com.apple.corecdp.passwordChange"
+ "com.apple.corecdp.passwordValidation"
+ "com.apple.corecdp.recoveryTokenInformationalAlertEscapeOffersPresented"
+ "com.apple.corecdp.recoveryTokenInformationalAlertEscapeOptionTapped"
+ "com.apple.corecdp.recoveryTokenInformationalEscapeOptionTapped"
+ "com.apple.corecdp.recoveryTokenInformationalLanding"
+ "com.apple.corecdp.recoveryTokenValidation"
+ "com.apple.corecdp.sendRecoveryToken"
+ "com.apple.corecdp.setUpIdentities"
+ "com.apple.dataaccess.recoveryToken.accessDataLater"
+ "com.apple.dataaccess.recoveryToken.dontHaveKey"
+ "com.apple.dataaccess.recoverytoken.dontHave"
+ "com.apple.protectedcloudstorage"
+ "componentsSeparatedByString:"
+ "contextForAccountWithDSID:"
+ "contextForCDPEDPStateRepair"
+ "contextForEDPStateRepair"
+ "country"
+ "createEDPLivenessDictionaryWithContext:error:"
+ "createEDPLivenessDictionaryWithContext:uiProvider:completion:"
+ "edp"
+ "edpEligible"
+ "edpHealth"
+ "edpPCSGuitarfishChangePassword:completion:"
+ "edpPCSGuitarfishGetRecoveryTokenInfo:completion:"
+ "edpPCSGuitarfishRepairIdentities:completion:"
+ "edpPCSGuitarfishSetupIdentities:completion:"
+ "edpPCSGuitarfishValidateIdentities:completion:"
+ "edpPCSResetProtectedData:completion:"
+ "edpRecoveryToken"
+ "edpState"
+ "edpStateForAccount:"
+ "fetchCompleted"
+ "fetchConfig"
+ "fetchEDPTokenForContext:completion:"
+ "fetchEDPTokenWithCompletion:"
+ "fetchGlobalConfigUsingCachePolicy:completion:"
+ "forceInteractiveCDPEDPRepair"
+ "interactiveAuthDefaultButtonString"
+ "is2FAFAUserFromNetwork"
+ "isBeneficiaryFlow"
+ "isGuitarfishEnabled"
+ "isICDPEnabledFromNetwork"
+ "kCDPEDPStateRepair"
+ "kEDPOnlyStateRepair"
+ "kPCSAltDSID"
+ "kPCSAuthenticateAppleID"
+ "kPCSDeviceSessionID"
+ "kPCSFlowID"
+ "kPCSSetupGuitarfish"
+ "kPCSSetupPasswordGeneration"
+ "kPCSSetupRecoveryToken"
+ "kPCSSetupVerifierIterationCount"
+ "kPCSSetupVerifierProtocol"
+ "kPCSSetupVerifierSalt"
+ "kcdp_PCSGuitarfishRepairIdentities:completion:"
+ "kcdp_PCSGuitarfishSetupIdentities:completion:"
+ "kcdp_PCSGuitarfishValidateIdentities:completion:"
+ "passwordVersion"
+ "passwordVersionForAccount:"
+ "recoveryToken"
+ "repairEDPStateWithCompletion:"
+ "repairEDPStateWithContext:completion:"
+ "repairEDPStateWithContext:uiProvider:completion:"
+ "replaceToken:withConfigToken:fallbackToken:"
+ "rtName"
+ "setEdpHealth:"
+ "setEdpRecoveryToken:"
+ "setEdpState:"
+ "setFetchCompleted:"
+ "setForceInteractiveCDPEDPRepair:"
+ "setInteractiveAuthDefaultButtonString:"
+ "setPasswordVersion:"
+ "setRecoveryToken:"
+ "setSrpIteration:"
+ "setSrpProtocol:"
+ "setSrpSalt:"
+ "setTokenName:"
+ "setTokenNameMedium:"
+ "setTokenNameTitle:"
+ "set_alwaysPromptForEDPRecoveryToken:"
+ "set_forceEDPReset:"
+ "shortRTName"
+ "srpIteration"
+ "srpProtocol"
+ "srpProtocolForAccount:"
+ "srpSalt"
+ "startCustodianRecoveryWithContext:validator:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "titleRTName"
+ "tokenName"
+ "tokenNameMedium"
+ "tokenNameTitle"
+ "uploadEDPRecoveryTokenForContext:uiProvider:completion:"
+ "uploadEDPRecoveryTokenWithCompletion:"
+ "v28@0:8@16B24"
+ "v32@0:8@\"CDPContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"CDPContext\"16@?<v@?BB@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSArray\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?Q@\"NSArray\"@\"NSString\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?QB@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSDictionary\"@\"NSError\">24"
+ "v32@0:8@\"NSDictionary\"16@?<v@?QQ@\"NSError\">24"
+ "v32@?0Q8@\"NSDictionary\"16@\"NSError\"24"
+ "v32@?0Q8Q16@\"NSError\"24"
+ "v40@0:8@\"CDPContext\"16@\"<CDPRemoteDeviceSecretValidatorProtocolInternal>\"24@?<v@?>32"
+ "v40@0:8@\"CDPContext\"16@\"<CDPStateUIProviderInternal>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"CDPContext\"16@\"<CDPStateUIProviderInternal>\"24@?<v@?Q@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"CDPContext\"16@\"CDPRemoteDeviceSecretValidator\"24@?<v@?>32"
+ "v40@?0Q8Q16@\"NSArray\"24@\"NSError\"32"
+ "v40@?0Q8Q16@\"NSDictionary\"24@\"NSError\"32"
+ "v48@?0Q8Q16@\"NSArray\"24@\"NSString\"32@\"NSError\"40"
+ "validateEDPIdentitiesWithContext:completion:"
+ "validateEDPIdentitiesWithContext:uiProvider:completion:"
+ "validateEDPRecoveryToken:withContext:completion:"
+ "{key.long.titlecase}"
+ "{key.long}"
+ "{key.medium}"
- "\x02f\x11\x15u$"
- "TB,R,N,V_isProxSignIn"
- "_isProxSignIn"
- "is2FAFAUser"
- "showCustodianOSInstructionScreen:validator:"
- "showRecoveryContactStartingScreen:validator:"
- "showRemoteDeviceCodeEntryScreen:validator:"
- "showRemoteDeviceListScreen:validator:"

```
