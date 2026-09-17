## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/Versions/A/PassKitCore`

```diff

-1695.3.1.0.0
-  __TEXT.__text: 0x85ebac
-  __TEXT.__objc_methlist: 0x6fee0
-  __TEXT.__const: 0x18fb0
-  __TEXT.__swift5_typeref: 0x7a86
-  __TEXT.__cstring: 0x6ec50
+1696.2.5.0.0
+  __TEXT.__text: 0x861df4
+  __TEXT.__objc_methlist: 0x70148
+  __TEXT.__const: 0x18f60
+  __TEXT.__swift5_typeref: 0x7a7e
+  __TEXT.__cstring: 0x6f54f
   __TEXT.__constg_swiftt: 0x6db4
   __TEXT.__swift5_reflstr: 0x5cfd
   __TEXT.__swift5_fieldmd: 0x7370

   __TEXT.__swift5_proto: 0x1164
   __TEXT.__swift5_types: 0x750
   __TEXT.__swift5_capture: 0x4714
-  __TEXT.__oslogstring: 0x36730
+  __TEXT.__oslogstring: 0x36e10
   __TEXT.__swift_as_entry: 0x160
   __TEXT.__swift_as_ret: 0x174
   __TEXT.__swift_as_cont: 0x2f4
-  __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x138
+  __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x6638
   __TEXT.__ustring: 0x1e6c
-  __TEXT.__unwind_info: 0x24800
-  __TEXT.__eh_frame: 0x7400
+  __TEXT.__unwind_info: 0x248b8
+  __TEXT.__eh_frame: 0x73e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12160
-  __DATA_CONST.__objc_classlist: 0x3d20
+  __DATA_CONST.__const: 0x12310
+  __DATA_CONST.__objc_classlist: 0x3d28
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x518
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23a38
+  __DATA_CONST.__objc_selrefs: 0x23b40
   __DATA_CONST.__objc_protorefs: 0x210
-  __DATA_CONST.__objc_superrefs: 0x3028
+  __DATA_CONST.__objc_superrefs: 0x3030
   __DATA_CONST.__objc_arraydata: 0x2850
-  __DATA_CONST.__got: 0x4928
-  __AUTH_CONST.__const: 0x2ec90
-  __AUTH_CONST.__cfstring: 0x777c0
-  __AUTH_CONST.__objc_const: 0xcbec8
+  __DATA_CONST.__got: 0x4920
+  __AUTH_CONST.__const: 0x2ece0
+  __AUTH_CONST.__cfstring: 0x77ee0
+  __AUTH_CONST.__objc_const: 0xcc140
   __AUTH_CONST.__objc_arrayobj: 0xd50
   __AUTH_CONST.__objc_intobj: 0x10e0
   __AUTH_CONST.__objc_dictobj: 0x1590
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH_CONST.__auth_got: 0x28b0
-  __AUTH.__objc_data: 0x20158
-  __AUTH.__data: 0x52c8
+  __AUTH_CONST.__auth_got: 0x28a0
+  __AUTH.__objc_data: 0x201a8
+  __AUTH.__data: 0x52b8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x7044
-  __DATA.__data: 0x8710
+  __DATA.__objc_ivar: 0x7058
+  __DATA.__data: 0x8720
   __DATA.__common: 0x1d9
-  __DATA_DIRTY.__objc_ivar: 0x1f10
+  __DATA_DIRTY.__objc_ivar: 0x1f1c
   __DATA_DIRTY.__objc_data: 0x76c0
   __DATA_DIRTY.__data: 0x88
-  __DATA_DIRTY.__bss: 0x10b0
+  __DATA_DIRTY.__bss: 0x10c0
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 53006
-  Symbols:   88478
-  CStrings:  20777
+  Functions: 53056
+  Symbols:   88613
+  CStrings:  20866
 
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
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table111
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table132
+ GCC_except_table135
+ GCC_except_table142
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table166
+ GCC_except_table168
+ GCC_except_table176
+ GCC_except_table184
+ GCC_except_table187
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table204
+ GCC_except_table220
+ GCC_except_table230
+ GCC_except_table235
+ GCC_except_table242
+ GCC_except_table249
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table267
+ GCC_except_table285
+ GCC_except_table292
+ GCC_except_table309
+ GCC_except_table311
+ GCC_except_table334
+ GCC_except_table338
+ GCC_except_table358
+ GCC_except_table364
+ GCC_except_table366
+ GCC_except_table382
+ GCC_except_table396
+ GCC_except_table436
+ GCC_except_table456
+ GCC_except_table472
+ GCC_except_table477
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table550
+ GCC_except_table558
+ GCC_except_table560
+ GCC_except_table575
+ GCC_except_table578
+ GCC_except_table581
+ GCC_except_table584
+ GCC_except_table602
+ GCC_except_table74
+ GCC_except_table891
+ GCC_except_table91
+ OBJC_IVAR_$_PKPaymentAuthorizationStateMachine._hasPausedPeerPaymentUpdates
+ OBJC_IVAR_$_PKPaymentOfferCriteria._supportsEcomConfirm
+ OBJC_IVAR_$_PKPeerPaymentControllerInternalState.analyticsBillSplitContext
+ OBJC_IVAR_$_PKPeerPaymentControllerInternalState.analyticsMessagesContext
+ OBJC_IVAR_$_PKSearchTransactionResult._bankConnectInstitutionID
+ OBJC_IVAR_$_PKSearchTransactionResult._bankConnectTransactionUUID
+ _OBJC_CLASS_$_PKPaymentSheetApplePayButtonTapAttribution
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
+ __65-[PKDAManager deleteCredentialsForIdentifiers:reason:completion:]_block_invoke
+ __71-[PKDAManager deleteCredentialsForReaderIdentifiers:reason:completion:]_block_invoke
+ __71-[PKPaymentService revokeCredentialsWithIdentifiers:reason:completion:]_block_invoke
+ __77-[PKPaymentService revokeCredentialsWithReaderIdentifiers:reason:completion:]_block_invoke
+ __78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke
+ __78-[PKPaymentWebService registerDeviceThroughTargetDeviceWithReason:completion:]_block_invoke_2
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
+ ___89-[PKPaymentWebServiceRemoteProxyTargetDevice deleteKeyMaterialForSubCredentialId:reason:]_block_invoke
+ ___PKCanonicalCredentialTypeForPaymentNetworkName_block_invoke
+ ___PKPaymentNetworkPrioritiesByNormalizedName_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56s_e61_v32?0"PKAsyncOperationState"8"NSNull"16?<v?"NSNull"B>24l
+ ___block_descriptor_72_e8_32s40s48s56s64s_e17_v16?0"NSArray"8l
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
+ _objc_msgSend$deleteKeyMaterialForSubCredentialId:reason:
+ _objc_msgSend$didProcessEvent:
+ _objc_msgSend$didSuccessfulPaymentWithTransaction:passUniqueID:
+ _objc_msgSend$isAutomatedPairing
+ _objc_msgSend$needsConsent
+ _objc_msgSend$registerDeviceThroughTargetDeviceWithReason:completion:
+ _objc_msgSend$remoteDeviceModel
+ _objc_msgSend$revokeCredentialsWithIdentifiers:reason:completion:
+ _objc_msgSend$revokeCredentialsWithReaderIdentifiers:reason:completion:
+ _objc_msgSend$setAnalyticsBillSplitContext:
+ _objc_msgSend$setExternalReferenceGUID:
+ _objc_msgSend$setPaymentTotalSummaryItemType:
+ _objc_msgSend$supportsAutomatedPairing
+ _objc_msgSend$supportsEcomConfirm
- -[PKPassLibrary automaticallyPresentedPassForPasses:applicationIdentifier:]
- -[PKPaymentAuthorizationStateMachine _handlePeerPaymentAccountChangedNotification:]
- -[PKPaymentAuthorizationStateMachine hasPendingPeerPaymentUpdate]
- -[PKPaymentAuthorizationStateMachine setHasPendingPeerPaymentUpdate:]
- -[PKPaymentOffersController didSuccessfulPayment]
- -[PKSecureElementPass isTruthOnServer]
- GCC_except_table108
- GCC_except_table112
- GCC_except_table115
- GCC_except_table128
- GCC_except_table131
- GCC_except_table133
- GCC_except_table136
- GCC_except_table138
- GCC_except_table140
- GCC_except_table145
- GCC_except_table147
- GCC_except_table149
- GCC_except_table150
- GCC_except_table154
- GCC_except_table162
- GCC_except_table178
- GCC_except_table179
- GCC_except_table181
- GCC_except_table189
- GCC_except_table191
- GCC_except_table199
- GCC_except_table213
- GCC_except_table222
- GCC_except_table234
- GCC_except_table236
- GCC_except_table243
- GCC_except_table245
- GCC_except_table247
- GCC_except_table259
- GCC_except_table260
- GCC_except_table265
- GCC_except_table268
- GCC_except_table270
- GCC_except_table272
- GCC_except_table288
- GCC_except_table312
- GCC_except_table314
- GCC_except_table333
- GCC_except_table340
- GCC_except_table352
- GCC_except_table354
- GCC_except_table367
- GCC_except_table376
- GCC_except_table384
- GCC_except_table430
- GCC_except_table450
- GCC_except_table466
- GCC_except_table476
- GCC_except_table484
- GCC_except_table486
- GCC_except_table489
- GCC_except_table549
- GCC_except_table557
- GCC_except_table559
- GCC_except_table574
- GCC_except_table577
- GCC_except_table580
- GCC_except_table583
- GCC_except_table601
- GCC_except_table889
- OBJC_IVAR_$_PKPaymentAuthorizationStateMachine._hasPendingPeerPaymentUpdate
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
- __51-[PKPaymentProvisioningController _registerDevice:]_block_invoke_2
- __58-[PKDAManager deleteCredentialsForIdentifiers:completion:]_block_invoke
- __64-[PKDAManager deleteCredentialsForReaderIdentifiers:completion:]_block_invoke
- __64-[PKPaymentService revokeCredentialsWithIdentifiers:completion:]_block_invoke
- __70-[PKPaymentService revokeCredentialsWithReaderIdentifiers:completion:]_block_invoke
- __OBJC_$_CLASS_METHODS_PKPaymentApplication(PKPaymentAuthorizationDataModel|Protobuf)
- __OBJC_$_INSTANCE_METHODS_PKPaymentApplication(PKPaymentAuthorizationDataModel|Protobuf)
- ___43-[PKDAManager deleteCredential:completion:]_block_invoke
- ___43-[PKDAManager deleteCredential:completion:]_block_invoke_2
- ___44-[PKDAManager deleteCredentials:completion:]_block_invoke
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
- ___block_descriptor_64_e8_32s40s48s56s_e17_v16?0"NSArray"8l
- _objc_msgSend$automaticallyPresentedPassForPasses:applicationIdentifier:
- _objc_msgSend$deleteCredential:completionHandler:
- _objc_msgSend$deleteCredentialsForIdentifiers:completion:
- _objc_msgSend$didSuccessfulPayment
- _objc_msgSend$revokeCredentialsWithIdentifiers:completion:
- _objc_msgSend$revokeCredentialsWithReaderIdentifiers:completion:
- _symbolic _____Sg 18AppIntentsServices0bC0O14InterfaceIdiomO
CStrings:
+ "%@/%@ [%@]"
+ "-[PKAppletSubcredentialManagementSession deleteCredential:completionHandler:]"
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
- "IdentityStreamlinedPresentment"
- "PKPaymentCredential"
- "Remote instrument '%@' checking app network '%@' (normalized: '%@') against region networks: %@"
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
