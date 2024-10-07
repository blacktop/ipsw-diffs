## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-493.100.4.0.0
-  __TEXT.__text: 0xcc930
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0xb258
+493.100.8.0.0
+  __TEXT.__text: 0xce3f4
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0xb368
   __TEXT.__const: 0x2121
-  __TEXT.__cstring: 0xd5f3
-  __TEXT.__oslogstring: 0x10216
-  __TEXT.__gcc_except_tab: 0x5184
+  __TEXT.__cstring: 0xd7aa
+  __TEXT.__oslogstring: 0x104cf
+  __TEXT.__gcc_except_tab: 0x5360
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x10e
-  __TEXT.__unwind_info: 0x3a10
-  __TEXT.__objc_classname: 0x1942
-  __TEXT.__objc_methname: 0x1f115
+  __TEXT.__unwind_info: 0x3ab8
+  __TEXT.__objc_classname: 0x1943
+  __TEXT.__objc_methname: 0x1f488
   __TEXT.__objc_methtype: 0x4283
-  __TEXT.__objc_stubs: 0xdbe0
-  __DATA_CONST.__got: 0x988
-  __DATA_CONST.__const: 0x5198
+  __TEXT.__objc_stubs: 0xdce0
+  __DATA_CONST.__got: 0x990
+  __DATA_CONST.__const: 0x5258
   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6460
+  __DATA_CONST.__objc_selrefs: 0x6530
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x148
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x10b0
-  __AUTH_CONST.__cfstring: 0xdee0
-  __AUTH_CONST.__objc_const: 0x24290
+  __AUTH_CONST.__cfstring: 0xe280
+  __AUTH_CONST.__objc_const: 0x243b0
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH.__objc_data: 0x1ab8
-  __DATA.__objc_ivar: 0xe9c
+  __DATA.__objc_ivar: 0xeac
   __DATA.__data: 0x1660
   __DATA.__bss: 0x630
   __DATA_DIRTY.__objc_data: 0x1bf8

   - /System/Library/PrivateFrameworks/CorePhoneNumbers.framework/CorePhoneNumbers
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
+  - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5652
-  Symbols:   7676
-  CStrings:  8864
+  Functions: 5691
+  Symbols:   7752
+  CStrings:  8939
 
