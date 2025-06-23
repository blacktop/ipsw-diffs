## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-512.1.3.0.0
-  __TEXT.__text: 0xda1c8
+514.2.0.0.0
+  __TEXT.__text: 0xd9b14
   __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0xd8d4
+  __TEXT.__objc_methlist: 0xd764
   __TEXT.__const: 0x6af0
-  __TEXT.__cstring: 0xeaa2
-  __TEXT.__oslogstring: 0x11213
-  __TEXT.__gcc_except_tab: 0x5730
+  __TEXT.__cstring: 0xe985
+  __TEXT.__oslogstring: 0x112b4
+  __TEXT.__gcc_except_tab: 0x5790
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x16c
   __TEXT.__unwind_info: 0x4018
-  __TEXT.__objc_classname: 0x1c2f
-  __TEXT.__objc_methname: 0x21a37
-  __TEXT.__objc_methtype: 0x456d
-  __TEXT.__objc_stubs: 0xec80
-  __DATA_CONST.__got: 0xa18
-  __DATA_CONST.__const: 0x7f18
-  __DATA_CONST.__objc_classlist: 0x628
+  __TEXT.__objc_classname: 0x1c02
+  __TEXT.__objc_methname: 0x2175f
+  __TEXT.__objc_methtype: 0x4529
+  __TEXT.__objc_stubs: 0xed20
+  __DATA_CONST.__got: 0xa08
+  __DATA_CONST.__const: 0x7ed8
+  __DATA_CONST.__objc_classlist: 0x618
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6da8
+  __DATA_CONST.__objc_selrefs: 0x6d68
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x3e0
+  __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x1c8
   __AUTH_CONST.__auth_got: 0x6f8
   __AUTH_CONST.__const: 0x1170
-  __AUTH_CONST.__cfstring: 0xf220
-  __AUTH_CONST.__objc_const: 0x255a8
+  __AUTH_CONST.__cfstring: 0xf140
+  __AUTH_CONST.__objc_const: 0x25080
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x25d0
-  __DATA.__objc_ivar: 0xfe8
+  __AUTH.__objc_data: 0x2530
+  __DATA.__objc_ivar: 0xfc0
   __DATA.__data: 0x18a0
   __DATA.__bss: 0x640
   __DATA_DIRTY.__objc_data: 0x17c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 14683BC9-92B2-35B7-9113-96C26C4FEE34
-  Functions: 6164
-  Symbols:   21487
-  CStrings:  11467
+  UUID: 5AF83EA5-6324-3A00-ACC2-E2EE233D844A
+  Functions: 6140
+  Symbols:   21407
+  CStrings:  11429
 
