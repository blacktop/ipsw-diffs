## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1695.1.4.0.0
-  __TEXT.__text: 0x8e6f6c
-  __TEXT.__objc_methlist: 0x72700
-  __TEXT.__const: 0x2d700
-  __TEXT.__swift5_typeref: 0x8c78
-  __TEXT.__cstring: 0x7334a
+1696.2.5.0.0
+  __TEXT.__text: 0x8e93e0
+  __TEXT.__objc_methlist: 0x72968
+  __TEXT.__const: 0x2d6a0
+  __TEXT.__swift5_typeref: 0x8c68
+  __TEXT.__cstring: 0x73c5e
   __TEXT.__constg_swiftt: 0x7554
-  __TEXT.__swift5_reflstr: 0x662d
+  __TEXT.__swift5_reflstr: 0x661d
   __TEXT.__swift5_fieldmd: 0x7da0
   __TEXT.__swift5_builtin: 0x53c
   __TEXT.__swift5_assocty: 0xe28
   __TEXT.__swift5_proto: 0x13e8
   __TEXT.__swift5_types: 0x7f4
   __TEXT.__swift5_capture: 0x512c
-  __TEXT.__oslogstring: 0x3c1bd
+  __TEXT.__oslogstring: 0x3c80d
   __TEXT.__swift_as_entry: 0x1a0
-  __TEXT.__swift_as_ret: 0x1c8
-  __TEXT.__swift_as_cont: 0x3c0
-  __TEXT.__swift5_protos: 0x68
+  __TEXT.__swift_as_ret: 0x1c4
+  __TEXT.__swift_as_cont: 0x3b8
   __TEXT.__swift5_mpenum: 0x140
+  __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x6ae8
   __TEXT.__ustring: 0x1e6c
-  __TEXT.__unwind_info: 0x27078
-  __TEXT.__eh_frame: 0x8a30
+  __TEXT.__unwind_info: 0x27120
+  __TEXT.__eh_frame: 0x8988
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x23550
-  __DATA_CONST.__objc_classlist: 0x3e40
+  __DATA_CONST.__const: 0x23700
+  __DATA_CONST.__objc_classlist: 0x3e48
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25218
+  __DATA_CONST.__objc_selrefs: 0x25328
   __DATA_CONST.__objc_protorefs: 0x260
-  __DATA_CONST.__objc_superrefs: 0x3150
+  __DATA_CONST.__objc_superrefs: 0x3158
   __DATA_CONST.__objc_arraydata: 0x2810
-  __DATA_CONST.__got: 0x53b8
-  __AUTH_CONST.__const: 0x26968
-  __AUTH_CONST.__cfstring: 0x79a20
-  __AUTH_CONST.__objc_const: 0xd0310
+  __DATA_CONST.__got: 0x53b0
+  __AUTH_CONST.__const: 0x269a8
+  __AUTH_CONST.__cfstring: 0x7a140
+  __AUTH_CONST.__objc_const: 0xd0590
   __AUTH_CONST.__objc_arrayobj: 0xd20
   __AUTH_CONST.__objc_intobj: 0x11d0
   __AUTH_CONST.__objc_dictobj: 0x15b8
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH_CONST.__auth_got: 0x2fe8
-  __AUTH.__objc_data: 0x22598
+  __AUTH_CONST.__auth_got: 0x2fd8
+  __AUTH.__objc_data: 0x225e8
   __AUTH.__data: 0x5818
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x7314
-  __DATA.__data: 0xa290
+  __DATA.__objc_ivar: 0x7328
+  __DATA.__data: 0xa280
   __DATA.__common: 0xc49
-  __DATA_DIRTY.__objc_ivar: 0x1f40
+  __DATA_DIRTY.__objc_ivar: 0x1f4c
   __DATA_DIRTY.__objc_data: 0x5eb0
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x1318
+  __DATA_DIRTY.__bss: 0x1328
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 55741
-  Symbols:   91386
-  CStrings:  21682
+  Functions: 55789
+  Symbols:   91510
+  CStrings:  21767
 
