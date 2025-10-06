## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-464.5.0.0.0
-  __TEXT.__text: 0xabf48
+466.7.12.0.0
+  __TEXT.__text: 0xada48
   __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x9650
+  __TEXT.__objc_methlist: 0x97a0
   __TEXT.__const: 0x1760
-  __TEXT.__cstring: 0xb3de
-  __TEXT.__oslogstring: 0xc9d2
-  __TEXT.__gcc_except_tab: 0x3c88
+  __TEXT.__cstring: 0xb6e1
+  __TEXT.__oslogstring: 0xcb41
+  __TEXT.__gcc_except_tab: 0x3d50
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x319c
-  __TEXT.__objc_classname: 0x14c6
-  __TEXT.__objc_methname: 0x197a5
+  __TEXT.__unwind_info: 0x320c
+  __TEXT.__objc_classname: 0x14e2
+  __TEXT.__objc_methname: 0x19c45
   __TEXT.__objc_methtype: 0x3606
-  __TEXT.__objc_stubs: 0xbba0
+  __TEXT.__objc_stubs: 0xbce0
   __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x45b8
-  __DATA_CONST.__objc_classlist: 0x470
+  __DATA_CONST.__const: 0x4648
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a6e8
-  __DATA_CONST.__objc_selrefs: 0x54b0
+  __DATA_CONST.__objc_const: 0x1a8e0
+  __DATA_CONST.__objc_selrefs: 0x55a0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0xb9e0
-  __AUTH_CONST.__objc_const: 0x4198
-  __AUTH_CONST.__const: 0xf30
+  __AUTH_CONST.__cfstring: 0xbe00
+  __AUTH_CONST.__objc_const: 0x41e0
+  __AUTH_CONST.__const: 0xf50
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH.__objc_data: 0x1a40
+  __AUTH.__objc_data: 0x1a90
   __DATA.__objc_protorefs: 0xd0
   __DATA.__objc_classrefs: 0x578
   __DATA.__objc_superrefs: 0x2a8
-  __DATA.__objc_ivar: 0xc7c
+  __DATA.__objc_ivar: 0xca0
   __DATA.__data: 0x1500
-  __DATA.__bss: 0x358
+  __DATA.__bss: 0x360
   __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__bss: 0x1f8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3862F148-551B-3E51-ABF9-99FA26526610
-  Functions: 5085
-  Symbols:   16534
-  CStrings:  8808
+  UUID: 1AA08F1F-82A7-3859-9EAA-4C5518C3AFAC
+  Functions: 5134
+  Symbols:   16680
+  CStrings:  8933
 
