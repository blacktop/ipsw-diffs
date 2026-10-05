## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1696.2.5.0.0
-  __TEXT.__text: 0x8e93e8
-  __TEXT.__objc_methlist: 0x72968
-  __TEXT.__const: 0x2d6a0
-  __TEXT.__swift5_typeref: 0x8c68
-  __TEXT.__cstring: 0x73c5e
-  __TEXT.__constg_swiftt: 0x7554
-  __TEXT.__swift5_reflstr: 0x661d
-  __TEXT.__swift5_fieldmd: 0x7da0
+1696.2.8.1.0
+  __TEXT.__text: 0x8f23bc
+  __TEXT.__objc_methlist: 0x72a98
+  __TEXT.__const: 0x2d760
+  __TEXT.__swift5_typeref: 0x8da0
+  __TEXT.__cstring: 0x741ce
+  __TEXT.__constg_swiftt: 0x7588
+  __TEXT.__swift5_reflstr: 0x664d
+  __TEXT.__swift5_fieldmd: 0x7de0
   __TEXT.__swift5_builtin: 0x53c
   __TEXT.__swift5_assocty: 0xe28
-  __TEXT.__swift5_proto: 0x13e8
-  __TEXT.__swift5_types: 0x7f4
-  __TEXT.__swift5_capture: 0x512c
-  __TEXT.__oslogstring: 0x3c80d
-  __TEXT.__swift_as_entry: 0x1a0
-  __TEXT.__swift_as_ret: 0x1c4
-  __TEXT.__swift_as_cont: 0x3b8
+  __TEXT.__swift5_proto: 0x13f0
+  __TEXT.__swift5_types: 0x7f8
+  __TEXT.__swift5_capture: 0x543c
+  __TEXT.__oslogstring: 0x3cc09
+  __TEXT.__swift_as_entry: 0x198
+  __TEXT.__swift_as_ret: 0x1bc
+  __TEXT.__swift_as_cont: 0x3ac
   __TEXT.__swift5_mpenum: 0x140
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift5_types2: 0x4
   __TEXT.__gcc_except_tab: 0x6ae8
   __TEXT.__ustring: 0x1e6c
-  __TEXT.__unwind_info: 0x27120
-  __TEXT.__eh_frame: 0x8988
+  __TEXT.__unwind_info: 0x27268
+  __TEXT.__eh_frame: 0x8978
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x23760
+  __DATA_CONST.__const: 0x238c8
   __DATA_CONST.__objc_classlist: 0x3e48
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25328
+  __DATA_CONST.__objc_selrefs: 0x25420
   __DATA_CONST.__objc_protorefs: 0x260
   __DATA_CONST.__objc_superrefs: 0x3158
   __DATA_CONST.__objc_arraydata: 0x2810
-  __DATA_CONST.__got: 0x53b0
-  __AUTH_CONST.__const: 0x269a8
-  __AUTH_CONST.__cfstring: 0x7a140
-  __AUTH_CONST.__objc_const: 0xd0590
+  __DATA_CONST.__got: 0x53a0
+  __AUTH_CONST.__const: 0x27208
+  __AUTH_CONST.__cfstring: 0x7a620
+  __AUTH_CONST.__objc_const: 0xd07b0
   __AUTH_CONST.__objc_arrayobj: 0xd20
   __AUTH_CONST.__objc_intobj: 0x11d0
   __AUTH_CONST.__objc_dictobj: 0x15b8
   __AUTH_CONST.__objc_doubleobj: 0x2b0
-  __AUTH_CONST.__auth_got: 0x2fd8
+  __AUTH_CONST.__auth_got: 0x3010
   __AUTH.__objc_data: 0x20b58
-  __AUTH.__data: 0x5828
+  __AUTH.__data: 0x59a8
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x7328
-  __DATA.__data: 0xa2a0
+  __DATA.__objc_ivar: 0x734c
+  __DATA.__data: 0xa2b0
   __DATA.__common: 0xc49