Symbols:
+ +[PKAnalyticsReporter(AppleCash) billSplitContextWithReceiptRequestType:receiptLength:]
+ +[PKAnalyticsReporter(AppleCash) messagesContextWithIsGroup:groupSize:]
+ +[PKAnalyticsReporter(AppleCash) reportAppleCashEvent:withMessagesContext:billSplitContext:]
+ -[PKAddCarKeyPassConfiguration _adoptProvisioningResolvedFieldsFromConfiguration:]
+ -[PKAddCarKeyPassConfiguration _adoptSessionOnlyFieldsFromConfiguration:]
+ -[PKAddCarKeyPassConfiguration reconcileWithPendingConfiguration:]
+ -[PKAppletSubcredentialManagementSession deleteCredential:reason:completionHandler:]
+ -[PKDAManager deleteCredential:reason:completion:]
+ -[PKDAManager deleteCredentials:reason:completion:]
+ -[PKDAManager deleteCredentialsForIdentifiers:reason:completion:]
+ -[PKDAManager deleteCredentialsForReaderIdentifiers:reason:completion:]
+ -[PKGroupsController groupForPassUniqueID:]
+ -[PKGroupsController isFilteringPassUniqueID:]
+ -[PKInAppPaymentService cacheApplePayButtonTapWithIdentifier:tapDate:]
+ -[PKLocation copyWithZone:]
+ -[PKPassLibrary automaticallyPresentedPassForPasses:webDomain:applicationIdentifier:]
+ -[PKPassLibrary deleteKeyMaterialForSubCredentialId:reason:]
+ -[PKPaymentApplication(Transit) transitConfirmationStyle]
+ -[PKPaymentAuthorizationStateMachine _handlePeerPaymentAccountChanged]
+ -[PKPaymentAuthorizationStateMachine _resumePeerPaymentUpdates]
+ -[PKPaymentAuthorizationStateMachine hasPausedPeerPaymentUpdates]
+ -[PKPaymentAuthorizationStateMachine setHasPausedPeerPaymentUpdates:]
+ -[PKPaymentOfferConfirmationRecord didProcessEvent:]
+ -[PKPaymentOfferCriteria setSupportsEcomConfirm:]
+ -[PKPaymentOfferCriteria supportsEcomConfirm]
+ -[PKPaymentOffersController _insertEcomConfirmationRecordForTransaction:passUniqueID:]
+ -[PKPaymentOffersController didSuccessfulPaymentWithTransaction:passUniqueID:]
+ -[PKPaymentRewrapRequestBase paymentTotalSummaryItemType]
+ -[PKPaymentRewrapRequestBase setPaymentTotalSummaryItemType:]
+ -[PKPaymentService revokeCredentialsWithIdentifiers:reason:completion:]
+ -[PKPaymentService revokeCredentialsWithReaderIdentifiers:reason:completion:]
+ -[PKPaymentSheetApplePayButtonTapAttribution initWithButtonIdentifier:bundleID:tapDate:expirationDate:]
+ -[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]
+ -[PKPaymentWebServiceLocalProxyTargetDevice deleteKeyMaterialForSubCredentialId:reason:]
+ -[PKPaymentWebServiceRemoteProxyTargetDevice deleteKeyMaterialForSubCredentialId:reason:]
+ -[PKPaymentWebServiceTargetDevice deleteKeyMaterialForSubCredentialId:reason:]
+ -[PKPaymentWebServiceTargetDevice revokeCredentialsWithReaderIdentifiers:reason:completion:]
+ -[PKPeerPaymentController analyticsBillSplitContext]
+ -[PKPeerPaymentController analyticsMessagesContext]
+ -[PKPeerPaymentController setAnalyticsBillSplitContext:]
+ -[PKPeerPaymentController setAnalyticsMessagesContext:]
+ -[PKPeerPaymentRequest analyticsBillSplitContext]
+ -[PKPeerPaymentRequest setAnalyticsBillSplitContext:]
+ -[PKSearchTransactionResult bankConnectInstitutionID]
+ -[PKSearchTransactionResult bankConnectTransactionUUID]
+ -[PKSearchTransactionResult setBankConnectInstitutionID:]
+ -[PKSearchTransactionResult setBankConnectTransactionUUID:]
+ -[PKSecureElementPass compareProvisioningDatesToPass:newestFirst:]
+ GCC_except_table132
+ GCC_except_table146
+ GCC_except_table152
+ GCC_except_table172
+ GCC_except_table178
+ GCC_except_table186
+ GCC_except_table197
+ GCC_except_table207
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table248
+ GCC_except_table253
+ GCC_except_table266
+ GCC_except_table276
+ GCC_except_table290
+ GCC_except_table292
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table319
+ GCC_except_table321
+ GCC_except_table340
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table367
+ GCC_except_table381
+ GCC_except_table395
+ GCC_except_table435
+ GCC_except_table455
+ GCC_except_table471
+ GCC_except_table482
+ GCC_except_table484
+ GCC_except_table487
+ GCC_except_table53
+ GCC_except_table547
+ GCC_except_table55
+ GCC_except_table555
+ GCC_except_table557
+ GCC_except_table572
+ GCC_except_table575
+ GCC_except_table578
+ GCC_except_table581
+ GCC_except_table599
+ GCC_except_table893
+ GCC_except_table92
+ GCC_except_table98
+ OBJC_IVAR_$_PKPeerPaymentControllerInternalState.analyticsBillSplitContext
+ OBJC_IVAR_$_PKPeerPaymentControllerInternalState.analyticsMessagesContext
+ _OBJC_CLASS_$_PKPaymentSheetApplePayButtonTapAttribution
+ _OBJC_IVAR_$_PKPaymentAuthorizationStateMachine._hasPausedPeerPaymentUpdates
+ _OBJC_IVAR_$_PKPaymentOfferCriteria._supportsEcomConfirm
+ _OBJC_IVAR_$_PKSearchTransactionResult._bankConnectInstitutionID
+ _OBJC_IVAR_$_PKSearchTransactionResult._bankConnectTransactionUUID
+ _OBJC_METACLASS_$_PKPaymentSheetApplePayButtonTapAttribution
+ _PDCredentialRevocationReasonForPassDeletionReason
+ _PKAcceptedNormalizedPaymentNetworkNames
+ _PKAccessibilityIdentifierCapture
+ _PKAccessibilityIdentifierFeeInterestTransactionsTitle
+ _PKAccessibilityIdentifierFrequentMerchantsTitle
+ _PKAccessibilityIdentifierHighAmountTransactionsTitle
+ _PKAccessibilityIdentifierLoading
+ _PKAccessibilityIdentifierMarkComplete
+ _PKAccessibilityIdentifierObserverBubble
+ _PKAccessibilityIdentifierPrice
+ _PKAccessibilityIdentifierQuantity
+ _PKAccessibilityIdentifierReceiptBubble
+ _PKAccessibilityIdentifierReceiptCameraGuidance
+ _PKAccessibilityIdentifierReceiptCapture
+ _PKAccessibilityIdentifierReceiptChargeDiscount
+ _PKAccessibilityIdentifierReceiptChargeEdit
+ _PKAccessibilityIdentifierReceiptChargeFee
+ _PKAccessibilityIdentifierReceiptChargeTax
+ _PKAccessibilityIdentifierReceiptChargesDetail
+ _PKAccessibilityIdentifierReceiptEditSheet
+ _PKAccessibilityIdentifierReceiptEvenSplit
+ _PKAccessibilityIdentifierReceiptLineItem
+ _PKAccessibilityIdentifierReceiptLineItemModifier
+ _PKAccessibilityIdentifierReceiptLineItemShare
+ _PKAccessibilityIdentifierReceiptModePicker
+ _PKAccessibilityIdentifierReceiptOtherCharges
+ _PKAccessibilityIdentifierReceiptRetake
+ _PKAccessibilityIdentifierReceiptSheet
+ _PKAccessibilityIdentifierReceiptSplitQuantity
+ _PKAccessibilityIdentifierReceiptSubtotal
+ _PKAccessibilityIdentifierReceiptTax
+ _PKAccessibilityIdentifierReceiptTaxEdit
+ _PKAccessibilityIdentifierReceiptTip
+ _PKAccessibilityIdentifierReceiptTip15
+ _PKAccessibilityIdentifierReceiptTip18
+ _PKAccessibilityIdentifierReceiptTip20
+ _PKAccessibilityIdentifierReceiptTip25
+ _PKAccessibilityIdentifierReceiptTipCustom
+ _PKAccessibilityIdentifierReceiptTipNone
+ _PKAccessibilityIdentifierReceiptTipOriginal
+ _PKAccessibilityIdentifierReceiptTotal
+ _PKAccessibilityIdentifierRecurringBubble
+ _PKAccessibilityIdentifierTotalReceived
+ _PKAccessibilityIdentifierTotalRequested
+ _PKAccessibilityIdentifierUnknownBubble
+ _PKAccessibilityIdentifierViewInMessages
+ _PKAddAcceptedNormalizedPaymentNetworkNames
+ _PKAnalyticsReportEventTypeAuthenticationPasscodeStarted
+ _PKAnalyticsReportPaymentApplePayButtonUniqueIdentifier
+ _PKCompareDatesPreferringPresent
+ _PKCredentialRevocationReasonCreate
+ _PKCredentialRevocationScenarioAuxiliaryRequirementFailure
+ _PKCredentialRevocationScenarioPassApplicationsRemoved
+ _PKCredentialRevocationScenarioProvisioningFailure
+ _PKCredentialRevocationScenarioProvisioningReplacement
+ _PKCredentialRevocationScenarioServerConsistencyCheck
+ _PKCredentialRevocationScenarioUnspecified
+ _PKISO18013_5_Street
+ _PKISO23220_1_PhotoID_FamilyNameUnicode
+ _PKISO23220_1_PhotoID_GivenNameUnicode
+ _PKISO23220_1_PhotoID_IssuingAuthorityUnicode
+ _PKISO23220_1_PhotoID_ResidentAddressUnicode
+ _PKISO23220_1_PhotoID_ResidentCityUnicode
+ _PKSharingForceTrackKeyNetworkErrorWithoutRequest
+ _PKSharingForceTrackKeyNetworkErrorWithoutRequestKey
+ __OBJC_$_CLASS_METHODS_PKPaymentApplication(PKPaymentAuthorizationDataModel|Protobuf|Transit)
+ __OBJC_$_CLASS_PROP_LIST_PKPaymentSheetApplePayButtonTapAttribution
+ __OBJC_$_INSTANCE_METHODS_PKPaymentApplication(PKPaymentAuthorizationDataModel|Protobuf|Transit)
+ __OBJC_$_INSTANCE_METHODS_PKPaymentSheetApplePayButtonTapAttribution
+ __OBJC_CLASS_PROTOCOLS_$_PKPaymentSheetApplePayButtonTapAttribution
+ __OBJC_CLASS_RO_$_PKPaymentSheetApplePayButtonTapAttribution
+ __OBJC_METACLASS_RO_$_PKPaymentSheetApplePayButtonTapAttribution
+ ___50-[PKDAManager deleteCredential:reason:completion:]_block_invoke
+ ___50-[PKDAManager deleteCredential:reason:completion:]_block_invoke_2
+ ___51-[PKDAManager deleteCredentials:reason:completion:]_block_invoke
+ ___60-[PKPassLibrary deleteKeyMaterialForSubCredentialId:reason:]_block_invoke
+ ___63-[PKPaymentAuthorizationStateMachine _resumePeerPaymentUpdates]_block_invoke
+ ___65-[PKDAManager deleteCredentialsForIdentifiers:reason:completion:]_block_invoke
+ ___65-[PKDAManager deleteCredentialsForIdentifiers:reason:completion:]_block_invoke_2
+ ___65-[PKDAManager deleteCredentialsForIdentifiers:reason:completion:]_block_invoke_3
+ ___70-[PKInAppPaymentService cacheApplePayButtonTapWithIdentifier:tapDate:]_block_invoke
+ ___70-[PKPaymentAuthorizationStateMachine _handlePeerPaymentAccountChanged]_block_invoke
+ ___71-[PKDAManager deleteCredentialsForReaderIdentifiers:reason:completion:]_block_invoke
+ ___71-[PKDAManager deleteCredentialsForReaderIdentifiers:reason:completion:]_block_invoke_2
+ ___71-[PKDAManager deleteCredentialsForReaderIdentifiers:reason:completion:]_block_invoke_3
+ ___71-[PKDAManager deleteCredentialsForReaderIdentifiers:reason:completion:]_block_invoke_4
+ ___71-[PKPaymentService revokeCredentialsWithIdentifiers:reason:completion:]_block_invoke
+ ___77-[PKPaymentService revokeCredentialsWithReaderIdentifiers:reason:completion:]_block_invoke
+ ___78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke
+ ___78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke_2
+ ___78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke_3
+ ___78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke_4
+ ___78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke_5
+ ___89-[PKPaymentWebServiceRemoteProxyTargetDevice deleteKeyMaterialForSubCredentialId:reason:]_block_invoke
+ ___PKCanonicalCredentialTypeForPaymentNetworkName_block_invoke
+ ___PKPaymentNetworkPrioritiesByNormalizedName_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56s64s_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8s64l8
+ _marketString
+ _objc_msgSend$_adoptProvisioningResolvedFieldsFromConfiguration:
+ _objc_msgSend$_adoptSessionOnlyFieldsFromConfiguration:
+ _objc_msgSend$_handlePeerPaymentAccountChanged
+ _objc_msgSend$_insertEcomConfirmationRecordForTransaction:passUniqueID:
+ _objc_msgSend$_resumePeerPaymentUpdates
+ _objc_msgSend$analyticsBillSplitContext
+ _objc_msgSend$automaticallyPresentedPassForPasses:webDomain:applicationIdentifier:
+ _objc_msgSend$billSplitContextWithSplitType:receiptLength:
+ _objc_msgSend$bucketValueForGroupSize:
+ _objc_msgSend$cacheApplePayButtonTapWithIdentifier:tapDate:
+ _objc_msgSend$deleteCredential:reason:completion:
+ _objc_msgSend$deleteCredential:reason:completionHandler:
+ _objc_msgSend$deleteCredentials:reason:completion:
+ _objc_msgSend$deleteCredentialsForIdentifiers:reason:completion:
+ _objc_msgSend$deleteCredentialsForReaderIdentifiers:reason:completion:
+ _objc_msgSend$deleteKey:reason:completionHandler:
+ _objc_msgSend$deleteKeyMaterialForSubCredentialId:reason:
+ _objc_msgSend$didProcessEvent:
+ _objc_msgSend$didSuccessfulPaymentWithTransaction:passUniqueID:
+ _objc_msgSend$registerDeviceThroughTargetDeviceWithReason:completion:
+ _objc_msgSend$remoteDeviceModel
+ _objc_msgSend$revokeCredentialsWithIdentifiers:reason:completion:
+ _objc_msgSend$revokeCredentialsWithReaderIdentifiers:reason:completion:
+ _objc_msgSend$setAnalyticsBillSplitContext:
+ _objc_msgSend$setPaymentTotalSummaryItemType:
+ _objc_msgSend$supportsAutomatedPairing
+ _objc_msgSend$supportsEcomConfirm
- -[PKPassLibrary automaticallyPresentedPassForPasses:applicationIdentifier:]
- -[PKPaymentAuthorizationStateMachine _handlePeerPaymentAccountChangedNotification:]
- -[PKPaymentAuthorizationStateMachine hasPendingPeerPaymentUpdate]
- -[PKPaymentAuthorizationStateMachine setHasPendingPeerPaymentUpdate:]
- -[PKPaymentOffersController didSuccessfulPayment]
- -[PKSecureElementPass isTruthOnServer]
- GCC_except_table104
- GCC_except_table114
- GCC_except_table117
- GCC_except_table119
- GCC_except_table133
- GCC_except_table134
- GCC_except_table138
- GCC_except_table145
- GCC_except_table147
- GCC_except_table154
- GCC_except_table156
- GCC_except_table161
- GCC_except_table171
- GCC_except_table180
- GCC_except_table181
- GCC_except_table183
- GCC_except_table191
- GCC_except_table192
- GCC_except_table206
- GCC_except_table215
- GCC_except_table223
- GCC_except_table245
- GCC_except_table261
- GCC_except_table262
- GCC_except_table268
- GCC_except_table275
- GCC_except_table279
- GCC_except_table293
- GCC_except_table317
- GCC_except_table318
- GCC_except_table320
- GCC_except_table343
- GCC_except_table352
- GCC_except_table354
- GCC_except_table359
- GCC_except_table370
- GCC_except_table375
- GCC_except_table383
- GCC_except_table429
- GCC_except_table449
- GCC_except_table465
- GCC_except_table473
- GCC_except_table481
- GCC_except_table483
- GCC_except_table486
- GCC_except_table546
- GCC_except_table554
- GCC_except_table556
- GCC_except_table571
- GCC_except_table574
- GCC_except_table577
- GCC_except_table580
- GCC_except_table598
- GCC_except_table891
- _OBJC_IVAR_$_PKPaymentAuthorizationStateMachine._hasPendingPeerPaymentUpdate
- _PKAccessibilityIdentifierReceiptBubblePayButton
- _PKAccessibilityIdentifierReceiptChargeEditInput
- _PKAccessibilityIdentifierReceiptCustomTaxInput
- _PKAccessibilityIdentifierReceiptCustomTipInput
- _PKAccessibilityIdentifierReceiptEditItemName
- _PKAccessibilityIdentifierReceiptEditPrice
- _PKAccessibilityIdentifierReceiptEditQuantityStepper
- _PKAccessibilityIdentifierReceiptEqualSplit
- _PKAccessibilityIdentifierReceiptLineItemSplit
- _PKAccessibilityIdentifierReceiptOtherChargesRow
- _PKAccessibilityIdentifierReceiptSplitPeopleStepper
- _PKAccessibilityIdentifierReceiptSplitQuantityStepper
- _PKAccessibilityIdentifierReceiptTaxRow
- _PKAccessibilityIdentifierReceiptTipPicker
- _PKAccessibilityIdentifierReceiptTipRow
- __OBJC_$_CLASS_METHODS_PKPaymentApplication(PKPaymentAuthorizationDataModel|Protobuf)
- __OBJC_$_INSTANCE_METHODS_PKPaymentApplication(PKPaymentAuthorizationDataModel|Protobuf)
- ___43-[PKDAManager deleteCredential:completion:]_block_invoke
- ___43-[PKDAManager deleteCredential:completion:]_block_invoke_2
- ___44-[PKDAManager deleteCredentials:completion:]_block_invoke
- ___51-[PKPaymentProvisioningController _registerDevice:]_block_invoke_4
- ___51-[PKPaymentProvisioningController _registerDevice:]_block_invoke_5
- ___51-[PKPaymentProvisioningController _registerDevice:]_block_invoke_6
- ___53-[PKPassLibrary deleteKeyMaterialForSubCredentialId:]_block_invoke
- ___58-[PKDAManager deleteCredentialsForIdentifiers:completion:]_block_invoke
- ___58-[PKDAManager deleteCredentialsForIdentifiers:completion:]_block_invoke_2
- ___58-[PKDAManager deleteCredentialsForIdentifiers:completion:]_block_invoke_3
- ___64-[PKDAManager deleteCredentialsForReaderIdentifiers:completion:]_block_invoke
- ___64-[PKDAManager deleteCredentialsForReaderIdentifiers:completion:]_block_invoke_2
- ___64-[PKDAManager deleteCredentialsForReaderIdentifiers:completion:]_block_invoke_3
- ___64-[PKDAManager deleteCredentialsForReaderIdentifiers:completion:]_block_invoke_4
- ___64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke
- ___70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke
- ___83-[PKPaymentAuthorizationStateMachine _handlePeerPaymentAccountChangedNotification:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSArray"8ls32l8s40l8s48l8s56l8
- _objc_msgSend$automaticallyPresentedPassForPasses:applicationIdentifier:
- _objc_msgSend$deleteCredential:completionHandler:
- _objc_msgSend$deleteCredentialsForIdentifiers:completion:
- _objc_msgSend$deleteKey:completionHandler:
- _objc_msgSend$didSuccessfulPayment
- _objc_msgSend$revokeCredentialsWithIdentifiers:completion:
- _objc_msgSend$revokeCredentialsWithReaderIdentifiers:completion:
- _symbolic _____Sg 18AppIntentsServices0bC0O14InterfaceIdiomO
CStrings:
+ "%@/%@ [%@]"
+ "-[PKAppletSubcredentialManagementSession deleteCredential:completionHandler:]"
+ "-[PKAppletSubcredentialManagementSession deleteCredential:reason:completionHandler:]"
+ "-[PKDAManager deleteCredential:completion:]"
+ "-[PKDAManager deleteCredentials:completion:]"
+ "-[PKDAManager deleteCredentialsForIdentifiers:completion:]"
+ "-[PKDAManager deleteCredentialsForReaderIdentifiers:completion:]"
+ "-[PKPassLibrary deleteKeyMaterialForSubCredentialId:]"
+ "-[PKPaymentProvisioningController _handleProvisioningError:forRequest:pass:]"
+ "-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]"
+ "-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]"
+ "-[PKPaymentWebServiceLocalProxyTargetDevice deleteKeyMaterialForSubCredentialId:]"
+ "-[PKPaymentWebServiceRemoteProxyTargetDevice deleteKeyMaterialForSubCredentialId:]_block_invoke"
+ "-[PKPaymentWebServiceTargetDevice deleteKeyMaterialForSubCredentialId:]"
+ "-[PKPaymentWebServiceTargetDevice revokeCredentialsWithReaderIdentifiers:completion:]"
+ "-[PKProvisioningUtility updateProvisioningRequestForEnableRequirements:externalizedAuth:sid:completion:]_block_invoke"
+ "AuxiliaryRequirementFailure"
+ "Creating ecom confirmation record and inserting into database %@"
+ "ERROR: X-Redirect-Encrypted-Data did not decode to a JSON object. Following redirect without reconfiguration."
+ "Not handling peer payment account update while paused on updates"
+ "PDCredentialRevocationReasonForPassDeletionReason"
+ "PKPaymentNotifyIssuerAppletDirtyRequest: endpoint component was nil, exiting early. deviceIdentifier is %s, passSerialNumber is %s, dpanIdentifier is %s"
+ "PKPaymentOffersController not creating ecom confirmation record: criteria %@ doesn't support the ecom confirm API"
+ "PKPaymentOffersController not creating ecom confirmation record: no pass unique ID for the paying pass"
+ "PKPaymentOffersController not creating ecom confirmation record: selected offer belongs to pass %@ but pass %@ paid"
+ "PKPaymentOffersController not creating ecom confirmation record: selected offer type is unknown"
+ "PKPaymentOffersController not creating ecom confirmation record: transaction has no payment hash"
+ "PKPaymentWebService: No device identifier present - exiting early (deleteForRequest:)"
+ "PKPaymentWebService: No device identifier present - exiting early (deprovisionForRequest:)"
+ "PKPaymentWebService: No device identifier present - exiting early (notifyIssuerAppletStateDirtyWithRequest:)"
+ "PKPaymentWebService: No device identifier present - exiting early (vehicleManufacturerWithRequest:)"
+ "PKPaymentWebService: Target device offers no device registration method"
+ "PKPeerPaymentController %p: No archived Apple Cash session token for payment authorization. The authorization session will not be related to a parent session."
+ "PKSharingForceTrackKeyNetworkErrorWithoutRequestKey"
+ "PassApplicationsRemoved"
+ "PassDeletionReasonCloudStore"
+ "PassDeletionReasonInvalid"
+ "PassDeletionReasonPaymentRemoveAll"
+ "PassDeletionReasonPaymentRemoveMultiple"
+ "PassDeletionReasonPaymentRemoveSingle"
+ "PassDeletionReasonRemoveAll"
+ "PassDeletionReasonRemoveMultiple"
+ "PassDeletionReasonRemoveSingle"
+ "PassDeletionReasonSignout"
+ "PassDeletionReasonUbiquity"
+ "Peer payment account changed while updates were paused. Handling update now"
+ "ProvisioningFailure"
+ "ProvisioningReplacement"
+ "Remote instrument '%@' checking app network '%@' against region networks: %@"
+ "ServerConsistencyCheck"
+ "Unspecified"
+ "Warning: %@ requested without a valid hostApplicationIdentifier or web domain. This is likely not what you want!"
+ "[%s] Simulating track key network failure without sending request on the wire"
+ "acceptInvite(completion:)"
+ "acceptedPaymentApplicationsForPass: regionNetworks: %@, acceptedRegionNetworkNames: %@"
+ "analyticsBillSplitContext"
+ "analyticsBillSplitContext: '%@'; "
+ "analyticsMessagesContext: '%@'; "
+ "applePayButtonTap"
+ "applePayButtonUniqueIdentifier"
+ "authenticationPasscodeStarted"
+ "bankConnectInstitutionID"
+ "bankConnectInstitutionID: '%@'; "
+ "bankConnectTransactionUUID"
+ "bankConnectTransactionUUID: '%@'; "
+ "capture"
+ "fee-interest-transactions-title"
+ "frequent-merchants-title"
+ "high-amount-transactions-title"
+ "issuerRegions filter: Checking app network '%@' against global: %@"
+ "issuerRegions filter: Checking app network '%@' against region: %@"
+ "issuerRegions filter: Region networks found: %@, acceptedRegionNetworkNames: %@"
+ "mark-complete"
+ "observer-bubble"
+ "paymentTotalSummaryItemType"
+ "receipt-bubble"
+ "receipt-camera-guidance"
+ "receipt-capture"
+ "receipt-charge-discount"
+ "receipt-charge-edit"
+ "receipt-charge-fee"
+ "receipt-charge-tax"
+ "receipt-charges-detail"
+ "receipt-edit-sheet"
+ "receipt-even-split"
+ "receipt-line-item"
+ "receipt-line-item-modifier"
+ "receipt-line-item-share"
+ "receipt-mode-picker"
+ "receipt-other-charges"
+ "receipt-retake"
+ "receipt-sheet"
+ "receipt-split-quantity"
+ "receipt-subtotal"
+ "receipt-tax"
+ "receipt-tax-edit"
+ "receipt-tip"
+ "receipt-tip-15"
+ "receipt-tip-18"
+ "receipt-tip-20"
+ "receipt-tip-25"
+ "receipt-tip-custom"
+ "receipt-tip-none"
+ "receipt-tip-original"
+ "receipt-total"
+ "recurring-bubble"
+ "resident_street"
+ "supportsEcomConfirm"
+ "supportsEcomConfirm: '%@'; "
+ "total-received"
+ "total-requested"
+ "unknown-bubble"
+ "view-in-messages"
- "Attachment collection failed: "
- "Failed to launch TapToRadar: "
- "IdentityStreamlinedPresentment"
- "PKPaymentCredential"
- "Remote instrument '%@' checking app network '%@' (normalized: '%@') against region networks: %@"
- "RemoteDeviceSelections"
- "TapToRadar: URL generation failed: %@"
- "TapToRadar: attachment collection failed: %@"
- "TapToRadar: collected %ld attachment(s)"
- "acceptedPaymentApplicationsForPass: regionNetworks: %@, regionNetworkIDs: %@"
- "issuerRegions filter: Checking app network '%@' (normalized: '%@') against global: %@"
- "issuerRegions filter: Checking app network '%@' (normalized: '%@') against region: %@"
- "issuerRegions filter: Region networks found: %@, normalizedRegionNetworks: %@"
- "receipt-bubble-pay-button"
- "receipt-charge-edit-input"
- "receipt-custom-tax-input"
- "receipt-custom-tip-input"
- "receipt-edit-item-name"
- "receipt-edit-price"
- "receipt-edit-quantity-stepper"
- "receipt-equal-split"
- "receipt-line-item-split"
- "receipt-other-charges-row"
- "receipt-split-people-stepper"
- "receipt-split-quantity-stepper"
- "receipt-tax-row"
- "receipt-tip-picker"
- "receipt-tip-row"
```
