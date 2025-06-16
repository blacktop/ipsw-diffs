## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-466.23.1.1.0
-  __TEXT.__text: 0xb3604
+466.31.0.0.0
+  __TEXT.__text: 0xb3048
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x9c88
-  __TEXT.__const: 0x1c61
-  __TEXT.__cstring: 0xbeb0
-  __TEXT.__oslogstring: 0xd508
-  __TEXT.__gcc_except_tab: 0x3f1c
+  __TEXT.__objc_methlist: 0x9d68
+  __TEXT.__const: 0x1c41
+  __TEXT.__cstring: 0xbf44
+  __TEXT.__oslogstring: 0xd6e1
+  __TEXT.__gcc_except_tab: 0x3f0c
   __TEXT.__ustring: 0x1b8
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0x3388
-  __TEXT.__objc_classname: 0x15c4
-  __TEXT.__objc_methname: 0x1aa83
-  __TEXT.__objc_methtype: 0x379e
-  __TEXT.__objc_stubs: 0xc060
+  __TEXT.__unwind_info: 0x3350
+  __TEXT.__objc_classname: 0x15c6
+  __TEXT.__objc_methname: 0x1ad81
+  __TEXT.__objc_methtype: 0x379f
+  __TEXT.__objc_stubs: 0xc0e0
   __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x49b8
+  __DATA_CONST.__const: 0x49e8
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b668
-  __DATA_CONST.__objc_selrefs: 0x5808
+  __DATA_CONST.__objc_const: 0x1b748
+  __DATA_CONST.__objc_selrefs: 0x5898
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_classrefs: 0x5b8
+  __DATA_CONST.__objc_classrefs: 0x5c8
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0xc300
+  __AUTH_CONST.__cfstring: 0xc5a0
   __AUTH_CONST.__objc_const: 0x4468
   __AUTH_CONST.__const: 0xf50
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x6a8
-  __AUTH.__objc_data: 0x1cc0
-  __DATA.__objc_ivar: 0xd20
-  __DATA.__data: 0x1588
-  __DATA.__bss: 0x388
-  __DATA_DIRTY.__objc_data: 0x1270
+  __AUTH.__objc_data: 0x1a40
+  __DATA.__objc_ivar: 0xd30
+  __DATA.__data: 0x15d0
+  __DATA.__bss: 0x328
+  __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A5AA018-9710-3F00-96F5-A39ECE0B4834
-  Functions: 5313
-  Symbols:   17223
-  CStrings:  9242
+  UUID: 624C1B70-0368-3106-AB17-A65404FCE7D6
+  Functions: 5319
+  Symbols:   17256
+  CStrings:  9313
 
