## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.575.7.0.0
-  __TEXT.__text: 0x19baf0
+525.575.8.0.0
+  __TEXT.__text: 0x19c21c
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0xf204
+  __TEXT.__objc_methlist: 0xf234
   __TEXT.__const: 0x6a48
-  __TEXT.__cstring: 0x109c7
-  __TEXT.__gcc_except_tab: 0xaa8c
-  __TEXT.__oslogstring: 0x14556
+  __TEXT.__cstring: 0x10a33
+  __TEXT.__gcc_except_tab: 0xab44
+  __TEXT.__oslogstring: 0x14634
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x300
-  __TEXT.__unwind_info: 0x4608
+  __TEXT.__unwind_info: 0x4628
   __TEXT.__objc_classname: 0x1e5f
-  __TEXT.__objc_methname: 0x25678
+  __TEXT.__objc_methname: 0x25746
   __TEXT.__objc_methtype: 0x4a55
-  __TEXT.__objc_stubs: 0x10ca0
+  __TEXT.__objc_stubs: 0x10cc0
   __DATA_CONST.__got: 0xad8
-  __DATA_CONST.__const: 0xa778
+  __DATA_CONST.__const: 0xa798
   __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x79a8
+  __DATA_CONST.__objc_selrefs: 0x79c8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x448
   __DATA_CONST.__objc_arraydata: 0x2e8
   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x1410
-  __AUTH_CONST.__cfstring: 0x116e0
-  __AUTH_CONST.__objc_const: 0x28690
+  __AUTH_CONST.__cfstring: 0x11760
+  __AUTH_CONST.__objc_const: 0x286c0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH.__objc_data: 0x2b70
-  __DATA.__objc_ivar: 0x1180
+  __DATA.__objc_ivar: 0x1184
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6f8
   __DATA_DIRTY.__objc_data: 0x1860

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E2C0698-99B5-3546-9A0E-038E9AF6F4BE
-  Functions: 5825
-  Symbols:   22007
-  CStrings:  12936
+  UUID: 8ECBE3A3-2EC5-35C3-8C01-73F08B414716
+  Functions: 5829
+  Symbols:   22022
+  CStrings:  12953
 
Symbols:
+ -[AKAccountManager rcUpsellEligibilityCohortForAccount:]
+ -[AKAccountManager setRCUpsellEligibilityCohort:forAccount:]
+ -[AKUserInformation rcUpsellEligibilityCohort]
+ -[AKUserInformation setRcUpsellEligibilityCohort:]
+ GCC_except_table161
+ GCC_except_table167
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table187
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table222
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table239
+ GCC_except_table264
+ GCC_except_table284
+ GCC_except_table303
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table317
+ GCC_except_table358
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table366
+ GCC_except_table367
+ GCC_except_table382
+ GCC_except_table383
+ _AKAuthenticationRCUpsellEligibilityCohortKey
+ _AKRCUpsellEligibilityCohortHeaderKey
+ _AKRCUpsellEligibilityCohortKey
+ _OBJC_IVAR_$_AKUserInformation._rcUpsellEligibilityCohort
+ ___block_literal_global.753
+ ___block_literal_global.755
+ ___block_literal_global.757
+ ___block_literal_global.759
+ ___block_literal_global.762
+ ___block_literal_global.764
+ _objc_msgSend$setRcUpsellEligibilityCohort:
- GCC_except_table165
- GCC_except_table176
- GCC_except_table178
- GCC_except_table189
- GCC_except_table192
- GCC_except_table198
- GCC_except_table209
- GCC_except_table216
- GCC_except_table224
- GCC_except_table236
- GCC_except_table238
- GCC_except_table263
- GCC_except_table286
- GCC_except_table304
- GCC_except_table307
- GCC_except_table310
- GCC_except_table329
- GCC_except_table359
- GCC_except_table364
- GCC_except_table365
- GCC_except_table368
- GCC_except_table369
- ___block_literal_global.743
- ___block_literal_global.745
- ___block_literal_global.747
- ___block_literal_global.749
- ___block_literal_global.754
- ___block_literal_global.756
CStrings:
+ "%@: RC Upsell cohort value %d obtained from IdMS outside the allowed range [0,9], rejected."
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\ttrustedDeviceId: %@,\n\tidmsTrustedDevicesVersion: %@, \n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\trcUpsellEligibilityCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpdpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
+ "Exception caught when fetching rcUpsellEligibilityCohort property: %@"
+ "Exception caught when setting rcUpsellEligibilityCohort: %@"
+ "T@\"NSNumber\",C,N,V_rcUpsellEligibilityCohort"
+ "X-Apple-I-RC-CH"
+ "_rcUpsellEligibilityCohort"
+ "rcUpCh"
+ "rcUpsellEligibilityCohort"
+ "rcUpsellEligibilityCohortForAccount:"
+ "setRCUpsellEligibilityCohort:forAccount:"
+ "setRcUpsellEligibilityCohort:"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\tcanCreateSimpleProfiles: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\ttrustedDeviceId: %@,\n\tidmsTrustedDevicesVersion: %@, \n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tpdpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"

```
