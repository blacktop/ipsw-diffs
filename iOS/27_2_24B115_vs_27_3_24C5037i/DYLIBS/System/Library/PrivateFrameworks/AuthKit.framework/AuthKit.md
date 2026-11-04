## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-560.125.6.0.0
-  __TEXT.__text: 0x1a56ac
-  __TEXT.__objc_methlist: 0x1091c
-  __TEXT.__const: 0xd30
-  __TEXT.__cstring: 0x132ad
-  __TEXT.__oslogstring: 0x1611e
-  __TEXT.__gcc_except_tab: 0x66fc
+560.250.3.0.0
+  __TEXT.__text: 0x1ab144
+  __TEXT.__objc_methlist: 0x10ca4
+  __TEXT.__const: 0xd40
+  __TEXT.__cstring: 0x137b0
+  __TEXT.__oslogstring: 0x16719
+  __TEXT.__gcc_except_tab: 0x67c4
   __TEXT.__dlopen_cstrs: 0x267
   __TEXT.__ustring: 0x3be
-  __TEXT.__unwind_info: 0x7040
+  __TEXT.__unwind_info: 0x7168
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x79e8
-  __DATA_CONST.__objc_classlist: 0x7f8
+  __DATA_CONST.__const: 0x7b88
+  __DATA_CONST.__objc_classlist: 0x810
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x248
+  __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8348
-  __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x4f0
+  __DATA_CONST.__objc_selrefs: 0x84a8
+  __DATA_CONST.__objc_protorefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0x508
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xbd0
-  __AUTH_CONST.__const: 0x1420
-  __AUTH_CONST.__cfstring: 0x142e0
-  __AUTH_CONST.__objc_const: 0x2f4b0
+  __DATA_CONST.__got: 0xbd8
+  __AUTH_CONST.__const: 0x1440
+  __AUTH_CONST.__cfstring: 0x14920
+  __AUTH_CONST.__objc_const: 0x30218
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x528
-  __AUTH.__objc_data: 0x3660
-  __DATA.__objc_ivar: 0x1284
-  __DATA.__data: 0x1c50
+  __AUTH.__objc_data: 0x3750
+  __DATA.__objc_ivar: 0x12c4
+  __DATA.__data: 0x1dd0
   __DATA_DIRTY.__objc_data: 0x1950
-  __DATA_DIRTY.__bss: 0x2f0
+  __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6189
-  Symbols:   12468
-  CStrings:  4684
+  Functions: 6255
+  Symbols:   12634
+  CStrings:  4764
 