Symbols:
+ -[AKAccountManager _idmsWalrusStatusForAccount:]
+ -[AKAccountManager _idmsWalrusStatusForAccount:].cold.1
+ -[AKAccountManager idmsWalrusStatusForAccount:]
+ -[AKAccountManager idmsWalrusStatusForAccount:].cold.1
+ -[AKAccountManager idmsWalrusStatusForAccount:].cold.2
+ -[AKAccountManager setIdmsWalrusStatus:forAccount:]
+ -[AKAccountManager setIdmsWalrusStatus:forAccount:].cold.1
+ -[AKAttestationRequestData client]
+ -[AKAttestationRequestData setClient:]
+ -[AKConfiguration idmsWalrusStatusOverride]
+ -[AKConfiguration setIdmsWalrusStatusOverride:]
+ -[AKDevice isInRecoveryPartition]
+ -[AKURLConfiguration initWithDictionary:device:]
+ -[AKURLConfiguration initWithDictionary:device:].cold.1
+ -[AKUserInformation idmsWalrusStatus]
+ -[AKUserInformation setIdmsWalrusStatus:]
+ -[NSMutableURLRequest(AuthKit) ak_addSupportedLanguageHeader]
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table163
+ GCC_except_table178
+ GCC_except_table200
+ GCC_except_table225
+ GCC_except_table245
+ GCC_except_table262
+ GCC_except_table265
+ GCC_except_table268
+ GCC_except_table273
+ GCC_except_table274
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table317
+ GCC_except_table318
+ GCC_except_table327
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table330
+ GCC_except_table368
+ _AKIdmsWalrusStatusKey
+ _AKIdmsWalrusStatusOverrideKey
+ _AKURLBagKeyCriticalAccountEdit
+ _OBJC_IVAR_$_AKAttestationRequestData._client
+ _OBJC_IVAR_$_AKUserInformation._idmsWalrusStatus
+ ___63-[AKCustodianController revokeCustodianWithContext:completion:]_block_invoke.6
+ ___63-[AKCustodianController revokeCustodianWithContext:completion:]_block_invoke.6.cold.1
+ ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.4
+ ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.4.cold.1
+ ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.5
+ ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.5.cold.1
+ ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.1
+ ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.1.cold.1
+ ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.3
+ ___74-[AKCustodianController updateCustodianRecoveryKeyWithContext:completion:]_block_invoke.7
+ ___74-[AKCustodianController updateCustodianRecoveryKeyWithContext:completion:]_block_invoke.7.cold.1
+ ___75-[AKCustodianController fetchCustodianRecoveryTokenWithContext:completion:]_block_invoke.14
+ ___75-[AKCustodianController fetchCustodianRecoveryTokenWithContext:completion:]_block_invoke.14.cold.1
+ ___76-[AKAccountManager removeContinuationTokenForAccount:telemetryFlowID:error:]_block_invoke
+ ___76-[AKAccountManager removeContinuationTokenForAccount:telemetryFlowID:error:]_block_invoke.cold.1
+ ___77-[AKCustodianController fetchCustodianDataRecoveryKeyWithContext:completion:]_block_invoke.15
+ ___77-[AKCustodianController fetchCustodianDataRecoveryKeyWithContext:completion:]_block_invoke.15.cold.1
+ ___77-[AKCustodianController startCustodianRecoveryRequestWithContext:completion:]_block_invoke.9
+ ___79-[AKCustodianController fetchCustodianRecoveryCodeConfigurationWithCompletion:]_block_invoke.10
+ ___81-[AKCustodianController startCustodianRecoveryTransactionWithContext:completion:]_block_invoke.12
+ ___81-[AKCustodianController startCustodianRecoveryTransactionWithContext:completion:]_block_invoke.12.cold.1
+ ___89-[AKCustodianController sendEmbargoEndNotificationFeedbackWithContext:urlKey:completion:]_block_invoke.16
+ ___89-[AKCustodianController sendEmbargoEndNotificationFeedbackWithContext:urlKey:completion:]_block_invoke.16.cold.1
+ ___block_descriptor_48_e8_32s40s_e24_v32?0"NSError"8Q16^B24ls32l8s40l8
+ ___block_literal_global.221
+ ___block_literal_global.246
+ _objc_msgSend$_deviceLanguage
+ _objc_msgSend$_idmsWalrusStatusForAccount:
+ _objc_msgSend$ak_addSupportedLanguageHeader
+ _objc_msgSend$idmsWalrusStatusOverride
+ _objc_msgSend$initWithDictionary:device:
+ _objc_msgSend$isInRecoveryPartition
+ _objc_msgSend$setIdmsWalrusStatus:
- +[AKTrustedContact supportsSecureCoding]
- +[AKTrustedContactsSyncResult supportsSecureCoding]
- -[AKAttestationRequestData clientName]
- -[AKAttestationRequestData setClientName:]
- -[AKCustodianContext beneficiaryContacts]
- -[AKCustodianContext custodianContacts]
- -[AKCustodianContext setBeneficiaryContacts:]
- -[AKCustodianContext setCustodianContacts:]
- -[AKCustodianController performTrustedContactsDataSync:completion:]
- -[AKTrustedContact .cxx_destruct]
- -[AKTrustedContact copyWithZone:]
- -[AKTrustedContact encodeWithCoder:]
- -[AKTrustedContact hashedWrappingKeyRKC]
- -[AKTrustedContact initWithCoder:]
- -[AKTrustedContact initWithUUID:status:]
- -[AKTrustedContact setHashedWrappingKeyRKC:]
- -[AKTrustedContact setStatus:]
- -[AKTrustedContact setUuid:]
- -[AKTrustedContact status]
- -[AKTrustedContact uuid]
- -[AKTrustedContactsSyncResult .cxx_destruct]
- -[AKTrustedContactsSyncResult beneficiaryListVersion]
- -[AKTrustedContactsSyncResult beneficiaryOperationsByID]
- -[AKTrustedContactsSyncResult copyWithZone:]
- -[AKTrustedContactsSyncResult custodianListVersion]
- -[AKTrustedContactsSyncResult custodianOperationsByID]
- -[AKTrustedContactsSyncResult debugDescription]
- -[AKTrustedContactsSyncResult encodeWithCoder:]
- -[AKTrustedContactsSyncResult initWithCoder:]
- -[AKTrustedContactsSyncResult orphanedBeneficiaryUUIDs]
- -[AKTrustedContactsSyncResult orphanedCustodianUUIDs]
- -[AKTrustedContactsSyncResult setBeneficiaryListVersion:]
- -[AKTrustedContactsSyncResult setBeneficiaryOperationsByID:]
- -[AKTrustedContactsSyncResult setCustodianListVersion:]
- -[AKTrustedContactsSyncResult setCustodianOperationsByID:]
- -[AKTrustedContactsSyncResult setOrphanedBeneficiaryUUIDs:]
- -[AKTrustedContactsSyncResult setOrphanedCustodianUUIDs:]
- GCC_except_table154
- GCC_except_table157
- GCC_except_table162
- GCC_except_table164
- GCC_except_table173
- GCC_except_table177
- GCC_except_table180
- GCC_except_table187
- GCC_except_table199
- GCC_except_table224
- GCC_except_table247
- GCC_except_table263
- GCC_except_table266
- GCC_except_table269
- GCC_except_table284
- GCC_except_table285
- GCC_except_table286
- GCC_except_table287
- GCC_except_table321
- GCC_except_table322
- GCC_except_table364
- _AKTrustedContactSyncOperationFromIntegerValue
- _AKTrustedContactsSyncOperationDelete
- _AKTrustedContactsSyncOperationFinish
- _AKTrustedContactsSyncOperationUpdateRKC
- _AKURLBagKeyTrustedContactsDataSync
- _OBJC_CLASS_$_AKTrustedContact
- _OBJC_CLASS_$_AKTrustedContactsSyncResult
- _OBJC_IVAR_$_AKAttestationRequestData._clientName
- _OBJC_IVAR_$_AKCustodianContext._beneficiaryContacts
- _OBJC_IVAR_$_AKCustodianContext._custodianContacts
- _OBJC_IVAR_$_AKTrustedContact._hashedWrappingKeyRKC
- _OBJC_IVAR_$_AKTrustedContact._status
- _OBJC_IVAR_$_AKTrustedContact._uuid
- _OBJC_IVAR_$_AKTrustedContactsSyncResult._beneficiaryListVersion
- _OBJC_IVAR_$_AKTrustedContactsSyncResult._beneficiaryOperationsByID
- _OBJC_IVAR_$_AKTrustedContactsSyncResult._custodianListVersion
- _OBJC_IVAR_$_AKTrustedContactsSyncResult._custodianOperationsByID
- _OBJC_IVAR_$_AKTrustedContactsSyncResult._orphanedBeneficiaryUUIDs
- _OBJC_IVAR_$_AKTrustedContactsSyncResult._orphanedCustodianUUIDs
- _OBJC_METACLASS_$_AKTrustedContact
- _OBJC_METACLASS_$_AKTrustedContactsSyncResult
- __OBJC_$_CLASS_METHODS_AKTrustedContact
- __OBJC_$_CLASS_METHODS_AKTrustedContactsSyncResult
- __OBJC_$_CLASS_PROP_LIST_AKTrustedContact
- __OBJC_$_CLASS_PROP_LIST_AKTrustedContactsSyncResult
- __OBJC_$_INSTANCE_METHODS_AKTrustedContact
- __OBJC_$_INSTANCE_METHODS_AKTrustedContactsSyncResult
- __OBJC_$_INSTANCE_VARIABLES_AKTrustedContact
- __OBJC_$_INSTANCE_VARIABLES_AKTrustedContactsSyncResult
- __OBJC_$_PROP_LIST_AKTrustedContact
- __OBJC_$_PROP_LIST_AKTrustedContactsSyncResult
- __OBJC_CLASS_PROTOCOLS_$_AKTrustedContact
- __OBJC_CLASS_PROTOCOLS_$_AKTrustedContactsSyncResult
- __OBJC_CLASS_RO_$_AKTrustedContact
- __OBJC_CLASS_RO_$_AKTrustedContactsSyncResult
- __OBJC_METACLASS_RO_$_AKTrustedContact
- __OBJC_METACLASS_RO_$_AKTrustedContactsSyncResult
- ___63-[AKCustodianController revokeCustodianWithContext:completion:]_block_invoke.22
- ___63-[AKCustodianController revokeCustodianWithContext:completion:]_block_invoke.22.cold.1
- ___67-[AKCustodianController performTrustedContactsDataSync:completion:]_block_invoke
- ___67-[AKCustodianController performTrustedContactsDataSync:completion:]_block_invoke.34
- ___67-[AKCustodianController performTrustedContactsDataSync:completion:]_block_invoke_2
- ___67-[AKCustodianController performTrustedContactsDataSync:completion:]_block_invoke_2.cold.1
- ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.20
- ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.20.cold.1
- ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.21
- ___70-[AKCustodianController finalizeCustodianSetupWithContext:completion:]_block_invoke.21.cold.1
- ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.17
- ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.17.cold.1
- ___70-[AKCustodianController initiateCustodianSetupWithContext:completion:]_block_invoke.19
- ___74-[AKCustodianController updateCustodianRecoveryKeyWithContext:completion:]_block_invoke.23
- ___74-[AKCustodianController updateCustodianRecoveryKeyWithContext:completion:]_block_invoke.23.cold.1
- ___75-[AKCustodianController fetchCustodianRecoveryTokenWithContext:completion:]_block_invoke.30
- ___75-[AKCustodianController fetchCustodianRecoveryTokenWithContext:completion:]_block_invoke.30.cold.1
- ___77-[AKCustodianController fetchCustodianDataRecoveryKeyWithContext:completion:]_block_invoke.31
- ___77-[AKCustodianController fetchCustodianDataRecoveryKeyWithContext:completion:]_block_invoke.31.cold.1
- ___77-[AKCustodianController startCustodianRecoveryRequestWithContext:completion:]_block_invoke.25
- ___79-[AKCustodianController fetchCustodianRecoveryCodeConfigurationWithCompletion:]_block_invoke.26
- ___81-[AKCustodianController startCustodianRecoveryTransactionWithContext:completion:]_block_invoke.28
- ___81-[AKCustodianController startCustodianRecoveryTransactionWithContext:completion:]_block_invoke.28.cold.1
- ___89-[AKCustodianController sendEmbargoEndNotificationFeedbackWithContext:urlKey:completion:]_block_invoke.32
- ___89-[AKCustodianController sendEmbargoEndNotificationFeedbackWithContext:urlKey:completion:]_block_invoke.32.cold.1
- ___block_descriptor_40_e8_32bs_e49_v24?0"AKTrustedContactsSyncResult"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32bs40r_e49_v24?0"AKTrustedContactsSyncResult"8"NSError"16lr40l8s32l8
- ___block_literal_global.220
- ___block_literal_global.245
- _objc_msgSend$initWithUUID:status:
- _objc_msgSend$performTrustedContactsDataSync:completion:
CStrings:
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tedpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tidmsEDPTTokenId: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n\tidmsWalrusStatus : %@,\n}>"
+ "<%@: %p> with \nCustodianUUID: %@ \naltDSID: %@ \nOwnerAppleID: %@ \nownerCustodianAltDSID: %@ \nwrappingKeyRKC: %@ \npushToken: %@ \nsessionID: %@ \ncustodianRecoveryToken: %@ \nrecoveryStep: %@ \ncliMode: %i \n isCustodianSyncAction: %d \nrecordBuildVersion: %@"
+ "@\"AKClient\""
+ "Accept-Language"
+ "Exception caught when fetching adpOfferEnabled property: %@"
+ "Exception caught when setting adpOfferEnabled property: %@"
+ "Removing continuation key as device is in lost mode"
+ "Server bag is requesting AKURLConfigurationUITypeForceRemoteUI in recovery mode. Falling back AKURLConfigurationUITypeDefault"
+ "T@\"AKClient\",&,N,V_client"
+ "T@\"NSNumber\",C,N,V_idmsWalrusStatus"
+ "T@\"NSNumber\",N"
+ "_AKIdmsWalrusStatusOverrideKey"
+ "_client"
+ "_deviceLanguage"
+ "_idmsWalrusStatus"
+ "_idmsWalrusStatusForAccount:"
+ "ak_addSupportedLanguageHeader"
+ "client"
+ "criticalAccountEdit"
+ "idmsWalrusStatus"
+ "idmsWalrusStatusForAccount:"
+ "idmsWalrusStatusOverride"
+ "idmsWalrusStatusOverride Override Enabled"
+ "idmsWalrusStatusOverrideKey"
+ "initWithDictionary:device:"
+ "isInRecoveryPartition"
+ "setClient:"
+ "setIdmsWalrusStatus:"
+ "setIdmsWalrusStatus:forAccount:"
+ "setIdmsWalrusStatusOverride:"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tparentalAgeConsent: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n\tedpState: %@,\n\tpasswordVersion: %@,\n\tsrpProtocol: %@,\n\tidmsEDPTTokenId: %@,\n\tpiggybackingApprovalEligible: %@,\n\tageMigrationEligible: %@,\n}>"
- "<%@: %p {\ncustodianListVersion: %@\nbeneficiaryListVersion: %@\n_custodianOperationsByID: %@\n_beneficiaryOperationsByID: %@\n}>"
- "<%@: %p> with \nCustodianUUID: %@ \naltDSID: %@ \nOwnerAppleID: %@ \nownerCustodianAltDSID: %@ \nwrappingKeyRKC: %@ \npushToken: %@ \nsessionID: %@ \ncustodianRecoveryToken: %@ \nrecoveryStep: %@ \ncliMode: %i \n custodianContacts: %@ \n beneficiaryContacts: %@ \n isCustodianSyncAction: %d \nrecordBuildVersion: %@"
- "AKTrustedContact"
- "AKTrustedContactsSyncResult"
- "Result of trusted contacts data sync call: %@. Error: %{public}@"
- "Starting call to perform trusted contacts data sync with IdMS: %@"
- "T@\"NSArray\",C,N,V_beneficiaryContacts"
- "T@\"NSArray\",C,N,V_custodianContacts"
- "T@\"NSArray\",C,N,V_orphanedBeneficiaryUUIDs"
- "T@\"NSArray\",C,N,V_orphanedCustodianUUIDs"
- "T@\"NSDictionary\",C,N,V_beneficiaryOperationsByID"
- "T@\"NSDictionary\",C,N,V_custodianOperationsByID"
- "T@\"NSString\",C,N,V_beneficiaryListVersion"
- "T@\"NSString\",C,N,V_custodianListVersion"
- "T@\"NSString\",C,N,V_hashedWrappingKeyRKC"
- "T@\"NSUUID\",C,N,V_uuid"
- "_beneficiaryContacts"
- "_beneficiaryListVersion"
- "_beneficiaryOperationsByID"
- "_custodianContacts"
- "_custodianListVersion"
- "_custodianOperationsByID"
- "_hashedWrappingKeyRKC"
- "_orphanedBeneficiaryUUIDs"
- "_orphanedCustodianUUIDs"
- "_uuid"
- "accountContactDataSync"
- "beneficiaryContacts"
- "beneficiaryOperationsByID"
- "custodian-authkit/perform-trustedContacts-sync"
- "custodianContacts"
- "custodianOperationsByID"
- "finish"
- "hashedWrappingKeyRKC"
- "initWithUUID:status:"
- "orphanedBeneficiaryUUIDs"
- "orphanedCustodianUUIDs"
- "performTrustedContactsDataSync:completion:"
- "setBeneficiaryContacts:"
- "setBeneficiaryListVersion:"
- "setBeneficiaryOperationsByID:"
- "setCustodianContacts:"
- "setCustodianListVersion:"
- "setCustodianOperationsByID:"
- "setHashedWrappingKeyRKC:"
- "setOrphanedBeneficiaryUUIDs:"
- "setOrphanedCustodianUUIDs:"
- "setUuid:"
- "updateRKC"
- "v24@?0@\"AKTrustedContactsSyncResult\"8@\"NSError\"16"
- "v32@0:8@\"AKCustodianContext\"16@?<v@?@\"AKTrustedContactsSyncResult\"@\"NSError\">24"

```