Symbols:
+ -[AKAccountManager adpCohortForAccount:]
+ -[AKAccountManager adpCohortForAccount:].cold.1
+ -[AKAccountManager authKitAccountForActiveStoreAccount]
+ -[AKAccountManager authKitAccountForActiveStoreAccount].cold.1
+ -[AKAccountManager removePasswordResetTokenForAccount:telemetryFlowID:error:]
+ -[AKAccountManager setADPCohort:forAccount:]
+ -[AKAccountManager setADPCohort:forAccount:].cold.1
+ -[AKAccountManager setADPCohort:forAccount:].cold.2
+ -[AKBiometricRatchetController .cxx_destruct]
+ -[AKCustodianContext recordBuildVersion]
+ -[AKCustodianContext setRecordBuildVersion:]
+ -[AKDeviceListResponse deletedDeviceHash]
+ -[AKDeviceListResponse setDeletedDeviceHash:]
+ -[AKDeviceListResponse setTrustedDeviceHash:]
+ -[AKDeviceListResponse setTrustedDevicesUpdateTimestamp:]
+ -[AKDeviceListResponse trustedDeviceHash]
+ -[AKDeviceListResponse trustedDevicesUpdateTimestamp]
+ -[AKFollowUpFactoryImpl _extensionIDFromPayload:]
+ -[AKFollowUpFactoryImpl _extensionIDFromPayload:].cold.1
+ -[AKFollowUpFactoryImpl _itemFromPayload:pushMessageInfo:withAltDSID:].cold.3
+ -[AKFollowUpFactoryImpl _itemShouldSuppressNotification:]
+ -[AKFollowUpSynchronizer synchronizeFollowUpsForAccount:error:]
+ -[AKFollowUpSynchronizer synchronizeFollowUpsForAccount:error:].cold.1
+ -[AKMediaServicesController activeStoreAccount]
+ -[AKMediaServicesController activeStoreAccount].cold.1
+ -[AKURLBag isTrustedDeviceListHashDisabled]
+ -[AKURLBag ttrConfigurationAtKey:]
+ -[AKUserInformation adpCohort]
+ -[AKUserInformation setAdpCohort:]
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table122
+ GCC_except_table123
+ GCC_except_table137
+ GCC_except_table149
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table172
+ GCC_except_table179
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table226
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table245
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table89
+ GCC_except_table93
+ _AKADPCohortHeaderKey
+ _AKADPCohortKey
+ _AKAuthenticationADPCohortKey
+ _AKDeletedDeviceHashKey
+ _AKFollowUpExtensionIdentifierCDP
+ _AKFollowUpPayloadExtensionKey
+ _AKNativeFollowUpActionKey
+ _AKTrustedDeviceHashKey
+ _AKTrustedDevicesUpdateTimestampKey
+ _AKURLBagKeyAddRecoveryKey
+ _AKURLBagKeyDeleteRecoveryKey
+ _OBJC_IVAR_$_AKBiometricRatchetController._context
+ _OBJC_IVAR_$_AKCustodianContext._recordBuildVersion
+ _OBJC_IVAR_$_AKDeviceListResponse._deletedDeviceHash
+ _OBJC_IVAR_$_AKDeviceListResponse._trustedDeviceHash
+ _OBJC_IVAR_$_AKDeviceListResponse._trustedDevicesUpdateTimestamp
+ _OBJC_IVAR_$_AKUserInformation._adpCohort
+ ___block_literal_global.192
+ ___block_literal_global.334
+ ___block_literal_global.49
+ _objc_msgSend$_extensionIDFromPayload:
+ _objc_msgSend$_itemShouldSuppressNotification:
+ _objc_msgSend$activeStoreAccount
+ _objc_msgSend$ams_activeiTunesAccount
+ _objc_msgSend$ams_sharedAccountStore
+ _objc_msgSend$authKitAccountForActiveStoreAccount
+ _objc_msgSend$setAdpCohort:
+ _objc_msgSend$synchronizeFollowUpsForAccount:inStore:error:
- -[AKAccountManager aidaServiceOwnermanager]
- -[AKAccountManager iTunesAccountType].cold.1
- -[AKAccountManager preferredAccountUsingStoreService].cold.1
- GCC_except_table103
- GCC_except_table104
- GCC_except_table106
- GCC_except_table107
- GCC_except_table108
- GCC_except_table110
- GCC_except_table128
- GCC_except_table129
- GCC_except_table130
- GCC_except_table132
- GCC_except_table133
- GCC_except_table134
- GCC_except_table136
- GCC_except_table155
- GCC_except_table157
- GCC_except_table183
- GCC_except_table218
- GCC_except_table221
- GCC_except_table224
- GCC_except_table230
- GCC_except_table231
- GCC_except_table233
- GCC_except_table234
- GCC_except_table235
- GCC_except_table236
- GCC_except_table252
- GCC_except_table267
- GCC_except_table268
- GCC_except_table269
- GCC_except_table270
- GCC_except_table271
- GCC_except_table272
- GCC_except_table273
- GCC_except_table70
- GCC_except_table71
- GCC_except_table79
- GCC_except_table83
- _AppleIDSSOAuthenticationLibrary
- _AppleIDSSOAuthenticationLibraryCore
- _AppleIDSSOAuthenticationLibraryCore.frameworkLibrary
- _CTEvaluateAMFICodeSignatureCMS
- _CTEvaluateAMFICodeSignatureCMSPubKey
- _CTEvaluateAMFICodeSignatureCMS_MaxDigestType
- _CTEvaluateProvisioningProfile
- _CTParseAmfiCMS
- _CTParseAmfiCMS_internal
- _CTParseContentInfoSignedData
- _CTParseSignerInfos
- _CTVerifyAmfiCMS
- _CTVerifyAmfiCertificateChain
- _OBJC_IVAR_$_AKAccountManager._aidaServiceOwnermanager
- _OBJC_IVAR_$_AKAccountManager._serialQueue
- ___43-[AKAccountManager aidaServiceOwnermanager]_block_invoke
- ___AppleIDSSOAuthenticationLibraryCore_block_invoke
- ___block_literal_global.199
- ___block_literal_global.322
- ___block_literal_global.39
- ___getAIDAServiceOwnersManagerClass_block_invoke
- ___getAIDAServiceOwnersManagerClass_block_invoke.cold.1
- ___getAIDAServiceTypeStoreSymbolLoc_block_invoke
- _getAIDAServiceOwnersManagerClass
- _getAIDAServiceOwnersManagerClass.softClass
- _getAIDAServiceTypeStore
- _getAIDAServiceTypeStore.cold.1
- _getAIDAServiceTypeStoreSymbolLoc
- _getAIDAServiceTypeStoreSymbolLoc.ptr
- _objc_msgSend$accountForService:
- _objc_msgSend$aidaServiceOwnermanager
- _objc_msgSend$altDSIDForAccount:service:
- _objc_msgSend$initWithAccountStore:
CStrings:
+ "\x03\x11\x11\x11\x11"
+ "\b"
+ "\x0e\x16!\x1f\x0f\t"
+ "\x15\x11/&"
+ "%@: ADP cohort value %d obtained from IdMS outside the allowed range, rejected."
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tadpCohort: %@,\n\tthirdPartyRegulatoryOverride: %@,\n}>"
+ "<%@: %p> with \nCustodianUUID: %@ \naltDSID: %@ \nOwnerAppleID: %@ \nownerCustodianAltDSID: %@ \nwrappingKeyRKC: %@ \npushToken: %@ \nsessionID: %@ \ncustodianRecoveryToken: %@ \nrecoveryStep: %@ \ncliMode: %i \n custodianContacts: %@ \n beneficiaryContacts: %@ \n isCustodianSyncAction: %d \nrecordBuildVersion: %@"
+ "<%@:%p> altDSID: %@, deviceListVersion: %@, deviceList: %@, deletedDeviceList: %@, deletedDevicesCacheExpiryOffset: %@, trustedDeviceHash: %@, deletedDeviceHash: %@, trustedDevicesUpdateTimestamp: %@"
+ "@\"AKBiometricRatchetContext\""
+ "AKFollowUpSynchronizer: Client provided nil account, defaulting to the primary iCloud account"
+ "AKNativeAction"
+ "Exception caught when fetching adpCohort property: %@"
+ "Notification should not be sent."
+ "Store account: %@"
+ "T@\"ACAccountType\",R,N,V_iTunesAccountType"
+ "T@\"NSNumber\",C,N,V_adpCohort"
+ "T@\"NSNumber\",C,N,V_trustedDevicesUpdateTimestamp"
+ "T@\"NSString\",C,N,V_deletedDeviceHash"
+ "T@\"NSString\",C,N,V_recordBuildVersion"
+ "T@\"NSString\",C,N,V_trustedDeviceHash"
+ "Unrecognized follow up extension identifier %{public}@. Please add support for this if necessary. Using extension identifier from factory property."
+ "X-Apple-I-ADP-CH"
+ "_adpCohort"
+ "_deletedDeviceHash"
+ "_extensionIDFromPayload:"
+ "_itemShouldSuppressNotification:"
+ "_recordBuildVersion"
+ "_trustedDeviceHash"
+ "_trustedDevicesUpdateTimestamp"
+ "activeStoreAccount"
+ "adpCh"
+ "adpCohort"
+ "adpCohortForAccount:"
+ "adpUpsell"
+ "adpUpsell CFU should not send a notification."
+ "ak-native-action"
+ "ams_activeiTunesAccount"
+ "ams_sharedAccountStore"
+ "authKitAccountForActiveStoreAccount"
+ "com.apple.CoreCDPUI.CDPFollowUpExtension"
+ "deletedDeviceHash"
+ "disableDataRecoveryKey"
+ "enableDataRecoveryKey"
+ "extension"
+ "isTrustedDeviceListHashDisabled"
+ "recordBuildVersion"
+ "removePasswordResetTokenForAccount:telemetryFlowID:error:"
+ "setADPCohort:forAccount:"
+ "setAdpCohort:"
+ "setDeletedDeviceHash:"
+ "setRecordBuildVersion:"
+ "setTrustedDeviceHash:"
+ "setTrustedDevicesUpdateTimestamp:"
+ "synchronizeFollowUpsForAccount:error:"
+ "trustedDeviceHash"
+ "trustedDeviceListHashDisabled"
+ "trustedDevicesUpdateTimestamp"
+ "ttr-cfgs"
+ "ttrConfigurationAtKey:"
- "\x04\x11\x11\x11\x12"
- "\x0e\x16!\x1f\x0f\b"
- "\x15\x11.&"
- "/AppleInternal/Library/Frameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication"
- "/System/Library/Frameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication"
- "/System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSiwaForChildEnabled: %@,\n\tuserAgeRange: %lu,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n\tthirdPartyRegulatoryOverride: %@,\n}>"
- "<%@: %p> with \nCustodianUUID: %@ \naltDSID: %@ \nOwnerAppleID: %@ \nownerCustodianAltDSID: %@ \nwrappingKeyRKC: %@ \npushToken: %@ \nsessionID: %@ \ncustodianRecoveryToken: %@ \nrecoveryStep: %@ \ncliMode: %i \n custodianContacts: %@ \n beneficiaryContacts: %@ \n isCustodianSyncAction: %d"
- "<%@:%p> altDSID: %@, deviceListVersion: %@, deviceList: %@, deletedDeviceList: %@, deletedDevicesCacheExpiryOffset: %@"
- "@\"AIDAServiceOwnersManager\""
- "AIDAServiceOwnersManager"
- "AIDAServiceTypeStore"
- "AKAccountManagerQueue.read.write"
- "_aidaServiceOwnermanager"
- "_serialQueue"
- "accountForService:"
- "aidaServiceOwnermanager"
- "altDSIDForAccount:service:"
- "initWithAccountStore:"

```