Symbols:
+ +[AKApprovalFlowIdentifiers supportsSecureCoding]
+ +[AKApprovalFlowViewServiceInterface XPCInterface]
+ -[AKAccountManager setStringArray:forAccount:withKey:]
+ -[AKAccountManager stringArrayFromAccount:withKey:]
+ -[AKAnalyticsSender .cxx_destruct]
+ -[AKAnalyticsSender initWithAnalyticsReporter:]
+ -[AKAnalyticsSender init]
+ -[AKAnalyticsSender sendAnalyticsEventNamed:context:account:error:]
+ -[AKAppleIDPasskeyCredential prfOutput]
+ -[AKAppleIDPasskeyCredential setPrfOutput:]
+ -[AKAppleIDPasskeyCredentialRequestContext prfSeed]
+ -[AKAppleIDPasskeyCredentialRequestContext setPrfSeed:]
+ -[AKAppleIDServerResourceLoadDelegate gsTokenIdentifier]
+ -[AKAppleIDServerResourceLoadDelegate pushTransactionID]
+ -[AKAppleIDServerResourceLoadDelegate setGsTokenIdentifier:]
+ -[AKAppleIDServerResourceLoadDelegate setPushTransactionID:]
+ -[AKAppleIDServerResourceLoadDelegate setSkipProcessBAAExclusionCheck:]
+ -[AKAppleIDServerResourceLoadDelegate skipProcessBAAExclusionCheck]
+ -[AKAppleIDSession setSkipProcessBAAExclusionCheck:]
+ -[AKAppleIDSession skipProcessBAAExclusionCheck]
+ -[AKAppleIDSessionContext setSkipProcessExclusionCheck:]
+ -[AKAppleIDSessionContext skipProcessExclusionCheck]
+ -[AKApprovalFlowContext approvalCode]
+ -[AKApprovalFlowContext flowIdentifiers]
+ -[AKApprovalFlowContext initWithCodeType:flowIdentifiers:ruiURLString:pushInfo:approvalCode:cardCopy:serverRequestConfiguration:]
+ -[AKApprovalFlowIdentifiers .cxx_destruct]
+ -[AKApprovalFlowIdentifiers copyWithZone:]
+ -[AKApprovalFlowIdentifiers description]
+ -[AKApprovalFlowIdentifiers encodeWithCoder:]
+ -[AKApprovalFlowIdentifiers flowKey]
+ -[AKApprovalFlowIdentifiers initWithCoder:]
+ -[AKApprovalFlowIdentifiers initWithFlowKey:telemetryFlowID:]
+ -[AKApprovalFlowIdentifiers telemetryFlowID]
+ -[AKAttestationRequestData setSkipProcessExclusionCheck:]
+ -[AKAttestationRequestData skipProcessExclusionCheck]
+ -[AKAuthorizationContext setTelemetryFlowID:]
+ -[AKAuthorizationContext telemetryFlowID]
+ -[AKBasicServerRequest gsTokenID]
+ -[AKBasicServerRequest setGsTokenID:]
+ -[AKCDPFactory beginCreateDBRRecordForPasskeyWithAltDSID:credentialID:prfOutput:force:completion:]
+ -[AKConfiguration approvalFlowTimeoutSecondsOverride]
+ -[AKOSEligibilityManager regulatoryCountryRegionsForDomain:]
+ -[AKSMSCodeApprovalController init]
+ -[AKSMSCodeApprovalController presentSMSApprovalForCode:completion:]
+ -[AKSMSCodeApprovalController validatePrimaryUserIsExpectingSMSCode:completion:]
+ -[AKSMSCodeApprovalController validateSMSSender:completion:]
+ -[AKUserInformation _parsePasskeyDBRInfo:]
+ -[AKUserInformation passkeyDBRCredentialIDsNeedingRecord]
+ -[AKUserInformation passkeyPRFSeed]
+ -[AKUserInformation setPasskeyDBRCredentialIDsNeedingRecord:]
+ -[AKUserInformation setPasskeyPRFSeed:]
+ -[NSData(AuthKit) ak_base64UrlEncodedString]
+ -[NSMutableURLRequest(AuthKit) ak_addAttestationDataHeadersSkippingProcessExclusionCheck:]
+ -[NSMutableURLRequest(AuthKit) ak_addPushTransactionIdHeader:]
+ GCC_except_table107
+ GCC_except_table110
+ GCC_except_table119
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table170
+ GCC_except_table177
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table205
+ GCC_except_table215
+ GCC_except_table218
+ GCC_except_table225
+ GCC_except_table226
+ GCC_except_table237
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table268
+ GCC_except_table291
+ GCC_except_table309
+ GCC_except_table312
+ GCC_except_table315
+ GCC_except_table323
+ GCC_except_table324
+ GCC_except_table364
+ GCC_except_table373
+ GCC_except_table374
+ GCC_except_table385
+ GCC_except_table386
+ _AKAppleIDAuthenticationAppProvidedContextApproval
+ _AKAppleSMSSenderListKey
+ _AKAuthenticationSMSCodeHeaderField
+ _AKOSEDomainTeenAttachedToFamilyOfferToJoin
+ _AKPasskeyDBRCredentialIDResponseKey
+ _AKPasskeyDBRInfoResponseKey
+ _AKPasskeyDBRNeedsRecordResponseKey
+ _AKPasskeyDBRPRFSeedResponseKey
+ _AKPasskeyDBRPasskeysResponseKey
+ _AKSecrecyFeatureServerDrivenApprovalFlowSMS
+ _AKTTRComponentID
+ _AKTTRComponentName
+ _AKTTRComponentVersion
+ _AKTemporaryCollectRiskingSignalsHeaderKey
+ _AKTemporaryRiskingSignalsHeaderKey
+ _AKURLBagKeyFetchPasskeyPrfSalt
+ _AKURLBagKeyHasActiveSMSCode
+ _AKURLBagKeyPDPRecreateWithFallback
+ _AKURLBagKeyPresentSMSProtectionFlow
+ _AKURLBagKeySMSApprovalFlowEnabled
+ _AKURLBagKeySavePasskeyPrfSalt
+ _OBJC_CLASS_$_AKApprovalFlowIdentifiers
+ _OBJC_CLASS_$_AKApprovalFlowViewServiceInterface
+ _OBJC_CLASS_$_AKSMSCodeApprovalController
+ _OBJC_IVAR_$_AKAnalyticsSender._analyticsReporter
+ _OBJC_IVAR_$_AKAppleIDPasskeyCredential._prfOutput
+ _OBJC_IVAR_$_AKAppleIDPasskeyCredentialRequestContext._prfSeed
+ _OBJC_IVAR_$_AKAppleIDServerResourceLoadDelegate._gsTokenIdentifier
+ _OBJC_IVAR_$_AKAppleIDServerResourceLoadDelegate._pushTransactionID
+ _OBJC_IVAR_$_AKAppleIDServerResourceLoadDelegate._skipProcessBAAExclusionCheck
+ _OBJC_IVAR_$_AKAppleIDSession._skipProcessBAAExclusionCheck
+ _OBJC_IVAR_$_AKAppleIDSessionContext._skipProcessExclusionCheck
+ _OBJC_IVAR_$_AKApprovalFlowContext._approvalCode
+ _OBJC_IVAR_$_AKApprovalFlowContext._flowIdentifiers
+ _OBJC_IVAR_$_AKApprovalFlowIdentifiers._flowKey
+ _OBJC_IVAR_$_AKApprovalFlowIdentifiers._telemetryFlowID
+ _OBJC_IVAR_$_AKAttestationRequestData._skipProcessExclusionCheck
+ _OBJC_IVAR_$_AKAuthorizationContext._telemetryFlowID
+ _OBJC_IVAR_$_AKBasicServerRequest._gsTokenID
+ _OBJC_IVAR_$_AKUserInformation._passkeyDBRCredentialIDsNeedingRecord
+ _OBJC_IVAR_$_AKUserInformation._passkeyPRFSeed
+ _OBJC_METACLASS_$_AKApprovalFlowIdentifiers
+ _OBJC_METACLASS_$_AKApprovalFlowViewServiceInterface
+ _OBJC_METACLASS_$_AKSMSCodeApprovalController
+ __AKAppleIDSessionContextSkipProcessExclusionCheckKey
+ __AKApprovalFlowTimeoutSecondsOverrideKey
+ __AKPushTransactionID
+ __OBJC_$_CLASS_METHODS_AKApprovalFlowIdentifiers
+ __OBJC_$_CLASS_METHODS_AKApprovalFlowViewServiceInterface
+ __OBJC_$_CLASS_PROP_LIST_AKApprovalFlowIdentifiers
+ __OBJC_$_INSTANCE_METHODS_AKAnalyticsSender
+ __OBJC_$_INSTANCE_METHODS_AKApprovalFlowIdentifiers
+ __OBJC_$_INSTANCE_METHODS_AKSMSCodeApprovalController
+ __OBJC_$_INSTANCE_VARIABLES_AKAnalyticsSender
+ __OBJC_$_INSTANCE_VARIABLES_AKApprovalFlowIdentifiers
+ __OBJC_$_PROP_LIST_AKApprovalFlowIdentifiers
+ __OBJC_$_PROP_LIST_AKCDPFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKAnisetteDataProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKApprovalFlowViewServiceProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKCDPFactoryProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKODIAssessmentSending
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKAnisetteDataProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKApprovalFlowViewServiceProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKCDPFactoryProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKODIAssessmentSending
+ __OBJC_$_PROTOCOL_REFS_AKAnisetteDataProviding
+ __OBJC_$_PROTOCOL_REFS_AKApprovalFlowViewServiceProtocol
+ __OBJC_$_PROTOCOL_REFS_AKCDPFactoryProtocol
+ __OBJC_$_PROTOCOL_REFS_AKODIAssessmentSending
+ __OBJC_CLASS_PROTOCOLS_$_AKAnisetteProvisioningController
+ __OBJC_CLASS_PROTOCOLS_$_AKApprovalFlowIdentifiers
+ __OBJC_CLASS_PROTOCOLS_$_AKCDPFactory
+ __OBJC_CLASS_RO_$_AKApprovalFlowIdentifiers
+ __OBJC_CLASS_RO_$_AKApprovalFlowViewServiceInterface
+ __OBJC_CLASS_RO_$_AKSMSCodeApprovalController
+ __OBJC_LABEL_PROTOCOL_$_AKAnisetteDataProviding
+ __OBJC_LABEL_PROTOCOL_$_AKApprovalFlowViewServiceProtocol
+ __OBJC_LABEL_PROTOCOL_$_AKCDPFactoryProtocol
+ __OBJC_LABEL_PROTOCOL_$_AKODIAssessmentSending
+ __OBJC_METACLASS_RO_$_AKApprovalFlowIdentifiers
+ __OBJC_METACLASS_RO_$_AKApprovalFlowViewServiceInterface
+ __OBJC_METACLASS_RO_$_AKSMSCodeApprovalController
+ __OBJC_PROTOCOL_$_AKAnisetteDataProviding
+ __OBJC_PROTOCOL_$_AKApprovalFlowViewServiceProtocol
+ __OBJC_PROTOCOL_$_AKCDPFactoryProtocol
+ __OBJC_PROTOCOL_$_AKODIAssessmentSending
+ __OBJC_PROTOCOL_REFERENCE_$_AKApprovalFlowViewServiceProtocol
+ ___50+[AKApprovalFlowViewServiceInterface XPCInterface]_block_invoke
+ ___60-[AKSMSCodeApprovalController validateSMSSender:completion:]_block_invoke
+ ___68-[AKSMSCodeApprovalController presentSMSApprovalForCode:completion:]_block_invoke
+ ___80-[AKSMSCodeApprovalController validatePrimaryUserIsExpectingSMSCode:completion:]_block_invoke
+ ___98-[AKCDPFactory beginCreateDBRRecordForPasskeyWithAltDSID:credentialID:prfOutput:force:completion:]_block_invoke
+ ___block_descriptor_64_e8_32bs40r_e20_v20?0B8"NSError"12ls32l8r40l8
+ ___getASAuthorizationPublicKeyCredentialPRFAssertionInputValuesClass_block_invoke
+ ___getASAuthorizationPublicKeyCredentialPRFRegistrationInputClass_block_invoke
+ _getASAuthorizationPublicKeyCredentialPRFAssertionInputValuesClass
+ _getASAuthorizationPublicKeyCredentialPRFAssertionInputValuesClass.softClass
+ _getASAuthorizationPublicKeyCredentialPRFRegistrationInputClass
+ _getASAuthorizationPublicKeyCredentialPRFRegistrationInputClass.softClass
+ _kAKAnalyticsApprovalCodeType
+ _kAKAnalyticsEvent2FAApprovalFlowEnd
+ _kAKAnalyticsEvent2FAApprovalFlowStart
+ _kAKAnalyticsEventAppleSMSSenderDetected
+ _kAKAnalyticsEventCallSignalsRequested
+ _kAKAnalyticsEventCheck2FACodeLegitimacy
+ _kAKAnalyticsEventCodeDisplayedWithInvisibleInk
+ _kAKAnalyticsEventInvisibleInkRemovedFromCode
+ _kAKAnalyticsEventLocalAuthentication
+ _kAKAnalyticsEventPushReceived
+ _kAKAnalyticsEventSignInDisclosure
+ _kAKApprovalFlowApprovalCodeKey
+ _kAKApprovalFlowFlowIdentifiersKey
+ _kAKApprovalFlowIdentifiersFlowKeyKey
+ _kAKApprovalFlowIdentifiersTelemetryFlowIDKey
+ _kAKBasicServerRequestGSTokenID
+ _kAKTeenAttachedToFamilyOfferToJoinDomain
+ _kApprovalFlowSMSRemoteUITag
+ _kApprovalFlowSignInDisclosureViewRemoteUITag
- -[AKApprovalFlowContext initWithCodeType:messageId:ruiURLString:pushInfo:cardCopy:serverRequestConfiguration:]
- -[AKApprovalFlowContext messageId]
- GCC_except_table112
- GCC_except_table120
- GCC_except_table121
- GCC_except_table124
- GCC_except_table152
- GCC_except_table153
- GCC_except_table167
- GCC_except_table168
- GCC_except_table175
- GCC_except_table179
- GCC_except_table189
- GCC_except_table192
- GCC_except_table201
- GCC_except_table212
- GCC_except_table213
- GCC_except_table216
- GCC_except_table220
- GCC_except_table228
- GCC_except_table239
- GCC_except_table265
- GCC_except_table266
- GCC_except_table272
- GCC_except_table292
- GCC_except_table293
- GCC_except_table311
- GCC_except_table314
- GCC_except_table317
- GCC_except_table335
- GCC_except_table336
- GCC_except_table366
- GCC_except_table375
- GCC_except_table376
- _OBJC_IVAR_$_AKApprovalFlowContext._messageId
- _kAKApprovalFlowMessageIdKey
CStrings:
+ "621449"
+ "<%@: %p codeType=%@ flowIdentifiers=%@ ruiURLString=%@ hasPushInfo=%@ cardCopy=%@>"
+ "<%@: %p flowKey=%@ telemetryFlowID=%@>"
+ "<%@: %p; altDSID=%@, urlBagKey=%@, requestBody=%@, additionalHeaders=%@, expectedResponseFormat=%lu, requestBodyFormat=%lu, telemetryFlowID=%@, gsTokenID=%@>"
+ "A sender number was not provided."
+ "AKApprovalFlowContext initialization failed, nil flowIdentifiers"
+ "AKApprovalFlowIdentifiers initialization failed, nil flowKey"
+ "ASAuthorizationPublicKeyCredentialPRFAssertionInputValues"
+ "ASAuthorizationPublicKeyCredentialPRFRegistrationInput"
+ "All"
+ "An SMS code was not provided."
+ "Authentication service returned an XPC error presenting SMS approval: %@"
+ "Authentication service returned an XPC error validating SMS sender: %@"
+ "Authentication service returned an XPC error validating expected SMS code: %@"
+ "BEGIN [%lld]: PresentSMSApproval  enableTelemetry=YES "
+ "BEGIN [%lld]: ValidatePrimaryUserIsExpectingCode  enableTelemetry=YES "
+ "BEGIN [%lld]: ValidateSMSSender  enableTelemetry=YES "
+ "CoreCDP stateController does not support beginCreateDBRRecordForPasskeyWithCredentialID:prfOutput:force:completion:"
+ "Creating passkey recovery record, force=%d"
+ "Dispatching SMS approval presentation to daemon"
+ "Dispatching SMS code validation to daemon"
+ "Dispatching SMS sender validation to daemon"
+ "END [%lld] %fs:PresentSMSApproval "
+ "END [%lld] %fs:ValidatePrimaryUserIsExpectingCode "
+ "END [%lld] %fs:ValidateSMSSender "
+ "Invalid domain string for regulatory regions: %@"
+ "No CDP context for the requested altDSID - refusing to create a passkey recovery record"
+ "No stored GS token for identifier %@"
+ "Passkey recovery record created."
+ "Passkey recovery record creation failed with error %{private}@"
+ "PasskeyDBR"
+ "PresentSMSApproval"
+ "Received server time [%@], from - %@"
+ "SMS"
+ "SMSCode"
+ "ServerDrivenApprovalFlowSMS"
+ "SignInDisclosureView"
+ "Signing request with GS token for identifier %@"
+ "Successfully obtained passkey credential."
+ "TEEN_ATTACHED_TO_FAMILY_OFFER_TO_JOIN"
+ "Teen attached to family offer to join - setting AKOSEOptionTeenAttachedToFamilyOfferToJoin flag"
+ "User is teen, using teen attached to family offer to join domain"
+ "ValidatePrimaryUserIsExpectingCode"
+ "ValidateSMSSender"
+ "X-Apple-Collect-Risking-Signals"
+ "X-Apple-I-Push-Txn-Id"
+ "X-Apple-I-SMS-Code"
+ "X-Apple-Risking-Signals"
+ "_AKApprovalFlowTimeoutSecondsOverride"
+ "_approvalCode"
+ "_flowIdentifiers"
+ "_flowKey"
+ "_gsTokenIdentifier"
+ "_passkeyDBRCredentialIDsNeedingRecord"
+ "_passkeyPRFSeed"
+ "_prfOutput"
+ "_prfSeed"
+ "_pushTransactionID"
+ "_skipProcessBAAExclusionCheck"
+ "_skipProcessExclusionCheck"
+ "abpSmsEnabled"
+ "appleSmsSenderList"
+ "approval"
+ "approvalCodeType"
+ "com.apple.authkit.callsignalsRequested"
+ "com.apple.authkit.codeDisplayedWithinvisibleInk"
+ "com.apple.authkit.grayTextDisclosures"
+ "com.apple.authkit.invisibleInkRemovedFromCode"
+ "com.apple.authkit.localAuthentication"
+ "com.apple.authkit.pushReceived"
+ "com.apple.authkit.signIn.2FAApprovalFlowEnd"
+ "com.apple.authkit.signIn.2FAApprovalFlowStart"
+ "com.apple.authkit.signIn.appleSMSSenderDetected"
+ "com.apple.authkit.signIn.check2FACodeLegitimacy"
+ "credentialId"
+ "fetchPrfSalt"
+ "gsTokenID"
+ "hsa2SmsAuthApprovalFlowUrl"
+ "needsDBRRecord"
+ "passkeyDBRInfo"
+ "passkeys"
+ "pdpRecreateWithFallback"
+ "prfSeed"
+ "savePrfSalt"
+ "validActiveSmsCodeUrl"
- "<%@: %p codeType=%@ messageId=%@ ruiURLString=%@ hasPushInfo=%@ cardCopy=%@>"
- "<%@: %p; altDSID=%@, urlBagKey=%@, requestBody=%@, additionalHeaders=%@, expectedResponseFormat=%lu, requestBodyFormat=%lu, telemetryFlowID=%@>"
- "AKApprovalFlowContext initialization failed, nil messageId"
- "Successfully obtained passkey credential: %@"
- "_messageId"
```