Symbols:
+ _AKEDPStateHeaderKey
+ _AKEDPStateKey
+ _AKIdMSEDPTokenIdKey
+ _AKPasswordVersionHeaderKey
+ _AKPasswordVersionKey
+ _AKRequestBodyEDPAttemptsRemaining
+ _AKRequestBodyEDPCountOfDBRRecordsMatchedToNewestRecoveryKey
+ _AKRequestBodyEDPCountOfRecordIdentities
+ _AKRequestBodyEDPIdentityHash
+ _AKRequestBodyEDPPasswordVersionMatchesIdms
+ _AKRequestBodyEDPPrimary
+ _AKRequestBodyEDPRecovery
+ _AKRequestBodyEDPStashedRecoveryTokenMatchesEscrow
+ _AKRequestBodyEDPState
+ _AKSRPIterationCountKey
+ _AKSRPIterationHeaderKey
+ _AKSRPProtocolHeaderKey
+ _AKSRPProtocolKey
+ _AKSRPSaltHeaderKey
+ _AKSRPSaltKey
+ _AKURLBagKeyEDPComplete
+ _AKURLBagKeyEDPMigration
+ _AKURLBagKeyRemoveEDPToken
+ _AKURLBagKeySendRecoveryTokenEmail
+ _AKURLBagKeyStoreEDPToken
+ _MAEGetActivationStateWithError
+ _kMAActivationStateUnactivated
CStrings:
+ "\x0f\x01\x16!\x1f\x0f\x0f\x01"
+ "<%!@(MISSING): %!p(MISSING) {\n\tgivenName: %!@(MISSING),\n\tfamilyName: %!@(MISSING),\n\tforwardingEmail: %!@(MISSING),\n\tprimaryEmailAddress: %!@(MISSING),\n\taccountName: %!@(MISSING),\n\taccountAliases: %!@(MISSING),\n\treachableEmails: %!@(MISSING),\n\tauthorizedApplicationsListVersion: %!@(MISSING),\n\tmasterKeyID: %!@(MISSING),\n\tvettedPrimaryEmail: %!@(MISSING),\n\tphoneAsAppleID: %!@(MISSING),\n\tisUnderage: %!@(MISSING),\n\tisSiwaForChildEnabled: %!@(MISSING),\n\tuserAgeRange: %!l(MISSING)u,\n\tisSenior: %!@(MISSING),\n\tageOfMajority: %!@(MISSING),\n\tisLegacyStudent: %!@(MISSING),\n\tappleIDCountryCode: %!@(MISSING),\n\thasUsedAuthorization: %!@(MISSING), \n\tprivateAttestationEnabled: %!@(MISSING), \n\tappleIDSecurityLevel: %!l(MISSING)u,\n\tauthMode: %!l(MISSING)u,\n\tisMdmInfoRequired: %!@(MISSING),\n\trepairState: %!l(MISSING)u,\n\tselectedEmail: %!@(MISSING),\n\tcanBeCustodian: %!@(MISSING),\n\tcanHaveCustodian: %!@(MISSING),\n\tcustodianEnabled: %!@(MISSING),\n\tcanBeBeneficiary: %!@(MISSING),\n\tcanHaveBeneficiary: %!@(MISSING),\n\thasMDM: %!@(MISSING),\n\tmanagedOrganizationType: %!@(MISSING),\n\tmanagedOrganizationName: %!@(MISSING),\n\tisNotificationEmailAvailable: %!@(MISSING),\n\tnotificationEmail: %!@(MISSING),\n\tadditionalInfo: %!@(MISSING),\n\ttrustedPhoneNumbers: %!@(MISSING),\n\tsecurityKeys: %!@(MISSING),\n\tloginHandles: %!@(MISSING),\n\tprivateEmailListVersion: %!@(MISSING),\n\tisProximityAuthEligible: %!@(MISSING),\n\twebAccessEnabled: %!@(MISSING),\n\tserverExperimentalFeatures: %!@(MISSING),\n\tcustodianInfos: %!@(MISSING),\n\tbeneficiaryInfo: %!@(MISSING),\n\tpasskeyEligible: %!@(MISSING),\n\tpasskeyPresent: %!@(MISSING),\n\tgroupKitEligibility: %!@(MISSING),\n\tpasscodeAuthEnabled: %!@(MISSING),\n\taskToBuy: %!@(MISSING),\n\thasSOSActiveDevice: %!@(MISSING),\n\tSOSNeeded: %!@(MISSING),\n\tdeviceListVersion: %!@(MISSING),\n\tconfigDataVersion: %!@(MISSING),\n\tbirthYear: %!@(MISSING),\n\tcriticalAccountEditsAllowed: %!@(MISSING),\n\thasModernRecoveryKey: %!@(MISSING),\n\tadpCohort: %!@(MISSING),\n\tthirdPartyRegulatoryOverride: %!@(MISSING),\n\tedpState: %!@(MISSING),\n\tpasswordVersion: %!@(MISSING),\n\tsrpProtocol: %!@(MISSING),\n\tidmsEDPTTokenId: %!@(MISSING),\n\tpiggybackingApprovalEligible: %!@(MISSING),\n}>"
+ "<%!@(MISSING): %!p(MISSING)> \nAuthorization Request %!@(MISSING) \nPassword Request: %!@(MISSING) \nProxied App Name: %!@(MISSING)\nProxied BundleID: %!@(MISSING)\nProxied Team: %!@(MISSING) \nSession ID: %!@(MISSING) \n_isWebLogin: %!d(MISSING) \n_isFirstPartyLogin: %!d(MISSING) \n"
+ "AKAccountManager clearDeviceRemovalReasonFromAccount"
+ "AKAccountManager setDeviceRemovalReason:%!l(MISSING)d onAccount:%!@(MISSING)"
+ "Calling out to remote auth service to perform EDP complete key drop"
+ "Calling out to remote auth service to perform EDP migration"
+ "Exception caught when fetching dcrtRenewalAttempted: %!@(MISSING)"
+ "Exception caught when fetching edpState property: %!@(MISSING)"
+ "Exception caught when fetching passwordVersion property: %!@(MISSING)"
+ "Exception caught when fetching srpProtocol property: %!@(MISSING)"
+ "Exception caught when fetching the idMSEDPTokenId property: %!@(MISSING)"
+ "Failed to fetch device activation state: %!@(MISSING)"
+ "First attempt fetching device activation state failed, retrying once."
+ "Rejecting out-of-range EDP state (%!@(MISSING))."
+ "Result of EDP complete remote call result: %!{(MISSING)BOOL}d and error: %!@(MISSING)"
+ "Result of EDP migration remote call result: %!{(MISSING)BOOL}d and error: %!@(MISSING)"
+ "T@\"NSNumber\",C,N,V_edpState"
+ "T@\"NSNumber\",C,N,V_passwordVersion"
+ "T@\"NSString\",C,N,V_idmsEDPTokenId"
+ "T@\"NSString\",C,N,V_srpProtocol"
+ "X-Apple-I-EDP-Iters"
+ "X-Apple-I-EDP-PV"
+ "X-Apple-I-EDP-S"
+ "X-Apple-I-EDP-SP"
+ "X-Apple-I-EDP-Salt"
+ "_edpState"
+ "_idmsEDPTokenId"
+ "_passwordVersion"
+ "_srpProtocol"
+ "ar"
+ "authkit/edp-complete"
+ "authkit/edp-migration"
+ "authkit/remove-edp-token"
+ "cri"
+ "dcrtRenewalAttempted"
+ "dcrtRenewalAttempted:"
+ "didConfirmDeviceWasActivated"
+ "edpComplete"
+ "edpMigration"
+ "edpPrimary"
+ "edpRecovery"
+ "edpState"
+ "edpStateForAccount:"
+ "edpStateValueForAccount:"
+ "edpTokenId"
+ "edpmc"
+ "edprtme"
+ "edps"
+ "idmsEDPTokenId"
+ "idmsEDPTokenIdForAccount:"
+ "ih"
+ "passwordVersion"
+ "passwordVersionForAccount:"
+ "performEdpCompleteKeyDropWithAltDSID:completion:"
+ "performEdpCompleteKeyDropWithAltDSID:error:"
+ "performEdpMigrationWithAltDSID:completion:"
+ "performEdpMigrationWithAltDSID:error:"
+ "performRemoveEdpTokenWithAltDSID:completion:"
+ "performRemoveEdpTokenWithAltDSID:error:"
+ "pv"
+ "pvmi"
+ "removeEdpToken"
+ "s"
+ "sendRecoveryTokenEmail"
+ "setDCRTRenewalAttempted:forAccount:"
+ "setEDPState:forAccount:"
+ "setEdpState:"
+ "setIdMSEDPTokenId:forAccount:"
+ "setIdmsEDPTokenId:"
+ "setPasswordVersion:"
+ "setPasswordVersion:forAccount:"
+ "setSRPProtocol:forAccount:"
+ "setSrpProtocol:"
+ "sp"
+ "srpProtocol"
+ "srpProtocolForAccount:"
+ "storeEdpToken"
- "\x0f\x01\x16!\x1f\x0f\f"
- "<%!@(MISSING): %!p(MISSING) {\n\tgivenName: %!@(MISSING),\n\tfamilyName: %!@(MISSING),\n\tforwardingEmail: %!@(MISSING),\n\tprimaryEmailAddress: %!@(MISSING),\n\taccountName: %!@(MISSING),\n\taccountAliases: %!@(MISSING),\n\treachableEmails: %!@(MISSING),\n\tauthorizedApplicationsListVersion: %!@(MISSING),\n\tmasterKeyID: %!@(MISSING),\n\tvettedPrimaryEmail: %!@(MISSING),\n\tphoneAsAppleID: %!@(MISSING),\n\tisUnderage: %!@(MISSING),\n\tisSiwaForChildEnabled: %!@(MISSING),\n\tuserAgeRange: %!l(MISSING)u,\n\tisSenior: %!@(MISSING),\n\tageOfMajority: %!@(MISSING),\n\tisLegacyStudent: %!@(MISSING),\n\tappleIDCountryCode: %!@(MISSING),\n\thasUsedAuthorization: %!@(MISSING), \n\tprivateAttestationEnabled: %!@(MISSING), \n\tappleIDSecurityLevel: %!l(MISSING)u,\n\tauthMode: %!l(MISSING)u,\n\tisMdmInfoRequired: %!@(MISSING),\n\trepairState: %!l(MISSING)u,\n\tselectedEmail: %!@(MISSING),\n\tcanBeCustodian: %!@(MISSING),\n\tcanHaveCustodian: %!@(MISSING),\n\tcustodianEnabled: %!@(MISSING),\n\tcanBeBeneficiary: %!@(MISSING),\n\tcanHaveBeneficiary: %!@(MISSING),\n\thasMDM: %!@(MISSING),\n\tmanagedOrganizationType: %!@(MISSING),\n\tmanagedOrganizationName: %!@(MISSING),\n\tisNotificationEmailAvailable: %!@(MISSING),\n\tnotificationEmail: %!@(MISSING),\n\tadditionalInfo: %!@(MISSING),\n\ttrustedPhoneNumbers: %!@(MISSING),\n\tsecurityKeys: %!@(MISSING),\n\tloginHandles: %!@(MISSING),\n\tprivateEmailListVersion: %!@(MISSING),\n\tisProximityAuthEligible: %!@(MISSING),\n\twebAccessEnabled: %!@(MISSING),\n\tserverExperimentalFeatures: %!@(MISSING),\n\tcustodianInfos: %!@(MISSING),\n\tbeneficiaryInfo: %!@(MISSING),\n\tpasskeyEligible: %!@(MISSING),\n\tpasskeyPresent: %!@(MISSING),\n\tgroupKitEligibility: %!@(MISSING),\n\tpasscodeAuthEnabled: %!@(MISSING),\n\taskToBuy: %!@(MISSING),\n\thasSOSActiveDevice: %!@(MISSING),\n\tSOSNeeded: %!@(MISSING),\n\tdeviceListVersion: %!@(MISSING),\n\tconfigDataVersion: %!@(MISSING),\n\tbirthYear: %!@(MISSING),\n\tcriticalAccountEditsAllowed: %!@(MISSING),\n\thasModernRecoveryKey: %!@(MISSING),\n\tadpCohort: %!@(MISSING),\n\tthirdPartyRegulatoryOverride: %!@(MISSING),\n\tpiggybackingApprovalEligible: %!@(MISSING),\n}>"
- "<%!@(MISSING): %!p(MISSING)> \nAuthorization Request %!@(MISSING) \nPassword Request: %!@(MISSING) \nProxied App Name: %!@(MISSING)\nProxied BundleID: %!@(MISSING)\nProxied Team: %!@(MISSING) \nSession ID: %!@(MISSING)"
- "AKAccountMAanger clearDeviceRemovalReasonFromAccount"
- "AKAccountMAanger setDeviceRemovalReason:%!l(MISSING)d onAccount:%!@(MISSING)"
- "Fetching accounts of type %!@(MISSING) succeeed!"
- "Fetching token: %!@(MISSING) for account %!@(MISSING)"

```