Symbols:
+ +[AKAlertImageURLProvider url]
+ +[AKAppleIDAuthenticationContext _identifierForContext:]
+ -[AKAccountManager _reportTokenWithName:forAccount:error:]
+ -[AKAccountManager _reportTokenWithName:forAccount:error:].cold.1
+ -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:]
+ -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:].cold.1
+ -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:].cold.2
+ -[AKAccountManager _reportTokenWithTelemetryID:account:telemetryFlowID:error:].cold.3
+ -[AKAccountManager beneficiaryInfoForAccount:]
+ -[AKAccountManager beneficiaryInfoForAccount:].cold.1
+ -[AKAccountManager deletedDevicesCacheExpiryOffsetForAccount:]
+ -[AKAccountManager deletedDevicesCacheExpiryOffsetForAccount:].cold.1
+ -[AKAccountManager removeContinuationTokenForAccount:telemetryFlowID:error:]
+ -[AKAccountManager setBeneficiaryInfo:forAccount:]
+ -[AKAccountManager setBeneficiaryInfo:forAccount:].cold.1
+ -[AKAccountManager setDeletedDevicesCacheExpiryOffset:forAccount:]
+ -[AKAccountManager setDeletedDevicesCacheExpiryOffset:forAccount:].cold.1
+ -[AKCredentialRequestContext _callerSceneID]
+ -[AKCredentialRequestContext set_callerSceneID:]
+ -[AKDeviceListRequestContext serialNumbers]
+ -[AKDeviceListRequestContext setSerialNumbers:]
+ -[AKDeviceListRequestContext setType:]
+ -[AKDeviceListRequestContext type]
+ -[AKDeviceListResponse _parseDeletedDevicesFromResponseBody:]
+ -[AKDeviceListResponse deletedDeviceList]
+ -[AKDeviceListResponse deletedDevicesCacheExpiryOffset]
+ -[AKDeviceListResponse setDeletedDeviceList:]
+ -[AKDeviceListResponse setDeletedDevicesCacheExpiryOffset:]
+ -[AKRemoteDevice deletedDate]
+ -[AKRemoteDevice removalReason]
+ -[AKRemoteDevice setDeletedDate:]
+ -[AKRemoteDevice setRemovalReason:]
+ -[AKURLBag easyStudentSignInDisabled]
+ -[AKURLBag isEasyStudentSignInDisabled]
+ -[AKUserInformation _parseBeneficiaryInfo:]
+ -[AKUserInformation _parseBeneficiaryInfo:].cold.1
+ -[AKUserInformation _parseBeneficiaryInfo:].cold.2
+ -[AKUserInformation _parseBeneficiaryInfo:].cold.3
+ -[AKUserInformation _parseCustodianInfo:]
+ -[AKUserInformation _parseCustodianInfo:].cold.1
+ -[AKUserInformation _parseCustodianInfo:].cold.2
+ -[AKUserInformation _parseCustodianInfo:].cold.3
+ -[AKUserInformation beneficiaryInfo]
+ -[AKUserInformation initWithResponseBody:].cold.44
+ -[AKUserInformation initWithResponseBody:].cold.45
+ -[AKUserInformation setBeneficiaryInfo:]
+ -[NSError(AuthKit) ak_allUnderlyingErrors]
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table133
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table163
+ GCC_except_table174
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table216
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table240
+ GCC_except_table252
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table257
+ _AKAppleIDAuthenticationAppProvidedContextEasyStudentSignIn
+ _AKCallerSceneIDKey
+ _AKDeletedDevicesCacheExpiryOffsetKey
+ _AKDeletedDevicesKey
+ _AKDeviceDeletedDateKey
+ _AKDeviceRemovalReasonKey
+ _AKInformationBeneficiaryClaimCodeKey
+ _AKInformationBeneficiaryInfoKey
+ _AKInformationBeneficiaryUuidKey
+ _AKInformationBeneficiaryWrappedKeyHashKey
+ _AKInformationCustodianPRKCHashKey
+ _AKInformationCustodianWrappingKeyHashKey
+ _OBJC_CLASS_$_AKAlertImageURLProvider
+ _OBJC_IVAR_$_AKCredentialRequestContext._callerSceneID
+ _OBJC_IVAR_$_AKDeviceListRequestContext._serialNumbers
+ _OBJC_IVAR_$_AKDeviceListRequestContext._type
+ _OBJC_IVAR_$_AKDeviceListResponse._deletedDeviceList
+ _OBJC_IVAR_$_AKDeviceListResponse._deletedDevicesCacheExpiryOffset
+ _OBJC_IVAR_$_AKRemoteDevice._deletedDate
+ _OBJC_IVAR_$_AKRemoteDevice._removalReason
+ _OBJC_IVAR_$_AKURLBag._easyStudentSignInDisabled
+ _OBJC_IVAR_$_AKUserInformation._beneficiaryInfo
+ _OBJC_METACLASS_$_AKAlertImageURLProvider
+ __DeviceIdentityIsSupported
+ __DeviceIdentityIsSupported.cold.1
+ __OBJC_$_CLASS_METHODS_AKAlertImageURLProvider
+ __OBJC_CLASS_RO_$_AKAlertImageURLProvider
+ __OBJC_METACLASS_RO_$_AKAlertImageURLProvider
+ ___41-[AKUserInformation _parseCustodianInfo:]_block_invoke
+ ___43-[AKUserInformation _parseBeneficiaryInfo:]_block_invoke
+ ___61-[AKDeviceListResponse _parseDeletedDevicesFromResponseBody:]_block_invoke
+ ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.103
+ ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.103.cold.1
+ ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.103.cold.2
+ ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.105
+ ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.105.cold.1
+ ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.105.cold.2
+ ___73-[AKAppleIDSigningController(Convenience) signWithBAAHeaders:completion:]_block_invoke.165
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.155
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.157
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.157.cold.1
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.158
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.162
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.162.cold.1
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.159
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.159.cold.1
+ ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.159.cold.2
+ ___block_descriptor_40_e8_32s_e24_v32?0"NSError"8Q16^B24ls32l8
+ ___block_literal_global.139
+ ___block_literal_global.189
+ ___block_literal_global.39
+ ___getDeviceIdentityIsSupportedSymbolLoc_block_invoke
+ __unnamed_array_storage.581
+ _getDeviceIdentityIsSupportedSymbolLoc
+ _getDeviceIdentityIsSupportedSymbolLoc.ptr
+ _kAKAnalyticsEventContinuationTokenDeletion
+ _kAKAnalyticsEventContinuationTokenFetch
+ _kAKAnalyticsEventHeartbeatTokenFetch
+ _kAKAnalyticsEventPasswordResetTokenDeletion
+ _kAKAnalyticsEventPasswordResetTokenFetch
+ _objc_msgSend$IDMSEnvironment
+ _objc_msgSend$URLForResource:withExtension:
+ _objc_msgSend$_identifierForContext:
+ _objc_msgSend$_parseBeneficiaryInfo:
+ _objc_msgSend$_parseCustodianInfo:
+ _objc_msgSend$_parseDeletedDevicesFromResponseBody:
+ _objc_msgSend$_reportTokenWithName:forAccount:error:
+ _objc_msgSend$_reportTokenWithTelemetryID:account:telemetryFlowID:error:
+ _objc_msgSend$ak_allUnderlyingErrors
+ _objc_msgSend$setBeneficiaryInfo:
+ _objc_msgSend$setValue:forKey:
- +[AKFeatureManager overrideAidProxAdvertismentEnabled]
- -[AKAccountManager removeContinuationTokenForAccount:]
- -[AKUserInformation _parseCustodiansInfo:]
- -[AKUserInformation _parseCustodiansInfo:].cold.1
- -[AKUserInformation _parseCustodiansInfo:].cold.2
- -[AKUserInformation _parseCustodiansInfo:].cold.3
- GCC_except_table139
- GCC_except_table151
- GCC_except_table157
- GCC_except_table165
- GCC_except_table176
- GCC_except_table177
- GCC_except_table212
- GCC_except_table215
- GCC_except_table227
- GCC_except_table228
- GCC_except_table229
- GCC_except_table230
- GCC_except_table244
- ___42-[AKUserInformation _parseCustodiansInfo:]_block_invoke
- ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.97
- ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.97.cold.1
- ___66-[AKAppleIDSigningController absintheSignatureForData:completion:]_block_invoke.97.cold.2
- ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.99
- ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.99.cold.1
- ___67-[AKAppleIDSigningController signaturesForData:options:completion:]_block_invoke.99.cold.2
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.149
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.151
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.151.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.152
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.156
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke.156.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.153
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.153.cold.1
- ___79-[AKAppleIDSigningController(Convenience) signingHeadersForRequest:completion:]_block_invoke_2.153.cold.2
- ___block_descriptor_48_e8_32s40s_e15_v32?08Q16^B24ls32l8s40l8
- ___block_literal_global.136
- ___block_literal_global.187
- __unnamed_array_storage.578
- _objc_msgSend$_parseCustodiansInfo:
CStrings:
+ "\x0f\x04!\x1f\x0f\x05"
+ "\x11\x13"
+ "\x1f\x02\x11"
+ "%@...%@"
+ "%@:%ld"
+ "(...%@)"
+ "/\x02\x14\x12"
+ "2"
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\thasModernRecoveryKey: %@,\n}>"
+ "<%@:%p> Name: %@, SN: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld "
+ "<%@:%p> altDSID: %@, deviceListVersion: %@, deviceList: %@, deletedDeviceList: %@, deletedDevicesCacheExpiryOffset: %@"
+ "AKAlertImageURLProvider"
+ "Begin reporting %@ for account: %@"
+ "Beneficiary Info found for account %@"
+ "DeviceIdentityIsSupported"
+ "Exception caught when fetching beneficiaryInfo property: %@"
+ "Exception caught when setting beneficiaryInfo: %@"
+ "Finish reporting %@ for account: %@"
+ "No beneficiary info for account."
+ "No valid Beneficiary Info found in beneficiaryInfoArray."
+ "Parsing beneficiaryInfo."
+ "Parsing custodianInfo."
+ "Reporting  %@ is not supported for non-prod environments"
+ "Reporting not supported for token - %@"
+ "T@\"NSArray\",C,N,V_beneficiaryInfo"
+ "T@\"NSArray\",C,N,V_deletedDeviceList"
+ "T@\"NSArray\",C,N,V_serialNumbers"
+ "T@\"NSDate\",C,N,V_deletedDate"
+ "T@\"NSString\",&,N,V_callerSceneID"
+ "T@\"NSString\",C,N,V_deletedDevicesCacheExpiryOffset"
+ "TB,R,N,GisEasyStudentSignInDisabled,V_easyStudentSignInDisabled"
+ "Tq,N,V_removalReason"
+ "Tq,N,V_type"
+ "URLForResource:withExtension:"
+ "X-Apple-Baa-Avail"
+ "X-Apple-Baa-UE"
+ "_beneficiaryInfo"
+ "_callerSceneID"
+ "_deletedDate"
+ "_deletedDeviceList"
+ "_deletedDevicesCacheExpiryOffset"
+ "_easyStudentSignInDisabled"
+ "_identifierForContext:"
+ "_parseBeneficiaryInfo:"
+ "_parseCustodianInfo:"
+ "_parseDeletedDevicesFromResponseBody:"
+ "_removalReason"
+ "_reportTokenWithName:forAccount:error:"
+ "_reportTokenWithTelemetryID:account:telemetryFlowID:error:"
+ "_serialNumbers"
+ "_type"
+ "ak_allUnderlyingErrors"
+ "appleaccount_mono_icon-60-dark"
+ "beneficiaryInfo"
+ "beneficiaryInfoForAccount:"
+ "beneficiaryUuid"
+ "claimCodeHash"
+ "com.apple.AuthKitUI"
+ "com.apple.authkit.token.ck.delete"
+ "com.apple.authkit.token.ck.fetch"
+ "com.apple.authkit.token.hb.fetch"
+ "com.apple.authkit.token.prk.delete"
+ "com.apple.authkit.token.prk.fetch"
+ "deletedDate"
+ "deletedDeviceList"
+ "deletedDevices"
+ "deletedDevicesCacheExpiryOffset"
+ "deletedDevicesCacheExpiryOffsetForAccount:"
+ "easyStudentSignIn"
+ "easyStudentSignInDisabled"
+ "isEasyStudentSignInDisabled"
+ "png"
+ "prkcHash"
+ "removalReason"
+ "removeContinuationTokenForAccount:telemetryFlowID:error:"
+ "serialNumbers"
+ "setBeneficiaryInfo:"
+ "setBeneficiaryInfo:forAccount:"
+ "setDeletedDate:"
+ "setDeletedDeviceList:"
+ "setDeletedDevicesCacheExpiryOffset:"
+ "setDeletedDevicesCacheExpiryOffset:forAccount:"
+ "setRemovalReason:"
+ "setSerialNumbers:"
+ "setType:"
+ "setValue:forKey:"
+ "set_callerSceneID:"
+ "v32@?0@\"NSError\"8Q16^B24"
+ "wrappedKeyHash"
+ "wrappingKeyHash"
+ "{<%@:%p>: type: %ld, altDSID: %@, forceFetch: %d, os: %@, services: %@, untrusted: %d, family: %d, serialNumbers: %@, }"
- "\x0f\x04!\x1f\x0f\x04"
- "\x1f\x02"
- "/\x01\x14\x12"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\thasModernRecoveryKey: %@,\n}>"
- "<%@:%p> Name: %@, SN: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@"
- "<%@:%p> altDSID: %@, deviceListVersion: %@, deviceList: %@"
- "<%@:%p> altDSID: %@, os: %@, services: %@, untrusted: %d, family: %d, forceFetch: %d"
- "AppleIDSetup"
- "Duplicate custodian UUID %@ with different values (%@ and %@) found in custodianInfos"
- "ProxAdvertisementOverride"
- "_parseCustodiansInfo:"
- "overrideAidProxAdvertismentEnabled"
- "removeContinuationTokenForAccount:"

```
