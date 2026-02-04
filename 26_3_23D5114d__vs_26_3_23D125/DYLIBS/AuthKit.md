## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.326.4.0.0
-  __TEXT.__text: 0x185ca0
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0xe534
+525.326.4.1.0
+  __TEXT.__text: 0x189ecc
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_methlist: 0xe72c
   __TEXT.__const: 0x69f8
-  __TEXT.__cstring: 0xfd86
-  __TEXT.__gcc_except_tab: 0xa04c
-  __TEXT.__oslogstring: 0x12aa2
+  __TEXT.__cstring: 0xffb1
+  __TEXT.__gcc_except_tab: 0xa464
+  __TEXT.__oslogstring: 0x12f42
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4288
-  __TEXT.__objc_classname: 0x1d7c
-  __TEXT.__objc_methname: 0x237e8
-  __TEXT.__objc_methtype: 0x47c0
-  __TEXT.__objc_stubs: 0xff80
-  __DATA_CONST.__got: 0xa98
-  __DATA_CONST.__const: 0xa378
-  __DATA_CONST.__objc_classlist: 0x680
+  __TEXT.__unwind_info: 0x4358
+  __TEXT.__objc_classname: 0x1d89
+  __TEXT.__objc_methname: 0x23b8e
+  __TEXT.__objc_methtype: 0x47ed
+  __TEXT.__objc_stubs: 0x101a0
+  __DATA_CONST.__got: 0xaa0
+  __DATA_CONST.__const: 0xa448
+  __DATA_CONST.__objc_classlist: 0x688
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x73c8
+  __DATA_CONST.__objc_selrefs: 0x74b0
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x410
+  __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x105e0
-  __AUTH_CONST.__objc_const: 0x26748
+  __AUTH_CONST.__cfstring: 0x109c0
+  __AUTH_CONST.__objc_const: 0x26e28
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH.__objc_data: 0x2c10
-  __DATA.__objc_ivar: 0x107c
+  __AUTH.__objc_data: 0x2c60
+  __DATA.__objc_ivar: 0x1098
   __DATA.__data: 0x1900
-  __DATA.__bss: 0x6f0
+  __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__bss: 0x2b0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 89B11132-D505-3A3C-8769-D83557437D20
-  Functions: 5551
-  Symbols:   20994
-  CStrings:  12204
+  UUID: 34986F66-57F6-3E1C-AEB2-8C937903AE31
+  Functions: 5596
+  Symbols:   21171
+  CStrings:  12330
 