-  __DATA_DIRTY.__objc_ivar: 0x1f4c
+  __DATA_DIRTY.__objc_ivar: 0x1f50
   __DATA_DIRTY.__objc_data: 0x7940
   __DATA_DIRTY.__data: 0x188
-  __DATA_DIRTY.__bss: 0x1328
+  __DATA_DIRTY.__bss: 0x1358
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 55789
-  Symbols:   79126
-  CStrings:  21767
+  Functions: 55942
+  Symbols:   79224
+  CStrings:  21824
 
Symbols:
+ +[PKAnalyticsReporter(Attribution) isNewToWalletUser]
+ +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:newToWalletUser:newToProductUser:]
+ +[PKCoreSpotlightUtilities _addNormalizedPhoneNumberForPhoneNumber:toAttributeSet:]
+ +[PKCoreSpotlightUtilities _normalizedPhoneNumberDigitsFromPhoneNumber:]
+ -[PKExistingCardAuthorizationRequestMessage contentType]
+ -[PKExistingCardAuthorizationRequestMessage initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:selectedCredentialCount:contentType:analyticsArchivedParentToken:]
+ -[PKPassCredentialShare isLocal]
+ -[PKPassShare isSameUnderlyingShareAs:ignoringRecipientHandle:]
+ -[PKPaymentButtonAnalytics _lock_payloadForEvent:error:]
+ -[PKPaymentButtonAnalytics _reportPayload:]
+ -[PKPaymentButtonAnalytics didRenderContent]
+ -[PKPaymentButtonAnalytics reportContentRendered]
+ -[PKPaymentPassAction isTopUpAction]
+ -[PKPaymentRemoteCredential supportsExistingCardAuthorization]
+ -[PKPaymentSetupFieldPickerItem localizedDescriptionStyle]
+ -[PKPaymentSetupFieldPickerItem localizedDescription]
+ -[PKPaymentSetupFieldPickerItem submissionConfirmationActionStyle]
+ -[PKPaymentSetupFieldPickerItem submissionConfirmationActionTitle]
+ -[PKPeerPaymentRequiredFieldsPage headerImageStyle]
+ -[PKPeerPaymentRequiredFieldsPage setHeaderImageStyle:]
+ -[PKProvisioningAnalyticsSession reportNCCCheck]
+ -[PKProvisioningAnalyticsSessionCampaignAttributionSubjectHandle reportNCCCheckWithState:]
+ -[PKProvisioningAnalyticsState campaignAttributionNewToProductUser]
+ -[PKProvisioningAnalyticsState campaignAttributionNewToWalletUser]
+ -[PKProvisioningAnalyticsState campaignAttributionReferralSource]
+ -[PKProvisioningAnalyticsState setCampaignAttributionNewToProductUser:]
+ -[PKProvisioningAnalyticsState setCampaignAttributionNewToWalletUser:]
+ -[PKSharedPassSharesController _activeUserShare]
+ -[PKSharedPassSharesController sharesCreatedByCurrentUser]
+ -[PKTransitBalanceModel displayableCommutePlanMatchingPlan:]
+ GCC_except_table104
+ _OBJC_IVAR_$_PKPaymentButtonAnalytics._didRenderContent
+ _OBJC_IVAR_$_PKPaymentButtonAnalytics._lock
+ _OBJC_IVAR_$_PKPaymentSetupFieldPickerItem._localizedDescription
+ _OBJC_IVAR_$_PKPaymentSetupFieldPickerItem._localizedDescriptionStyle
+ _OBJC_IVAR_$_PKPaymentSetupFieldPickerItem._submissionConfirmationActionStyle
+ _OBJC_IVAR_$_PKPaymentSetupFieldPickerItem._submissionConfirmationActionTitle
+ _OBJC_IVAR_$_PKPeerPaymentRequiredFieldsPage._headerImageStyle
+ _OBJC_IVAR_$_PKProvisioningAnalyticsSession._didReportNCCCheck
+ _OBJC_IVAR_$_PKProvisioningAnalyticsState._campaignAttributionNewToProductUser
+ _OBJC_IVAR_$_PKProvisioningAnalyticsState._campaignAttributionNewToWalletUser
+ _PKAggDKeyApplePayButtonErrorTypeCardArtNotDisplayed
+ _PKAggDKeyApplePayButtonErrorTypeNoEligibleCard
+ _PKAggDKeyApplePayButtonErrorTypePassImageConversionFailed
+ _PKAggDKeyApplePayButtonErrorTypePassLibraryUnavailable
+ _PKAggDKeyApplePayButtonErrorTypePaymentPassLookupFailed
+ _PKAggDKeyApplePayButtonEventTypeContentRendered
+ _PKAnalyticsReportErrorTypeHandoffPaymentFailure
+ _PKAnalyticsReportErrorTypeHandoffUserDismissed
+ _PKAnalyticsReportNewToCreditUserKey
+ _PKAnalyticsReportNewToDebitUserKey
+ _PKAnalyticsReportNewToTransitUserKey
+ _PKAnalyticsReportNewToWalletUserKey
+ _PKAnalyticsReportPeerPaymentKeyboardTapBillSplitButtonTag
+ _PKAnalyticsReportPeerPaymentKeyboardTapButtonTag
+ _PKAnalyticsReportPeerPaymentKeyboardTapOpenButtonTag
+ _PKCoreSpotlightCustomKeyNormalizedPhoneNumbers
+ _PKCurrentSecureElementPasses
+ _PKExistingCardAuthorizationContentTypeKey
+ _PKHomeAppSharingHost
+ _PKHomeAppURLScheme
+ _PKHomeAppUserLockSettingsHost
+ _PKISO23220_1_PhotoID_ResidentAddressLatinCharacter
+ _PKISO23220_1_PhotoID_ResidentState
+ _PKISO23220_1_PhotoID_ResidentStateLatinCharacter
+ _PKISO23220_1_PhotoID_ResidentStateUnicode
+ _PKISO23220_1_PhotoID_ResidentStreet
+ _PKISO23220_1_PhotoID_ResidentStreetLatinCharacter
+ _PKISO23220_1_PhotoID_ResidentStreetUnicode
+ _PKPassCredentialShareTargetDeviceIsLocal
+ _PKPaymentFieldPickerItemLocalizedDescriptionStyleKey
+ _PKPaymentFieldPickerItemSubmissionConfirmationActionStyleKey
+ _PKPaymentFieldPickerItemSubmissionConfirmationActionTitleKey
+ _PKPaymentSetupHeaderImageStyleFromString
+ _PKPeerPaymentReceiptMockingEnabled
+ _PKPendingCampaignAttributionCampaignIdentifierKey
+ _PKPendingCampaignAttributionForPassUniqueIdentifier
+ _PKPendingCampaignAttributionNewToProductUserKey
+ _PKPendingCampaignAttributionNewToWalletUserKey
+ _PKPendingCampaignAttributionProductTypeKey
+ _PKPendingCampaignAttributionReferralSourceKey
+ _PKRemovePendingCampaignAttributionForPassUniqueIdentifier
+ _PKSetLocalSecureElementPassesProvider
+ _PKSetPendingCampaignAttributionForPassUniqueIdentifier
+ _PKSharingInvitationFlowIsDeviceTransfer
+ _PKSharingSanitizedRelayURL
+ _PKUserGeneratedPassSupported
+ __DoNotUse_PassDesignerOnly_PKPassSecurePreviewContextCreateMessagesPreviewForUnsignedPass
+ ___188-[PKExistingCardAuthorizationRequestMessage initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:selectedCredentialCount:contentType:analyticsArchivedParentToken:]_block_invoke
+ ___48-[PKSharedPassSharesController _activeUserShare]_block_invoke
+ ___58-[PKSharedPassSharesController sharesCreatedByCurrentUser]_block_invoke
+ ___58-[PKSharedPassSharesController sharesCreatedByCurrentUser]_block_invoke_2
+ ___60-[PKTransitBalanceModel displayableCommutePlanMatchingPlan:]_block_invoke
+ ___60-[PKTransitBalanceModel displayableCommutePlanMatchingPlan:]_block_invoke_2
+ ____PKPaymentButtonAnalyticsDeviceClass_block_invoke
+ ____PKPaymentButtonAnalyticsOSVersion_block_invoke
+ ___block_descriptor_32_e21_B16?0"PKPassShare"8l
+ ___block_descriptor_40_e8_32s_e30_B16?0"PKTransitCommutePlan"8ls32l8
+ ___block_descriptor_40_e8_32s_e37_B32?0"PKTransitCommutePlan"8Q16^B24ls32l8
+ ___swift__destructor.219Tm
+ ___swift_closure_destructor.150Tm
+ ___swift_closure_destructor.159Tm
+ ___swift_closure_destructor.173Tm
+ ___swift_closure_destructor.252Tm
+ ___swift_closure_destructor.34Tm
+ ___swift_closure_destructor.41Tm
+ ___swift_closure_destructor.54Tm
+ ___swift_closure_destructor.68Tm
+ ___swift_closure_destructor.9Tm
+ _associated conformance 11PassKitCore37ProvisioningDeviceTransferContentTypeOSHAASQ
+ _generic environment 11PassKitCore25ProvisioningOperationStepRzl
+ _symbolic SDySSSo19PKPaymentCredentialCGz_Xx
+ _symbolic SS_So19PKPaymentCredentialCt
+ _symbolic Say______pG 11PassKitCore27ProvisioningOperationRunnerP
+ _symbolic SiIegd_
+ _symbolic _____ 11PassKitCore37ProvisioningDeviceTransferContentTypeO
+ _symbolic _____ySDySSSo19PKPaymentCredentialCG_____G s6ResultOsRi_zRi0_zrlE 11PassKitCore27ProvisioningContinuityErrorO
+ _symbolic _____ySDySSSo19PKPaymentCredentialCG_____GIegn_ s6ResultOsRi_zRi0_zrlE 11PassKitCore27ProvisioningContinuityErrorO
+ _symbolic _____ySS_So19PKPaymentCredentialCtG s23_ContiguousArrayStorageC
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic x4step_______p6runnert 11PassKitCore27ProvisioningOperationRunnerP
+ _symbolic y_____ySDySSSo19PKPaymentCredentialCG_____GcSg s6ResultOsRi_zRi0_zrlE 11PassKitCore27ProvisioningContinuityErrorO
- +[PKAnalyticsReporter(Attribution) reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:]
- -[PKExistingCardAuthorizationRequestMessage initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:selectedCredentialCount:analyticsArchivedParentToken:]
- -[PKPaymentButtonAnalytics _recordEvent:]
- -[PKPaymentButtonAnalytics _recordEvent:withError:]
- -[PKStatefulTransferCredential serialNumber]
- -[PKStatefulTransferCredential setSerialNumber:]
- GCC_except_table64
- GCC_except_table71
- _OBJC_IVAR_$_PKStatefulTransferCredential._serialNumber
- _PKAnalyticsReportViewedLineItemKey
- _PKPassSecurePreviewContextCreateMessagesPreviewForUnsignedPass
- ___176-[PKExistingCardAuthorizationRequestMessage initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:selectedCredentialCount:analyticsArchivedParentToken:]_block_invoke
- ___swift__destructor.176Tm
- ___swift_closure_destructor.113Tm
- ___swift_closure_destructor.156Tm
- ___swift_closure_destructor.176Tm
- ___swift_closure_destructor.19Tm
- ___swift_closure_destructor.209Tm
- ___swift_closure_destructor.23Tm
- ___swift_closure_destructor.29Tm
- _symbolic ScTy___________pG 11PassKitCore24UnifiedCardReaderAdapterC13PrepareResultV s5ErrorP
- _symbolic Scgy___________pG 11PassKitCore24UnifiedCardReaderAdapterC13PrepareResultV s5ErrorP
- _symbolic _____Sg 11PassKitCore24UnifiedCardReaderAdapterC13PrepareResultV
- _symbolic _____ySaySo19PKPaymentCredentialCG_____G s6ResultOsRi_zRi0_zrlE 11PassKitCore27ProvisioningContinuityErrorO
- _symbolic y_____ySaySo19PKPaymentCredentialCG_____GcSg s6ResultOsRi_zRi0_zrlE 11PassKitCore27ProvisioningContinuityErrorO
CStrings:
+ "ADT source UI provider: self deallocated in _generateCryptograms"
+ "B16@?0@\"PKTransitCommutePlan\"8"
+ "B32@?0@\"PKTransitCommutePlan\"8Q16^B24"
+ "COULD_NOT_ADD_KEY_TITLE"
+ "PKPendingCampaignAttributionKey"
+ "PROVISIONING_DEVICE_TRANSFER_GENERIC_ERROR_MESSAGE"
+ "Passbook_normalizedPhoneNumbers"
+ "SHAREABLE_CREDENTIAL_ERROR_MISMATCHED_ROLE_MESSAGE"
+ "SHAREABLE_CREDENTIAL_ERROR_MISMATCHED_ROLE_TITLE"
+ "Sharing Capabilities: %{public}@ cannot share, activation state %ld and application state %ld."
+ "[%@] PKPaymentProvisioningController: skipping NCCE for FPAN credential, missing a field required by this card's issuer (expiration required: %d missing: %d, name required: %d missing: %d)"
+ "[%s] Car key destination provider: Missing pass identifiers on credential"
+ "[%s] Dropping credential %s: failed to create PKExistingCardAuthorizationCredential"
+ "[%s] Dropping credential %s: no redemption token in response"
+ "[%s] Dropping credential with no remote credential"
+ "[%s] Failed to deprovision removed pass, result %lu: %@"
+ "[%s] Failed to deprovision rolled back pass, result %lu: %@"
+ "[%s] Failed to deprovision tracked pass during teardown, result %lu: %@"
+ "[%s] ProvisioningOperationComposer: Timed out tearing down %ld step(s); continuing"
+ "[%s] Timed out deprovisioning removed passes"
+ "[%s] Timed out deprovisioning rolled back passes."
+ "appleAccount"
+ "campaignAttributionNewToProductUser"
+ "campaignAttributionNewToWalletUser"
+ "cardReadyToUse"
+ "com.apple.Home-private"
+ "com.apple.wallet.ecom.smartButtons.errorType.CardArtNotDisplayed"
+ "com.apple.wallet.ecom.smartButtons.errorType.NoEligibleCard"
+ "com.apple.wallet.ecom.smartButtons.errorType.PassImageConversionFailed"
+ "com.apple.wallet.ecom.smartButtons.errorType.PassLibraryUnavailable"
+ "com.apple.wallet.ecom.smartButtons.errorType.PaymentPassLookupFailed"
+ "com.apple.wallet.ecom.smartButtons.eventType.applePayButtonContentRendered"
+ "contentType"
+ "contentType: '%ld'; "
+ "destructive"
+ "didRenderContent"
+ "didRenderContent: '%@'; "
+ "headerImageStyle"
+ "highlighted"
+ "keyboardTap"
+ "keyboardTapBillSplit"
+ "keyboardTapOpen"
+ "localizedDescriptionStyle"
+ "nccCheck"
+ "newToCreditUser"
+ "newToDebitUser"
+ "newToProductUser"
+ "newToTransitUser"
+ "newToWalletUser"
+ "paymentFailure"
+ "resident_address_latin1"
+ "resident_state_latin1"
+ "resident_state_unicode"
+ "resident_street_latin1"
+ "resident_street_unicode"
+ "submissionConfirmationActionStyle"
+ "submissionConfirmationActionTitle"
+ "userDismissed"
+ "userLockSettings"
- "ADT source UI provider: self deallocated in _generateCrytogram"
- "viewedLineItem"
```
