## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/Versions/A/PassKitCore`

```diff

-1581.2.1.0.0
-  __TEXT.__text: 0x793c54
-  __TEXT.__auth_stubs: 0x4490
-  __TEXT.__objc_methlist: 0x5ebf4
-  __TEXT.__const: 0xd650
-  __TEXT.__cstring: 0x60f2f
-  __TEXT.__swift5_typeref: 0x49d6
+1583.4.1.0.0
+  __TEXT.__text: 0x797468
+  __TEXT.__auth_stubs: 0x44e0
+  __TEXT.__objc_methlist: 0x5ee34
+  __TEXT.__const: 0xd690
+  __TEXT.__cstring: 0x610d7
+  __TEXT.__swift5_typeref: 0x49e0
   __TEXT.__swift5_capture: 0x2dec
-  __TEXT.__oslogstring: 0x2d99b
-  __TEXT.__constg_swiftt: 0x44e8
-  __TEXT.__swift5_fieldmd: 0x49f4
-  __TEXT.__swift5_reflstr: 0x3c2d
+  __TEXT.__oslogstring: 0x2da9e
+  __TEXT.__constg_swiftt: 0x450c
+  __TEXT.__swift5_fieldmd: 0x4a10
+  __TEXT.__swift5_reflstr: 0x3c4d
   __TEXT.__swift5_builtin: 0x320
   __TEXT.__swift5_assocty: 0x7b0
   __TEXT.__swift5_proto: 0xaf0
-  __TEXT.__swift5_types: 0x49c
+  __TEXT.__swift5_types: 0x4a0
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0xe0
   __TEXT.__gcc_except_tab: 0x6d04
   __TEXT.__ustring: 0x1ed6
-  __TEXT.__unwind_info: 0x19b50
-  __TEXT.__eh_frame: 0x4588
-  __TEXT.__objc_classname: 0xeb64
-  __TEXT.__objc_methname: 0xba5ed
-  __TEXT.__objc_methtype: 0x15696
-  __TEXT.__objc_stubs: 0x506a0
-  __DATA_CONST.__got: 0x3e00
-  __DATA_CONST.__const: 0xe850
-  __DATA_CONST.__objc_classlist: 0x36b0
+  __TEXT.__unwind_info: 0x19c10
+  __TEXT.__eh_frame: 0x45e8
+  __TEXT.__objc_classname: 0xebac
+  __TEXT.__objc_methname: 0xba9d4
+  __TEXT.__objc_methtype: 0x15736
+  __TEXT.__objc_stubs: 0x507a0
+  __DATA_CONST.__got: 0x3e58
+  __DATA_CONST.__const: 0xe968
+  __DATA_CONST.__objc_classlist: 0x36c0
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb80
+  __DATA_CONST.__objc_selrefs: 0x1fc38
   __DATA_CONST.__objc_protorefs: 0x1e0
-  __DATA_CONST.__objc_superrefs: 0x2b30
-  __DATA_CONST.__objc_arraydata: 0x3078
-  __AUTH_CONST.__auth_got: 0x2258
-  __AUTH_CONST.__auth_ptr: 0x8a0
-  __AUTH_CONST.__const: 0x254d8
-  __AUTH_CONST.__cfstring: 0x68360
-  __AUTH_CONST.__objc_const: 0xc2358
-  __AUTH_CONST.__objc_arrayobj: 0xa98
+  __DATA_CONST.__objc_superrefs: 0x2b40
+  __DATA_CONST.__objc_arraydata: 0x3080
+  __AUTH_CONST.__auth_got: 0x2280
+  __AUTH_CONST.__auth_ptr: 0x8c0
+  __AUTH_CONST.__const: 0x254a0
+  __AUTH_CONST.__cfstring: 0x685e0
+  __AUTH_CONST.__objc_const: 0xc2770
+  __AUTH_CONST.__objc_arrayobj: 0xab0
   __AUTH_CONST.__objc_dictobj: 0x1d88
   __AUTH_CONST.__objc_intobj: 0xfd8
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH.__objc_data: 0x111a0
+  __AUTH.__objc_data: 0x11248
   __AUTH.__data: 0x2fd0
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x8358
+  __DATA.__objc_ivar: 0x8390
   __DATA.__data: 0x6d18
   __DATA.__bss: 0x15bc8
   __DATA.__common: 0x1b0

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SEService.framework/Versions/A/SEService
+  - /System/Library/PrivateFrameworks/Sharing.framework/Versions/A/Sharing
   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libDiagnosticMessagesClient.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 46288
-  Symbols:   80852
-  CStrings:  15299
+  Functions: 46365
+  Symbols:   80977
+  CStrings:  15322
 
Symbols:
+ +[PKPaymentOfferCriteriaIneligibleDetails ineligibleDetailsWithReason:preferredLanguage:criteria:isWebPaymentRequest:]
+ +[PKPaymentOfferCriteriaIneligibleDetails ineligibleDetailsWithReason:preferredLanguage:overrideDisplayString:criteria:isWebPaymentRequest:]
+ +[PKPeerPaymentFailureDiagnostic supportsSecureCoding]
+ -[PKACAccountChange event]
+ -[PKACAccountChange initWithChangeType:event:newAccount:oldAccount:]
+ -[PKAccountUser hasHandle:]
+ -[PKAnalyticsReporter bucketedSessionDurationFromDuration:]
+ -[PKDashboardTransactionFetcher filterPeerPaymentPaymentMode:]
+ -[PKEventDateInfo timeZone]
+ -[PKFamilyMember hasAppleIDAlias:]
+ -[PKPaymentAuthorizationDataModel canSupportDisbursementsOnRemoteDevice:]
+ -[PKPaymentOfferCriteriaIneligibleDetails initWithIneligibleDetailsWithReason:overrideDisplayString:preferredLanguage:criteria:isWebPaymentRequest:]
+ -[PKPaymentOfferCriteriaIneligibleDetails isWebPaymentRequest]
+ -[PKPaymentSetupField setSource:]
+ -[PKPaymentSetupField source]
+ -[PKPaymentSetupField submissionStringMeetsValidationRegex]
+ -[PKPaymentSetupField supportsAddressAutofill]
+ -[PKPaymentSetupFieldBuiltInAddressLine1 supportsAddressAutofill]
+ -[PKPaymentSetupFieldBuiltInAddressLine2 supportsAddressAutofill]
+ -[PKPaymentSetupFieldBuiltInCity supportsAddressAutofill]
+ -[PKPaymentSetupFieldBuiltInPostalCode supportsAddressAutofill]
+ -[PKPaymentSetupFieldBuiltInState supportsAddressAutofill]
+ -[PKPaymentSetupFieldText codeOnError]
+ -[PKPaymentSetupFieldText setCodeOnError:]
+ -[PKPaymentSetupFieldText setValidationRegex:]
+ -[PKPaymentSetupFieldText submissionStringMeetsValidationRegex]
+ -[PKPaymentSetupFieldText validationRegex]
+ -[PKPaymentSetupFieldsModel prefillDefaultValuesWithPostalAddress:]
+ -[PKPaymentToken initWithPaymentMethod:transactionIdentifier:paymentData:]
+ -[PKPeerPaymentFailureDiagnostic .cxx_destruct]
+ -[PKPeerPaymentFailureDiagnostic encodeWithCoder:]
+ -[PKPeerPaymentFailureDiagnostic error]
+ -[PKPeerPaymentFailureDiagnostic flowType]
+ -[PKPeerPaymentFailureDiagnostic initWithCoder:]
+ -[PKPeerPaymentFailureDiagnostic reasonCode]
+ -[PKPeerPaymentFailureDiagnostic role]
+ -[PKPeerPaymentFailureDiagnostic setError:]
+ -[PKPeerPaymentFailureDiagnostic setFlowType:]
+ -[PKPeerPaymentFailureDiagnostic setReasonCode:]
+ -[PKPeerPaymentFailureDiagnostic setRole:]
+ -[PKPeerPaymentFailureDiagnostic setTransactionIdentifier:]
+ -[PKPeerPaymentFailureDiagnostic transactionIdentifier]
+ -[PKPeerPaymentFailureDiagnosticRequest .cxx_destruct]
+ -[PKPeerPaymentFailureDiagnosticRequest _urlRequestWithServiceURL:appleAccountInformation:]
+ -[PKPeerPaymentFailureDiagnosticRequest initWithFailureDiagnostic:]
+ -[PKPeerPaymentIdentityVerificationResponse useDeviceValidation]
+ -[PKPeerPaymentService reportFailureDiagnostic:completion:]
+ -[PKPeerPaymentWebService peerPaymentFailureDiagnosticWithRequest:withCompletion:]
+ GCC_except_table394
+ GCC_except_table590
+ GCC_except_table633
+ GCC_except_table641
+ OBJC_IVAR_$_PKACAccountChange._event
+ OBJC_IVAR_$_PKDashboardTransactionFetcher._peerPaymentPaymentMode
+ OBJC_IVAR_$_PKEventDateInfo._timeZone
+ OBJC_IVAR_$_PKPaymentOfferCriteriaIneligibleDetails._isWebPaymentRequest
+ OBJC_IVAR_$_PKPaymentSetupField._source
+ OBJC_IVAR_$_PKPeerPaymentFailureDiagnostic._error
+ OBJC_IVAR_$_PKPeerPaymentFailureDiagnostic._flowType
+ OBJC_IVAR_$_PKPeerPaymentFailureDiagnostic._reasonCode
+ OBJC_IVAR_$_PKPeerPaymentFailureDiagnostic._role
+ OBJC_IVAR_$_PKPeerPaymentFailureDiagnostic._transactionIdentifier
+ OBJC_IVAR_$_PKPeerPaymentFailureDiagnosticRequest._failureDiagnostic
+ _OBJC_CLASS_$_PKPeerPaymentFailureDiagnostic
+ _OBJC_CLASS_$_PKPeerPaymentFailureDiagnosticRequest
+ _OBJC_METACLASS_$_PKPeerPaymentFailureDiagnostic
+ _OBJC_METACLASS_$_PKPeerPaymentFailureDiagnosticRequest
+ _PKACAccountChangeEventDescription
+ _PKAccessibilityIdentifierNearby
+ _PKAnalyticsReportAcceptAsButtonTag
+ _PKAnalyticsReportAcceptButtonTag
+ _PKAnalyticsReportCardDetailsButtonTag
+ _PKAnalyticsReportDeclineButtonTag
+ _PKAnalyticsReportEventTypePaymentBalanceUpdated
+ _PKAnalyticsReportIsRemoteRequestKey
+ _PKAnalyticsReportPayLaterInitialOfferDetailsTag
+ _PKAnalyticsReportPeerPaymentAmountSelectionPageTag
+ _PKAnalyticsReportPeerPaymentDeviceTapPaymentAuthPageTag
+ _PKAnalyticsReportPeerPaymentDeviceTapPaymentDetailsPageTag
+ _PKAnalyticsReportPeerPaymentDeviceTapReadyToAcceptPageTag
+ _PKAnalyticsReportPeerPaymentP2PContextDeviceTap
+ _PKAnalyticsReportPeerPaymentP2PSendStateAcceptOrDeclineKey
+ _PKAnalyticsReportPeerPaymentP2PSendStateKey
+ _PKAnalyticsReportPeerPaymentP2PSendStateReadyKey
+ _PKAnalyticsReportPeerPaymentP2PSendStateSendingKey
+ _PKAnalyticsReportPeerPaymentP2PSendStateSentKey
+ _PKAnalyticsReportPeerPaymentP2PSideRecipient
+ _PKAnalyticsReportReferralSourceButtonTap
+ _PKAnalyticsReportReferralSourceScannedCode
+ _PKDeviceModel
+ _PKPassEventDateInfoKeyTimeZone
+ _PKPassKeyUseAutomaticColors
+ _PKPaymentFieldTextCodeOnErrorKey
+ _PKPaymentFieldTextValidationRegexKey
+ _PKPaymentOffersUseEphemeralSessionEnabled
+ _PKPaymentOffersUseEphemeralSessionKey
+ _PKPaymentSetupFieldSourceFromString
+ _PKPaymentSetupFieldSourceToString
+ _PKPaymentSetupFieldsModelFieldSourcesKey
+ _PKPeerPaymentSetupFieldSubmissionValueAddressSourceKey
+ _PKRemoteNetworkPaymentLoadingViewDelay
+ _PKRemoteNetworkPaymentLoadingViewDelayKey
+ _PKRemoteNetworkPaymentLoadingViewHold
+ _PKRemoteNetworkPaymentLoadingViewHoldKey
+ _PKSetRemoteNetworkPaymentLoadingViewDelay
+ _PKSetRemoteNetworkPaymentLoadingViewHold
+ _PKStartOfMonthWithTimeZone
+ __152-[PKPaymentRequirementsRequest _urlRequestWithServiceURL:deviceIdentifier:appleAccountInformation:certChain:devSigned:deviceData:webService:completion:]_block_invoke.346
+ __152-[PKPaymentRequirementsRequest _urlRequestWithServiceURL:deviceIdentifier:appleAccountInformation:certChain:devSigned:deviceData:webService:completion:]_block_invoke.377
+ __49-[PKPaymentSetupFieldsModel prefillDefaultValues]_block_invoke.39
+ __49-[PKPaymentSetupFieldsModel prefillDefaultValues]_block_invoke.50
+ __52-[PKPaymentAuthorizationDataModel unavailablePasses]_block_invoke.174
+ __59-[PKPeerPaymentService reportFailureDiagnostic:completion:]_block_invoke.170
+ __72-[PKPaymentAuthorizationCoordinator listener:shouldAcceptNewConnection:]_block_invoke.66
+ __87-[PKPaymentAuthorizationCoordinatorExportedObject authorizationDidSelectPaymentMethod:]_block_invoke.334
+ __88-[PKPaymentAuthorizationCoordinatorExportedObject authorizationDidSelectShippingMethod:]_block_invoke.310
+ __89-[PKPaymentAuthorizationCoordinatorExportedObject authorizationDidSelectShippingAddress:]_block_invoke.322
+ __OBJC_$_CLASS_METHODS_PKPeerPaymentFailureDiagnostic
+ __OBJC_$_CLASS_PROP_LIST_PKPeerPaymentFailureDiagnostic
+ __OBJC_$_INSTANCE_METHODS_PKPeerPaymentFailureDiagnostic
+ __OBJC_$_INSTANCE_METHODS_PKPeerPaymentFailureDiagnosticRequest
+ __OBJC_$_INSTANCE_VARIABLES_PKPeerPaymentFailureDiagnostic
+ __OBJC_$_INSTANCE_VARIABLES_PKPeerPaymentFailureDiagnosticRequest
+ __OBJC_$_PROP_LIST_PKPeerPaymentFailureDiagnostic
+ __OBJC_CLASS_PROTOCOLS_$_PKPeerPaymentFailureDiagnostic
+ __OBJC_CLASS_RO_$_PKPeerPaymentFailureDiagnostic
+ __OBJC_CLASS_RO_$_PKPeerPaymentFailureDiagnosticRequest
+ __OBJC_METACLASS_RO_$_PKPeerPaymentFailureDiagnostic
+ __OBJC_METACLASS_RO_$_PKPeerPaymentFailureDiagnosticRequest
+ __PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1024
+ __Z20PKTimeStringFromDateP6NSDateP10NSTimeZone
+ __Z31PKDateRangeStringFromDateToDateP6NSDateS0_bbbP10NSTimeZone
+ __Z33PKMediumDayAndMonthStringFromDateP6NSDateP10NSTimeZone
+ ___35-[PKGroupsController accountAdded:]_block_invoke
+ ___37-[PKGroupsController accountChanged:]_block_invoke
+ ___37-[PKGroupsController accountRemoved:]_block_invoke
+ ___59-[PKPeerPaymentService reportFailureDiagnostic:completion:]_block_invoke
+ ___59-[PKPeerPaymentService reportFailureDiagnostic:completion:]_block_invoke_2
+ ___59-[PKPeerPaymentService reportFailureDiagnostic:completion:]_block_invoke_3
+ ___67-[PKPaymentSetupFieldsModel prefillDefaultValuesWithPostalAddress:]_block_invoke
+ ___67-[PKPaymentSetupFieldsModel prefillDefaultValuesWithPostalAddress:]_block_invoke_2
+ ___82-[PKPeerPaymentWebService peerPaymentFailureDiagnosticWithRequest:withCompletion:]_block_invoke
+ ____Z20PKTimeStringFromDateP6NSDateP10NSTimeZone_block_invoke
+ ____Z33PKMediumDayAndMonthStringFromDateP6NSDateP10NSTimeZone_block_invoke
+ __block_literal_global.1023
+ __block_literal_global.1051
+ __block_literal_global.160
+ __block_literal_global.1860
+ __block_literal_global.196
+ __block_literal_global.2572
+ __block_literal_global.2589
+ __block_literal_global.27
+ __block_literal_global.42
+ __block_literal_global.425
+ __block_literal_global.657
+ __block_literal_global.800
+ __block_literal_global.871
+ _objc_msgSend$bucketedSessionDurationFromDuration:
+ _objc_msgSend$canSupportDisbursementsOnRemoteDevice:
+ _objc_msgSend$flowType
+ _objc_msgSend$ineligibleDetailsWithReason:preferredLanguage:criteria:isWebPaymentRequest:
+ _objc_msgSend$ineligibleDetailsWithReason:preferredLanguage:overrideDisplayString:criteria:isWebPaymentRequest:
+ _objc_msgSend$initWithChangeType:event:newAccount:oldAccount:
+ _objc_msgSend$initWithIneligibleDetailsWithReason:overrideDisplayString:preferredLanguage:criteria:isWebPaymentRequest:
+ _objc_msgSend$reasonCode
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$reportFailureDiagnostic:completion:
+ _objc_msgSend$setCodeOnError:
+ _objc_msgSend$setPeerPaymentPaymentMode:
+ _objc_msgSend$setValidationRegex:
+ _objc_msgSend$submissionStringMeetsValidationRegex
+ _objc_msgSend$supportsAddressAutofill
+ _objc_msgSend$validationRegex
+ _symbolic _____ 11PassKitCore43NearbyPeerPaymentFailureDiagnosticUtilitiesO
+ _symbolic _____Sg 7Sharing13SFAirDropSendO7FailureO
+ _symbolic _____Sg 7Sharing16SFAirDropReceiveO7FailureO
+ block_copy_helper.62
+ block_copy_helper.70
+ block_descriptor.64
+ block_descriptor.72
+ block_destroy_helper.63
+ block_destroy_helper.71
- +[PKPaymentOfferCriteriaIneligibleDetails ineligibleDetailsWithReason:preferredLanguage:criteria:]
- +[PKPaymentOfferCriteriaIneligibleDetails ineligibleDetailsWithReason:preferredLanguage:overrideDisplayString:criteria:]
- -[PKPaymentOfferCriteriaIneligibleDetails initWithIneligibleDetailsWithReason:overrideDisplayString:preferredLanguage:criteria:]
- GCC_except_table174
- GCC_except_table22
- GCC_except_table585
- GCC_except_table628
- GCC_except_table636
- _PKAnalyticsReportPassDetailsButtonTag
- _PKAnalyticsReportReferralSourceQRCode
- _PKDisableIdentitySecurityCheckInHeaderEnabled
- _PKDisableIdentitySecurityCheckInHeaderKey
- _PKSendLegacyProvisioningParametersEnabled
- _PKSendLegacyProvisioningParametersKey
- __152-[PKPaymentRequirementsRequest _urlRequestWithServiceURL:deviceIdentifier:appleAccountInformation:certChain:devSigned:deviceData:webService:completion:]_block_invoke.352
- __152-[PKPaymentRequirementsRequest _urlRequestWithServiceURL:deviceIdentifier:appleAccountInformation:certChain:devSigned:deviceData:webService:completion:]_block_invoke.383
- __49-[PKPaymentSetupFieldsModel prefillDefaultValues]_block_invoke.36
- __49-[PKPaymentSetupFieldsModel prefillDefaultValues]_block_invoke.47
- __52-[PKPaymentAuthorizationDataModel unavailablePasses]_block_invoke.176
- __72-[PKPaymentAuthorizationCoordinator listener:shouldAcceptNewConnection:]_block_invoke.65
- __87-[PKPaymentAuthorizationCoordinatorExportedObject authorizationDidSelectPaymentMethod:]_block_invoke.333
- __88-[PKPaymentAuthorizationCoordinatorExportedObject authorizationDidSelectShippingMethod:]_block_invoke.309
- __89-[PKPaymentAuthorizationCoordinatorExportedObject authorizationDidSelectShippingAddress:]_block_invoke.321
- __PKPeerPaymentRemoveRecurringPaymentRecentMemoIcon_block_invoke.1027
- ___49-[PKPaymentProvisioningRequest _secureParameters]_block_invoke_3
- ___49-[PKPaymentProvisioningRequest _secureParameters]_block_invoke_4
- ___49-[PKPaymentProvisioningRequest _secureParameters]_block_invoke_5
- ___PKMediumDayAndMonthStringFromDate_block_invoke
- ___PKTimeStringFromDate_block_invoke
- __block_literal_global.1026
- __block_literal_global.1045
- __block_literal_global.155
- __block_literal_global.169
- __block_literal_global.179
- __block_literal_global.1879
- __block_literal_global.2591
- __block_literal_global.2608
- __block_literal_global.424
- __block_literal_global.614
- __block_literal_global.62
- __block_literal_global.801
- __block_literal_global.874
- __block_literal_global.877
- __block_literal_global.885
- __block_literal_global.887
- _objc_msgSend$ineligibleDetailsWithReason:preferredLanguage:criteria:
- _objc_msgSend$ineligibleDetailsWithReason:preferredLanguage:overrideDisplayString:criteria:
- _objc_msgSend$initWithIneligibleDetailsWithReason:overrideDisplayString:preferredLanguage:criteria:
- _objc_msgSend$isCurrentValueFromCameraCapture
- _objc_msgSend$keyReferenceIdentifier
- _objc_msgSend$rootAttestation
- _objc_msgSend$securityAccessControl
- _objc_msgSend$setCurrentValueFromCameraCapture:
- _symbolic So7NSErrorC
- block_copy_helper.61
- block_copy_helper.69
- block_descriptor.63
- block_descriptor.71
- block_destroy_helper.62
- block_destroy_helper.70
CStrings:
+ "/AppleInternal/Library/BuildRoots/23fe9468-3783-11ef-b7e3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/AppleSSE/AppleSSElib/AppleSSElib.m"
+ "Failed to decode merchant coupon code changed"
+ "Failed to decode merchant payment method selected"
+ "Failed to decode merchant shipping contact selected"
+ "Failed to decode merchant shipping method selected"
+ "PASS_ACTION_UNAVAILABLE_GENERIC_TITLE"
+ "PKPaymentOffersUseEphemeralSessionKey"
+ "PKRemoteNetworkPaymentLoadingViewDelay"
+ "PKRemoteNetworkPaymentLoadingViewHold"
+ "PassKitCore.ReceiverDataError"
+ "Sharing.SFAirDropReceive.Failure"
+ "Sharing.SFAirDropSend.Failure"
+ "_failureDiagnostic"
+ "acceptAs"
+ "acceptOrDecline"
+ "addressSource"
+ "amountSelection"
+ "autofill"
+ "autofillEdited"
+ "codeOnError"
+ "failureDiagnostic"
+ "fieldSources"
+ "isRemoteRequest"
+ "isWebPaymentRequest: '%!@(MISSING)'; "
+ "p2pSendState"
+ "payLaterInitialOfferDetails"
+ "paymentAuth"
+ "paymentBalanceUpdated"
+ "ready"
+ "readyToAccept"
+ "receiver"
+ "scannedCode"
+ "sending"
+ "type: %!@(MISSING), operation: %!@(MISSING), event: %!@(MISSING), wallet dataclass changed: %!@(MISSING), ubiquity dataclass changed: %!@(MISSING), managed state changed: %!@(MISSING), order changed: %!@(MISSING), storefront changed: %!@(MISSING)"
+ "useAutomaticColors"
+ "useDeviceValidation"
+ "validationRegex"
- "/AppleInternal/Library/BuildRoots/d3a62b52-2ef5-11ef-9ecd-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleSSE/AppleSSElib/AppleSSElib.m"
- "Failed to decode coupon code changed"
- "Failed to decode payment method selected"
- "Failed to decode shipping contact selected"
- "Failed to decode shipping method selected"
- "PASS_ACTION_UNAVAILABLE_GENERIC_TITLE_FORMAT"
- "PKDisableIdentitySecurityCheckInHeader"
- "PKSendLegacyProvisioningParameters"
- "appletPresentmentACL"
- "partnerDataEncryptionAuthorization"
- "qrCode"
- "thirdPartyProgenitorKeyAttestation"
- "type: %!@(MISSING), operation: %!@(MISSING), wallet dataclass changed: %!@(MISSING), ubiquity dataclass changed: %!@(MISSING), managed state changed: %!@(MISSING), order changed: %!@(MISSING), storefront changed: %!@(MISSING)"
- "x-apple-identity-device-security-check-disable"

```