Symbols:
+ +[AKPDPContext supportsSecureCoding]
+ +[AKUserInformation(Updates) _getIsPDPOperation]
+ +[AKUserInformation(Updates) _setIsPDPOperation:]
+ -[AKAccountManager _pdpStateFromRawState:]
+ -[AKAccountManager _pdpStateValueForAccount:]
+ -[AKAccountManager isPDPEligibleForAccount:]
+ -[AKAccountManager passwordVersionForAccount:]
+ -[AKAccountManager pdpStateForAccount:]
+ -[AKAccountManager pdpStateValueForAccount:]
+ -[AKAccountManager setPDPState:forAccount:]
+ -[AKAccountManager setPasswordVersion:forAccount:]
+ -[AKAccountManager setSRPProtocol:forAccount:]
+ -[AKAccountManager srpProtocolForAccount:]
+ -[AKAppleIDAuthenticationController performPDPNativeIntermissionWithPDPContext:completion:]
+ -[AKAppleIDAuthenticationController performPdpCompleteKeyDropWithAltDSID:error:]
+ -[AKAppleIDAuthenticationController performPdpMigrationWithAltDSID:error:]
+ -[AKConfiguration pdpStateOverride]
+ -[AKConfiguration setPdpStateOverride:]
+ -[AKPDPContext .cxx_destruct]
+ -[AKPDPContext _identifier]
+ -[AKPDPContext altDSID]
+ -[AKPDPContext copyWithZone:]
+ -[AKPDPContext description]
+ -[AKPDPContext encodeWithCoder:]
+ -[AKPDPContext initWithCoder:]
+ -[AKPDPContext initWithRawPassword:altDSID:]
+ -[AKPDPContext init]
+ -[AKPDPContext rawPassword]
+ -[AKPDPContext setAltDSID:]
+ -[AKUserInformation isPDPOperation]
+ -[AKUserInformation passwordVersion]
+ -[AKUserInformation pdpState]
+ -[AKUserInformation setIsPDPOperation:]
+ -[AKUserInformation setPasswordVersion:]
+ -[AKUserInformation setPdpState:]
+ -[AKUserInformation setSrpProtocol:]
+ -[AKUserInformation srpProtocol]
+ GCC_except_table138
+ GCC_except_table154
+ GCC_except_table160
+ GCC_except_table167
+ GCC_except_table180
+ GCC_except_table192
+ GCC_except_table194
+ GCC_except_table209
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table224
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table227
+ GCC_except_table230
+ GCC_except_table248
+ GCC_except_table268
+ GCC_except_table269
+ GCC_except_table287
+ GCC_except_table290
+ GCC_except_table293
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table304
+ GCC_except_table305
+ GCC_except_table306
+ GCC_except_table307
+ GCC_except_table308
+ GCC_except_table340
+ GCC_except_table343
+ GCC_except_table344
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table359
+ GCC_except_table360
+ GCC_except_table361
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table364
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table367
+ _AKPDPStateHeaderKey
+ _AKPDPStateKey
+ _AKPasswordVersionHeaderKey
+ _AKPasswordVersionKey
+ _AKRequestBodyPDPAttemptsRemaining
+ _AKRequestBodyPDPCountOfDBRRecordsMatchedToNewestRecoveryKey
+ _AKRequestBodyPDPCountOfRecordIdentities
+ _AKRequestBodyPDPIdentityHash
+ _AKRequestBodyPDPPasswordVersionMatchesIdms
+ _AKRequestBodyPDPPrimary
+ _AKRequestBodyPDPRecovery
+ _AKRequestBodyPDPStashedRecoveryTokenMatchesEscrow
+ _AKRequestBodyPDPState
+ _AKSRPIterationCountKey
+ _AKSRPIterationHeaderKey
+ _AKSRPProtocolHeaderKey
+ _AKSRPProtocolKey
+ _AKSRPSaltHeaderKey
+ _AKSRPSaltKey
+ _AKURLBagKeyPDPComplete
+ _AKURLBagKeyPDPMigration
+ _AKURLBagKeyPDPNativeIntermission
+ _OBJC_CLASS_$_AKPDPContext
+ _OBJC_IVAR_$_AKPDPContext._altDSID
+ _OBJC_IVAR_$_AKPDPContext._identifier
+ _OBJC_IVAR_$_AKPDPContext._rawPassword
+ _OBJC_IVAR_$_AKUserInformation._isPDPOperation
+ _OBJC_IVAR_$_AKUserInformation._passwordVersion
+ _OBJC_IVAR_$_AKUserInformation._pdpState
+ _OBJC_IVAR_$_AKUserInformation._srpProtocol
+ _OBJC_METACLASS_$_AKPDPContext
+ __AKPdpStateOverrideKey
+ __OBJC_$_CLASS_METHODS_AKPDPContext
+ __OBJC_$_CLASS_PROP_LIST_AKPDPContext
+ __OBJC_$_INSTANCE_METHODS_AKPDPContext
+ __OBJC_$_INSTANCE_VARIABLES_AKPDPContext
+ __OBJC_$_PROP_LIST_AKPDPContext
+ __OBJC_CLASS_PROTOCOLS_$_AKPDPContext
+ __OBJC_CLASS_RO_$_AKPDPContext
+ __OBJC_METACLASS_RO_$_AKPDPContext
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.381
+ ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.382
+ ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.361
+ ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.363
+ ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.374
+ ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.364
+ ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.387
+ ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.377
+ ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.370
+ ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.373
+ ___74-[AKAppleIDAuthenticationController performPdpMigrationWithAltDSID:error:]_block_invoke
+ ___74-[AKAppleIDAuthenticationController performPdpMigrationWithAltDSID:error:]_block_invoke.375
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.367
+ ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.368
+ ___80-[AKAppleIDAuthenticationController performPdpCompleteKeyDropWithAltDSID:error:]_block_invoke
+ ___80-[AKAppleIDAuthenticationController performPdpCompleteKeyDropWithAltDSID:error:]_block_invoke.376
+ ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.369
+ ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.366
+ ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.371
+ ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.365
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.379
+ ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.380
+ ___91-[AKAppleIDAuthenticationController performPDPNativeIntermissionWithPDPContext:completion:]_block_invoke
+ ___91-[AKAppleIDAuthenticationController performPDPNativeIntermissionWithPDPContext:completion:]_block_invoke.357
+ ___91-[AKAppleIDAuthenticationController performPDPNativeIntermissionWithPDPContext:completion:]_block_invoke.358
+ ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.372
+ ___block_literal_global.360
+ ___block_literal_global.448
+ ___block_literal_global.708
+ ___block_literal_global.710
+ ___block_literal_global.712
+ ___block_literal_global.714
+ ___block_literal_global.716
+ ___block_literal_global.719
+ ___block_literal_global.721
+ ___os_log_helper_16_2_3_8_64_8_0_4_0
+ __classIsPDPOperation
+ _kAKAnalyticsPdpEligibility
+ _kAKAnalyticsPdpHealth
+ _objc_getProperty
+ _objc_msgSend$_getIsPDPOperation
+ _objc_msgSend$_pdpStateFromRawState:
+ _objc_msgSend$_pdpStateValueForAccount:
+ _objc_msgSend$_setIsPDPOperation:
+ _objc_msgSend$passwordVersion
+ _objc_msgSend$pdpState
+ _objc_msgSend$pdpStateForAccount:
+ _objc_msgSend$pdpStateOverride
+ _objc_msgSend$pdpStateValueForAccount:
+ _objc_msgSend$performPDPNativeIntermissionWithPDPContext:completion:
+ _objc_msgSend$performPdpCompleteKeyDropWithAltDSID:completion:
+ _objc_msgSend$performPdpMigrationWithAltDSID:completion:
+ _objc_msgSend$rawPassword
+ _objc_msgSend$setIsPDPOperation:
+ _objc_msgSend$setPasswordVersion:
+ _objc_msgSend$setPdpState:
+ _objc_msgSend$setSrpProtocol:
- GCC_except_table146
- GCC_except_table162
- GCC_except_table164
- GCC_except_table175
- GCC_except_table184
- GCC_except_table195
- GCC_except_table196
- GCC_except_table199
- GCC_except_table200
- GCC_except_table206
- GCC_except_table216
- GCC_except_table217
- GCC_except_table243
- GCC_except_table244
- GCC_except_table245
- GCC_except_table247
- GCC_except_table249
- GCC_except_table250
- GCC_except_table256
- GCC_except_table276
- GCC_except_table277
- GCC_except_table295
- GCC_except_table298
- GCC_except_table313
- GCC_except_table314
- GCC_except_table315
- GCC_except_table316
- GCC_except_table317
- GCC_except_table318
- GCC_except_table319
- GCC_except_table320
- GCC_except_table348
- GCC_except_table354
- GCC_except_table355
- ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.368
- ___106-[AKAppleIDAuthenticationController upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:]_block_invoke.369
- ___60-[AKAppleIDAuthenticationController accountNamesForAltDSID:]_block_invoke.350
- ___70-[AKAppleIDAuthenticationController fetchURLBagForAltDSID:completion:]_block_invoke.352
- ___71-[AKAppleIDAuthenticationController fetchBAADeviceTokenWithCompletion:]_block_invoke.363
- ___72-[AKAppleIDAuthenticationController _urlBagFromCache:altDSID:withError:]_block_invoke.353
- ___72-[AKAppleIDAuthenticationController fetchBirthdayForAltDSID:completion:]_block_invoke.374
- ___72-[AKAppleIDAuthenticationController shieldSignInOrCreateFlowsWithError:]_block_invoke.364
- ___73-[AKAppleIDAuthenticationController deleteDeviceListCacheWithCompletion:]_block_invoke.359
- ___73-[AKAppleIDAuthenticationController refreshBAADeviceTokenWithCompletion:]_block_invoke.362
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.356
- ___80-[AKAppleIDAuthenticationController performPasswordResetWithContext:completion:]_block_invoke.357
- ___81-[AKAppleIDAuthenticationController deleteDeviceListCacheWithContext:completion:]_block_invoke.358
- ___84-[AKAppleIDAuthenticationController fetchGlobalConfigurationUsingPolicy:completion:]_block_invoke.355
- ___88-[AKAppleIDAuthenticationController fetchTokensWithAltDSID:tokenIdentifiers:completion:]_block_invoke.360
- ___90-[AKAppleIDAuthenticationController forceURLBagUpdateForAltDSID:urlSwitchData:completion:]_block_invoke.354
- ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.366
- ___91-[AKAppleIDAuthenticationController fetchUpgradeURLForSponsor:forSimpleProfile:completion:]_block_invoke.367
- ___98-[AKAppleIDAuthenticationController deleteTokensFromCacheWithAltDSID:tokenIdentifiers:completion:]_block_invoke.361
- ___block_literal_global.349
- ___block_literal_global.439
- ___block_literal_global.674
- ___block_literal_global.676
- ___block_literal_global.678
- ___block_literal_global.680
- ___block_literal_global.682
- ___block_literal_global.685
- ___block_literal_global.687
CStrings:
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpdpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
+ "<%@: %p { UUID: %@, altDSID: %@, hasPassword: %@ }>"
+ "AKPDPContext"
+ "Calling out to remote auth service for PDP native intermission with context: %@"
+ "Calling out to remote auth service to perform PDP complete key drop"
+ "Calling out to remote auth service to perform PDP migration"
+ "Cannot determine PDP eligibility for nil account"
+ "Exception caught when fetching passwordVersion property: %@"
+ "Exception caught when fetching pdpState property: %@"
+ "Exception caught when fetching srpProtocol property: %@"
+ "PDP context is required for native intermission"
+ "PDP eligibility check for account %@: state=%lu, eligible=%{BOOL}d"
+ "PDP native intermission called with invalid altDSID"
+ "PDP native intermission called with invalid password"
+ "PDP native intermission called with nil context"
+ "PDP native intermission called without completion handler - operation cannot proceed"
+ "PDP native intermission completed successfully"
+ "PDP native intermission failed: %@"
+ "Rejecting out-of-range PDP state (%@)."
+ "Result of PDP complete remote call result: %{BOOL}d and error: %@"
+ "Result of PDP migration remote call result: %{BOOL}d and error: %@"
+ "Result of remote call: %d and error: %@"
+ "Skipping security level check for PDP operations."
+ "T@\"NSNumber\",C,N,V_passwordVersion"
+ "T@\"NSNumber\",C,N,V_pdpState"
+ "T@\"NSString\",C,N,V_srpProtocol"
+ "T@\"NSString\",R,C,V_rawPassword"
+ "TB,N,V_isPDPOperation"
+ "Valid altDSID is required for PDP native intermission"
+ "Valid password is required for PDP native intermission"
+ "X-Apple-I-Iters"
+ "X-Apple-I-PDP-S"
+ "X-Apple-I-PV"
+ "X-Apple-I-SP"
+ "X-Apple-I-Salt"
+ "_AKPdpStateOverrideKey"
+ "_getIsPDPOperation"
+ "_isPDPOperation"
+ "_passwordVersion"
+ "_pdpState"
+ "_pdpStateFromRawState:"
+ "_pdpStateValueForAccount:"
+ "_rawPassword"
+ "_setIsPDPOperation:"
+ "_srpProtocol"
+ "ar"
+ "authkit/pdp-complete"
+ "authkit/pdp-migration"
+ "authkit/pdp-native-intermission"
+ "cri"
+ "ih"
+ "initWithRawPassword:altDSID:"
+ "isPDPEligibleForAccount:"
+ "isPDPOperation"
+ "passwordVersion"
+ "passwordVersionForAccount:"
+ "pdpComplete"
+ "pdpEligible"
+ "pdpHealth"
+ "pdpIntermission"
+ "pdpMigration"
+ "pdpPrimary"
+ "pdpRecovery"
+ "pdpState"
+ "pdpStateForAccount:"
+ "pdpStateOverride"
+ "pdpStateOverride Override Enabled"
+ "pdpStateValueForAccount:"
+ "pdpmc"
+ "pdprtme"
+ "pdps"
+ "performPDPNativeIntermissionWithPDPContext:completion:"
+ "performPdpCompleteKeyDropWithAltDSID:completion:"
+ "performPdpCompleteKeyDropWithAltDSID:error:"
+ "performPdpMigrationWithAltDSID:completion:"
+ "performPdpMigrationWithAltDSID:error:"
+ "pv"
+ "pvmi"
+ "rawPassword"
+ "setIsPDPOperation:"
+ "setPDPState:forAccount:"
+ "setPasswordVersion:"
+ "setPasswordVersion:forAccount:"
+ "setPdpState:"
+ "setPdpStateOverride:"
+ "setSRPProtocol:forAccount:"
+ "setSrpProtocol:"
+ "sp"
+ "srpProtocol"
+ "srpProtocolForAccount:"
+ "v32@0:8@\"AKPDPContext\"16@?<v@?B@\"NSError\">24"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"

```
